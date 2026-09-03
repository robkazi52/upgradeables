# Progressive Context Intake (`activation-budget-funnel@1.1.0`)

Recovered name: Activation-Budget Funnel

Purpose: Protect limited active context by progressively disclosing sources and transferring verified evidence into compact indexed state before higher-level decisions.

Activate when: many sources or modules compete for attention.

Do not use when: a short single source fits comfortably in context; creative work uses no references.

Requires: none.

## Runtime mechanism

Admit only a bounded set of live source or module pulls, historically roughly five to seven, and move each through a fixed funnel: retrieve, quote or capture, index verified atoms, transform those atoms, write from the index, then verify against sources. Retire raw pulls from active attention after their durable evidence is indexed so retrieval and decision-making do not compete in one step.

## Procedure

1. Define the question and the evidence fields the task needs.
2. Queue candidate sources or modules rather than activating all of them.
3. Retrieve a bounded batch, keeping roughly no more than five to seven active pulls when that heuristic fits the host.
4. Capture source-grounded quotes or facts with provenance.
5. Index verified atoms into compact state and release unneeded raw context.

## Guardrails

- Mandatory even on strong models: retrieval-before-synthesis separation; provenance-preserving indexing; claim-to-source verification.
- Conflict/precedence: Source-boundary and authority rules control what may enter the funnel; If compacting an item would lose evidence needed for verification, retain or reload the source rather than forcing it through the budget.
- Stop or fail when: Pause synthesis when evidence has not been captured with provenance or active pulls cannot be bounded without losing required coverage; Fail verification when a synthesized claim cannot be traced back through the index.

Full package and provenance: [`activation-budget-funnel`](../../upgradeables/context-retrieval/activation-budget-funnel/UPGRADEABLE.md).
