"""Exact local harness and component version locks."""
from __future__ import annotations

from ..registry.load import load_manifest


def default_lockfile() -> dict:
    manifest = load_manifest()
    registry_version = manifest.get("registry_version")
    if registry_version != "0.2.1":
        raise ValueError(f"bundled registry must be 0.2.1, found {registry_version!r}")
    return {
        "schema_version": "1.0.0",
        "harness_version": manifest.get("harness_version", "0.3.0"),
        "registry_version": registry_version,
        "registry_source": {
            "type": "bundled",
            "commit": manifest.get("source_commit", "unknown"),
            "tag": manifest.get("source_tag"),
            "snapshot_hash": manifest.get("snapshot_hash"),
        },
        "components": {},
        "skills": {},
    }
