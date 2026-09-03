"""Low-level deterministic registry querying."""
from __future__ import annotations

import re

from .load import load_aliases, load_catalog, load_recipes

STOPWORDS = {
    "a", "an", "and", "are", "for", "from", "i", "in", "is", "it", "me",
    "my", "of", "on", "or", "please", "the", "this", "to", "with",
}


def normalize(value: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", str(value).casefold()))


def tokens(value: str) -> set[str]:
    result: set[str] = set()
    for token in normalize(value).split():
        if token in STOPWORDS:
            continue
        result.add(token)
        if len(token) > 4 and token.endswith("s"):
            result.add(token[:-1])
        if len(token) > 5 and token.endswith("ing"):
            result.add(token[:-3])
    return result


def search(query: str, *, kinds=("component", "recipe"), limit=10):
    phrase = normalize(query)
    wanted = tokens(query)
    results = []
    if "component" in kinds:
        for item in load_catalog()["components"]:
            fields = [item["slug"], item["display_name"], item["plain_display_name"],
                      item["purpose"], *item.get("plain_aliases", []),
                      *item.get("task_phrases", []), *item.get("best_fit_tasks", [])]
            normalized = [normalize(value) for value in fields]
            overlap = wanted & set().union(*(tokens(value) for value in fields))
            if phrase in normalized or overlap:
                exact = int(phrase in normalized)
                results.append({"kind": "component", "slug": item["slug"],
                                "score": exact * 100 + len(overlap), "matched": sorted(overlap)})
    if "recipe" in kinds:
        for item in load_recipes()["recipes"]:
            fields = [item["slug"], item["display_name"], item["purpose"],
                      item["task_family"], *item.get("task_phrases", [])]
            normalized = [normalize(value) for value in fields]
            overlap = wanted & set().union(*(tokens(value) for value in fields))
            if phrase in normalized or overlap:
                exact = int(phrase in normalized)
                results.append({"kind": "recipe", "slug": item["slug"],
                                "score": exact * 100 + len(overlap), "matched": sorted(overlap)})
    results.sort(key=lambda item: (-item["score"], item["kind"], item["slug"]))
    return results if not limit else results[:limit]


def resolve_alias(label: str):
    normalized = normalize(label)
    matches = [row for row in load_aliases()["aliases"] if normalize(row["label"]) == normalized]
    matches.sort(key=lambda row: (row["kind"] == "historical-alias", row["slug"]))
    return matches
