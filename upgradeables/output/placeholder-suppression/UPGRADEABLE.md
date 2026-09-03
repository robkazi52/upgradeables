# Placeholder Suppression

## Summary

Blocks finalization until unfinished markers, dummy values, unresolved variables, and empty required sections are resolved, omitted, or clearly labeled.

## Purpose

Prevent scaffolding artifacts from escaping as if they were complete content.

## Problem Solved

Templates and multi-stage generation leave TODOs, bracket prompts, synthetic values, interpolation tokens, or structurally empty requirements that readers may mistake for finished output.

## Where It Fits in the OS

Roles: final-output guard, completion validator. Pipeline stages: artifact assembly, pre-release scan, finalization gate.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- template-based documents
- generated repositories
- forms and reports
- configuration generation
- multi-agent artifact assembly

## When Not to Use

- the deliverable is explicitly a template whose placeholders are the product
- an example intentionally teaches placeholder syntax
- redacted fields must retain an approved marker

## Scope

Canonical package: `placeholder-suppression@1.1.0`. ID: `T1-08`. Functional classes: output, validation. Activation: `U1-common-conditional`. Mechanism basis: `recovered`. Activation cost: `low` (architectural burden, not measured compute).

## Trigger Conditions

- templates or staged artifacts are finalized

## Non-Triggers

- the deliverable is explicitly a template whose placeholders are the product
- an example intentionally teaches placeholder syntax
- redacted fields must retain an approved marker

## Inputs / Required State

- artifact
- required-field schema
- marker patterns
- intentional-placeholder allowlist
- authoritative replacement values

## Outputs / Produced State

- placeholder inventory
- resolved or classified hits
- clean rescan
- pass or blocked finalization decision

## Mechanism

Run a two-layer completion scan: a lexical detector for markers such as TODO, TBD, FIXME, bracket prompts, dummy domains, sample IDs, and unresolved interpolation syntax; then a schema detector for empty required sections, null required fields, and uninstantiated variables. Classify every hit using a narrow allowlist for intentional template, example, or redaction contexts; all other hits must be filled from authority, removed with requirement revalidation, or explicitly labeled unresolved before release.

## Procedure

1. Load the artifact's required sections, fields, and variable schema.
2. Scan text and code for known marker tokens, dummy values, bracketed instructions, and unresolved interpolation forms.
3. Scan structure for empty or default-valued required elements.
4. Classify hits as accidental, intentionally illustrative, approved redaction, or genuinely unresolved using context and an explicit allowlist.
5. Resolve accidental hits from authoritative inputs, omit only when the requirement permits, and label genuine gaps with impact and owner.
6. Rescan the final artifact and fail the release gate on any unclassified or accidental hit.

## Always-Do Rules

- combine lexical and structural scans
- use contextual allowlisting rather than global token exceptions
- rescan after resolution
- distinguish explicit unresolved disclosure from accidental placeholder leakage

## Never-Do / Avoid Rules

- replace unknown values with plausible inventions
- delete a required section just to clear the scan
- flag every bracket in code or citation as a placeholder
- allow an unclassified marker in final output

## Interaction Rules

### `safe-rewrite`

Safe Rewrite removes or labels placeholders without altering neighboring facts.

### `parallel-qms`

Final Validation treats an unresolved accidental marker as a release-blocking defect.

## Compatible Upgradeables

- `safe-rewrite` — Safe Rewrite removes or labels placeholders without altering neighboring facts.
- `parallel-qms` — Final Validation treats an unresolved accidental marker as a release-blocking defect.

## Counterbalancing Upgradeables

### `safe-rewrite`

An explicit template context protects intentional placeholders from destructive suppression.

## Potential Redundancy

### `grounding-no-invention`

Grounding prevents invented replacements; Placeholder Suppression specifically detects unfinished output artifacts and completion gaps.

## Conflict / Precedence Rules

- Never fabricate content to satisfy completion.
- Approved template and example placeholders remain only when clearly scoped and non-executable.
- A required unknown is labeled unresolved and blocks completion when the contract requires a concrete value.

## Failure Boundary

- false completion
- fabricated replacements
- overbroad allowlist
- false positives on legitimate syntax
- empty required structure

## Strong-Model Scaling

May skip:

- reporting every zero-hit pattern in the final response

Keep mandatory:

- lexical plus schema scan
- context-specific classification
- post-fix rescan
- fail-closed finalization

## Recommended Skill Types

- template-based documents
- generated repositories
- forms and reports
- configuration generation
- multi-agent artifact assembly

## Example Composition

**Task context:** Publish a generated GitHub repository.

**Why it activates:** README templates, manifests, and examples may retain setup prompts or dummy URLs.

**Inputs/state:** Repository files, manifest schema, approved example fixtures, and project metadata are available.

**Action:** Finds a `[your-org]` README token, an empty license field, and `example.com` in a test fixture; resolves the first two and allowlists the fixture by path before rescanning.

**Does not:** Replace the license with a guess or globally allow every `example.com` occurrence.

**Result/state change:** A release with no accidental placeholders and one documented intentional fixture.

**Companions:** ['safe-rewrite', 'grounding-no-invention']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T1-08` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: None.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T1-08. Placeholder Suppression (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 5. January 5, 2026 — training/scaffolding Upgradeables snapshot (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 17. VERBATIM-COPY / FIDELITY WORKFLOW — EXAMPLE OF UPGRADEABLE COMPOSITION (historical_assistant_artifact)
