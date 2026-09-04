"""Deterministic v0.3 TaskResolution to v0.4 RuntimePlan compiler."""
from __future__ import annotations

import hashlib
import json
from copy import deepcopy
from typing import Any

from .budget import estimate_tokens, lower_level
from .data import load_model_profiles, load_runtime_registry, runtime_components
from .models import RuntimeContext

COMPILER_VERSION = "0.4.0"
LEVEL_ORDER = {"micro": 0, "standard": 1, "full": 2}
ACTIVE_GROUPS = ("required_by_recipe", "trigger_likely")
EDITING_CLASSES = {"editing-repair"}
REQUIRED_RESOLUTION_FIELDS = {
    "schema_version", "registry_version", "selection_only", "query", "normalized_task",
    "task", "environment", "failure_modes", "complexity", "matched_prior_rules",
    "hard_restrictions", "required_checks", "best_recipe", "candidates",
    "required_by_recipe", "trigger_likely", "conditional", "optional", "excluded",
    "needs_agent_evaluation", "activation_note",
}
SELECTION_GROUPS = (*ACTIVE_GROUPS, "conditional", "optional", "excluded", "needs_agent_evaluation")
SELECTION_ITEM_FIELDS = {"slug", "version", "plain_display_name", "recipe_role", "status", "reasons"}
COMPLEXITY_LEVELS = ("L0", "L1", "L2", "L3", "L4", "L5")


class RuntimeCompileError(ValueError):
    """Compilation failed closed because the input or composition is unsafe."""


def canonical_hash(value: Any) -> str:
    encoded = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _require_string(value: Any, path: str, *, nonempty: bool = False) -> None:
    if not isinstance(value, str) or (nonempty and not value.strip()):
        qualifier = "non-empty " if nonempty else ""
        raise RuntimeCompileError(f"TaskResolution {path} must be a {qualifier}string")


def _require_string_array(value: Any, path: str) -> None:
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise RuntimeCompileError(f"TaskResolution {path} must be an array of strings")


def validate_task_resolution(resolution: dict, components: dict[str, dict]) -> None:
    """Validate the dependency-free subset of the published TaskResolution schema."""
    if not isinstance(resolution, dict):
        raise RuntimeCompileError("TaskResolution must be an object")
    missing = sorted(REQUIRED_RESOLUTION_FIELDS - set(resolution))
    if missing:
        raise RuntimeCompileError("TaskResolution missing required fields: " + ", ".join(missing))
    if resolution["schema_version"] != "1.0.0" or resolution["selection_only"] is not True:
        raise RuntimeCompileError("Unsupported TaskResolution contract; expected schema 1.0.0 selection_only=true")
    _require_string(resolution["registry_version"], "registry_version")
    expected_registry_version = load_runtime_registry()["registry_version"]
    if resolution["registry_version"] != expected_registry_version:
        raise RuntimeCompileError(
            f"Unsupported TaskResolution registry_version {resolution['registry_version']!r}; "
            f"installed runtime data expects {expected_registry_version!r}"
        )
    _require_string(resolution["query"], "query", nonempty=True)
    _require_string(resolution["normalized_task"], "normalized_task", nonempty=True)
    _require_string(resolution["activation_note"], "activation_note", nonempty=True)

    if "project" in resolution and resolution["project"] is not None and not isinstance(resolution["project"], dict):
        raise RuntimeCompileError("TaskResolution project must be an object or null")
    task = resolution["task"]
    if not isinstance(task, dict):
        raise RuntimeCompileError("TaskResolution task must be an object")
    missing_task = sorted({"resolution", "archetype", "subtype", "execution_form"} - set(task))
    if missing_task:
        raise RuntimeCompileError("TaskResolution task missing required fields: " + ", ".join(missing_task))
    if task["resolution"] not in {"matched", "ambiguous", "no-match"}:
        raise RuntimeCompileError("TaskResolution task.resolution is unsupported")
    for key in ("archetype", "subtype"):
        if task[key] is not None and not isinstance(task[key], str):
            raise RuntimeCompileError(f"TaskResolution task.{key} must be a string or null")
    _require_string(task["execution_form"], "task.execution_form")

    if not isinstance(resolution["environment"], dict):
        raise RuntimeCompileError("TaskResolution environment must be an object")
    if not isinstance(resolution["failure_modes"], list):
        raise RuntimeCompileError("TaskResolution failure_modes must be an array")
    complexity = resolution["complexity"]
    if not isinstance(complexity, dict):
        raise RuntimeCompileError("TaskResolution complexity must be an object")
    missing_complexity = sorted({"floor", "ceiling", "reasons"} - set(complexity))
    if missing_complexity:
        raise RuntimeCompileError(
            "TaskResolution complexity missing required fields: " + ", ".join(missing_complexity)
        )
    if complexity["floor"] not in COMPLEXITY_LEVELS or complexity["ceiling"] not in COMPLEXITY_LEVELS:
        raise RuntimeCompileError("TaskResolution complexity floor and ceiling must be L0 through L5")
    if COMPLEXITY_LEVELS.index(complexity["floor"]) > COMPLEXITY_LEVELS.index(complexity["ceiling"]):
        raise RuntimeCompileError("TaskResolution complexity floor cannot exceed ceiling")
    _require_string_array(complexity["reasons"], "complexity.reasons")

    if not isinstance(resolution["matched_prior_rules"], list):
        raise RuntimeCompileError("TaskResolution matched_prior_rules must be an array")
    _require_string_array(resolution["hard_restrictions"], "hard_restrictions")
    _require_string_array(resolution["required_checks"], "required_checks")
    if resolution["best_recipe"] is not None and not isinstance(resolution["best_recipe"], dict):
        raise RuntimeCompileError("TaskResolution best_recipe must be an object or null")
    if not isinstance(resolution["candidates"], list):
        raise RuntimeCompileError("TaskResolution candidates must be an array")

    for group in SELECTION_GROUPS:
        if not isinstance(resolution[group], list):
            raise RuntimeCompileError(f"TaskResolution {group} must be an array")
        for index, selected in enumerate(resolution[group]):
            if not isinstance(selected, dict):
                raise RuntimeCompileError(f"TaskResolution {group}[{index}] must be an object")
            missing_selected = sorted(SELECTION_ITEM_FIELDS - set(selected))
            if missing_selected:
                raise RuntimeCompileError(
                    f"TaskResolution {group}[{index}] missing required fields: " + ", ".join(missing_selected)
                )
            _require_string(selected["slug"], f"{group}[{index}].slug", nonempty=True)
            _require_string(selected["version"], f"{group}[{index}].version", nonempty=True)
            _require_string_array(selected["reasons"], f"{group}[{index}].reasons")
            slug = selected["slug"]
            if slug not in components:
                raise RuntimeCompileError(f"Unknown runtime component: {slug!r}")
            if selected.get("version") != components[slug]["component_version"]:
                raise RuntimeCompileError(
                    f"Pinned version mismatch for {slug}: {selected.get('version')!r}; "
                    f"runtime data has {components[slug]['component_version']!r}"
                )


def _initial_level(profile: str, ceiling: str, maximum: str) -> str:
    level = load_model_profiles()["profiles"][profile]["default_level"]
    if ceiling == "L0":
        level = "micro"
    elif ceiling == "L1" and LEVEL_ORDER[level] > LEVEL_ORDER["standard"]:
        level = "standard"
    if LEVEL_ORDER[level] > LEVEL_ORDER[maximum]:
        level = maximum
    return level


def _directive_order(record: dict) -> tuple[int, str]:
    classes = set(record.get("functional_classes", []))
    slug = record["slug"]
    if "authority" in slug or "authenticity" in slug:
        rank = 0
    elif slug in {"task-set-lock-in", "mode-lock-in"}:
        rank = 1
    elif classes & {"truth-grounding", "context-retrieval"}:
        rank = 2
    elif classes & {"state", "drift-control"}:
        rank = 3
    elif classes & {"planning-reasoning", "framing-intake", "meta-control"}:
        rank = 4
    elif "editing-repair" in classes:
        rank = 5
    elif "validation" in classes:
        rank = 6
    elif "output" in classes:
        rank = 7
    else:
        rank = 4
    return rank, slug


def _capability_available(requirement: str, context: RuntimeContext) -> bool:
    if requirement == "parallel-workers":
        return context.host.parallelism
    if requirement == "durable-state":
        return context.host.state_support not in {"", "none", "unsupported"}
    return requirement in context.host.tools


def _render_capsule(hard_restrictions: list[str], directives: list[str]) -> str:
    lines = ["<upgradeables-runtime version=\"0.4.0\">", "Task controls:"]
    lines.extend(f"- {item}" for item in [*hard_restrictions, *directives])
    lines.append("</upgradeables-runtime>")
    return "\n".join(lines) if hard_restrictions or directives else ""


def _directive_fingerprint(value: str) -> str:
    """Conservatively identify only text-equivalent controls within a declared group."""
    return " ".join(value.split()).casefold().rstrip(" .")


def _unique_channel(items: list[dict]) -> list[dict]:
    seen = set()
    output = []
    for item in items:
        key = json.dumps(item, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
        if key not in seen:
            seen.add(key)
            output.append(item)
    return output


def compile(task_resolution: dict, runtime_context: RuntimeContext | dict | None = None) -> dict:
    context = RuntimeContext.from_value(runtime_context)
    if context.model_profile not in {"small", "medium", "strong", "auto", "custom"}:
        raise RuntimeCompileError(f"Unknown model profile: {context.model_profile}")
    if context.max_directive_tokens < 0:
        raise RuntimeCompileError("max_directive_tokens must be non-negative")
    records = runtime_components()
    validate_task_resolution(task_resolution, records)
    resolution = deepcopy(task_resolution)
    decisions: list[dict] = []
    warnings: list[str] = []
    excluded: list[dict] = []
    selected: list[tuple[str, str, bool, list[str]]] = []
    seen = set()
    for group in ACTIVE_GROUPS:
        required = group == "required_by_recipe"
        for item in resolution[group]:
            if item["slug"] not in seen:
                selected.append((item["slug"], group, required, list(item.get("reasons", []))))
                seen.add(item["slug"])
    for group, reason in (
        ("conditional", "condition was not deterministically activated by v0.3"),
        ("optional", "optional selection was not explicitly activated"),
        ("needs_agent_evaluation", "task-time trigger requires host/agent evaluation"),
        ("excluded", "excluded by v0.3 selection, authority, or complexity rules"),
    ):
        for item in resolution[group]:
            if item["slug"] not in seen:
                excluded.append({"slug": item["slug"], "reason": reason, "source_group": group})

    # Required package dependencies are structural, not a new task-selection pass.
    index = 0
    while index < len(selected):
        slug, _, _, _ = selected[index]
        for dependency in records[slug]["compile_constraints"].get("requires", []):
            if dependency not in records:
                raise RuntimeCompileError(f"Runtime dependency {dependency!r} required by {slug!r} is unavailable")
            if dependency not in seen:
                selected.append((dependency, "runtime-dependency", True, [f"required by {slug}"]))
                seen.add(dependency)
                decisions.append({"type": "dependency", "component": dependency, "reason": f"required by {slug}"})
        index += 1

    selected_slugs = {item[0] for item in selected}
    for slug, _, _, _ in selected:
        conflicts = set(records[slug]["compile_constraints"].get("do_not_combine_with", [])) & selected_slugs
        conflicts.discard(slug)
        if conflicts:
            raise RuntimeCompileError(f"Unresolved runtime conflict: {slug} conflicts with {sorted(conflicts)[0]}")

    review_only = resolution["environment"].get("review_only") is True
    ceiling = resolution["complexity"]["ceiling"]
    compiled: list[dict] = []
    channels = {key: [] for key in ("state_contract", "validators", "orchestration", "tool_requirements", "output_contract")}
    for slug, source_group, required, reasons in selected:
        record = records[slug]
        classes = set(record.get("functional_classes", []))
        if review_only and classes & EDITING_CLASSES:
            excluded.append({"slug": slug, "reason": "review-only authority suppresses editing and repair controls"})
            decisions.append({"type": "precedence", "component": slug, "decision": "suppressed-review-only"})
            continue
        if record["runtime_form"] == "not-runtime-injectable":
            excluded.append({"slug": slug, "reason": "package is a builder/meta tool, not a per-task runtime control"})
            decisions.append({"type": "runtime-form", "component": slug, "decision": "not-runtime-injectable"})
            continue
        level = _initial_level(
            context.model_profile,
            ceiling,
            record["compile_constraints"].get("maximum_default_verbosity", "full"),
        )
        missing_capabilities = [req for req in record["tool_requirements"] if not _capability_available(req, context)]
        if missing_capabilities:
            warning = f"{slug} requires unavailable host capability: {', '.join(missing_capabilities)}"
            warnings.append(warning)
            decisions.append({"type": "capability", "component": slug, "decision": "limitation", "missing": missing_capabilities})
        directives = [] if missing_capabilities else list(record["compile"][level]["directives"])
        invariants = (
            [f"Required invariant: {value}" for value in record["compile"][level]["mandatory_invariants"]]
            if record["runtime_injectable"] else []
        )
        compiled.append({
            "slug": slug,
            "version": record["component_version"],
            "runtime_level": level,
            "runtime_form": record["runtime_form"],
            "source_group": source_group,
            "required": required,
            "selection_reasons": reasons,
            "directives": directives,
            "mandatory_invariants": invariants,
            "dedupe_group": record["compile_constraints"].get("dedupe_group"),
            "source_path": record["source_path"],
        })
        for value in record["state_contract"]:
            channels["state_contract"].append({"component": slug, "contract": value})
        for value in record["validator_checks"]:
            channels["validators"].append({"component": slug, "check": value})
        for value in record["orchestration"]:
            channels["orchestration"].append({"component": slug, "control": value})
        for value in record["tool_requirements"]:
            channels["tool_requirements"].append({"component": slug, "capability": value, "available": _capability_available(value, context)})
        for value in record["output_contract"]:
            channels["output_contract"].append({"component": slug, "contract": value})

    for check in resolution["required_checks"]:
        channels["validators"].append({"component": "task-resolution", "check": check})

    def capsule_for_current() -> tuple[str, list[dict]]:
        ordered = sorted(compiled, key=lambda item: _directive_order(records[item["slug"]]))
        emitted: list[str] = []
        provenance_rows: list[dict] = []
        occupied_groups: dict[str, dict[str, str]] = {}
        for item in ordered:
            group = item["dedupe_group"]
            occupied = occupied_groups.setdefault(group, {}) if group else {}
            for directive in item["directives"]:
                fingerprint = _directive_fingerprint(directive)
                retained_from = occupied.get(fingerprint) if group else None
                suppressed = retained_from is not None
                if suppressed:
                    decisions.append({
                        "type": "dedupe", "component": item["slug"], "group": group,
                        "decision": "equivalent-directive-suppressed", "retained_from": retained_from,
                        "directive": directive,
                    })
                else:
                    emitted.append(directive)
                    if group:
                        occupied[fingerprint] = item["slug"]
                provenance_rows.append({
                    "item": item, "text": directive, "kind": "directive", "emitted": not suppressed,
                    "suppression_reason": f"equivalent directive retained from {retained_from}" if suppressed else None,
                })
            # Mandatory invariants survive semantic-group dedupe and density compression.
            for invariant in item["mandatory_invariants"]:
                emitted_here = invariant not in emitted
                if emitted_here:
                    emitted.append(invariant)
                provenance_rows.append({
                    "item": item, "text": invariant, "kind": "mandatory-invariant", "emitted": emitted_here,
                    "suppression_reason": None if emitted_here else "identical invariant already emitted",
                })
        restrictions = list(dict.fromkeys(resolution["hard_restrictions"]))
        return _render_capsule(restrictions, emitted), provenance_rows

    capsule, _ = capsule_for_current()
    # Compress all components deterministically before removing adaptive additions.
    while estimate_tokens(capsule) > context.max_directive_tokens:
        candidate = next((item for item in reversed(compiled) if lower_level(item["runtime_level"])), None)
        if candidate is None:
            break
        old = candidate["runtime_level"]
        new = lower_level(old)
        candidate["runtime_level"] = new
        candidate["directives"] = list(records[candidate["slug"]]["compile"][new]["directives"])
        candidate["mandatory_invariants"] = [
            f"Required invariant: {value}"
            for value in records[candidate["slug"]]["compile"][new]["mandatory_invariants"]
        ]
        decisions.append({"type": "budget", "component": candidate["slug"], "decision": f"{old}-to-{new}"})
        capsule, _ = capsule_for_current()

    if estimate_tokens(capsule) > context.max_directive_tokens:
        for item in reversed(compiled):
            if not item["required"] and item["directives"]:
                item["directives"] = []
                decisions.append({"type": "budget", "component": item["slug"], "decision": "optional-directive-removed"})
                capsule, _ = capsule_for_current()
                if estimate_tokens(capsule) <= context.max_directive_tokens:
                    break
    if estimate_tokens(capsule) > context.max_directive_tokens:
        warnings.append(
            f"Minimum required runtime capsule exceeds budget: approximately {estimate_tokens(capsule)} > {context.max_directive_tokens} tokens"
        )

    capsule, final_rows = capsule_for_current()
    provenance = [
        {
            "text": restriction,
            "kind": "hard-restriction",
            "component": "task-resolution",
            "version": resolution["schema_version"],
            "runtime_form": "authority-constraint",
            "runtime_level": "source",
            "source_path": "spec/harness/TASK_RESOLUTION_SCHEMA.json",
            "selected_because": ["v0.3 resolver emitted this task-specific hard restriction"],
            "emitted": True,
            "suppression_reason": None,
        }
        for restriction in dict.fromkeys(resolution["hard_restrictions"])
    ]
    for row in final_rows:
        item = row["item"]
        provenance.append({
            "text": row["text"],
            "kind": row["kind"],
            "component": item["slug"],
            "version": item["version"],
            "runtime_form": item["runtime_form"],
            "runtime_level": item["runtime_level"],
            "source_path": item["source_path"],
            "selected_because": item["selection_reasons"],
            "emitted": row["emitted"],
            "suppression_reason": row["suppression_reason"],
        })

    plan = {
        "schema_version": "1.0.0",
        "compiler_version": COMPILER_VERSION,
        "task_resolution_hash": canonical_hash(resolution),
        "model_profile": context.model_profile,
        "host": context.host.as_dict(),
        "base_instructions_present": context.base_instructions_present,
        "task": {
            "archetype": resolution["task"].get("archetype"),
            "subtype": resolution["task"].get("subtype"),
            "execution_form": resolution["task"].get("execution_form"),
        },
        "failure_modes": resolution["failure_modes"],
        "complexity": resolution["complexity"],
        "instruction_capsule": capsule,
        "state_contract": _unique_channel(channels["state_contract"]),
        "validators": _unique_channel(channels["validators"]),
        "orchestration": _unique_channel(channels["orchestration"]),
        "tool_requirements": _unique_channel(channels["tool_requirements"]),
        "output_contract": _unique_channel(channels["output_contract"]),
        "components": [{key: value for key, value in item.items() if key not in {"directives", "mandatory_invariants", "dedupe_group"}} for item in compiled],
        "excluded_runtime_components": excluded,
        "warnings": list(dict.fromkeys(warnings)),
        "token_estimate": estimate_tokens(capsule),
        "token_estimate_approximate": True,
        "decisions": _unique_channel(decisions),
        "directive_provenance": provenance,
        "manifest_hash": "",
    }
    plan["manifest_hash"] = canonical_hash({key: value for key, value in plan.items() if key != "manifest_hash"})
    return plan
