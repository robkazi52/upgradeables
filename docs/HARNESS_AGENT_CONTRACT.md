# Harness Agent Contract

An agent using a project harness should:

1. Read `.upgradeables/project.json` and `.upgradeables/task-map.json` when present.
2. Classify the current task before choosing controls.
3. Prefer one primary recipe.
4. Evaluate recipe `R/A/C/O/X` roles, then canonical triggers and non-triggers.
5. Resolve dependencies, conflicts, and counterbalances.
6. Use the smallest sufficient composition within the task's complexity ceiling.
7. Respect exact component versions in `.upgradeables/lock.json`.
8. Use a validated project Skill when it matches the current task.
9. Consider a Skill only for a genuinely recurring workflow and store project Skills under `.upgradeables/skills/`.
10. Keep project state explicit; do not claim hidden memory or learning.
11. Do not edit the global registry merely because this project uses it.

The harness files do not grant shell, network, write, external-action, or approval authority. Availability and permission must be established separately for the current host and task.
