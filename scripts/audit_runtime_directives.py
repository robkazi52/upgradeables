#!/usr/bin/env python3
"""Fail CI when v0.4 runtime representations drift from their source contracts."""
from __future__ import annotations

import argparse
import csv
import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = Path("src/upgradeables_harness/data/catalog.json")
REGISTRY_PATH = Path("runtime/runtime_registry.json")
INSTALLED_REGISTRY_PATH = Path("src/upgradeables_harness/data/runtime-registry.json")
DEDUPE_PATH = Path("runtime/dedupe_groups.json")
AUDIT_CSV_PATH = Path("audit/UPGRADEABLE_RUNTIME_FORM_REVIEW_v0.4.csv")
AUDIT_MD_PATH = Path("audit/UPGRADEABLE_RUNTIME_FORM_REVIEW_v0.4.md")

LEVELS = ("micro", "standard", "full")
FORMS = {
    "instruction-directive",
    "state-contract",
    "validator-check",
    "orchestration-control",
    "tool-capability",
    "output-contract",
    "host-behavior",
    "mixed",
    "not-runtime-injectable",
}
CHANNELS = {
    "state_contract": "state",
    "validator_checks": "validation",
    "orchestration": "orchestration",
    "output_contract": "output",
}
PURE_CHANNEL = {
    "state-contract": "state_contract",
    "validator-check": "validator_checks",
    "orchestration-control": "orchestration",
    "tool-capability": "tool_requirements",
    "output-contract": "output_contract",
}
COMPONENT_FIELDS = {
    "schema_version",
    "slug",
    "component_version",
    "runtime_form",
    "runtime_injectable",
    "functional_classes",
    "compile",
    "validator_checks",
    "state_contract",
    "orchestration",
    "tool_requirements",
    "output_contract",
    "compile_constraints",
    "basis",
    "source_support",
    "source_path",
}
CONSTRAINT_FIELDS = {
    "minimum_complexity",
    "maximum_default_verbosity",
    "requires",
    "counterbalances",
    "do_not_combine_with",
    "dedupe_group",
    "precedence",
}
AUDIT_COLUMNS = (
    "slug",
    "version",
    "runtime_form",
    "runtime_injectable",
    "micro_directive_review",
    "standard_directive_review",
    "full_directive_review",
    "state_contract_review",
    "validator_review",
    "orchestration_review",
    "tool_requirement_review",
    "strong_model_scaling_review",
    "small_model_expansion_review",
    "conflict_review",
    "dedupe_review",
    "source_support",
    "final_status",
    "notes",
)
FINAL_STATUSES = {
    "PASS",
    "PASS_WITH_LIMITATION",
    "BLOCKED_BY_SOURCE_GAP",
    "NOT_RUNTIME_INJECTABLE",
}
LEVEL_LIMITS = {
    "micro": {"items": 1, "words": 60, "characters": 500},
    "standard": {"items": 4, "words": 140, "characters": 1200},
    "full": {"items": 10, "words": 250, "characters": 2000},
}
PRIVATE_REASONING_TARGET = re.compile(
    r"\b(?:all\s+reasoning|(?:private|hidden|internal)\s+(?:chain[- ]of[- ]thought|reasoning|deliberation)|chain[- ]of[- ]thought)\b",
    re.IGNORECASE,
)
DISCLOSURE_VERB = re.compile(
    r"\b(?:show|reveal|expose|provide|write|display|output|include|transcribe)\b",
    re.IGNORECASE,
)
NEGATION = re.compile(
    r"\b(?:do\s+not|don't|never|must\s+not|without|avoid|instead\s+of|rather\s+than)\b",
    re.IGNORECASE,
)
VAGUE_DIRECTIVES = (
    re.compile(r"\breason better\b", re.IGNORECASE),
    re.compile(r"\bthink harder\b", re.IGNORECASE),
    re.compile(r"\bbe more accurate\b", re.IGNORECASE),
)
TOOL_CLAIMS = (
    (re.compile(r"\b(?:browse|search) (?:the )?web\b", re.IGNORECASE), "web"),
    (re.compile(r"\bparallel workers?\b", re.IGNORECASE), "parallel-workers"),
    (re.compile(r"\bdurable state\b", re.IGNORECASE), "durable-state"),
    (re.compile(r"\bimage input\b", re.IGNORECASE), "image-input"),
)


def _normalize(value: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", value.casefold()))


def _strings(value: Any, label: str, errors: list[str]) -> list[str]:
    if not isinstance(value, list):
        errors.append(f"{label}: expected a list")
        return []
    result: list[str] = []
    for index, item in enumerate(value):
        if not isinstance(item, str) or not item.strip():
            errors.append(f"{label}[{index}]: expected a non-empty string")
        else:
            result.append(item.strip())
    return result


def _runtime_text(component: dict[str, Any], errors: list[str]) -> Iterable[tuple[str, str]]:
    compile_data = component.get("compile", {})
    if isinstance(compile_data, dict):
        for level in LEVELS:
            level_data = compile_data.get(level, {})
            if not isinstance(level_data, dict):
                continue
            for field in ("directives", "mandatory_invariants"):
                for index, value in enumerate(
                    _strings(level_data.get(field), f"{component.get('slug', '?')}.compile.{level}.{field}", errors)
                ):
                    yield f"compile.{level}.{field}[{index}]", value
    for field in (*CHANNELS, "tool_requirements"):
        for index, value in enumerate(_strings(component.get(field), f"{component.get('slug', '?')}.{field}", errors)):
            yield f"{field}[{index}]", value
    constraints = component.get("compile_constraints", {})
    if isinstance(constraints, dict):
        for index, value in enumerate(
            _strings(constraints.get("precedence"), f"{component.get('slug', '?')}.compile_constraints.precedence", errors)
        ):
            yield f"compile_constraints.precedence[{index}]", value


def _requests_private_reasoning(value: str) -> bool:
    for clause in re.split(r"[.;!?]\s*", value):
        target = PRIVATE_REASONING_TARGET.search(clause)
        if not target:
            continue
        prefix = clause[: target.start()]
        verbs = list(DISCLOSURE_VERB.finditer(prefix))
        if not verbs:
            continue
        verb_prefix = prefix[: verbs[-1].start()]
        guarded = NEGATION.search(prefix[-100:]) or re.search(
            r"\b(?:would|could|might|may)\s*$", verb_prefix, re.IGNORECASE
        )
        if not guarded:
            return True
    return False


def _source_supported(value: str, source_text: str) -> bool:
    normalized = _normalize(value)
    return not normalized or normalized in _normalize(source_text)


def _expected_audit_status(component: dict[str, Any]) -> str:
    if component.get("runtime_form") == "not-runtime-injectable":
        return "NOT_RUNTIME_INJECTABLE"
    if component.get("source_support") == "source-gap":
        return "PASS_WITH_LIMITATION"
    return "PASS"


def audit_data(
    *,
    root: Path,
    catalog: dict[str, Any],
    registry: dict[str, Any],
    dedupe: dict[str, Any],
    audit_rows: list[dict[str, str]],
    audit_columns: tuple[str, ...],
    installed_registry: dict[str, Any] | None,
    audit_markdown: str | None,
) -> list[str]:
    """Return stable, human-readable conformance errors for loaded runtime data."""
    errors: list[str] = []
    catalog_components = catalog.get("components")
    runtime_components = registry.get("components")
    if not isinstance(catalog_components, list):
        return ["catalog.components: expected a list"]
    if not isinstance(runtime_components, list):
        return ["runtime registry components: expected a list"]

    catalog_by_slug: dict[str, dict[str, Any]] = {}
    for item in catalog_components:
        if not isinstance(item, dict) or not isinstance(item.get("slug"), str):
            errors.append("catalog: component without a valid slug")
            continue
        slug = item["slug"]
        if slug in catalog_by_slug:
            errors.append(f"catalog: duplicate slug {slug}")
        catalog_by_slug[slug] = item

    runtime_by_slug: dict[str, dict[str, Any]] = {}
    for item in runtime_components:
        if not isinstance(item, dict) or not isinstance(item.get("slug"), str):
            errors.append("runtime registry: component without a valid slug")
            continue
        slug = item["slug"]
        if slug in runtime_by_slug:
            errors.append(f"runtime registry: duplicate slug {slug}")
        runtime_by_slug[slug] = item

    catalog_slugs = set(catalog_by_slug)
    runtime_slugs = set(runtime_by_slug)
    card_slugs = {path.stem for path in (root / "runtime/components").glob("*.md")}
    runtime_order = [item.get("slug") for item in runtime_components if isinstance(item, dict)]
    if len(catalog_slugs) != 96:
        errors.append(f"coverage: expected 96 operational packages, found {len(catalog_slugs)}")
    if registry.get("schema_version") != "1.0.0":
        errors.append("runtime registry: invalid schema_version")
    if registry.get("component_count") != len(runtime_components):
        errors.append("coverage: component_count does not match runtime component rows")
    if runtime_order != sorted(runtime_order):
        errors.append("runtime registry: component order is not deterministic by slug")
    if registry.get("registry_version") != catalog.get("registry_version"):
        errors.append("registry_version: runtime registry does not match catalog")
    if runtime_slugs != catalog_slugs:
        errors.append(
            "coverage: runtime registry mismatch "
            f"(missing={sorted(catalog_slugs - runtime_slugs)}, extra={sorted(runtime_slugs - catalog_slugs)})"
        )
    if card_slugs != catalog_slugs:
        errors.append(
            "coverage: compact-card mismatch "
            f"(missing={sorted(catalog_slugs - card_slugs)}, extra={sorted(card_slugs - catalog_slugs)})"
        )
    if installed_registry is not None and installed_registry != registry:
        errors.append("installed runtime registry differs from runtime/runtime_registry.json")

    if dedupe.get("schema_version") != "1.0.0":
        errors.append("dedupe_groups: invalid schema_version")
    if not isinstance(dedupe.get("rule"), str) or not dedupe["rule"].strip():
        errors.append("dedupe_groups: missing deterministic rule")
    groups = _strings(dedupe.get("groups"), "dedupe_groups.groups", errors)
    if len(groups) != len(set(groups)):
        errors.append("dedupe_groups.groups: duplicate group")
    group_set = set(groups)

    duplicate_directives: dict[str, list[str]] = defaultdict(list)
    for slug in sorted(runtime_slugs):
        component = runtime_by_slug[slug]
        source = catalog_by_slug.get(slug)
        prefix = slug
        missing_fields = sorted(COMPONENT_FIELDS - set(component))
        if missing_fields:
            errors.append(f"{prefix}: missing fields {missing_fields}")
        if component.get("schema_version") != "1.0.0":
            errors.append(f"{prefix}: invalid runtime representation schema_version")
        if not isinstance(component.get("basis"), str) or not component["basis"].strip():
            errors.append(f"{prefix}: missing runtime representation basis")
        if source is None:
            continue
        if component.get("component_version") != source.get("version"):
            errors.append(f"{prefix}: component version does not match catalog")
        selection = source.get("selection_prior", {})
        if component.get("source_support") != selection.get("source_support"):
            errors.append(f"{prefix}: source_support does not match catalog")
        if component.get("functional_classes") != source.get("functional_classes"):
            errors.append(f"{prefix}: functional_classes do not match catalog")

        expected_source = f"runtime/components/{slug}.md"
        source_path_value = component.get("source_path")
        if source_path_value != expected_source:
            errors.append(f"{prefix}: source_path must be {expected_source}")
        card_path = root / expected_source
        card_text = card_path.read_text(encoding="utf-8") if card_path.is_file() else ""
        if not card_text:
            errors.append(f"{prefix}: compact runtime card is missing or empty")
        expected_identity = f"`{slug}@{source.get('version')}`"
        card_heading = card_text.splitlines()[0] if card_text else ""
        if expected_identity not in card_heading:
            errors.append(f"{prefix}: compact card heading does not identify {slug}@{source.get('version')}")
        package_path_value = source.get("package_path")
        package_path = root / package_path_value if isinstance(package_path_value, str) else None
        if package_path is None or not package_path.is_file():
            errors.append(f"{prefix}: catalog source package is missing")
        else:
            expected_link = f"](../../{package_path_value})"
            if expected_link not in card_text:
                errors.append(f"{prefix}: compact card does not link to its catalog source package")
            metadata_path = package_path.parent / "metadata.yaml"
            try:
                metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError) as exc:
                errors.append(f"{prefix}: cannot load source package metadata: {exc}")
            else:
                if metadata.get("slug") != slug or metadata.get("version") != source.get("version"):
                    errors.append(f"{prefix}: source package metadata identity/version mismatch")

        form = component.get("runtime_form")
        injectable = component.get("runtime_injectable")
        if form not in FORMS:
            errors.append(f"{prefix}: invalid runtime_form {form!r}")
        if not isinstance(injectable, bool):
            errors.append(f"{prefix}: runtime_injectable must be boolean")
            injectable = False

        compile_data = component.get("compile")
        if not isinstance(compile_data, dict):
            errors.append(f"{prefix}.compile: expected an object")
            compile_data = {}
        elif set(compile_data) != set(LEVELS):
            errors.append(f"{prefix}.compile: levels must be exactly {list(LEVELS)}")
        directives: dict[str, list[str]] = {}
        invariants: dict[str, list[str]] = {}
        for level in LEVELS:
            level_data = compile_data.get(level)
            if not isinstance(level_data, dict):
                errors.append(f"{prefix}.compile.{level}: expected an object")
                level_data = {}
            elif set(level_data) != {"directives", "mandatory_invariants"}:
                errors.append(f"{prefix}.compile.{level}: invalid or missing fields")
            directives[level] = _strings(level_data.get("directives"), f"{prefix}.compile.{level}.directives", errors)
            invariants[level] = _strings(
                level_data.get("mandatory_invariants"),
                f"{prefix}.compile.{level}.mandatory_invariants",
                errors,
            )
            limits = LEVEL_LIMITS[level]
            word_count = sum(len(value.split()) for value in directives[level])
            character_count = sum(len(value) for value in directives[level])
            if len(directives[level]) > limits["items"]:
                errors.append(f"{prefix}.compile.{level}: exceeds {limits['items']} directive items")
            if word_count > limits["words"]:
                errors.append(f"{prefix}.compile.{level}: exceeds {limits['words']} words")
            if character_count > limits["characters"]:
                errors.append(f"{prefix}.compile.{level}: exceeds {limits['characters']} characters")

        if injectable:
            for level in LEVELS:
                if not directives[level]:
                    errors.append(f"{prefix}.compile.{level}: injectable component has no directive")
        elif any(directives[level] for level in LEVELS):
            errors.append(f"{prefix}: non-injectable component contains instruction directives")
        if directives["standard"][: len(directives["micro"])] != directives["micro"]:
            errors.append(f"{prefix}: micro directives are not contained in standard")
        if directives["full"][: len(directives["standard"])] != directives["standard"]:
            errors.append(f"{prefix}: standard directives are not contained in full")
        if not (invariants["micro"] == invariants["standard"] == invariants["full"]):
            errors.append(f"{prefix}: mandatory invariants differ across runtime levels")
        if injectable and len(directives["full"]) <= len(directives["micro"]):
            errors.append(f"{prefix}: full level does not expand beyond micro")

        channel_values = {
            field: _strings(component.get(field), f"{prefix}.{field}", errors)
            for field in (*CHANNELS, "tool_requirements")
        }
        if form in PURE_CHANNEL:
            expected = PURE_CHANNEL[form]
            if injectable:
                errors.append(f"{prefix}: {form} must not be directly injectable")
            if not channel_values[expected]:
                errors.append(f"{prefix}: {form} requires a non-empty {expected} channel")
            for field, values in channel_values.items():
                if field != expected and values:
                    errors.append(f"{prefix}: {form} unexpectedly populates {field}")
        elif form in {"instruction-directive", "host-behavior"}:
            if not injectable:
                errors.append(f"{prefix}: {form} must provide instruction directives")
            for field, values in channel_values.items():
                if values:
                    errors.append(f"{prefix}: {form} unexpectedly populates {field}")
        elif form == "not-runtime-injectable":
            if injectable:
                errors.append(f"{prefix}: not-runtime-injectable cannot be injectable")
            for field, values in channel_values.items():
                if values:
                    errors.append(f"{prefix}: not-runtime-injectable unexpectedly populates {field}")
        elif form == "mixed":
            populated = int(bool(directives["standard"])) + sum(bool(values) for values in channel_values.values())
            if populated < 2:
                errors.append(f"{prefix}: mixed form must populate at least two runtime channels")
            classes = set(component.get("functional_classes", []))
            for field, functional_class in CHANNELS.items():
                if bool(channel_values[field]) != (functional_class in classes):
                    errors.append(
                        f"{prefix}: mixed {field} population does not match {functional_class!r} functional class"
                    )

        constraints = component.get("compile_constraints")
        if not isinstance(constraints, dict):
            errors.append(f"{prefix}.compile_constraints: expected an object")
            constraints = {}
        missing_constraints = sorted(CONSTRAINT_FIELDS - set(constraints))
        if missing_constraints:
            errors.append(f"{prefix}: missing compile constraints {missing_constraints}")
        if constraints.get("minimum_complexity") != selection.get("default_complexity_min"):
            errors.append(f"{prefix}: minimum_complexity does not match catalog")
        if constraints.get("maximum_default_verbosity") not in LEVELS:
            errors.append(f"{prefix}: invalid maximum_default_verbosity")
        reference_fields = {
            "requires": source.get("requires", []),
            "counterbalances": source.get("counterbalances", []),
            "do_not_combine_with": source.get("conflicts", []),
        }
        for field, source_values in reference_fields.items():
            values = _strings(constraints.get(field), f"{prefix}.compile_constraints.{field}", errors)
            if values != sorted(source_values):
                errors.append(f"{prefix}: {field} does not match sorted catalog references")
            for reference in values:
                if reference == slug:
                    errors.append(f"{prefix}: {field} contains a self-reference")
                elif reference not in catalog_slugs:
                    errors.append(f"{prefix}: {field} references unknown component {reference}")
        dedupe_group = constraints.get("dedupe_group")
        if dedupe_group is not None and dedupe_group not in group_set:
            errors.append(f"{prefix}: unknown dedupe group {dedupe_group!r}")
        precedence = _strings(constraints.get("precedence"), f"{prefix}.compile_constraints.precedence", errors)
        if not precedence:
            errors.append(f"{prefix}: conflict/precedence review has no rule")

        source_checked_fields = {
            "state_contract",
            "validator_checks",
            "orchestration",
            "output_contract",
            "compile_constraints.precedence",
        }
        for location, value in _runtime_text(component, errors):
            if location.startswith("tool_requirements"):
                continue
            if location.startswith("compile.") or any(location.startswith(name) for name in source_checked_fields):
                if card_text and not _source_supported(value, card_text):
                    errors.append(f"{prefix}.{location}: text is not supported by the compact runtime card")
            if _requests_private_reasoning(value):
                errors.append(f"{prefix}.{location}: requests disclosure of private reasoning")
            if any(pattern.search(value) for pattern in VAGUE_DIRECTIVES):
                errors.append(f"{prefix}.{location}: contains a vague generic directive")

        tool_requirements = set(channel_values["tool_requirements"])
        for level in LEVELS:
            for value in directives[level]:
                for pattern, requirement in TOOL_CLAIMS:
                    if pattern.search(value) and requirement not in tool_requirements:
                        errors.append(f"{prefix}.compile.{level}: claims {requirement} without a tool requirement")
                normalized = _normalize(value)
                if normalized:
                    duplicate_directives[normalized].append(f"{prefix}:{level}")

    for appearances in duplicate_directives.values():
        slugs = {item.split(":", 1)[0] for item in appearances}
        if len(slugs) > 1:
            errors.append(f"duplicate directive across components: {sorted(appearances)}")

    if audit_columns != AUDIT_COLUMNS:
        errors.append(f"audit CSV columns must be exactly {list(AUDIT_COLUMNS)}")
    rows_by_slug: dict[str, dict[str, str]] = {}
    for index, row in enumerate(audit_rows, start=2):
        slug = row.get("slug", "")
        if not slug:
            errors.append(f"audit row {index}: missing slug")
            continue
        if slug in rows_by_slug:
            errors.append(f"audit CSV: duplicate slug {slug}")
        rows_by_slug[slug] = row
        for column in AUDIT_COLUMNS:
            value = row.get(column)
            if value is None or not value.strip():
                errors.append(f"{slug}: audit column {column} is empty")
        if row.get("final_status") not in FINAL_STATUSES:
            errors.append(f"{slug}: invalid audit final_status {row.get('final_status')!r}")

    audit_slugs = set(rows_by_slug)
    audit_order = [row.get("slug", "") for row in audit_rows]
    if audit_order != sorted(audit_order):
        errors.append("audit CSV: row order is not deterministic by slug")
    if audit_slugs != catalog_slugs:
        errors.append(
            "coverage: audit CSV mismatch "
            f"(missing={sorted(catalog_slugs - audit_slugs)}, extra={sorted(audit_slugs - catalog_slugs)})"
        )
    for slug in sorted(runtime_slugs & audit_slugs):
        component = runtime_by_slug[slug]
        row = rows_by_slug[slug]
        expected = {
            "version": str(component.get("component_version", "")),
            "runtime_form": str(component.get("runtime_form", "")),
            "runtime_injectable": str(bool(component.get("runtime_injectable"))).lower(),
            "micro_directive_review": "PASS" if component.get("runtime_injectable") else "N/A",
            "standard_directive_review": "PASS" if component.get("runtime_injectable") else "N/A",
            "full_directive_review": "PASS" if component.get("runtime_injectable") else "N/A",
            "state_contract_review": "PASS" if component.get("state_contract") else "N/A",
            "validator_review": "PASS" if component.get("validator_checks") else "N/A",
            "orchestration_review": "PASS" if component.get("orchestration") else "N/A",
            "tool_requirement_review": "PASS" if component.get("tool_requirements") else "N/A",
            "strong_model_scaling_review": "PASS",
            "small_model_expansion_review": "PASS" if component.get("runtime_injectable") else "N/A",
            "conflict_review": "PASS",
            "dedupe_review": "PASS" if component.get("compile_constraints", {}).get("dedupe_group") else "N/A",
            "source_support": str(component.get("source_support", "")),
            "final_status": _expected_audit_status(component),
        }
        for column, value in expected.items():
            if row.get(column) != value:
                errors.append(f"{slug}: audit {column} is {row.get(column)!r}, expected {value!r}")

    if audit_markdown is not None:
        expected_summary = (
            f"- Baseline: {len(catalog_slugs)}",
            f"- Reviewed: {len(audit_rows)}",
            "- Missing: 0",
            "- Unreviewed: 0",
        )
        for line in expected_summary:
            if line not in audit_markdown:
                errors.append(f"audit markdown: missing summary line {line!r}")

    return sorted(set(errors))


def _load_json(path: Path, errors: list[str]) -> dict[str, Any] | None:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{path}: cannot load JSON: {exc}")
        return None
    if not isinstance(value, dict):
        errors.append(f"{path}: expected a JSON object")
        return None
    return value


def audit_repository(root: Path = ROOT) -> list[str]:
    """Load and audit repository artifacts without modifying them."""
    load_errors: list[str] = []
    catalog = _load_json(root / CATALOG_PATH, load_errors)
    registry = _load_json(root / REGISTRY_PATH, load_errors)
    installed = _load_json(root / INSTALLED_REGISTRY_PATH, load_errors)
    dedupe = _load_json(root / DEDUPE_PATH, load_errors)
    try:
        with (root / AUDIT_CSV_PATH).open(encoding="utf-8", newline="") as handle:
            reader = csv.DictReader(handle)
            audit_columns = tuple(reader.fieldnames or ())
            audit_rows = list(reader)
    except OSError as exc:
        load_errors.append(f"{root / AUDIT_CSV_PATH}: cannot load CSV: {exc}")
        audit_columns = ()
        audit_rows = []
    try:
        audit_markdown = (root / AUDIT_MD_PATH).read_text(encoding="utf-8")
    except OSError as exc:
        load_errors.append(f"{root / AUDIT_MD_PATH}: cannot load Markdown: {exc}")
        audit_markdown = None
    if load_errors or catalog is None or registry is None or installed is None or dedupe is None:
        return sorted(set(load_errors))
    return audit_data(
        root=root,
        catalog=catalog,
        registry=registry,
        dedupe=dedupe,
        audit_rows=audit_rows,
        audit_columns=audit_columns,
        installed_registry=installed,
        audit_markdown=audit_markdown,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check",
        action="store_true",
        help="verify all generated runtime representations and audit rows without writing files",
    )
    parser.parse_args()
    errors = audit_repository()
    if errors:
        print("runtime directive audit: FAILED", file=sys.stderr)
        for error in errors:
            print("- " + error, file=sys.stderr)
        return 1
    print("runtime directive audit: OK (96 packages, 0 unreviewed)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
