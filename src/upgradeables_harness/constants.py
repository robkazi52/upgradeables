"""Stable harness constants."""

HARNESS_VERSION = "0.4.0"
REGISTRY_VERSION = "0.2.1"
AGGREGATE_REGISTRY_SCHEMA_VERSION = "1.0.0"
COMPONENT_SCHEMA_VERSION = "2.0.0"
HARNESS_DIRECTORY = ".upgradeables"
SOURCE_REPOSITORY = "https://github.com/robkazi52/upgradeables"

ROLE_GROUPS = {
    "R": "required_by_recipe",
    "A": "trigger_likely",
    "C": "conditional",
    "O": "optional",
    "X": "excluded",
}

COMPLEXITY_ORDER = ("L0", "L1", "L2", "L3", "L4", "L5")
