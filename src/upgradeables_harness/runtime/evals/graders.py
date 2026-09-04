"""Objective output graders for synthetic runtime tasks."""
from __future__ import annotations

import json


def grade(response: str, specification: dict) -> dict:
    if not isinstance(response, str):
        raise TypeError("objective grader response must be a string")
    if not isinstance(specification, dict) or not isinstance(specification.get("type"), str):
        raise ValueError("objective grader specification requires a string type")
    kind = specification["type"]
    normalized = response.strip()
    details = {}
    if kind == "exact":
        if not isinstance(specification.get("expected"), str):
            raise ValueError("exact grader requires a string expected value")
        success = normalized == specification["expected"]
    elif kind == "contains-all":
        _validate_values(specification, kind)
        missing = [value for value in specification["values"] if value.lower() not in normalized.lower()]
        success = not missing
        details["missing"] = missing
    elif kind == "contains-any":
        _validate_values(specification, kind)
        matched = [value for value in specification["values"] if value.lower() in normalized.lower()]
        success = bool(matched)
        details["matched"] = matched
    elif kind == "excludes":
        _validate_values(specification, kind)
        found = [value for value in specification["values"] if value.lower() in normalized.lower()]
        success = not found
        details["found"] = found
    elif kind == "json-fields":
        fields = specification.get("fields")
        if not isinstance(fields, dict):
            raise ValueError("json-fields grader requires an object fields value")
        try:
            payload = json.loads(normalized)
        except json.JSONDecodeError as error:
            success = False
            details["error"] = str(error)
        else:
            if not isinstance(payload, dict):
                success = False
                details["error"] = "response JSON must be an object"
            else:
                mismatches = {
                    key: {
                        "expected": value,
                        "actual": payload.get(key),
                        "missing": key not in payload,
                    }
                    for key, value in fields.items()
                    if key not in payload or payload[key] != value
                }
                success = not mismatches
                details["mismatches"] = mismatches
    else:
        raise ValueError(f"Unknown objective grader: {kind}")
    return {
        "schema_version": "1.0.0",
        "grader_kind": "deterministic",
        "grader_type": "objective",
        "grader": kind,
        "status": "graded",
        "success": success,
        "score": 1.0 if success else 0.0,
        "details": details,
    }


def _validate_values(specification: dict, kind: str) -> None:
    values = specification.get("values")
    if not isinstance(values, list) or not values or not all(isinstance(value, str) for value in values):
        raise ValueError(f"{kind} grader requires a non-empty array of strings")
