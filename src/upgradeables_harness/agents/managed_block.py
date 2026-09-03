"""Byte-stable Markdown managed-block operations."""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

START_MARKER = "<!-- upgradeables-harness:start -->"
END_MARKER = "<!-- upgradeables-harness:end -->"


class ManagedBlockError(ValueError):
    """Raised when markers are malformed or ambiguous."""


@dataclass(frozen=True)
class ManagedBlockResult:
    text: str
    action: str
    changed: bool


def _span(text: str) -> tuple[int, int] | None:
    starts = [index for index in range(len(text)) if text.startswith(START_MARKER, index)]
    ends = [index for index in range(len(text)) if text.startswith(END_MARKER, index)]
    if not starts and not ends:
        return None
    if len(starts) != 1 or len(ends) != 1 or starts[0] >= ends[0]:
        raise ManagedBlockError("managed block has missing, doubled, or out-of-order markers")
    end = ends[0] + len(END_MARKER)
    if START_MARKER in text[starts[0] + len(START_MARKER):end - len(END_MARKER)]:
        raise ManagedBlockError("managed block contains nested markers")
    return starts[0], end


def validate_managed_block(text: str) -> bool:
    _span(text)
    return True


def render_managed_block(fragment: str, newline: str = "\n") -> str:
    if START_MARKER in fragment or END_MARKER in fragment:
        raise ManagedBlockError("fragment must not contain managed-block markers")
    body = fragment.strip().replace("\r\n", "\n").replace("\r", "\n")
    body = body.replace("\n", newline)
    return newline.join((START_MARKER, body, END_MARKER))


def insert_or_update_managed_block(text: str, fragment: str) -> ManagedBlockResult:
    newline = "\r\n" if "\r\n" in text else "\n"
    block = render_managed_block(fragment, newline)
    span = _span(text)
    if span is None:
        separator = "" if not text or text.endswith(("\n", "\r")) else newline
        suffix = newline
        updated = text + separator + block + suffix
        return ManagedBlockResult(updated, "inserted", updated != text)
    start, end = span
    updated = text[:start] + block + text[end:]
    return ManagedBlockResult(updated, "unchanged" if updated == text else "updated", updated != text)


def remove_managed_block(text: str) -> ManagedBlockResult:
    span = _span(text)
    if span is None:
        return ManagedBlockResult(text, "absent", False)
    start, end = span
    updated = text[:start] + text[end:]
    return ManagedBlockResult(updated, "removed", True)


def update_file(path: Path, fragment: str, *, remove: bool = False) -> ManagedBlockResult:
    if path.is_symlink():
        raise ManagedBlockError(f"refusing to modify symlink: {path}")
    original = path.read_bytes().decode("utf-8") if path.exists() else ""
    result = remove_managed_block(original) if remove else insert_or_update_managed_block(original, fragment)
    if result.changed:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(result.text.encode("utf-8"))
    return result
