"""Provider-neutral approximate instruction budgeting."""
from __future__ import annotations


def estimate_tokens(text: str) -> int:
    """Return a deliberately labelled approximation (roughly four chars/token)."""
    return (len(text) + 3) // 4


def lower_level(level: str) -> str | None:
    return {"full": "standard", "standard": "micro", "micro": None}[level]
