"""Read the bundled snapshot without assuming a source checkout exists."""
from __future__ import annotations

import json
from functools import lru_cache
from importlib.resources import files

DATA_PACKAGE = "upgradeables_harness.data"


@lru_cache(maxsize=None)
def _load(name: str):
    resource = files(DATA_PACKAGE).joinpath(name)
    return json.loads(resource.read_text(encoding="utf-8"))


def load_catalog():
    return _load("catalog.json")


def load_recipes():
    return _load("recipes.json")


def load_profiles():
    return _load("profiles.json")


def load_aliases():
    return _load("aliases.json")


def load_ontology():
    return _load("ontology.json")


def load_manifest():
    return _load("registry-manifest.json")


def load_snapshot():
    return {
        "manifest": load_manifest(),
        "catalog": load_catalog(),
        "recipes": load_recipes(),
        "profiles": load_profiles(),
        "aliases": load_aliases(),
        "ontology": load_ontology(),
    }


def get_component(slug: str):
    return next((item for item in load_catalog()["components"] if item["slug"] == slug), None)


def get_recipe(slug: str):
    return next((item for item in load_recipes()["recipes"] if item["slug"] == slug), None)
