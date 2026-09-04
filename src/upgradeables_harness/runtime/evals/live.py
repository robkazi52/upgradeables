"""Explicit live evaluation adapters built on the runtime HTTP adapters."""
from __future__ import annotations

import math
import re
import urllib.request
from time import perf_counter
from typing import Callable
from urllib.parse import urlsplit

from ..adapters.generic import AdapterRequestError, endpoint_type
from ..adapters.ollama import (
    build_ollama_request,
    chat as ollama_chat,
    normalize_response as normalize_ollama_response,
)
from ..adapters.openai_compatible import (
    build_chat_completions_request,
    chat_completions,
    normalize_response as normalize_openai_response,
)
from ..manifest import redact_secrets

LIVE_ADAPTERS = {"ollama", "openai-compatible"}
ENVIRONMENT_NAME = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def validate_endpoint_origin(endpoint: str, adapter: str) -> str:
    """Validate an explicit adapter origin without resolving or contacting it."""
    if adapter not in LIVE_ADAPTERS:
        raise ValueError(f"unsupported live evaluation adapter: {adapter}")
    if (
        not isinstance(endpoint, str)
        or not endpoint.strip()
        or endpoint != endpoint.strip()
        or any(character.isspace() or ord(character) < 32 or ord(character) == 127 for character in endpoint)
        or "\\" in endpoint
    ):
        raise ValueError("endpoint must be a non-empty origin without whitespace or control characters")
    try:
        parsed = urlsplit(endpoint)
        port = parsed.port
    except ValueError as error:
        raise ValueError("endpoint must be a valid HTTP(S) origin") from error
    if parsed.scheme not in {"http", "https"} or not parsed.hostname:
        raise ValueError("endpoint must use an explicit http or https origin")
    if parsed.username is not None or parsed.password is not None:
        raise ValueError("endpoint must not contain credentials")
    if parsed.query or parsed.fragment:
        raise ValueError("endpoint origin must not contain a query or fragment")
    allowed_paths = {"", "/", "/api"} if adapter == "ollama" else {"", "/", "/v1"}
    if parsed.path.rstrip("/") not in {value.rstrip("/") for value in allowed_paths}:
        suffix = "/api" if adapter == "ollama" else "/v1"
        raise ValueError(f"endpoint must be an origin with at most the {suffix} suffix")
    if endpoint_type(endpoint) == "remote" and parsed.scheme != "https":
        raise ValueError("remote evaluation endpoints must use https")
    hostname = parsed.hostname
    if ":" in hostname and not hostname.startswith("["):
        hostname = f"[{hostname}]"
    default_port = (parsed.scheme == "http" and port == 80) or (parsed.scheme == "https" and port == 443)
    authority = hostname if port is None or default_port else f"{hostname}:{port}"
    path = parsed.path.rstrip("/")
    return f"{parsed.scheme}://{authority}{path}"


def validate_api_key_environment(name: str | None) -> str | None:
    if name is None:
        return None
    if not isinstance(name, str) or not ENVIRONMENT_NAME.fullmatch(name):
        raise ValueError("--api-key-env must be an environment variable name")
    return name


def _redact_text(value: str, secrets: tuple[str, ...] = ()) -> str:
    output = redact_secrets(value)
    for secret in secrets:
        if secret:
            output = output.replace(secret, "[REDACTED]")
    return output


def _redact_value(value, secrets: tuple[str, ...] = ()):
    if isinstance(value, str):
        return _redact_text(value, secrets)
    if isinstance(value, dict):
        return {
            _redact_text(key, secrets) if isinstance(key, str) else key:
            _redact_value(item, secrets)
            for key, item in value.items()
        }
    if isinstance(value, (list, tuple)):
        return [_redact_value(item, secrets) for item in value]
    return value


def _condition_plan(request: dict) -> dict:
    plan = request.get("runtime_plan")
    if isinstance(plan, dict):
        return plan
    return {
        "instruction_capsule": request.get("instructions", ""),
        "state_contract": [],
        "validators": [],
        "orchestration": [],
        "tool_requirements": [],
        "output_contract": [],
        "warnings": [],
    }


def create_live_adapter(
    adapter: str,
    *,
    model: str,
    endpoint: str,
    api_key: str | None = None,
    timeout: float = 60,
    opener=urllib.request.urlopen,
) -> Callable[[dict, dict, dict], dict]:
    """Create one no-retry callable for the evaluation runner."""
    if adapter not in LIVE_ADAPTERS:
        raise ValueError(f"unsupported live evaluation adapter: {adapter}")
    if not isinstance(model, str) or not model.strip() or model != model.strip():
        raise ValueError("live evaluation requires an exact non-empty model identifier")
    endpoint = validate_endpoint_origin(endpoint, adapter)
    if isinstance(timeout, bool) or not isinstance(timeout, (int, float)) or not math.isfinite(timeout) or timeout <= 0:
        raise ValueError("timeout must be a positive finite number")
    if api_key is not None and (not isinstance(api_key, str) or not api_key):
        raise ValueError("API key must be a non-empty string when supplied")
    if adapter != "openai-compatible" and api_key is not None:
        raise ValueError("API keys are supported only by the openai-compatible adapter")
    secrets = (api_key,) if api_key else ()

    def execute(request: dict, _task: dict, manifest: dict) -> dict:
        plan = _condition_plan(request)
        generation_parameters = dict(manifest.get("generation_parameters", {}))
        generation_parameters.setdefault("temperature", manifest["temperature"])
        generation_parameters.pop("stream", None)
        if adapter == "ollama":
            provider_request = build_ollama_request(
                model=model,
                user_content=request["task"],
                plan=plan,
                options=generation_parameters,
                stream=False,
            )
        else:
            generation_parameters["stream"] = False
            provider_request = build_chat_completions_request(
                model=model,
                user_content=request["task"],
                plan=plan,
                instruction_role="system",
                generation_parameters=generation_parameters,
            )
        started = perf_counter()
        try:
            if adapter == "ollama":
                payload = ollama_chat(endpoint, provider_request, timeout=timeout, opener=opener)
                normalized = normalize_ollama_response(payload)
            else:
                payload = chat_completions(
                    endpoint, provider_request, api_key=api_key,
                    timeout=timeout, opener=opener,
                )
                normalized = normalize_openai_response(payload)
        except AdapterRequestError as error:
            payload = {"adapter_error": error.error}
            normalized = {
                "response_text": "",
                "usage": {"input_tokens": None, "output_tokens": None, "total_tokens": None},
                "error": error.error,
                "partial": False,
                "truncated": False,
                "finish_reason": None,
            }
        except Exception as error:
            unexpected = {
                "kind": "unexpected_adapter_error",
                "provider": adapter,
                "status": None,
                "message": _redact_text(str(error), secrets),
                "response_started": False,
            }
            payload = {"adapter_error": unexpected}
            normalized = {
                "response_text": "",
                "usage": {"input_tokens": None, "output_tokens": None, "total_tokens": None},
                "error": unexpected,
                "partial": False,
                "truncated": False,
                "finish_reason": None,
            }
        latency_ms = (perf_counter() - started) * 1000
        return {
            "response_text": _redact_text(normalized.get("response_text", ""), secrets),
            "provider_request": _redact_value(provider_request, secrets),
            "raw_response": _redact_value(payload, secrets),
            "usage": _redact_value(normalized.get("usage", {}), secrets),
            "latency_ms": latency_ms,
            "model_id": _redact_value(normalized.get("model_id"), secrets),
            "provider_timing": _redact_value(normalized.get("timing", {}), secrets),
            "finish_reason": normalized.get("finish_reason"),
            "partial": bool(normalized.get("partial")),
            "truncated": bool(normalized.get("truncated")),
            "error": _redact_value(normalized.get("error"), secrets),
        }

    return execute
