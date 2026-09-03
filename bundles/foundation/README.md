# Foundation Bundle

Establish scoped task identity, state, and grounding for complex work.

## Activation boundary

Activate individual foundations when constraints could be lost; it is not a universal preamble.

## Required and optional components

- [`scoped-loader@1.1.0`](../../upgradeables/context-retrieval/scoped-loader/UPGRADEABLE.md) — optional; activate by trigger
- [`stateblock@1.1.0`](../../upgradeables/state/stateblock/UPGRADEABLE.md) — optional; activate by trigger
- [`task-set-lock-in@1.1.0`](../../upgradeables/state/task-set-lock-in/UPGRADEABLE.md) — required
- [`working-memory-cues@1.1.0`](../../upgradeables/state/working-memory-cues/UPGRADEABLE.md) — optional; activate by trigger
- [`grounding-no-invention@1.1.0`](../../upgradeables/truth-grounding/grounding-no-invention/UPGRADEABLE.md) — required
- [`drift-suppression@1.1.0`](../../upgradeables/drift-control/drift-suppression/UPGRADEABLE.md) — optional; activate by trigger
- [`placeholder-suppression@1.1.0`](../../upgradeables/output/placeholder-suppression/UPGRADEABLE.md) — optional; activate by trigger
- [`mode-lock-in@1.1.0`](../../upgradeables/state/mode-lock-in/UPGRADEABLE.md) — optional; activate by trigger

## Load order and critical interactions

Use the metadata `load_order`. Task and mode locks constrain state; the loader may add evidence but never authority.

## Over-scaffolding boundary

Excessive for a simple direct request that the host can reliably complete without explicit state.
