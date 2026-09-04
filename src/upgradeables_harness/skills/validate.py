"""Draft and final validation for project-local Skills."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

from .common import SkillFactoryError, argument, emit_json, registry_version
from .map import ensure_skill_map


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
SPLIT_COMPONENT = re.compile(
    r"\|\s*`([a-z0-9]+(?:-[a-z0-9]+)*)`\s*\|\s*`(\d+\.\d+\.\d+)`\s*\|"
)
PRIMARY_RECIPE = re.compile(r"Primary recipe:\s*`([^`]+)`", re.IGNORECASE)


def frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.DOTALL)
    if not match:
        return {}
    result: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def section_body(text: str, heading: str) -> str:
    match = re.search(
        rf"^## {re.escape(heading)}\s*$\n(.*?)(?=^## |\Z)",
        text,
        re.MULTILINE | re.DOTALL,
    )
    return match.group(1).strip() if match else ""


def _known_component(slug: str) -> dict[str, Any] | None:
    try:
        from upgradeables_harness.registry.load import get_component

        value = get_component(slug)
    except (ImportError, ModuleNotFoundError, KeyError, OSError, ValueError):
        return None
    return value if isinstance(value, dict) else None


def _known_recipe(slug: str) -> dict[str, Any] | None:
    try:
        from upgradeables_harness.registry.load import get_recipe

        value = get_recipe(slug)
    except (ImportError, ModuleNotFoundError, KeyError, OSError, ValueError):
        return None
    return value if isinstance(value, dict) else None


def _skill_file(path: str | Path) -> Path:
    candidate = Path(path).expanduser().resolve()
    return candidate / "SKILL.md" if candidate.is_dir() else candidate


def _test_case_errors(skill_file: Path) -> list[str]:
    path = skill_file.parent / "tests" / "cases.json"
    if not path.is_file():
        return ["final Skill requires tests/cases.json"]
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        return [f"cannot read tests/cases.json: {error}"]
    cases = value.get("cases") if isinstance(value, dict) else None
    if not isinstance(cases, list):
        return ["tests/cases.json must contain a cases array"]
    kinds = {
        item.get("kind") for item in cases if isinstance(item, dict)
    }
    required = {"positive", "negative", "authority", "failure", "composition"}
    missing = sorted(required - kinds)
    errors = [f"tests/cases.json missing case kinds: {', '.join(missing)}"] if missing else []
    if re.search(r"\bTODO\b", path.read_text(encoding="utf-8"), re.IGNORECASE):
        errors.append("tests/cases.json contains TODO placeholders")
    return errors


def validate_skill_path(path: str | Path, *, draft: bool = False) -> dict[str, Any]:
    skill_file = _skill_file(path)
    errors: list[str] = []
    warnings: list[str] = []
    if not skill_file.is_file():
        return {
            "path": str(skill_file),
            "mode": "draft" if draft else "final",
            "valid": False,
            "errors": [f"Skill file not found: {skill_file}"],
            "warnings": [],
            "name": None,
            "recipe": None,
            "components": [],
        }
    try:
        text = skill_file.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        return {
            "path": str(skill_file),
            "mode": "draft" if draft else "final",
            "valid": False,
            "errors": [f"Cannot read Skill file: {error}"],
            "warnings": [],
            "name": None,
            "recipe": None,
            "components": [],
        }

    metadata = frontmatter(text)
    name = metadata.get("name", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        errors.append("frontmatter name must be a lowercase hyphenated slug")
    if len(metadata.get("description", "")) < 20:
        errors.append("frontmatter description must explain activation")
    if name and skill_file.name == "SKILL.md" and name != skill_file.parent.name:
        errors.append(f"frontmatter name must match folder: {skill_file.parent.name}")

    for heading in REQUIRED_HEADINGS:
        if not section_body(text, heading):
            errors.append(f"missing section: {heading}")

    selected = section_body(text, "Selected Upgradeables")
    selected = re.split(r"^Resolver exclusions:\s*$", selected, maxsplit=1, flags=re.MULTILINE)[0]
    selected_lines = [
        line for line in selected.splitlines()
        if not re.search(r"\|\s*Drop\s*\|", line, re.IGNORECASE)
    ]
    selected_text = "\n".join(selected_lines)
    components = sorted(set(COMPONENT.findall(selected_text)) | set(SPLIT_COMPONENT.findall(selected_text)))
    for slug, version in components:
        record = _known_component(slug)
        if record is None:
            errors.append(f"unknown Upgradeable: {slug}")
        elif version != record.get("version"):
            errors.append(
                f"version mismatch for {slug}: expected {record.get('version')}, found {version}"
            )

    recipe_match = PRIMARY_RECIPE.search(text)
    recipe = recipe_match.group(1).strip() if recipe_match else None
    if recipe and recipe not in {"none-selected", "direct-path", "direct path"}:
        if _known_recipe(recipe) is None:
            errors.append(f"unknown recipe: {recipe}")

    registry_mentions = re.findall(r"Registry:\s*`([^`]+)`", text, re.IGNORECASE)
    for value in registry_mentions:
        if value != registry_version():
            errors.append(
                f"registry version mismatch: expected {registry_version()}, found {value}"
            )

    if draft:
        if not components:
            warnings.append("no pinned selected Upgradeables yet")
        if "TODO" in text:
            warnings.append("draft contains TODO placeholders")
    else:
        if re.search(r"\bTODO\b|<[^>]+>", text, re.IGNORECASE):
            errors.append("final Skill contains TODO or angle-bracket placeholders")
        if re.search(r"^Status:\s*draft\s*$", text, re.MULTILINE | re.IGNORECASE):
            errors.append("final Skill still has draft status")
        if not components:
            errors.append("final Skill needs at least one selected Upgradeable slug@version")
        if recipe in (None, "none-selected"):
            errors.append("final Skill needs a canonical primary recipe or explicit direct-path")
        activation = section_body(text, "Task Identity and Activation Boundary").casefold()
        if "positive" not in activation or not any(
            marker in activation for marker in ("do not", "non-trigger", "negative")
        ):
            errors.append("final Skill needs positive activation and an explicit non-trigger")
        inputs = section_body(text, "Required Inputs and Explicit State").casefold()
        missing_markers = ("missing", "cannot", "absent", "unavailable", "not supplied")
        if not any(marker in inputs for marker in missing_markers) or len(inputs.split()) < 20:
            errors.append("final Skill needs substantive required-input and missing-input behavior")
        compatibility = section_body(text, "Target Host and Compatibility").casefold()
        if "capabil" not in compatibility or len(compatibility.split()) < 15:
            errors.append("final Skill needs host/capability compatibility and fallback behavior")
        authority = section_body(text, "Authority and Precedence").casefold()
        if "authority" not in authority and "permission" not in authority:
            errors.append("final Skill needs an explicit authority boundary")
        if len(section_body(text, "Procedure").split()) < 40:
            errors.append("final Skill procedure is not substantive")
        if len(section_body(text, "Output Contract").split()) < 20:
            errors.append("final Skill output contract is not substantive")
        validation = section_body(text, "Validators and Failure Handling").casefold()
        failure_markers = ("fail", "conflict", "missing", "cannot", "unsupported")
        stopping_markers = ("stop", "finish", "complete", "completion")
        if not any(marker in validation for marker in failure_markers) or not any(
            marker in validation for marker in stopping_markers
        ):
            errors.append("final Skill needs failure behavior and a stopping rule")
        tests = section_body(text, "Tests").casefold()
        for label in ("positive", "negative", "failure", "composition"):
            if label not in tests:
                errors.append(f"tests section must include a {label} case")
        if "authority" not in tests and "conflict" not in tests:
            errors.append("tests section must include an authority or conflict case")
        errors.extend(_test_case_errors(skill_file))

    return {
        "path": str(skill_file),
        "mode": "draft" if draft else "final",
        "valid": not errors,
        "errors": errors,
        "warnings": warnings,
        "name": name or None,
        "recipe": recipe,
        "components": [f"{slug}@{version}" for slug, version in components],
    }


def validate_project_skill(
    project_root: str | Path, slug: str | None = None
) -> list[dict[str, Any]]:
    """Validate one or all mapped project Skills for `doctor` and init checks."""

    root = Path(project_root).resolve()
    try:
        skill_map = ensure_skill_map(root, write=False)
    except SkillFactoryError as error:
        return [{"slug": slug, "valid": False, "errors": [str(error)], "warnings": []}]
    records = skill_map.get("skills", [])
    if slug is not None:
        records = [item for item in records if item.get("slug") == slug]
        if not records:
            return [{"slug": slug, "valid": False, "errors": ["Skill is not registered"], "warnings": []}]
    results: list[dict[str, Any]] = []
    for item in records:
        path = root / item["path"]
        result = validate_skill_path(path, draft=item.get("status") != "validated")
        if result["valid"]:
            mapped_components = sorted(item.get("components", []))
            if mapped_components != result["components"]:
                result["errors"].append(
                    "Skill map components do not match selected Upgradeables in SKILL.md"
                )
            mapped_recipe = item.get("recipe")
            skill_recipe = result["recipe"]
            if skill_recipe == "none-selected":
                skill_recipe = None
            if mapped_recipe != skill_recipe:
                result["errors"].append(
                    "Skill map recipe does not match the primary recipe in SKILL.md"
                )
            result["valid"] = not result["errors"]
        result["slug"] = item.get("slug")
        result["map_status"] = item.get("status")
        results.append(result)
    return results


def command_validate(args: Any) -> int:
    result = validate_skill_path(
        argument(args, "path", ""), draft=bool(argument(args, "draft", False))
    )
    if argument(args, "json", False):
        emit_json(result)
    elif result["valid"]:
        print(f"Project Skill validation: OK ({result['mode']}, {result['path']})")
        for warning in result["warnings"]:
            print(f"WARN: {warning}")
    else:
        print(f"Project Skill validation failed: {result['path']}", file=sys.stderr)
        for error in result["errors"]:
            print(f"- {error}", file=sys.stderr)
    return 0 if result["valid"] else 1
