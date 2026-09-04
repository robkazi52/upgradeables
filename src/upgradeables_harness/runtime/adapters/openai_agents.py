"""Optional OpenAI Agents SDK instruction integration without a core dependency."""
from __future__ import annotations

import inspect
from typing import Any

from .generic import capability, compose_instructions

_BASE_ATTRIBUTE = "_upgradeables_v04_base_instructions"
_APPLIED_ATTRIBUTE = "_upgradeables_v04_applied_instructions"
_MISSING = object()


def _append(base: str | None, plan: dict) -> str:
    return compose_instructions(base, plan, mode="append-managed-runtime-block")["combined_instructions"]


def describe_capabilities(agent: Any) -> dict:
    """Describe only integration surfaces observable on an agent object."""
    has_instructions = hasattr(agent, "instructions")
    return {
        "adapter": "openai-agents",
        "instruction_callback": capability(
            "supported" if has_instructions else "unsupported",
            "agent object instructions attribute",
        ),
        "tools": capability(
            "supported" if hasattr(agent, "tools") else "unknown",
            "agent object tools attribute" if hasattr(agent, "tools") else "not introspectable",
        ),
        "output_contract": capability(
            "supported" if hasattr(agent, "output_type") else "unknown",
            "agent object output_type attribute" if hasattr(agent, "output_type") else "not introspectable",
        ),
        "input_guardrails": capability(
            "supported" if hasattr(agent, "input_guardrails") else "unknown",
            "agent object input_guardrails attribute" if hasattr(agent, "input_guardrails") else "not introspectable",
        ),
        "output_guardrails": capability(
            "supported" if hasattr(agent, "output_guardrails") else "unknown",
            "agent object output_guardrails attribute" if hasattr(agent, "output_guardrails") else "not introspectable",
        ),
        "orchestration": capability(
            "supported" if hasattr(agent, "handoffs") else "unknown",
            "agent object handoffs attribute" if hasattr(agent, "handoffs") else "not introspectable",
        ),
    }


def _dynamic_wrapper(original, plan: dict):
    def dynamic(context, current_agent):
        result = original(context, current_agent)
        if inspect.isawaitable(result):
            async def finish():
                return _append(await result, plan)
            return finish()
        return _append(result, plan)

    dynamic.__upgradeables_base_instructions__ = original
    dynamic.__upgradeables_plan_hash__ = plan.get("manifest_hash")
    return dynamic


def apply_runtime_plan(agent: Any, plan: dict) -> Any:
    """Preserve an Agent's static or dynamic instructions and append one managed block."""
    if not hasattr(agent, "instructions"):
        raise TypeError("agent must expose an instructions attribute")
    if not isinstance(plan, dict):
        raise TypeError("plan must be a RuntimePlan dictionary")
    current = getattr(agent, "instructions", None)
    applied = getattr(agent, _APPLIED_ATTRIBUTE, _MISSING)
    if callable(current) and hasattr(current, "__upgradeables_base_instructions__"):
        original = current.__upgradeables_base_instructions__
    elif applied is not _MISSING and current == applied:
        original = getattr(agent, _BASE_ATTRIBUTE, current)
    else:
        original = current
    try:
        setattr(agent, _BASE_ATTRIBUTE, original)
    except (AttributeError, TypeError):
        pass
    if not callable(original):
        agent.instructions = _append(original, plan)
    else:
        agent.instructions = _dynamic_wrapper(original, plan)
    try:
        setattr(agent, _APPLIED_ATTRIBUTE, agent.instructions)
    except (AttributeError, TypeError):
        pass
    return agent
