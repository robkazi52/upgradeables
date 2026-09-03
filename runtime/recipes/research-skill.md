# Research Skill — Runtime Pack

Purpose: Research a question across multiple sources and produce a bounded, cited synthesis.

Task family: multi-source research and evidence synthesis

Activation boundary: Use when a deliverable must synthesize multiple accessible sources and corpus size or ambiguity makes scoped loading, shared state, and claim-level grounding necessary.

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
| R | `task-set-lock-in@1.1.0` — Task-Set Lock-In | multi-step work begins or scope changes |
| R | `scoped-loader@1.1.0` — Scoped Loader / Loader Sequencing | a modular workflow has multiple available components |
| R | `stateblock@1.1.0` — Canonical Task State | work spans multiple steps or components |
| R | `grounding-no-invention@1.1.0` — Grounding / No-Invention | work relies on documents, data, external facts, or consequential claims |
| A | `activation-budget-funnel@1.1.0` — Progressive Context Intake | many sources or modules compete for attention |
| A | `neuro-focus@1.1.0` — Bounded Attention Focus | large sources or a narrow debug region demand concentration |
| A | `stable-long-context@1.1.0` — Stable Long-Context | large corpus or long-running workflow |
| A | `sequential-memory-state-engine@1.1.0` — Ordered Memory-State Update Engine | state changes across steps or source chunks |
| A | `multi-truth-gating@1.1.0` — Independent Evidence Gate | an important conclusion rests on fragile evidence |
| A | `citation-fidelity@1.1.0` — Citation Fidelity Gate | output contains citations or source-attributed claims |
| A | `truth-priority-hierarchy@1.1.0` — Truth Priority Hierarchy | evidence classes or authorities conflict |
| C | `critical-atomic-verification@1.1.0` — Critical Fact Verification | small factual errors could change the outcome |
| A | `parallel-qms@1.1.0` — Parallel Validation System | a composed workflow needs structured quality evaluation |
| O | `anti-tunnel-vision@1.1.0` — Anti-Tunnel Vision | premature fixation could hide credible alternatives |
| C | `state-snapshot@1.1.0` — State Snapshot | a workflow pauses, hands off, or persists |

## Runtime component cards

### R — Task-Set Lock-In

Purpose: Prevent scope substitution and goal drift during execution.

Activate when: multi-step work begins or scope changes.

Do not use when: the task is still materially ambiguous; open-ended ideation intentionally has no fixed deliverable.

Requires: none.

#### Runtime mechanism

Convert the clarified request into a compact task-set contract: primary objective, required outputs, quality gates, constraints, non-goals, dependencies, and change authority. Check each planned action and final artifact against it; update only through an explicit, versioned scope-change decision.

#### Procedure

1. Extract the objective, required artifacts, constraints, success tests, and exclusions.
2. Resolve material ambiguity before locking.
3. Record the task set as locked fields with a version and change authority.
4. Gate planned actions and newly proposed work against the set.
5. For legitimate changes, record the requester, rationale, and new version.

#### Guardrails

- Mandatory even on strong models: objective; required deliverables; constraints and non-goals.
- Conflict/precedence: System and latest explicit authorized user scope changes override older task-set versions; When a new request conflicts with locked acceptance criteria, pause for a scope-change decision.
- Stop or fail when: Do not claim completion when a required artifact or quality gate lacks evidence; Unlock and clarify when task identity changes materially.

Full package and provenance: [`task-set-lock-in`](../../upgradeables/state/task-set-lock-in/UPGRADEABLE.md).

### R — Scoped Loader / Loader Sequencing

Purpose: Keep modular OS or Skill execution relevant, ordered, and within context limits instead of loading the full library at session start.

Activate when: a modular workflow has multiple available components.

Do not use when: the workflow has one small fixed instruction set; selection criteria are unavailable.

Requires: none.

#### Runtime mechanism

Resolve the active task first, then load in recovered authority/function order: task shell, applicable Behavior Gene, authorized Core, only triggered Upgradeables, references or resources on demand, and validators before commitment. Record what was loaded and why; leave unrelated modules inactive so their rules and context cannot leak into the task.

#### Procedure

1. Classify the task, domain, mode, risk, and output contract.
2. Load the task shell and its authority constraints.
3. Load at most the required Behavior Gene and authorized Core/reference layer.
4. Evaluate Upgradeable triggers and dependencies, then activate only the minimal matching set.
5. Fetch deep references, resources, or tools only when a retained component needs them.

#### Guardrails

- Mandatory even on strong models: task-first selection; authority-ordered loading; inactive-by-default treatment of unrelated modules.
- Conflict/precedence: Host/system and task authority determine eligibility; relevance alone cannot authorize a module; If two loaders disagree, prefer the route tied to the locked task and explicit manifests, or escalate rather than merging all candidates.
- Stop or fail when: Do not load a component when its trigger, authority, dependency, or host capability cannot be established; Escalate when required components conflict and precedence cannot resolve them.

Full package and provenance: [`scoped-loader`](../../upgradeables/context-retrieval/scoped-loader/UPGRADEABLE.md).

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

### R — Grounding / No-Invention

Purpose: Prevent fabricated facts, citations, measurements, policies, records, and gap-filling in source-grounded work.

Activate when: work relies on documents, data, external facts, or consequential claims.

Do not use when: pure creative generation has no asserted factual source boundary; the task explicitly asks for labeled brainstorming rather than factual claims.

Requires: none.

#### Runtime mechanism

Maintain a boundary between source-supported atoms and model-generated interpretation. Each material factual claim must resolve to supplied data or verified external evidence; missing fields remain missing, and permissible inference is labeled instead of being written back as source fact.

#### Procedure

1. Declare the allowed evidence boundary.
2. Extract material source-supported facts without filling absent fields.
3. Separate facts from interpretations and hypotheses.
4. For each candidate factual claim, locate supporting evidence inside the boundary.
5. Label, narrow, omit, or fail closed on unsupported claims.

#### Guardrails

- Mandatory even on strong models: every asserted material fact must remain within the authorized evidence boundary.
- Conflict/precedence: Verified evidence outranks fluent completion and stylistic requests; An explicit hypothetical mode may generate possibilities, but they remain outside factual state.
- Stop or fail when: When an essential material claim lacks support inside the authorized evidence boundary, omit it or fail closed.

Full package and provenance: [`grounding-no-invention`](../../upgradeables/truth-grounding/grounding-no-invention/UPGRADEABLE.md).

### A — Progressive Context Intake

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

Full package and provenance: [`activation-budget-funnel`](../../upgradeables/context-retrieval/activation-budget-funnel/UPGRADEABLE.md).

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

Full package and provenance: [`neuro-focus`](../../upgradeables/context-retrieval/neuro-focus/UPGRADEABLE.md).

### A — Stable Long-Context

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

### A — Ordered Memory-State Update Engine

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

### A — Independent Evidence Gate

Recovered name: Multi-Truth Gating

Purpose: Reduce dependence on one fragile source, inference chain, or evaluator before a consequential conclusion is committed.

Activate when: an important conclusion rests on fragile evidence.

Do not use when: the claim is low consequence and one authoritative direct source is sufficient; the supposed anchors merely duplicate the same underlying source.

Requires: none.

#### Runtime mechanism

For each decision-critical conclusion, identify a primary factual anchor and at least one genuinely independent corroborating anchor or verification path. Compare what each supports; convergence permits commitment, while material divergence triggers re-evaluation, a narrower claim, explicit uncertainty, or abstention.

#### Procedure

1. Identify conclusions whose failure would materially change the outcome.
2. Record the primary evidence or reasoning anchor for each.
3. Select an independent corroborating source or validation path.
4. Check independence and compare the supported propositions.
5. Resolve differences by evidence and authority rules rather than averaging.

#### Guardrails

- Mandatory even on strong models: decision-critical claims require genuinely independent support or an explicit unresolved status.
- Conflict/precedence: A higher-authority direct source can outweigh a weaker corroborating path, but the disagreement must be recorded; Safety vetoes are not overridable by numerical agreement among other checks.
- Stop or fail when: If an important conclusion lacks an independent check or the anchors materially disagree without resolution, do not certify the conclusion.

Full package and provenance: [`multi-truth-gating`](../../upgradeables/truth-grounding/multi-truth-gating/UPGRADEABLE.md).

### A — Citation Fidelity Gate

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

### A — Truth Priority Hierarchy

Purpose: Resolve conflicting signals without letting fluency, optimization, or an undifferentiated vote override stronger evidence or safety authority.

Activate when: evidence classes or authorities conflict.

Do not use when: no material evidence or authority conflict exists; the domain lacks an authorized hierarchy and inventing one would decide the outcome.

Requires: none.

#### Runtime mechanism

Before resolving a conflict, declare a domain-appropriate ordering such as host safety over task optimization, direct source fact over inference, and verified evidence over stylistic fluency. Map each conflicting claim to its evidence and authority class, apply the ordering, and preserve unresolved ties rather than silently choosing.

#### Procedure

1. Identify the conflicting propositions or validator outcomes.
2. Record the source, authority, epistemic status, and domain applicability of each.
3. Load or declare the authorized domain hierarchy.
4. Apply the hierarchy and any hard vetoes.
5. Document the winning, narrowed, or unresolved result.

#### Guardrails

- Mandatory even on strong models: evidence and authority, not fluency or optimization, determine conflict resolution.
- Conflict/precedence: Host/system safety and organization policy remain above repository-level truth ordering; If no authorized rule distinguishes materially conflicting claims, return unresolved rather than fabricate priority.
- Stop or fail when: If a material conflict has no defensible domain/authority ordering, the resolver must not select a winner.

Full package and provenance: [`truth-priority-hierarchy`](../../upgradeables/truth-grounding/truth-priority-hierarchy/UPGRADEABLE.md).

### C — Critical Fact Verification

Recovered name: Critical Atomic Verification

Purpose: Concentrate verification on the smallest facts whose failure would invalidate the output.

Activate when: small factual errors could change the outcome.

Do not use when: no factual conclusion or consequential action depends on the output; the content is purely expressive.

Requires: none.

#### Runtime mechanism

Build a dependency graph from the intended conclusion back to minimal truth-bearing atoms. Mark an atom critical when its falsity, reversal, or absence would change the conclusion or safe action. Verify every critical atom directly at depth proportional to risk; propagate any failed or unknown atom forward so the dependent conclusion is repaired, qualified, or blocked.

#### Procedure

1. State the conclusion or action being certified.
2. Decompose it into atomic claims and dependencies.
3. Use a removal or reversal test to mark critical atoms.
4. Assign verification depth and evidence requirements by consequence.
5. Verify each critical atom independently and record true, false, unknown, or conflicting.

#### Guardrails

- Mandatory even on strong models: criticality test; atom-wise evidence status; uncertainty propagation.
- Conflict/precedence: A false critical atom vetoes any dependent conclusion; An unknown critical atom requires qualification or abstention, not a guessed value.
- Stop or fail when: Do not certify a conclusion while any indispensable atom is false, materially conflicting, or unsupported beyond the allowed risk threshold.

Full package and provenance: [`critical-atomic-verification`](../../upgradeables/validation/critical-atomic-verification/UPGRADEABLE.md).

### A — Parallel Validation System

Recovered name: Parallel Quality Management System

Purpose: Match validation topology to failure risk instead of treating QMS as one generic critic or a majority vote.

Activate when: a composed workflow needs structured quality evaluation.

Do not use when: one low-risk deterministic check is sufficient; the caller cannot define a decision criterion or bounded exit.

Requires: none.

#### Runtime mechanism

Select modes by distinct failure hypotheses, run them with separated evidence where independence matters, preserve typed outputs, and collapse only after resolving material disagreement and honoring vetoes. Mirror QMS compares two independently derived answers; Risk-Tier-Split allocates shallow, medium, or deep checks by consequence; Cross-Phase separately inspects factual, evaluative, framing, and hypothetical phases; Redundancy QMS seeks logical, structural, narrative, and safety corroboration; ExIt-Integrated couples scores to bounded repair and convergence; Hierarchical validates atom, paragraph/component, section/subsystem, and global levels; Transversal cuts across temporal, causal, modal, and logical dimensions; Heterogeneous assigns coherence, evidence, relevance, and safety to different validator lenses; Monte QMS perturbs assumptions, wording, or structure without claiming…

#### Procedure

1. State the decision, critical truths, risk tier, and stop conditions.
2. Choose only modes tied to plausible distinct failures: QMS-M for independent-answer agreement; QMS-RTS for consequence-scaled depth; QMS-XP for factual/evaluative/framing/hypothetical separation; QMS-R for logical/structural/narrative/safety redundancy; QMS-EI for bounded repair convergence; HQMS for atom-to-global hierarchy; T-QMS for temporal/causal/modal/logical cuts; hQMS for…
3. Define inputs, independence boundaries, and typed pass/fail output for each selected mode.
4. Run independent modes without sharing draft conclusions when contamination would defeat the purpose.
5. Collect disagreements without averaging them away.

#### Guardrails

- Mandatory even on strong models: mode distinction; critical-truth agreement; conflict preservation.
- Conflict/precedence: Crucial factual conflict must be resolved or surfaced before collapse; Safety and ethical vetoes cannot be outvoted.
- Stop or fail when: Do not certify while a crucial truth is disputed, a safety/ethical veto is active, validator independence is falsely claimed, or bounded repair fails to converge.

Full package and provenance: [`parallel-qms`](../../upgradeables/validation/parallel-qms/UPGRADEABLE.md).

### O — Anti-Tunnel Vision

Purpose: Preserve enough search breadth to expose premature fixation, then collapse quickly when evidence discriminates.

Activate when: premature fixation could hide credible alternatives.

Do not use when: the answer is directly established by a locked source; a safety or policy veto already determines the outcome.

Requires: none.

#### Runtime mechanism

Name the leading path and at least one genuinely plausible competitor, specify the observation that would distinguish them, and compare only on that discriminating evidence. The controller is bounded: it prevents first-path lock-in without turning every task into open-ended brainstorming.

#### Procedure

1. State the current favored hypothesis or plan and the evidence supporting it.
2. Generate one or two materially different competitors, not cosmetic restatements.
3. For each candidate, identify its strongest confirming signal and strongest disconfirming signal.
4. Acquire or inspect the cheapest decisive evidence available.
5. Select, synthesize, or explicitly preserve uncertainty; retire alternatives that lose on the discriminating evidence.

#### Guardrails

- Mandatory even on strong models: explicitly test at least one plausible rival before a costly commitment; retain the stop rule.
- Conflict/precedence: If a hard veto eliminates a branch, do not keep it alive for balance; When evidence cannot discriminate within budget, report unresolved alternatives instead of manufacturing certainty.
- Stop or fail when: unbounded ideation; token alternatives with no material difference.

Full package and provenance: [`anti-tunnel-vision`](../../upgradeables/reasoning/anti-tunnel-vision/UPGRADEABLE.md).

### C — State Snapshot

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
