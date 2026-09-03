# Drift Sink Scaffold

## Summary

Temporarily quarantine low-authority, obsolete, or repeatedly distracting branches outside active state while preserving traceable retrieval and review.

## Purpose

Stop known drift attractors from repeatedly re-entering active reasoning without destroying potentially useful history.

## Problem Solved

Superseded drafts, rejected hypotheses, and irrelevant branches can keep resurfacing and pulling work away from the current task.

## Where It Fits in the OS

Roles: drift quarantine, task-local scaffold, retired-branch containment. Pipeline stages: conflict resolution, context compaction, branch retirement, review or restore.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- long branching investigations
- iterative drafting
- agent workflows with recurring stale branches
- large mixed-authority contexts

## When Not to Use

- the branch is unresolved rather than rejected
- quarantine would conceal contrary evidence
- retention or audit policy requires it to remain actively visible

## Scope

Canonical package: `drift-sink-scaffold@1.1.0`. ID: `JAN26-10`. Functional classes: drift-control, state. Activation: `U2-specialized`. Mechanism basis: `provisional`. Activation cost: `medium` (architectural burden, not measured compute).

## Trigger Conditions

- Activate when the task requires discarded branches keep resurfacing.

## Non-Triggers

- the branch is unresolved rather than rejected
- quarantine would conceal contrary evidence
- retention or audit policy requires it to remain actively visible

## Inputs / Required State

- candidate branch
- authority and relevance classification
- dependency graph
- retention policy
- review triggers

## Outputs / Produced State

- reversible quarantine entry
- active-retrieval exclusion
- restore pointer
- review record

## Mechanism

A cautious modern interpretation is a reversible quarantine ledger: move an explicitly classified branch out of the active view, record why, by whose authority, its provenance, dependencies, review condition, and stable pointer, then block automatic retrieval unless a matching review trigger fires. The sink is neither deletion nor a semantic garbage collector, and the unrecovered ECL label must not be expanded speculatively.

**Modern operational interpretation:** The procedure below is useful current guidance, not a claim that the full historical mechanism was recovered.

## Procedure

1. Identify a branch that repeatedly causes drift and classify it as superseded, rejected, irrelevant, or low-authority.
2. Check whether any active claim depends on it and whether contrary-evidence duties require visibility.
3. Create a task-local sink entry with reason, authority, provenance, dependencies, and restore trigger.
4. Remove it from automatic active retrieval while retaining its stable pointer.
5. Review the sink at milestone or trigger events.
6. Restore, archive, or delete only under the applicable authority and retention policy; retire the scaffold when the task ends.

## Always-Do Rules

- make quarantine reversible
- retain provenance and reason
- check dependencies
- define review and retirement triggers

## Never-Do / Avoid Rules

- use the sink to hide inconvenient evidence
- equate quarantine with deletion
- expand ECL or claim an unrecovered historical algorithm
- sink unresolved safety-critical branches

## Interaction Rules

### `non-authoritative-branch-suppression`

Can classify lower-authority branches that qualify for reversible quarantine.

### `stable-long-context`

Excludes sink entries from the active view while preserving indexed history.

### `drift-suppression`

Identifies recurring deviations whose causal branch may be quarantined.

## Compatible Upgradeables

- `non-authoritative-branch-suppression` — Can classify lower-authority branches that qualify for reversible quarantine.
- `stable-long-context` — Excludes sink entries from the active view while preserving indexed history.
- `drift-suppression` — Identifies recurring deviations whose causal branch may be quarantined.

## Counterbalancing Upgradeables

### `clarification-gateway`

Prevents sinking a branch whose relevance or authority is merely unclear.

### `state-snapshot`

Preserves a pre-quarantine checkpoint for recovery.

## Potential Redundancy

### `non-authoritative-branch-suppression`

Suppression blocks a class at selection time; the sink records and contains repeatedly problematic instances.

### `stable-long-context`

Long-context compaction marks history; the sink adds an explicit no-auto-retrieval quarantine and review lifecycle.

## Conflict / Precedence Rules

- Higher-authority evidence or audit obligations can force restoration.
- When a branch contains both obsolete and still-relevant facts, split it rather than sinking the whole branch.

## Failure Boundary

- Do not quarantine unresolved contrary evidence or safety-critical information.
- Treat the mechanism as provisional until original concept-specific documentation is recovered.

## Strong-Model Scaling

May skip:

- a formal sink for a single harmless rejected idea
- persistent quarantine after a disposable task ends

Keep mandatory:

- reversibility
- authority/reason record
- dependency check
- no concealment of contrary evidence

## Recommended Skill Types

- long branching investigations
- iterative drafting
- agent workflows with recurring stale branches
- large mixed-authority contexts

## Example Composition

**Task context:** An investigation repeatedly retrieves an obsolete draft theory after it was disproven.

**Why it activates:** The branch consumes attention and contaminates new summaries.

**Inputs/state:** Disproof evidence, decision authority, dependency map, and retention requirement.

**Action:** Places the theory in a reversible task-local sink with its disproof, pointer, and restore condition.

**Does not:** It does not delete the branch or sink unresolved evidence that challenges the current theory.

**Result/state change:** Automatic retrieval stops resurfacing the disproven branch while auditability remains.

**Companions:** ['non-authoritative-branch-suppression', 'stable-long-context', 'state-snapshot']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `JAN26-10` in `OS_Upgradeables_Historical_Recovery_Inventory.md`. Registry generation: `training-scaffolding-2026-01-05`. Historical aliases: None.

Source support: `source-gap`. Mechanism basis: `provisional`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — ECL / Drift Sink (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 10.3 Drift widths (historical_assistant_artifact)
