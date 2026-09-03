# Multi-Agent / Orchestration — Runtime Pack

Purpose: Coordinate distinct workers through scoped tasks, explicit state handoffs, and result collection.

Task family: multi-worker delegation, handoffs, and synthesis

Activation boundary: Use only when the host can run or coordinate distinct workers and the task needs explicit routing, state exchange, and result collection.

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
| R | `architect-orchestrator@1.1.0` — Modular System Design Orchestrator | designing or refactoring a Skill, OS, framework, or workflow |
| R | `scoped-loader@1.1.0` — Scoped Loader / Loader Sequencing | a modular workflow has multiple available components |
| R | `state-routing-bus@1.1.0` — Task-State Handoff Router | multiple components must exchange typed state |
| R | `stateblock@1.1.0` — Canonical Task State | work spans multiple steps or components |
| R | `state-snapshot@1.1.0` — State Snapshot | a workflow pauses, hands off, or persists |
| R | `domain-mode-isolation@1.1.0` — Domain / Mode Isolation | multiple domains or semantic modes coexist |
| A | `resonance@1.1.0` — Cross-Module Coordination | several active modules must align |
| A | `parallel-qms@1.1.0` — Parallel Validation System | a composed workflow needs structured quality evaluation |
| A | `multi-layer-consistency@1.1.0` — Multi-Layer Consistency | multiple authority layers are composed |
| C | `external-state-automation@1.1.0` — External State Automation | continuation requires real external state |

## Runtime component cards

### R — Modular System Design Orchestrator

Recovered name: Architect Orchestrator

Purpose: Plan and coordinate modular system design from goal discovery through critique, localized repair, synthesis, and continuation state.

Activate when: designing or refactoring a Skill, OS, framework, or workflow.

Do not use when: the task is a narrow domain execution job with no architecture decision; a single existing component already performs the complete bounded task.

Requires: none.

#### Runtime mechanism

Translate the locked goal and constraints into a modular plan, select only the necessary OS layers, Genes, Cores, Upgradeables, references, and validators, then coordinate their ordered execution. After execution, run a separate critique, route localized defects to bounded repair, synthesize one result, and emit the minimum continuation state. The orchestrator owns coordination, not every domain operation.

#### Procedure

1. Lock the goal, constraints, deliverable, authority, and completion criteria.
2. Decompose the architecture into modules with explicit interfaces and dependencies.
3. Select the minimum required components and resolve authority, conflict, and load order.
4. Coordinate execution or delegation while passing only explicit bounded state.
5. Critique the assembled result, apply localized repair, synthesize, and emit a compact state snapshot.

#### Guardrails

- Mandatory even on strong models: explicit modular interfaces, authority resolution, independent critique, and continuation state.
- Conflict/precedence: Host, system, domain, and explicit user authority take precedence over this component; If required module interfaces or authority relationships cannot be resolved, stop or escalate rather than forcing a nominal success.
- Stop or fail when: required module interfaces or authority relationships cannot be resolved; the requested work is domain execution outside the orchestrator's design scope.

Full package and provenance: [`architect-orchestrator`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/orchestration/architect-orchestrator/UPGRADEABLE.md).

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

Full package and provenance: [`scoped-loader`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/context-retrieval/scoped-loader/UPGRADEABLE.md).

### R — Task-State Handoff Router

Recovered name: State Routing Bus

Purpose: Pass explicit task state, decisions, evidence pointers, and module outputs through real host-supported handoffs.

Activate when: multiple components must exchange typed state.

Do not use when: all work occurs inside one uninterrupted component; the host provides no real file, message, context, or structured-state handoff.

Requires: none.

#### Runtime mechanism

Represent the handoff as a typed envelope containing sender, receiver, schema version, authority, provenance, payload, and unresolved status. Validate the envelope and receiver permissions, transmit it through an actual host mechanism such as context, file, message, or database, then require acknowledgement. No latent pointer or hidden channel is assumed.

#### Procedure

1. Define the sender, receiver, state schema, and permitted payload fields.
2. Package decisions, evidence pointers, module outputs, provenance, and unresolved items in a bounded envelope.
3. Validate schema, authority, size, and receiver permissions.
4. Transmit through an available explicit host channel and record delivery status.
5. Require acknowledgement or fail with a recoverable handoff record.

#### Guardrails

- Mandatory even on strong models: explicit payload, provenance, receiver boundary, and delivery status.
- Conflict/precedence: Host, system, domain, and explicit user authority take precedence over this component; If no real host-supported handoff channel exists, stop or escalate rather than forcing a nominal success.
- Stop or fail when: no real host-supported handoff channel exists; payload schema, authority, provenance, or receiver acknowledgement fails.

Full package and provenance: [`state-routing-bus`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/orchestration/state-routing-bus/UPGRADEABLE.md).

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

### R — State Snapshot

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

### R — Domain / Mode Isolation

Purpose: Prevent cross-domain contamination while permitting explicit, reviewed transfers of shared facts.

Activate when: multiple domains or semantic modes coexist.

Do not use when: the task is genuinely single-domain; the supposed domains share identical authority and semantics.

Requires: none.

#### Runtime mechanism

Create a named compartment for each active domain with its own instructions, terms, sources, permissions, and state. Route new material into the matching compartment; make cross-domain transfer an explicit projection with provenance, and validate the final output against the selected domain rather than the union of all modes.

#### Procedure

1. Classify the task and enumerate domains that are actually needed.
2. Create separate domain scopes for instructions, sources, vocabulary, and mutable state.
3. Load only the selected scope into each domain operation.
4. Transfer shared facts through an explicit provenance-bearing bridge.
5. On transition, unload or deactivate the old domain scope and validate for leakage.

#### Guardrails

- Mandatory even on strong models: active-domain marker; authority separation; explicit transfer boundary.
- Conflict/precedence: System and task authority outrank domain-local preferences; When a fact must cross domains, transfer the fact and provenance, not the source domain's behavioral rules.
- Stop or fail when: Pause when the domain is ambiguous and different classifications change safety or authority; Do not claim isolation if the host cannot control context or tool exposure; emulate with explicit labels and validation.

Full package and provenance: [`domain-mode-isolation`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/state/domain-mode-isolation/UPGRADEABLE.md).

### A — Cross-Module Coordination

Recovered name: Resonance

Purpose: Coordinate active modules that should reinforce one another while suppressing irrelevant effects and preserving authority boundaries.

Activate when: several active modules must align.

Do not use when: only one module is active; the proposed reinforcement would amplify repetition, exaggeration, or an authority conflict.

Requires: none.

#### Runtime mechanism

Identify the specific outputs or constraints through which selected modules should reinforce one another, declare the direction and limit of that coupling, and suppress unrelated effects. Check hierarchy before amplification so a lower-authority module cannot become stronger through repetition. Amplification means clearer coordination and usable handoff, not duplicated content.

#### Procedure

1. List active modules and the exact relationship that should be reinforced.
2. Verify their authority, source, and state boundaries are compatible.
3. Define the bounded handoff or mutual constraint that creates the useful coupling.
4. Suppress duplicate, irrelevant, or conflicting module effects.
5. Check the coordinated result and dissolve the coupling when its trigger ends.

#### Guardrails

- Mandatory even on strong models: explicit relationship, bounded effect, noise suppression, and authority preservation.
- Conflict/precedence: Host, system, domain, and explicit user authority take precedence over this component; If the modules have incompatible authority or source boundaries, stop or escalate rather than forcing a nominal success.
- Stop or fail when: the modules have incompatible authority or source boundaries; the coupling produces repetition or exaggeration instead of clearer coordination.

Full package and provenance: [`resonance`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/orchestration/resonance/UPGRADEABLE.md).

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

Full package and provenance: [`parallel-qms`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/validation/parallel-qms/UPGRADEABLE.md).

### A — Multi-Layer Consistency

Purpose: Maintain vertical consistency from local facts and operations to the overall conclusion or system behavior.

Activate when: multiple authority layers are composed.

Do not use when: the artifact has only one meaningful level; levels are intentionally alternative rather than nested.

Requires: none.

#### Runtime mechanism

Define nested levels and invariants linking them, then validate both upward and downward: atoms must support their containing unit, units must compose into section or subsystem claims, and the global result must not assert anything contradicted below; conversely global constraints must be realized in the relevant lower layers. A pass requires agreement across boundaries, not independent passes at each level.

#### Procedure

1. Map the artifact into atom, local unit, intermediate group, and global levels.
2. State invariants and claimed summaries at each boundary.
3. Check upward support from atoms to local and global claims.
4. Check downward realization of global constraints in lower levels.
5. Locate contradictions, orphan claims, and locally valid but globally incompatible parts.

#### Guardrails

- Mandatory even on strong models: at least one upward and one downward boundary check in hierarchical work.
- Conflict/precedence: A lower-level verified contradiction defeats an unsupported global summary; An explicit global hard constraint requires lower-layer implementation or a documented exception.
- Stop or fail when: Do not certify when a global claim lacks lower-layer support or a lower-layer fact violates an undeclared global exception.

Full package and provenance: [`multi-layer-consistency`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/validation/multi-layer-consistency/UPGRADEABLE.md).

### C — External State Automation

Purpose: Serialize and restore important task state through real files, memory stores, databases, or project documents when the host supports persistence.

Activate when: continuation requires real external state.

Do not use when: the task ends in one session and needs no continuation; the host exposes no authorized persistent storage.

Requires: none.

#### Runtime mechanism

Declare the actual storage capability and a versioned state schema, serialize only the minimum continuation fields with provenance and timestamp, write through an authorized host operation, and verify the write. On restoration, validate version and integrity before merging; never treat a requested or imagined write as persisted state.

#### Procedure

1. Confirm an authorized storage mechanism, location, lifetime, and data policy.
2. Select the minimum state fields needed for continuation and serialize them with schema and provenance.
3. Write through the real host capability and verify the stored representation.
4. On resume, read and validate schema, integrity, freshness, and authority.
5. Reconcile restored state with current instructions and report any failed or stale persistence.

#### Guardrails

- Mandatory even on strong models: capability declaration, minimum-state serialization, write verification, and restore validation.
- Conflict/precedence: Host, system, domain, and explicit user authority take precedence over this component; If no authorized storage capability is available, stop or escalate rather than forcing a nominal success.
- Stop or fail when: no authorized storage capability is available; write verification, schema validation, integrity, freshness, or restoration reconciliation fails.

Full package and provenance: [`external-state-automation`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/persistence/external-state-automation/UPGRADEABLE.md).
