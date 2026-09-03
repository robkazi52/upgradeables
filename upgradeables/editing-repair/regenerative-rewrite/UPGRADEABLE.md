# Regenerative Rewrite

## Summary

Rebuilds an artifact from its locked truths and constraints when local repairs cannot recover global coherence or source mapping.

## Purpose

Replace a systemically broken expression or structure without losing verified content, requirements, provenance, or accepted decisions.

## Problem Solved

An artifact can be locally polished yet remain globally incoherent because its architecture is wrong, sections conflict, or evidence-to-claim mapping has collapsed.

## Where It Fits in the OS

Roles: global content rebuilder, systemic-failure recovery. Pipeline stages: failure diagnosis, truth-and-constraint extraction, fresh reconstruction, global validation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- globally incoherent drafts
- broken source-to-section mapping
- documents with incompatible inherited structures
- outputs damaged by repeated patching

## When Not to Use

- one sentence or field is wrong
- the existing architecture is sound
- locked atoms and provenance cannot yet be separated from generated content

## Scope

Canonical package: `regenerative-rewrite@1.1.0`. ID: `T2-03`. Functional classes: editing-repair. Activation: `U2-specialized`. Mechanism basis: `recovered`. Activation cost: `medium` (architectural burden, not measured compute).

## Trigger Conditions

- architecture or source mapping is globally broken

## Non-Triggers

- one sentence or field is wrong
- the existing architecture is sound
- locked atoms and provenance cannot yet be separated from generated content

## Inputs / Required State

- failed artifact
- systemic-failure evidence
- locked truth ledger
- requirements
- source map

## Outputs / Produced State

- freshly structured artifact
- coverage and provenance validation
- discarded-material record

## Mechanism

Quarantine the failed artifact, extract a ledger of verified facts, citations, requirements, decisions, and protected wording, and design a fresh structure from that ledger rather than editing the old prose in place. Reintroduce each locked atom with provenance, validate global coherence and coverage, and compare against the ledger—not against the failed wording—as the acceptance baseline.

## Procedure

1. Demonstrate systemic failure: wrong architecture, cross-section contradiction, or broken source mapping that resists bounded repair.
2. Extract and classify locked facts, citations, constraints, requirements, and accepted decisions.
3. Set the failed draft aside and create a new outline or artifact structure from the locked ledger.
4. Rebuild content section by section, attaching every factual claim to its source or ledger atom.
5. Validate requirement coverage, global coherence, citation mapping, and absence of imported failed assumptions.
6. Compare the rebuilt artifact with the locked ledger and record intentionally discarded generated material.

## Always-Do Rules

- prove local repair is insufficient
- build a locked-atom ledger before rewriting
- reconstruct from verified state rather than memory of the old prose
- validate global source mapping

## Never-Do / Avoid Rules

- use regeneration for one awkward sentence
- discard accepted decisions because the wording is inconvenient
- copy incoherent passages wholesale into the new structure
- claim historical wording was preserved when only semantics were locked

## Interaction Rules

### `task-set-lock-in`

Task-Set Lock-In preserves the goals and requirements during reconstruction.

### `surgery-edit`

Surgery can replace the artifact's architecture before Regenerative Rewrite repopulates it.

### `citation-fidelity`

Citation Fidelity ensures the rebuilt claims remain mapped to original sources.

## Compatible Upgradeables

- `task-set-lock-in` — Task-Set Lock-In preserves the goals and requirements during reconstruction.
- `surgery-edit` — Surgery can replace the artifact's architecture before Regenerative Rewrite repopulates it.
- `citation-fidelity` — Citation Fidelity ensures the rebuilt claims remain mapped to original sources.

## Counterbalancing Upgradeables

### `micro-repair`

Micro-Repair should be tried first for bounded defects and prevents unnecessary regeneration.

## Potential Redundancy

### `surgery-edit`

Both address macro failure, but Surgery changes structural interfaces while Regenerative Rewrite reconstructs content from locked truth and constraints.

## Conflict / Precedence Rules

- Verified facts, citations, and non-negotiable requirements survive even if they complicate the new structure.
- If the architecture alone is defective, Surgery may define the replacement skeleton; regeneration then fills it.
- If no reliable locked ledger can be formed, stop for source recovery rather than regenerate from guesses.

## Failure Boundary

- unnecessary global rewrite
- loss of locked facts
- source laundering
- reimporting the failed architecture
- regeneration from unverified memory

## Strong-Model Scaling

May skip:

- verbose quarantine ceremony when the failed draft is already versioned

Keep mandatory:

- locked-atom extraction
- fresh-structure reconstruction
- ledger-based global validation

## Recommended Skill Types

- globally incoherent drafts
- broken source-to-section mapping
- documents with incompatible inherited structures
- outputs damaged by repeated patching

## Example Composition

**Task context:** A research report has accurate notes but sections mix methods, results, and unsupported conclusions.

**Why it activates:** Multiple local edits have not restored coherent source mapping.

**Inputs/state:** Verified notes, citations, requirements, and the failed report are available.

**Action:** Builds a fact-and-citation ledger, creates a new section map, writes afresh from the ledger, and records which unsupported passages were discarded.

**Does not:** Polish each old section in sequence or carry unsupported transitions into the rebuild.

**Result/state change:** A coherent report whose claims map back to verified source atoms.

**Companions:** ['task-set-lock-in', 'citation-fidelity', 'surgery-edit']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T2-03` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T2-03. Regenerative Rewrite (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 11. Advanced architecture Upgradeables retained (historical_recovery_inventory)
