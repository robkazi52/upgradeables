# Image Text Fidelity Capture

## Summary

The Image Text Fidelity Capture sense of ITFC transcribes visible text and reconstructs visible layout from images while marking, rather than guessing, obscured or illegible content.

## Purpose

Create a source-faithful textual representation of image-borne evidence for downstream indexing, analysis, or copying.

## Problem Solved

Prevents OCR-like completion, inferred missing words, and invented structural relationships from entering the source record.

## Where It Fits in the OS

Roles: evidence-capture, image-fidelity-guard. Pipeline stages: source-intake, evidence-capture, capture-validation.

This component acts within those stages; it does not take over the complete task or outrank the host Skill.

## Best-Fit Activities / Tasks

- document image transcription
- figure or screenshot capture
- scanned-record intake
- long-document source fidelity

## When Not to Use

- no image contains source text or visible structure
- the task asks for visual interpretation rather than faithful capture and that different mode is not declared

## Scope

Canonical package: `image-text-fidelity-capture@1.1.0`. ID: `T2-14A`. Functional classes: context-retrieval, truth-grounding. Activation: `U2-specialized`. Mechanism basis: `recovered`. Activation cost: `medium` (architectural burden, not measured compute).

## Trigger Conditions

- an image contains source text to transcribe

## Non-Triggers

- no image contains source text or visible structure
- the task asks for visual interpretation rather than faithful capture and that different mode is not declared

## Inputs / Required State

- source image
- page/image identifier
- reading-order or region instructions
- fidelity requirements

## Outputs / Produced State

- verified transcription
- visible-structure map
- location-specific uncertainty markers
- capture verification status

## Mechanism

Traverse the image in a declared order, transcribe only visible characters, and reconstruct headings, rows, columns, or spatial groups only where visible evidence supports them. Unreadable regions receive explicit illegible/uncertain markers linked to their location; context is never used to silently complete missing text.

## Procedure

1. Record the image/page identifier and reading order.
2. Segment visible text and structural regions.
3. Transcribe characters exactly, preserving capitalization, numbers, and punctuation where legible.
4. Represent visible layout without inferring hidden cells or labels.
5. Mark obscured or ambiguous regions with location-specific uncertainty.
6. Run a second pass against the image and finalize only verified capture.

## Always-Do Rules

- Preserve visible spelling, numbers, labels, and structure.
- Mark uncertainty at the exact region.
- Keep the ITFC acronym collision explicit in provenance.

## Never-Do / Avoid Rules

- Autocomplete an obscured word from context.
- Invent a table cell or reading order not visible in the image.
- Merge this package with the unresolved Intent/Task Framing Controller sense of ITFC.

## Interaction Rules

### `grounding-no-invention`

Prevents contextual guessing during capture.

### `zero-drift-zones`

Locks verified transcription atoms against later rewriting.

### `citation-fidelity`

Can verify later claims or quotations against the captured source region.

## Compatible Upgradeables

- `grounding-no-invention` — Prevents contextual guessing during capture.
- `zero-drift-zones` — Locks verified transcription atoms against later rewriting.
- `citation-fidelity` — Can verify later claims or quotations against the captured source region.

## Counterbalancing Upgradeables

No natural counterbalance was identified after review; ordinary authority, scope, and validation controls still apply.

## Potential Redundancy

### `grounding-no-invention`

Grounding supplies the general no-invention rule; Image Text Fidelity Capture adds image segmentation, reading order, and legibility handling.

## Conflict / Precedence Rules

- Visible evidence outranks grammatical completion.
- If layout and lexical readings conflict, preserve both uncertainty and coordinates rather than choosing silently.

## Failure Boundary

- If a region is not legible enough to verify, mark it uncertain and do not produce a confident transcription for that region.

## Strong-Model Scaling

May skip:

- verbose region narration for a short, plainly legible image

Keep mandatory:

- only visible evidence may determine captured text or structure

## Recommended Skill Types

- document image transcription
- figure or screenshot capture
- scanned-record intake
- long-document source fidelity

## Example Composition

**Task context:** A scanned form has one partly obscured account number and visible row labels.

**Why it activates:** Text must be captured from an image for evidence use.

**Inputs/state:** The page image and a requirement for exact transcription.

**Action:** Transcribes legible digits, preserves row order, and marks the obscured digits with their location.

**Does not:** Infer the missing digits from another identifier.

**Result/state change:** A usable transcription whose uncertainty remains auditable.

**Companions:** ['grounding-no-invention', 'zero-drift-zones']

## Tests

See [`tests/cases.json`](tests/cases.json) for six structured behavior cases and [`tests/composition.md`](tests/composition.md) for the human-readable expectations. Behavioral cases are specifications until run through a real model adapter; CI validates their structure, not model quality.

## Provenance / Historical Aliases

Primary source ID: `T2-14A` in `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md`. Registry generation: `consolidated-2026-09`. Historical aliases: ITFC.

Source support: `sufficiently-recovered`. Mechanism basis: `recovered`.

Structured source references:

- OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md — T2-14. ITFC — Historical Acronym Collision (current_consolidated_catalog)
- OS_Upgradeables_Historical_Recovery_Inventory.md — 7. ABF, ITFC, OCG, ECL — corrections and collisions (historical_recovery_inventory)
- OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md — 17. VERBATIM-COPY / FIDELITY WORKFLOW — EXAMPLE OF UPGRADEABLE COMPOSITION (historical_assistant_artifact)
