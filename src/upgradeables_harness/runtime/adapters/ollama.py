"""Ollama native `/api/chat` request composition."""
from __future__ import annotations

import json
import re
import urllib.error
import urllib.request
from collections.abc import Iterable
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .generic import (
    AdapterRequestError,
    capability,
    compose_instructions,
    endpoint_type,
    normalized_error,
)


def _api_url(endpoint: str, resource: str) -> str:
    base = endpoint.rstrip("/")
    suffix = resource.lstrip("/")
    return f"{base}/{suffix}" if base.endswith("/api") else f"{base}/api/{suffix}"


def _model_names(tags: dict | None) -> set[str]:
    if not isinstance(tags, dict) or not isinstance(tags.get("models"), list):
        return set()
    return {
        str(value)
        for item in tags["models"] if isinstance(item, dict)
        for value in (item.get("name"), item.get("model")) if value
    }


def _context_values(model: str, show: dict | None, running: dict | None) -> dict:
    maximum = None
    configured = None
    effective = None
    if isinstance(show, dict):
        model_info = show.get("model_info", {})
        if isinstance(model_info, dict):
            candidates = [
                value for key, value in model_info.items()
                if key.endswith(".context_length") and isinstance(value, int)
            ]
            maximum = max(candidates) if candidates else None
        parameters = show.get("parameters")
        if isinstance(parameters, str):
            match = re.search(r"(?m)^\s*num_ctx\s+(\d+)\s*$", parameters)
            configured = int(match.group(1)) if match else None
        elif isinstance(parameters, dict) and isinstance(parameters.get("num_ctx"), int):
            configured = parameters["num_ctx"]
    if isinstance(running, dict) and isinstance(running.get("models"), list):
        for item in running["models"]:
            if not isinstance(item, dict):
                continue
            if model in {item.get("name"), item.get("model")}:
                value = item.get("context_length")
                effective = value if isinstance(value, int) else None
                break
    return {
        "model_max_context_tokens": maximum,
        "configured_context_tokens": configured,
        "effective_context_tokens": effective,
    }


def normalize_discovery(
    *,
    endpoint: str,
    model: str,
    version: dict | None = None,
    tags: dict | None = None,
    show: dict | None = None,
    running: dict | None = None,
) -> dict:
    """Normalize explicit Ollama discovery responses without inferring from names."""
    names = _model_names(tags)
    if isinstance(tags, dict) and isinstance(tags.get("models"), list):
        model_status = "supported" if model in names else "unsupported"
    else:
        model_status = "unknown"
    declared = set(show.get("capabilities", [])) if isinstance(show, dict) and isinstance(show.get("capabilities"), list) else None

    def declared_capability(name: str) -> dict:
        if declared is None:
            return capability("unknown", "/api/show did not declare capabilities")
        return capability(
            "supported" if name in declared else "unsupported",
            f"/api/show capabilities {'contains' if name in declared else 'omits'} {name}",
        )

    return {
        "adapter": "ollama",
        "endpoint": endpoint,
        "endpoint_type": endpoint_type(endpoint),
        "server_version": version.get("version") if isinstance(version, dict) else None,
        "model_id": model,
        "model_available": capability(model_status, "/api/tags exact model identifier"),
        "instruction_roles": {
            "system": capability("supported", "native /api/chat message role"),
            "developer": capability("unsupported", "native /api/chat uses system role"),
        },
        "features": {
            "chat": capability("supported", "native /api/chat endpoint"),
            "streaming": capability("supported", "native /api/chat NDJSON protocol"),
            "tools": declared_capability("tools"),
            "vision": declared_capability("vision"),
            "thinking": declared_capability("thinking"),
            "structured_output": capability("unknown", "endpoint feature is not a per-model declaration"),
        },
        "context": _context_values(model, show, running),
        "evidence": {
            "version": version,
            "tags": tags,
            "show": show,
            "running": running,
        },
    }


def _read_json(
    endpoint: str,
    resource: str,
    *,
    method: str = "GET",
    body: dict | None = None,
    timeout: float = 10,
    opener=urllib.request.urlopen,
) -> dict:
    request = urllib.request.Request(
        _api_url(endpoint, resource),
        data=None if body is None else json.dumps(body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method=method,
    )
    try:
        with opener(request, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        normalized = normalized_error(
            provider="ollama", status=error.code, message=error.reason,
        )
        error.close()
        raise AdapterRequestError(normalized) from error
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        raise AdapterRequestError(normalized_error(
            provider="ollama", message=str(getattr(error, "reason", error)),
        )) from error
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise AdapterRequestError({
            **normalized_error(provider="ollama", message="malformed JSON response"),
            "kind": "malformed_response",
        }) from error
    if not isinstance(payload, dict):
        raise AdapterRequestError({
            **normalized_error(provider="ollama", message="expected a JSON object"),
            "kind": "malformed_response",
        })
    return payload


def discover(
    endpoint: str,
    model: str,
    *,
    timeout: float = 10,
    opener=urllib.request.urlopen,
) -> dict:
    """Perform explicit read-only discovery; never pulls or loads a model."""
    version = _read_json(endpoint, "version", timeout=timeout, opener=opener)
    tags = _read_json(endpoint, "tags", timeout=timeout, opener=opener)
    running = _read_json(endpoint, "ps", timeout=timeout, opener=opener)
    show = None
    if model in _model_names(tags):
        show = _read_json(
            endpoint, "show", method="POST", body={"model": model},
            timeout=timeout, opener=opener,
        )
    return normalize_discovery(
        endpoint=endpoint, model=model, version=version, tags=tags,
        show=show, running=running,
    )


def build_ollama_request(
    *,
    model: str,
    user_content: str,
    plan: dict,
    base_instructions: str | None = None,
    options: dict[str, Any] | None = None,
    stream: bool = False,
) -> dict:
    composed = compose_instructions(base_instructions, plan, mode="append-managed-runtime-block")
    messages = []
    if composed["combined_instructions"]:
        messages.append({"role": "system", "content": composed["combined_instructions"]})
    messages.append({"role": "user", "content": user_content})
    request = {"model": model, "messages": messages, "stream": bool(stream)}
    if options:
        request["options"] = dict(options)
    return request


def chat(
    endpoint: str,
    request_body: dict,
    *,
    timeout: float = 60,
    opener=urllib.request.urlopen,
) -> dict:
    """Execute an explicit Ollama request; never pulls or mutates a model."""
    url = _api_url(endpoint, "chat")
    request = urllib.request.Request(
        url,
        data=json.dumps(request_body).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with opener(request, timeout=timeout) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        normalized = normalized_error(
            provider="ollama", status=error.code, message=error.reason,
        )
        error.close()
        raise AdapterRequestError(normalized) from error
    except (urllib.error.URLError, TimeoutError, OSError) as error:
        raise AdapterRequestError(normalized_error(
            provider="ollama", message=str(getattr(error, "reason", error)),
        )) from error
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise AdapterRequestError({
            **normalized_error(provider="ollama", message="malformed JSON response"),
            "kind": "malformed_response",
        }) from error


def normalize_response(payload: dict) -> dict:
    """Normalize one non-streaming Ollama chat response."""
    if not isinstance(payload, dict):
        raise TypeError("Ollama response must be a JSON object")
    message = payload.get("message") if isinstance(payload.get("message"), dict) else {}
    provider_error = payload.get("error")
    malformed = None
    if not provider_error and not isinstance(payload.get("message"), dict):
        malformed = "response has no message object"
    elif not provider_error and not isinstance(message.get("content", ""), str):
        malformed = "response message content is not text"
    error = None
    if provider_error:
        error = normalized_error(provider="ollama", message=str(provider_error))
        error["kind"] = "request_failed"
    elif malformed:
        error = normalized_error(provider="ollama", message=malformed)
        error["kind"] = "malformed_response"
    return {
        "provider": "ollama",
        "response_text": message.get("content", "") if isinstance(message.get("content", ""), str) else "",
        "raw_response": payload,
        "model_id": payload.get("model"),
        "finish_reason": payload.get("done_reason"),
        "usage": {
            "input_tokens": payload.get("prompt_eval_count"),
            "output_tokens": payload.get("eval_count"),
            "total_tokens": (
                payload["prompt_eval_count"] + payload["eval_count"]
                if isinstance(payload.get("prompt_eval_count"), int) and isinstance(payload.get("eval_count"), int)
                else None
            ),
        },
        "timing": {
            key: payload.get(key) for key in (
                "total_duration", "load_duration", "prompt_eval_duration", "eval_duration",
            )
        },
        "tool_calls": message.get("tool_calls", []) if isinstance(message.get("tool_calls", []), list) else [],
        "partial": payload.get("done") is not True or error is not None,
        "truncated": payload.get("done_reason") == "length",
        "error": error,
    }


def normalize_stream(chunks: Iterable[bytes | str]) -> dict:
    """Parse Ollama NDJSON conservatively and preserve partial public output."""
    buffer = ""
    records: list[dict] = []
    text_parts: list[str] = []
    tool_calls: list[dict] = []
    terminal = None
    stream_error = None
    malformed = None
    for chunk in chunks:
        try:
            buffer += chunk.decode("utf-8") if isinstance(chunk, bytes) else str(chunk)
        except UnicodeDecodeError:
            malformed = "stream contains invalid UTF-8"
            break
        while "\n" in buffer:
            line, buffer = buffer.split("\n", 1)
            if not line.strip():
                continue
            try:
                record = json.loads(line)
            except json.JSONDecodeError:
                malformed = "stream contains malformed NDJSON"
                break
            if not isinstance(record, dict):
                malformed = "stream record is not a JSON object"
                break
            records.append(record)
            if record.get("error"):
                stream_error = str(record["error"])
                break
            message = record.get("message") if isinstance(record.get("message"), dict) else {}
            if isinstance(message.get("content"), str):
                text_parts.append(message["content"])
            if isinstance(message.get("tool_calls"), list):
                tool_calls.extend(message["tool_calls"])
            if record.get("done") is True:
                terminal = record
        if malformed or stream_error:
            break
    if not malformed and not stream_error and buffer.strip():
        try:
            record = json.loads(buffer)
        except json.JSONDecodeError:
            malformed = "stream ended with incomplete NDJSON"
        else:
            if not isinstance(record, dict):
                malformed = "stream record is not a JSON object"
            else:
                records.append(record)
                if record.get("error"):
                    stream_error = str(record["error"])
                else:
                    message = record.get("message") if isinstance(record.get("message"), dict) else {}
                    if isinstance(message.get("content"), str):
                        text_parts.append(message["content"])
                    if isinstance(message.get("tool_calls"), list):
                        tool_calls.extend(message["tool_calls"])
                    if record.get("done") is True:
                        terminal = record
    source = terminal or (records[-1] if records else {})
    message = malformed or stream_error
    return {
        "provider": "ollama",
        "response_text": "".join(text_parts),
        "raw_response": records,
        "model_id": source.get("model"),
        "finish_reason": source.get("done_reason"),
        "usage": {
            "input_tokens": source.get("prompt_eval_count"),
            "output_tokens": source.get("eval_count"),
            "total_tokens": (
                source["prompt_eval_count"] + source["eval_count"]
                if isinstance(source.get("prompt_eval_count"), int) and isinstance(source.get("eval_count"), int)
                else None
            ),
        },
        "timing": {
            key: source.get(key) for key in (
                "total_duration", "load_duration", "prompt_eval_duration", "eval_duration",
            )
        },
        "tool_calls": tool_calls,
        "partial": terminal is None or message is not None,
        "truncated": source.get("done_reason") == "length",
        "error": (
            {**normalized_error(provider="ollama", message=message, response_started=bool(records)),
             "kind": "malformed_response" if malformed else "stream_interrupted"}
            if message else None
        ),
    }


def run_ollama(
    *,
    model: str,
    task: str,
    endpoint: str = "http://127.0.0.1:11434",
    project: str | Path | dict | None = None,
    model_profile: str = "medium",
    max_directive_tokens: int = 500,
    base_instructions: str | None = None,
    options: dict[str, Any] | None = None,
    timeout: float = 60,
    output_root: str | Path = ".upgradeables/runs",
    dry_run: bool = False,
    use_project_profile: bool = True,
    opener=urllib.request.urlopen,
) -> dict:
    """Compile and optionally execute one explicit, non-streaming Ollama run."""
    if not isinstance(model, str) or not model.strip():
        raise ValueError("model must be a non-empty exact Ollama model identifier")
    if not isinstance(task, str) or not task.strip():
        raise ValueError("task must be non-empty")
    if timeout <= 0:
        raise ValueError("timeout must be positive")
    if options is not None and not isinstance(options, dict):
        raise TypeError("options must be a JSON object")

    # Imported lazily so adapter request-building remains independent of resolver setup.
    from .. import compile_task
    from ..compiler import canonical_hash
    from ..manifest import build_manifest, write_run_artifacts
    from ..models import HostCapabilities

    plan = compile_task(
        task,
        project=project,
        model_profile=model_profile,
        max_directive_tokens=max_directive_tokens,
        host=HostCapabilities(
            instruction_channel="system",
            tools=(),
            state_support="none",
            parallelism=False,
        ),
        use_project_profile=use_project_profile,
    )
    request_body = build_ollama_request(
        model=model,
        user_content=task,
        plan=plan,
        base_instructions=base_instructions,
        options=options,
        stream=False,
    )
    result = {
        "adapter": "ollama",
        "dry_run": bool(dry_run),
        "network_performed": False,
        "endpoint": endpoint,
        "endpoint_type": endpoint_type(endpoint),
        "model_id": model,
        "runtime_plan_hash": plan["manifest_hash"],
        "request_hash": canonical_hash(request_body),
        "runtime_plan": plan,
        "request": request_body,
        "response": None,
        "artifact_directory": None,
        "run_manifest_hash": None,
    }
    if dry_run:
        return result

    result["network_performed"] = True
    try:
        raw_response = chat(
            endpoint,
            request_body,
            timeout=timeout,
            opener=opener,
        )
        normalized = normalize_response(raw_response)
    except AdapterRequestError as error:
        raw_response = {"adapter_error": error.error}
        normalized = {
            "provider": "ollama",
            "response_text": "",
            "raw_response": raw_response,
            "model_id": model,
            "finish_reason": None,
            "usage": {"input_tokens": None, "output_tokens": None, "total_tokens": None},
            "timing": {},
            "tool_calls": [],
            "partial": False,
            "truncated": False,
            "error": error.error,
        }
    result["response"] = normalized

    manifest = build_manifest(
        plan=plan,
        model_identifier=str(normalized.get("model_id") or model),
        endpoint_type=f"ollama:{result['endpoint_type']}",
        generation_parameters={
            "options": dict(options or {}),
            "stream": False,
            "timeout_seconds": timeout,
        },
    )
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    plan_suffix = plan["manifest_hash"].removeprefix("sha256:")[:12]
    artifact_directory = Path(output_root) / f"ollama-{stamp}-{plan_suffix}"
    compiled_instructions = next(
        (
            message["content"] for message in request_body["messages"]
            if message.get("role") == "system"
        ),
        "",
    )
    metrics = {
        "request_hash": result["request_hash"],
        "finish_reason": normalized.get("finish_reason"),
        "usage": normalized.get("usage"),
        "timing": normalized.get("timing"),
        "partial": normalized.get("partial"),
        "truncated": normalized.get("truncated"),
        "error": normalized.get("error"),
    }
    write_run_artifacts(
        artifact_directory,
        manifest=manifest,
        task=task,
        plan=plan,
        compiled_instructions=compiled_instructions,
        raw_response=json.dumps(raw_response, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        metrics=metrics,
    )
    result["artifact_directory"] = str(artifact_directory)
    result["run_manifest_hash"] = manifest["manifest_hash"]
    return result
