"""Initialize deterministic, project-local harness artifacts."""
from __future__ import annotations

import json
import os
import time
from argparse import Namespace
from contextlib import contextmanager
from pathlib import Path

from ..agents.base import PROVIDERS, generate_fragment
from ..project.inspect import inspect_project
from ..project.profile import PROFILES, recommend_project, select_profiles
from ..project.root import resolve_project_root
from .config import default_config
from .lockfile import default_lockfile
from .manifest import WriteResult, harness_root, owned_path, write_owned_json, write_owned_text
from .task_map import build_task_map


@contextmanager
def _initialization_lock(base: Path):
    """Serialize initialization of one project across threads/processes."""
    lock = base / ".init.lock"
    deadline = time.monotonic() + 30.0
    descriptor = None
    while descriptor is None:
        try:
            descriptor = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY)
            os.write(descriptor, f"{os.getpid()}\n".encode("ascii"))
        except FileExistsError:
            try:
                stale = time.time() - lock.stat().st_mtime > 60.0
            except OSError:
                stale = False
            if stale:
                try:
                    lock.unlink()
                except OSError:
                    pass
                continue
            if time.monotonic() >= deadline:
                raise RuntimeError(f"timed out waiting for harness initialization lock: {lock}")
            time.sleep(0.01)
    try:
        yield
    finally:
        os.close(descriptor)
        try:
            lock.unlink(missing_ok=True)
        except OSError:
            pass


def _depth(args: Namespace) -> str:
    chosen = [name for name in ("minimal", "standard", "full") if getattr(args, name, False)]
    if len(chosen) > 1:
        raise ValueError("choose only one of --minimal, --standard, or --full")
    return chosen[0] if chosen else "standard"


def _project_record(inspection: dict, profiles: list[str], likely_tasks: list[str]) -> dict:
    return {
        "schema_version": "1.0.0",
        "registry_version": "0.2.1",
        "project_root": ".",
        "languages": inspection["languages"],
        "frameworks": inspection["frameworks"],
        "project_types": inspection["project_types"],
        "selected_profiles": profiles,
        "features": inspection["features"],
        "signals": inspection["signals"],
        "likely_task_families": likely_tasks,
        "host_capabilities": inspection["host_capabilities"],
    }


def _ensure_skill_state(root: Path, *, force: bool) -> list:
    """Ask the Skill workstream to create its state, with a safe empty fallback."""
    try:
        from ..skills.map import ensure_skill_map  # type: ignore
    except (ImportError, AttributeError):
        return [write_owned_json(root, "skill-map.json", {"schema_version": "1.0.0", "skills": []}, force=force)]
    target = owned_path(root, "skill-map.json")
    existed = target.exists()
    before = target.read_bytes() if existed else None
    result = ensure_skill_map(root, write=True)
    after = target.read_bytes()
    action = "unchanged" if existed and before == after else "created" if not existed else "updated"
    return [WriteResult(target, action)]


def initialize_project(
    path: str | Path | None = None,
    *,
    profile: str | None = None,
    no_detect: bool = False,
    depth: str = "standard",
    force: bool = False,
) -> dict:
    resolution = resolve_project_root(path)
    root = resolution.root
    if profile and profile not in PROFILES:
        raise ValueError(f"unknown project profile: {profile}")
    inspection = inspect_project(root, no_detect=no_detect)
    profiles = select_profiles(inspection, [profile] if profile else None)
    recommendation = recommend_project(root, preferred_profiles=profiles, inspection=inspection)
    project_record = _project_record(inspection, profiles, recommendation["likely_recipes"])
    # Establish the owned directory once before individual atomic writes. This
    # removes a first-run directory-creation race when multiple agents or shells
    # initialize the same project concurrently.
    harness_root(root).mkdir(parents=True, exist_ok=True)
    with _initialization_lock(harness_root(root)):
        results = [
            write_owned_json(root, "project.json", project_record, force=force),
            write_owned_json(
                root, "config.json",
                default_config(
                    preferred_profiles=[profile] if profile else [],
                    reference_roots=inspection["reference_roots"],
                    install_depth=depth,
                ),
                force=force,
            ),
            write_owned_json(root, "lock.json", default_lockfile(), force=force),
            write_owned_text(root, "agents/generic.md", generate_fragment("generic"), force=force),
        ]
        if depth in {"standard", "full"}:
            results.append(write_owned_json(root, "task-map.json", build_task_map(recommendation, inspection["features"]), force=force))
            results.extend(_ensure_skill_state(root, force=force))
            for provider in (provider for provider in PROVIDERS if provider != "generic"):
                results.append(write_owned_text(root, f"agents/{provider}.md", generate_fragment(provider), force=force))
            for relative in ("skills", "briefs"):
                (harness_root(root) / relative).mkdir(parents=True, exist_ok=True)
        if depth == "full":
            (harness_root(root) / "runtime" / "session").mkdir(parents=True, exist_ok=True)
            events = harness_root(root) / "runtime" / "task-events.jsonl"
            if not events.exists():
                events.write_bytes(b"")
    return {
        "schema_version": "1.0.0",
        "project_root": str(root),
        "root_source": resolution.source,
        "depth": depth,
        "profiles": profiles,
        "likely_task_families": recommendation["likely_recipes"],
        "created": [item.path.relative_to(root).as_posix() for item in results if item.action == "created"],
        "updated": [item.path.relative_to(root).as_posix() for item in results if item.action == "updated"],
        "unchanged": [item.path.relative_to(root).as_posix() for item in results if item.action == "unchanged"],
        "preserved": [item.path.relative_to(root).as_posix() for item in results if item.action == "preserved"],
        "host_files_modified": [],
    }


def command_init(args: Namespace) -> int:
    try:
        result = initialize_project(
            getattr(args, "path", None),
            profile=getattr(args, "profile", None),
            no_detect=bool(getattr(args, "no_detect", False)),
            depth=_depth(args),
            force=bool(getattr(args, "force", False)),
        )
    except (OSError, RuntimeError, ValueError) as error:
        print(f"init failed: {error}")
        return 1
    if getattr(args, "json", False):
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print("Upgradeables Harness initialized.")
        print("Project: " + result["project_root"])
        print("Likely task families: " + ", ".join(result["likely_task_families"]))
        if result["preserved"]:
            print("Preserved existing harness files: " + ", ".join(result["preserved"]))
        print("Nothing was added to AGENTS.md, CLAUDE.md, or Copilot instructions.")
        print('Next: upgradeables task "<current task>"')
    return 0


run_init = command_init
