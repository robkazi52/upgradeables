"""Command-line interface for the Upgradeables project harness."""
from __future__ import annotations

import argparse
import importlib
import json
import sys
from pathlib import Path

from .constants import HARNESS_VERSION
from .registry.load import load_manifest
from .resolver.explain import render_task
from .resolver.task import resolve_task


def _lazy(module: str, function: str, args):
    try:
        handler = getattr(importlib.import_module(module), function)
    except (ImportError, AttributeError) as error:
        print(f"Command implementation unavailable: {module}.{function}: {error}", file=sys.stderr)
        return 2
    result = handler(args)
    return 0 if result is None else int(result)


def _find_project(start: str | None):
    if start:
        return Path(start)
    current = Path.cwd().resolve()
    for candidate in (current, *current.parents):
        if (candidate / ".upgradeables" / "project.json").is_file():
            return candidate
    return None


def command_task(args):
    project = _find_project(args.project) if not args.no_project_profile else None
    result = resolve_task(args.task, project=project,
                          use_project_profile=not args.no_project_profile)
    if args.record:
        if project is None:
            print("Task recording requires an initialized project; run `upgradeables init` first.", file=sys.stderr)
            return 2
        try:
            history = importlib.import_module("upgradeables_harness.skills.history")
            component_groups = (
                "required_by_recipe", "trigger_likely", "conditional", "optional",
                "needs_agent_evaluation",
            )
            event = {
                "raw_task": result["query"],
                "normalized_task": result["normalized_task"],
                "task_archetype": result["task"]["archetype"],
                "selected_recipe": result["best_recipe"]["slug"] if result["best_recipe"] else None,
                "candidate_components": [
                    item["slug"] for key in component_groups for item in result[key]
                ],
                "environment_modifiers": {
                    key: value for key, value in result["environment"].items() if value is not None
                },
                "authority_mode": "review" if result["environment"].get("review_only") else (
                    "edit" if result["environment"].get("editing_requested") else "unspecified"
                ),
                "component_composition": [
                    f"{item['slug']}@{item['version']}"
                    for item in result["required_by_recipe"] + result["trigger_likely"]
                ],
            }
            history.record_task_event(project, event, explicitly_requested=True)
        except (ImportError, AttributeError) as error:
            print(f"Task recording unavailable: {error}", file=sys.stderr)
            return 2
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        sys.stdout.write(render_task(result, explain=args.explain))
    return 0


def command_version(args):
    manifest = load_manifest()
    project = _find_project(args.project)
    lock_version = None
    if project:
        lock = project / ".upgradeables" / "lock.json"
        if lock.is_file():
            try:
                lock_version = json.loads(lock.read_text(encoding="utf-8")).get("registry_version")
            except (OSError, json.JSONDecodeError):
                lock_version = "invalid"
    result = {
        "harness_version": HARNESS_VERSION,
        "bundled_registry_version": manifest["registry_version"],
        "aggregate_registry_schema_version": manifest["aggregate_registry_schema_version"],
        "component_schema_version": manifest["component_schema_version"],
        "registry_commit": manifest["source_commit"],
        "project_lock": lock_version,
    }
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Upgradeables Harness: {result['harness_version']}")
        print(f"Bundled registry: {result['bundled_registry_version']}")
        print(f"Registry schemas: aggregate {result['aggregate_registry_schema_version']}; components {result['component_schema_version']}")
        print(f"Registry commit: {result['registry_commit']}")
        print(f"Project lock: {result['project_lock'] or 'none'}")
    return 0


def command_update(args):
    if args.apply:
        print("Registry update apply is not implemented in v0.3.0; pinned projects were not changed.", file=sys.stderr)
        return 2
    if not args.check:
        print("Use `upgradeables update --check`; network access is explicit.", file=sys.stderr)
        return 2
    from .registry.update import check_for_update
    try:
        result = check_for_update()
    except Exception as error:  # Network and protocol failures become explicit CLI errors.
        print(f"Registry update check failed: {error}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Bundled registry: {result['current_registry_version']}")
        print(f"Remote registry: {result['remote_registry_version']}")
        print("Update available." if result["update_available"] else "No registry update detected.")
    return 0


def build_parser():
    parser = argparse.ArgumentParser(prog="upgradeables", description="Local-first Upgradeables project harness")
    parser.add_argument("--version", action="version", version=f"%(prog)s {HARNESS_VERSION}")
    commands = parser.add_subparsers(dest="command", required=True)

    init = commands.add_parser("init", help="initialize a project-local harness")
    init.add_argument("path", nargs="?")
    init.add_argument("--profile")
    init.add_argument("--no-detect", action="store_true")
    depth = init.add_mutually_exclusive_group()
    depth.add_argument("--minimal", action="store_true")
    depth.add_argument("--standard", action="store_true")
    depth.add_argument("--full", action="store_true")
    init.add_argument("--force", action="store_true")
    init.add_argument("--json", action="store_true")
    init.set_defaults(handler=lambda a: _lazy("upgradeables_harness.harness.init", "command_init", a))

    inspect = commands.add_parser("inspect", help="inspect project signals without executing code")
    inspect.add_argument("--project")
    inspect.add_argument("--json", action="store_true")
    inspect.set_defaults(handler=lambda a: _lazy("upgradeables_harness.project.inspect", "command_inspect", a))

    recommend = commands.add_parser("recommend", help="show project-level selection priors")
    recommend.add_argument("--project")
    recommend.add_argument("--json", action="store_true")
    recommend.set_defaults(handler=lambda a: _lazy("upgradeables_harness.project.profile", "command_recommend", a))

    task = commands.add_parser("task", help="resolve a natural-language task deterministically")
    task.add_argument("task")
    task.add_argument("--json", action="store_true")
    task.add_argument("--explain", action="store_true")
    task.add_argument("--project")
    task.add_argument("--no-project-profile", action="store_true")
    task.add_argument("--record", action="store_true")
    task.set_defaults(handler=command_task)

    skill = commands.add_parser("skill", help="project Skill factory")
    skills = skill.add_subparsers(dest="skill_command", required=True)
    brief = skills.add_parser("brief")
    brief.add_argument("task")
    brief.add_argument("--project")
    brief.add_argument("--json", action="store_true")
    brief.set_defaults(handler=lambda a: _lazy("upgradeables_harness.skills.brief", "command_brief", a))
    scaffold = skills.add_parser("scaffold")
    scaffold.add_argument("slug")
    scaffold.add_argument("--task")
    scaffold.add_argument("--project")
    scaffold.add_argument("--force", action="store_true")
    scaffold.add_argument("--json", action="store_true")
    scaffold.set_defaults(handler=lambda a: _lazy("upgradeables_harness.skills.scaffold", "command_scaffold", a))
    listing = skills.add_parser("list")
    listing.add_argument("--project")
    listing.add_argument("--json", action="store_true")
    listing.set_defaults(handler=lambda a: _lazy("upgradeables_harness.skills.scaffold", "command_list", a))
    validate = skills.add_parser("validate")
    validate.add_argument("path")
    validate.add_argument("--draft", action="store_true")
    validate.add_argument("--json", action="store_true")
    validate.set_defaults(handler=lambda a: _lazy("upgradeables_harness.skills.validate", "command_validate", a))
    suggest = skills.add_parser("suggest")
    suggest.add_argument("--project")
    suggest.add_argument("--json", action="store_true")
    suggest.set_defaults(handler=lambda a: _lazy("upgradeables_harness.skills.suggest", "command_suggest", a))

    integrate = commands.add_parser("integrate", help="preview or manage agent instruction fragments")
    integrate.add_argument("provider", choices=("list", "codex", "claude", "copilot", "generic"))
    integrate.add_argument("--project")
    writes = integrate.add_mutually_exclusive_group()
    writes.add_argument("--write", action="store_true")
    writes.add_argument("--remove", action="store_true")
    integrate.add_argument("--json", action="store_true")
    integrate.set_defaults(handler=lambda a: _lazy("upgradeables_harness.agents.base", "command_integrate", a))

    doctor = commands.add_parser("doctor", help="diagnose project harness state")
    doctor.add_argument("--project")
    doctor.add_argument("--fix", action="store_true")
    doctor.add_argument("--json", action="store_true")
    doctor.set_defaults(handler=lambda a: _lazy("upgradeables_harness.harness.doctor", "command_doctor", a))

    update = commands.add_parser("update", help="explicitly check registry releases")
    update_mode = update.add_mutually_exclusive_group()
    update_mode.add_argument("--check", action="store_true")
    update_mode.add_argument("--apply", action="store_true")
    update.add_argument("--json", action="store_true")
    update.set_defaults(handler=command_update)

    version = commands.add_parser("version", help="show harness and registry versions")
    version.add_argument("--project")
    version.add_argument("--json", action="store_true")
    version.set_defaults(handler=command_version)
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.handler(args)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        if getattr(args, "json", False):
            print(json.dumps({"error": str(error), "command": args.command}), file=sys.stderr)
        else:
            print(f"upgradeables: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
