"""Conservative `/v1/chat/completions` compatible adapter."""
from __future__ import annotations

import json
import urllib.error
import urllib.request
from collections.abc import Iterable
from typing import Any

from .generic import (
    AdapterRequestError,
    capability,
    compose_instructions,
    endpoint_type,
    normalized_error,
)


def _v1_url(endpoint: str, resource: str) -> str:
    base = endpoint.rstrip("/")
    suffix = resource.lstrip("/")
    return f"{base}/{suffix}" if base.endswith("/v1") else f"{base}/v1/{suffix}"


def normalize_discovery(
    *,
    endpoint: str,
    model: str,
    payload: dict | None,
    declared_capabilities: dict[str, bool | str | None] | None = None,
) -> dict:
    """Normalize `/models`; all non-identity capabilities remain caller-declared."""
    models = payload.get("data") if isinstance(payload, dict) else None
    identifiers = {
        item["id"] for item in models or []
        if isinstance(item, dict) and isinstance(item.get("id"), str)
    }
    if isinstance(models, list):
        availability = "supported" if model in identifiers else "unsupported"
    else:
        availability = "unknown"
    declarations = declared_capabilities or {}

    def declared(name: str) -> dict:
        value = declarations.get(name)
        if isinstance(value, bool):
            return capability("supported" if value else "unsupported", "explicit caller declaration")
        if isinstance(value, str) and value in {"supported", "unsupported", "unknown"}:
            return capability(str(value), "explicit caller declaration")
        return capability("unknown", "/models does not report this capability")

    return {
        "adapter": "openai-compatible",
        "endpoint": endpoint,
        "endpoint_type": endpoint_type(endpoint),
        "server_version": None,
        "model_id": model,
        "model_available": capability(availability, "/models exact identifier"),
        "instruction_roles": {
            "system": declared("system_role"),
            "developer": declared("developer_role"),
        },
        "features": {
            "chat": declared("chat"),
            "streaming": declared("streaming"),
            "tools": declared("tools"),
            "structured_output": declared("structured_output"),
        },
        "context": {
            "model_max_context_tokens": None,
            "configured_context_tokens": (
                declarations["context_window_tokens"]
                if isinstance(declarations.get("context_window_tokens"), int)
                and not isinstance(declarations.get("context_window_tokens"), bool)
                and declarations["context_window_tokens"] > 0
                else None
            ),
            "effective_context_tokens": None,
        },
        "evidence": {"models": payload, "declarations": declarations},
    }


def discover_models(
    endpoint: str,
    model: str,
    *,
    api_key: str | None = None,
    timeout: float = 10,
    declared_capabilities: dict[str, bool | str | None] | None = None,
    opener=urllib.request.urlopen,
) -> dict:
    """Perform explicit identity-only discovery against `/models`."""
    headers = {"Accept": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    request = urllib.request.Request(_v1_url(endpoint, "models"), headers=headers, method="GET")
    try:
        with opener(request, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        raise AdapterRequestError(normalized_error(
            provider="openai-compatible", status=error.code, message=error.reason,
        )) from error
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        raise AdapterRequestError(normalized_error(
            provider="openai-compatible", message=str(getattr(error, "reason", error)),
        )) from error
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise AdapterRequestError({
            **normalized_error(provider="openai-compatible", message="malformed JSON response"),
            "kind": "malformed_response",
        }) from error
    if not isinstance(payload, dict):
        raise AdapterRequestError({
            **normalized_error(provider="openai-compatible", message="expected a JSON object"),
            "kind": "malformed_response",
        })
    return normalize_discovery(
        endpoint=endpoint, model=model, payload=payload,
        declared_capabilities=declared_capabilities,
    )


def build_chat_completions_request(
    *,
    model: str,
    user_content: str,
    plan: dict,
    base_instructions: str | None = None,
    instruction_role: str = "system",
    generation_parameters: dict[str, Any] | None = None,
) -> dict:
    if instruction_role not in {"system", "developer"}:
        raise ValueError("instruction_role must be explicitly system or developer")
    composed = compose_instructions(base_instructions, plan, mode="append-managed-runtime-block")
    messages = []
    if composed["combined_instructions"]:
        messages.append({"role": instruction_role, "content": composed["combined_instructions"]})
    messages.append({"role": "user", "content": user_content})
    request = {"model": model, "messages": messages}
    for key, value in (generation_parameters or {}).items():
        if key in {"model", "messages"}:
            raise ValueError(f"generation parameter cannot replace {key}")
        request[key] = value
    return request


def chat_completions(
    endpoint: str,
    request_body: dict,
    *,
    api_key: str | None = None,
    timeout: float = 60,
    opener=urllib.request.urlopen,
) -> dict:
    url = _v1_url(endpoint, "chat/completions")
    headers = {"Content-Type": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    request = urllib.request.Request(
        url,
        data=json.dumps(request_body).encode("utf-8"),
        headers=headers,
        method="POST",
    )
    try:
        with opener(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        raise AdapterRequestError(normalized_error(
            provider="openai-compatible", status=error.code, message=error.reason,
        )) from error
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        raise AdapterRequestError(normalized_error(
            provider="openai-compatible", message=str(getattr(error, "reason", error)),
        )) from error
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise AdapterRequestError({
            **normalized_error(provider="openai-compatible", message="malformed JSON response"),
            "kind": "malformed_response",
        }) from error


def _content_text(content: Any) -> str:
    if isinstance(content, str):
        return content
    if not isinstance(content, list):
        return ""
    return "".join(
        block.get("text", "") for block in content
        if isinstance(block, dict) and block.get("type") in {None, "text", "output_text"}
        and isinstance(block.get("text", ""), str)
    )


def normalize_response(payload: dict) -> dict:
    """Normalize one OpenAI-compatible non-streaming chat response."""
    if not isinstance(payload, dict):
        raise TypeError("chat completion response must be a JSON object")
    choices = payload.get("choices") if isinstance(payload.get("choices"), list) else []
    first = choices[0] if choices and isinstance(choices[0], dict) else {}
    message = first.get("message") if isinstance(first.get("message"), dict) else {}
    usage = payload.get("usage") if isinstance(payload.get("usage"), dict) else {}
    provider_error = payload.get("error")
    finish_reason = first.get("finish_reason")
    error = None
    if provider_error:
        error = normalized_error(provider="openai-compatible", message=str(provider_error))
        error["kind"] = "request_failed"
    elif not choices or not isinstance(first.get("message"), dict):
        error = normalized_error(provider="openai-compatible", message="response has no choice message")
        error["kind"] = "malformed_response"
    return {
        "provider": "openai-compatible",
        "response_text": _content_text(message.get("content")),
        "raw_response": payload,
        "model_id": payload.get("model"),
        "finish_reason": finish_reason,
        "usage": {
            "input_tokens": usage.get("prompt_tokens"),
            "output_tokens": usage.get("completion_tokens"),
            "total_tokens": usage.get("total_tokens"),
        },
        "timing": {},
        "tool_calls": message.get("tool_calls", []) if isinstance(message.get("tool_calls", []), list) else [],
        "partial": error is not None,
        "truncated": finish_reason == "length",
        "error": error,
    }


def normalize_stream(chunks: Iterable[bytes | str]) -> dict:
    """Parse OpenAI-compatible SSE while preserving extensions and partial output."""
    buffer = ""
    records: list[dict] = []
    text_parts: list[str] = []
    tool_calls: list[dict] = []
    model_id = None
    finish_reason = None
    usage: dict = {}
    saw_done = False
    failure = None

    def consume(line: str) -> None:
        nonlocal model_id, finish_reason, usage, saw_done, failure
        stripped = line.strip()
        if not stripped or stripped.startswith(":") or stripped.startswith("event:"):
            return
        if not stripped.startswith("data:"):
            return
        data = stripped[5:].strip()
        if data == "[DONE]":
            saw_done = True
            return
        try:
            record = json.loads(data)
        except json.JSONDecodeError:
            failure = "stream contains malformed SSE JSON"
            return
        if not isinstance(record, dict):
            failure = "stream event is not a JSON object"
            return
        records.append(record)
        if record.get("error"):
            failure = str(record["error"])
            return
        if record.get("model"):
            model_id = record["model"]
        if isinstance(record.get("usage"), dict):
            usage = record["usage"]
        choices = record.get("choices") if isinstance(record.get("choices"), list) else []
        for choice in choices:
            if not isinstance(choice, dict):
                continue
            delta = choice.get("delta") if isinstance(choice.get("delta"), dict) else {}
            if isinstance(delta.get("content"), str):
                text_parts.append(delta["content"])
            if isinstance(delta.get("tool_calls"), list):
                tool_calls.extend(delta["tool_calls"])
            if choice.get("finish_reason") is not None:
                finish_reason = choice["finish_reason"]

    for chunk in chunks:
        try:
            buffer += chunk.decode("utf-8") if isinstance(chunk, bytes) else str(chunk)
        except UnicodeDecodeError:
            failure = "stream contains invalid UTF-8"
            break
        while "\n" in buffer:
            line, buffer = buffer.split("\n", 1)
            consume(line.rstrip("\r"))
            if failure:
                break
        if failure:
            break
    if not failure and buffer.strip():
        consume(buffer.rstrip("\r"))
    error = None
    if failure:
        error = normalized_error(
            provider="openai-compatible", message=failure,
            response_started=bool(records),
        )
        if "malformed" in failure or "invalid UTF-8" in failure or "not a JSON object" in failure:
            error["kind"] = "malformed_response"
    return {
        "provider": "openai-compatible",
        "response_text": "".join(text_parts),
        "raw_response": records,
        "model_id": model_id,
        "finish_reason": finish_reason,
        "usage": {
            "input_tokens": usage.get("prompt_tokens"),
            "output_tokens": usage.get("completion_tokens"),
            "total_tokens": usage.get("total_tokens"),
        },
        "timing": {},
        "tool_calls": tool_calls,
        "partial": not saw_done or error is not None,
        "truncated": finish_reason == "length",
        "error": error,
    }
