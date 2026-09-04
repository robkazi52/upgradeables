"""Project-local harness configuration."""
from __future__ import annotations


def default_config(
    *,
    preferred_profiles: list[str] | None = None,
    reference_roots: list[str] | None = None,
    install_depth: str = "standard",
) -> dict:
    return {
        "schema_version": "1.0.0",
        "profile_mode": "fixed" if preferred_profiles else "auto",
        "install_depth": install_depth,
        "preferred_profiles": preferred_profiles or [],
        "agent_integrations": [],
        "record_task_events": False,
        "skill_suggestion_threshold": 3,
        "reference_roots": reference_roots or [],
        "network": {"allow_registry_update": False},
        "runtime": {
            "enabled": True,
            "default_model_profile": "medium",
            "max_directive_tokens": 500,
            "debug": False,
        },
        "models": {},
    }
