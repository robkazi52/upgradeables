"""Build deterministic top-level registries from package metadata."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DISCOVERY_KEYWORDS = {
    "anti-tunnel-vision": ["review", "unsafe", "unsafe-assumption"],
    "bidirectional-consistency": ["code-review", "pull-request", "regression", "regressions", "correctness"],
    "critical-atomic-verification": ["code-review", "security-review", "correctness"],
    "grounding-no-invention": ["review", "unsafe-assumption", "source-bounded"],
    "invariance-stress-scaffold": ["code-review", "pull-request", "regression", "regressions", "correctness"],
    "parallel-qms": ["review", "quality-assurance", "unsafe-assumption"],
}

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

def catalog_payload(data):
    """Render a compact discovery surface without duplicating canonical metadata."""
    fields = (
        "slug", "display_name", "version", "purpose", "activation_class",
        "functional_classes", "triggers", "requires", "package_path",
    )
    entries = []
    for item in data["upgradeables"]:
        entry = {key: item[key] for key in fields}
        entry["keywords"] = DISCOVERY_KEYWORDS.get(item["slug"], [])
        entries.append(entry)
    by_slug = {item["slug"]: item for item in entries}
    recipes = []
    for recipe in data["recipes"]:
        components = []
        for slug, role in recipe["classifications"].items():
            item = by_slug[slug]
            components.append({
                "slug": slug,
                "role": role,
                "display_name": item["display_name"],
                "version": item["version"],
                "trigger_summary": item["triggers"][0] if item["triggers"] else "",
                "requires": item["requires"],
                "package_path": item["package_path"],
            })
        recipes.append({
            "slug": recipe["slug"],
            "display_name": recipe["display_name"],
            "recipe_path": f"recipes/resolved/{recipe['slug']}.md",
            "source_recipe_path": f"recipes/{recipe['slug']}.md",
            "components": components,
        })
    return {
        "schema_version": "1.0.0",
        "registry_version": data["registry_version"],
        "purpose": "Compact discovery catalog. registry/registry.json remains authoritative.",
        "entrypoint": "START_HERE.md",
        "upgradeables": entries,
        "recipes": recipes,
    }

def render_recipe_card(recipe):
    lines = [
        f"# {recipe['display_name']} — Resolved Recipe",
        "",
        "Generated discovery view. Evaluate triggers here, then open only retained packages.",
        f"See the [source recipe notes](../{recipe['slug']}.md) for composition and tests.",
        "",
        "`R` stays required after selecting this recipe. `A`, `C`, and `O` require an",
        "active trigger. `X` is excluded without explicit justification.",
        "",
        "| Role | Component | Trigger summary | Requires |",
        "|:---:|---|---|---|",
    ]
    for item in recipe["components"]:
        requires = ", ".join(f"`{slug}`" for slug in item["requires"]) or "—"
        trigger = item["trigger_summary"].replace("|", "\\|") or "See package"
        package = "../../" + item["package_path"]
        component = f"[{item['display_name']} (`{item['slug']}@{item['version']}`)]({package})"
        lines.append(f"| {item['role']} | {component} | {trigger} | {requires} |")
    lines.extend([
        "",
        "Do not merge whole recipes. Add individual cross-cutting components only for",
        "explicit requirements the primary recipe does not cover.",
        "",
    ])
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    data = payload()
    expected = render(data)
    catalog_data = catalog_payload(data)
    expected_catalog = render(catalog_data)
    recipe_cards = {
        ROOT / recipe["recipe_path"]: render_recipe_card(recipe)
        for recipe in catalog_data["recipes"]
    }
    targets = [ROOT / "registry/registry.yaml", ROOT / "registry/registry.json"]
    if args.check:
        stale = [str(path.relative_to(ROOT)) for path in targets if not path.exists() or path.read_text(encoding="utf-8") != expected]
        catalog = ROOT / "registry/catalog.json"
        if not catalog.exists() or catalog.read_text(encoding="utf-8") != expected_catalog:
            stale.append(str(catalog.relative_to(ROOT)))
        stale.extend(
            str(path.relative_to(ROOT))
            for path, content in recipe_cards.items()
            if not path.exists() or path.read_text(encoding="utf-8") != content
        )
        if stale:
            print("stale generated registry: " + ", ".join(stale), file=sys.stderr)
            return 1
        print(f"registry build check: OK ({len(data['upgradeables'])} operational entries)")
        return 0
    for path in targets:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(expected, encoding="utf-8", newline="\n")
    (ROOT / "registry/catalog.json").write_text(expected_catalog, encoding="utf-8", newline="\n")
    for path, content in recipe_cards.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8", newline="\n")
    print(f"built registry with {len(data['upgradeables'])} operational entries")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
