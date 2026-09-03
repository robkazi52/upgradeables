# Architecture / Skill Building — Runtime Pack

Purpose: Design a portable multi-component Skill with explicit interfaces, authority, host assumptions, and tests.

Task family: Skill, agent, prompt-system, and workflow architecture

Activation boundary: Use when designing or restructuring a portable multi-component Skill whose interfaces, authority order, and host assumptions must be explicit.

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
| A | `power-mode@1.1.0` — Deep Exploration Mode | architecture or design benefits from broad exploration |
| A | `hybrid-mode@1.1.0` — Explore-Then-Commit Mode | work includes both broad design and grounded execution |
| A | `reasoning-scale-controller@1.1.0` — Task-Scope Reasoning Controller | task complexity or risk requires depth selection |
| A | `multiverse-reasoning@1.1.0` — Bounded Alternative Search | competing hypotheses or designs would add value |
| C | `behavior-gene-builder@1.1.0` — Reusable Behavior Component Builder | a recurring task family needs reusable behavior |
| C | `domain-core-builder@1.1.0` — Shared Domain Knowledge Component Builder | a recurring domain needs structured knowledge and decision logic |
| R | `scoped-loader@1.1.0` — Scoped Loader / Loader Sequencing | a modular workflow has multiple available components |
| R | `stateblock@1.1.0` — Canonical Task State | work spans multiple steps or components |
| R | `parallel-qms@1.1.0` — Parallel Validation System | a composed workflow needs structured quality evaluation |
| A | `meta-supervisor@1.1.0` — Workflow Repair Supervisor | complex scaffolding itself needs supervision |
| A | `adapter-first-experimentation@1.1.0` — Adapter-First Experimentation | a new capability may destabilize a base workflow |
| A | `crispr-edit@1.1.0` — Precision Local System Edit | a change is small and local |
| C | `surgery-edit@1.1.0` — Structural System Edit | layers, Cores, or workflows require major replacement |
| A | `dynamic-depth-allocation@1.1.0` — Per-Region Reasoning Depth | task regions vary in difficulty or risk |
| A | `anti-tunnel-vision@1.1.0` — Anti-Tunnel Vision | premature fixation could hide credible alternatives |
| A | `state-snapshot@1.1.0` — State Snapshot | a workflow pauses, hands off, or persists |
| A | `future-proof-mode-selector@1.1.0` — Runtime Compatibility Mode Selector | an implementation targets models with different capabilities |

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

Full package and provenance: [`architect-orchestrator`](../../upgradeables/orchestration/architect-orchestrator/UPGRADEABLE.md).

### A — Deep Exploration Mode

Recovered name: POWER Mode

Purpose: Increase solution search and architectural depth before commitment when the problem is genuinely ambiguous or system-wide.

Activate when: architecture or design benefits from broad exploration.

Do not use when: the task is a precise grounded execution step; a hard constraint leaves only one valid action.

Requires: none.

#### Runtime mechanism

Declare a bounded exploration budget, open two or three materially distinct plans under identical goals and constraints, reason at system or Cosmic scale only where dependencies justify it, and evaluate all candidates with QMS before collapse. POWER produces a selected design and uncertainty map; it does not authorize consequential execution without an explicit transition to SAFE or another execution profile.

#### Procedure

1. Declare POWER, the design question, non-negotiable constraints, and exploration budget.
2. Generate two or three materially distinct plans or architectures.
3. Develop system dependencies, long-horizon effects, reversibility, and risks for each to equal decision depth.
4. Evaluate candidates using a common QMS rubric and hard vetoes.
5. Select or compatibly synthesize one design and retire losing assumptions.

#### Guardrails

- Mandatory even on strong models: bounded alternatives; common QMS; collapse.
- Conflict/precedence: Hard constraints and vetoes apply equally in broad exploration; No branch may mutate consequential external state before collapse and execution authorization.
- Stop or fail when: unbounded ideation; architecture theater.

Full package and provenance: [`power-mode`](../../upgradeables/meta-control/power-mode/UPGRADEABLE.md).

### A — Explore-Then-Commit Mode

Recovered name: HYBRID Mode

Purpose: Combine broad planning capability with conservative implementation without letting speculative branch assumptions leak into committed work.

Activate when: work includes both broad design and grounded execution.

Do not use when: the task needs only narrow execution; the task is pure open exploration with no commitment.

Requires: none.

#### Runtime mechanism

Run POWER only to generate and compare bounded plans, then collapse to one plan and construct a handoff containing locked goals, selected decisions, rejected assumptions, evidence needs, risks, and execution invariants. A supervisor validates the handoff before activating SAFE, which executes only the committed plan with narrow drift and atomic checks. Re-enter POWER only through a checkpoint when execution exposes an architecture-level defect.

#### Procedure

1. Declare HYBRID and define separate planning and execution completion criteria.
2. Use POWER to generate, evaluate, and collapse candidate plans.
3. Create a transition state with the selected plan, locked constraints, evidence, risks, unresolved items, and retired branches.
4. Have the supervisor verify that the plan is executable and no speculative assumptions remain active.
5. Switch explicitly to SAFE and execute with grounding, narrow drift, and atomic validation.

#### Guardrails

- Mandatory even on strong models: explicit collapse; handoff state; supervisor gate.
- Conflict/precedence: No POWER branch may execute until one plan passes collapse and handoff validation; SAFE findings can reopen design only through a recorded checkpoint.
- Stop or fail when: mode leakage; uncollapsed execution.

Full package and provenance: [`hybrid-mode`](../../upgradeables/meta-control/hybrid-mode/UPGRADEABLE.md).

### A — Task-Scope Reasoning Controller

Recovered name: Reasoning-Scale Controller

Purpose: Match reasoning depth and scope to the unit of work instead of applying either shallow local analysis or system-wide architecture indiscriminately.

Activate when: task complexity or risk requires depth selection.

Do not use when: a governing workflow already fixes the required scale; the unit is safety-critical and policy mandates the highest review tier.

Requires: none.

#### Runtime mechanism

Route work through one controller: Subatomic for a fact, local relation, constraint, or sentence decision; Atomic for a small verified inference or action; Nano as a light intermediate structure whose detailed historical spec remains unrecovered; Micro for task-local scaffolds and dependencies; QMS for quality evaluation; Cosmic for global architecture, strategy, or long-horizon planning. Escalate when dependency span, ambiguity, irreversibility, or risk exceeds the current scale; de-escalate after the larger question is resolved.

#### Procedure

1. Identify the unit of work, dependency radius, uncertainty, and consequence of error.
2. Choose the lowest scale that can represent all relevant dependencies.
3. Execute only the operations appropriate to that scale.
4. Escalate one or more levels when local reasoning exposes unresolved cross-unit dependencies, competing quality dimensions, or global architecture effects.
5. After the higher-scale decision, return local implementation to the smallest adequate scale and record the boundary.

#### Guardrails

- Mandatory even on strong models: smallest-adequate-scope selection; explicit escalation signals; global-to-local decomposition.
- Conflict/precedence: Risk-mandated review overrides the desire to stay at a cheaper scale; Cosmic conclusions must be decomposed back into verifiable local units before execution.
- Stop or fail when: scale theater; chronic overthinking.

Full package and provenance: [`reasoning-scale-controller`](../../upgradeables/reasoning/reasoning-scale-controller/UPGRADEABLE.md).

### A — Bounded Alternative Search

Recovered name: Multiverse Engine

Purpose: Obtain real alternative search without losing control of truth, constraints, cost, or convergence.

Activate when: competing hypotheses or designs would add value.

Do not use when: a locked source dictates a single faithful transformation; one hard constraint eliminates all but one path.

Requires: none.

#### Runtime mechanism

Open exactly two or three branch records that differ in strategy, causal model, or architecture. Give every branch the same locked facts, requirements, risk limits, and evaluation rubric; develop each only far enough to expose its decisive tradeoffs. Score them, apply hard vetoes before soft preferences, select or synthesize one committed path, and mark every losing branch retired so its assumptions cannot leak into execution.

#### Procedure

1. Lock shared facts, goals, constraints, risk boundaries, and a branch budget of two or three.
2. Define branches with a one-sentence strategy, distinctive assumption, predicted advantage, and disconfirming condition.
3. Develop each branch to the same decision depth; do not let the favored branch consume the entire budget.
4. Evaluate all branches on the same dimensions, such as truth, requirement coverage, coherence, cost, risk, and reversibility.
5. Veto any branch that violates a hard constraint, then select the strongest survivor or synthesize only compatible components.

#### Guardrails

- Mandatory even on strong models: material branch distinctness; shared rubric; hard-veto precedence.
- Conflict/precedence: A hard truth, safety, or authorization veto cannot be outvoted by soft quality scores; Synthesis is allowed only when selected components share compatible assumptions and interfaces.
- Stop or fail when: cosmetic branch variants; unbounded branching.

Full package and provenance: [`multiverse-reasoning`](../../upgradeables/reasoning/multiverse-reasoning/UPGRADEABLE.md).

### C — Reusable Behavior Component Builder

Recovered name: Behavior Gene Builder

Purpose: Turn repeatable behavior, logic, evidence handling, and output contracts into swappable components that compose with Cores and validators.

Activate when: a recurring task family needs reusable behavior.

Do not use when: the content is primarily domain knowledge; the behavior occurs only once.

Requires: none.

#### Runtime mechanism

Extract the invariant behavior shared by a task family and encode it in the recovered Gene schema: name/version, purpose, scope, triggers, always and avoid rules, reasoning pattern, evidence handling, Core interface, output contract, and compatibility notes. Test activation and non-activation cases, conflict precedence, and behavior with representative Cores; publish the behavior separately from knowledge and loader policy.

#### Procedure

1. Collect repeated successful and failed task instances and isolate the stable behavior rather than domain facts.
2. Define scope, activation conditions, and explicit non-triggers.
3. Specify always-do, never-do, reasoning pattern, evidence handling, and output contract.
4. Declare Core, validator, and other-Gene interfaces plus authority and conflict rules.
5. Test positive activation, false activation, missing-Core, and conflicting-Gene cases.

#### Guardrails

- Mandatory even on strong models: behavior/Core separation; trigger contract; always/avoid rules.
- Conflict/precedence: Global truth, safety, and authorization rules outrank any Gene; A Gene may query a Core but cannot silently redefine its sourced domain facts.
- Stop or fail when: behavior-knowledge conflation; monolithic Gene.

Full package and provenance: [`behavior-gene-builder`](../../upgradeables/meta-control/behavior-gene-builder/UPGRADEABLE.md).

### C — Shared Domain Knowledge Component Builder

Recovered name: Domain Core Builder

Purpose: Give multiple behaviors a shared, sourced domain substrate without duplicating knowledge across Genes or turning a Core into an OS.

Activate when: a recurring domain needs structured knowledge and decision logic.

Do not use when: the need is purely behavioral; the source corpus is too weak to support a domain model.

Requires: none.

#### Runtime mechanism

Compile sourced domain material into the recovered Core fields: scope, entities and variables, reasoning map, required data, evidence hierarchy, decision logic, failure modes, canonical examples, Gene and validator interfaces, and version provenance. Keep prescriptive behavior in Genes, expose queries and typed outputs rather than dumping the entire Core into every task, and validate both source fidelity and interface sufficiency. The C-00 builder wrapper is a modern normalization of the recovered Core schema.

#### Procedure

1. Define domain boundaries, target decisions, and excluded neighboring domains.
2. Inventory authoritative sources, entities, variables, required data, and uncertainty.
3. Build reasoning and evidence maps with provenance at the smallest maintainable units.
4. Encode decision logic, failure modes, and canonical examples without adding behavioral voice rules.
5. Declare query interfaces for Genes and validation interfaces for truth and citation checks.

#### Guardrails

- Mandatory even on strong models: source provenance; evidence hierarchy; Core/Gene separation.
- Conflict/precedence: Source evidence outranks a convenient decision map; Conflicting authoritative sources remain represented with scope and uncertainty rather than silently merged.
- Stop or fail when: knowledge-behavior conflation; unsourced compression.

Full package and provenance: [`domain-core-builder`](../../upgradeables/meta-control/domain-core-builder/UPGRADEABLE.md).

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

### R — Parallel Validation System

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

### A — Workflow Repair Supervisor

Recovered name: Meta-Supervisor Bundle

Purpose: Coordinate Meta-Awareness, Stuck-Pattern Reset, and Contradiction Micro-Repair without becoming the suite-wide mode and architecture authority.

Activate when: complex scaffolding itself needs supervision.

Do not use when: the task needs suite-wide mode declaration and Core-stack governance; one module can handle an obvious local issue.

Requires: none.

#### Runtime mechanism

Collect evidence from Meta-Awareness, classify it as loop/stale path, localized contradiction, broader state instability, or unverifiable, and activate only the smallest matching repair pack. Preserve locked state, serialize repair ownership so packs do not race, then re-observe the affected process. Meta-Supervisor manages health diagnosis and repair; Ultimate Suite Supervisor remains responsible for global modes, stack enforcement, edit-class selection, and suite conflicts.

#### Procedure

1. Request or read an evidence-bearing process-health snapshot.
2. Classify the failure and identify the smallest responsible state or reasoning region.
3. Select no action, Stuck-Pattern Reset, Contradiction Micro-Repair, or escalation to Meta-Stability or suite supervision.
4. Lock facts, constraints, and unaffected modules; assign one repair owner.
5. Run the bounded repair and request a fresh health observation.

#### Guardrails

- Mandatory even on strong models: diagnosis-before-repair; smallest-pack selection; locked-state preservation.
- Conflict/precedence: Suite-wide mode or authority conflicts escalate to Ultimate Suite Supervisor; One repair owner controls a failed region at a time.
- Stop or fail when: supervisor recursion; repair-pack races.

Full package and provenance: [`meta-supervisor`](../../upgradeables/meta-control/meta-supervisor/UPGRADEABLE.md).

### A — Adapter-First Experimentation

Purpose: Protect a working OS or workflow from speculative capabilities while preserving a path for evidence-based evolution.

Activate when: a new capability may destabilize a base workflow.

Do not use when: the change is a mandatory security repair; no stable interface can isolate the capability.

Requires: none.

#### Runtime mechanism

Define an adapter contract around the proposed capability, route only an explicit test cohort through it, and preserve the unchanged base as control and rollback. Compare quality, cost, latency, drift, and failure behavior against predeclared acceptance thresholds; promote only the demonstrated stable interface, otherwise revise or retire the adapter without contaminating core rules.

#### Procedure

1. State the hypothesis, acceptance metrics, test cohort, and non-negotiable invariants.
2. Expose the smallest stable interface needed by the capability.
3. Implement or specify it as a detachable adapter with base-path fallback and isolated state.
4. Run representative and adversarial trials against the unchanged base.
5. Compare benefit, regressions, operating cost, and rollback behavior.

#### Guardrails

- Mandatory even on strong models: detachable boundary; control comparison; invariant gate.
- Conflict/precedence: Security and integrity repairs follow their mandated path rather than waiting for experimental promotion; If the adapter cannot be isolated from base state or authority, do not trial it in production.
- Stop or fail when: base contamination; unmeasured promotion.

Full package and provenance: [`adapter-first-experimentation`](../../upgradeables/meta-control/adapter-first-experimentation/UPGRADEABLE.md).

### A — Precision Local System Edit

Recovered name: CRISPR Editing

Purpose: Make high-confidence micro-edits to structured systems without collateral semantic or interface drift.

Activate when: a change is small and local.

Do not use when: the governing structure is wrong; multiple interfaces must be redesigned.

Requires: none.

#### Runtime mechanism

Construct a patch contract before editing: exact target coordinates, requested semantic delta, protected invariants, allowed collateral region, and validation probes. Snapshot the target plus its immediate dependency boundary, apply the smallest diff that realizes the delta, and compare before/after behavior on both the changed case and invariant cases. A patch that requires broad remapping is rejected and escalated to Surgery rather than stretched into disguised rewrite.

#### Procedure

1. Identify the exact editable unit and the request's semantic delta.
2. Enumerate invariants: facts, IDs, interfaces, precedence, citations, unaffected behaviors, and formatting contracts that must not change.
3. Trace immediate inbound and outbound dependencies to set a finite collateral boundary.
4. Create and apply the smallest patch inside that boundary.
5. Run a positive probe for the new behavior and negative probes for each protected invariant.

#### Guardrails

- Mandatory even on strong models: explicit invariant set; bounded dependency inspection; positive and negative probes.
- Conflict/precedence: Locked safety, truth, and authorization invariants cannot be included in the requested delta; If the new behavior and protected invariants cannot coexist, stop and expose the conflict.
- Stop or fail when: collateral semantic drift; syntactically valid but behaviorally wrong patch.

Full package and provenance: [`crispr-edit`](../../upgradeables/editing-repair/crispr-edit/UPGRADEABLE.md).

### C — Structural System Edit

Recovered name: Surgery Editing

Purpose: Make macro changes to layers, cores, workflows, or incompatible interfaces without losing invariants, dependents, or rollback control.

Activate when: layers, Cores, or workflows require major replacement.

Do not use when: a localized invariant-preserving patch suffices; the replacement architecture lacks acceptance criteria.

Requires: none.

#### Runtime mechanism

Declare the failing structural boundary and why CRISPR cannot preserve it, inventory every inbound and outbound interface, and define a replacement architecture with mapped invariants. Plan old-to-new state migration, adapters, staged cutover, observability, and rollback; change the structure in bounded phases, validate each dependent contract, then remove the old path only after the replacement passes global checks.

#### Procedure

1. Document the architecture-level failure and evidence that local editing is insufficient.
2. Inventory components, state, public and internal interfaces, dependents, precedence rules, and invariants.
3. Design the replacement structure and map every old responsibility and interface to retain, adapt, retire, or explicitly reject.
4. Define migration order, compatibility adapters, checkpoints, observability, rollback, and cutover criteria.
5. Implement or specify the replacement in stages while validating each interface and state transfer.

#### Guardrails

- Mandatory even on strong models: CRISPR-insufficiency proof; interface inventory; old-to-new mapping.
- Conflict/precedence: Use CRISPR when all required behavior can coexist with current interfaces inside a bounded patch; A hard invariant without a valid old-to-new mapping blocks cutover.
- Stop or fail when: macro edit disguised as patch accumulation; unmapped dependents.

Full package and provenance: [`surgery-edit`](../../upgradeables/editing-repair/surgery-edit/UPGRADEABLE.md).

### A — Per-Region Reasoning Depth

Recovered name: Dynamic Depth Allocation

Purpose: Concentrate analysis and verification where local marginal value is highest instead of applying uniform depth across a task.

Activate when: task regions vary in difficulty or risk.

Do not use when: every unit has the same mandated review depth; the task is one atomic operation.

Requires: none.

#### Runtime mechanism

Partition the task into meaningful regions, score each on difficulty, uncertainty, consequence, dependency centrality, and current evidence deficit, and assign depth bands under the Cognitive Governor's total envelope. Re-score after discoveries and move effort toward unresolved hotspots while maintaining a minimum pass everywhere. DDA decides where depth goes, not the total budget or execution concurrency.

#### Procedure

1. Decompose the task into independently inspectable regions or claims.
2. Score each region for uncertainty, consequence, coupling, novelty, and evidence deficit.
3. Reserve a minimum validation pass for all regions.
4. Allocate the remaining governed budget to high-score regions and choose appropriate methods for each.
5. Re-score when a local finding changes dependencies or risk.

#### Guardrails

- Mandatory even on strong models: minimum regional pass; hotspot-driven allocation; budget-bound re-scoring.
- Conflict/precedence: A high-risk mandatory check receives its floor even if its estimated uncertainty is low; When every region exceeds the available envelope, escalate the budget or narrow scope rather than fabricate coverage.
- Stop or fail when: uniform-depth default; hotspot tunnel vision.

Full package and provenance: [`dynamic-depth-allocation`](../../upgradeables/meta-control/dynamic-depth-allocation/UPGRADEABLE.md).

### A — Anti-Tunnel Vision

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

### A — Runtime Compatibility Mode Selector

Recovered name: Future-Proof Mode Selector

Purpose: Keep workflows portable across frontier and smaller models, tool environments, and future hosts without weakening invariant controls.

Activate when: an implementation targets models with different capabilities.

Do not use when: the host and task profile are fixed; capability cannot be tested and no conservative fallback exists.

Requires: none.

#### Runtime mechanism

Probe real host affordances—context, tools, state persistence, structured outputs, reliability evidence, and execution permissions—then combine them with task risk to choose a named light, standard, or heavy scaffold profile. Use model-size drift scaling as one capability signal, never as the selector itself; capability claims must be observed or declared, and truth, safety, state, and integrity invariants remain mandatory in every profile.

#### Procedure

1. Declare the task's risk, state, tool, and validation requirements.
2. Probe or read the host's actual capabilities and permissions without assuming hidden persistence or tools.
3. Map capability and risk to a predeclared operating profile with explicit enabled and omitted controls.
4. Run a readiness check and select a conservative fallback when any required affordance is absent.
5. Monitor failures that invalidate the profile and switch modes at a checkpoint.

#### Guardrails

- Mandatory even on strong models: risk overlay; real capability check; invariant preservation.
- Conflict/precedence: Task-risk requirements override host convenience; Absent required capability routes to fallback or blocked, never simulated capability.
- Stop or fail when: capability hallucination; model-brand heuristics.

Full package and provenance: [`future-proof-mode-selector`](../../upgradeables/meta-control/future-proof-mode-selector/UPGRADEABLE.md).
