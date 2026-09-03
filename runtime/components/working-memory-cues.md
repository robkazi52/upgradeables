# Working-Memory Cues (`working-memory-cues@1.1.0`)

Purpose: Keep easily forgotten but relevant information salient during execution.

Activate when: many constraints must remain active.

Do not use when: the cue duplicates already salient text; too many cues would become noise.

Requires: none.

## Runtime mechanism

Derive a very short cue from canonical state and attach it to the step where omission is likely: a field pointer, invariant, question, or validation instruction. Retire the cue when its trigger or risk disappears; changes to truth occur in canonical state, never inside the cue.

## Procedure

1. Identify a recurrent omission risk and its decision point.
2. Select the smallest canonical state item that prevents it.
3. Write an imperative cue with a stable field or source pointer.
4. Present it only at the triggering step.
5. Measure whether it prevents the omission and remove stale or redundant cues.

## Guardrails

- Mandatory even on strong models: highest-risk cue at transition points; canonical pointer; retirement discipline.
- Conflict/precedence: Canonical state and higher-authority instructions override stale cues; When multiple cues compete, surface the one tied to the highest-risk immediate decision.
- Stop or fail when: Do not cue an unverified claim as fact; Escalate to a larger state view when the decision cannot be represented safely in a short reminder.

Full package and provenance: [`working-memory-cues`](../../upgradeables/state/working-memory-cues/UPGRADEABLE.md).
