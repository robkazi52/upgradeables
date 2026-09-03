"""Build the compact, deterministic data snapshot used by the installed harness."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "src" / "upgradeables_harness" / "data"
MANIFEST_PATH = TARGET / "registry-manifest.json"
HARNESS_VERSION = "0.3.0"
CANONICAL_SNAPSHOT_INPUTS = (
    "registry/registry.json",
    "registry/upgradeable_task_priors.json",
    "registry/task_archetypes.json",
    "registry/task_complexity_levels.json",
    "registry/failure_modes.json",
    "registry/environment_modifiers.json",
    "registry/composition_priors.json",
    "registry/project_profiles.json",
    "recipes/recipes.json",
    "bundles",
)


def load(relative: str):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def render(data) -> str:
    return json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True) + "\n"


def git_value(*args: str) -> str | None:
    try:
        result = subprocess.run(
            ["git", *args], cwd=ROOT, capture_output=True, text=True, check=True
        )
    except (OSError, subprocess.CalledProcessError):
        return None
    value = result.stdout.strip().splitlines()
    return value[0] if value else None


def source_commit(explicit: str | None) -> str:
    if explicit:
        return explicit
    if os.environ.get("UPGRADEABLES_SOURCE_COMMIT"):
        return os.environ["UPGRADEABLES_SOURCE_COMMIT"]
    if MANIFEST_PATH.exists():
        try:
            existing = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
            if existing.get("source_commit"):
                return existing["source_commit"]
        except (OSError, json.JSONDecodeError):
            pass
    return (
        git_value("log", "-1", "--format=%H", "--", *CANONICAL_SNAPSHOT_INPUTS)
        or git_value("rev-parse", "HEAD")
        or "unknown"
    )


def compact_catalog(registry, priors, commit: str):
    prior_by_slug = {item["slug"]: item for item in priors["upgradeables"]}
    keep = (
        "id", "slug", "display_name", "plain_display_name", "plain_aliases",
        "historical_aliases", "task_phrases", "version", "purpose", "activation_class",
        "functional_classes", "os_role", "pipeline_stages", "best_fit_tasks",
        "usually_not_needed_for", "triggers", "non_triggers", "avoid_when", "requires",
        "recommended_with", "counterbalances", "conflicts", "activation_cost", "package_path",
    )
    components = []
    for item in registry["upgradeables"]:
        result = {key: item.get(key) for key in keep}
        result["selection_prior"] = prior_by_slug[item["slug"]]
        result["source_url"] = (
            "https://github.com/robkazi52/upgradeables/blob/"
            f"{commit}/{item['package_path']}"
        )
        components.append(result)
    return {
        "schema_version": "1.0.0",
        "registry_version": registry["registry_version"],
        "selection_prior_disclaimer": priors["selection_prior_disclaimer"],
        "components": components,
    }


def recipe_snapshot(registry, commit: str):
    components = {item["slug"]: item for item in registry["upgradeables"]}
    recipes = []
    for item in registry["recipes"]:
        record = dict(item)
        record["components"] = [
            {
                "slug": slug,
                "version": components[slug]["version"],
                "plain_display_name": components[slug]["plain_display_name"],
                "role": role,
            }
            for slug, role in item["classifications"].items()
        ]
        record["source_url"] = (
            "https://github.com/robkazi52/upgradeables/blob/"
            f"{commit}/recipes/{item['slug']}.md"
        )
        recipes.append(record)
    return {
        "schema_version": "1.0.0",
        "registry_version": registry["registry_version"],
        "role_semantics": {
            "R": "required-by-recipe",
            "A": "trigger-likely",
            "C": "conditional",
            "O": "optional",
            "X": "excluded",
        },
        "recipes": recipes,
    }


def ontology_snapshot():
    return {
        "schema_version": "1.0.0",
        "task_archetypes": load("registry/task_archetypes.json"),
        "task_complexity_levels": load("registry/task_complexity_levels.json"),
        "failure_modes": load("registry/failure_modes.json"),
        "environment_modifiers": load("registry/environment_modifiers.json"),
        "composition_priors": load("registry/composition_priors.json"),
    }


def aliases_snapshot(registry):
    aliases = []
    for item in registry["upgradeables"]:
        for label, kind in (
            (item["display_name"], "display-name"),
            (item["plain_display_name"], "plain-display-name"),
            *((value, "plain-alias") for value in item.get("plain_aliases", [])),
            *((value, "historical-alias") for value in item.get("historical_aliases", [])),
        ):
            aliases.append({"label": label, "slug": item["slug"], "kind": kind})
    aliases.sort(key=lambda row: (row["label"].casefold(), row["slug"], row["kind"]))
    return {"schema_version": "1.0.0", "aliases": aliases}


def validate_inputs(registry, priors, profiles):
    components = {item["slug"] for item in registry["upgradeables"]}
    recipes = {item["slug"] for item in registry["recipes"]}
    mapped = {item["slug"] for item in priors["upgradeables"]}
    if registry.get("registry_version") != "0.2.1":
        raise ValueError("canonical registry_version must be 0.2.1")
    if mapped != components:
        raise ValueError("selection-prior coverage does not match operational components")
    for recipe in registry["recipes"]:
        unknown = set(recipe["classifications"]) - components
        if unknown:
            raise ValueError(f"{recipe['slug']}: unknown components {sorted(unknown)}")
    for profile in profiles["profiles"]:
        unknown_recipes = set(profile["likely_recipes"] + profile["likely_exclusions"]) - recipes
        unknown_components = set(profile["candidate_cross_cutting"]) - components
        if unknown_recipes or unknown_components:
            raise ValueError(
                f"{profile['slug']}: unknown recipes={sorted(unknown_recipes)} "
                f"components={sorted(unknown_components)}"
            )


def payloads(commit: str):
    registry = load("registry/registry.json")
    priors = load("registry/upgradeable_task_priors.json")
    profiles = load("registry/project_profiles.json")
    validate_inputs(registry, priors, profiles)
    outputs = {
        "catalog.json": compact_catalog(registry, priors, commit),
        "recipes.json": recipe_snapshot(registry, commit),
        "profiles.json": profiles,
        "aliases.json": aliases_snapshot(registry),
        "ontology.json": ontology_snapshot(),
    }
    digest = hashlib.sha256()
    for name in sorted(outputs):
        digest.update(name.encode("utf-8"))
        digest.update(b"\0")
        digest.update(render(outputs[name]).encode("utf-8"))
    tag = git_value("tag", "--points-at", commit)
    component_schemas = {item["schema_version"] for item in registry["upgradeables"]}
    if len(component_schemas) != 1:
        raise ValueError(f"mixed component schema versions: {sorted(component_schemas)}")
    outputs["registry-manifest.json"] = {
        "schema_version": "1.0.0",
        "harness_version": HARNESS_VERSION,
        "registry_version": registry["registry_version"],
        "aggregate_registry_schema_version": registry["schema_version"],
        "component_schema_version": next(iter(component_schemas)),
        "source_commit": commit,
        "source_tag": tag,
        "snapshot_hash": f"sha256:{digest.hexdigest()}",
        "normal_operations_require_network": False,
    }
    return outputs


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    parser.add_argument("--source-commit")
    args = parser.parse_args(argv)
    try:
        outputs = payloads(source_commit(args.source_commit))
    except (OSError, KeyError, ValueError, json.JSONDecodeError) as error:
        print(f"harness data build failed: {error}", file=sys.stderr)
        return 1
    rendered = {TARGET / name: render(data) for name, data in outputs.items()}
    if args.check:
        stale = [str(path.relative_to(ROOT)) for path, text in rendered.items()
                 if not path.exists() or path.read_text(encoding="utf-8") != text]
        if stale:
            print("stale harness data: " + ", ".join(stale), file=sys.stderr)
            return 1
        print(f"harness data check: OK ({len(outputs['catalog.json']['components'])} components)")
        return 0
    TARGET.mkdir(parents=True, exist_ok=True)
    for path, text in rendered.items():
        path.write_text(text, encoding="utf-8", newline="\n")
    print(f"built harness data ({len(outputs['catalog.json']['components'])} components)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
