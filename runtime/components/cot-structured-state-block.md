# Auditable Reasoning State (`cot-structured-state-block@1.1.0`)

Recovered name: CoT-Structured State Block

Purpose: Make reasoning-relevant state portable and auditable while preserving the boundary between useful state and hidden internal deliberation.

Activate when: structured intermediate task state must survive across steps.

Do not use when: a one-turn answer has no meaningful state; the request seeks hidden chain-of-thought.

Requires: none.

## Runtime mechanism

Maintain an explicit schema of externally useful reasoning state: verified facts with provenance, user-provided constraints, labeled assumptions, concise conclusion summaries, unresolved questions, confidence, and next action. The block records what another worker needs to continue; it never stores token-level private deliberation or presents inference as evidence.

## Procedure

1. Define the minimum state schema and sensitivity boundary.
2. Populate facts only from cited or user-provided material and label assumptions separately.
3. Record concise decision rationales and confidence rather than hidden reasoning traces.
4. Update changed fields at checkpoints and preserve provenance.
5. Project only the fields needed by the next consumer.

## Guardrails

- Mandatory even on strong models: fact/inference separation; provenance; explicit uncertainty.
- Conflict/precedence: Canonical cited evidence overrides stale state summaries; If a requested field would expose private reasoning, provide a concise rationale or evidence ledger instead.
- Stop or fail when: Stop treating the block as authoritative if provenance is missing or fields are stale; Do not use the pattern to satisfy requests for hidden chain-of-thought.

Full package and provenance: [`cot-structured-state-block`](../../upgradeables/state/cot-structured-state-block/UPGRADEABLE.md).
