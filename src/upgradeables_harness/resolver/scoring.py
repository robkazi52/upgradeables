"""Transparent text scoring primitives."""
from __future__ import annotations

from collections.abc import Iterable

from upgradeables_harness.registry.query import normalize, tokens


def score_values(query: str, values: Iterable[str], *, weight: int = 1):
    query_text = normalize(query)
    query_tokens = tokens(query)
    score = 0
    matched: set[str] = set()
    for raw in values:
        value = normalize(raw)
        if not value:
            continue
        overlap = query_tokens & tokens(value)
        if value == query_text:
            score += weight * 8
            matched.add(raw)
        elif len(value) >= 4 and value in query_text:
            score += weight * 4
            matched.add(raw)
        if overlap:
            score += weight * len(overlap)
            matched.update(overlap)
    return score, sorted(matched, key=str.casefold)


def score_fields(query: str, record: dict, weights: dict[str, int]):
    total = 0
    matched: set[str] = set()
    field_matches = []
    for field, weight in weights.items():
        value = record.get(field, [])
        values = value if isinstance(value, list) else [value]
        score, evidence = score_values(query, (str(item) for item in values), weight=weight)
        if score:
            field_matches.append({"field": field, "score": score, "matched": evidence[:6]})
            matched.update(evidence)
            total += score
    return total, sorted(matched, key=str.casefold)[:10], field_matches


def level_index(level: str) -> int:
    return int(level[1:])
