"""Validate the portable contract of one contributed Skill."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_HEADINGS = (
    "Task Identity and Activation Boundary",
    "Target Host and Compatibility",
    "Required Inputs and Explicit State",
    "Selected Upgradeables",
    "Authority and Precedence",
    "Procedure",
    "Validators and Failure Handling",
    "Output Contract",
    "Provenance",
    "Tests",
)
COMPONENT = re.compile(r"`([a-z0-9]+(?:-[a-z0-9]+)*)@(\d+\.\d+\.\d+)`")


def frontmatter(text):
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}
    result = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip()
    return result


def section_body(text, heading):
    match = re.search(
        rf"^## {re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    return match.group(1).strip() if match else ""


def validate(path):
    errors = []
    text = path.read_text(encoding="utf-8")
    metadata = frontmatter(text)
    name = metadata.get("name", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append("frontmatter name must be a lowercase hyphenated slug")
    if len(metadata.get("description", "")) < 20:
        errors.append("frontmatter description must explain activation")
    if path.name == "SKILL.md" and name and name != path.parent.name:
        errors.append(f"frontmatter name must match folder: {path.parent.name}")
    for heading in REQUIRED_HEADINGS:
        body = section_body(text, heading)
        if not body:
            errors.append(f"missing section: {heading}")

    known = {
        item["slug"]: item["version"]
        for item in json.loads((ROOT / "registry/catalog.json").read_text(encoding="utf-8"))["upgradeables"]
    }
    selected_body = section_body(text, "Selected Upgradeables")
    selected_lines = [
        line for line in selected_body.splitlines()
        if not re.search(r"\|\s*Drop\s*\|", line, re.IGNORECASE)
    ]
    components = set(COMPONENT.findall("\n".join(selected_lines)))
    if not components:
        errors.append("no selected Upgradeable slug@version references found")
    for slug, version in components:
        if slug not in known:
            errors.append(f"unknown Upgradeable: {slug}")
        elif version != known[slug]:
            errors.append(f"version mismatch for {slug}: expected {known[slug]}, found {version}")
    tests = section_body(text, "Tests").casefold()
    for label in ("positive", "negative", "failure", "composition"):
        if label not in tests:
            errors.append(f"tests must include a {label} case")
    if "authority" not in tests and "conflict" not in tests:
        errors.append("tests must include an authority or conflict case")
    return errors


def main():
    parser = argparse.ArgumentParser(description="Validate contributed SKILL.md files")
    parser.add_argument("paths", nargs="*", type=Path, help="Skill file or folder; omit to validate all implementations")
    args = parser.parse_args()
    candidates = args.paths or sorted((ROOT / "implementations").glob("**/SKILL.md"))
    paths = [path / "SKILL.md" if path.is_dir() else path for path in candidates]
    failed = False
    for path in paths:
        if not path.is_file():
            print(f"Skill file not found: {path}", file=sys.stderr)
            failed = True
            continue
        errors = validate(path)
        if errors:
            print(f"Skill validation failed: {path}", file=sys.stderr)
            for error in errors:
                print(f"- {error}", file=sys.stderr)
            failed = True
        else:
            print(f"Skill validation: OK ({path})")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
