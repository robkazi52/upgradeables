# Cross-Context Resonance Lock

## Summary

Preserve an explicitly declared relationship between related contexts without blending their facts, authority, or unresolved assumptions.

## Purpose

Preserve an explicitly declared relationship between related contexts without blending their facts, authority, or unresolved assumptions.

## Problem Solved

Multi-document and multi-agent work can either lose an important cross-context dependency or merge separate contexts into an unsupported composite.

## Where It Fits in the OS

Roles: cross-context coordination, boundary-preserving state control. Pipeline stages: context intake, cross-context handoff, synthesis verification.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- multi-document synthesis
- multi-agent handoffs
- parallel workstream integration

## When Not to Use

- the contexts are unrelated
- the relationship is speculative or would require merging incompatible authority domains

## Scope

Canonical package: `cross-context-resonance-lock@1.1.0`. ID: `JAN26-11`. Functional classes: orchestration, state. Activation: `U2-specialized`. Mechanism basis: `provisional`. Activation cost: `medium` (architectural burden, not measured compute).

## Trigger Conditions

- related contexts must stay aligned across a long task

## Non-Triggers

- the contexts are unrelated
- the relationship is speculative or would require merging incompatible authority domains

## Inputs / Required State

- two or more bounded context states
- declared relationship and allowed transfers
- source and authority metadata

## Outputs / Produced State

- validated cross-context link
- boundary-preserving handoff or rejected transfer

## Mechanism

Modern operational interpretation: represent each context as a separately identified state with its own source and authority, then store only the declared relationship as a typed link between them. On update or synthesis, refresh the link if both endpoints still support it and reject transfers that copy unverified facts or authority across the boundary.

**Modern operational interpretation:** The procedure below is useful current guidance, not a claim that the full historical mechanism was recovered.

## Procedure

1. Identify each context, its source boundary, authority, and current state.
2. State the exact relationship that must remain aligned across contexts.
3. Store a typed link without copying the full contents of either context.
4. Revalidate both endpoints and the relationship when either context changes.
5. During synthesis, transfer only explicitly supported fields and preserve provenance.

## Always-Do Rules

- Preserve the defining invariant: separate provenance and authority for every linked context.
- Record material routing, transition, and failure decisions in explicit task state.

## Never-Do / Avoid Rules

- merging both contexts or transferring unsupported assumptions
- Never claim hidden state, unavailable host capability, or authority beyond the active Skill.

## Interaction Rules

### `state-routing-bus`

Carries the explicitly permitted linked fields between modules.

### `domain-mode-isolation`

Prevents the lock from collapsing separate domain or authority states.

## Compatible Upgradeables

- `state-routing-bus` — Carries the explicitly permitted linked fields between modules.
- `domain-mode-isolation` — Prevents the lock from collapsing separate domain or authority states.

## Counterbalancing Upgradeables

### `anti-tunnel-vision`

Challenges an assumed relationship when fixation could make unrelated contexts appear aligned.

## Potential Redundancy

### `resonance`

Resonance coordinates reinforcing modules generally; Cross-Context Resonance Lock preserves one explicit relationship across bounded contexts.

## Conflict / Precedence Rules

- Host, system, domain, and explicit user authority take precedence over this component.
- If the relationship cannot be supported independently in both contexts, stop or escalate rather than forcing a nominal success.

## Failure Boundary

- the relationship cannot be supported independently in both contexts
- maintaining alignment would require transferring incompatible authority or unverified state

## Strong-Model Scaling

May skip:

- a single-context task has no cross-boundary relationship to preserve

Keep mandatory:

- separate provenance and authority for every linked context

## Recommended Skill Types

- long-context workflows
- multi-step task execution
- skill and agent workflows

## Example Composition

**Task context:** Two agents analyze technical feasibility and legal constraints for the same feature.

**Why it activates:** Their decisions must align on the feature identifier, but their evidence and authority differ.

**Inputs/state:** Two scoped states, shared feature key, allowed handoff fields, and provenance.

**Action:** Maintains the feature link and transfers only the declared decision fields with sources.

**Does not:** Does not merge legal claims into technical evidence or give one agent the other's authority.

**Result/state change:** The synthesis aligns on the feature while retaining two auditable contexts.

**Companions:** State Routing Bus carries allowed fields; Domain Isolation preserves boundaries.

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `JAN26-11` in `OS_Upgradeables_Historical_Recovery_Inventory.md`. Registry generation: `training-scaffolding-2026-01-05`. Historical aliases: Resonance Upgradeable.

Source support: `source-gap`. Mechanism basis: `provisional`.

Structured source references:

- OS_Upgradeables_Historical_Recovery_Inventory.md — 11. Advanced architecture Upgradeables retained (historical_recovery_inventory)
- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
