"""Generic host composition with explicit base-instruction preservation."""
from __future__ import annotations

import ipaddress
from urllib.parse import urlsplit

from ..manifest import redact_secrets

MODES = {
    "append-managed-runtime-block",
    "prepend-managed-runtime-block",
    "return-separate-block",
}
TRI_STATES = {"supported", "unsupported", "unknown"}


class AdapterRequestError(RuntimeError):
    """An adapter transport failure with a provider-neutral public record."""

    def __init__(self, error: dict):
        self.error = error
        super().__init__(f"{error['kind']}: {error['message']}")


def capability(status: str = "unknown", evidence: str | None = None) -> dict:
    """Return one normalized tri-state capability declaration."""
    if status not in TRI_STATES:
        raise ValueError(f"invalid capability status: {status}")
    result = {"status": status}
    if evidence:
        result["evidence"] = evidence
    return result


def endpoint_type(endpoint: str) -> str:
    """Classify an endpoint conservatively without performing network I/O."""
    try:
        parsed = urlsplit(endpoint)
        hostname = (parsed.hostname or "").rstrip(".").lower()
    except ValueError:
        return "unknown"
    if not parsed.scheme or not hostname:
        return "unknown"
    if hostname == "localhost" or hostname.endswith(".localhost"):
        return "loopback"
    try:
        address = ipaddress.ip_address(hostname)
    except ValueError:
        if hostname.endswith(".local") or "." not in hostname:
            return "private-network"
        return "remote"
    if address.is_loopback:
        return "loopback"
    if address.is_private or address.is_link_local:
        return "private-network"
    return "remote"


def normalized_error(
    *,
    provider: str,
    message: str,
    status: int | None = None,
    response_started: bool = False,
) -> dict:
    """Classify an adapter failure without embedding credentials or headers."""
    if response_started:
        kind = "stream_interrupted"
    elif status is None:
        kind = "endpoint_unavailable"
    elif status in {400, 422}:
        kind = "capability_mismatch"
    elif status == 401:
        kind = "authentication_failed"
    elif status == 403:
        kind = "permission_denied"
    elif status == 404 and provider == "ollama":
        kind = "model_unavailable"
    elif status == 404:
        kind = "not_found"
    elif status == 429:
        kind = "rate_limited"
    elif status >= 500:
        kind = "server_error"
    else:
        kind = "request_failed"
    return {
        "kind": kind,
        "provider": provider,
        "status": status,
        "message": redact_secrets(str(message)),
        "response_started": response_started,
    }


def compose_instructions(
    base_instructions: str | None,
    plan: dict,
    *,
    mode: str = "return-separate-block",
) -> dict:
    if mode not in MODES:
        raise ValueError(f"Unknown instruction composition mode: {mode}")
    if base_instructions is not None and not isinstance(base_instructions, str):
        raise TypeError("base_instructions must be a string or None")
    base = base_instructions or ""
    runtime = plan.get("instruction_capsule", "")
    if not isinstance(runtime, str):
        raise TypeError("plan instruction_capsule must be a string")
    if mode == "return-separate-block":
        combined = base
    elif mode == "append-managed-runtime-block":
        combined = "\n\n".join(value for value in (base, runtime) if value)
    else:
        combined = "\n\n".join(value for value in (runtime, base) if value)
    return {
        "mode": mode,
        "base_instructions": base,
        "runtime_instructions": runtime,
        "combined_instructions": combined,
        "state_contract": plan.get("state_contract", []),
        "validators": plan.get("validators", []),
        "orchestration": plan.get("orchestration", []),
        "tool_requirements": plan.get("tool_requirements", []),
        "output_contract": plan.get("output_contract", []),
        "warnings": plan.get("warnings", []),
    }
