# Architect Bundle

A curated composition, not an always-on monolith. Activate components only
when their individual triggers apply and preserve repository precedence.

## Components and default load order

- [`architect-orchestrator`](../../upgradeables/orchestration/architect-orchestrator/UPGRADEABLE.md)
- [`behavior-gene-builder`](../../upgradeables/meta-control/behavior-gene-builder/UPGRADEABLE.md)
- [`domain-core-builder`](../../upgradeables/meta-control/domain-core-builder/UPGRADEABLE.md)
- [`adapter-first-experimentation`](../../upgradeables/meta-control/adapter-first-experimentation/UPGRADEABLE.md)
- [`crispr-edit`](../../upgradeables/editing-repair/crispr-edit/UPGRADEABLE.md)
- [`surgery-edit`](../../upgradeables/editing-repair/surgery-edit/UPGRADEABLE.md)
- [`scoped-loader`](../../upgradeables/context-retrieval/scoped-loader/UPGRADEABLE.md)
- [`state-snapshot`](../../upgradeables/state/state-snapshot/UPGRADEABLE.md)
- [`ultimate-suite-supervisor`](../../upgradeables/meta-control/ultimate-suite-supervisor/UPGRADEABLE.md)

## Composition boundary

Remove redundant or inactive controls. Validators do not add facts. Any state,
persistence, or parallel execution must be backed by a real host mechanism.
