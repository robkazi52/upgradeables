# Micro-Scaffolding (`micro-scaffolding@1.1.0`)

Purpose: Protect a difficult local operation without loading the full OS, duplicating the parent StateBlock, or leaving permanent context residue.

Activate when: multi-step or high-constraint work.

Do not use when: a one-step task has no fragile constraints; the proposed scaffold repeats the full StateBlock or source corpus.

Requires: none.

## Runtime mechanism

At the start of a fragile subtask, extract only the few invariants and checkpoints that could be lost locally, such as preserve all numbers, preserve citation mapping, change tone only, and do not alter the conclusion. Use that compact scaffold while performing the step, check the local result against it, then retire the scaffold immediately when the subtask is accepted. It remains strictly smaller and shorter-lived than the workflow's canonical StateBlock.

## Procedure

1. Identify the current subtask and the specific failure risks within it.
2. Select the minimum local invariants, evidence pointers, and next-step checkpoints needed to control those risks.
3. Write a compact scaffold; do not copy unrelated global rules or full source material into it.
4. Execute the subtask while checking decisions against the scaffold.
5. Verify the local output against each scaffold item.

## Guardrails

- Mandatory even on strong models: identify the fragile local invariants; verify them after the step; retire temporary scaffolding.
- Conflict/precedence: Global task locks and source boundaries outrank a local scaffold; If the subtask expands into an architecture-level problem, retire the scaffold and re-plan at the parent task level.
- Stop or fail when: Escalate when the required control cannot remain local or when the scaffold grows into a duplicate of the parent plan/state; Reject the local result if any protected item was lost or changed without authorization.

Full package and provenance: [`micro-scaffolding`](../../upgradeables/foundation/micro-scaffolding/UPGRADEABLE.md).
