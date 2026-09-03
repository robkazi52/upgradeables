"""Deterministic harness-owned JSON I/O."""
from __future__ import annotations

import json
import os
from dataclasses import dataclass
from pathlib import Path

HARNESS_DIRECTORY = ".upgradeables"


@dataclass(frozen=True)
class WriteResult:
    path: Path
    action: str


def harness_root(project_root: Path) -> Path:
    target = project_root / HARNESS_DIRECTORY
    if target.is_symlink():
        raise ValueError(f"refusing harness symlink: {target}")
    resolved_root = project_root.resolve()
    if not target.resolve(strict=False).is_relative_to(resolved_root):
        raise ValueError("harness directory escapes project root")
    return target


def owned_path(project_root: Path, relative: str | Path) -> Path:
    base = harness_root(project_root)
    target = base / relative
    if not target.resolve(strict=False).is_relative_to(base.resolve(strict=False)):
        raise ValueError(f"harness path escapes .upgradeables: {relative}")
    if target.is_symlink():
        raise ValueError(f"refusing harness-owned symlink: {target}")
    return target


def encode_json(value: object) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def write_owned_json(
    project_root: Path,
    relative: str | Path,
    value: object,
    *,
    force: bool = False,
) -> WriteResult:
    target = owned_path(project_root, relative)
    expected = encode_json(value)
    existed = target.exists()
    if existed:
        current = target.read_bytes()
        if current == expected:
            return WriteResult(target, "unchanged")
        if not force:
            return WriteResult(target, "preserved")
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_name(target.name + ".upgradeables-tmp")
    temporary.write_bytes(expected)
    os.replace(temporary, target)
    return WriteResult(target, "updated" if existed else "created")


def write_owned_text(
    project_root: Path,
    relative: str | Path,
    text: str,
    *,
    force: bool = False,
) -> WriteResult:
    target = owned_path(project_root, relative)
    expected = text.replace("\r\n", "\n").replace("\r", "\n").rstrip() + "\n"
    payload = expected.encode("utf-8")
    existed = target.exists()
    if existed:
        current = target.read_bytes()
        if current == payload:
            return WriteResult(target, "unchanged")
        if not force:
            return WriteResult(target, "preserved")
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_name(target.name + ".upgradeables-tmp")
    temporary.write_bytes(payload)
    os.replace(temporary, target)
    return WriteResult(target, "updated" if existed else "created")


def read_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value
