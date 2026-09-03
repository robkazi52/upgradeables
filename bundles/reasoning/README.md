# Reasoning Bundle

Add bounded planning, alternatives, checks, and convergence to a difficult task.

## Activation boundary

Activate controls only for complexity that direct reasoning does not already handle.

## Required and optional components

- [`micro-scaffolding@1.1.0`](../../upgradeables/foundation/micro-scaffolding/UPGRADEABLE.md) — optional; activate by trigger
- [`reasoning-scale-controller@1.1.0`](../../upgradeables/reasoning/reasoning-scale-controller/UPGRADEABLE.md) — required
- [`anti-tunnel-vision@1.1.0`](../../upgradeables/reasoning/anti-tunnel-vision/UPGRADEABLE.md) — optional; activate by trigger
- [`forethought-checkpoints@1.1.0`](../../upgradeables/reasoning/forethought-checkpoints/UPGRADEABLE.md) — optional; activate by trigger
- [`bidirectional-consistency@1.1.0`](../../upgradeables/validation/bidirectional-consistency/UPGRADEABLE.md) — optional; activate by trigger
- [`multiverse-reasoning@1.1.0`](../../upgradeables/reasoning/multiverse-reasoning/UPGRADEABLE.md) — optional; activate by trigger
- [`bounded-exit@1.1.0`](../../upgradeables/reasoning/bounded-exit/UPGRADEABLE.md) — optional; activate by trigger

## Load order and critical interactions

Use the metadata `load_order`. Scale control determines depth; Bounded ExIt stops refinement and retires unused branches.

## Over-scaffolding boundary

Excessive for a short deterministic task or when branching cannot change the answer.
