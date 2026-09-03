# Placeholder Suppression (`placeholder-suppression@1.1.0`)

Purpose: Prevent scaffolding artifacts from escaping as if they were complete content.

Activate when: templates or staged artifacts are finalized.

Do not use when: the deliverable is explicitly a template whose placeholders are the product; an example intentionally teaches placeholder syntax.

Requires: none.

## Runtime mechanism

Run a two-layer completion scan: a lexical detector for markers such as TODO, TBD, FIXME, bracket prompts, dummy domains, sample IDs, and unresolved interpolation syntax; then a schema detector for empty required sections, null required fields, and uninstantiated variables. Classify every hit using a narrow allowlist for intentional template, example, or redaction contexts; all other hits must be filled from authority, removed with requirement revalidation, or explicitly labeled unresolved before release.

## Procedure

1. Load the artifact's required sections, fields, and variable schema.
2. Scan text and code for known marker tokens, dummy values, bracketed instructions, and unresolved interpolation forms.
3. Scan structure for empty or default-valued required elements.
4. Classify hits as accidental, intentionally illustrative, approved redaction, or genuinely unresolved using context and an explicit allowlist.
5. Resolve accidental hits from authoritative inputs, omit only when the requirement permits, and label genuine gaps with impact and owner.

## Guardrails

- Mandatory even on strong models: lexical plus schema scan; context-specific classification; post-fix rescan.
- Conflict/precedence: Never fabricate content to satisfy completion; Approved template and example placeholders remain only when clearly scoped and non-executable.
- Stop or fail when: false completion; fabricated replacements.

Full package and provenance: [`placeholder-suppression`](../../upgradeables/output/placeholder-suppression/UPGRADEABLE.md).
