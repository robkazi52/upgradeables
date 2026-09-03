# Citation Fidelity Gate

## Summary

A claim-to-source gate that separately verifies source existence, claim support, quotation exactness, paraphrase preservation, and correct source adjacency.

## Purpose

Ensure citations prove the precise nearby claim instead of functioning as decorative evidence.

## Problem Solved

Models often cite a real source that discusses the topic but does not support the exact claim, silently alter quotations, or borrow support from an adjacent citation.

## Where It Fits in the OS

Roles: evidence-entailment-gate, quotation-integrity-validator, provenance-controller. Pipeline stages: evidence collection, draft validation, pre-publication.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- research reports
- technical documentation
- legal or policy synthesis
- fact-checked public writing

## When Not to Use

- the output contains no externally attributed factual claims
- the task explicitly requests unsupported fiction

## Scope

Canonical package: `citation-fidelity@1.1.0`. ID: `T3-13`. Functional classes: validation, truth-grounding. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- output contains citations or source-attributed claims

## Non-Triggers

- the output contains no externally attributed factual claims
- the task explicitly requests unsupported fiction

## Inputs / Required State

- claim atoms
- citation locators
- source artifacts
- quotation/paraphrase text
- version metadata

## Outputs / Produced State

- claim-citation entailment ledger
- quote comparison
- unsupported-atom list
- corrected citations or downgraded claims

## Mechanism

For every citation-bearing claim, open the exact cited artifact and pass five independent tests: the artifact exists and is the represented edition; the cited passage entails the full claim including qualifiers; quoted text matches exactly; paraphrase retains scope, modality, polarity, and attribution; and evidence belongs to this claim rather than being borrowed from an adjacent citation, nearby sentence, or different source. A failure at any layer blocks the claim, even if the source is authoritative.

## Procedure

1. Atomize each externally checkable claim and bind each citation to a specific atom.
2. Resolve the cited artifact, version, locator, and authorship.
3. Inspect the cited passage rather than relying on search snippets or secondary descriptions.
4. Test entailment of subject, predicate, scope, date, quantity, and modal strength.
5. For quotes, compare exact words and mark every omission or alteration.
6. For paraphrases, compare meaning, qualifiers, uncertainty, and attribution.
7. Check that evidence was not borrowed from an adjacent citation or adjacent passage.
8. Downgrade, recite, replace, or remove any unsupported atom and record the decision.

## Always-Do Rules

- Bind citations at claim-atom granularity.
- Preserve uncertainty and limitations from the source.
- Use direct primary support when the claim represents primary findings.

## Never-Do / Avoid Rules

- Treat source existence as proof of claim support.
- Use a search-result snippet as the final evidence check.
- Make a paraphrase more certain or general than the source.
- Let one citation silently support multiple unrelated neighboring claims.

## Interaction Rules

### `grounding-no-invention`

Removes unsupported facts discovered by the citation audit.

### `critical-atomic-verification`

Defines and checks the precise claim atoms cited.

### `truth-priority-hierarchy`

Resolves conflicts among primary, secondary, and stale sources.

## Compatible Upgradeables

- `grounding-no-invention` — Removes unsupported facts discovered by the citation audit.
- `critical-atomic-verification` — Defines and checks the precise claim atoms cited.
- `truth-priority-hierarchy` — Resolves conflicts among primary, secondary, and stale sources.

## Counterbalancing Upgradeables

### `specificity-penalty-gate`

Discourages unnecessary precision that the available citation cannot support.

## Potential Redundancy

### `critical-atomic-verification`

CAV may verify from any evidence; Citation Fidelity additionally audits citation identity, attachment, quotation, and paraphrase behavior.

## Conflict / Precedence Rules

- The source passage outranks a draft's intended meaning.
- A precise unsupported subclaim must be removed even when the broader sentence is supported.
- A secondary source cannot be cited as if it were the primary experiment.

## Failure Boundary

- Block any material claim whose cited artifact cannot be opened, whose passage does not entail it, or whose quote/paraphrase changes meaning.

## Strong-Model Scaling

May skip:

- formal ledger formatting for a single low-stakes citation

Keep mandatory:

- direct passage inspection
- claim-level entailment
- quote exactness
- paraphrase scope and modality
- adjacent-source separation

## Recommended Skill Types

- research reports
- technical documentation
- legal or policy synthesis
- fact-checked public writing

## Example Composition

**Task context:** A report says a study proves an intervention reduces risk by 40 percent and cites the paper.

**Why it activates:** A real citation may not support the magnitude, population, or causal verb.

**Inputs/state:** The report sentence, DOI, paper version, table, and limitations section.

**Action:** Finds the 40 percent is a subgroup association, verifies no causal design, and narrows the sentence.

**Does not:** Pass the sentence merely because the paper mentions the intervention and risk.

**Result/state change:** The claim becomes a correctly scoped subgroup association with a pinpoint citation.

**Companions:** ['critical-atomic-verification', 'grounding-no-invention', 'truth-priority-hierarchy']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T3-13` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T3-13. Citation Fidelity Gate (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — T3-13. Citation Fidelity Gate (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 17. VERBATIM-COPY / FIDELITY WORKFLOW (historical_assistant_artifact)
