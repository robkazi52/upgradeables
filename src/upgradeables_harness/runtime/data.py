"""Load installed runtime data without assuming a source checkout."""
from __future__ import annotations

from functools import lru_cache

from ..registry.load import _load


@lru_cache(maxsize=None)
def load_runtime_registry() -> dict:
    return _load("runtime-registry.json")


def runtime_components() -> dict[str, dict]:
    return {item["slug"]: item for item in load_runtime_registry()["components"]}


def load_model_profiles() -> dict:
    return load_runtime_registry()["model_profiles"]


def load_dedupe_groups() -> dict:
    return load_runtime_registry()["dedupe_groups"]
