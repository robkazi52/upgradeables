# Adapter-First Experimentation

## Summary

Tests a new capability behind a detachable boundary and promotes it into the base only after comparative evidence shows stable value.

## Purpose

Protect a working OS or workflow from speculative capabilities while preserving a path for evidence-based evolution.

## Problem Solved

Directly rewriting the base for every experiment couples unproven behavior to production, obscures evaluation, and makes rollback difficult.

## Where It Fits in the OS

Roles: architecture experiment controller, promotion gate. Pipeline stages: experiment design, detached trial, evaluation, promotion or retirement.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- new loader or validator trials
- tool integrations
- alternative routing logic
- model-specific optimization

## When Not to Use

- the change is a mandatory security repair
- no stable interface can isolate the capability
- the experiment cannot be measured against the base

## Scope

Canonical package: `adapter-first-experimentation@1.1.0`. ID: `T2-21`. Functional classes: meta-control, orchestration. Activation: `U4-meta-architecture`. Mechanism basis: `recovered`. Activation cost: `high` (architectural burden, not measured compute).

## Trigger Conditions

- a new capability may destabilize a base workflow

## Non-Triggers

- the change is a mandatory security repair
- no stable interface can isolate the capability
- the experiment cannot be measured against the base

## Inputs / Required State

- capability hypothesis
- base workflow
- adapter interface
- test cohort
- acceptance metrics and invariants

## Outputs / Produced State

- detached experimental adapter
- base-versus-adapter evidence
- promote, revise, or retire decision
- rollback record

## Mechanism

Define an adapter contract around the proposed capability, route only an explicit test cohort through it, and preserve the unchanged base as control and rollback. Compare quality, cost, latency, drift, and failure behavior against predeclared acceptance thresholds; promote only the demonstrated stable interface, otherwise revise or retire the adapter without contaminating core rules.

## Procedure

1. State the hypothesis, acceptance metrics, test cohort, and non-negotiable invariants.
2. Expose the smallest stable interface needed by the capability.
3. Implement or specify it as a detachable adapter with base-path fallback and isolated state.
4. Run representative and adversarial trials against the unchanged base.
5. Compare benefit, regressions, operating cost, and rollback behavior.
6. Promote the stable behavior only after thresholds pass; otherwise revise or remove the adapter and retain the base.

## Always-Do Rules

- keep the base path available during evaluation
- predeclare promotion criteria
- isolate experimental state and authority
- record promotion or retirement evidence

## Never-Do / Avoid Rules

- declare an experiment core because it is novel
- let adapter-only assumptions leak into the base
- promote on one favorable example
- remove rollback before stability is demonstrated

## Interaction Rules

### `architect-orchestrator`

The architect defines the adapter boundary and routes the controlled cohort.

### `future-proof-mode-selector`

A model- or environment-specific capability can remain an adapter selected only where supported.

## Compatible Upgradeables

- `architect-orchestrator` — The architect defines the adapter boundary and routes the controlled cohort.
- `future-proof-mode-selector` — A model- or environment-specific capability can remain an adapter selected only where supported.

## Counterbalancing Upgradeables

### `meta-stability`

Meta-Stability freezes the base and suppresses experimental activation when coherence is already degrading.

## Potential Redundancy

### `crispr-edit`

CRISPR changes an established component precisely; Adapter-First evaluates an unproven capability without changing that component.

## Conflict / Precedence Rules

- Security and integrity repairs follow their mandated path rather than waiting for experimental promotion.
- If the adapter cannot be isolated from base state or authority, do not trial it in production.
- A benefit score cannot override a failed invariant or rollback test.

## Failure Boundary

- base contamination
- unmeasured promotion
- hidden experimental state
- interface sprawl
- irreversible trial

## Strong-Model Scaling

May skip:

- a heavyweight experiment document for a local reversible sandbox test

Keep mandatory:

- detachable boundary
- control comparison
- invariant gate
- explicit promotion decision

## Recommended Skill Types

- multi-step task execution
- skill and agent workflows

## Example Composition

**Task context:** Try semantic search in a repository skill loader.

**Why it activates:** Search may improve discovery but could add latency and unstable ranking to a working deterministic loader.

**Inputs/state:** The current resolver, a candidate search adapter, representative queries, and latency and precision thresholds are available.

**Action:** Routes a test cohort through the adapter, compares it with deterministic resolution, tests fallback, and promotes only the stable query interface after thresholds pass.

**Does not:** Replace the base resolver before evaluation or let the adapter mutate registry records.

**Result/state change:** Evidence-backed adoption or clean retirement with the original loader intact.

**Companions:** ['architect-orchestrator', 'meta-stability']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T2-21` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 11. Advanced architecture Upgradeables retained (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 19.5 OS / Skill construction (historical_assistant_artifact)
