# Forethought / Checkpoints (`forethought-checkpoints@1.1.0`)

Purpose: Catch missing prerequisites and foreseeable downstream failure while reversal is still cheap.

Activate when: an action is costly, irreversible, or dependency-sensitive.

Do not use when: reversible low-cost local edits; the checkpoint would duplicate an already enforced transaction guard.

Requires: none.

## Runtime mechanism

At each consequential boundary, predict the most likely downstream failure, verify the prerequisite that would prevent it, define observable success and rollback, then commit and check the result. Checkpoints are placed by consequence rather than at every trivial step.

## Procedure

1. Identify the next irreversible, high-cost, or dependency-sensitive action.
2. Name the plausible downstream failure and affected dependency.
3. Verify prerequisites, authority, backups, and rollback path proportionate to risk.
4. Define the immediate post-action observation that indicates success or failure.
5. Commit only if the checkpoint passes, then inspect the result before continuing.

## Guardrails

- Mandatory even on strong models: pre-commit prerequisite check for consequential actions; success and rollback observation.
- Conflict/precedence: A failed hard prerequisite blocks commitment regardless of schedule pressure; During urgent containment, use the approved emergency checkpoint rather than omitting checks entirely.
- Stop or fail when: ritual checklists unrelated to risk; analysis after commitment instead of before.

Full package and provenance: [`forethought-checkpoints`](../../upgradeables/reasoning/forethought-checkpoints/UPGRADEABLE.md).
