"""Project-local Skill map creation, validation, and updates."""
from __future__ import annotations

from pathlib import Path
import re
from typing import Any

from .common import (
    HARNESS_DIR,
    SkillFactoryError,
    component_version,
    read_json,
    validate_slug,
    write_json,
)


SKILL_MAP_SCHEMA_VERSION = "1.0.0"
SKILL_STATUSES = {"draft", "candidate", "validated", "deprecated"}
COMPONENT_PIN = re.compile(r"([a-z0-9]+(?:-[a-z0-9]+)*)@(\d+\.\d+\.\d+)\Z")
SKILLS_README = """# Project Skills

This directory contains project-local workflows. Create a draft with
`upgradeables skill scaffold <slug>` and validate it before changing its status
to `validated` in `.upgradeables/skill-map.json`.

Project Skills may reference maintained local contracts and conventions. They do
not change the global Upgradeables registry or grant additional authority.
"""


def _harness_version() -> str:
    try:
        from upgradeables_harness.constants import HARNESS_VERSION

        return str(HARNESS_VERSION)
    except (ImportError, AttributeError):
        return "0.4.0"


def _known_recipe(slug: str) -> bool:
    try:
        from upgradeables_harness.registry.load import get_recipe

        return isinstance(get_recipe(slug), dict)
    except (ImportError, ModuleNotFoundError, OSError, ValueError):
        return False


def empty_skill_map() -> dict[str, Any]:
    return {
        "schema_version": SKILL_MAP_SCHEMA_VERSION,
        "harness_version": _harness_version(),
        "skills": [],
    }


def skill_map_path(project_root: str | Path) -> Path:
    return Path(project_root).resolve() / HARNESS_DIR / "skill-map.json"


def validate_skill_map(value: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if value.get("schema_version") != SKILL_MAP_SCHEMA_VERSION:
        errors.append(
            f"schema_version must be {SKILL_MAP_SCHEMA_VERSION!r}"
        )
    compatible_versions = {_harness_version()}
    if _harness_version() == "0.4.0":
        compatible_versions.add("0.3.0")
    if value.get("harness_version") not in compatible_versions:
        errors.append(f"harness_version must be one of {sorted(compatible_versions)!r}")
    skills = value.get("skills")
    if not isinstance(skills, list):
        return [*errors, "skills must be an array"]
    seen: set[str] = set()
    for index, item in enumerate(skills):
        location = f"skills[{index}]"
        if not isinstance(item, dict):
            errors.append(f"{location} must be an object")
            continue
        slug = item.get("slug")
        try:
            validate_slug(slug)
        except SkillFactoryError as error:
            errors.append(f"{location}.slug: {error}")
            continue
        if slug in seen:
            errors.append(f"duplicate Skill slug: {slug}")
        seen.add(slug)
        expected = f"{HARNESS_DIR}/skills/{slug}/SKILL.md"
        if item.get("path") != expected:
            errors.append(f"{location}.path must be {expected!r}")
        if item.get("status") not in SKILL_STATUSES:
            errors.append(f"{location}.status must be one of {sorted(SKILL_STATUSES)}")
        recipe = item.get("recipe")
        if recipe is not None and not isinstance(recipe, str):
            errors.append(f"{location}.recipe must be a string or null")
        elif isinstance(recipe, str) and not _known_recipe(recipe):
            errors.append(f"{location}.recipe references unknown recipe: {recipe}")
        components = item.get("components")
        if not isinstance(components, list) or not all(
            isinstance(component, str) for component in components
        ):
            errors.append(f"{location}.components must be an array of strings")
        else:
            if len(components) != len(set(components)):
                errors.append(f"{location}.components contains duplicate pins")
            for component in components:
                match = COMPONENT_PIN.fullmatch(component)
                if not match:
                    errors.append(
                        f"{location}.components must use canonical slug@version pins: {component!r}"
                    )
                    continue
                slug_value, version = match.groups()
                expected_version = component_version(slug_value)
                if expected_version is None:
                    errors.append(f"{location}.components references unknown Upgradeable: {slug_value}")
                elif version != expected_version:
                    errors.append(
                        f"{location}.components expected {slug_value}@{expected_version}, found {component}"
                    )
        if item.get("project_specific") is not True:
            errors.append(f"{location}.project_specific must be true")
    return errors


def ensure_skill_map(
    project_root: str | Path, *, write: bool = True
) -> dict[str, Any]:
    """Return a valid project Skill map, creating it only when requested."""

    path = skill_map_path(project_root)
    if write:
        skills_directory = path.parent / "skills"
        skills_directory.mkdir(parents=True, exist_ok=True)
        readme = skills_directory / "README.md"
        if not readme.exists():
            readme.write_text(SKILLS_README, encoding="utf-8")
    if path.is_file():
        value = read_json(path, required=True)
        errors = validate_skill_map(value)
        if errors:
            raise SkillFactoryError(
                f"Invalid Skill map {path}: " + "; ".join(errors)
            )
        return value
    value = empty_skill_map()
    if write:
        write_json(path, value)
    return value


def save_skill_map(project_root: str | Path, value: dict[str, Any]) -> None:
    errors = validate_skill_map(value)
    if errors:
        raise SkillFactoryError("Refusing to write invalid Skill map: " + "; ".join(errors))
    write_json(skill_map_path(project_root), value)


def upsert_skill(
    project_root: str | Path,
    *,
    slug: str,
    status: str = "draft",
    recipe: str | None = None,
    components: list[str] | None = None,
) -> dict[str, Any]:
    validate_slug(slug)
    if status not in SKILL_STATUSES:
        raise SkillFactoryError(f"Unknown Skill status: {status}")
    value = ensure_skill_map(project_root, write=True)
    record = {
        "slug": slug,
        "path": f"{HARNESS_DIR}/skills/{slug}/SKILL.md",
        "status": status,
        "recipe": recipe,
        "components": sorted(set(components or [])),
        "project_specific": True,
    }
    skills = value["skills"]
    for index, existing in enumerate(skills):
        if existing["slug"] == slug:
            skills[index] = record
            break
    else:
        skills.append(record)
    skills.sort(key=lambda item: item["slug"])
    save_skill_map(project_root, value)
    return record


def list_skill_records(project_root: str | Path) -> list[dict[str, Any]]:
    """List map records without creating files or silently registering orphans."""

    value = ensure_skill_map(project_root, write=False)
    root = Path(project_root).resolve()
    records: list[dict[str, Any]] = []
    for item in value["skills"]:
        record = dict(item)
        record["exists"] = (root / item["path"]).is_file()
        records.append(record)
    return records
