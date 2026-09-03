# Coding / Debugging — Runtime Pack

Purpose: Reproduce, diagnose, and repair a software defect with the smallest verified change.

Task family: software debugging, reproduction, diagnosis, and verified repair

Activation boundary: Use after a software defect is reproducible or tightly localized and the task requests a verified repair, not a review-only finding.

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
| A | `stateblock@1.1.0` — Canonical Task State | work spans multiple steps or components |
| A | `forethought-checkpoints@1.1.0` — Forethought / Checkpoints | an action is costly, irreversible, or dependency-sensitive |
| A | `dominant-driver-isolation-scaffold@1.1.0` — Dominant-Driver Isolation Scaffold | many plausible causes compete for priority |
| A | `anti-tunnel-vision@1.1.0` — Anti-Tunnel Vision | premature fixation could hide credible alternatives |
| A | `bidirectional-consistency@1.1.0` — Bidirectional Consistency | causal, logical, quantitative, or evidence claims are central |
| R | `invariance-stress-scaffold@1.1.0` — Protected-Constraint Robustness Test | a patch or rewrite must preserve invariants |
| R | `micro-repair@1.1.0` — Minimal Local Correction | a specific defect has been localized |
| A | `crispr-edit@1.1.0` — Precision Local System Edit | a change is small and local |
| C | `surgery-edit@1.1.0` — Structural System Edit | layers, Cores, or workflows require major replacement |
| A | `structured-refinement@1.1.0` — Structured Refinement Cycles | revision has multiple defect classes |
| A | `bounded-exit@1.1.0` — Bounded Iteration Stop Rule | a draft needs iterative improvement |
| A | `parallel-qms@1.1.0` — Parallel Validation System | a composed workflow needs structured quality evaluation |
| A | `drift-suppression@1.1.0` — Drift Suppression | long, branching, or iterative work |

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

### A — Canonical Task State

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

### A — Dominant-Driver Isolation Scaffold

Purpose: Separate high-leverage causes or constraints from correlated, downstream, or low-impact factors.

Activate when: many plausible causes compete for priority.

Do not use when: the system is known to require irreducibly joint causes; available evidence supports only correlation.

Requires: none.

#### Runtime mechanism

Modern conservative interpretation: enumerate candidate drivers, define the target outcome, estimate each candidate's unique explanatory or intervention leverage, and test the leading driver against the strongest alternative and interaction effects. The historical sources recover only the scaffold's exact name.

#### Procedure

1. Define the outcome and the time or system boundary.
2. List candidate drivers and distinguish causes, constraints, symptoms, and proxies.
3. Estimate each candidate's marginal effect using available comparisons, traces, or counterfactuals.
4. Test the leader against the strongest rival and check whether a pairwise interaction changes the ranking.
5. Select the dominant driver or report that no single driver is defensible; route effort accordingly.

#### Guardrails

- Mandatory even on strong models: rival test; interaction check; causal-evidence label.
- Conflict/precedence: A safety-critical factor is not discarded solely because its probability or average effect is lower; If interaction terms dominate marginal effects, return a coupled-driver result rather than forcing one winner.
- Stop or fail when: correlation presented as cause; single-factor oversimplification.

Full package and provenance: [`dominant-driver-isolation-scaffold`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/reasoning/dominant-driver-isolation-scaffold/UPGRADEABLE.md).

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

Full package and provenance: [`anti-tunnel-vision`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/reasoning/anti-tunnel-vision/UPGRADEABLE.md).

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

### R — Protected-Constraint Robustness Test

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

### R — Minimal Local Correction

Recovered name: Micro-Repair

Purpose: Restore local correctness or completeness with the minimum semantic blast radius.

Activate when: a specific defect has been localized.

Do not use when: the artifact architecture is globally wrong; the same defect repeats systemically.

Requires: none.

#### Runtime mechanism

Define a repair window around the smallest unit that fails an explicit criterion, freeze the surrounding accepted region, patch only that unit and any directly required connective token, then compare the window before and after. Widen once only when a direct dependency proves the first window insufficient; recurring or architecture-level failure escalates instead of allowing scope creep.

#### Procedure

1. Identify the exact failed criterion and the smallest text, field, rule, or code unit causing it.
2. Mark the surrounding accepted content and locked facts as frozen.
3. Draft the smallest replacement that satisfies the criterion.
4. Check boundary coherence with the immediately preceding and following units.
5. Verify the target defect is gone and no frozen atom changed.

#### Guardrails

- Mandatory even on strong models: smallest-fault localization; changed-atom comparison; systemic-failure escalation.
- Conflict/precedence: Do not preserve a frozen neighbor if it is proven part of the defect; explicitly widen the window instead; A locked invariant outranks local fluency.
- Stop or fail when: scope creep; cosmetic rewriting around a defect.

Full package and provenance: [`micro-repair`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/editing-repair/micro-repair/UPGRADEABLE.md).

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

Full package and provenance: [`crispr-edit`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/editing-repair/crispr-edit/UPGRADEABLE.md).

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

Full package and provenance: [`surgery-edit`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/editing-repair/surgery-edit/UPGRADEABLE.md).

### A — Structured Refinement Cycles

Purpose: Prevent one revision pass from trading away correctness while improving structure or style.

Activate when: revision has multiple defect classes.

Do not use when: only one bounded defect exists; the artifact requires complete regeneration.

Requires: none.

#### Runtime mechanism

Classify defects before editing and run passes in dependency order: facts and source mapping first, structure and requirement coverage second, style and pedagogy third, final validation last. Accepted decisions are locked between passes, and a later pass may not silently reopen an earlier one.

#### Procedure

1. Inventory defects and assign each to factual, structural, stylistic, or validation class.
2. Correct facts, citations, and locked constraints; freeze the accepted semantic ledger.
3. Repair ordering, dependencies, section roles, and requirement coverage without changing the frozen facts.
4. Adjust voice, clarity, and pedagogy without changing facts or structure except where explicitly authorized.
5. Run an independent final check across all classes and use Bounded ExIt to decide whether another pass is justified.

#### Guardrails

- Mandatory even on strong models: dependency order; between-pass locks; final cross-class review.
- Conflict/precedence: Factual correctness outranks structural elegance and style; A later pass that discovers an upstream defect returns explicitly to the relevant pass and revalidates downstream results.
- Stop or fail when: mixed-objective drift; later-pass regression.

Full package and provenance: [`structured-refinement`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/editing-repair/structured-refinement/UPGRADEABLE.md).

### A — Bounded Iteration Stop Rule

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

### A — Drift Suppression

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
