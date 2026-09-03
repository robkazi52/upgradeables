# Style-Alignment Module (`style-alignment@1.1.0`)

Purpose: Make artifacts consistent with audience, publication, or organizational style while keeping truth and requirements dominant.

Activate when: a style or voice is specified.

Do not use when: the requested style impersonates a living person or conflicts with policy; exact quoted language must remain untouched.

Requires: none.

## Runtime mechanism

Translate the authorized style request into an observable style vector—tone, formality, sentence rhythm, vocabulary level, structure, formatting, and disallowed tendencies—while extracting a separate semantic invariant ledger. Transform surface choices toward the style vector, protect quoted and zero-drift zones, then score both conformance and semantic preservation; truth, task, and citation constraints veto any stylistic gain.

## Procedure

1. Extract the authorized style source and convert it into observable positive and negative constraints.
2. Lock facts, reasoning relations, requirements, citations, uncertainty, and exact-text zones.
3. Revise diction, rhythm, organization, and formatting only where the style contract permits.
4. Compare the result against the style vector using representative passages rather than vague resemblance.
5. Run a semantic and citation diff; revert any stylistic change that alters truth, logic, or attribution.

## Guardrails

- Mandatory even on strong models: explicit target dimensions; truth and task veto; semantic and citation back-check.
- Conflict/precedence: Truth, safety, citation fidelity, and explicit task constraints outrank the style guide; Exact quotations and legally controlled text are excluded from stylistic transformation.
- Stop or fail when: fact drift for tone; vague imitation.

Full package and provenance: [`style-alignment`](../../upgradeables/output/style-alignment/UPGRADEABLE.md).
