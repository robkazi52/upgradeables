"""Matched baseline, static-full, and adaptive runtime conditions."""
from __future__ import annotations

from .. import compile_task
from ..compiler import canonical_hash
from ..data import load_runtime_registry


def static_full_text() -> str:
    return load_runtime_registry()["static_full"]["text"]


def build_condition(task: str, condition: str, *, model_profile: str = "medium", max_directive_tokens: int = 500) -> dict:
    if condition == "baseline":
        instructions = ""
        plan = None
    elif condition == "static-full":
        instructions = static_full_text()
        plan = None
    elif condition == "adaptive-runtime":
        plan = compile_task(task, model_profile=model_profile, max_directive_tokens=max_directive_tokens)
        instructions = plan["instruction_capsule"]
    else:
        raise ValueError(f"Unsupported core evaluation condition: {condition}")
    result = {
        "condition": condition,
        "task": task,
        "instructions": instructions,
        "instruction_hash": canonical_hash(instructions),
        "runtime_plan": plan,
        "runtime_plan_hash": (
            (plan.get("manifest_hash") or canonical_hash(plan)) if plan is not None else None
        ),
    }
    result["condition_hash"] = canonical_hash(result)
    return result
