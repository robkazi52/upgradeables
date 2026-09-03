# Creative Ideation — Runtime Pack

Purpose: Generate materially distinct ideas and converge on a bounded selection using explicit criteria.

Task family: bounded brainstorming, concept generation, and selection

Activation boundary: Use when the user needs multiple materially distinct concepts followed by bounded convergence, while factual claims remain outside the creative corridor.

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
| R | `controlled-drift-corridors@1.1.0` — Bounded Change Rules | synthesis or creativity must coexist with fidelity |
| A | `counterfactual-integrity@1.1.0` — Counterfactual Integrity Gate | counterfactual or hypothetical reasoning is used |
| A | `domain-mode-isolation@1.1.0` — Domain / Mode Isolation | multiple domains or semantic modes coexist |
| A | `multiverse-reasoning@1.1.0` — Bounded Alternative Search | competing hypotheses or designs would add value |
| A | `anti-tunnel-vision@1.1.0` — Anti-Tunnel Vision | premature fixation could hide credible alternatives |
| C | `parallel-qms@1.1.0` — Parallel Validation System | a composed workflow needs structured quality evaluation |
| C | `grounding-no-invention@1.1.0` — Grounding / No-Invention | work relies on documents, data, external facts, or consequential claims |

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

### R — Bounded Change Rules

Recovered name: Controlled Drift Corridors

Purpose: Enable adaptation, compression, or creativity without surrendering semantic control.

Activate when: synthesis or creativity must coexist with fidelity.

Do not use when: all content is zero-drift; allowed dimensions cannot be tested.

Requires: none.

#### Runtime mechanism

Partition the artifact into regions or claim types and assign each a corridor specifying fixed invariants, allowed dimensions of change, maximum semantic distance, evidence requirements, and rollback trigger. Transform only after the corridor is explicit, then compare output to the source and tighten or revert any region outside bounds.

#### Procedure

1. Segment the task into regions with materially different tolerance.
2. For each region, list invariants and allowed changes such as tone, length, order, or abstraction.
3. Set validation metrics or review questions and a rollback threshold.
4. Transform one region inside its corridor.
5. Compare claims, obligations, entities, and required structure to source.

#### Guardrails

- Mandatory even on strong models: explicit allowed dimensions; locked invariants; region-specific validation.
- Conflict/precedence: Higher-authority task constraints and zero-drift fields override corridor permissions; If validation signals disagree, apply the narrowest supported corridor or request review.
- Stop or fail when: Stop transformation when invariants cannot be measured or recovered; Revert regions that cross the boundary instead of rationalizing post hoc.

Full package and provenance: [`controlled-drift-corridors`](../../upgradeables/drift-control/controlled-drift-corridors/UPGRADEABLE.md).

### A — Counterfactual Integrity Gate

Purpose: Make counterfactual exploration safe and auditable by preserving an explicit boundary between factual, evaluative, framing, and hypothetical phases.

Activate when: counterfactual or hypothetical reasoning is used.

Do not use when: the task contains no hypothetical branch; the user explicitly requires purely factual extraction, where counterfactual-silence is the narrower control.

Requires: none.

#### Runtime mechanism

Tag each proposition by semantic phase and keep hypothetical premises, derived consequences, and branch-local assumptions in a separate compartment. Any transfer from a hypothetical branch into factual state requires independent factual support; otherwise the proposition remains labeled hypothetical or is excluded from the factual output.

#### Procedure

1. Declare the factual baseline and the allowed counterfactual question.
2. Tag introduced premises as hypothetical and retain their branch identity.
3. Derive consequences only inside that branch.
4. Check the draft for branch-local material presented without a hypothesis label.
5. Move a proposition into factual state only when independent evidence supports it.

#### Guardrails

- Mandatory even on strong models: no hypothetical premise or consequence may silently become fact.
- Conflict/precedence: A factual-only task boundary overrides permission to explore counterfactuals; A stylistic request to write hypotheticals as certain cannot override phase labels.
- Stop or fail when: If branch-local assumptions cannot be separated from factual claims, do not certify the mixed output.

Full package and provenance: [`counterfactual-integrity`](../../upgradeables/truth-grounding/counterfactual-integrity/UPGRADEABLE.md).

### A — Domain / Mode Isolation

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

Full package and provenance: [`domain-mode-isolation`](../../upgradeables/state/domain-mode-isolation/UPGRADEABLE.md).

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

### C — Parallel Validation System

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

### C — Grounding / No-Invention

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
