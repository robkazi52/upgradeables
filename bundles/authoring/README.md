# Authoring Bundle

Produce controlled writing while separating style, pedagogy, evidence, and placeholders.

## Activation boundary

Activate only the controls demanded by the deliverable.

## Required and optional components

- [`style-alignment@1.1.0`](../../upgradeables/output/style-alignment/UPGRADEABLE.md) — required
- [`pedagogical-alignment@1.1.0`](../../upgradeables/output/pedagogical-alignment/UPGRADEABLE.md) — optional; activate by trigger
- [`safe-rewrite@1.1.0`](../../upgradeables/editing-repair/safe-rewrite/UPGRADEABLE.md) — optional; activate by trigger
- [`citation-fidelity@1.1.0`](../../upgradeables/validation/citation-fidelity/UPGRADEABLE.md) — optional; activate by trigger
- [`placeholder-suppression@1.1.0`](../../upgradeables/output/placeholder-suppression/UPGRADEABLE.md) — required

## Load order and critical interactions

Use the metadata `load_order`. Safe Rewrite protects locked meaning while style or pedagogy changes.

## Over-scaffolding boundary

Excessive for unconstrained prose with no sources, locked content, or template fields.
