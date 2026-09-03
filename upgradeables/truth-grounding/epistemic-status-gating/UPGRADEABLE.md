# Epistemic Status Gating

## Summary

A proposition-level gate that records whether a statement is an input fact, supported inference, framing choice, or hypothesis before allowing it to influence a conclusion.

## Purpose

Keep mixed-certainty reasoning auditable and stop conclusions from laundering inference or hypothesis into fact.

## Problem Solved

Prevents unmarked certainty upgrades as information moves from source intake through reasoning and synthesis.

## Where It Fits in the OS

Roles: truth-state-classifier, validation-gate. Pipeline stages: evidence-capture, reasoning, pre-output-verification.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- evidence synthesis
- investigation
- decision support
- source-grounded research
- high-stakes review

## When Not to Use

- the task contains only direct transformation with no inferential claims
- labels would be exposed as private chain-of-thought rather than concise epistemic status

## Scope

Canonical package: `epistemic-status-gating@1.1.0`. ID: `JAN26-05`. Functional classes: truth-grounding, validation. Activation: `U1-common-conditional`. Mechanism basis: `normalized-from-recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- claims of mixed certainty are present

## Non-Triggers

- the task contains only direct transformation with no inferential claims
- labels would be exposed as private chain-of-thought rather than concise epistemic status

## Inputs / Required State

- material propositions
- source/evidence pointers
- semantic phase
- topic or compartment

## Outputs / Produced State

- status-labeled propositions
- blocked status promotions
- uncertainty or repair request

## Mechanism

Represent material propositions with an explicit status drawn from factual, evaluative/inferential, framing, or hypothetical phases, plus their evidence pointer and topic. A downstream conclusion may consume a proposition only under rules appropriate to that status; unsupported status promotion is rejected or surfaced as uncertainty.

## Procedure

1. Split the candidate reasoning product into material propositions.
2. Assign each proposition a status and evidence pointer.
3. Check whether downstream conclusions use each status permissibly.
4. Flag any inference or hypothesis presented as direct fact.
5. Downgrade, relabel, remove, or seek evidence for the offending proposition.
6. Emit concise status labels only where they help the user audit the answer.

## Always-Do Rules

- Keep evidence pointers with factual claims.
- Make uncertainty visible when status affects the conclusion.
- Maintain topic and phase isolation for stored propositions.

## Never-Do / Avoid Rules

- Treat plausibility as factual status.
- Promote a hypothesis because several later statements depend on it.
- Claim access to hidden chain-of-thought.

## Interaction Rules

### `grounding-no-invention`

Grounding supplies the evidence boundary used to assign factual status.

### `counterfactual-integrity`

Consumes the hypothesis labels to prevent phase leakage.

### `truth-priority-hierarchy`

Uses epistemic status when resolving conflicts among evidence and inference.

## Compatible Upgradeables

- `grounding-no-invention` — Grounding supplies the evidence boundary used to assign factual status.
- `counterfactual-integrity` — Consumes the hypothesis labels to prevent phase leakage.
- `truth-priority-hierarchy` — Uses epistemic status when resolving conflicts among evidence and inference.

## Counterbalancing Upgradeables

No natural counterbalance was identified after review; ordinary authority, scope, and validation controls still apply.

## Potential Redundancy

### `counterfactual-integrity`

Epistemic gating classifies all material propositions; counterfactual integrity specifically governs the factual/hypothetical boundary.

## Conflict / Precedence Rules

- Direct source evidence outranks an unlabeled model inference.
- A domain policy may define finer statuses but may not silently promote unsupported content.

## Failure Boundary

- If a decision-critical proposition has no defensible status or evidence pointer, it cannot support the conclusion.

## Strong-Model Scaling

May skip:

- visible labels for routine, obviously sourced statements

Keep mandatory:

- the distinction between source fact, inference, framing, and hypothesis

## Recommended Skill Types

- evidence synthesis
- investigation
- decision support
- source-grounded research
- high-stakes review

## Example Composition

**Task context:** A reviewer combines observed test output with an inferred root cause.

**Why it activates:** Observed evidence and causal inference have different certainty.

**Inputs/state:** Failing test log, changed code, and a plausible but unconfirmed explanation.

**Action:** Marks the failure as fact and the root cause as an inference requiring confirmation.

**Does not:** Report the suspected cause as established.

**Result/state change:** A review finding with calibrated certainty and a verification step.

**Companions:** ['grounding-no-invention', 'bidirectional-consistency']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `JAN26-05` in `OS_Upgradeables_Historical_Recovery_Inventory.md`. Registry generation: `training-scaffolding-2026-01-05`. Historical aliases: None.

Source support: `strongly-derivable`. Mechanism basis: `normalized-from-recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — C. JANUARY 5, 2026 TRAINING / SCAFFOLDING UPGRADEABLES (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 5. January 5, 2026 — training/scaffolding Upgradeables snapshot (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 6.2 T3 structured reasoning-state representation (historical_assistant_artifact)
