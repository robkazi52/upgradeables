"""Snapshot integrity helpers."""
from __future__ import annotations

import hashlib
import json

from .load import load_aliases, load_catalog, load_manifest, load_ontology, load_profiles, load_recipes


def snapshot_hash() -> str:
    payloads = {
        "aliases.json": load_aliases(),
        "catalog.json": load_catalog(),
        "ontology.json": load_ontology(),
        "profiles.json": load_profiles(),
        "recipes.json": load_recipes(),
    }
    digest = hashlib.sha256()
    for name in sorted(payloads):
        digest.update(name.encode("utf-8"))
        digest.update(b"\0")
        text = json.dumps(payloads[name], ensure_ascii=False, indent=2, sort_keys=True) + "\n"
        digest.update(text.encode("utf-8"))
    return f"sha256:{digest.hexdigest()}"


def verify_snapshot() -> tuple[bool, str]:
    actual = snapshot_hash()
    expected = load_manifest()["snapshot_hash"]
    return actual == expected, actual
