# Repair Bundle

Choose repair depth while protecting locked content and interfaces.

## Activation boundary

Activate after locating a defect and deciding whether its scope is local, targeted, or architectural.

## Required and optional components

- [`safe-rewrite@1.1.0`](../../upgradeables/editing-repair/safe-rewrite/UPGRADEABLE.md) — required
- [`micro-repair@1.1.0`](../../upgradeables/editing-repair/micro-repair/UPGRADEABLE.md) — optional; activate by trigger
- [`regenerative-rewrite@1.1.0`](../../upgradeables/editing-repair/regenerative-rewrite/UPGRADEABLE.md) — optional; activate by trigger
- [`crispr-edit@1.1.0`](../../upgradeables/editing-repair/crispr-edit/UPGRADEABLE.md) — optional; activate by trigger
- [`surgery-edit@1.1.0`](../../upgradeables/editing-repair/surgery-edit/UPGRADEABLE.md) — optional; activate by trigger
- [`contradiction-micro-repair@1.1.0`](../../upgradeables/editing-repair/contradiction-micro-repair/UPGRADEABLE.md) — optional; activate by trigger

## Load order and critical interactions

Use the metadata `load_order`. Failure boundaries escalate from micro repair toward surgery; deeper editors must preserve declared invariants.

## Over-scaffolding boundary

Excessive when multiple editors compete or an architectural rewrite is used for a local defect.
