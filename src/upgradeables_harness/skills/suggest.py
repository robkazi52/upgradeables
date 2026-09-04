"""Transparent repetition analysis for project Skill suggestions."""
from __future__ import annotations

import json
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

from .common import (
    SkillFactoryError,
    argument,
    emit_json,
    project_config,
    require_harness,
    resolve_project_root,
    task_slug,
)
from .history import load_task_events
from .map import ensure_skill_map


def _stable(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _components(event: dict[str, Any]) -> list[str]:
    values = event.get("component_composition")
    if values is None:
        values = event.get("candidate_components", [])
    if not isinstance(values, list):
        return []
    result: list[str] = []
    for item in values:
        if isinstance(item, str):
            result.append(item)
        elif isinstance(item, dict) and isinstance(item.get("slug"), str):
            version = item.get("version")
            result.append(
                f"{item['slug']}@{version}" if isinstance(version, str) else item["slug"]
            )
    return sorted(set(result))


def _group_key(event: dict[str, Any]) -> tuple[str, ...]:
    output = event.get("output_contract", event.get("requested_output_shape", ""))
    return (
        str(event.get("normalized_task", "")).strip().casefold(),
        str(event.get("task_archetype", "")),
        str(event.get("selected_recipe", "")),
        _stable(event.get("project_constraints", [])),
        _stable(output),
        str(event.get("authority_mode", "")),
        _stable(_components(event)),
    )


def _same_nonempty(events: list[dict[str, Any]], field: str) -> tuple[bool, Any]:
    values = [event.get(field) for event in events]
    if any(value in (None, "", [], {}) for value in values):
        return False, None
    encoded = {_stable(value) for value in values}
    return len(encoded) == 1, values[0] if len(encoded) == 1 else None


def _compatible_existing(
    skill_map: dict[str, Any], slug: str, recipe: str | None
) -> str | None:
    for item in skill_map.get("skills", []):
        if item.get("status") != "validated":
            continue
        if item.get("slug") == slug or (
            recipe and item.get("recipe") == recipe and item.get("slug") == slug
        ):
            return str(item["slug"])
    return None


def analyze_skill_suggestions(project_root: str | Path) -> dict[str, Any]:
    root = resolve_project_root(project_root)
    require_harness(root)
    config = project_config(root)
    threshold = config.get("skill_suggestion_threshold", 3)
    if not isinstance(threshold, int) or isinstance(threshold, bool) or threshold < 2:
        threshold = 3
    events = load_task_events(root)
    skill_map = ensure_skill_map(root, write=False)
    groups: dict[tuple[str, ...], list[dict[str, Any]]] = defaultdict(list)
    for event in events:
        if isinstance(event.get("normalized_task"), str):
            groups[_group_key(event)].append(event)

    suggestions: list[dict[str, Any]] = []
    for key, members in sorted(groups.items(), key=lambda item: item[0]):
        if len(members) < threshold:
            continue
        normalized_task, archetype, recipe, constraints, output, authority, components = key
        slug = task_slug(normalized_task)
        activation_ok, activation = _same_nonempty(members, "activation_boundary")
        inputs_ok, inputs = _same_nonempty(members, "required_inputs")
        procedure_ok, procedure = _same_nonempty(members, "procedure_signature")
        output_ok = bool(output and output not in ('""', "null", "[]", "{}"))
        existing = _compatible_existing(skill_map, slug, recipe or None)
        checks = {
            "recurrence": "pass",
            "activation_boundary": "pass" if activation_ok else "needs-user-definition",
            "stable_inputs": "pass" if inputs_ok else "needs-user-definition",
            "stable_procedure": "pass" if procedure_ok else "needs-user-definition",
            "output_contract": "pass" if output_ok else "needs-user-definition",
            "existing_skill_gap": "fail" if existing else "pass",
        }
        if existing:
            status = "existing-skill"
        elif all(value == "pass" for value in checks.values()):
            status = "candidate"
        else:
            status = "needs-user-definition"
        timestamps = sorted(
            str(event.get("timestamp")) for event in members if event.get("timestamp")
        )
        suggestions.append(
            {
                "status": status,
                "packaging_form": "project-skill",
                "slug": slug,
                "event_ids": [str(event.get("event_id", "")) for event in members],
                "occurrence_count": len(members),
                "date_range": {
                    "first": timestamps[0] if timestamps else None,
                    "last": timestamps[-1] if timestamps else None,
                },
                "normalized_task": normalized_task,
                "task_archetype": archetype or None,
                "recipe": recipe or None,
                "authority_mode": authority or None,
                "project_constraints": json.loads(constraints),
                "output_contract": json.loads(output) if output else None,
                "components": json.loads(components),
                "activation_boundary": activation,
                "required_inputs": inputs,
                "procedure_signature": procedure,
                "eligibility_checks": checks,
                "existing_skill": existing,
                "next_command": (
                    f'upgradeables skill scaffold {slug} --task "{normalized_task}"'
                    if status == "candidate"
                    else None
                ),
            }
        )

    if not events:
        overall = "not-enough-history"
    elif not suggestions:
        overall = "not-enough-history"
    elif any(item["status"] == "candidate" for item in suggestions):
        overall = "candidate"
    elif all(item["status"] == "existing-skill" for item in suggestions):
        overall = "existing-skill"
    else:
        overall = "needs-user-definition"
    return {
        "schema_version": "1.0.0",
        "status": overall,
        "method": "workflow repetition analysis",
        "project_root": str(root),
        "recorded_event_count": len(events),
        "threshold": threshold,
        "suggestions": suggestions,
        "writes_performed": False,
    }


def command_suggest(args: Any) -> int:
    try:
        result = analyze_skill_suggestions(argument(args, "project"))
    except SkillFactoryError as error:
        if argument(args, "json", False):
            emit_json({"status": "error", "error": str(error)})
        else:
            print(f"Skill suggestion failed: {error}", file=sys.stderr)
        return 2
    if argument(args, "json", False):
        emit_json(result)
        return 0
    if not result["suggestions"]:
        print(
            f"No Skill candidate: {result['recorded_event_count']} recorded task event(s); "
            f"threshold is {result['threshold']}."
        )
        return 0
    for item in result["suggestions"]:
        print(f"Candidate Skill: {item['slug']}")
        print(f"Status: {item['status']}")
        print(f"Observed comparable events: {item['occurrence_count']}")
        print(f"Primary job: {item['normalized_task']}")
        print(f"Primary recipe: {item['recipe'] or 'direct path'}")
        failed = [key for key, value in item["eligibility_checks"].items() if value != "pass"]
        if failed:
            print(f"Needs definition: {', '.join(failed)}")
        if item["next_command"]:
            print(f"Next: {item['next_command']}")
    return 0
