# Architect Bundle

Design or restructure a composed Skill system without losing interfaces or authority.

## Activation boundary

Activate for multi-component architecture work, not a small prompt edit.

## Required and optional components

- [`architect-orchestrator@1.1.0`](../../upgradeables/orchestration/architect-orchestrator/UPGRADEABLE.md) — required
- [`behavior-gene-builder@1.1.0`](../../upgradeables/meta-control/behavior-gene-builder/UPGRADEABLE.md) — optional; activate by trigger
- [`domain-core-builder@1.1.0`](../../upgradeables/meta-control/domain-core-builder/UPGRADEABLE.md) — optional; activate by trigger
- [`adapter-first-experimentation@1.1.0`](../../upgradeables/meta-control/adapter-first-experimentation/UPGRADEABLE.md) — optional; activate by trigger
- [`crispr-edit@1.1.0`](../../upgradeables/editing-repair/crispr-edit/UPGRADEABLE.md) — optional; activate by trigger
- [`surgery-edit@1.1.0`](../../upgradeables/editing-repair/surgery-edit/UPGRADEABLE.md) — optional; activate by trigger
- [`scoped-loader@1.1.0`](../../upgradeables/context-retrieval/scoped-loader/UPGRADEABLE.md) — required
- [`state-snapshot@1.1.0`](../../upgradeables/state/state-snapshot/UPGRADEABLE.md) — required
- [`ultimate-suite-supervisor@1.1.0`](../../upgradeables/meta-control/ultimate-suite-supervisor/UPGRADEABLE.md) — optional; activate by trigger

## Load order and critical interactions

Use the metadata `load_order`. The orchestrator selects builders and edit depth; snapshots preserve handoffs.

## Over-scaffolding boundary

Excessive for a single bounded Skill or documentation-only change.
