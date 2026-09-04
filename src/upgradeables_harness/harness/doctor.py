"""Deterministic diagnostics and harness-owned safe repair."""
from __future__ import annotations

import json
from argparse import Namespace
from dataclasses import asdict, dataclass
from pathlib import Path

from ..agents.base import HOST_PATHS, PROVIDERS, generate_fragment
from ..agents.managed_block import ManagedBlockError, validate_managed_block
from ..project.root import resolve_project_root
from ..project.profile import PROFILES
from ..registry.load import load_catalog, load_manifest, load_recipes
from ..constants import HARNESS_VERSION
from .init import initialize_project
from .manifest import harness_root, read_json, write_owned_text


@dataclass(frozen=True)
class Diagnostic:
    status: str
    code: str
    path: str
    message: str
    fixable: bool = False


def _diag(status, code, path, message, fixable=False):
    return Diagnostic(status, code, path, message, fixable)


def _load_local(root: Path, relative: str, diagnostics: list[Diagnostic]) -> dict | None:
    path = harness_root(root) / relative
    if not path.is_file():
        diagnostics.append(_diag("FAIL", "missing-artifact", f".upgradeables/{relative}", "Required harness artifact is missing.", True))
        return None
    try:
        return read_json(path)
    except (OSError, UnicodeError, ValueError, json.JSONDecodeError) as error:
        diagnostics.append(_diag("FAIL", "invalid-json", f".upgradeables/{relative}", str(error)))
        return None


def _component_versions() -> dict[str, str]:
    return {item["slug"]: item["version"] for item in load_catalog()["components"]}


def _locked_components(value: object):
    if not isinstance(value, dict):
        return []
    output = []
    for slug, record in value.items():
        if isinstance(record, str):
            version = record.removeprefix(f"{slug}@")
        elif isinstance(record, dict):
            version = record.get("version")
        else:
            version = None
        output.append((slug, version))
    return output


def _skill_component(value: object) -> tuple[str, str | None] | None:
    if not isinstance(value, str) or not value:
        return None
    slug, separator, version = value.partition("@")
    return slug, version if separator else None


def diagnose_project(project_root: Path) -> list[Diagnostic]:
    diagnostics: list[Diagnostic] = []
    try:
        from ..runtime.data import load_runtime_registry
        runtime_registry = load_runtime_registry()
        runtime_slugs = {item["slug"] for item in runtime_registry.get("components", [])}
        catalog_slugs = {item["slug"] for item in load_catalog()["components"]}
        if runtime_registry.get("schema_version") != "1.0.0" or runtime_registry.get("compiler_version") != "0.4.0":
            diagnostics.append(_diag("FAIL", "runtime-data-version", "bundled:runtime-registry", "Expected runtime schema 1.0.0 and compiler 0.4.0."))
        if runtime_slugs != catalog_slugs:
            diagnostics.append(_diag("FAIL", "runtime-coverage", "bundled:runtime-registry", "Runtime representation coverage does not match the bundled catalog."))
    except (ImportError, KeyError, OSError, ValueError) as error:
        diagnostics.append(_diag("FAIL", "runtime-data-unavailable", "bundled:runtime-registry", str(error)))
    base = harness_root(project_root)
    if not base.is_dir():
        return [_diag("FAIL", "harness-missing", ".upgradeables", "Harness is not initialized; run upgradeables init.")]
    manifest = load_manifest()
    components = _component_versions()
    recipes = {item["slug"] for item in load_recipes()["recipes"]}
    project = _load_local(project_root, "project.json", diagnostics)
    config = _load_local(project_root, "config.json", diagnostics)
    lock = _load_local(project_root, "lock.json", diagnostics)
    depth = config.get("install_depth", "standard") if config else "standard"
    if depth not in {"minimal", "standard", "full"}:
        diagnostics.append(_diag("FAIL", "invalid-config", ".upgradeables/config.json", "install_depth must be minimal, standard, or full."))
        depth = "standard"
    task_map = _load_local(project_root, "task-map.json", diagnostics) if depth != "minimal" else None
    skill_map = _load_local(project_root, "skill-map.json", diagnostics) if depth != "minimal" else None

    for relative, record in (("project.json", project), ("config.json", config), ("lock.json", lock), ("task-map.json", task_map)):
        if record is not None and record.get("schema_version") != "1.0.0":
            diagnostics.append(_diag("FAIL", "schema-version", f".upgradeables/{relative}", "Expected schema_version 1.0.0."))
    if lock is not None:
        for field, expected in (("registry_version", "0.2.1"),):
            if lock.get(field) != expected:
                diagnostics.append(_diag("FAIL", "version-mismatch", ".upgradeables/lock.json", f"{field} must be {expected}."))
        locked_harness = lock.get("harness_version")
        if locked_harness == "0.3.0" and HARNESS_VERSION == "0.4.0":
            diagnostics.append(_diag("WARN", "compatible-v03-lock", ".upgradeables/lock.json", "v0.3 lock remains compatible; reinitialize explicitly to adopt v0.4 defaults."))
        elif locked_harness != HARNESS_VERSION:
            diagnostics.append(_diag("FAIL", "version-mismatch", ".upgradeables/lock.json", f"harness_version must be {HARNESS_VERSION}."))
        if not isinstance(lock.get("components"), dict):
            diagnostics.append(_diag("FAIL", "invalid-lock", ".upgradeables/lock.json", "components must be an object."))
        for slug, version in _locked_components(lock.get("components")):
            if slug not in components:
                diagnostics.append(_diag("FAIL", "unknown-component", ".upgradeables/lock.json", f"Unknown component slug: {slug}."))
            elif version != components[slug]:
                diagnostics.append(_diag("FAIL", "component-version", ".upgradeables/lock.json", f"{slug} must pin {components[slug]}, found {version!r}."))
    if task_map is not None:
        if task_map.get("registry_version") != "0.2.1":
            diagnostics.append(_diag("FAIL", "version-mismatch", ".upgradeables/task-map.json", "registry_version must be 0.2.1."))
        entries = task_map.get("recipes")
        if task_map.get("selection_only") is not True:
            diagnostics.append(_diag("FAIL", "invalid-task-map", ".upgradeables/task-map.json", "selection_only must be true."))
        if not isinstance(entries, dict):
            diagnostics.append(_diag("FAIL", "invalid-task-map", ".upgradeables/task-map.json", "recipes must be an object."))
        else:
            for slug, entry in entries.items():
                if slug not in recipes:
                    diagnostics.append(_diag("FAIL", "unknown-recipe", ".upgradeables/task-map.json", f"Unknown recipe slug: {slug}."))
                if not isinstance(entry, dict) or entry.get("priority") not in {"high", "medium", "low"} or not isinstance(entry.get("reason"), list):
                    diagnostics.append(_diag("FAIL", "invalid-task-entry", ".upgradeables/task-map.json", f"Invalid task-map entry: {slug}."))
    if config is not None:
        network = config.get("network")
        if not isinstance(network, dict) or network.get("allow_registry_update") not in {True, False}:
            diagnostics.append(_diag("FAIL", "invalid-config", ".upgradeables/config.json", "network.allow_registry_update must be boolean."))
        references = config.get("reference_roots", [])
        if not isinstance(references, list) or not all(isinstance(item, str) for item in references):
            diagnostics.append(_diag("FAIL", "invalid-config", ".upgradeables/config.json", "reference_roots must be an array of relative paths."))
        else:
            for relative in references:
                target = project_root / relative
                if Path(relative).is_absolute() or not target.resolve(strict=False).is_relative_to(project_root.resolve()):
                    diagnostics.append(_diag("FAIL", "unsafe-reference-path", ".upgradeables/config.json", f"Reference root escapes the project: {relative!r}."))
        runtime = config.get("runtime")
        if runtime is not None:
            if not isinstance(runtime, dict):
                diagnostics.append(_diag("FAIL", "invalid-runtime-config", ".upgradeables/config.json", "runtime must be an object."))
            else:
                if runtime.get("default_model_profile") not in {"small", "medium", "strong", "auto", "custom"}:
                    diagnostics.append(_diag("FAIL", "invalid-runtime-profile", ".upgradeables/config.json", "runtime.default_model_profile is invalid."))
                if not isinstance(runtime.get("max_directive_tokens"), int) or runtime.get("max_directive_tokens", -1) < 0:
                    diagnostics.append(_diag("FAIL", "invalid-runtime-budget", ".upgradeables/config.json", "runtime.max_directive_tokens must be a non-negative integer."))
                if runtime.get("enabled") not in {True, False} or runtime.get("debug") not in {True, False}:
                    diagnostics.append(_diag("FAIL", "invalid-runtime-config", ".upgradeables/config.json", "runtime.enabled and runtime.debug must be boolean."))
        models = config.get("models")
        if models is not None:
            if not isinstance(models, dict) or any(
                not isinstance(value, dict) or value.get("runtime_profile") not in {"small", "medium", "strong", "auto", "custom"}
                for value in models.values()
            ):
                diagnostics.append(_diag("FAIL", "invalid-model-runtime-profile", ".upgradeables/config.json", "models entries require a valid runtime_profile."))
    if project is not None and Path(project.get("project_root", ".")) != Path("."):
        diagnostics.append(_diag("FAIL", "invalid-project-root", ".upgradeables/project.json", "project_root must be the portable value '.'."))
    if project is not None:
        selected = project.get("selected_profiles")
        if not isinstance(selected, list) or any(slug not in PROFILES for slug in selected):
            diagnostics.append(_diag("FAIL", "unknown-profile", ".upgradeables/project.json", "selected_profiles contains an unknown profile."))

    if skill_map is not None:
        try:
            from ..skills.map import validate_skill_map
        except (ImportError, AttributeError):
            map_errors = []
        else:
            map_errors = validate_skill_map(skill_map)
        for error in map_errors:
            diagnostics.append(_diag("FAIL", "invalid-skill-map", ".upgradeables/skill-map.json", error))
        skills = skill_map.get("skills")
        if not isinstance(skills, list):
            diagnostics.append(_diag("FAIL", "invalid-skill-map", ".upgradeables/skill-map.json", "skills must be an array."))
        else:
            for item in skills:
                if not isinstance(item, dict):
                    diagnostics.append(_diag("FAIL", "invalid-skill-entry", ".upgradeables/skill-map.json", "Skill entries must be objects."))
                    continue
                slug = item.get("slug", "<missing>")
                relative = item.get("path")
                if not isinstance(relative, str):
                    diagnostics.append(_diag("FAIL", "invalid-skill-path", ".upgradeables/skill-map.json", f"Skill {slug} has no path."))
                else:
                    target = project_root / relative
                    if not target.resolve(strict=False).is_relative_to(project_root.resolve()):
                        diagnostics.append(_diag("FAIL", "unsafe-skill-path", ".upgradeables/skill-map.json", f"Skill {slug} path escapes the project."))
                    elif not target.is_file():
                        diagnostics.append(_diag("WARN", "missing-skill-file", relative, f"Skill {slug} file is missing."))
                for raw in item.get("components", []):
                    parsed = _skill_component(raw)
                    if parsed is None or parsed[0] not in components:
                        diagnostics.append(_diag("FAIL", "unknown-component", ".upgradeables/skill-map.json", f"Skill {slug} references unknown component {raw!r}."))
                    elif parsed[1] and parsed[1] != components[parsed[0]]:
                        diagnostics.append(_diag("FAIL", "component-version", ".upgradeables/skill-map.json", f"Skill {slug} pins {raw}; expected {parsed[0]}@{components[parsed[0]]}."))

    expected_providers = ("generic",) if depth == "minimal" else PROVIDERS
    for provider in expected_providers:
        relative = f"agents/{provider}.md"
        path = base / relative
        expected = generate_fragment(provider).encode("utf-8")
        if not path.is_file():
            diagnostics.append(_diag("WARN", "missing-agent-fragment", f".upgradeables/{relative}", "Harness-owned adapter fragment is missing.", True))
        elif path.read_bytes() != expected:
            diagnostics.append(_diag("WARN", "stale-agent-fragment", f".upgradeables/{relative}", "Harness-owned adapter fragment is stale.", True))
    for provider, relative in HOST_PATHS.items():
        path = project_root / relative
        if not path.is_file():
            continue
        try:
            text = path.read_bytes().decode("utf-8")
            validate_managed_block(text)
        except (OSError, UnicodeError, ManagedBlockError) as error:
            diagnostics.append(_diag("FAIL", "malformed-managed-block", relative, str(error)))
    if not diagnostics:
        diagnostics.append(_diag("PASS", "harness-clean", ".upgradeables", "Harness-owned state is consistent."))
    return diagnostics


def _safe_fix(root: Path, diagnostics: list[Diagnostic]) -> list[str]:
    if not (root / ".upgradeables").is_dir():
        return []
    fixed: list[str] = []
    missing_core = any(item.code == "missing-artifact" and item.path != ".upgradeables/skill-map.json" for item in diagnostics)
    if missing_core:
        result = initialize_project(root, depth="standard", force=False)
        fixed.extend(result["created"])
    if any(item.code == "missing-artifact" and item.path == ".upgradeables/skill-map.json" for item in diagnostics):
        try:
            from ..skills.map import ensure_skill_map
        except (ImportError, AttributeError):
            pass
        else:
            ensure_skill_map(root, write=True)
            fixed.append(".upgradeables/skill-map.json")
    for item in diagnostics:
        if item.code not in {"missing-agent-fragment", "stale-agent-fragment"}:
            continue
        provider = Path(item.path).stem
        result = write_owned_text(root, f"agents/{provider}.md", generate_fragment(provider), force=True)
        if result.action in {"created", "updated"}:
            fixed.append(item.path)
    return list(dict.fromkeys(fixed))


def doctor_project(project: str | Path | None = None, *, fix: bool = False) -> dict:
    resolution = resolve_project_root(project)
    before = diagnose_project(resolution.root)
    fixed = _safe_fix(resolution.root, before) if fix else []
    diagnostics = diagnose_project(resolution.root) if fixed else before
    severity = "FAIL" if any(item.status == "FAIL" for item in diagnostics) else "WARN" if any(item.status == "WARN" for item in diagnostics) else "PASS"
    return {
        "schema_version": "1.0.0",
        "project_root": str(resolution.root),
        "status": severity,
        "diagnostics": [asdict(item) for item in diagnostics],
        "fixed": fixed,
    }


def command_doctor(args: Namespace) -> int:
    try:
        result = doctor_project(getattr(args, "project", None), fix=bool(getattr(args, "fix", False)))
    except (OSError, RuntimeError, ValueError) as error:
        print(f"doctor failed: {error}")
        return 1
    if getattr(args, "json", False):
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(f"Doctor: {result['status']}")
        for item in result["diagnostics"]:
            print(f"{item['status']} {item['code']}: {item['path']} — {item['message']}")
        if result["fixed"]:
            print("Fixed harness-owned artifacts: " + ", ".join(result["fixed"]))
    return 1 if result["status"] == "FAIL" else 0


run_doctor = command_doctor
