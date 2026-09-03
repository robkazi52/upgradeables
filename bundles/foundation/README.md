# Foundation Bundle

A curated composition, not an always-on monolith. Activate components only
when their individual triggers apply and preserve repository precedence.

## Components and default load order

- [`scoped-loader`](../../upgradeables/context-retrieval/scoped-loader/UPGRADEABLE.md)
- [`stateblock`](../../upgradeables/state/stateblock/UPGRADEABLE.md)
- [`task-set-lock-in`](../../upgradeables/state/task-set-lock-in/UPGRADEABLE.md)
- [`working-memory-cues`](../../upgradeables/state/working-memory-cues/UPGRADEABLE.md)
- [`grounding-no-invention`](../../upgradeables/truth-grounding/grounding-no-invention/UPGRADEABLE.md)
- [`drift-suppression`](../../upgradeables/drift-control/drift-suppression/UPGRADEABLE.md)
- [`placeholder-suppression`](../../upgradeables/output/placeholder-suppression/UPGRADEABLE.md)
- [`mode-lock-in`](../../upgradeables/state/mode-lock-in/UPGRADEABLE.md)

## Composition boundary

Remove redundant or inactive controls. Validators do not add facts. Any state,
persistence, or parallel execution must be backed by a real host mechanism.
