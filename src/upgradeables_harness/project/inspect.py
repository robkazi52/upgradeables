"""Project inspection API and CLI handler."""
from __future__ import annotations

import json
from argparse import Namespace
from pathlib import Path

from .capabilities import detect_host_capabilities
from .detectors import detect_project_signals
from .root import resolve_project_root


def inspect_project(project: str | Path | None = None, *, no_detect: bool = False) -> dict:
    resolution = resolve_project_root(project)
    detected = {
        "languages": [], "frameworks": [], "project_types": ["general"],
        "features": {
            "git": False, "tests": False, "documentation": False,
            "ci": False, "pull_requests": False, "long_context": False,
        },
        "signals": [], "reference_roots": [],
    } if no_detect else detect_project_signals(resolution.root)
    return {
        "schema_version": "1.0.0",
        "project_root": ".",
        "selected_root": str(resolution.root),
        "root_source": resolution.source,
        **detected,
        "host_capabilities": detect_host_capabilities(resolution.root),
    }


def _summary(result: dict) -> str:
    features = result["features"]
    types = ", ".join(result["project_types"]) or "general"
    languages = ", ".join(result["languages"]) or "none detected"
    return "\n".join([
        f"Project root: {result['selected_root']} ({result['root_source']})",
        f"Project types: {types}",
        f"Languages: {languages}",
        "Signals: " + ", ".join(
            name for name in ("git", "tests", "documentation", "ci", "long_context")
            if features[name]
        ) if any(features.values()) else "Signals: none detected",
        "Inspection was shallow and read-only; no project code was executed.",
    ])


def command_inspect(args: Namespace) -> int:
    try:
        result = inspect_project(getattr(args, "project", None))
    except (OSError, ValueError) as error:
        print(f"inspect failed: {error}")
        return 1
    if getattr(args, "json", False):
        print(json.dumps(result, indent=2, sort_keys=True))
    else:
        print(_summary(result))
    return 0


run_inspect = command_inspect
