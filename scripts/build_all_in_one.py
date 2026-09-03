"""Build the portable all-in-one kit from canonical repository content."""
from __future__ import annotations
import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md"

LINK = re.compile(r"(?<!!)\[([^\]]+)\]\(([^)]+)\)")

def portable_text(relative_path):
    """Read a document and relocate repository links for the dist directory."""
    source = ROOT / relative_path
    text = source.read_text(encoding="utf-8")

    def relocate(match):
        label, raw_target = match.groups()
        target = raw_target.strip().strip("<>")
        if target.startswith(("http://", "https://", "mailto:", "#")):
            return match.group(0)
        path_part, separator, anchor = target.partition("#")
        if not path_part:
            return match.group(0)
        resolved = (source.parent / path_part).resolve()
        try:
            repo_path = resolved.relative_to(ROOT.resolve()).as_posix()
        except ValueError:
            return match.group(0)
        suffix = f"#{anchor}" if separator else ""
        return f"[{label}](../{repo_path}{suffix})"

    return LINK.sub(relocate, text)

def render():
    sections = [
        "# All-in-One Upgradeable Skill Kit\n\n> Generated file. Edit canonical repository content, not this artifact.\n",
    ]
    for path in [
        "START_HERE.md",
        "MODEL_CONSUMPTION_GUIDE.md",
        "prompts/QUICK_TASK.md",
        "prompts/BUILD_A_SKILL.md",
        "templates/SKILL_IMPLEMENTATION_TEMPLATE.md",
        "implementations/community/source-bounded-research/SKILL.md",
    ]:
        sections.append(portable_text(path))
    for path in ["spec/OS_PHILOSOPHY.md", "spec/UPGRADEABLE_SPEC.md", "spec/COMPOSITION_SPEC.md", "spec/PRECEDENCE_SPEC.md", "spec/SKILL_TRANSLATION_SPEC.md"]:
        sections.append(portable_text(path))
    sections.append("# Skill Recipe Matrix\n")
    recipes = json.loads((ROOT / "recipes/recipes.json").read_text(encoding="utf-8"))["recipes"]
    for recipe in recipes:
        roles = ", ".join(f"{slug}={role}" for slug, role in recipe["classifications"].items())
        sections.append(f"## {recipe['display_name']}\n\n{roles}\n")
    sections.append("# Recovered Recipe Procedures\n")
    for path in ["recipes/deterministic-intake-routing.md", "recipes/long-context-source-fidelity.md"]:
        sections.append(portable_text(path))
    sections.append(portable_text("bundles/qms/OPERATING_RULES.md"))
    sections.append("# Domain OS Examples\n")
    for path in sorted((ROOT / "domain-os").glob("*.md")):
        sections.append(portable_text(path.relative_to(ROOT)))
    registry = json.loads((ROOT / "registry/registry.json").read_text(encoding="utf-8"))
    sections.append("# Current Registry Summaries\n")
    for item in registry["upgradeables"]:
        companions = ", ".join(f"`{slug}`" for slug in item["recommended_with"]) or "none required"
        counterbalances = ", ".join(f"`{slug}`" for slug in item["counterbalances"]) or "none identified"
        sections.append(
            f"## {item['display_name']} (`{item['slug']}@{item['version']}`)\n\n"
            f"{item['purpose']}\n\n"
            f"- ID: `{item['id']}`\n"
            f"- OS role: {', '.join(item['os_role'])}\n"
            f"- Pipeline stages: {', '.join(item['pipeline_stages'])}\n"
            f"- Best-fit tasks: {', '.join(item['best_fit_tasks'])}\n"
            f"- Trigger: {item['triggers'][0]}\n"
            f"- When not to use: {item['avoid_when'][0]}\n"
            f"- Mechanism basis: `{item['mechanism_basis']}`\n"
            f"- Mechanism: {item['mechanism']}\n"
            f"- Companions: {companions}\n"
            f"- Counterbalances: {counterbalances}\n"
            f"- Failure boundary: {item['failure_boundary'][0]}\n"
            f"- Package: `{item['package_path']}`\n"
        )
    sections.append("# Deep-Recovery Historical Index\n")
    for item in registry["historical_records"]:
        if item.get("source_document") == "OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md" or item.get("additional_context_source"):
            sections.append(f"- **{item['display_name']}** (`{item['historical_id']}`, `{item['registry_generation']}`): {item.get('recovered_purpose', item.get('notes', 'historical record'))} Canonicality: `{item['canonicality']}`; source kind: `{item['source_kind']}`.\n")
    sections.append(portable_text("spec/RECOVERY_AND_PROVENANCE_SPEC.md"))
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
