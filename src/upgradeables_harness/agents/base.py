"""Agent fragment registry and integration command handler."""
from __future__ import annotations

import json
from argparse import Namespace
from importlib import import_module
from pathlib import Path

from ..project.root import resolve_project_root
from .managed_block import ManagedBlockError, insert_or_update_managed_block, remove_managed_block, update_file

PROVIDERS = ("generic", "codex", "claude", "copilot")
HOST_PATHS = {
    "generic": "UPGRADEABLES.md",
    "codex": "AGENTS.md",
    "claude": "CLAUDE.md",
    "copilot": ".github/copilot-instructions.md",
}


def generate_fragment(provider: str) -> str:
    if provider not in PROVIDERS:
        raise ValueError(f"unknown integration provider: {provider}")
    module = import_module(f"{__package__}.{provider}")
    return module.fragment().strip() + "\n"


def fragment_path(project_root: Path, provider: str) -> Path:
    return project_root / ".upgradeables" / "agents" / f"{provider}.md"


def host_path(project_root: Path, provider: str) -> Path:
    target = project_root / HOST_PATHS[provider]
    root = project_root.resolve()
    if not target.resolve(strict=False).is_relative_to(root):
        raise ValueError("integration target escapes the project root")
    return target


def command_integrate(args: Namespace) -> int:
    provider = getattr(args, "provider", "list")
    as_json = getattr(args, "json", False)
    if provider == "list":
        result = {"providers": list(PROVIDERS), "writes": False}
        print(json.dumps(result, indent=2, sort_keys=True) if as_json else "\n".join(PROVIDERS))
        return 0
    if provider not in PROVIDERS:
        print(f"integrate failed: unknown provider {provider!r}")
        return 1
    write = bool(getattr(args, "write", False))
    remove = bool(getattr(args, "remove", False))
    if write and remove:
        print("integrate failed: --write and --remove are mutually exclusive")
        return 1
    try:
        resolution = resolve_project_root(getattr(args, "project", None))
        root = resolution.root
        if not (root / ".upgradeables").is_dir():
            raise FileNotFoundError(".upgradeables not found; run upgradeables init first")
        fragment = generate_fragment(provider)
        target = host_path(root, provider)
        original = target.read_bytes().decode("utf-8") if target.exists() else ""
        if remove:
            preview = remove_managed_block(original)
            result = update_file(target, fragment, remove=True)
        elif write:
            preview = insert_or_update_managed_block(original, fragment)
            result = update_file(target, fragment)
        else:
            preview = insert_or_update_managed_block(original, fragment)
            result = preview
    except (OSError, UnicodeError, ValueError, ManagedBlockError) as error:
        print(f"integrate failed: {error}")
        return 1
    output = {
        "schema_version": "1.0.0",
        "provider": provider,
        "project_root": str(root),
        "target": target.relative_to(root).as_posix(),
        "mode": "remove" if remove else "write" if write else "preview",
        "action": result.action,
        "changed": result.changed,
        "fragment": fragment,
        "preview": preview.text,
    }
    if as_json:
        print(json.dumps(output, indent=2, sort_keys=True))
    elif write or remove:
        print(f"{provider}: {result.action} managed block in {output['target']}")
    else:
        print(fragment, end="")
        print(f"\nPreview only; {output['target']} was not modified. Use --write to apply.")
    return 0


run_integrate = command_integrate
