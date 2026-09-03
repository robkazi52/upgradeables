# Planning, decision, creative, and reasoning work

Research track F for the v0.3 selection ontology. Sources were reviewed on
2026-09-03.

## Scope and evidence labels

This note covers planning, trade-off analysis, architecture and design,
ideation, hypothesis generation and testing, logical constraints, and spatial
reasoning. It also examines when branching, critique, external validation, and
falsification are justified.

- **Evidence** means a finding stated or directly supported by a linked paper
  or primary provider document.
- **Synthesis** means a proposed resolver category or selection rule. It is not
  evidence that an Upgradeable improves the task.
- Benchmark results describe bounded experimental settings. They do not prove
  equivalent reliability in arbitrary real-world decisions.

## Source-grounded findings

### Planning is constraint coordination, not merely a long answer

**Evidence.** PlanBench evaluates plan generation and reasoning about actions
and change in formal Blocksworld and Logistics domains, where actions have
preconditions and effects and plans can be checked for validity. [F1]

**Evidence.** TravelPlanner adds real-world information gathering, tools,
commonsense requirements, and multiple explicit constraints. Its reported
failure patterns include losing the task, choosing the wrong tools, and failing
to track constraints across a complete plan. [F2]

**Synthesis.** `planning` should require a goal, current state, constraints,
available actions/resources, and a completion condition. A prose roadmap,
formal executable plan, and adaptive replanning loop are distinct task forms.
The presence of many steps alone should not trigger agentic execution.

### Branching helps on search-shaped problems but has a cost

**Evidence.** Tree of Thoughts evaluates deliberate exploration, state
evaluation, lookahead, and backtracking on Game of 24, creative writing, and
crosswords. The gains are demonstrated on tasks where early choices materially
affect later feasibility. [F3]

**Evidence.** Anthropic recommends increasing workflow complexity only when the
task warrants the latency and cost, and recommends parallelization when work is
independent or multiple attempts materially improve confidence. [F4]

**Synthesis.** Branching is a conditional mechanism, not a generic reasoning
upgrade. Promote it when the search space has consequential forks, a branch can
be evaluated, and the task ceiling permits the cost. Otherwise use a single
candidate plus a bounded check. A branch budget and pruning rule should be
explicit.

### Revision is only as good as its feedback signal

**Evidence.** Self-Refine demonstrates a generate-feedback-refine loop across
several generation and reasoning tasks without additional training. [F5]

**Evidence.** CRITIC reports that tool-grounded feedback can improve correction
and warns that self-verification without reliable external feedback can be
inefficient or unreliable. Its tools include search and code execution suited
to the property being checked. [F6]

**Synthesis.** Separate `draft_revision` from `falsification`. Revision asks how
to improve an output; falsification asks what observable result would show a
candidate is wrong. Prefer external or deterministic checks when available.
Repeated self-critique by the same model is not independent validation.

### Constraint feasibility and optimality are separate

**Evidence.** ZebraLogic generates logic-grid constraint-satisfaction problems
with controllable search complexity and reports declining accuracy as problem
complexity grows, including when additional inference compute is used. [F7]

**Evidence.** ConstraintBench separately measures whether a generated solution
satisfies every constraint and whether a feasible solution reaches a
solver-proven optimum. Its results show that feasibility and optimality can
diverge. [F8]

**Synthesis.** A constraint task must check feasibility before ranking or
optimizing solutions. The resolver should distinguish hard constraints, soft
preferences, and objectives. It should prefer a deterministic verifier or
solver when one is available and authorized.

### Spatial reasoning needs relational state, not generic verbosity

**Evidence.** StepGame tests multi-hop spatial relations expressed in varied
language and includes irrelevant or redundant information to measure robust
relation composition. [F9]

**Synthesis.** Spatial tasks should promote an explicit relational map,
coordinate/frame consistency, and inverse-relation checks. They should not
automatically promote broad alternative search unless the task also contains
route or configuration choices.

### Divergence and convergence are different creative phases

**Evidence.** Research comparing models and humans on divergent association and
creative-writing tasks treats originality/diversity as constructs distinct from
ordinary correctness. It also cautions that performance on one creativity test
does not establish a general creative faculty. [F10]

**Synthesis.** `creative-ideation` should optimize breadth or novelty before
selection. `concept-selection` should then evaluate candidates against explicit
criteria. Mixing the phases too early creates premature convergence; refusing
to converge creates endless ideation.

### Missing information is a reasoning state, not permission to guess

**Evidence.** QuestBench formalizes underspecified logic, planning, and math
problems where one missing variable assignment can be obtained by one question.
Models that can solve the complete problem may still fail to identify the
minimal clarification needed. [F11]

**Synthesis.** Add `missing_required_information` as an observable state. The
resolver should choose among asking a minimal question, returning conditional
branches, or abstaining. It should not disguise an absent premise as uncertainty
inside an otherwise definitive plan.

## Proposed normalized task archetypes

The table below is **synthesis** for deterministic discovery.

| Archetype | User goal | Typical output | Boundary |
|---|---|---|---|
| `plan-generation` | Choose an ordered path from a current state to a goal | steps, dependencies, checkpoints | Does not execute the plan |
| `plan-validation` | Determine whether a proposed plan is feasible and complete | violated constraints, gaps, corrected plan | Validate before optimizing |
| `adaptive-replanning` | Revise a plan after observed state changes | updated state and remaining plan | Requires explicit observations/state |
| `task-decomposition` | Divide a goal into manageable work units | task graph, ownership, interfaces | Decomposition does not imply parallelism |
| `tradeoff-analysis` | Compare alternatives across competing criteria | criterion-by-option analysis and sensitivities | Does not choose without decision authority |
| `decision-recommendation` | Recommend an option for an accountable decision-maker | recommendation, reasons, uncertainties | Recommendation is not external action |
| `architecture-design` | Define components, interfaces, and quality trade-offs | design or decision record | Does not authorize implementation |
| `creative-ideation` | Generate materially distinct possibilities | candidate set grouped by concept | Delay pruning until intended breadth is reached |
| `concept-selection` | Narrow candidates against criteria | shortlist or selected concept | Preserve reasons and rejected constraints |
| `hypothesis-generation` | Propose testable explanations or mechanisms | hypotheses with predictions | Plausibility is not evidence |
| `hypothesis-testing` | Seek observations that discriminate candidates | tests, results, supported/rejected status | Prefer disconfirming evidence and external checks |
| `logical-constraint-solving` | Find an assignment satisfying formal or natural-language rules | assignment plus constraint check | Feasibility precedes optimality |
| `spatial-relational-reasoning` | Infer relations, paths, or layouts | relation/coordinate map and conclusion | Preserve frame and inverse relations |
| `counterfactual-analysis` | Evaluate what changes under an altered assumption | delta from baseline and affected conclusions | Change one declared assumption at a time |
| `argument-evaluation` | Test whether claims follow from premises and evidence | supported, contradicted, or unresolved claims | Rhetorical fluency is not validity |

### Cross-archetype distinctions

**Synthesis.** Preserve these boundaries:

- `task-decomposition` describes structure; `plan-generation` adds ordering,
  dependencies, resources, and goal reachability.
- `tradeoff-analysis` makes criteria and tensions visible;
  `decision-recommendation` applies priorities and returns a preferred option.
- `architecture-design` is a domain-specialized decision task with interface
  and quality-attribute consequences.
- `creative-ideation` is divergent; `concept-selection` is convergent. A task
  can request both, but should preserve a phase boundary.
- `hypothesis-generation` produces testable candidates;
  `hypothesis-testing` seeks discriminating evidence. It should be possible to
  end with all candidates unresolved or rejected.
- `logical-constraint-solving` and `spatial-relational-reasoning` use explicit
  state models, but spatial reasoning has frame, direction, and composition
  failures that deserve separate signals.
- Planning and reasoning do not imply hidden chain-of-thought disclosure. The
  required artifacts are inspectable states, criteria, checks, and conclusions.

## Recurring failure patterns

These are **synthesis categories** informed by the sources above.

| Failure-mode candidate | Observable signal | Selection implication |
|---|---|---|
| `goal-drift` | Plan or analysis optimizes a different goal | Lock goal and completion condition |
| `constraint-omission` | One or more hard constraints are absent from evaluation | Create a constraint ledger and verify all entries |
| `preference-constraint-confusion` | A preference is treated as mandatory, or vice versa | Type each criterion as hard, soft, or objective |
| `feasibility-optimality-confusion` | High-scoring infeasible option is recommended | Check feasibility before ranking |
| `premature-commitment` | First plausible plan/hypothesis is adopted | Generate alternatives when ambiguity and stakes justify them |
| `tunnel-vision` | Evidence is interpreted only through the favored candidate | Seek discriminating or disconfirming observations |
| `over-branching` | Candidate count grows without useful discrimination | Set branch budget, scoreability, and pruning rule |
| `branch-contamination` | Assumptions or facts leak between alternatives | Give branches explicit state and reconcile only at synthesis |
| `unsupported-scoring` | Numeric rankings lack a defined scale or evidence | Use ordinal comparison or explicit rubric unless data supports precision |
| `self-validation-loop` | Generator repeatedly endorses its own answer | Add external evidence, deterministic check, or independent review |
| `revision-without-progress` | Iterations rephrase rather than repair a failed criterion | Track failed checks and stop after bounded attempts |
| `missing-premise-guessing` | Required unknown is silently invented | Ask minimal clarification or return conditional result |
| `spatial-frame-drift` | Left/right, reference origin, or viewpoint changes mid-solution | Lock coordinate/reference frame |
| `relation-inversion` | Inverse or transitive relation is applied incorrectly | Check reciprocal and composed relations |
| `counterfactual-leakage` | Baseline facts are incorrectly changed with the counterfactual | Record baseline, intervention, and propagated effects separately |
| `endless-ideation` | More ideas are generated after criteria are sufficient | Switch explicitly to convergence or stop |
| `early-convergence` | Near-duplicate first ideas crowd out distinct concepts | Separate divergent generation from evaluation |
| `weak-stopping-rule` | Search or revision continues without a success/failure bound | Define evidence, branch, iteration, and time budgets |

## Environment modifiers

The following are **synthesis recommendations**.

| Modifier | Resolver effect |
|---|---|
| `goal_explicit` | Enables direct planning; otherwise request the intended end state |
| `current_state_known` | Enables executable planning rather than a generic roadmap |
| `hard_constraints_present` | Require feasibility ledger and complete validation |
| `soft_preferences_present` | Promote trade-off analysis without treating preferences as vetoes |
| `objective_function_present` | Permit optimization after feasibility is established |
| `missing_required_information` | Promote minimal clarification, conditional branches, or abstention |
| `plan_execution_requested` | Separately permits action; planning alone remains read-only |
| `state_changes_during_task` | Promote adaptive replanning and explicit observations |
| `deterministic_verifier_available` | Prefer tool-based validation for plans/constraints |
| `external_evidence_available` | Promote grounded critique and hypothesis discrimination |
| `high_stakes` | Raise evidence, alternative, validation, and human-review requirements |
| `reversible_decision` | Permits lighter exploration than an irreversible commitment |
| `time_or_cost_limited` | Tighten branch and iteration budgets |
| `diversity_requested` | Promote divergent generation and duplicate suppression |
| `single_best_answer_requested` | Add convergence criteria after any justified exploration |
| `spatial_frame_defined` | Lock frame; absence may require clarification |
| `multi_step_relations` | Promote explicit relation state and composition checks |
| `counterfactual_requested` | Preserve a baseline and isolate the intervention |
| `parallel_workers_available` | Enables independent alternatives/checks but does not require them |
| `human_decision_owner` | Keep recommendation and final commitment separate |

## Complexity implications

This table is **synthesis**, consistent with evidence that search, critique, and
agent loops are task-dependent rather than universal.

| Task shape | Default ceiling | Conditions that raise it | Usually excessive |
|---|---|---|---|
| Simple comparison with explicit criteria | L0-L1 | Consequential or conflicting evidence | Search trees and multiple agents |
| Short deterministic plan | L1 | Coupled constraints or uncertain state | Evaluator loops without a checkable criterion |
| Multi-constraint plan | L2-L3 | Tool retrieval, dynamic state, high stakes | Unbounded alternatives |
| Architecture decision | L2-L3 | Multiple systems, irreversible migration, weak evidence | Implementation agents before decision approval |
| Brainstorm | L1-L2 | Need for independent domains or very broad coverage | Validators during early divergence |
| Hypothesis generation | L1-L2 | Expensive consequences or broad evidence corpus | Treating every hypothesis as an agent task |
| Hypothesis testing | L2-L4 | Adaptive experiments/tools or long feedback loops | Self-critique as sole verifier |
| Small logic/spatial problem | L1-L2 | Many coupled constraints or long relation chains | Multi-agent orchestration |
| Large constraint search | L3-L4 | Solver/tool loop and adaptive recovery | Pure prose reasoning when a verifier exists |
| Multiple independent design workstreams | L3-L5 | True separability plus synthesis need | L5 merely because workers are available |

Suggested raising sequence:

1. Add explicit state and constraints.
2. Add one suitable validator.
3. Add a bounded alternative only when the first choice is consequential or
   difficult to evaluate locally.
4. Add a tool loop when state must be gathered or tested adaptively.
5. Add parallel workers only when the work is separable and synthesis is
   specified.

## Falsification and branch-control recommendations

All items here are **synthesis**.

- For every hypothesis, record at least one expected observation and one result
  that would count against it.
- Prefer tests that discriminate among candidates, not evidence compatible with
  all of them.
- Keep candidate generation, evaluation, and final selection as named phases.
- Use a branch budget based on task ceiling; L0-L1 normally permits zero or one
  alternative check, while L3 may justify several scored candidates.
- Give each branch its own assumptions, constraints, evidence, and failure
  status to prevent contamination.
- Prune only with a stated failed constraint, inferior criterion result, or
  budget rule.
- Allow `no feasible option`, `insufficient information`, and `all hypotheses
  unresolved` as legitimate outcomes.
- Treat external observations, executable tests, solvers, and source evidence
  as stronger correction signals than ungrounded self-evaluation.

## Ontology recommendations for synthesis

1. Use separate fields for `goal`, `current_state`, `hard_constraints`,
   `soft_preferences`, `objective`, `actions`, and `completion_evidence`.
2. Classify divergence, convergence, validation, and execution as phases that
   can modify an archetype rather than as synonyms for “reasoning.”
3. Keep `planning` distinct from `plan_execution`; authority must not flow from
   the former to the latter.
4. Promote explicit-state mechanisms before branching mechanisms.
5. Tie alternative search to observable ambiguity, coupled constraints, or
   high-cost commitment—not to generic requests to “think harder.”
6. Apply the complexity ceiling before selecting Multiverse, QMS, or supervisor
   patterns.
7. Require a verifier interface when plans or constraint assignments are
   mechanically checkable.
8. Pair creative breadth with duplicate suppression, then switch to a separate
   criteria-based convergence phase.
9. Treat falsification as a search for candidate-discriminating evidence, not a
   generic critique paragraph.
10. Represent missing premises explicitly and prefer the smallest useful
    clarification question.

## Sources

- **[F1]** Valmeekam et al., [PlanBench: An Extensible Benchmark for Evaluating Large Language Models on Planning and Reasoning about Change](https://arxiv.org/abs/2206.10498), 2022.
- **[F2]** Xie et al., [TravelPlanner: A Benchmark for Real-World Planning with Language Agents](https://arxiv.org/abs/2402.01622), 2024.
- **[F3]** Yao et al., [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601), 2023.
- **[F4]** Anthropic, [Building effective agents](https://www.anthropic.com/engineering/building-effective-agents), 2024.
- **[F5]** Madaan et al., [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651), NeurIPS 2023.
- **[F6]** Gou et al., [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://arxiv.org/abs/2305.11738), ICLR 2024.
- **[F7]** Lin et al., [ZebraLogic: On the Scaling Limits of LLMs for Logical Reasoning](https://arxiv.org/abs/2502.01100), 2025.
- **[F8]** Tso et al., [ConstraintBench: Benchmarking LLM Constraint Reasoning on Direct Optimization](https://arxiv.org/abs/2602.22465), 2026.
- **[F9]** Shi, Zhang, and Lipani, [StepGame: A New Benchmark for Robust Multi-Hop Spatial Reasoning in Texts](https://arxiv.org/abs/2204.08292), AAAI 2022.
- **[F10]** Bellemare-Pepin et al., [Divergent Creativity in Humans and Large Language Models](https://arxiv.org/abs/2405.13012), 2024.
- **[F11]** Gandhi et al., [QuestBench: Can LLMs ask the right question to acquire information in reasoning tasks?](https://arxiv.org/abs/2503.22674), 2025.
