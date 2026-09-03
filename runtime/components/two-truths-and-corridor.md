# Dual-Source Bounded Synthesis (`two-truths-and-corridor@1.1.0`)

Recovered name: Two Truths + Corridor

Purpose: Enable useful synthesis without losing redundant factual grounding.

Activate when: source-grounded synthesis permits bounded interpretation.

Do not use when: only one defensible anchor exists; the task requires exact extraction with zero interpretive drift.

Requires: none.

## Runtime mechanism

Verify two independent anchors, declare which atoms in them are fixed, and set the synthesis corridor to zero, micro, or bounded exploratory drift. Generate connecting interpretation only inside that corridor, then check every synthesized claim against at least one anchor and the permitted transformation width.

## Procedure

1. Select and verify two independent anchors.
2. Extract the fixed facts and any material disagreement.
3. Declare the allowed synthesis corridor and prohibited transformations.
4. Create the synthesis while keeping each connection traceable.
5. Audit the result for unsupported bridging claims or altered anchor meaning.

## Guardrails

- Mandatory even on strong models: two verified anchors and the declared transformation boundary.
- Conflict/precedence: Zero-drift atoms override a wider surrounding synthesis corridor; If the anchors materially conflict, resolve or expose the conflict before generating a unified narrative.
- Stop or fail when: If either anchor is unverified or the synthesis requires claims outside the declared corridor, do not certify the synthesis.

Full package and provenance: [`two-truths-and-corridor`](../../upgradeables/truth-grounding/two-truths-and-corridor/UPGRADEABLE.md).
