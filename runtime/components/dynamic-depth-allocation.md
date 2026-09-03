# Per-Region Reasoning Depth (`dynamic-depth-allocation@1.1.0`)

Recovered name: Dynamic Depth Allocation

Purpose: Concentrate analysis and verification where local marginal value is highest instead of applying uniform depth across a task.

Activate when: task regions vary in difficulty or risk.

Do not use when: every unit has the same mandated review depth; the task is one atomic operation.

Requires: none.

## Runtime mechanism

Partition the task into meaningful regions, score each on difficulty, uncertainty, consequence, dependency centrality, and current evidence deficit, and assign depth bands under the Cognitive Governor's total envelope. Re-score after discoveries and move effort toward unresolved hotspots while maintaining a minimum pass everywhere. DDA decides where depth goes, not the total budget or execution concurrency.

## Procedure

1. Decompose the task into independently inspectable regions or claims.
2. Score each region for uncertainty, consequence, coupling, novelty, and evidence deficit.
3. Reserve a minimum validation pass for all regions.
4. Allocate the remaining governed budget to high-score regions and choose appropriate methods for each.
5. Re-score when a local finding changes dependencies or risk.

## Guardrails

- Mandatory even on strong models: minimum regional pass; hotspot-driven allocation; budget-bound re-scoring.
- Conflict/precedence: A high-risk mandatory check receives its floor even if its estimated uncertainty is low; When every region exceeds the available envelope, escalate the budget or narrow scope rather than fabricate coverage.
- Stop or fail when: uniform-depth default; hotspot tunnel vision.

Full package and provenance: [`dynamic-depth-allocation`](../../upgradeables/meta-control/dynamic-depth-allocation/UPGRADEABLE.md).
