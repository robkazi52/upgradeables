# Safe Rewrite Logic (`safe-rewrite@1.1.0`)

Purpose: Make paraphrase, polish, tone, or formatting safe by treating content atoms as invariants rather than suggestions.

Activate when: paraphrasing, polishing, or format conversion.

Do not use when: the user asks to change substantive meaning; the source is internally contradictory and needs adjudication.

Requires: none.

## Runtime mechanism

Extract a before-state ledger of factual and constraint atoms, mark the dimensions authorized to change, perform the rewrite only along those dimensions, then compare names, numbers, dates, quotes, citations, modality, requirements, and causal claims. Any atom difference not explicitly authorized is reverted or surfaced for approval.

## Procedure

1. Identify authorized change dimensions such as tone, length, format, or reading level.
2. Extract locked atoms: claims, entities, numbers, dates, quotations, citations, requirements, negations, and uncertainty markers.
3. Rewrite without adding evidence or changing the locked atoms.
4. Diff the rewritten artifact against the atom ledger and inspect citation-to-claim fit.
5. Restore unauthorized changes and report any requested transformation that cannot preserve meaning.

## Guardrails

- Mandatory even on strong models: internal atom extraction; authorized-dimension discipline; post-rewrite names/numbers/dates/quotes/citations check.
- Conflict/precedence: Truth and locked constraints outrank requested style; If shortening would remove a required qualification, keep the qualification or report the conflict.
- Stop or fail when: semantic drift; citation drift.

Full package and provenance: [`safe-rewrite`](../../upgradeables/editing-repair/safe-rewrite/UPGRADEABLE.md).
