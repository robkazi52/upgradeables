"""Create and list project-local Skill scaffolds."""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from .brief import build_skill_brief
from .common import (
    SkillFactoryError,
    argument,
    display_name,
    emit_json,
    registry_version,
    require_harness,
    resolve_project_root,
    skill_path,
    validate_slug,
)
from .map import ensure_skill_map, list_skill_records, upsert_skill


def _single_line(value: str) -> str:
    return " ".join(value.replace("\x00", "").split())


def _selected_table(components: list[str]) -> str:
    if not components:
        return (
            "| Component | Version | Decision | Active trigger | Reason |\n"
            "|---|---|---|---|---|\n"
            "| `TODO` | `TODO` | Keep / Drop | TODO | TODO |"
        )
    rows = [
        "| Component | Version | Decision | Active trigger | Reason |",
        "|---|---|---|---|---|",
    ]
    for reference in components:
        slug, _, version = reference.partition("@")
        version = version or "TODO"
        rows.append(
            f"| `{slug}` | `{version}` | Keep | TODO: confirm canonical trigger | "
            "TODO: explain why this mechanism is necessary for this project job |"
        )
    return "\n".join(rows)


def _skill_text(
    slug: str, *, task: str | None, brief: dict[str, Any] | None
) -> str:
    task_text = _single_line(task) if task else "TODO: define the project-specific job"
    recipe = brief.get("primary_recipe") if brief else None
    components = list(brief.get("selected_component_pins", [])) if brief else []
    excluded = list(brief.get("excluded_components", [])) if brief else []
    references = list(brief.get("project_references", [])) if brief else []
    description = (
        f"Draft project Skill for {task_text}. Use only after its activation boundary "
        "and nearby exclusions are completed and validated."
    )
    selected = _selected_table(components)
    excluded_text = "\n".join(f"- `{value}`" for value in excluded) or "- TODO"
    reference_text = (
        "\n".join(
            f"- `{value}` — TODO: state the exact condition for loading it."
            for value in references
        )
        or "- TODO: add only maintained project references and say when to load each one."
    )
    return f"""---
name: {slug}
description: {json.dumps(description, ensure_ascii=False)}
---

# {display_name(slug)}

Status: draft

This project-local scaffold contains deterministic resolver output and explicit
TODOs. Resolver candidates are not active until their canonical triggers,
non-triggers, authority, and necessity are checked.

## Task Identity and Activation Boundary

Task: {task_text}

- Positive activation: TODO: describe the recognizable project job.
- Do not activate: TODO: name at least one nearby task this Skill must not handle.
- Primary recipe: `{recipe or 'none-selected'}`
- Project profile: read `.upgradeables/project.json`; do not invent missing project facts.

## Target Host and Compatibility

- Host: model-agnostic project harness.
- Required capabilities: TODO.
- Optional capabilities and fallback: TODO.
- Network: not required unless explicitly declared here and authorized at task time.

## Required Inputs and Explicit State

- Required inputs: TODO.
- Missing-input behavior: stop or ask for the smallest useful clarification.
- Source of truth: TODO: identify project paths or user-supplied artifacts.
- Do not record private chain-of-thought or claim hidden memory.

## Behavior Gene (optional)

None selected. Add one only when a reusable behavior materially improves this job.

## Core / References (optional)

{reference_text}

## Selected Upgradeables

Registry: `0.2.1`

{selected}

Resolver exclusions:

{excluded_text}

## Authority and Precedence

Current user instructions and host permissions control reads, edits, sends,
deployments, and other actions. Skill activation grants no additional authority.
Review-only tasks must remain non-mutating.

## Procedure

1. Confirm the task matches the positive boundary and no non-trigger applies.
2. Read only the project profile, references, and source material needed for this job.
3. Confirm required inputs, current-task authority, and host capabilities.
4. Evaluate each proposed Upgradeable against its canonical trigger and non-trigger.
5. Execute the smallest sufficient workflow. TODO: replace this line with stable,
   project-specific steps without inventing domain semantics.
6. Validate the output contract and stop at the declared completion condition.

## Validators and Failure Handling

- Draft validator: structure, identity, paths, and canonical references.
- Final validator: activation/non-activation, authority, behavior, failure path,
  component versions, and TODO removal.
- Missing capability: report the boundary and use a declared safe fallback or stop.
- Failed validation: do not claim completion; preserve observed evidence and next step.

## Output Contract

TODO: define an observable artifact or response, required fields, evidence, and
completion check. A fluent response is not by itself validation.

## Strong-Model Scaling

Do not add branches, state, agents, or validators above the task's complexity ceiling.

## Provenance

- Project task: {task_text}
- Primary recipe: `{recipe or 'none-selected'}`
- Bundled registry: `{registry_version()}`
- Component candidates were produced by deterministic task resolution and require
  task-time trigger evaluation.

## Tests

- Positive activation: TODO.
- Negative activation: TODO.
- Authority or conflict case: TODO.
- Failure case: TODO.
- Composition case: TODO.
"""


def _support_files(slug: str) -> dict[str, str]:
    return {
        "references/README.md": (
            f"# {display_name(slug)} references\n\n"
            "Add maintained project references only. For each file, document the exact "
            "condition under which the Skill should load it.\n"
        ),
        "scripts/README.md": (
            "# Scripts\n\nPlace deterministic repeated operations here. Document inputs, "
            "outputs, failure behavior, and required authority.\n"
        ),
        "assets/README.md": (
            "# Assets\n\nPlace only fixed materials needed in Skill output here.\n"
        ),
        "tests/cases.json": json.dumps(
            {
                "schema_version": "1.0.0",
                "skill": slug,
                "status": "draft",
                "cases": [
                    {"kind": "positive", "task": "TODO", "expected": "activate"},
                    {"kind": "negative", "task": "TODO", "expected": "do-not-activate"},
                    {"kind": "authority", "task": "TODO", "expected": "respect-boundary"},
                    {"kind": "failure", "task": "TODO", "expected": "safe-failure"},
                    {"kind": "composition", "task": "TODO", "expected": "minimum-sufficient"},
                ],
            },
            indent=2,
        ) + "\n",
    }


def scaffold_skill(
    project_root: str | Path,
    slug: str,
    *,
    task: str | None = None,
    force: bool = False,
) -> dict[str, Any]:
    root = resolve_project_root(project_root)
    require_harness(root)
    validate_slug(slug)
    target = skill_path(root, slug)
    skill_file = target / "SKILL.md"
    if target.is_dir() and any(target.iterdir()) and not force:
        raise SkillFactoryError(
            f"Skill directory is not empty: {target}. Use --force to replace scaffold-owned files."
        )
    if target.exists() and not target.is_dir():
        raise SkillFactoryError(f"Skill path exists and is not a directory: {target}")

    brief = build_skill_brief(task, root) if task else None
    files = {"SKILL.md": _skill_text(slug, task=task, brief=brief), **_support_files(slug)}
    target.mkdir(parents=True, exist_ok=True)
    for relative, content in files.items():
        path = target / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    recipe = brief.get("primary_recipe") if brief else None
    components = list(brief.get("selected_component_pins", [])) if brief else []
    record = upsert_skill(
        root, slug=slug, status="draft", recipe=recipe, components=components
    )
    return {
        "schema_version": "1.0.0",
        "status": "created" if not force else "replaced",
        "project_root": str(root),
        "skill": record,
        "created_files": [str((target / relative).relative_to(root)) for relative in files],
        "validation": "draft",
        "next_command": f"upgradeables skill validate --draft {skill_file}",
    }


def command_scaffold(args: Any) -> int:
    try:
        result = scaffold_skill(
            argument(args, "project"),
            argument(args, "slug", ""),
            task=argument(args, "task"),
            force=bool(argument(args, "force", False)),
        )
    except SkillFactoryError as error:
        if argument(args, "json", False):
            emit_json({"status": "error", "error": str(error)})
        else:
            print(f"Skill scaffold failed: {error}", file=sys.stderr)
        return 2
    if argument(args, "json", False):
        emit_json(result)
    else:
        print(f"Project Skill scaffold {result['status']}.")
        print(f"Path: {result['skill']['path']}")
        print(f"Status: {result['skill']['status']}")
        print(f"Next: {result['next_command']}")
    return 0


def command_list(args: Any) -> int:
    try:
        root = resolve_project_root(argument(args, "project"))
        require_harness(root)
        ensure_skill_map(root, write=False)
        skills = list_skill_records(root)
    except SkillFactoryError as error:
        if argument(args, "json", False):
            emit_json({"status": "error", "error": str(error)})
        else:
            print(f"Skill list failed: {error}", file=sys.stderr)
        return 2
    result = {
        "schema_version": "1.0.0",
        "project_root": str(root),
        "count": len(skills),
        "skills": skills,
    }
    if argument(args, "json", False):
        emit_json(result)
    elif not skills:
        print("No project Skills are registered.")
    else:
        for item in skills:
            marker = "" if item["exists"] else " (missing file)"
            print(f"{item['slug']}  {item['status']}  {item['path']}{marker}")
    return 0
