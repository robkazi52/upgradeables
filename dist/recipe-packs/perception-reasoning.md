# Perception & Spatial Reasoning — Runtime Pack

Purpose: Infer and apply transformations in bounded grid, symbolic, visual-analogy, or spatial-reasoning tasks.

Task family: grid puzzles, pattern completion, visual analogies, inductive rule inference, and spatial transformations

Activation boundary: Use for bounded integer-grid or symbolic transformation tasks with at least one training pair and a test input; disclose reduced verification when only one pair is available.

Use this generated pack for execution. Do not also load the source recipe,
resolved recipe, catalog record, or full packages unless a material ambiguity
requires deeper inspection.

`R` owns a required guarantee but may remain dormant until its pipeline phase.
`A`, `C`, and `O` still require active triggers. `X` remains excluded without
a task-specific reason.

## Composition

Observe without committing, generate only as many candidates as the examples
justify, attempt to falsify each candidate across every training pair, lock one
rule, then construct and verify the output locally. `X` components remain excluded
unless a task-specific trigger overrides the recipe.

## Output contract

Return the requested artifact, evidence, limitations, and unresolved inputs.

## Component routing

| Role | Component | Activate when |
|:---:|---|---|
| R | `task-set-lock-in@1.1.0` — Task-Set Lock-In | multi-step work begins or scope changes |
| R | `grounding-no-invention@1.1.0` — Grounding / No-Invention | work relies on documents, data, external facts, or consequential claims |
| R | `anti-tunnel-vision@1.1.0` — Anti-Tunnel Vision | premature fixation could hide credible alternatives |
| R | `bounded-exit@1.1.0` — Bounded Iteration Stop Rule | a draft needs iterative improvement |
| R | `micro-scaffolding@1.1.0` — Micro-Scaffolding | multi-step or high-constraint work |
| A | `bidirectional-consistency@1.1.0` — Bidirectional Consistency | causal, logical, quantitative, or evidence claims are central |
| A | `forethought-checkpoints@1.1.0` — Forethought / Checkpoints | an action is costly, irreversible, or dependency-sensitive |
| A | `cot-structured-state-block@1.1.0` — Auditable Reasoning State | structured intermediate task state must survive across steps |
| C | `decision-first-scaffold@1.1.0` — Decision-First Scaffold | analysis risks becoming directionless before commitment |
| C | `invariance-stress-scaffold@1.1.0` — Protected-Constraint Robustness Test | a patch or rewrite must preserve invariants |
| C | `counterfactual-integrity@1.1.0` — Counterfactual Integrity Gate | counterfactual or hypothetical reasoning is used |
| O | `multiverse-reasoning@1.1.0` — Bounded Alternative Search | competing hypotheses or designs would add value |
| O | `cognitive-governor@1.1.0` — Reasoning Effort Budget Controller | effort allocation materially affects cost or quality |
| X | `coherence-heartbeat@1.1.0` — Periodic Whole-Task Consistency Check | a workflow is long or multi-stage |
| X | `meta-supervisor@1.1.0` — Workflow Repair Supervisor | complex scaffolding itself needs supervision |

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

Full package and provenance: [`task-set-lock-in`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/state/task-set-lock-in/UPGRADEABLE.md).

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

Full package and provenance: [`grounding-no-invention`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/truth-grounding/grounding-no-invention/UPGRADEABLE.md).

### R — Anti-Tunnel Vision

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

Full package and provenance: [`anti-tunnel-vision`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/reasoning/anti-tunnel-vision/UPGRADEABLE.md).

### R — Bounded Iteration Stop Rule

Recovered name: Bounded ExIt

Purpose: Turn iterative improvement into a terminating control loop with explicit quality, budget, and diminishing-return gates.

Activate when: a draft needs iterative improvement.

Do not use when: a mandatory validator has not yet passed; a hard defect requires escalation rather than iteration.

Requires: none.

#### Runtime mechanism

Each pass evaluates the artifact against locked goals, chooses the single highest-value remaining defect, repairs it, and re-evaluates. Exit occurs on threshold satisfaction, budget exhaustion, or diminishing expected improvement; the historical acronym expansion is deliberately left unrecovered.

#### Procedure

1. Lock acceptance criteria and a maximum pass or cost budget.
2. Score the current artifact against those criteria.
3. Choose the highest-impact repair that can be completed without reopening accepted decisions.
4. Apply the repair and record whether the target metric improved.
5. Stop when criteria pass, no repair has positive expected value, or the budget is reached; otherwise repeat.

#### Guardrails

- Mandatory even on strong models: predeclared exit rule; post-repair re-evaluation; mandatory-gate precedence.
- Conflict/precedence: Mandatory acceptance checks outrank a pass budget; if budget expires first, return blocked rather than pass; A newly discovered architecture failure hands off to Surgery or Regenerative Rewrite instead of repeating local passes.
- Stop or fail when: endless recursive polishing; stopping with a known blocking defect.

Full package and provenance: [`bounded-exit`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/reasoning/bounded-exit/UPGRADEABLE.md).

### R — Micro-Scaffolding

Purpose: Protect a difficult local operation without loading the full OS, duplicating the parent StateBlock, or leaving permanent context residue.

Activate when: multi-step or high-constraint work.

Do not use when: a one-step task has no fragile constraints; the proposed scaffold repeats the full StateBlock or source corpus.

Requires: none.

#### Runtime mechanism

At the start of a fragile subtask, extract only the few invariants and checkpoints that could be lost locally, such as preserve all numbers, preserve citation mapping, change tone only, and do not alter the conclusion. Use that compact scaffold while performing the step, check the local result against it, then retire the scaffold immediately when the subtask is accepted. It remains strictly smaller and shorter-lived than the workflow's canonical StateBlock.

#### Procedure

1. Identify the current subtask and the specific failure risks within it.
2. Select the minimum local invariants, evidence pointers, and next-step checkpoints needed to control those risks.
3. Write a compact scaffold; do not copy unrelated global rules or full source material into it.
4. Execute the subtask while checking decisions against the scaffold.
5. Verify the local output against each scaffold item.

#### Guardrails

- Mandatory even on strong models: identify the fragile local invariants; verify them after the step; retire temporary scaffolding.
- Conflict/precedence: Global task locks and source boundaries outrank a local scaffold; If the subtask expands into an architecture-level problem, retire the scaffold and re-plan at the parent task level.
- Stop or fail when: Escalate when the required control cannot remain local or when the scaffold grows into a duplicate of the parent plan/state; Reject the local result if any protected item was lost or changed without authorization.

Full package and provenance: [`micro-scaffolding`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/foundation/micro-scaffolding/UPGRADEABLE.md).

### A — Bidirectional Consistency

Purpose: Expose lossy, non-invertible, or spuriously plausible transformations that one-way review misses.

Activate when: causal, logical, quantitative, or evidence claims are central.

Do not use when: the transformation is intentionally irreversible and no reverse contract is claimed; creative output has no declared source mapping.

Requires: none.

#### Runtime mechanism

Run a forward check from source conditions to proposed result, then independently read the result backward to enumerate which source conditions it actually entails. Compare the reconstructed set with the locked source atoms; missing, invented, or many-to-one-collapsed atoms fail even when the forward narrative is fluent.

#### Procedure

1. Lock the source atoms and declared transformation contract.
2. Verify that each source atom has a forward image in the result.
3. Hide the source and reconstruct its implied atoms from the result alone.
4. Compare reconstructed atoms with the locked set.
5. Classify omissions, inventions, and ambiguity introduced by the mapping.

#### Guardrails

- Mandatory even on strong models: independent backward reconstruction for lossy or high-stakes transformations.
- Conflict/precedence: The declared transformation contract determines which information may be lost; A reverse contradiction on a locked atom overrides stylistic forward plausibility.
- Stop or fail when: Do not certify when a material source constraint has no forward image or when the result implies a contradictory source condition.

Full package and provenance: [`bidirectional-consistency`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/validation/bidirectional-consistency/UPGRADEABLE.md).

### A — Forethought / Checkpoints

Purpose: Catch missing prerequisites and foreseeable downstream failure while reversal is still cheap.

Activate when: an action is costly, irreversible, or dependency-sensitive.

Do not use when: reversible low-cost local edits; the checkpoint would duplicate an already enforced transaction guard.

Requires: none.

#### Runtime mechanism

At each consequential boundary, predict the most likely downstream failure, verify the prerequisite that would prevent it, define observable success and rollback, then commit and check the result. Checkpoints are placed by consequence rather than at every trivial step.

#### Procedure

1. Identify the next irreversible, high-cost, or dependency-sensitive action.
2. Name the plausible downstream failure and affected dependency.
3. Verify prerequisites, authority, backups, and rollback path proportionate to risk.
4. Define the immediate post-action observation that indicates success or failure.
5. Commit only if the checkpoint passes, then inspect the result before continuing.

#### Guardrails

- Mandatory even on strong models: pre-commit prerequisite check for consequential actions; success and rollback observation.
- Conflict/precedence: A failed hard prerequisite blocks commitment regardless of schedule pressure; During urgent containment, use the approved emergency checkpoint rather than omitting checks entirely.
- Stop or fail when: ritual checklists unrelated to risk; analysis after commitment instead of before.

Full package and provenance: [`forethought-checkpoints`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/reasoning/forethought-checkpoints/UPGRADEABLE.md).

### A — Auditable Reasoning State

Recovered name: CoT-Structured State Block

Purpose: Make reasoning-relevant state portable and auditable while preserving the boundary between useful state and hidden internal deliberation.

Activate when: structured intermediate task state must survive across steps.

Do not use when: a one-turn answer has no meaningful state; the request seeks hidden chain-of-thought.

Requires: none.

#### Runtime mechanism

Maintain an explicit schema of externally useful reasoning state: verified facts with provenance, user-provided constraints, labeled assumptions, concise conclusion summaries, unresolved questions, confidence, and next action. The block records what another worker needs to continue; it never stores token-level private deliberation or presents inference as evidence.

#### Procedure

1. Define the minimum state schema and sensitivity boundary.
2. Populate facts only from cited or user-provided material and label assumptions separately.
3. Record concise decision rationales and confidence rather than hidden reasoning traces.
4. Update changed fields at checkpoints and preserve provenance.
5. Project only the fields needed by the next consumer.

#### Guardrails

- Mandatory even on strong models: fact/inference separation; provenance; explicit uncertainty.
- Conflict/precedence: Canonical cited evidence overrides stale state summaries; If a requested field would expose private reasoning, provide a concise rationale or evidence ledger instead.
- Stop or fail when: Stop treating the block as authoritative if provenance is missing or fields are stale; Do not use the pattern to satisfy requests for hidden chain-of-thought.

Full package and provenance: [`cot-structured-state-block`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/state/cot-structured-state-block/UPGRADEABLE.md).

### C — Decision-First Scaffold

Purpose: Keep analysis shaped around a decision, options, and decision criteria rather than accumulating directionless detail.

Activate when: analysis risks becoming directionless before commitment.

Do not use when: the task asks only for faithful extraction or description; the decision owner or available options are unknown.

Requires: none.

#### Runtime mechanism

Modern conservative interpretation: write a decision sentence with owner, options, criteria, and deadline or commitment point; then admit analysis only when it changes an option score, exposes a constraint, or reduces a named uncertainty. The historical corpus recovers the exact name but not this mechanism.

#### Procedure

1. State the decision in one sentence, including who will act.
2. List viable options, including defer or gather-more-evidence where legitimate.
3. Lock decision criteria and non-negotiable constraints.
4. Map each analysis question to a criterion or uncertainty.
5. Produce a recommendation with the evidence and unresolved uncertainty that drives it.

#### Guardrails

- Mandatory even on strong models: explicit decision statement; criterion linkage; uncertainty-aware outcome.
- Conflict/precedence: If the user requests exploration without commitment, do not impose a final choice; If evidence cannot support any option, return the missing evidence rather than a fabricated recommendation.
- Stop or fail when: invented historical mechanics; premature option closure.

Full package and provenance: [`decision-first-scaffold`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/reasoning/decision-first-scaffold/UPGRADEABLE.md).

### C — Protected-Constraint Robustness Test

Recovered name: Invariance Stress Scaffold

Purpose: Operationalize the recovered name without pretending the original January 2026 mechanics were recovered.

Activate when: a patch or rewrite must preserve invariants.

Do not use when: the transformed feature is itself decision-relevant; the invariants cannot be stated.

Requires: none.

#### Runtime mechanism

Define the properties claimed invariant, generate a small controlled set of transformations that should preserve those properties—such as reordering independent facts, paraphrasing without modal change, or changing irrelevant formatting—and compare outputs. Any decision-relevant change is reported as sensitivity; this is a modern stress-test interpretation, not a recovered historical algorithm.

#### Procedure

1. State the claimed invariant and observable pass condition.
2. Separate semantics-preserving perturbations from meaning-changing controls.
3. Construct a bounded perturbation set and preserve provenance.
4. Run the task independently on original and perturbed inputs.
5. Compare conclusions, confidence, constraints, and safety behavior.

#### Guardrails

- Mandatory even on strong models: explicit invariant and at least one controlled counterfactual comparison when robustness is claimed.
- Conflict/precedence: Meaning-changing controls are not invariant breaches; Safety behavior must remain at least as conservative under semantics-preserving perturbations.
- Stop or fail when: Do not claim robustness when decision-relevant output changes under a justified semantics-preserving perturbation.

Full package and provenance: [`invariance-stress-scaffold`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/validation/invariance-stress-scaffold/UPGRADEABLE.md).

### C — Counterfactual Integrity Gate

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

Full package and provenance: [`counterfactual-integrity`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/truth-grounding/counterfactual-integrity/UPGRADEABLE.md).

### O — Bounded Alternative Search

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

Full package and provenance: [`multiverse-reasoning`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/reasoning/multiverse-reasoning/UPGRADEABLE.md).

### O — Reasoning Effort Budget Controller

Recovered name: Reasoning Budget / Cognitive Governor

Purpose: Prevent both expensive overthinking of trivial work and unsafe underchecking of consequential work.

Activate when: effort allocation materially affects cost or quality.

Do not use when: a mandatory protocol fixes the review budget; the task is a trivial deterministic transformation.

Requires: none.

#### Runtime mechanism

Estimate a total effort envelope from complexity, uncertainty, consequence, irreversibility, and the expected value of another check. Allocate caps for planning, execution, and validation, reserve extra capacity for high-risk unknowns, and periodically compare remaining defect or uncertainty value with remaining cost. The governor owns how much total reasoning is justified; it does not choose which regions receive that effort or how much work flows concurrently.

#### Procedure

1. Classify task complexity, uncertainty, consequence, and reversibility.
2. Set an effort envelope and mandatory validation floor.
3. Divide the envelope among planning, execution, verification, and contingency.
4. Track evidence gained, defects removed, and budget consumed at milestones.
5. Increase the envelope only when newly exposed risk has positive expected value; otherwise invoke the exit rule.

#### Guardrails

- Mandatory even on strong models: risk-based validation floor; marginal-value review; explicit stop or escalation.
- Conflict/precedence: Risk-mandated validation overrides a lower convenience budget; If the envelope cannot cover hard checks, return an explicit resource or evidence blocker.
- Stop or fail when: over-polishing; premature exit.

Full package and provenance: [`cognitive-governor`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/meta-control/cognitive-governor/UPGRADEABLE.md).
