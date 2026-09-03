# Activation-Budget Funnel

## Summary

A staged context controller that moves sources through retrieve, evidence capture, indexing, transformation, writing, and verification instead of keeping raw retrieval and synthesis active together.

## Purpose

Protect limited active context by progressively disclosing sources and transferring verified evidence into compact indexed state before higher-level decisions.

## Problem Solved

Prevents source overload, recency domination, and premature synthesis when many documents, modules, or tool results compete for the same live workspace.

## Where It Fits in the OS

Roles: context-retrieval, activation budgeting, state orchestration. Pipeline stages: retrieval, evidence capture, indexing, synthesis, pre-output verification.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- multi-source research
- long-document analysis
- evidence-heavy authoring
- policy or legal evidence review
- large modular agent workflows

## When Not to Use

- a short single source fits comfortably in context
- creative work uses no references
- staging overhead exceeds the risk of context competition

## Scope

Canonical package: `activation-budget-funnel@1.1.0`. ID: `T2-16`. Functional classes: context-retrieval, state. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- many sources or modules compete for attention

## Non-Triggers

- a short single source fits comfortably in context
- creative work uses no references
- staging overhead exceeds the risk of context competition

## Inputs / Required State

- task question
- source/module queue
- active-pull budget
- evidence capture schema
- current indexed state

## Outputs / Produced State

- provenance-linked evidence index
- bounded active context
- synthesis-ready atoms
- verification status

## Mechanism

Admit only a bounded set of live source or module pulls, historically roughly five to seven, and move each through a fixed funnel: retrieve, quote or capture, index verified atoms, transform those atoms, write from the index, then verify against sources. Retire raw pulls from active attention after their durable evidence is indexed so retrieval and decision-making do not compete in one step.

## Procedure

1. Define the question and the evidence fields the task needs.
2. Queue candidate sources or modules rather than activating all of them.
3. Retrieve a bounded batch, keeping roughly no more than five to seven active pulls when that heuristic fits the host.
4. Capture source-grounded quotes or facts with provenance.
5. Index verified atoms into compact state and release unneeded raw context.
6. Transform and synthesize from indexed evidence only after capture is complete for the batch.
7. Write the result, then verify material claims back against the source pointers.

## Always-Do Rules

- Separate retrieval/capture from synthesis.
- Preserve provenance when compressing a source into indexed state.
- Treat five-to-seven as an architectural heuristic, not a measured universal limit.

## Never-Do / Avoid Rules

- Do not summarize unsupported material into the evidence index.
- Do not keep adding raw pulls while simultaneously committing a decision.
- Do not discard a source pointer needed for later verification.

## Interaction Rules

### `scoped-loader`

Chooses which sources/modules may enter the funnel and in what authority order.

### `neuro-focus`

Concentrates work on the highest-value active batch after ABF limits concurrent pulls.

### `stateblock`

Stores verified indexed atoms and their provenance between funnel stages.

## Compatible Upgradeables

- `scoped-loader` — Chooses which sources/modules may enter the funnel and in what authority order.
- `neuro-focus` — Concentrates work on the highest-value active batch after ABF limits concurrent pulls.
- `stateblock` — Stores verified indexed atoms and their provenance between funnel stages.

## Counterbalancing Upgradeables

### `anti-tunnel-vision`

Checks that a narrow active batch has not hidden a plausible competing source or interpretation.

## Potential Redundancy

### `attention-compression-scaffold`

Compression reduces representation size; ABF additionally governs stage order and concurrent activation.

### `scoped-loader`

Loader selects material; ABF budgets and stages its processing after selection.

## Conflict / Precedence Rules

- Source-boundary and authority rules control what may enter the funnel.
- If compacting an item would lose evidence needed for verification, retain or reload the source rather than forcing it through the budget.

## Failure Boundary

- Pause synthesis when evidence has not been captured with provenance or active pulls cannot be bounded without losing required coverage.
- Fail verification when a synthesized claim cannot be traced back through the index.

## Strong-Model Scaling

May skip:

- explicit queue bookkeeping for a very small corpus
- rigid adherence to the historical five-to-seven heuristic when the host context safely supports a different bound

Keep mandatory:

- retrieval-before-synthesis separation
- provenance-preserving indexing
- claim-to-source verification

## Recommended Skill Types

- multi-source research
- long-document analysis
- evidence-heavy authoring
- policy or legal evidence review
- large modular agent workflows

## Example Composition

**Task context:** Compare twelve vendor proposals against six criteria.

**Why it activates:** All proposals cannot remain active without recency and attention competition.

**Inputs/state:** Proposal queue, six-field evidence-card schema, source-page pointers.

**Action:** Processes bounded batches, captures criterion evidence, indexes it, releases raw text, then compares from the index and verifies finalists.

**Does not:** It does not draft the recommendation while still pulling unindexed proposal text.

**Result/state change:** A complete comparison built from traceable evidence cards with a bounded live workspace.

**Companions:** ['scoped-loader', 'stateblock', 'anti-tunnel-vision']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T2-16` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: ABF.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T2-16. ABF — Activation-Budget Funnel (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — ABF — Activation-Budget Funnel (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 18. ABF — DEEP CONTEXT IMPLICATION (historical_assistant_artifact)
