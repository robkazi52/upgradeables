"""Generic project-local agent contract."""


def fragment() -> str:
    return """## Upgradeables Harness

For each task:
1. Read `.upgradeables/project.json` and `.upgradeables/task-map.json`.
2. Classify the current task and prefer one primary recipe.
3. Evaluate recipe R/A/C/O/X roles, then component triggers and non-triggers.
4. Resolve dependencies, conflicts, and counterbalances; use the smallest sufficient composition.
5. Respect versions in `.upgradeables/lock.json` and use a validated project Skill when applicable.
6. Consider a project Skill only for a genuinely recurring workflow; store it under `.upgradeables/skills/`.

These files are selection aids, not always-on activation. Do not edit the global registry merely because this project uses it. Do not assume network, tools, memory, or permissions that the current host has not provided."""
