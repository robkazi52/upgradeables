# Meta Control Bundle

A curated composition, not an always-on monolith. Activate components only
when their individual triggers apply and preserve repository precedence.

## Components and default load order

- [`meta-supervisor`](../../upgradeables/meta-control/meta-supervisor/UPGRADEABLE.md)
- [`meta-awareness`](../../upgradeables/meta-control/meta-awareness/UPGRADEABLE.md)
- [`stuck-pattern-reset`](../../upgradeables/meta-control/stuck-pattern-reset/UPGRADEABLE.md)
- [`coherence-heartbeat`](../../upgradeables/validation/coherence-heartbeat/UPGRADEABLE.md)
- [`resonance`](../../upgradeables/orchestration/resonance/UPGRADEABLE.md)
- [`neuro-focus`](../../upgradeables/context-retrieval/neuro-focus/UPGRADEABLE.md)
- [`dynamic-depth-allocation`](../../upgradeables/meta-control/dynamic-depth-allocation/UPGRADEABLE.md)
- [`reasoning-throughput-governor`](../../upgradeables/meta-control/reasoning-throughput-governor/UPGRADEABLE.md)
- [`drift-spectra-scaling`](../../upgradeables/drift-control/drift-spectra-scaling/UPGRADEABLE.md)
- [`compute-adaptive-drift`](../../upgradeables/drift-control/compute-adaptive-drift/UPGRADEABLE.md)
- [`domain-normalized-drift`](../../upgradeables/drift-control/domain-normalized-drift/UPGRADEABLE.md)
- [`drift-immunity-propagation`](../../upgradeables/drift-control/drift-immunity-propagation/UPGRADEABLE.md)
- [`meta-stability`](../../upgradeables/meta-control/meta-stability/UPGRADEABLE.md)
- [`cross-universe-consistency`](../../upgradeables/validation/cross-universe-consistency/UPGRADEABLE.md)
- [`future-proof-mode-selector`](../../upgradeables/meta-control/future-proof-mode-selector/UPGRADEABLE.md)
- [`model-size-drift-scaling`](../../upgradeables/meta-control/model-size-drift-scaling/UPGRADEABLE.md)

## Composition boundary

Remove redundant or inactive controls. Validators do not add facts. Any state,
persistence, or parallel execution must be backed by a real host mechanism.
