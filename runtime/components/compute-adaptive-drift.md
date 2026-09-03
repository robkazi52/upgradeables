# Runtime-Adaptive Drift Checks (`compute-adaptive-drift@1.1.0`)

Recovered name: Compute-Adaptive Drift Constraining

Purpose: Maintain semantic reliability across weak and strong runtimes without burdening every runtime identically.

Activate when: compute/depth varies across a task.

Do not use when: adaptation would weaken factual or safety invariants; runtime capability is unknown in a high-risk task.

Requires: none.

## Runtime mechanism

Classify the task risk and runtime's demonstrated capacity, then choose an enforcement profile: weaker or unverified runtimes receive smaller steps, explicit state, more frequent source checks, and tighter drift corridors; stronger verified runtimes may combine steps and reduce scaffolding. The semantic acceptance tests, authority hierarchy, citations, and zero-drift fields never relax.

## Procedure

1. Classify consequence of drift and identify non-negotiable invariants.
2. Assess demonstrated context, reasoning, tool, and verification capacity without trusting branding alone.
3. Choose checkpoint frequency, step size, scaffold depth, and corridor width.
4. Run a calibration or early sample against the same semantic tests.
5. Tighten controls on failure; relax only process overhead after repeated success.

## Guardrails

- Mandatory even on strong models: zero-drift fields; authority hierarchy; source grounding.
- Conflict/precedence: Task risk and zero-drift requirements cap any relaxation due to compute; When capability evidence conflicts, use the stricter profile until a calibration passes.
- Stop or fail when: Do not relax controls for high-impact claims without demonstrated validation performance; Fall back to the strict profile when runtime behavior is unstable or unobservable.

Full package and provenance: [`compute-adaptive-drift`](../../upgradeables/drift-control/compute-adaptive-drift/UPGRADEABLE.md).
