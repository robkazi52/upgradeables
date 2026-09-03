# Parallel Quality Management System

## Summary

A selectable family of orthogonal validation modes whose judgments are preserved separately and collapsed under explicit consensus, consistency, and veto rules.

## Purpose

Match validation topology to failure risk instead of treating QMS as one generic critic or a majority vote.

## Problem Solved

A single evaluator misses correlated errors, while indiscriminate parallel review duplicates work, conceals disagreement, and can recurse without convergence.

## Where It Fits in the OS

Roles: validator-family-orchestrator, multi-perspective-quality-gate, global-collapse-controller. Pipeline stages: validation design, parallel or staged evaluation, repair, global QMS collapse.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- high-stakes synthesis
- complex repository validation
- multiverse collapse
- long-form factual work
- safety-sensitive decisions

## When Not to Use

- one low-risk deterministic check is sufficient
- the caller cannot define a decision criterion or bounded exit
- distributed isolation is only nominal

## Scope

Canonical package: `parallel-qms@1.1.0`. ID: `PQ-00`. Functional classes: validation, orchestration. Activation: `U1-common-conditional`. Mechanism basis: `normalized-from-recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- a composed workflow needs structured quality evaluation

## Non-Triggers

- one low-risk deterministic check is sufficient
- the caller cannot define a decision criterion or bounded exit
- distributed isolation is only nominal

## Inputs / Required State

- candidate output or branches
- critical truths
- risk model
- selected mode plan
- independence boundaries
- veto predicates
- exit budget

## Outputs / Produced State

- per-mode validation ledger
- agreement and conflict map
- repair requests
- veto record
- global collapse decision
- convergence reason

## Mechanism

Select modes by distinct failure hypotheses, run them with separated evidence where independence matters, preserve typed outputs, and collapse only after resolving material disagreement and honoring vetoes. Mirror QMS compares two independently derived answers; Risk-Tier-Split allocates shallow, medium, or deep checks by consequence; Cross-Phase separately inspects factual, evaluative, framing, and hypothetical phases; Redundancy QMS seeks logical, structural, narrative, and safety corroboration; ExIt-Integrated couples scores to bounded repair and convergence; Hierarchical validates atom, paragraph/component, section/subsystem, and global levels; Transversal cuts across temporal, causal, modal, and logical dimensions; Heterogeneous assigns coherence, evidence, relevance, and safety to different validator lenses; Monte QMS perturbs assumptions, wording, or structure without claiming formal Monte Carlo; Inversion reasons from a proposed conclusion backward to required evidence; Conflict-Resolution classifies and adjudicates validator disagreement; Distributed QMS runs actually isolated instances before comparison; Meta-QMS evaluates validator consensus, consistency, calibration, and safety; Semantic Glass-Box exposes reasoning checkpoints and evidence paths; Ethical QMS applies a non-compensable harm or policy veto. Global collapse requires agreement on crucial truths, explicit treatment of conflicts, and survival of all safety vetoes—never majority alone.

## Procedure

1. State the decision, critical truths, risk tier, and stop conditions.
2. Choose only modes tied to plausible distinct failures: QMS-M for independent-answer agreement; QMS-RTS for consequence-scaled depth; QMS-XP for factual/evaluative/framing/hypothetical separation; QMS-R for logical/structural/narrative/safety redundancy; QMS-EI for bounded repair convergence; HQMS for atom-to-global hierarchy; T-QMS for temporal/causal/modal/logical cuts; hQMS for coherence/evidence/relevance/safety heterogeneity; mQMS for bounded perturbation; Inv-QMS for conclusion-to-evidence reversal; CR-QMS for disagreement resolution; dQMS only for real isolation; QMS² for evaluator-of-evaluators; SG-QMS for inspectable evidence paths; E-QMS for ethical veto.
3. Define inputs, independence boundaries, and typed pass/fail output for each selected mode.
4. Run independent modes without sharing draft conclusions when contamination would defeat the purpose.
5. Collect disagreements without averaging them away.
6. Use CR-QMS to classify factual, criteria, scope, or value conflict and request targeted repair.
7. Use QMS-EI to rerun only affected modes within a fixed budget and stop on convergence or stable failure.
8. Perform Global QMS Collapse: require crucial-truth agreement, cross-mode consistency, and no unresolved safety or ethical veto.
9. Return a decision plus per-mode ledger, minority findings, unresolved conflicts, and stop reason.

## Always-Do Rules

- Select modes by failure hypothesis, not quantity.
- Keep QMS-M and dQMS genuinely independent when claimed.
- Preserve mode-specific minority findings through collapse.
- Apply E-QMS and other hard vetoes outside weighted averaging.
- Bound ExIt repair cycles.

## Never-Do / Avoid Rules

- Call repeated passes by one shared-context evaluator distributed QMS.
- Describe mQMS as formal Monte Carlo without actual stochastic simulation.
- Collapse by simple majority.
- Let Meta-QMS replace primary evidence checks.
- Run every mode by default.

## Interaction Rules

### `multi-layer-consistency`

Provides the standalone vertical invariant model used by HQMS.

### `cross-universe-consistency`

Uses QMS evidence during branch collapse and checks cross-branch assumptions.

### `fermionic-veto`

Ensures a decisive contradiction survives aggregate scoring.

### `critical-atomic-verification`

Supplies critical truths that all selected modes must preserve.

### `bounded-exit`

Terminates QMS-EI refinement.

## Compatible Upgradeables

- `multi-layer-consistency` — Provides the standalone vertical invariant model used by HQMS.
- `cross-universe-consistency` — Uses QMS evidence during branch collapse and checks cross-branch assumptions.
- `fermionic-veto` — Ensures a decisive contradiction survives aggregate scoring.
- `critical-atomic-verification` — Supplies critical truths that all selected modes must preserve.
- `bounded-exit` — Terminates QMS-EI refinement.

## Counterbalancing Upgradeables

### `dynamic-depth-allocation`

Limits mode count and depth to consequence.

### `crispr-edit`

Constrains repair requested by validators to precise causal changes.

## Potential Redundancy

### `cross-checking-chains`

Chains are ordered dependencies; Parallel QMS is a selectable set of independent, cross-cutting, hierarchical, perturbative, reverse, meta, and veto topologies.

### `multi-layer-consistency`

HQMS is one mode inside the family, not the entire family.

## Conflict / Precedence Rules

- Crucial factual conflict must be resolved or surfaced before collapse.
- Safety and ethical vetoes cannot be outvoted.
- Dependent validators do not count as independent consensus.
- If Meta-QMS finds correlated evidence or inconsistent criteria, reduce confidence and rerun with corrected separation.
- Stable disagreement at the iteration limit yields abstention or an external decision, not fabricated consensus.

## Failure Boundary

- Do not certify while a crucial truth is disputed, a safety/ethical veto is active, validator independence is falsely claimed, or bounded repair fails to converge.

## Strong-Model Scaling

May skip:

- modes with no distinct failure hypothesis
- formal orchestration for a low-risk deterministic check

Keep mandatory:

- mode distinction
- critical-truth agreement
- conflict preservation
- veto survival
- bounded convergence
- honest independence labels

## Recommended Skill Types

- analysis and decision support
- high-stakes evidence work
- long-context workflows
- multi-step task execution

## Example Composition

**Task context:** A frontier-model skill for reviewing pull requests must be validated before community release.

**Why it activates:** It has factual instructions, workflow structure, safety behavior, and cross-file consistency risks.

**Inputs/state:** Skill files, schema, tests, contribution contract, and release criteria.

**Action:** Uses HQMS across instruction/test/repository levels, T-QMS for causal and logical review flow, Inv-QMS from promised result back to required checks, SG-QMS for traceability, and E-QMS for unsafe advice; QMS-EI bounds repair to two passes before global collapse.

**Does not:** Launch 15 identical reviewers or approve on majority when E-QMS finds unsafe behavior.

**Result/state change:** The release ledger shows distinct passes, one repaired traceability gap, no veto, and explicit convergence.

**Companions:** ['multi-layer-consistency', 'critical-atomic-verification', 'bounded-exit', 'fermionic-veto']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `PQ-00` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: Parallel-QMS.

Source support: `sufficiently-recovered`. Mechanism basis: `normalized-from-recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — OS Philosophy and Upgradeable-to-Skill Translation Catalog (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 9. Parallel-QMS recovered family (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 8. PARALLEL-QMS — DEEP HISTORICAL OPERATING DETAILS (historical_assistant_artifact)
