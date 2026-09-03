# Image Text Fidelity Capture (`image-text-fidelity-capture@1.1.0`)

Purpose: Create a source-faithful textual representation of image-borne evidence for downstream indexing, analysis, or copying.

Activate when: an image contains source text to transcribe.

Do not use when: no image contains source text or visible structure; the task asks for visual interpretation rather than faithful capture and that different mode is not declared.

Requires: none.

## Runtime mechanism

Traverse the image in a declared order, transcribe only visible characters, and reconstruct headings, rows, columns, or spatial groups only where visible evidence supports them. Unreadable regions receive explicit illegible/uncertain markers linked to their location; context is never used to silently complete missing text.

## Procedure

1. Record the image/page identifier and reading order.
2. Segment visible text and structural regions.
3. Transcribe characters exactly, preserving capitalization, numbers, and punctuation where legible.
4. Represent visible layout without inferring hidden cells or labels.
5. Mark obscured or ambiguous regions with location-specific uncertainty.

## Guardrails

- Mandatory even on strong models: only visible evidence may determine captured text or structure.
- Conflict/precedence: Visible evidence outranks grammatical completion; If layout and lexical readings conflict, preserve both uncertainty and coordinates rather than choosing silently.
- Stop or fail when: If a region is not legible enough to verify, mark it uncertain and do not produce a confident transcription for that region.

Full package and provenance: [`image-text-fidelity-capture`](../../upgradeables/truth-grounding/image-text-fidelity-capture/UPGRADEABLE.md).
