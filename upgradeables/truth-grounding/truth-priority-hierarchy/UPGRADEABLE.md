# Truth Priority Hierarchy

## Summary

A domain-explicit conflict resolver that determines which evidence, authority, or semantic class governs when candidate truths disagree.

## Purpose

Resolve conflicting signals without letting fluency, optimization, or an undifferentiated vote override stronger evidence or safety authority.

## Problem Solved

Prevents ad hoc conflict resolution and hidden selection of whichever claim best fits the draft.

## Where It Fits in the OS

Roles: truth-conflict-resolver, authority-ordering. Pipeline stages: task-framing, evidence-conflict-resolution, qms-collapse.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- multi-source research
- policy and regulatory analysis
- multi-validator workflows
- domain decisions with mixed evidence classes

## When Not to Use

- no material evidence or authority conflict exists
- the domain lacks an authorized hierarchy and inventing one would decide the outcome

## Scope

Canonical package: `truth-priority-hierarchy@1.1.0`. ID: `T3-06`. Functional classes: truth-grounding, orchestration. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- evidence classes or authorities conflict

## Non-Triggers

- no material evidence or authority conflict exists
- the domain lacks an authorized hierarchy and inventing one would decide the outcome

## Inputs / Required State

- conflicting claims or validator outcomes
- evidence provenance
- epistemic status
- authorized domain hierarchy

## Outputs / Produced State

- precedence decision
- narrowed synthesis
- unresolved conflict record

## Mechanism

Before resolving a conflict, declare a domain-appropriate ordering such as host safety over task optimization, direct source fact over inference, and verified evidence over stylistic fluency. Map each conflicting claim to its evidence and authority class, apply the ordering, and preserve unresolved ties rather than silently choosing.

## Procedure

1. Identify the conflicting propositions or validator outcomes.
2. Record the source, authority, epistemic status, and domain applicability of each.
3. Load or declare the authorized domain hierarchy.
4. Apply the hierarchy and any hard vetoes.
5. Document the winning, narrowed, or unresolved result.
6. Recheck that the selected claim remains supported in its original context.

## Always-Do Rules

- Make domain-specific precedence explicit.
- Separate evidence authority from rhetorical confidence.
- Preserve unresolved ties that affect the conclusion.

## Never-Do / Avoid Rules

- Assume one universal evidence hierarchy for every domain.
- Let a weighted score override a hard constraint.
- Choose the more fluent claim when evidence authority favors the other.

## Interaction Rules

### `multi-truth-gating`

Provides the resolution rule when independent anchors disagree.

### `parallel-qms`

Resolves material disagreement among QMS modes or evaluators.

### `epistemic-status-gating`

Supplies fact/inference/hypothesis classes used by the hierarchy.

## Compatible Upgradeables

- `multi-truth-gating` — Provides the resolution rule when independent anchors disagree.
- `parallel-qms` — Resolves material disagreement among QMS modes or evaluators.
- `epistemic-status-gating` — Supplies fact/inference/hypothesis classes used by the hierarchy.

## Counterbalancing Upgradeables

No natural counterbalance was identified after review; ordinary authority, scope, and validation controls still apply.

## Potential Redundancy

### `fermionic-veto`

A veto defines a hard blocking condition; Truth Priority Hierarchy orders competing non-veto evidence and authorities.

## Conflict / Precedence Rules

- Host/system safety and organization policy remain above repository-level truth ordering.
- If no authorized rule distinguishes materially conflicting claims, return unresolved rather than fabricate priority.

## Failure Boundary

- If a material conflict has no defensible domain/authority ordering, the resolver must not select a winner.

## Strong-Model Scaling

May skip:

- restating obvious precedence where one direct authoritative source controls

Keep mandatory:

- evidence and authority, not fluency or optimization, determine conflict resolution

## Recommended Skill Types

- multi-source research
- policy and regulatory analysis
- multi-validator workflows
- domain decisions with mixed evidence classes

## Example Composition

**Task context:** A policy summary contains a current primary policy text and an older interpretive memo that disagree.

**Why it activates:** Two evidence classes conflict.

**Inputs/state:** Both texts, dates, applicability, and an authorized policy-source hierarchy.

**Action:** Applies the hierarchy, explains the controlling source, and preserves the disagreement.

**Does not:** Blend incompatible statements into a false compromise.

**Result/state change:** A source-ranked conclusion with traceable precedence.

**Companions:** ['multi-truth-gating', 'epistemic-status-gating']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T3-06` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T3-06. Truth Priority Hierarchy (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 8. Tier-3 / Paper-Author alignment family recovered from late-November work (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 15.2 Historical Meta-OS template (historical_assistant_artifact)
