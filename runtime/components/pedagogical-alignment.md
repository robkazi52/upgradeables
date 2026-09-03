# Pedagogical Alignment Constraint (`pedagogical-alignment@1.1.0`)

Purpose: Make correct content learnable and usable for a specified audience without diluting claims or inventing simplifications.

Activate when: an audience or teaching level is known.

Do not use when: the audience and purpose cannot be inferred and the choice materially changes content; exact legal or technical wording must remain verbatim.

Requires: none.

## Runtime mechanism

Build a compact audience model—known prerequisites, target capability, jargon tolerance, and action context—then choose the smallest conceptual steps that bridge from that model to the target. Define or replace jargon at first use, order prerequisite before dependent ideas, add an example only where it resolves a likely misconception, and run an accuracy-backcheck against the unsimplified claim.

## Procedure

1. Identify the reader's likely starting knowledge and the capability they need after reading.
2. List prerequisites and terms that the explanation currently assumes.
3. Sequence content from familiar anchor through the minimum conceptual bridge to the target.
4. Define necessary jargon or replace it with accurate plain language; add a representative example where abstraction alone is likely to fail.
5. Back-check every simplification, analogy, and example against the original technical claim and retain important limitations.

## Guardrails

- Mandatory even on strong models: internal prerequisite model; accuracy back-check; boundary-preserving simplification.
- Conflict/precedence: Accuracy, scope, and uncertainty outrank ease of explanation; Exact source language is preserved in quoted or zero-drift zones and explained around rather than rewritten.
- Stop or fail when: oversimplification; undefined jargon.

Full package and provenance: [`pedagogical-alignment`](../../upgradeables/output/pedagogical-alignment/UPGRADEABLE.md).
