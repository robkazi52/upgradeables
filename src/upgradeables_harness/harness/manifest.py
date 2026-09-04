"""Deterministic harness-owned JSON I/O."""
from __future__ import annotations

import json
import os
import tempfile
import time
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


def _atomic_write(target: Path, payload: bytes) -> None:
    """Atomically replace *target* without sharing a temporary name.

    A unique sibling file matters when two shells initialize the same project at
    once.  A fixed ``.tmp`` name lets the writers delete or replace each other's
    staging file, which is especially visible on Windows.
    """
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{target.name}.", suffix=".upgradeables-tmp", dir=target.parent
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as stream:
            stream.write(payload)
            stream.flush()
            os.fsync(stream.fileno())
        for attempt in range(8):
            try:
                os.replace(temporary, target)
                break
            except PermissionError:
                # Windows can briefly deny a concurrent replacement even after
                # the other writer has closed its handle. If that writer
                # installed the same deterministic bytes, our work is complete.
                try:
                    if target.read_bytes() == payload:
                        break
                except OSError:
                    pass
                if attempt == 7:
                    raise
                time.sleep(0.005 * (attempt + 1))
    finally:
        try:
            temporary.unlink(missing_ok=True)
        except OSError:
            pass


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
    _atomic_write(target, expected)
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
    _atomic_write(target, payload)
    return WriteResult(target, "updated" if existed else "created")


def read_json(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"expected JSON object: {path}")
    return value
