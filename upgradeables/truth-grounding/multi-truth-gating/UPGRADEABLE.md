# Multi-Truth Gating

## Summary

A commitment gate for important conclusions that requires compatible independent truth anchors or validation paths and refuses to force agreement when they materially diverge.

## Purpose

Reduce dependence on one fragile source, inference chain, or evaluator before a consequential conclusion is committed.

## Problem Solved

Prevents a single unnoticed evidence or reasoning failure from propagating into an important decision.

## Where It Fits in the OS

Roles: high-risk-truth-gate, commitment-validator. Pipeline stages: post-analysis, pre-synthesis, pre-output-commitment.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- high-stakes evidence synthesis
- conflicting-source research
- medical, legal, or policy decisions
- critical architecture choices

## When Not to Use

- the claim is low consequence and one authoritative direct source is sufficient
- the supposed anchors merely duplicate the same underlying source

## Scope

Canonical package: `multi-truth-gating@1.1.0`. ID: `T3-01`. Functional classes: truth-grounding, validation. Activation: `U3-high-risk-expensive`. Mechanism basis: `recovered`. Activation cost: `high` (architectural burden, not measured compute).

## Trigger Conditions

- an important conclusion rests on fragile evidence

## Non-Triggers

- the claim is low consequence and one authoritative direct source is sufficient
- the supposed anchors merely duplicate the same underlying source

## Inputs / Required State

- decision-critical conclusion
- primary anchor
- independent corroborating anchor or check
- evidence priority rules

## Outputs / Produced State

- pass to commit
- narrowed conclusion
- re-evaluation request
- abstention or unresolved-conflict status

## Mechanism

For each decision-critical conclusion, identify a primary factual anchor and at least one genuinely independent corroborating anchor or verification path. Compare what each supports; convergence permits commitment, while material divergence triggers re-evaluation, a narrower claim, explicit uncertainty, or abstention.

## Procedure

1. Identify conclusions whose failure would materially change the outcome.
2. Record the primary evidence or reasoning anchor for each.
3. Select an independent corroborating source or validation path.
4. Check independence and compare the supported propositions.
5. Resolve differences by evidence and authority rules rather than averaging.
6. Commit, narrow, rework, or abstain according to the comparison.

## Always-Do Rules

- Test anchor independence.
- Scope the gate to important conclusions.
- Preserve unresolved material disagreement.

## Never-Do / Avoid Rules

- Count two summaries of the same source as independent anchors.
- Use majority voting to erase a critical contradiction.
- Run expensive redundant checks on every trivial statement.

## Interaction Rules

### `truth-redundancy`

Constructs the two independent anchors consumed by the gate.

### `parallel-qms`

Provides independent validation modes and a controlled collapse result.

### `truth-priority-hierarchy`

Resolves disagreements by explicit evidence authority.

## Compatible Upgradeables

- `truth-redundancy` — Constructs the two independent anchors consumed by the gate.
- `parallel-qms` — Provides independent validation modes and a controlled collapse result.
- `truth-priority-hierarchy` — Resolves disagreements by explicit evidence authority.

## Counterbalancing Upgradeables

No natural counterbalance was identified after review; ordinary authority, scope, and validation controls still apply.

## Potential Redundancy

### `truth-redundancy`

Truth Redundancy creates redundant anchors; Multi-Truth Gating decides whether their agreement is sufficient for commitment.

## Conflict / Precedence Rules

- A higher-authority direct source can outweigh a weaker corroborating path, but the disagreement must be recorded.
- Safety vetoes are not overridable by numerical agreement among other checks.

## Failure Boundary

- If an important conclusion lacks an independent check or the anchors materially disagree without resolution, do not certify the conclusion.

## Strong-Model Scaling

May skip:

- redundant checks for low-risk claims with a single decisive authority

Keep mandatory:

- decision-critical claims require genuinely independent support or an explicit unresolved status

## Recommended Skill Types

- high-stakes evidence synthesis
- conflicting-source research
- medical, legal, or policy decisions
- critical architecture choices

## Example Composition

**Task context:** A policy recommendation rests on a reported outcome and a causal interpretation.

**Why it activates:** The recommendation is consequential and one reasoning path may be fragile.

**Inputs/state:** Primary study result, independent dataset or reverse-consistency check, and authority rules.

**Action:** Compares independent support and narrows the recommendation if causal support diverges.

**Does not:** Treat repeated citations to the same study as multiple truths.

**Result/state change:** A committed or bounded recommendation with its support status.

**Companions:** ['truth-redundancy', 'parallel-qms', 'truth-priority-hierarchy']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T3-01` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T3-01. Multi-Truth Gating (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 8. Tier-3 / Paper-Author alignment family recovered from late-November work (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 8.12 Historical global collapse rule (historical_assistant_artifact)
