# Authoring Bundle

Produce controlled writing while separating style, pedagogy, evidence, and placeholders.

## Activation boundary

Activate only the controls demanded by the deliverable.

## Required and optional components

- [`pedagogical-alignment@1.1.0`](../../upgradeables/output/pedagogical-alignment/UPGRADEABLE.md) — optional; activate by trigger
- [`style-alignment@1.1.0`](../../upgradeables/output/style-alignment/UPGRADEABLE.md) — required
- [`safe-rewrite@1.1.0`](../../upgradeables/editing-repair/safe-rewrite/UPGRADEABLE.md) — optional; activate by trigger
- [`citation-fidelity@1.1.0`](../../upgradeables/validation/citation-fidelity/UPGRADEABLE.md) — optional; activate by trigger
- [`placeholder-suppression@1.1.0`](../../upgradeables/output/placeholder-suppression/UPGRADEABLE.md) — optional; activate by trigger

## Load order and critical interactions

Use the metadata `load_order`. Audience and style contracts precede transformation; Citation Fidelity validates sourced claims, and Placeholder Suppression is the finalization gate only when templates are present.

## Over-scaffolding boundary

Excessive for unconstrained prose with no sources, locked content, or template fields.
