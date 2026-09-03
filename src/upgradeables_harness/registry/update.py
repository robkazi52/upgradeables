"""Explicit registry update availability check."""
from __future__ import annotations

import json
from urllib.request import Request, urlopen

from .load import load_catalog, load_manifest, load_recipes

REMOTE_REGISTRY_URL = "https://raw.githubusercontent.com/robkazi52/upgradeables/main/registry/registry.json"


def _changes(local: list[dict], remote: list[dict]):
    local_versions = {item["slug"]: item.get("version") for item in local}
    remote_versions = {item["slug"]: item.get("version") for item in remote}
    return {
        "added": sorted(set(remote_versions) - set(local_versions)),
        "removed": sorted(set(local_versions) - set(remote_versions)),
        "version_changed": sorted(
            slug for slug in set(local_versions) & set(remote_versions)
            if local_versions[slug] != remote_versions[slug]
        ),
    }


def check_for_update(*, opener=urlopen, url: str = REMOTE_REGISTRY_URL, timeout: float = 10.0):
    """Contact the canonical remote registry only when explicitly called."""
    request = Request(url, headers={"Accept": "application/json",
                                    "User-Agent": "upgradeables-harness/0.3.0"})
    with opener(request, timeout=timeout) as response:
        payload = json.load(response)
    current = load_manifest()["registry_version"]
    remote_version = payload.get("registry_version")
    if not isinstance(remote_version, str):
        raise ValueError("remote registry has no registry_version")
    component_changes = _changes(load_catalog()["components"], payload.get("upgradeables", []))
    recipe_changes = _changes(load_recipes()["recipes"], payload.get("recipes", []))
    changed = any(component_changes.values()) or any(recipe_changes.values())
    return {
        "schema_version": "1.0.0",
        "current_registry_version": current,
        "remote_registry_version": remote_version,
        "update_available": remote_version != current or changed,
        "component_changes": component_changes,
        "recipe_changes": recipe_changes,
        "source_url": url,
        "network_used": True,
        "apply_supported": False,
    }
