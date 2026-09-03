# Periodic Whole-Task Consistency Check (`coherence-heartbeat@1.1.0`)

Recovered name: Global Coherence Heartbeat

Purpose: Detect long-horizon drift early without rerunning a full review after every step.

Activate when: a workflow is long or multi-stage.

Do not use when: the task completes in one obvious operation; a full coherence loop is already required at the same boundary.

Requires: none.

## Runtime mechanism

At predefined cadence or meaningful state transitions, compare a compact current-state snapshot against four anchors: objective, hard constraints, accepted decisions, and outstanding obligations. Emit a small delta signal—aligned, warning, or repair-required—and escalate to a full coherence loop only when the pulse detects material divergence.

## Procedure

1. Capture a compact baseline of objective, constraints, decisions, and open obligations.
2. Choose event-based or interval checkpoints proportional to task length.
3. At each checkpoint, compare current state with every anchor.
4. Classify differences as intended progress, harmless update, or drift.
5. Repair small drift immediately; invoke a coherence loop for systemic mismatch.

## Guardrails

- Mandatory even on strong models: event-triggered pulse after major state changes in long work.
- Conflict/precedence: Hard constraints and explicit user updates outrank the stored baseline; Do not accept a baseline refresh merely to clear an unresolved warning.
- Stop or fail when: Escalate when a hard constraint, core objective, or accepted decision no longer matches current work.

Full package and provenance: [`coherence-heartbeat`](../../upgradeables/validation/coherence-heartbeat/UPGRADEABLE.md).
