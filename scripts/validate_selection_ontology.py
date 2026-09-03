"""Validate the research-first v0.3 selection ontology and its generated audit."""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]

ONTOLOGY_PATHS = {
    "task archetypes": "registry/task_archetypes.json",
    "failure modes": "registry/failure_modes.json",
    "environment modifiers": "registry/environment_modifiers.json",
    "complexity levels": "registry/task_complexity_levels.json",
    "composition priors": "registry/composition_priors.json",
}
SOURCE_NOTES = {
    "A": "research/source-notes/general-agent-task-taxonomy.md",
    "B": "research/source-notes/software-agent-tasks.md",
    "C": "research/source-notes/research-and-knowledge-tasks.md",
    "D": "research/source-notes/long-context-and-stateful-work.md",
    "E": "research/source-notes/tool-use-and-action-workflows.md",
    "F": "research/source-notes/planning-decision-and-reasoning.md",
    "G": "research/source-notes/high-stakes-and-validation.md",
    "H": "research/source-notes/skills-and-recurring-workflows.md",
}
EVIDENCE_COLUMNS = (
    "source",
    "source_type",
    "date_accessed",
    "task_domain",
    "claim_or_pattern",
    "supports_archetype",
    "supports_failure_mode",
    "supports_environment_modifier",
    "notes",
)
PRIOR_FIELDS = (
    "slug",
    "version",
    "plain_display_name",
    "primary_task_archetypes",
    "secondary_task_archetypes",
    "primary_failure_modes",
    "secondary_failure_modes",
    "pipeline_stages",
    "environment_promoters",
    "environment_demoters",
    "default_complexity_min",
    "default_complexity_max",
    "project_profile_priors",
    "normally_exclude_for",
    "escalates_from",
    "escalates_to",
    "counterbalance_notes",
    "source_support",
    "review_status",
    "notes",
)
GENERATED_PATHS = (
    "registry/upgradeable_task_priors.json",
    "audit/UPGRADEABLE_TASK_PRIOR_REVIEW_v0.3.csv",
    "audit/UPGRADEABLE_TASK_PRIOR_REVIEW_v0.3.md",
)
RESEARCH_GATE_PATH = "audit/SELECTION_ONTOLOGY_REVIEW_v0.3.md"
EXTERNAL_SOURCE = re.compile(r"https?://", re.IGNORECASE)
TRACK_PREFIX = re.compile(r"^\s*([A-H])(?:\b|[\s:_-])", re.IGNORECASE)


def _load_json(root: Path, relative: str, errors: list[str]) -> dict[str, Any] | None:
    path = root / relative
    if not path.is_file():
        errors.append(f"missing required JSON: {relative}")
        return None
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        errors.append(f"invalid JSON in {relative}: {error}")
        return None
    if not isinstance(value, dict):
        errors.append(f"{relative}: top level must be an object")
        return None
    return value


def _items(
    data: dict[str, Any], key: str, label: str, errors: list[str]
) -> list[dict[str, Any]]:
    value = data.get(key)
    if not isinstance(value, list) or not all(isinstance(item, dict) for item in value):
        errors.append(f"{label}: {key} must be an array of objects")
        return []
    return value


def _unique_slugs(items: list[dict[str, Any]], label: str, errors: list[str]) -> set[str]:
    slugs = [item.get("slug") for item in items]
    invalid = [slug for slug in slugs if not isinstance(slug, str) or not slug]
    if invalid:
        errors.append(f"{label}: every record needs a nonempty string slug")
    strings = [slug for slug in slugs if isinstance(slug, str) and slug]
    duplicates = sorted({slug for slug in strings if strings.count(slug) > 1})
    if duplicates:
        errors.append(f"{label}: duplicate slugs: {duplicates}")
    return set(strings)


def _check_refs(
    values: Any, known: set[str], location: str, errors: list[str]
) -> None:
    if not isinstance(values, list) or not all(isinstance(value, str) for value in values):
        errors.append(f"{location}: must be an array of strings")
        return
    unknown = sorted(set(values) - known)
    if unknown:
        errors.append(f"{location}: undefined references: {unknown}")


def _condition_values(condition: Any, location: str, errors: list[str]):
    """Yield structured predicates while validating recursive all/any syntax."""
    if not isinstance(condition, dict):
        errors.append(f"{location}: condition must be an object")
        return
    if condition.get("always") is True and len(condition) == 1:
        return
    group_keys = [key for key in ("all", "any") if key in condition]
    if group_keys:
        if len(group_keys) != 1 or len(condition) != 1:
            errors.append(f"{location}: grouped condition must contain exactly one of all/any")
            return
        children = condition[group_keys[0]]
        if not isinstance(children, list) or not children:
            errors.append(f"{location}.{group_keys[0]}: must be a nonempty array")
            return
        for index, child in enumerate(children):
            yield from _condition_values(child, f"{location}.{group_keys[0]}[{index}]", errors)
        return
    if set(condition) != {"field", "op", "value"}:
        errors.append(f"{location}: predicate requires exactly field, op, and value")
        return
    if not isinstance(condition["field"], str) or not isinstance(condition["op"], str):
        errors.append(f"{location}: field and op must be strings")
        return
    yield condition


def _check_evidence(root: Path, errors: list[str]) -> None:
    matrix = root / "research/EVIDENCE_MATRIX.csv"
    if not matrix.is_file():
        errors.append("missing research/EVIDENCE_MATRIX.csv")
    else:
        try:
            with matrix.open(encoding="utf-8-sig", newline="") as handle:
                reader = csv.DictReader(handle)
                header = reader.fieldnames or []
                rows = list(reader)
        except (OSError, UnicodeError, csv.Error) as error:
            errors.append(f"cannot read research/EVIDENCE_MATRIX.csv: {error}")
        else:
            missing = [column for column in EVIDENCE_COLUMNS if column not in header]
            if missing:
                errors.append(f"research/EVIDENCE_MATRIX.csv: missing columns {missing}")
            covered = {
                match.group(1).upper()
                for row in rows
                if (match := TRACK_PREFIX.match(row.get("task_domain", "")))
            }
            missing_tracks = sorted(set(SOURCE_NOTES) - covered)
            if missing_tracks:
                errors.append(
                    "research/EVIDENCE_MATRIX.csv: no evidence rows for tracks "
                    + ", ".join(missing_tracks)
                )
    for track, relative in SOURCE_NOTES.items():
        path = root / relative
        if not path.is_file():
            errors.append(f"track {track}: missing source note {relative}")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            errors.append(f"track {track}: cannot read {relative}: {error}")
            continue
        if not EXTERNAL_SOURCE.search(text):
            errors.append(f"track {track}: {relative} contains no external http(s) source")


def _check_composition(
    composition: dict[str, Any],
    archetypes: set[str],
    execution_forms: set[str],
    environment_by_namespace: dict[str, set[str]],
    levels: set[str],
    level_order: dict[str, int],
    recipes: set[str],
    components: set[str],
    errors: list[str],
) -> None:
    matching_semantics = composition.get("matching_semantics")
    if not isinstance(matching_semantics, dict):
        errors.append("composition priors: matching_semantics must be an object")
        matching_semantics = {}
    local_derived = matching_semantics.get("derived_signals", {})
    local_derived_slugs: set[str] = set()
    if not isinstance(local_derived, dict):
        errors.append("composition priors: matching_semantics.derived_signals must be an object")
    else:
        for slug, definition in local_derived.items():
            location = f"composition priors: local derived signal {slug!r}"
            if not isinstance(slug, str) or not slug:
                errors.append(f"{location}: slug must be a nonempty string")
                continue
            if not isinstance(definition, dict):
                errors.append(f"{location}: definition must be an object")
                continue
            if definition.get("type") != "tri_state":
                errors.append(f"{location}: type must be tri_state")
            if not isinstance(definition.get("derive_only_when"), str) or not definition["derive_only_when"].strip():
                errors.append(f"{location}: derive_only_when must be a nonempty string")
            inputs = definition.get("required_inputs")
            if not isinstance(inputs, list) or not inputs or not all(
                isinstance(value, str) and value for value in inputs
            ):
                errors.append(f"{location}: required_inputs must be a nonempty string array")
            local_derived_slugs.add(slug)
    environment_by_namespace = dict(environment_by_namespace)
    environment_by_namespace["derived"] = (
        set(environment_by_namespace.get("derived", set())) | local_derived_slugs
    )
    rules = _items(composition, "rules", "composition priors", errors)
    rule_ids = {item.get("id") for item in rules if isinstance(item.get("id"), str)}
    operators = set(matching_semantics.get("operators", []))
    for rule in rules:
        rule_id = rule.get("id", "<missing-id>")
        inherited = rule.get("inherits")
        if inherited is not None and inherited not in rule_ids:
            errors.append(f"composition rule {rule_id}: undefined inherits target {inherited!r}")
        for predicate in _condition_values(rule.get("when"), f"composition rule {rule_id}.when", errors):
            field, op, value = predicate["field"], predicate["op"], predicate["value"]
            if operators and op not in operators:
                errors.append(f"composition rule {rule_id}: unsupported operator {op!r}")
            values = value if isinstance(value, list) else [value]
            if field == "task.archetype":
                unknown = sorted({entry for entry in values if isinstance(entry, str)} - archetypes)
                if unknown:
                    errors.append(f"composition rule {rule_id}: undefined archetypes {unknown}")
            elif field == "task.execution_form":
                unknown = sorted({entry for entry in values if isinstance(entry, str)} - execution_forms)
                if unknown:
                    errors.append(f"composition rule {rule_id}: undefined execution forms {unknown}")
            elif "." in field:
                namespace, slug = field.split(".", 1)
                if namespace in environment_by_namespace and slug not in environment_by_namespace[namespace]:
                    errors.append(f"composition rule {rule_id}: undefined {namespace} signal {slug!r}")
        effects = rule.get("effects")
        if not isinstance(effects, dict):
            errors.append(f"composition rule {rule_id}: effects must be an object")
            continue
        candidate_recipes = effects.get("candidate_recipes", {})
        if isinstance(candidate_recipes, dict):
            for key in ("promote", "conditional", "exclude"):
                if key in candidate_recipes:
                    _check_refs(
                        candidate_recipes[key], recipes,
                        f"composition rule {rule_id}.candidate_recipes.{key}", errors,
                    )
        elif candidate_recipes:
            errors.append(f"composition rule {rule_id}.candidate_recipes: must be an object")
        component_effects = effects.get("components", {})
        if isinstance(component_effects, dict):
            for key in ("promote", "conditional", "demote", "hard_exclude"):
                if key in component_effects:
                    _check_refs(
                        component_effects[key], components,
                        f"composition rule {rule_id}.components.{key}", errors,
                    )
        elif component_effects:
            errors.append(f"composition rule {rule_id}.components: must be an object")
        complexity = effects.get("complexity", {})
        if isinstance(complexity, dict):
            floor, ceiling = complexity.get("floor"), complexity.get("ceiling")
            for key, value in (("floor", floor), ("ceiling", ceiling)):
                if value is not None and value not in levels:
                    errors.append(f"composition rule {rule_id}: undefined complexity {key} {value!r}")
            if floor in levels and ceiling in levels and level_order[floor] > level_order[ceiling]:
                errors.append(f"composition rule {rule_id}: inverted complexity range {floor}..{ceiling}")
        elif complexity:
            errors.append(f"composition rule {rule_id}.complexity: must be an object")


def _check_prior_records(
    records: list[dict[str, Any]],
    canonical: dict[str, dict[str, Any]],
    archetypes: set[str],
    failures: set[str],
    environment: set[str],
    levels: set[str],
    level_order: dict[str, int],
    profiles: set[str],
    errors: list[str],
) -> None:
    if len(canonical) != 96:
        errors.append(f"canonical registry: expected 96 operational Upgradeables, found {len(canonical)}")
    slugs = [item.get("slug") for item in records]
    duplicates = sorted({slug for slug in slugs if isinstance(slug, str) and slugs.count(slug) > 1})
    if duplicates:
        errors.append(f"upgradeable task priors: duplicate slugs {duplicates}")
    present = {slug for slug in slugs if isinstance(slug, str)}
    missing = sorted(set(canonical) - present)
    extra = sorted(present - set(canonical))
    if len(records) != 96 or missing or extra:
        errors.append(
            f"upgradeable task priors: expected exactly-once coverage of 96; "
            f"found {len(records)}, missing={missing}, extra={extra}"
        )
    array_fields = {
        "primary_task_archetypes", "secondary_task_archetypes",
        "primary_failure_modes", "secondary_failure_modes", "pipeline_stages",
        "environment_promoters", "environment_demoters", "project_profile_priors",
        "normally_exclude_for", "escalates_from", "escalates_to",
    }
    for item in records:
        slug = item.get("slug", "<missing-slug>")
        absent = [field for field in PRIOR_FIELDS if field not in item]
        if absent:
            errors.append(f"upgradeable task prior {slug}: missing fields {absent}")
            continue
        for field in array_fields:
            if not isinstance(item[field], list) or not all(isinstance(value, str) for value in item[field]):
                errors.append(f"upgradeable task prior {slug}.{field}: must be an array of strings")
        counterbalances = item["counterbalance_notes"]
        if not isinstance(counterbalances, list):
            errors.append(f"upgradeable task prior {slug}.counterbalance_notes: must be an array")
        else:
            for index, note in enumerate(counterbalances):
                location = f"upgradeable task prior {slug}.counterbalance_notes[{index}]"
                if isinstance(note, str):
                    if not note.strip():
                        errors.append(f"{location}: string note must be nonempty")
                elif isinstance(note, dict):
                    note_slug, reason = note.get("slug"), note.get("reason")
                    if note_slug not in canonical:
                        errors.append(f"{location}: undefined component slug {note_slug!r}")
                    if not isinstance(reason, str) or not reason.strip():
                        errors.append(f"{location}: reason must be a nonempty string")
                else:
                    errors.append(
                        f"{location}: must be a nonempty string or a component slug/reason object"
                    )
        if slug not in canonical:
            continue
        source = canonical[slug]
        for field in ("version", "plain_display_name", "pipeline_stages", "source_support"):
            if item[field] != source.get(field):
                errors.append(f"upgradeable task prior {slug}: {field} differs from canonical registry")
        _check_refs(item["primary_task_archetypes"], archetypes, f"{slug}.primary_task_archetypes", errors)
        _check_refs(item["secondary_task_archetypes"], archetypes, f"{slug}.secondary_task_archetypes", errors)
        _check_refs(item["normally_exclude_for"], archetypes, f"{slug}.normally_exclude_for", errors)
        _check_refs(item["primary_failure_modes"], failures, f"{slug}.primary_failure_modes", errors)
        _check_refs(item["secondary_failure_modes"], failures, f"{slug}.secondary_failure_modes", errors)
        _check_refs(item["environment_promoters"], environment, f"{slug}.environment_promoters", errors)
        _check_refs(item["environment_demoters"], environment, f"{slug}.environment_demoters", errors)
        _check_refs(item["project_profile_priors"], profiles, f"{slug}.project_profile_priors", errors)
        _check_refs(item["escalates_from"], set(canonical), f"{slug}.escalates_from", errors)
        _check_refs(item["escalates_to"], set(canonical), f"{slug}.escalates_to", errors)
        minimum, maximum = item["default_complexity_min"], item["default_complexity_max"]
        if minimum not in levels or maximum not in levels:
            errors.append(f"upgradeable task prior {slug}: invalid complexity range {minimum}..{maximum}")
        elif level_order[minimum] > level_order[maximum]:
            errors.append(f"upgradeable task prior {slug}: inverted complexity range {minimum}..{maximum}")
        if item["review_status"] != "PASS":
            errors.append(f"upgradeable task prior {slug}: review_status must be PASS")


def _check_csv_parity(
    root: Path, records: list[dict[str, Any]], errors: list[str]
) -> None:
    relative = "audit/UPGRADEABLE_TASK_PRIOR_REVIEW_v0.3.csv"
    path = root / relative
    if not path.is_file():
        return
    try:
        with path.open(encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            header = reader.fieldnames or []
            rows = list(reader)
    except (OSError, UnicodeError, csv.Error) as error:
        errors.append(f"cannot read {relative}: {error}")
        return
    if header != list(PRIOR_FIELDS):
        errors.append(f"{relative}: header does not match required prior fields")
    json_by_slug = {item.get("slug"): item for item in records if isinstance(item.get("slug"), str)}
    csv_slugs = [row.get("slug", "") for row in rows]
    if len(rows) != len(records) or set(csv_slugs) != set(json_by_slug):
        errors.append(f"{relative}: row set does not match registry/upgradeable_task_priors.json")
        return
    if len(csv_slugs) != len(set(csv_slugs)):
        errors.append(f"{relative}: duplicate slug rows")
        return
    for row in rows:
        slug = row["slug"]
        expected = json_by_slug[slug]
        for field in PRIOR_FIELDS:
            raw = row.get(field, "")
            if isinstance(expected.get(field), list):
                try:
                    actual = json.loads(raw)
                except json.JSONDecodeError:
                    errors.append(f"{relative}: {slug}.{field} is not a JSON array")
                    continue
            else:
                actual = raw
            if actual != expected.get(field):
                errors.append(f"{relative}: {slug}.{field} differs from generated JSON")


def validate(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    canonical_data = _load_json(root, "registry/registry.json", errors)
    ontology = {
        name: _load_json(root, relative, errors)
        for name, relative in ONTOLOGY_PATHS.items()
    }
    _check_evidence(root, errors)
    if canonical_data is None or any(data is None for data in ontology.values()):
        return errors

    task_data = ontology["task archetypes"]
    failure_data = ontology["failure modes"]
    environment_data = ontology["environment modifiers"]
    complexity_data = ontology["complexity levels"]
    composition_data = ontology["composition priors"]
    assert task_data and failure_data and environment_data and complexity_data and composition_data

    canonical_items = _items(canonical_data, "upgradeables", "canonical registry", errors)
    canonical = {item["slug"]: item for item in canonical_items if isinstance(item.get("slug"), str)}
    component_slugs = set(canonical)
    for key in ("qms_modes", "behavior_genes", "cores", "domain_os"):
        component_slugs |= _unique_slugs(
            _items(canonical_data, key, "canonical registry", errors),
            f"canonical registry.{key}", errors,
        )
    recipes = _items(canonical_data, "recipes", "canonical registry", errors)
    recipe_slugs = _unique_slugs(recipes, "canonical recipes", errors)
    for recipe in recipes:
        classifications = recipe.get("classifications")
        if not isinstance(classifications, dict):
            errors.append(
                f"recipe {recipe.get('slug', '<missing>')}.classifications: "
                "must be a component-to-role object"
            )
        else:
            unknown = sorted(set(classifications) - component_slugs)
            if unknown:
                errors.append(
                    f"recipe {recipe.get('slug', '<missing>')}.classifications: "
                    f"undefined component references: {unknown}"
                )

    archetype_items = _items(task_data, "archetypes", "task archetypes", errors)
    archetypes = _unique_slugs(archetype_items, "task archetypes", errors)
    execution_items = _items(task_data, "execution_forms", "task archetypes", errors)
    execution_forms = _unique_slugs(execution_items, "execution forms", errors)
    profiles = {
        profile
        for item in archetype_items
        for profile in item.get("likely_project_profiles", [])
        if isinstance(profile, str)
    }

    failure_items = _items(failure_data, "failure_modes", "failure modes", errors)
    failures = _unique_slugs(failure_items, "failure modes", errors)
    environment_keys = (
        "task_environment_modifiers", "host_capabilities", "permissions", "derived_signals"
    )
    environment_items = {
        key: _items(environment_data, key, "environment modifiers", errors)
        for key in environment_keys
    }
    environment_sets = {
        key: _unique_slugs(items, f"environment modifiers.{key}", errors)
        for key, items in environment_items.items()
    }
    all_environment = set().union(*environment_sets.values())
    if sum(map(len, environment_sets.values())) != len(all_environment):
        errors.append("environment modifiers: slugs overlap between modifier/capability/permission/derived categories")

    expected_order = ["L0", "L1", "L2", "L3", "L4", "L5"]
    ordering = complexity_data.get("ordering")
    if ordering != expected_order:
        errors.append(f"complexity levels: ordering must be exactly {expected_order}, found {ordering!r}")
    level_items = _items(complexity_data, "levels", "complexity levels", errors)
    level_slugs = [item.get("slug") for item in level_items]
    if level_slugs != expected_order:
        errors.append(f"complexity levels: level records must appear exactly as {expected_order}")
    levels = set(expected_order)
    level_order = {slug: index for index, slug in enumerate(expected_order)}

    for item in archetype_items:
        slug = item.get("slug", "<missing>")
        _check_refs(item.get("common_failure_modes"), failures, f"task archetype {slug}.common_failure_modes", errors)
        _check_refs(item.get("candidate_recipes"), recipe_slugs, f"task archetype {slug}.candidate_recipes", errors)
        _check_refs(item.get("normally_excluded_recipes"), recipe_slugs, f"task archetype {slug}.normally_excluded_recipes", errors)
        _check_refs(item.get("environment_modifiers"), all_environment, f"task archetype {slug}.environment_modifiers", errors)
        _check_refs(item.get("compatible_execution_forms"), execution_forms, f"task archetype {slug}.compatible_execution_forms", errors)
        for field in ("default_complexity_floor", "default_complexity_ceiling"):
            if item.get(field) not in levels:
                errors.append(f"task archetype {slug}: undefined {field} {item.get(field)!r}")

    control_fields = (
        "primary_controls", "secondary_controls", "counterbalances",
        "normally_unnecessary_controls",
    )
    for item in failure_items:
        slug = item.get("slug", "<missing>")
        _check_refs(item.get("common_task_archetypes"), archetypes, f"failure mode {slug}.common_task_archetypes", errors)
        for field in control_fields:
            _check_refs(item.get(field), component_slugs, f"failure mode {slug}.{field}", errors)

    namespace_map = {
        "modifiers": environment_sets["task_environment_modifiers"],
        "capabilities": environment_sets["host_capabilities"],
        "permissions": environment_sets["permissions"],
        "derived": environment_sets["derived_signals"],
    }
    for key, items in environment_items.items():
        for item in items:
            slug = item.get("slug", "<missing>")
            for field in ("promote_components", "demote_components", "exclude_components"):
                _check_refs(item.get(field), component_slugs, f"environment {slug}.{field}", errors)
            ranking = item.get("recipe_ranking")
            if not isinstance(ranking, dict):
                errors.append(f"environment {slug}.recipe_ranking: must be an object")
            else:
                for field in ("promote", "demote"):
                    _check_refs(ranking.get(field), recipe_slugs, f"environment {slug}.recipe_ranking.{field}", errors)

    bounds = complexity_data.get("archetype_bounds")
    if not isinstance(bounds, dict):
        errors.append("complexity levels: archetype_bounds must be an object")
    else:
        if set(bounds) != archetypes:
            errors.append(
                "complexity levels: archetype_bounds keys differ from task archetypes; "
                f"missing={sorted(archetypes - set(bounds))}, extra={sorted(set(bounds) - archetypes)}"
            )
        by_archetype = {item["slug"]: item for item in archetype_items if item.get("slug") in archetypes}
        for slug in set(bounds) & archetypes:
            bound = bounds[slug]
            if not isinstance(bound, dict):
                errors.append(f"complexity levels: archetype_bounds.{slug} must be an object")
                continue
            for field in ("default_complexity_floor", "default_complexity_ceiling"):
                if bound.get(field) != by_archetype[slug].get(field):
                    errors.append(f"complexity levels: {slug}.{field} differs from task archetype registry")

    _check_composition(
        composition_data, archetypes, execution_forms, namespace_map,
        levels, level_order, recipe_slugs, component_slugs, errors,
    )

    priors = _load_json(root, GENERATED_PATHS[0], errors)
    records: list[dict[str, Any]] = []
    if priors is not None:
        records = _items(priors, "upgradeables", "upgradeable task priors", errors)
        _check_prior_records(
            records, canonical, archetypes, failures, all_environment,
            levels, level_order, profiles, errors,
        )
    for relative in GENERATED_PATHS[1:]:
        if not (root / relative).is_file():
            errors.append(f"missing generated selection-ontology artifact: {relative}")
    if priors is not None:
        _check_csv_parity(root, records, errors)

    gate_path = root / RESEARCH_GATE_PATH
    if not gate_path.is_file():
        errors.append(f"missing research-gate audit: {RESEARCH_GATE_PATH}")
    else:
        try:
            gate_text = gate_path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as error:
            errors.append(f"cannot read {RESEARCH_GATE_PATH}: {error}")
        else:
            if "RESEARCH_GATE = PASS" not in gate_text:
                errors.append(f"{RESEARCH_GATE_PATH}: missing literal RESEARCH_GATE = PASS")
    return errors


def main() -> int:
    errors = validate()
    if errors:
        print(f"selection ontology validation failed ({len(errors)} issue(s)):", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    print("selection ontology validation: OK (5 registries, 8 research tracks, 96 reviewed Upgradeables)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
