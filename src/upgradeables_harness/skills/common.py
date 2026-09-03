"""Shared, dependency-free helpers for the project Skill factory."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


SKILL_SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
HARNESS_DIR = ".upgradeables"
SKILLS_DIR = "skills"


class SkillFactoryError(RuntimeError):
    """A user-facing, deterministic Skill-factory error."""


def argument(args: Any, name: str, default: Any = None) -> Any:
    """Read an argparse-style attribute without coupling helpers to argparse."""

    return getattr(args, name, default)


def read_json(path: Path, *, required: bool = False) -> dict[str, Any]:
    if not path.is_file():
        if required:
            raise SkillFactoryError(f"Required file not found: {path}")
        return {}
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError) as error:
        raise SkillFactoryError(f"Cannot read JSON file {path}: {error}") from error
    if not isinstance(value, dict):
        raise SkillFactoryError(f"Expected a JSON object in {path}")
    return value


def write_json(path: Path, value: dict[str, Any]) -> None:
    """Write one harness-owned JSON artifact with stable formatting."""

    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.tmp")
    temporary.write_text(
        json.dumps(value, indent=2, ensure_ascii=False, sort_keys=False) + "\n",
        encoding="utf-8",
    )
    temporary.replace(path)


def resolve_project_root(value: str | Path | None = None) -> Path:
    """Resolve an initialized harness root without importing project code."""

    try:
        if value is not None:
            start = Path(value).expanduser().resolve()
        else:
            start = Path.cwd().resolve()
    except (OSError, RuntimeError) as error:
        raise SkillFactoryError(f"Cannot resolve project path {value!r}: {error}") from error

    try:
        from upgradeables_harness.project.root import find_project_root
    except (ImportError, ModuleNotFoundError):
        find_project_root = None

    if find_project_root is not None:
        try:
            found = find_project_root(start)
        except (FileNotFoundError, NotADirectoryError, OSError, ValueError) as error:
            raise SkillFactoryError(str(error)) from error
        if found is not None:
            return Path(found).resolve()

    cursor = start if start.is_dir() else start.parent
    for candidate in (cursor, *cursor.parents):
        if (candidate / HARNESS_DIR).is_dir():
            return candidate
    if value is not None:
        return start
    return cursor


def require_harness(project_root: Path) -> Path:
    harness = project_root / HARNESS_DIR
    if not harness.is_dir():
        raise SkillFactoryError(
            f"No {HARNESS_DIR} harness found at {project_root}. Run `upgradeables init` first."
        )
    return harness


def validate_slug(slug: str) -> str:
    if not isinstance(slug, str) or not SKILL_SLUG.fullmatch(slug):
        raise SkillFactoryError(
            "Skill slug must contain lowercase letters or digits separated by single hyphens."
        )
    return slug


def skill_path(project_root: Path, slug: str) -> Path:
    validate_slug(slug)
    base = (project_root / HARNESS_DIR / SKILLS_DIR).resolve()
    candidate = (base / slug).resolve()
    if candidate.parent != base:
        raise SkillFactoryError("Skill path escapes the project Skill directory.")
    return candidate


def emit_json(value: Any) -> None:
    print(json.dumps(value, indent=2, ensure_ascii=False, sort_keys=False))


def display_name(slug: str) -> str:
    return " ".join(part.capitalize() for part in slug.split("-"))


def task_slug(task: str, *, fallback: str = "project-workflow") -> str:
    words = re.findall(r"[a-z0-9]+", task.casefold())
    ignored = {
        "a", "an", "and", "for", "from", "in", "into", "of", "on", "please",
        "the", "this", "to", "with",
    }
    useful = [word for word in words if word not in ignored][:7]
    slug = "-".join(useful) or fallback
    return slug[:63].rstrip("-") or fallback


def project_profile(project_root: Path) -> dict[str, Any]:
    return read_json(project_root / HARNESS_DIR / "project.json")


def project_config(project_root: Path) -> dict[str, Any]:
    return read_json(project_root / HARNESS_DIR / "config.json")


def project_references(project_root: Path) -> list[str]:
    config = project_config(project_root)
    values = config.get("reference_roots", [])
    if not isinstance(values, list):
        return []
    return [value for value in values if isinstance(value, str) and value.strip()]


def registry_version() -> str:
    """Return the bundled registry version; v0.3 is pinned to 0.2.1."""

    try:
        from upgradeables_harness.registry.load import load_manifest

        manifest = load_manifest()
        value = manifest.get("registry_version")
        if isinstance(value, str) and value:
            return value
    except (ImportError, ModuleNotFoundError, OSError, ValueError):
        pass
    return "0.2.1"


def component_version(slug: str) -> str | None:
    try:
        from upgradeables_harness.registry.load import get_component

        record = get_component(slug)
    except (ImportError, ModuleNotFoundError, KeyError, OSError, ValueError):
        return None
    if not isinstance(record, dict):
        return None
    value = record.get("version")
    return value if isinstance(value, str) and value else None
