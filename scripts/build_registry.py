"""Build deterministic top-level registries from package metadata."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def load(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def payload():
    entries = [load(path) for path in ROOT.glob("upgradeables/*/*/metadata.yaml")]
    entries.sort(key=lambda item: item["slug"])
    historical = load(ROOT / "registry/historical/index.yaml")["records"]
    unresolved = [load(path) for path in ROOT.glob("registry/unresolved/*.yaml")]
    unresolved.sort(key=lambda item: item["slug"])
    recipes = load(ROOT / "recipes/recipes.json")["recipes"]
    return {
        "schema_version": "1.0.0",
        "registry_version": "0.1.0",
        "generated_from": "upgradeables/*/*/metadata.yaml",
        "source_corpus": [
            "archive/source/OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md",
            "archive/source/OS_Upgradeables_Historical_Recovery_Inventory.md",
            "archive/source/OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md",
        ],
        "historical_source_precedence": [
            "direct_user_spec", "user_accepted", "historical_recovery_inventory",
            "current_consolidated_catalog", "historical_assistant_artifact",
            "modern_implementation_recommendation",
        ],
        "upgradeables": entries,
        "historical_records": historical,
        "unresolved_records": unresolved,
        "recipes": recipes,
        "qms_modes": load(ROOT / "registry/qms_modes.json")["modes"],
        "behavior_genes": load(ROOT / "genes/index.json")["behavior_genes"],
        "cores": load(ROOT / "cores/index.json")["cores"],
        "domain_os": load(ROOT / "domain-os/index.json")["domain_os"],
    }

def render(data):
    # JSON is a strict YAML 1.2 subset: one deterministic serializer, two formats.
    return json.dumps(data, ensure_ascii=False, indent=2) + "\n"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render(payload())
    targets = [ROOT / "registry/registry.yaml", ROOT / "registry/registry.json"]
    if args.check:
        stale = [str(path.relative_to(ROOT)) for path in targets if not path.exists() or path.read_text(encoding="utf-8") != expected]
        if stale:
            print("stale generated registry: " + ", ".join(stale), file=sys.stderr)
            return 1
        print(f"registry build check: OK ({len(payload()['upgradeables'])} operational entries)")
        return 0
    for path in targets:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(expected, encoding="utf-8", newline="\n")
    print(f"built registry with {len(payload()['upgradeables'])} operational entries")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
