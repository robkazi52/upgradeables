"""Compile reviewed v0.3 Upgradeable selection priors and audit artifacts."""
from __future__ import annotations

import argparse
import csv
import io
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PART_DIR = ROOT / "tools/selection_priors"
JSON_TARGET = ROOT / "registry/upgradeable_task_priors.json"
CSV_TARGET = ROOT / "audit/UPGRADEABLE_TASK_PRIOR_REVIEW_v0.3.csv"
MD_TARGET = ROOT / "audit/UPGRADEABLE_TASK_PRIOR_REVIEW_v0.3.md"

FIELDS = (
    "slug", "version", "plain_display_name", "primary_task_archetypes",
    "secondary_task_archetypes", "primary_failure_modes",
    "secondary_failure_modes", "pipeline_stages", "environment_promoters",
    "environment_demoters", "default_complexity_min",
    "default_complexity_max", "project_profile_priors",
    "normally_exclude_for", "escalates_from", "escalates_to",
    "counterbalance_notes", "source_support", "review_status", "notes",
)
PROJECT_PROFILES = {
    "general", "software-development", "research", "long-context", "authoring",
    "data-analysis", "medical-evidence", "legal-evidence", "agent-development",
    "documentation",
}


def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def ontology_sets():
    archetypes = {item["slug"] for item in load(ROOT / "registry/task_archetypes.json")["archetypes"]}
    failures = {item["slug"] for item in load(ROOT / "registry/failure_modes.json")["failure_modes"]}
    environment = load(ROOT / "registry/environment_modifiers.json")
    environment_slugs = {
        item["slug"]
        for key in ("task_environment_modifiers", "host_capabilities", "permissions", "derived_signals")
        for item in environment[key]
    }
    complexity = load(ROOT / "registry/task_complexity_levels.json")
    levels = set(complexity["ordering"])
    order = {slug: index for index, slug in enumerate(complexity["ordering"])}
    return archetypes, failures, environment_slugs, levels, order


def read_parts():
    paths = sorted(PART_DIR.glob("part-*.json"))
    records = []
    for path in paths:
        data = load(path)
        if data.get("registry_version") != "0.2.1":
            raise ValueError(f"{path}: registry_version must be 0.2.1")
        records.extend(data.get("upgradeables", []))
    return paths, sorted(records, key=lambda item: item.get("slug", ""))


def validate(records):
    errors = []
    registry = load(ROOT / "registry/registry.json")
    canonical = {item["slug"]: item for item in registry["upgradeables"]}
    archetypes, failures, environment, levels, level_order = ontology_sets()
    slugs = [item.get("slug") for item in records]
    if len(slugs) != len(set(slugs)):
        errors.append("selection-prior records contain duplicate slugs")
    missing = sorted(set(canonical) - set(slugs))
    extra = sorted(set(slugs) - set(canonical))
    if missing:
        errors.append(f"missing operational Upgradeables: {missing}")
    if extra:
        errors.append(f"unknown Upgradeables: {extra}")
    for item in records:
        slug = item.get("slug", "<missing>")
        absent = [field for field in FIELDS if field not in item]
        if absent:
            errors.append(f"{slug}: missing fields {absent}")
            continue
        if slug not in canonical:
            continue
        source = canonical[slug]
        for field in ("version", "plain_display_name", "pipeline_stages", "source_support"):
            if item[field] != source[field]:
                errors.append(f"{slug}: {field} does not match canonical registry")
        for field in (
            "primary_task_archetypes", "primary_failure_modes", "pipeline_stages",
            "environment_promoters", "environment_demoters",
            "project_profile_priors", "normally_exclude_for", "escalates_from",
            "escalates_to", "counterbalance_notes",
        ):
            if not isinstance(item[field], list):
                errors.append(f"{slug}: {field} must be an array")
        for field in ("secondary_task_archetypes", "secondary_failure_modes"):
            if not isinstance(item[field], list):
                errors.append(f"{slug}: {field} must be an array")
        for value in item["primary_task_archetypes"] + item["secondary_task_archetypes"]:
            if value not in archetypes:
                errors.append(f"{slug}: unknown task archetype {value}")
        for value in item["primary_failure_modes"] + item["secondary_failure_modes"]:
            if value not in failures:
                errors.append(f"{slug}: unknown failure mode {value}")
        for value in item["environment_promoters"] + item["environment_demoters"]:
            if value not in environment:
                errors.append(f"{slug}: unknown environment signal {value}")
        for value in item["project_profile_priors"]:
            if value not in PROJECT_PROFILES:
                errors.append(f"{slug}: unknown project profile {value}")
        for field in ("escalates_from", "escalates_to"):
            for value in item[field]:
                if value not in canonical:
                    errors.append(f"{slug}: {field} references unknown component {value}")
        minimum, maximum = item["default_complexity_min"], item["default_complexity_max"]
        if minimum not in levels or maximum not in levels:
            errors.append(f"{slug}: invalid complexity range {minimum}..{maximum}")
        elif level_order[minimum] > level_order[maximum]:
            errors.append(f"{slug}: inverted complexity range {minimum}..{maximum}")
        if item["review_status"] != "PASS":
            errors.append(f"{slug}: review_status must be PASS")
    return errors


def render_json(records):
    data = {
        "schema_version": "1.0.0",
        "registry_version": "0.2.1",
        "kind": "upgradeable-selection-priors",
        "selection_prior_disclaimer": (
            "These reviewed mappings guide candidate selection. They do not activate "
            "components or prove effectiveness. Task-time triggers, exclusions, "
            "authority, and complexity limits still apply."
        ),
        "upgradeables": records,
    }
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"


def render_csv(records):
    output = io.StringIO(newline="")
    writer = csv.DictWriter(output, fieldnames=FIELDS, lineterminator="\n")
    writer.writeheader()
    for item in records:
        writer.writerow({
            field: json.dumps(item[field], ensure_ascii=False) if isinstance(item[field], list) else item[field]
            for field in FIELDS
        })
    return output.getvalue()


def render_markdown(records):
    lines = [
        "# Upgradeable Task-Prior Review v0.3",
        "",
        "> Generated from the reviewed shards under `tools/selection_priors/`.",
        "> These are candidate-selection priors, not activation claims or evidence of efficacy.",
        "",
        f"Operational Upgradeables reviewed: **{len(records)}/96**",
        f"Missing mappings: **{96 - len(records)}**",
        f"Unreviewed: **{sum(item['review_status'] != 'PASS' for item in records)}**",
        "",
        "| Upgradeable | Primary tasks | Primary failures | Complexity | Project priors |",
        "|---|---|---|---|---|",
    ]
    for item in records:
        lines.append(
            f"| `{item['slug']}@{item['version']}` — {item['plain_display_name']} | "
            f"{', '.join(item['primary_task_archetypes'])} | "
            f"{', '.join(item['primary_failure_modes'])} | "
            f"{item['default_complexity_min']}–{item['default_complexity_max']} | "
            f"{', '.join(item['project_profile_priors']) or 'general'} |"
        )
    lines.extend(["", "For full fields and notes, use `registry/upgradeable_task_priors.json` or the CSV audit.", ""])
    return "\n".join(lines)


def outputs(records):
    return {
        JSON_TARGET: render_json(records),
        CSV_TARGET: render_csv(records),
        MD_TARGET: render_markdown(records),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    try:
        paths, records = read_parts()
        errors = validate(records)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"selection ontology build failed: {error}", file=sys.stderr)
        return 1
    if len(paths) != 3:
        errors.append(f"expected 3 selection-prior shards, found {len(paths)}")
    if errors:
        print("selection ontology build failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1
    generated = outputs(records)
    if args.check:
        stale = [path for path, content in generated.items() if not path.exists() or path.read_text(encoding="utf-8") != content]
        if stale:
            print("stale selection ontology outputs: " + ", ".join(str(path.relative_to(ROOT)) for path in stale), file=sys.stderr)
            return 1
        print(f"selection ontology build check: OK ({len(records)} reviewed Upgradeables)")
        return 0
    for path, content in generated.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
    print(f"built selection ontology audit ({len(records)} reviewed Upgradeables)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
