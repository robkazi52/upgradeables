"""Build the portable all-in-one kit from canonical repository content."""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md"

def render():
    sections = [
        "# All-in-One Upgradeable Skill Kit\n\n> Generated file. Edit canonical repository content, not this artifact.\n",
    ]
    for path in ["spec/OS_PHILOSOPHY.md", "spec/UPGRADEABLE_SPEC.md", "spec/COMPOSITION_SPEC.md", "spec/PRECEDENCE_SPEC.md", "spec/SKILL_TRANSLATION_SPEC.md"]:
        sections.append((ROOT / path).read_text(encoding="utf-8"))
    sections.append("# Skill Recipe Matrix\n")
    recipes = json.loads((ROOT / "recipes/recipes.json").read_text(encoding="utf-8"))["recipes"]
    for recipe in recipes:
        roles = ", ".join(f"{slug}={role}" for slug, role in recipe["classifications"].items())
        sections.append(f"## {recipe['display_name']}\n\n{roles}\n")
    sections.append("# Recovered Recipe Procedures\n")
    for path in ["recipes/deterministic-intake-routing.md", "recipes/long-context-source-fidelity.md"]:
        sections.append((ROOT / path).read_text(encoding="utf-8"))
    sections.append((ROOT / "bundles/qms/OPERATING_RULES.md").read_text(encoding="utf-8"))
    sections.append("# Domain OS Examples\n")
    for path in sorted((ROOT / "domain-os").glob("*.md")):
        sections.append(path.read_text(encoding="utf-8"))
    registry = json.loads((ROOT / "registry/registry.json").read_text(encoding="utf-8"))
    sections.append("# Current Registry Summaries\n")
    for item in registry["upgradeables"]:
        sections.append(f"## {item['display_name']} (`{item['slug']}`)\n\n{item['purpose']}\n\n- ID: `{item['id']}`\n- Activation: `{item['activation_class']}`\n- Classes: {', '.join(item['functional_classes'])}\n- Forms: {', '.join(item['implementation_forms'])}\n- Package: `{item['package_path']}`\n")
    sections.append("# Deep-Recovery Historical Index\n")
    for item in registry["historical_records"]:
        if item.get("source_document") == "OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md" or item.get("additional_context_source"):
            sections.append(f"- **{item['display_name']}** (`{item['historical_id']}`, `{item['registry_generation']}`): {item.get('recovered_purpose', item.get('notes', 'historical record'))} Canonicality: `{item['canonicality']}`; source kind: `{item['source_kind']}`.\n")
    sections.append((ROOT / "spec/RECOVERY_AND_PROVENANCE_SPEC.md").read_text(encoding="utf-8"))
    sections.append("# Unresolved Records\n")
    for item in registry["unresolved_records"]:
        sections.append(f"- **{item['display_name']}** (`{item['slug']}`): {item['known_gap']} Status: archival-only.\n")
    return "\n---\n\n".join(section.strip() for section in sections) + "\n"

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    expected = render()
    if args.check:
        if not TARGET.exists() or TARGET.read_text(encoding="utf-8") != expected:
            print("all-in-one artifact is stale", file=sys.stderr)
            return 1
        print("all-in-one build check: OK")
        return 0
    TARGET.parent.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(expected, encoding="utf-8", newline="\n")
    print(f"built {TARGET.relative_to(ROOT)}")
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
