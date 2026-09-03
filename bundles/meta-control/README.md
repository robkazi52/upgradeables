# Meta Control Bundle

Monitor and adapt a long or unstable reasoning process.

## Activation boundary

Activate when observed instability, repeated failure, or resource pressure justifies supervision.

## Required and optional components

- [`meta-supervisor@1.1.0`](../../upgradeables/meta-control/meta-supervisor/UPGRADEABLE.md) — required
- [`meta-awareness@1.1.0`](../../upgradeables/meta-control/meta-awareness/UPGRADEABLE.md) — optional; activate by trigger
- [`stuck-pattern-reset@1.1.0`](../../upgradeables/meta-control/stuck-pattern-reset/UPGRADEABLE.md) — optional; activate by trigger
- [`coherence-heartbeat@1.1.0`](../../upgradeables/validation/coherence-heartbeat/UPGRADEABLE.md) — optional; activate by trigger
- [`resonance@1.1.0`](../../upgradeables/orchestration/resonance/UPGRADEABLE.md) — optional; activate by trigger
- [`neuro-focus@1.1.0`](../../upgradeables/context-retrieval/neuro-focus/UPGRADEABLE.md) — optional; activate by trigger
- [`dynamic-depth-allocation@1.1.0`](../../upgradeables/meta-control/dynamic-depth-allocation/UPGRADEABLE.md) — optional; activate by trigger
- [`reasoning-throughput-governor@1.1.0`](../../upgradeables/meta-control/reasoning-throughput-governor/UPGRADEABLE.md) — optional; activate by trigger
- [`drift-spectra-scaling@1.1.0`](../../upgradeables/drift-control/drift-spectra-scaling/UPGRADEABLE.md) — optional; activate by trigger
- [`compute-adaptive-drift@1.1.0`](../../upgradeables/drift-control/compute-adaptive-drift/UPGRADEABLE.md) — optional; activate by trigger
- [`domain-normalized-drift@1.1.0`](../../upgradeables/drift-control/domain-normalized-drift/UPGRADEABLE.md) — optional; activate by trigger
- [`drift-immunity-propagation@1.1.0`](../../upgradeables/drift-control/drift-immunity-propagation/UPGRADEABLE.md) — optional; activate by trigger
- [`meta-stability@1.1.0`](../../upgradeables/meta-control/meta-stability/UPGRADEABLE.md) — optional; activate by trigger
- [`cross-universe-consistency@1.1.0`](../../upgradeables/validation/cross-universe-consistency/UPGRADEABLE.md) — optional; activate by trigger
- [`future-proof-mode-selector@1.1.0`](../../upgradeables/meta-control/future-proof-mode-selector/UPGRADEABLE.md) — optional; activate by trigger
- [`model-size-drift-scaling@1.1.0`](../../upgradeables/meta-control/model-size-drift-scaling/UPGRADEABLE.md) — optional; activate by trigger

## Load order and critical interactions

Use the metadata `load_order`. The supervisor chooses a targeted correction; monitors must not all run continuously.

## Over-scaffolding boundary

Excessive when loaded wholesale or when no measurable instability signal exists.
