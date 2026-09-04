"""Deterministic, agent-ready project Skill briefs."""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Iterable

from .common import (
    SkillFactoryError,
    argument,
    component_version,
    emit_json,
    project_profile,
    project_references,
    require_harness,
    resolve_project_root,
    task_slug,
)


ROLE_KEYS = (
    "required-by-recipe",
    "trigger-likely",
    "conditional",
    "optional",
    "excluded",
    "needs-agent-evaluation",
)


def _recipe_slug(value: Any) -> str | None:
    if isinstance(value, str):
        return value or None
    if isinstance(value, dict):
        for key in ("slug", "recipe", "id"):
            found = value.get(key)
            if isinstance(found, str) and found:
                return found
    return None


def _component_ref(value: Any) -> str | None:
    if isinstance(value, str):
        if "@" in value:
            return value
        version = component_version(value)
        return f"{value}@{version}" if version else value
    if isinstance(value, dict):
        slug = value.get("slug") or value.get("component") or value.get("id")
        version = value.get("version")
        if isinstance(slug, str) and slug:
            if not isinstance(version, str) or not version:
                version = component_version(slug)
            return f"{slug}@{version}" if version else slug
    return None


def _refs(values: Any) -> list[str]:
    if values is None:
        return []
    if isinstance(values, (str, dict)):
        values = [values]
    if not isinstance(values, Iterable):
        return []
    refs = [_component_ref(value) for value in values]
    return sorted({ref for ref in refs if ref})


def normalize_resolution(result: dict[str, Any]) -> dict[str, Any]:
    """Normalize the stable resolver schema while tolerating additive fields."""

    grouped = result.get("components")
    if not isinstance(grouped, dict):
        grouped = result.get("component_roles")
    if not isinstance(grouped, dict):
        grouped = {}

    aliases = {
        "required-by-recipe": ("required-by-recipe", "required_by_recipe", "required"),
        "trigger-likely": ("trigger-likely", "trigger_likely"),
        "conditional": ("conditional",),
        "optional": ("optional",),
        "excluded": ("excluded", "hard_excluded"),
        "needs-agent-evaluation": (
            "needs-agent-evaluation", "needs_agent_evaluation"
        ),
    }
    roles: dict[str, list[str]] = {}
    for role, keys in aliases.items():
        values: Any = None
        for key in keys:
            if key in grouped:
                values = grouped[key]
                break
            if key in result:
                values = result[key]
                break
        roles[role] = _refs(values)

    best = result.get("best_recipe")
    if best is None:
        best = result.get("primary_recipe")
    return {
        "primary_recipe": _recipe_slug(best),
        "roles": roles,
        "resolution": result,
    }


def resolve_for_skill(task: str, project: dict[str, Any]) -> dict[str, Any]:
    try:
        from upgradeables_harness.resolver.task import resolve_task
    except (ImportError, ModuleNotFoundError) as error:
        raise SkillFactoryError("The task resolver is unavailable in this installation.") from error
    result = resolve_task(task, project=project or None, use_project_profile=True)
    if not isinstance(result, dict):
        raise SkillFactoryError("The task resolver returned an invalid result.")
    return normalize_resolution(result)


def build_skill_brief(task: str, project_root: str | Path | None = None) -> dict[str, Any]:
    if not isinstance(task, str) or not task.strip():
        raise SkillFactoryError("A non-empty task is required.")
    root = resolve_project_root(project_root)
    require_harness(root)
    profile = project_profile(root)
    normalized = resolve_for_skill(task.strip(), profile)
    roles = normalized["roles"]
    recipe = normalized["primary_recipe"]
    candidate = task_slug(task)
    project_types = profile.get("project_types", [])
    if not isinstance(project_types, list):
        project_types = []
    references = project_references(root)
    status = "candidate-brief" if recipe else "needs-agent-evaluation"
    selected = sorted(
        set(roles["required-by-recipe"] + roles["trigger-likely"])
    )
    return {
        "schema_version": "1.0.0",
        "status": status,
        "candidate_skill": candidate,
        "task": task.strip(),
        "project_root": str(root),
        "project_types": project_types,
        "primary_recipe": recipe,
        "required_components": roles["required-by-recipe"],
        "trigger_likely_components": roles["trigger-likely"],
        "conditional_components": roles["conditional"],
        "optional_components": roles["optional"],
        "excluded_components": roles["excluded"],
        "needs_agent_evaluation": roles["needs-agent-evaluation"],
        "selected_component_pins": selected,
        "project_references": references,
        "instructions": [
            "Confirm the activation boundary and at least one nearby non-trigger.",
            "Confirm required inputs, missing-input behavior, authority, and host capabilities.",
            "Evaluate candidate components against canonical triggers and non-triggers.",
            "Keep the smallest sufficient composition and pin each selected slug@version.",
            "Define an observable output contract, stopping rule, and failure behavior.",
        ],
        "next_command": (
            f'upgradeables skill scaffold {candidate} --task "{task.strip()}"'
        ),
    }


def _print_brief(brief: dict[str, Any]) -> None:
    print(f"Candidate Skill: {brief['candidate_skill']}")
    print(f"Status: {brief['status']}")
    print(f"Task: {brief['task']}")
    project = ", ".join(brief["project_types"]) or "unclassified project"
    print(f"Project: {project}")
    print(f"Primary recipe: {brief['primary_recipe'] or 'no confident recipe'}")
    labels = (
        ("Required", "required_components"),
        ("Trigger-likely", "trigger_likely_components"),
        ("Conditional", "conditional_components"),
        ("Excluded", "excluded_components"),
    )
    for label, key in labels:
        values = brief[key]
        print(f"{label}: {', '.join(values) if values else 'none'}")
    references = brief["project_references"]
    print(f"Project references: {', '.join(references) if references else 'none declared'}")
    print(f"Next: {brief['next_command']}")


def command_brief(args: Any) -> int:
    try:
        brief = build_skill_brief(
            argument(args, "task", ""), argument(args, "project")
        )
    except SkillFactoryError as error:
        if argument(args, "json", False):
            emit_json({"status": "error", "error": str(error)})
        else:
            print(f"Skill brief failed: {error}", file=sys.stderr)
        return 2
    if argument(args, "json", False):
        emit_json(brief)
    else:
        _print_brief(brief)
    return 0
