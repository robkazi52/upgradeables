"""Dependency-free semantic validation for the Upgradeables registry."""
from __future__ import annotations
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ALLOWED_RECOVERY = {"exact_recovery", "partial_recovery", "family_recovery", "historical_artifact", "unresolved", "modern_inference"}
ALLOWED_LIFECYCLE = {"historical", "unresolved", "experimental", "candidate", "stable", "core", "deprecated"}
ALLOWED_ACTIVATION = {"U0-foundational", "U1-common-conditional", "U2-specialized", "U3-high-risk-expensive", "U4-meta-architecture"}
ALLOWED_FUNCTIONS = {"framing-intake", "state", "context-retrieval", "planning-reasoning", "truth-grounding", "validation", "drift-control", "editing-repair", "output", "orchestration", "meta-control", "persistence"}
ALLOWED_SOURCE_KINDS = {"direct_user_spec", "user_accepted", "historical_assistant_artifact", "current_consolidated_catalog", "historical_recovery_inventory", "modern_implementation_recommendation"}
ALLOWED_CANONICALITY = {"canonical", "accepted", "provisional", "historical_only", "unresolved"}
ALLOWED_CONFIDENCE = {"high", "medium", "low"}
REQUIRED = {"id", "slug", "display_name", "version", "registry_generation", "recovery_status", "lifecycle_status", "tiers", "functional_classes", "activation_class", "implementation_forms", "purpose", "triggers", "non_triggers", "requires", "recommended_with", "counterbalances", "potentially_redundant_with", "conflicts", "inputs", "outputs", "strong_model_scaling", "failure_boundary", "supersedes", "superseded_by", "package_path", "provenance"}

def load(path):
    return json.loads(path.read_text(encoding="utf-8"))

def validate():
    errors = []
    yaml_data = load(ROOT / "registry/registry.yaml")
    json_data = load(ROOT / "registry/registry.json")
    if yaml_data != json_data:
        errors.append("registry YAML/JSON divergence")
    entries = json_data.get("upgradeables", [])
    slugs = [entry.get("slug") for entry in entries]
    ids = [entry.get("id") for entry in entries]
    if len(slugs) != len(set(slugs)):
        errors.append("duplicate canonical slug")
    if len(ids) != len(set(ids)):
        errors.append("duplicate canonical ID")
    known = set(slugs)
    aliases = {}
    for entry in entries:
        missing = REQUIRED - set(entry)
        if missing:
            errors.append(f"{entry.get('slug')}: missing {sorted(missing)}")
        slug = entry.get("slug", "")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
            errors.append(f"{slug}: invalid slug")
        if entry.get("recovery_status") not in ALLOWED_RECOVERY:
            errors.append(f"{slug}: invalid recovery status")
        if entry.get("lifecycle_status") not in ALLOWED_LIFECYCLE:
            errors.append(f"{slug}: invalid lifecycle")
        if entry.get("activation_class") not in ALLOWED_ACTIVATION:
            errors.append(f"{slug}: invalid activation class")
        if not set(entry.get("functional_classes", [])) <= ALLOWED_FUNCTIONS:
            errors.append(f"{slug}: invalid functional class")
        package = ROOT / entry.get("package_path", "__missing__")
        raw_package = Path(entry.get("package_path", ""))
        if raw_package.is_absolute() or ".." in raw_package.parts:
            errors.append(f"{slug}: unsafe package path {entry.get('package_path')}")
        if not package.is_file():
            errors.append(f"{slug}: nonexistent package path {entry.get('package_path')}")
        metadata = package.parent / "metadata.yaml"
        if not metadata.is_file() or load(metadata) != entry:
            errors.append(f"{slug}: package metadata differs from registry")
        expected_package = metadata.parent / "UPGRADEABLE.md"
        if package.resolve() != expected_package.resolve():
            errors.append(f"{slug}: package path does not match metadata directory")
        for key in ("tiers", "functional_classes", "implementation_forms", "triggers", "non_triggers", "requires", "recommended_with", "counterbalances", "potentially_redundant_with", "conflicts", "inputs", "outputs", "failure_boundary"):
            if not isinstance(entry.get(key), list):
                errors.append(f"{slug}: {key} must be an array")
        for key in ("display_name", "purpose", "registry_generation"):
            if not isinstance(entry.get(key), str) or not entry.get(key, "").strip():
                errors.append(f"{slug}: {key} must be non-empty text")
        if not re.fullmatch(r"\d+\.\d+\.\d+", entry.get("version", "")):
            errors.append(f"{slug}: invalid semantic version")
        scaling = entry.get("strong_model_scaling")
        if not isinstance(scaling, dict) or not isinstance(scaling.get("may_skip"), list) or not isinstance(scaling.get("keep_mandatory"), list) or not scaling.get("keep_mandatory"):
            errors.append(f"{slug}: invalid strong_model_scaling")
        provenance = entry.get("provenance")
        provenance_keys = {"source_document", "source_id", "source_date", "source_kind", "canonicality", "recovery_confidence", "notes"}
        if not isinstance(provenance, dict) or not provenance_keys <= set(provenance):
            errors.append(f"{slug}: incomplete provenance metadata")
        elif provenance["source_kind"] not in ALLOWED_SOURCE_KINDS or provenance["canonicality"] not in ALLOWED_CANONICALITY or provenance["recovery_confidence"] not in ALLOWED_CONFIDENCE:
            errors.append(f"{slug}: invalid provenance classification")
        for key in ("requires", "recommended_with", "counterbalances", "potentially_redundant_with", "conflicts"):
            for ref in entry.get(key, []):
                if ref not in known:
                    errors.append(f"{slug}: broken {key} reference {ref}")
        for alias in entry.get("historical_aliases", []):
            aliases.setdefault(alias.casefold(), set()).add(slug)
    for alias, owners in aliases.items():
        if len(owners) > 1:
            errors.append(f"ambiguous alias collision {alias}: {sorted(owners)}")

    for path in ROOT.glob("registry/unresolved/*.yaml"):
        record = load(path)
        if record.get("recovery_status") != "unresolved" or record.get("operational_status") != "archival_only":
            errors.append(f"{path.name}: unresolved record status invalid")
        forbidden = {"procedure", "mechanism", "triggers", "outputs"} & set(record)
        if forbidden:
            errors.append(f"{path.name}: unresolved record invents operational fields {sorted(forbidden)}")

    for path in ROOT.glob("bundles/*/metadata.yaml"):
        bundle = load(path)
        for key in ("slug", "display_name", "version", "purpose"):
            if not isinstance(bundle.get(key), str) or not bundle.get(key).strip():
                errors.append(f"{path.parent.name}: invalid {key}")
        if not isinstance(bundle.get("components"), list) or not bundle.get("components"):
            errors.append(f"{path.parent.name}: components must be a non-empty array")
        for ref in bundle.get("components", []):
            if ref not in known:
                errors.append(f"{path.parent.name}: unknown bundle component {ref}")
        if set(bundle.get("load_order", [])) != set(bundle.get("components", [])):
            errors.append(f"{path.parent.name}: load order/component mismatch")

    recipes = load(ROOT / "recipes/recipes.json")["recipes"]
    for recipe in recipes:
        if not isinstance(recipe.get("classifications"), dict) or not recipe.get("classifications"):
            errors.append(f"{recipe.get('slug')}: classifications must be a non-empty object")
        for ref, role in recipe.get("classifications", {}).items():
            if ref not in known:
                errors.append(f"{recipe['slug']}: unknown recipe component {ref}")
            if role not in {"R", "A", "C", "O", "X"}:
                errors.append(f"{recipe['slug']}: invalid recipe role {role}")
    # Explicit recovery invariants.
    unresolved_slugs = {item["slug"] for item in json_data.get("unresolved_records", [])}
    for slug in {"ocg", "ecl-drift-sink", "lros", "intent-task-framing-controller"}:
        if slug not in unresolved_slugs:
            errors.append(f"missing required unresolved record {slug}")
    itfc = next((item for item in entries if item["slug"] == "image-text-fidelity-capture"), None)
    if not itfc or "ITFC" not in itfc.get("historical_aliases", []):
        errors.append("Image Text Fidelity Capture does not preserve ITFC alias")
    return errors, len(entries), len(json_data.get("historical_records", [])), len(json_data.get("unresolved_records", []))

def main():
    errors, operational, historical, unresolved = validate()
    if errors:
        print("registry validation: FAILED", file=sys.stderr)
        for error in errors:
            print("- " + error, file=sys.stderr)
        return 1
    print(f"registry validation: OK ({operational} operational, {historical} historical-only, {unresolved} unresolved records)")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
