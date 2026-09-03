# Long-Context Source Fidelity — Runtime Pack

Purpose: Transform a long or segmented source without losing quotations, identifiers, sequence, or provenance.

Task family: long-document transformation and source-faithful continuation

Activation boundary: Use when a long or segmented source must be transformed without losing sequence, quotations, identifiers, or provenance across context boundaries.

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
| R | `working-memory-lock-in@1.1.0` — Working-Memory Lock-In | critical state competes with large context |
| R | `sequential-memory-state-engine@1.1.0` — Ordered Memory-State Update Engine | state changes across steps or source chunks |
| R | `stateblock@1.1.0` — Canonical Task State | work spans multiple steps or components |
| R | `stable-long-context@1.1.0` — Stable Long-Context | large corpus or long-running workflow |
| R | `zero-drift-zones@1.1.0` — Immutable Content Zones | content contains fidelity-locked atoms |
| R | `drift-suppression@1.1.0` — Drift Suppression | long, branching, or iterative work |
| C | `image-text-fidelity-capture@1.1.0` — Image Text Fidelity Capture | an image contains source text to transcribe |
| A | `reflectos@1.1.0` — Checkpointed Work Reflection | output needs a deliberate quality pass |
| R | `fail-closed-abstention@1.1.0` — Fail-Closed Abstention | required evidence cannot be verified |
| A | `truth-redundancy@1.1.0` — Independent Evidence Redundancy | a consequential claim can be independently checked |
| C | `citation-fidelity@1.1.0` — Citation Fidelity Gate | output contains citations or source-attributed claims |
| A | `state-snapshot@1.1.0` — State Snapshot | a workflow pauses, hands off, or persists |

## Runtime component cards

### R — Working-Memory Lock-In

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

Full package and provenance: [`working-memory-lock-in`](../../upgradeables/state/working-memory-lock-in/UPGRADEABLE.md).

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

Full package and provenance: [`sequential-memory-state-engine`](../../upgradeables/state/sequential-memory-state-engine/UPGRADEABLE.md).

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

Full package and provenance: [`stateblock`](../../upgradeables/state/stateblock/UPGRADEABLE.md).

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

Full package and provenance: [`stable-long-context`](../../upgradeables/state/stable-long-context/UPGRADEABLE.md).

### R — Immutable Content Zones

Recovered name: Zero-Drift Zones

Purpose: Protect facts, identifiers, quotations, obligations, safety limits, and other high-consequence content from transformation drift.

Activate when: content contains fidelity-locked atoms.

Do not use when: the user explicitly authorizes change to the marked content; immutability scope cannot be identified.

Requires: none.

#### Runtime mechanism

Identify minimal semantic atoms whose alteration would invalidate the task, assign stable IDs and source spans, and specify their preservation rule: exact text, exact value/unit, or meaning-equivalent statement with required qualifiers. Carry the IDs through all transforms and require a deterministic check or source-grounded review before acceptance.

#### Procedure

1. Locate high-consequence atoms such as names, numbers, negations, conditions, quotations, obligations, and safety thresholds.
2. Minimize each zone so surrounding exposition can still change.
3. Choose exact-string, structured-value, or semantic-equivalence preservation rules.
4. Attach stable source pointers and propagate the zone contract downstream.
5. Validate every derivative and block or repair failures.

#### Guardrails

- Mandatory even on strong models: minimal immutable atoms; qualifier/unit preservation; source pointers.
- Conflict/precedence: Latest authorized source correction may replace a zone, with version history retained; When exact wording and required target format conflict, preserve the semantic atom and surface the formatting exception for authority review.
- Stop or fail when: Block release when a required zone fails validation; Do not claim semantic equivalence where domain expertise or source context is insufficient.

Full package and provenance: [`zero-drift-zones`](../../upgradeables/drift-control/zero-drift-zones/UPGRADEABLE.md).

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

Full package and provenance: [`drift-suppression`](../../upgradeables/drift-control/drift-suppression/UPGRADEABLE.md).

### C — Image Text Fidelity Capture

Purpose: Create a source-faithful textual representation of image-borne evidence for downstream indexing, analysis, or copying.

Activate when: an image contains source text to transcribe.

Do not use when: no image contains source text or visible structure; the task asks for visual interpretation rather than faithful capture and that different mode is not declared.

Requires: none.

#### Runtime mechanism

Traverse the image in a declared order, transcribe only visible characters, and reconstruct headings, rows, columns, or spatial groups only where visible evidence supports them. Unreadable regions receive explicit illegible/uncertain markers linked to their location; context is never used to silently complete missing text.

#### Procedure

1. Record the image/page identifier and reading order.
2. Segment visible text and structural regions.
3. Transcribe characters exactly, preserving capitalization, numbers, and punctuation where legible.
4. Represent visible layout without inferring hidden cells or labels.
5. Mark obscured or ambiguous regions with location-specific uncertainty.

#### Guardrails

- Mandatory even on strong models: only visible evidence may determine captured text or structure.
- Conflict/precedence: Visible evidence outranks grammatical completion; If layout and lexical readings conflict, preserve both uncertainty and coordinates rather than choosing silently.
- Stop or fail when: If a region is not legible enough to verify, mark it uncertain and do not produce a confident transcription for that region.

Full package and provenance: [`image-text-fidelity-capture`](../../upgradeables/truth-grounding/image-text-fidelity-capture/UPGRADEABLE.md).

### A — Checkpointed Work Reflection

Recovered name: Work Reflection Loop OS / ReflectOS

Purpose: Correct process and output errors at meaningful checkpoints without turning reflection into unbounded rumination or invented content.

Activate when: output needs a deliberate quality pass.

Do not use when: a deterministic fix is already known and reflection adds no decision value; the caller asks for unconstrained ideation rather than requirement checking.

Requires: none.

#### Runtime mechanism

At a bounded checkpoint, re-read the session goal and current subgoal, compare the actual output to explicit requirements, audit contradictions, omissions, and risk, then select exactly one transition: accept, revise, or ask/escalate where permitted. After the transition, update the StateBlock to reflect task reality; reflection may correct process errors but may not invent facts or construct an identity narrative.

#### Procedure

1. Recheck the session goal and current subgoal.
2. Compare the produced artifact or action with every explicit requirement.
3. Audit contradictions, missing requirements, failed evidence, and material risk.
4. Choose accept, revise, or ask/escalate when permitted.
5. If revising, make the smallest requirement-linked correction and retest.

#### Guardrails

- Mandatory even on strong models: goal comparison, requirement audit, explicit transition, and state update for long or risky work.
- Conflict/precedence: Explicit requirements and evidence outrank the reflector's preference; When a missing fact cannot be recovered, escalate or qualify rather than fabricate.
- Stop or fail when: Do not accept when a material requirement is unmet; do not revise with invented facts; stop and surface the dependency when progress requires external authority.

Full package and provenance: [`reflectos`](../../upgradeables/validation/reflectos/UPGRADEABLE.md).

### R — Fail-Closed Abstention

Purpose: Ensure that missing essential support produces an explicit bounded result rather than fabricated closure.

Activate when: required evidence cannot be verified.

Do not use when: the failed condition is optional and does not affect the supported deliverable; a harmless creative task has no factual commitment gate.

Requires: none.

#### Runtime mechanism

Consume explicit validator outcomes and distinguish essential from optional failures. If an essential condition is failed or unverifiable, block the affected conclusion, preserve any independently supported subset, and state the unresolved dependency; never synthesize a missing fact merely to obtain a pass.

#### Procedure

1. List the conditions required to commit the conclusion.
2. Read each condition's pass, fail, or unverifiable result.
3. Determine which failures invalidate only one claim and which invalidate the whole conclusion.
4. Remove or narrow invalidated claims while preserving independently supported content.
5. Return the supported subset plus the unresolved dependency or an explicit abstention.

#### Guardrails

- Mandatory even on strong models: no essential failed gate may be bypassed by fluency or confidence.
- Conflict/precedence: A request for a definitive answer cannot override a failed required truth gate; Preserve supported content unless higher authority requires withholding the entire output.
- Stop or fail when: A conclusion cannot be committed while any indispensable evidence or integrity condition remains failed or unverifiable.

Full package and provenance: [`fail-closed-abstention`](../../upgradeables/truth-grounding/fail-closed-abstention/UPGRADEABLE.md).

### A — Independent Evidence Redundancy

Recovered name: Truth Redundancy

Purpose: Reduce single-point truth failure before high-impact synthesis or decision-making.

Activate when: a consequential claim can be independently checked.

Do not use when: the claim is low risk and an authoritative primary source is decisive; a second anchor would merely repeat the first source.

Requires: none.

#### Runtime mechanism

For a selected truth atom, establish two evidence or validation anchors whose failure modes are meaningfully independent. Record provenance and the proposition each anchor supports; the pair is then passed to a gate or resolver rather than treated as automatic proof.

#### Procedure

1. Identify the consequential truth atom.
2. Select the primary anchor and record its failure mode.
3. Select a second anchor with a distinct source or validation path.
4. Verify that the second does not merely derive from the first.
5. Record each anchor's supported scope and hand the pair to Multi-Truth Gating.

#### Guardrails

- Mandatory even on strong models: when redundancy is claimed, the anchors must be genuinely independent.
- Conflict/precedence: Independence is invalid if both anchors share the same unverified upstream source; A safety veto still controls even when two non-safety anchors agree.
- Stop or fail when: If no genuinely independent second anchor is available, report that limitation and do not claim redundant verification.

Full package and provenance: [`truth-redundancy`](../../upgradeables/truth-grounding/truth-redundancy/UPGRADEABLE.md).

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

Full package and provenance: [`citation-fidelity`](../../upgradeables/validation/citation-fidelity/UPGRADEABLE.md).

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

Full package and provenance: [`state-snapshot`](../../upgradeables/state/state-snapshot/UPGRADEABLE.md).
