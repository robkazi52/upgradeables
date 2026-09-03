# Independent Evidence Redundancy (`truth-redundancy@1.1.0`)

Recovered name: Truth Redundancy

Purpose: Reduce single-point truth failure before high-impact synthesis or decision-making.

Activate when: a consequential claim can be independently checked.

Do not use when: the claim is low risk and an authoritative primary source is decisive; a second anchor would merely repeat the first source.

Requires: none.

## Runtime mechanism

For a selected truth atom, establish two evidence or validation anchors whose failure modes are meaningfully independent. Record provenance and the proposition each anchor supports; the pair is then passed to a gate or resolver rather than treated as automatic proof.

## Procedure

1. Identify the consequential truth atom.
2. Select the primary anchor and record its failure mode.
3. Select a second anchor with a distinct source or validation path.
4. Verify that the second does not merely derive from the first.
5. Record each anchor's supported scope and hand the pair to Multi-Truth Gating.

## Guardrails

- Mandatory even on strong models: when redundancy is claimed, the anchors must be genuinely independent.
- Conflict/precedence: Independence is invalid if both anchors share the same unverified upstream source; A safety veto still controls even when two non-safety anchors agree.
- Stop or fail when: If no genuinely independent second anchor is available, report that limitation and do not claim redundant verification.

Full package and provenance: [`truth-redundancy`](../../upgradeables/truth-grounding/truth-redundancy/UPGRADEABLE.md).
