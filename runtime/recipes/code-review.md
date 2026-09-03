# Code / Pull Request Review — Runtime Pack

Purpose: Review a concrete diff or pull request for bugs, regressions, unsafe assumptions, and missing tests without editing it.

Task family: pull-request, diff, commit, and regression review

Activation boundary: Use when the requested deliverable is review-only analysis of a concrete diff or pull request for correctness, regressions, and unsupported assumptions.

Use this generated pack for execution. Do not also load the source recipe,
resolved recipe, catalog record, or full packages unless a material ambiguity
requires deeper inspection.

`R` owns a required guarantee but may remain dormant until its pipeline phase.
`A`, `C`, and `O` still require active triggers. `X` remains excluded without
a task-specific reason.

## Composition

Lock the requested review scope and expected output. Inspect the diff, relevant
callers, contracts, tests, and configuration without assuming unseen behavior.
If no diff, branch, commit range, or pull-request link is supplied, request one
and stop rather than inventing review findings.
Look for correctness defects, regressions, unsafe assumptions, missing tests, and
scope drift. This is a review-only recipe: do not activate editing components
unless the user separately asks for fixes.

Parallel QMS means independent evidence, logic, and regression checks. Run those
checks sequentially when the host cannot execute real parallel workers.

## Output contract

Lead with actionable findings ordered by severity. For each finding, identify the
affected file/location, evidence, impact, and a bounded repair direction. Separate
confirmed defects from questions and low-confidence risks. State when no material
finding is supported and summarize remaining test or context gaps.

## Component routing

| Role | Component | Activate when |
|:---:|---|---|
| R | `task-set-lock-in@1.1.0` — Task-Set Lock-In | multi-step work begins or scope changes |
| R | `scoped-loader@1.1.0` — Scoped Loader / Loader Sequencing | a modular workflow has multiple available components |
| R | `grounding-no-invention@1.1.0` — Grounding / No-Invention | work relies on documents, data, external facts, or consequential claims |
| C | `stateblock@1.1.0` — Canonical Task State | work spans multiple steps or components |
| A | `forethought-checkpoints@1.1.0` — Forethought / Checkpoints | an action is costly, irreversible, or dependency-sensitive |
| A | `dominant-driver-isolation-scaffold@1.1.0` — Dominant-Driver Isolation Scaffold | many plausible causes compete for priority |
| A | `anti-tunnel-vision@1.1.0` — Anti-Tunnel Vision | premature fixation could hide credible alternatives |
| A | `bidirectional-consistency@1.1.0` — Bidirectional Consistency | causal, logical, quantitative, or evidence claims are central |
| C | `invariance-stress-scaffold@1.1.0` — Protected-Constraint Robustness Test | a patch or rewrite must preserve invariants |
| A | `epistemic-status-gating@1.1.0` — Evidence-Confidence Gate | claims of mixed certainty are present |
| C | `critical-atomic-verification@1.1.0` — Critical Fact Verification | small factual errors could change the outcome |
| C | `citation-fidelity@1.1.0` — Citation Fidelity Gate | output contains citations or source-attributed claims |
| A | `parallel-qms@1.1.0` — Parallel Validation System | a composed workflow needs structured quality evaluation |
| A | `drift-suppression@1.1.0` — Drift Suppression | long, branching, or iterative work |
| C | `fail-closed-abstention@1.1.0` — Fail-Closed Abstention | required evidence cannot be verified |

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

### C — Canonical Task State

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

Full package and provenance: [`forethought-checkpoints`](../../upgradeables/reasoning/forethought-checkpoints/UPGRADEABLE.md).

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

Full package and provenance: [`dominant-driver-isolation-scaffold`](../../upgradeables/reasoning/dominant-driver-isolation-scaffold/UPGRADEABLE.md).

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

Full package and provenance: [`bidirectional-consistency`](../../upgradeables/validation/bidirectional-consistency/UPGRADEABLE.md).

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

Full package and provenance: [`invariance-stress-scaffold`](../../upgradeables/validation/invariance-stress-scaffold/UPGRADEABLE.md).

### A — Evidence-Confidence Gate

Recovered name: Epistemic Status Gating

Purpose: Keep mixed-certainty reasoning auditable and stop conclusions from laundering inference or hypothesis into fact.

Activate when: claims of mixed certainty are present.

Do not use when: the task contains only direct transformation with no inferential claims; labels would be exposed as private chain-of-thought rather than concise epistemic status.

Requires: none.

#### Runtime mechanism

Represent material propositions with an explicit status drawn from factual, evaluative/inferential, framing, or hypothetical phases, plus their evidence pointer and topic. A downstream conclusion may consume a proposition only under rules appropriate to that status; unsupported status promotion is rejected or surfaced as uncertainty.

#### Procedure

1. Split the candidate reasoning product into material propositions.
2. Assign each proposition a status and evidence pointer.
3. Check whether downstream conclusions use each status permissibly.
4. Flag any inference or hypothesis presented as direct fact.
5. Downgrade, relabel, remove, or seek evidence for the offending proposition.

#### Guardrails

- Mandatory even on strong models: the distinction between source fact, inference, framing, and hypothesis.
- Conflict/precedence: Direct source evidence outranks an unlabeled model inference; A domain policy may define finer statuses but may not silently promote unsupported content.
- Stop or fail when: If a decision-critical proposition has no defensible status or evidence pointer, it cannot support the conclusion.

Full package and provenance: [`epistemic-status-gating`](../../upgradeables/truth-grounding/epistemic-status-gating/UPGRADEABLE.md).

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

Full package and provenance: [`drift-suppression`](../../upgradeables/drift-control/drift-suppression/UPGRADEABLE.md).

### C — Fail-Closed Abstention

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
