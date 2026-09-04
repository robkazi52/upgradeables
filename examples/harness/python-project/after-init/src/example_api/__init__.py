"""Synthetic public API used by the harness example."""


def normalize_name(value: str, *, strict: bool = False) -> str:
    """Return a normalized public name."""
    result = value.strip()
    if strict and not result:
        raise ValueError("name must not be empty")
    return result
