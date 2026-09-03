# Truth Redundancy

## Summary

A two-anchor safety pattern that deliberately obtains independent support for a consequential truth atom so one failed source or reasoning path cannot silently control the result.

## Purpose

Reduce single-point truth failure before high-impact synthesis or decision-making.

## Problem Solved

Prevents apparent confidence based on only one fragile anchor and exposes when supposed corroboration is not independent.

## Where It Fits in the OS

Roles: evidence-redundancy, truth-safety. Pipeline stages: evidence-selection, pre-synthesis-validation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- high-stakes evidence work
- critical factual claims
- source-grounded decision support
- safety-relevant tradeoffs

## When Not to Use

- the claim is low risk and an authoritative primary source is decisive
- a second anchor would merely repeat the first source

## Scope

Canonical package: `truth-redundancy@1.1.0`. ID: `T3-03`. Functional classes: truth-grounding, validation. Activation: `U3-high-risk-expensive`. Mechanism basis: `recovered`. Activation cost: `high` (architectural burden, not measured compute).

## Trigger Conditions

- a consequential claim can be independently checked

## Non-Triggers

- the claim is low risk and an authoritative primary source is decisive
- a second anchor would merely repeat the first source

## Inputs / Required State

- consequential truth atom
- primary source/check
- candidate independent source/check
- provenance

## Outputs / Produced State

- verified independent anchor pair
- non-independence warning
- missing-anchor status

## Mechanism

For a selected truth atom, establish two evidence or validation anchors whose failure modes are meaningfully independent. Record provenance and the proposition each anchor supports; the pair is then passed to a gate or resolver rather than treated as automatic proof.

## Procedure

1. Identify the consequential truth atom.
2. Select the primary anchor and record its failure mode.
3. Select a second anchor with a distinct source or validation path.
4. Verify that the second does not merely derive from the first.
5. Record each anchor's supported scope and hand the pair to Multi-Truth Gating.

## Always-Do Rules

- Test independence, not just numerical multiplicity.
- Keep anchor provenance and supported scope.
- Apply redundancy selectively to consequential claims.

## Never-Do / Avoid Rules

- Count copied or circular claims as independent truth.
- Assume two anchors automatically resolve disagreement.
- Create unsupported content to supply a missing second anchor.

## Interaction Rules

### `multi-truth-gating`

Evaluates whether the two anchors agree sufficiently for commitment.

### `critical-atomic-verification`

Identifies which small, consequential claims merit redundant anchoring.

## Compatible Upgradeables

- `multi-truth-gating` — Evaluates whether the two anchors agree sufficiently for commitment.
- `critical-atomic-verification` — Identifies which small, consequential claims merit redundant anchoring.

## Counterbalancing Upgradeables

No natural counterbalance was identified after review; ordinary authority, scope, and validation controls still apply.

## Potential Redundancy

### `multi-truth-gating`

Truth Redundancy constructs an independent pair; Multi-Truth Gating compares it and determines disposition.

## Conflict / Precedence Rules

- Independence is invalid if both anchors share the same unverified upstream source.
- A safety veto still controls even when two non-safety anchors agree.

## Failure Boundary

- If no genuinely independent second anchor is available, report that limitation and do not claim redundant verification.

## Strong-Model Scaling

May skip:

- redundant anchoring for low-impact routine facts

Keep mandatory:

- when redundancy is claimed, the anchors must be genuinely independent

## Recommended Skill Types

- analysis and decision support
- high-stakes evidence work
- review and quality assurance
- source-grounded research

## Example Composition

**Task context:** A high-impact numerical claim drives a decision.

**Why it activates:** A single transcription or calculation error could change the outcome.

**Inputs/state:** The source table and an independently reproduced calculation.

**Action:** Records both anchors and checks their independence.

**Does not:** Treat two paragraphs citing the same table as independent.

**Result/state change:** An anchor pair ready for Multi-Truth Gating.

**Companions:** ['critical-atomic-verification', 'multi-truth-gating']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T3-03` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: Dual-Lepton Truth Redundancy.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 8. Tier-3 / Paper-Author alignment family recovered from late-November work (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 10.4 Multiverse / plan generation (historical_assistant_artifact)
