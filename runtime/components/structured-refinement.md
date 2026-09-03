# Structured Refinement Cycles (`structured-refinement@1.1.0`)

Purpose: Prevent one revision pass from trading away correctness while improving structure or style.

Activate when: revision has multiple defect classes.

Do not use when: only one bounded defect exists; the artifact requires complete regeneration.

Requires: none.

## Runtime mechanism

Classify defects before editing and run passes in dependency order: facts and source mapping first, structure and requirement coverage second, style and pedagogy third, final validation last. Accepted decisions are locked between passes, and a later pass may not silently reopen an earlier one.

## Procedure

1. Inventory defects and assign each to factual, structural, stylistic, or validation class.
2. Correct facts, citations, and locked constraints; freeze the accepted semantic ledger.
3. Repair ordering, dependencies, section roles, and requirement coverage without changing the frozen facts.
4. Adjust voice, clarity, and pedagogy without changing facts or structure except where explicitly authorized.
5. Run an independent final check across all classes and use Bounded ExIt to decide whether another pass is justified.

## Guardrails

- Mandatory even on strong models: dependency order; between-pass locks; final cross-class review.
- Conflict/precedence: Factual correctness outranks structural elegance and style; A later pass that discovers an upstream defect returns explicitly to the relevant pass and revalidates downstream results.
- Stop or fail when: mixed-objective drift; later-pass regression.

Full package and provenance: [`structured-refinement`](../../upgradeables/editing-repair/structured-refinement/UPGRADEABLE.md).
