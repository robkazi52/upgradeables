"""Matched baseline, static, fixed-resolution, and end-to-end conditions."""
from __future__ import annotations

from copy import deepcopy

from .. import compile_task
from ..compiler import canonical_hash, compile as compile_resolution
from ..data import load_runtime_registry
from ..models import RuntimeContext

CANONICAL_CONDITIONS = (
    "baseline",
    "static-full",
    "adaptive-fixed-resolution",
    "adaptive-end-to-end",
)
CONDITION_ALIASES = {"adaptive-runtime": "adaptive-end-to-end"}


def canonical_condition(condition: str) -> str:
    """Return the public canonical label while preserving one v0.4 alias."""
    if not isinstance(condition, str):
        raise ValueError("Evaluation condition must be a string")
    canonical = CONDITION_ALIASES.get(condition, condition)
    if canonical not in CANONICAL_CONDITIONS:
        raise ValueError(f"Unsupported core evaluation condition: {condition}")
    return canonical


def static_full_text() -> str:
    return load_runtime_registry()["static_full"]["text"]


def build_condition(
    task: str,
    condition: str,
    *,
    fixed_resolution: dict | None = None,
    model_profile: str = "medium",
    max_directive_tokens: int = 500,
) -> dict:
    canonical = canonical_condition(condition)
    task_resolution_source = None
    fixed_resolution_hash = None
    if canonical == "baseline":
        instructions = ""
        plan = None
    elif canonical == "static-full":
        instructions = static_full_text()
        plan = None
    elif canonical == "adaptive-fixed-resolution":
        if fixed_resolution is None:
            raise ValueError("adaptive-fixed-resolution requires a fixed TaskResolution for this task")
        if not isinstance(fixed_resolution, dict):
            raise ValueError("fixed TaskResolution must be an object")
        if fixed_resolution.get("query") != task:
            raise ValueError("fixed TaskResolution query must match the suite task prompt exactly")
        fixed_resolution_hash = canonical_hash(fixed_resolution)
        plan = compile_resolution(
            deepcopy(fixed_resolution),
            RuntimeContext(
                model_profile=model_profile,
                max_directive_tokens=max_directive_tokens,
            ),
        )
        task_resolution_source = "fixed-suite"
        instructions = plan["instruction_capsule"]
    elif canonical == "adaptive-end-to-end":
        plan = compile_task(
            task,
            model_profile=model_profile,
            max_directive_tokens=max_directive_tokens,
            use_project_profile=False,
        )
        task_resolution_source = "v0.3-resolver"
        instructions = plan["instruction_capsule"]
    result = {
        "condition": canonical,
        "evaluation_mode": canonical,
        "task": task,
        "instructions": instructions,
        "instruction_hash": canonical_hash(instructions),
        "runtime_plan": plan,
        "runtime_plan_hash": (
            (plan.get("manifest_hash") or canonical_hash(plan)) if plan is not None else None
        ),
        "task_resolution_source": task_resolution_source,
        "task_resolution_hash": plan.get("task_resolution_hash") if plan is not None else None,
        "fixed_resolution_hash": fixed_resolution_hash,
    }
    result["condition_hash"] = canonical_hash(result)
    return result
