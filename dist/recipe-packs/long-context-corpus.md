# Long-Context / Corpus — Runtime Pack

Purpose: Analyze a corpus too large for one context while preserving sequence, provenance, and resumable state.

Task family: large-corpus analysis and resumable document workflows

Activation boundary: Use when the authorized corpus cannot be handled safely as one undifferentiated context and indexed state must preserve sequence and provenance.

Use this generated pack for execution. Do not also load the source recipe,
resolved recipe, catalog record, or full packages unless a material ambiguity
requires deeper inspection.

`R` owns a required guarantee but may remain dormant until its pipeline phase.
`A`, `C`, and `O` still require active triggers. `X` remains excluded without
a task-specific reason.

## Composition

Frame and lock the task, establish explicit state, load evidence and behavior
components, perform the task, then run applicable validators. Increase depth
with risk; remove scaffolding that has no active trigger.

## Output contract

Return the requested artifact, evidence, limitations, and unresolved inputs.

## Component routing

| Role | Component | Activate when |
|:---:|---|---|
| R | `stateblock@1.1.0` — Canonical Task State | work spans multiple steps or components |
| R | `sequential-memory-state-engine@1.1.0` — Ordered Memory-State Update Engine | state changes across steps or source chunks |
| A | `working-memory-lock-in@1.1.0` — Working-Memory Lock-In | critical state competes with large context |
| R | `stable-long-context@1.1.0` — Stable Long-Context | large corpus or long-running workflow |
| R | `activation-budget-funnel@1.1.0` — Progressive Context Intake | many sources or modules compete for attention |
| A | `attention-compression-scaffold@1.1.0` — Temporary Focused-Context View | source volume exceeds the active workspace |
| A | `neuro-focus@1.1.0` — Bounded Attention Focus | large sources or a narrow debug region demand concentration |
| R | `drift-suppression@1.1.0` — Drift Suppression | long, branching, or iterative work |
| A | `coherence-heartbeat@1.1.0` — Periodic Whole-Task Consistency Check | a workflow is long or multi-stage |
| C | `cross-context-resonance-lock@1.1.0` — Cross-Context Relationship Guard | related contexts must stay aligned across a long task |
| A | `state-snapshot@1.1.0` — State Snapshot | a workflow pauses, hands off, or persists |
| C | `citation-fidelity@1.1.0` — Citation Fidelity Gate | output contains citations or source-attributed claims |

## Runtime component cards

### R — Canonical Task State

Recovered name: StateBlock

Purpose: Give tools, agents, validators, and handoffs a shared source of current task truth.

Activate when: work spans multiple steps or components.

Do not use when: a trivial one-turn task needs no persistent state; the proposed schema would collect unnecessary sensitive data.

Requires: none.

#### Runtime mechanism

Define a typed block with identity, objective, authority, constraints, active mode, progress, evidence pointers, decisions, uncertainties, open actions, and version metadata. Assign each field an owner and mutability rule; update through validated deltas, and derive views from this block so no consumer silently becomes a second authority.

#### Procedure

1. Select only fields required to execute and verify the task.
2. Declare field types, authority, mutability, and sensitivity.
3. Initialize values from clarified instructions and canonical sources.
4. Route changes through validated versioned deltas.
5. Expose least-privilege projections to consumers.

#### Guardrails

- Mandatory even on strong models: single source of truth; locked-field authority; explicit unknowns.
- Conflict/precedence: System and explicit task authority govern locked fields; evidence updates factual fields only through their declared owners; Version conflicts must be resolved before action; never merge incompatible values by concatenation.
- Stop or fail when: Do not proceed on dependent actions when required state is contradictory or unknown; Fall back to an explicit local checklist if the host cannot maintain a reliable shared block.

Full package and provenance: [`stateblock`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/state/stateblock/UPGRADEABLE.md).

### R — Ordered Memory-State Update Engine

Recovered name: Sequential Memory State Engine (SMSE)

Purpose: Preserve sequence, provenance, relevance, and current truth across long-running work.

Activate when: state changes across steps or source chunks.

Do not use when: a one-shot task has no state evolution; event ordering cannot be established and ordering is safety-critical.

Requires: none.

#### Runtime mechanism

For each event, preserve source and time, normalize it into the state schema, classify affected fields, compare with the current version, resolve contradiction by authority and recency rules, commit an atomic delta, derive consumer-specific projections, and emit a checkpoint. History remains available, but only the resolved current state drives action.

#### Procedure

1. Ingest one event with source, time, and authority metadata.
2. Normalize it without discarding the original payload pointer.
3. Classify affected state fields and compare against the current version.
4. Resolve additions, updates, contradictions, and retractions using explicit precedence.
5. Commit the delta atomically and increment the version.

#### Guardrails

- Mandatory even on strong models: ordered transitions; provenance; current/history separation.
- Conflict/precedence: Authority outranks recency unless the authoritative source explicitly delegates update power; Unresolvable contradictions remain labeled and block dependent actions rather than being averaged.
- Stop or fail when: Stop dependent actions when a safety-critical contradiction cannot be resolved; Do not assert chronological correctness when timestamps or event identity are missing.

Full package and provenance: [`sequential-memory-state-engine`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/state/sequential-memory-state-engine/UPGRADEABLE.md).

### A — Working-Memory Lock-In

Purpose: Prevent critical goals, constraints, identifiers, or safety conditions from being displaced by incoming context.

Activate when: critical state competes with large context.

Do not use when: nothing needs continuous salience; the proposed lock is large enough to crowd out working context.

Requires: none.

#### Runtime mechanism

Select only the invariants whose omission would materially corrupt the task, store canonical pointers plus compact current values, and run a heartbeat before major actions to confirm freshness and consistency. Refresh on accepted state change; if a locked item conflicts or goes stale, block dependent work until reconciled.

#### Procedure

1. Rank candidate state by consequence of omission.
2. Lock the smallest critical subset with canonical field pointers and version.
3. Check it before major actions and after context changes.
4. Refresh values only from accepted canonical updates.
5. Block or reconcile when a locked value is missing, stale, or contradictory.

#### Guardrails

- Mandatory even on strong models: small high-consequence invariant set; canonical pointers; freshness checks.
- Conflict/precedence: Canonical accepted state overrides cached values after validation; A stale or contradictory safety-critical lock blocks dependent execution; lower-authority context cannot resolve it.
- Stop or fail when: Do not proceed when a critical locked field cannot be reconciled; Shrink the set when lock overhead begins to reduce task performance.

Full package and provenance: [`working-memory-lock-in`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/state/working-memory-lock-in/UPGRADEABLE.md).

### R — Stable Long-Context

Purpose: Extend usable context duration without treating the entire transcript as equally current or important.

Activate when: large corpus or long-running workflow.

Do not use when: all relevant material fits clearly in one short exchange; lossless verbatim retention is required for every item.

Requires: none.

#### Runtime mechanism

Maintain an invariant anchor containing task, authority, definitions, accepted decisions, and open obligations; keep detailed material behind stable indexed pointers; periodically reconcile new state, mark superseded items, and regenerate a compact current view. Retrieval expands only the region needed for the next step, and final validation checks output against the anchors rather than conversational recency.

#### Procedure

1. Establish task, authority, terminology, and zero-drift facts as anchors.
2. Index detailed evidence and prior artifacts with stable identifiers.
3. At checkpoints, merge accepted deltas and mark replaced state as superseded.
4. Compact the active view while preserving pointers and unresolved items.
5. On resume, load the anchor first, then retrieve only the relevant detail.

#### Guardrails

- Mandatory even on strong models: anchored invariants; current-versus-superseded distinction; retrievable provenance.
- Conflict/precedence: Explicit authority and accepted state transitions outrank recency; If compaction cannot preserve a high-impact nuance, retain the original excerpt or pointer in the active view.
- Stop or fail when: Do not compact evidence beyond recoverability when precise citation is required; Rebuild from canonical sources when anchor integrity or version lineage is uncertain.

Full package and provenance: [`stable-long-context`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/state/stable-long-context/UPGRADEABLE.md).

### R — Progressive Context Intake

Recovered name: Activation-Budget Funnel

Purpose: Protect limited active context by progressively disclosing sources and transferring verified evidence into compact indexed state before higher-level decisions.

Activate when: many sources or modules compete for attention.

Do not use when: a short single source fits comfortably in context; creative work uses no references.

Requires: none.

#### Runtime mechanism

Admit only a bounded set of live source or module pulls, historically roughly five to seven, and move each through a fixed funnel: retrieve, quote or capture, index verified atoms, transform those atoms, write from the index, then verify against sources. Retire raw pulls from active attention after their durable evidence is indexed so retrieval and decision-making do not compete in one step.

#### Procedure

1. Define the question and the evidence fields the task needs.
2. Queue candidate sources or modules rather than activating all of them.
3. Retrieve a bounded batch, keeping roughly no more than five to seven active pulls when that heuristic fits the host.
4. Capture source-grounded quotes or facts with provenance.
5. Index verified atoms into compact state and release unneeded raw context.

#### Guardrails

- Mandatory even on strong models: retrieval-before-synthesis separation; provenance-preserving indexing; claim-to-source verification.
- Conflict/precedence: Source-boundary and authority rules control what may enter the funnel; If compacting an item would lose evidence needed for verification, retain or reload the source rather than forcing it through the budget.
- Stop or fail when: Pause synthesis when evidence has not been captured with provenance or active pulls cannot be bounded without losing required coverage; Fail verification when a synthesized claim cannot be traced back through the index.

Full package and provenance: [`activation-budget-funnel`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/context-retrieval/activation-budget-funnel/UPGRADEABLE.md).

### A — Temporary Focused-Context View

Recovered name: Attention Compression Scaffold

Purpose: Reduce attention burden while retaining the facts, constraints, provenance, and retrieval pointers required by the current subtask.

Activate when: source volume exceeds the active workspace.

Do not use when: the original context is already small; exact source wording must remain live.

Requires: none.

#### Runtime mechanism

Modern operational interpretation: select task-relevant facts, locked literals, decisions, open questions, and source pointers from a larger context; encode them in a compact indexed view; validate that protected meaning and provenance remain recoverable; and keep a route back to the original material. Compression changes representation size, not truth status or authority.

#### Procedure

1. Define the current subtask and protected atoms that compression must preserve.
2. Partition context into retain verbatim, summarize with provenance, pointer-only, and retire classes.
3. Build a compact indexed view with stable source references.
4. Check every locked atom and decision against the original context.
5. Use the compact view for the subtask while retaining reload pointers.

#### Guardrails

- Mandatory even on strong models: protected-atom preservation; provenance and reloadability; invalidation on state change.
- Conflict/precedence: Zero-drift and source-fidelity requirements override compression goals; If meaning preservation cannot be verified, use the original context or a pointer rather than a lossy substitute.
- Stop or fail when: Do not activate the compressed view when a protected fact, conflict, or provenance link is lost or unverifiable.

Full package and provenance: [`attention-compression-scaffold`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/context-retrieval/attention-compression-scaffold/UPGRADEABLE.md).

### A — Bounded Attention Focus

Recovered name: Neuro-Focus

Purpose: Increase depth and signal quality on a bounded target when irrelevant material would otherwise dilute effort.

Activate when: large sources or a narrow debug region demand concentration.

Do not use when: the task requires broad discovery before a target is known; decisive evidence has not yet been sampled.

Requires: none.

#### Runtime mechanism

Rank active regions by relevance to the locked task and expected decision impact, choose a bounded focus corridor, suppress unrelated material from the live workspace without deleting it, and periodically test whether excluded regions now contain material counterevidence. The recovered Neuro-Focus purpose and its Anti-Tunnel Vision caution support this normalized control; it is not a neurological claim.

#### Procedure

1. Lock the question and define what evidence would make a region high value.
2. Score or order candidate regions by relevance, uncertainty reduction, and consequence.
3. Activate the smallest region sufficient for deep work and retain pointers to excluded regions.
4. Perform the focused analysis or repair.
5. At checkpoints, invoke an alternative scan or Anti-Tunnel Vision test.

#### Guardrails

- Mandatory even on strong models: explicit focus boundary; recoverability of excluded context; anti-fixation check before commitment.
- Conflict/precedence: Source coverage and truth gates override the desire to stay narrowly focused; If the focus target was selected from incomplete evidence, preserve provisional status and run an alternative scan.
- Stop or fail when: Relax or move focus when a credible alternative, uncovered dependency, or counterevidence lies outside the corridor; Stop claiming adequate coverage if excluded material cannot be recovered for checking.

Full package and provenance: [`neuro-focus`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/context-retrieval/neuro-focus/UPGRADEABLE.md).

### R — Drift Suppression

Purpose: Keep execution aligned after distracting context, repeated transformation, or model error.

Activate when: long, branching, or iterative work.

Do not use when: no semantic baseline or allowed corridor exists; creative divergence is the explicit objective.

Requires: none.

#### Runtime mechanism

Compare current plan, state, or artifact against locked task fields, authoritative source anchors, and region-specific corridor tests. Classify each deviation as authorized change, benign variation, or drift; for drift, restore the smallest affected region from the last validated state, reapply the transform under tighter constraints, and record the cause so recurrence can be prevented.

#### Procedure

1. Establish baseline anchors and permitted drift corridors before substantive transformation.
2. Run checks at risk-based checkpoints and after context transitions.
3. Compare objective, entities, claims, quantities, obligations, uncertainty, and required structure.
4. Classify discrepancies using authority and corridor rules.
5. Rollback the smallest affected region, tighten the relevant control, and regenerate or request review.

#### Guardrails

- Mandatory even on strong models: source/task baseline; risk-based checks; minimal rollback.
- Conflict/precedence: Latest authorized task/source state defines the baseline, not the oldest lock by default; When automated checks and cited source inspection disagree, hold the output and resolve the checker or source version.
- Stop or fail when: Stop publication when a high-impact deviation cannot be repaired or adjudicated; Do not claim suppression if no independent baseline survives the transformation.

Full package and provenance: [`drift-suppression`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/drift-control/drift-suppression/UPGRADEABLE.md).

### A — Periodic Whole-Task Consistency Check

Recovered name: Global Coherence Heartbeat

Purpose: Detect long-horizon drift early without rerunning a full review after every step.

Activate when: a workflow is long or multi-stage.

Do not use when: the task completes in one obvious operation; a full coherence loop is already required at the same boundary.

Requires: none.

#### Runtime mechanism

At predefined cadence or meaningful state transitions, compare a compact current-state snapshot against four anchors: objective, hard constraints, accepted decisions, and outstanding obligations. Emit a small delta signal—aligned, warning, or repair-required—and escalate to a full coherence loop only when the pulse detects material divergence.

#### Procedure

1. Capture a compact baseline of objective, constraints, decisions, and open obligations.
2. Choose event-based or interval checkpoints proportional to task length.
3. At each checkpoint, compare current state with every anchor.
4. Classify differences as intended progress, harmless update, or drift.
5. Repair small drift immediately; invoke a coherence loop for systemic mismatch.

#### Guardrails

- Mandatory even on strong models: event-triggered pulse after major state changes in long work.
- Conflict/precedence: Hard constraints and explicit user updates outrank the stored baseline; Do not accept a baseline refresh merely to clear an unresolved warning.
- Stop or fail when: Escalate when a hard constraint, core objective, or accepted decision no longer matches current work.

Full package and provenance: [`coherence-heartbeat`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/validation/coherence-heartbeat/UPGRADEABLE.md).

### C — Cross-Context Relationship Guard

Recovered name: Cross-Context Resonance Lock

Purpose: Preserve an explicitly declared relationship between related contexts without blending their facts, authority, or unresolved assumptions.

Activate when: related contexts must stay aligned across a long task.

Do not use when: the contexts are unrelated; the relationship is speculative or would require merging incompatible authority domains.

Requires: none.

#### Runtime mechanism

Modern operational interpretation: represent each context as a separately identified state with its own source and authority, then store only the declared relationship as a typed link between them. On update or synthesis, refresh the link if both endpoints still support it and reject transfers that copy unverified facts or authority across the boundary.

#### Procedure

1. Identify each context, its source boundary, authority, and current state.
2. State the exact relationship that must remain aligned across contexts.
3. Store a typed link without copying the full contents of either context.
4. Revalidate both endpoints and the relationship when either context changes.
5. During synthesis, transfer only explicitly supported fields and preserve provenance.

#### Guardrails

- Mandatory even on strong models: separate provenance and authority for every linked context.
- Conflict/precedence: Host, system, domain, and explicit user authority take precedence over this component; If the relationship cannot be supported independently in both contexts, stop or escalate rather than forcing a nominal success.
- Stop or fail when: the relationship cannot be supported independently in both contexts; maintaining alignment would require transferring incompatible authority or unverified state.

Full package and provenance: [`cross-context-resonance-lock`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/orchestration/cross-context-resonance-lock/UPGRADEABLE.md).

### A — State Snapshot

Purpose: Create a stable checkpoint that can be resumed or audited after interruption.

Activate when: a workflow pauses, hands off, or persists.

Do not use when: a snapshot would persist prohibited sensitive data; state is invalid or mid-transaction.

Requires: none.

#### Runtime mechanism

At an explicit checkpoint, validate and freeze the canonical state version together with schema version, timestamp, task identity, provenance pointers, unresolved items, and a link to any previous snapshot. Consumers resume by verifying lineage and reconciling newer events; the snapshot itself remains immutable.

#### Procedure

1. Choose a transaction-safe checkpoint.
2. Validate required fields and unresolved-state labels.
3. Serialize the state plus schema/version, time, identity, and provenance pointers.
4. Compute or record an integrity identifier and predecessor link.
5. On resume, verify integrity and reconcile all post-snapshot events before acting.

#### Guardrails

- Mandatory even on strong models: immutable version identity; unresolved items; provenance pointers.
- Conflict/precedence: A newer validated canonical state outranks an older snapshot; If snapshot identity or lineage fails verification, rebuild from authoritative events instead of guessing.
- Stop or fail when: Do not restore when integrity, task identity, or schema compatibility cannot be established; Exclude or redact fields that cannot legally or safely persist.

Full package and provenance: [`state-snapshot`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/state/state-snapshot/UPGRADEABLE.md).

### C — Citation Fidelity Gate

Purpose: Ensure citations prove the precise nearby claim instead of functioning as decorative evidence.

Activate when: output contains citations or source-attributed claims.

Do not use when: the output contains no externally attributed factual claims; the task explicitly requests unsupported fiction.

Requires: none.

#### Runtime mechanism

For every citation-bearing claim, open the exact cited artifact and pass five independent tests: the artifact exists and is the represented edition; the cited passage entails the full claim including qualifiers; quoted text matches exactly; paraphrase retains scope, modality, polarity, and attribution; and evidence belongs to this claim rather than being borrowed from an adjacent citation, nearby sentence, or different source. A failure at any layer blocks the claim, even if the source is authoritative.

#### Procedure

1. Atomize each externally checkable claim and bind each citation to a specific atom.
2. Resolve the cited artifact, version, locator, and authorship.
3. Inspect the cited passage rather than relying on search snippets or secondary descriptions.
4. Test entailment of subject, predicate, scope, date, quantity, and modal strength.
5. For quotes, compare exact words and mark every omission or alteration.

#### Guardrails

- Mandatory even on strong models: direct passage inspection; claim-level entailment; quote exactness.
- Conflict/precedence: The source passage outranks a draft's intended meaning; A precise unsupported subclaim must be removed even when the broader sentence is supported.
- Stop or fail when: Block any material claim whose cited artifact cannot be opened, whose passage does not entail it, or whose quote/paraphrase changes meaning.

Full package and provenance: [`citation-fidelity`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/validation/citation-fidelity/UPGRADEABLE.md).
