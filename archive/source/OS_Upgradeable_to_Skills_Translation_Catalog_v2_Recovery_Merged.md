# OS Philosophy and Upgradeable-to-Skill Translation Catalog

Version: 2.0 — Historical Recovery Merged
Date: 2026-09-03
Purpose: Source specification for a frontier LLM to translate the user's OS, CAF, and Upgradeable architecture into modern Agent Skills / SKILL.md packages.

IMPORTANT:
- This is a translation source, not a set of finished Skills.
- Preserve the conceptual distinctions among OS, Upgradeable, Behavior Gene, Core, Loader, Orchestrator, Validator, and domain package.
- Do not collapse the system into one giant Skill.
- Do not invent definitions for labels marked "definition not fully recovered."
- Translate conceptual metaphors into explicit, implementable behavior. Example: Teleport Bus means explicit state routing, not a hidden communication channel.

======================================================================
PART I. CORE PHILOSOPHY OF THE OS
======================================================================

1. THE LLM IS THE REASONING SUBSTRATE; THE OS IS THE OPERATING LAYER
The model supplies general intelligence. The OS supplies task identity, behavioral rules, routing, state, domain structure, evidence handling, safety, and quality control.
The OS should shape how the model works without pretending to replace the model's native reasoning.

2. LAYERED, COMPONENT-BASED, NONMONOLITHIC DESIGN
The system should be decomposed into swappable, versionable components.
Canonical hierarchy used in prior work:

Global OS
  -> Project / Kernel OS
    -> Per-chat or Task OS Shell
      -> Behavior Genes
      -> Reasoning / Singularity Cores
      -> Upgradeables
      -> Loader / State mechanisms
      -> Orchestrator
      -> Validation / QMS layers
      -> Output

No single prompt should contain every behavior, domain rule, evidence source, and safety mechanism.

3. MINIMUM NECESSARY CONTEXT
Load only what the current task needs.
The OS should first identify the task and relevant modules, then load deeper instructions, references, tools, examples, or Cores only when needed.
This was expressed in prior work as scoped loading, loader sequencing, task-set lock-in, and micro-scaffolding.
This closely maps to modern progressive-disclosure Skill design.

4. SEPARATE BEHAVIOR FROM KNOWLEDGE
Behavior Gene:
- Defines how to reason and write.
- Contains always-do rules, avoid rules, logic pattern, evidence handling, and output shape.

Core:
- Holds high-density domain knowledge representations.
- Contains reasoning maps, domain anchors, patterns, templates, data requirements, and evidence architecture.

Upgradeable:
- Adds a cross-cutting capability or control behavior that can be reused across tasks, Genes, Cores, and OS layers.

Do not use a Core as a style prompt.
Do not use a Gene as a knowledge dump.
Do not use an Upgradeable as a substitute for the entire OS.

5. ORCHESTRATION OVER PROMPT ACCUMULATION
The system should decide:
- Which modules are relevant.
- In what order they load.
- Which module has authority when instructions conflict.
- When a module should deactivate.
- Whether the task needs a behavior Gene, a knowledge Core, a validator, or a full domain OS.

6. TASK AND MODE STABILITY
Once the task is identified, preserve:
- Goal
- Scope
- Mode
- Constraints
- Source boundaries
- Output contract
- Current subtask
- Next step

Do not allow incidental text or intermediate reasoning to silently redefine the task.

7. TRUTH-FIRST, SOURCE-GROUNDED OPERATION
The OS should prefer:
1. Explicit source-supported facts.
2. Valid evaluation or inference clearly separated from facts.
3. Framing or synthesis that does not alter factual meaning.
4. Hypothesis only when explicitly permitted and labeled.

Do not invent missing facts, citations, source content, patient details, policies, measurements, or external evidence.

8. SEMANTIC PHASE SEPARATION
Prior work used truth / reasoning phases:
- Lf: factual
- Le: evaluative
- Lp: framing / paper or presentation construction
- Lh: hypothetical

The system should not allow hypothetical content to leak into factual claims.
Phase boundaries should be explicit when risk is meaningful.

9. CONTROLLED DRIFT, NOT ZERO CREATIVITY
Some tasks require exact fidelity. Others require synthesis.
The OS distinguishes:
- Zero-drift zones: quotes, citations, definitions, source facts, exact constraints.
- Micro-drift corridors: bounded paraphrase, synthesis, organization, analogy, or stylistic variation.
- Wider reasoning space: architecture, ideation, exploratory design, when risk is low.

10. MULTI-TRUTH GATING
Important conclusions should not rest on one fragile reasoning path.
Where appropriate, use multiple independent anchors, cross-checks, or perspectives.
When crucial claims disagree, resolve the conflict or abstain rather than force a conclusion.

11. RISK-SCALED REASONING
Reasoning depth, verification, and safety gates should increase with consequence and uncertainty.
Low-risk tasks should not be burdened with maximal machinery.
High-risk tasks should receive stronger truth checks, redundancy, and veto authority.

12. FAIL-CLOSED WHEN REQUIRED
When a required fact, source, or integrity condition cannot be verified:
- Omit the unsupported claim.
- Mark the uncertainty.
- Ask only when asking is appropriate to the operating environment.
- Otherwise choose the safest bounded completion.
Do not fill gaps with plausible-sounding content.

13. LOCAL REPAIR BEFORE GLOBAL REWRITE
When an output has a localized failure:
- Identify the faulty region.
- Repair only that region when possible.
- Preserve correct material and locked decisions.
Use full regenerative rewrite only when the architecture or global coherence is broken.

14. BOUNDED ITERATION
Reflection and refinement should have a purpose and stopping rule.
Use "reflect -> test -> revise" only while it improves task quality.
Avoid endless self-reflection, identity narratives, or recursive loops.

15. DESIGN AND EXECUTION ARE DIFFERENT MODES
Architect / Design mode:
- Can use deeper planning, multiverse exploration, QMS, Cosmic reasoning, and broader option search.

Execution mode:
- Uses a tighter Atomic / Subatomic / Micro path.
- Prioritizes fidelity, safety, consistency, and direct completion.

The accepted hybrid principle was:
- Maximum useful power for planning.
- Maximum practical safety for execution.
- Supervisor-controlled switching.

16. COMPOSABILITY
Small reusable modules should combine to solve larger tasks.
A strong system should be able to activate several Upgradeables without requiring a bespoke monolith for every use case.

17. VERSIONABILITY AND SWAPPABILITY
Genes, Cores, Upgradeables, and OS shells should be independently replaceable.
A new version of one module should not require rewriting the entire architecture.

18. EXPLICIT STATE OVER HIDDEN ASSUMPTIONS
State should be represented in visible structures such as StateBlock, source maps, task locks, or snapshots.
Do not rely on an imagined hidden pointer, hidden memory channel, or implicit cross-module awareness.

19. FUTURE-MODEL SCALING
The OS should remain useful as frontier models gain stronger native reasoning.
Stronger models should receive:
- Less unnecessary scaffolding.
- More dynamic depth allocation.
- Wider reasoning only where safe.
- Persistent integrity and state controls.
The OS should become thinner and more supervisory as native model capability rises.

20. QUALITY SYSTEMS SHOULD VALIDATE, NOT COMPETE WITH THE TASK
QMS and safety validators should inspect, score, veto, or request repair.
They should not become uncontrolled parallel authors that introduce new unsupported content.

======================================================================
PART II. TARGET SKILL TRANSLATION CONTRACT
======================================================================

A frontier LLM translating this catalog into Agent Skills should classify each item as one of:

A. Standalone Skill
Use when the capability has a distinct trigger, procedure, and output behavior.

B. Parent Skill with modes
Use when several variants share the same workflow and differ mainly in validation strategy.
Example: Parallel-QMS variants can be one parent Skill with named modes.

C. Reference module
Use when the item is primarily knowledge, policy, a reasoning map, or a reusable schema.

D. Validator / guard Skill
Use when the item checks output rather than generating primary content.

E. Orchestrator Skill
Use when the item selects, sequences, or coordinates other Skills.

F. Domain Plugin / Skill bundle
Use for a whole domain OS such as CAF, Research OS, or Paper-Author OS.

For each generated Skill, produce:

1. name
- Lowercase, hyphenated, concise.
- Preserve the original concept in metadata if the Skill name must be normalized.

2. description
- Explain what the Skill does.
- Explain exactly when it should activate.
- Include activation keywords and exclusions.

3. purpose

4. scope

5. trigger conditions

6. non-trigger conditions

7. required inputs / state

8. always-do rules

9. never-do / avoid rules

10. step-by-step procedure

11. interaction rules
- What it may call or combine with.
- What has priority in a conflict.
- Whether it is generator, validator, router, or state manager.

12. failure handling

13. output contract

14. optional references/
- Detailed policy
- Domain rules
- Examples
- Schemas
- Test cases

15. optional scripts/
- Deterministic checks
- Scoring
- File parsing
- Validation
- State serialization

16. tests
- Positive trigger examples
- Negative trigger examples
- Conflict tests
- Long-context tests
- Hallucination / unsupported-claim tests
- Safety-veto tests where relevant

Current Agent Skills packaging target:
- Minimum package: SKILL.md
- Optional: scripts/, references/, assets/
- Use progressive disclosure.
- Keep the primary SKILL.md concise and move deep reference material out of the main instructions.
- The modern Agent Skills specification recommends the full instruction body remain below roughly 5,000 tokens and the main file below 500 lines.
- The description is a primary activation mechanism, so it must state both function and trigger.

======================================================================
PART III. TIER 1: CORE RELIABILITY UPGRADEABLES
======================================================================

T1-01. Micro-Scaffolding
Suggested Skill: micro-scaffolding
Type: Control / reasoning scaffold
Purpose: Instantiate only the minimum temporary structure needed to complete the current subtask correctly.
Trigger: Multi-step reasoning, transformation, high-constraint writing, or situations where the model is likely to lose a requirement.
Behavior:
- Create small task-local checkpoints.
- Preserve goal, constraints, evidence boundary, and next step.
- Remove or stop using scaffolds when no longer necessary.
Avoid:
- Huge visible planning structures for simple tasks.
- Permanent context bloat.
Interaction: Works with Task-Set Lock-In, Working-Memory Cues, Drift Suppression, QMS.

T1-02. Drift Suppression
Suggested Skill: drift-suppression
Type: Guard
Purpose: Prevent gradual movement away from the user's actual goal, constraints, terminology, or evidence.
Trigger: Long conversations, multi-pass work, iterative design, repeated revisions.
Behavior:
- Re-anchor to explicit goal and locked constraints.
- Detect newly introduced assumptions.
- Remove irrelevant branches.
Avoid: Suppressing legitimate, user-requested scope expansion.

T1-03. Clarification Gateway / Clarification-First
Suggested Skill: clarification-gateway
Type: Router / guard
Purpose: Decide whether ambiguity materially blocks correct execution.
Trigger: Missing required variables, conflicting instructions, ambiguous task identity.
Behavior:
- Distinguish resolvable ambiguity from truly blocking ambiguity.
- Ask only when necessary in environments that permit clarification.
- Otherwise make the narrowest labeled assumption or bounded completion.
Note: In environments with a "best effort, do not ask" rule, this becomes an assumption-selection gate rather than a question generator.

T1-04. Grounding / No-Invention
Suggested Skill: grounding-no-invention
Type: Safety / truth guard
Purpose: Prevent fabricated facts, citations, source claims, measurements, policies, or records.
Trigger: Any task grounded in supplied documents, structured data, external facts, or high-stakes evidence.
Behavior:
- Separate provided data from interpretation.
- Do not fill missing fields.
- Mark uncertainty.
- Fail closed where the missing information is essential.

T1-05. Mode Lock-In
Suggested Skill: mode-lock-in
Type: State / control
Purpose: Preserve the selected operating mode.
Trigger: Tasks that can accidentally switch between design, execution, hypothetical, factual, critique, drafting, or other modes.
Behavior:
- Store active mode.
- Reject incidental mode changes.
- Change only on explicit task evidence or supervisor instruction.

T1-06. Task-Set Lock-In
Suggested Skill: task-set-lock-in
Type: State / control
Purpose: Preserve the actual task definition across long or branching work.
State to lock:
- Goal
- Deliverable
- Constraints
- Terminology
- Source boundaries
- Current subtask
- Completion criteria

T1-07. Loader Sequencing
Suggested Skill: loader-sequencing
Type: Orchestrator
Purpose: Load only relevant Genes, Cores, Upgradeables, references, and tools in the correct order.
Trigger: Any modular OS with multiple available capabilities.
Behavior:
1. Identify task.
2. Load task shell.
3. Load required Behavior Genes.
4. Load required Cores.
5. Load only necessary Upgradeables.
6. Load references/resources on demand.
7. Activate validators before final commitment.
Avoid: Loading the entire library at session start.

T1-08. Placeholder Suppression
Suggested Skill: placeholder-suppression
Type: Output guard
Purpose: Prevent unfinished markers from leaking into final work.
Trigger: Draft generation, templates, artifact creation, multi-stage composition.
Detect:
- TODO
- TBD
- [insert]
- dummy values
- unresolved variable names
- empty required sections
Behavior: Resolve, omit, or explicitly label unresolved material before final output.

T1-09. Working-Memory Cues
Suggested Skill: working-memory-cues
Type: State helper
Purpose: Maintain lightweight reminders of the current objective and constraints.
Trigger: Long-context work or tasks with many simultaneous requirements.
Behavior: Use compact internal or explicit state cues rather than repeatedly reloading full instructions.

T1-10. Safe Rewrite Logic
Suggested Skill: safe-rewrite
Type: Editing guard
Purpose: Rewrite text without silently changing locked facts, meaning, citations, or constraints.
Trigger: Paraphrasing, polishing, format conversion, tone change.
Behavior:
- Preserve factual atoms.
- Change only requested dimensions.
- Recheck names, numbers, dates, quotes, and citations.

======================================================================
PART IV. TIER 2: ADVANCED REASONING, STATE, AND REPAIR UPGRADEABLES
======================================================================

T2-01. Bounded ExIt
Suggested Skill: bounded-exit
Type: Refinement controller
Purpose: Run a bounded evaluate-and-improve loop until quality is sufficient or further iteration has diminishing value.
Core loop:
1. Evaluate current output against locked goals.
2. Identify highest-value defect.
3. Repair.
4. Re-evaluate.
5. Stop when threshold or iteration budget is reached.
Avoid: Endless recursion or self-reflection.

T2-02. Structured Refinement Cycles
Suggested Skill: structured-refinement
Type: Refinement controller
Purpose: Make revision systematic rather than ad hoc.
Behavior:
- Separate factual correction, structural repair, style repair, and final validation.
- Preserve accepted decisions across cycles.

T2-03. Regenerative Rewrite
Suggested Skill: regenerative-rewrite
Type: Editing engine
Purpose: Rebuild an output when local repair cannot fix broken global structure or coherence.
Trigger:
- Architecture is wrong.
- Multiple sections conflict.
- Source mapping is fundamentally broken.
Non-trigger: One bad sentence or localized error.

T2-04. Micro-Repair
Suggested Skill: micro-repair
Type: Editing engine
Purpose: Correct the smallest faulty unit while preserving correct surrounding work.
Trigger: Local contradiction, unsupported claim, awkward transition, missing requirement, small formatting failure.
Priority: Preferred before Regenerative Rewrite.

T2-05. Multi-Layer Consistency
Suggested Skill: multi-layer-consistency
Type: Validator
Purpose: Check that system, project, task, Gene, Core, evidence, and output layers do not contradict each other.
Trigger: Complex composed workflows.

T2-06. Progressive Mode Shaping
Suggested Skill: progressive-mode-shaping
Type: Control
Purpose: Gradually narrow a broad exploratory mode into a precise execution mode as decisions become locked.
Example:
Explore -> compare -> choose -> plan -> execute -> validate.

T2-07. Stable Long-Context / Long-Context Coherence
Suggested Skill: stable-long-context
Type: State / integrity
Purpose: Preserve decisions, terminology, constraints, and source meaning across large context windows.
Behavior:
- Periodically refresh compact state.
- Distinguish current decisions from obsolete branches.
- Prevent old alternatives from reappearing as active requirements.

T2-08. Working-Memory Lock-In
Suggested Skill: working-memory-lock-in
Type: State manager
Purpose: Lock the most task-critical information in a compact active state.
Known use: Goal can be locked verbatim when exact fidelity is required.

T2-09. StateBlock
Suggested Skill: stateblock
Type: State schema
Purpose: Maintain an explicit task-state object.
Recommended fields:
- Goal
- Current phase
- Subtasks
- Constraints
- Source boundary
- Decisions
- Open uncertainties
- Active modules
- Completed work
- Next step

T2-10. SMSE — Sequential Memory State Engine
Suggested Skill: sequential-memory-state-engine
Type: State update mechanism
Recovery status: Exact expansion recovered from December 3, 2025 OS work.
Recovered function: StateBlock update mechanism; also used for chunked SourceState intake preserving boundaries and provenance.
Behavior:
- Update state incrementally.
- Preserve source chunk boundaries and provenance.
- Prevent new input from overwriting locked state without reconciliation.

T2-11. SelfBlock Auto-Update
Suggested Skill: selfblock-auto-update
Type: State automation
Purpose: Automatically maintain working state as tasks progress.
Behavior:
- Record completed decisions.
- Update current subgoal.
- Retire obsolete branches.
- Preserve constraints.
Caution: State updates must reflect task work, not build an identity or self-story.

T2-12. WRL / ReflectOS
Suggested Skill: reflectos
Type: Bounded QA loop
Recovered expansion: Work Reflection Loop OS / ReflectOS.
Purpose: Goal-anchored "reflect -> test -> revise" loop.
Procedure:
1. Recheck session goal and current subgoal.
2. Compare output to requirements.
3. Audit contradictions, missing requirements, and risk.
4. Choose accept, revise, ask/escalate when permitted.
5. Update StateBlock.
Constraint: Correct process errors only; do not invent new facts.

T2-13. OCG
Suggested Skill: ocg
Type: Unresolved legacy Upgradeable
Definition: Not fully recovered from available history.
Instruction to translator: Preserve label in a legacy appendix. Do not invent expansion or behavior until source material is recovered.

T2-14. ITFC — Historical Acronym Collision
Type: Legacy namespace collision
Recovery status: Two historical uses were identified; do not merge them into one Skill.

ITFC-A: Image Text Fidelity Capture
Suggested Skill: image-text-fidelity-capture
Recovered purpose: Extract text from images faithfully; do not infer or hallucinate missing text; rebuild structure only from visible evidence.

ITFC-B: Intent/Task Framing Controller
Suggested Skill: intent-task-framing-controller
Recovery status: Name recovered as a separate architecture use, but the full original specification was not re-exposed in this pass.
Instruction to translator: Keep the two ITFC senses in separate namespaces and preserve legacy_acronym metadata.

T2-15. ECL / Drift Sink
Suggested Skill: drift-sink
Type: Drift-control concept
Recovered name: ECL / Drift Sink.
Exact expansion and full original definition: Not fully recovered.
Translation guidance: Preserve as a candidate drift-absorption / context-cleanup concept only after recovering original source. Do not manufacture an acronym expansion.

T2-16. ABF — Activation-Budget Funnel
Suggested Skill: activation-budget-funnel
Type: Context / activation-budget controller
Recovery status: Historical expansion and operating sequence recovered.
Purpose: Prevent active-context overload by staging source/module activation rather than allowing raw retrieval and decision-making to compete in the same step.
Recovered sequence:
1. Retrieve.
2. Quote / capture evidence.
3. Index into compact state.
4. Transform.
5. Write.
6. Verify.
Recovered operating heuristic:
- Keep roughly <=5–7 active pulls in the live workspace.
- Prefer progressive disclosure and staged activation.
- Move verified facts into compact indexed state before higher-level synthesis.

T2-17. Forethought / Checkpoints
Suggested Skill: forethought-checkpoints
Type: Planning control
Purpose: Before irreversible or high-cost steps, predict likely downstream failures and establish a checkpoint.
Behavior:
- Anticipate dependency.
- Verify prerequisite.
- Commit.
- Check result before continuing.

T2-18. Bidirectional Consistency
Suggested Skill: bidirectional-consistency
Type: Validator
Purpose: Verify that reasoning works forward from evidence to conclusion and backward from conclusion to required evidence.
Trigger: Complex causal, logical, quantitative, or evidence-based reasoning.

T2-19. Anti-Tunnel Vision
Suggested Skill: anti-tunnel-vision
Type: Reasoning guard
Purpose: Prevent premature fixation on one interpretation, cause, plan, or solution.
Behavior:
- Generate a small bounded alternative set.
- Test the favored path against at least one plausible competitor.
- Collapse quickly when evidence clearly favors one path.

T2-20. External State Automation
Suggested Skill: external-state-automation
Type: State persistence interface
Purpose: Serialize important task state to files, memory, databases, project documents, or other explicit storage when the environment supports it.
Caution: Never claim persistence unless the actual environment provides it.

T2-21. Adapter-First Experimentation
Suggested Skill: adapter-first-experimentation
Type: Architecture / experimentation
Purpose: Test new capabilities as detachable modules before rewriting the base OS.
Principle:
- Prototype as an adapter.
- Evaluate.
- Promote to a core/global rule only after demonstrated value.
This protects the base system from unstable experimental changes.

======================================================================
PART V. REASONING-SCALE STACK
======================================================================

STACK: Subatomic -> Atomic -> Nano -> Micro -> QMS -> Cosmic

This stack was used as a depth hierarchy. A translator may implement it as one "reasoning-scale-controller" Skill with modes rather than six independent Skills.

RS-01. Subatomic
Suggested mode: subatomic
Purpose: Smallest local reasoning operations.
Use for:
- Individual fact checks
- Local relation checks
- One constraint
- One sentence-level decision
Execution should be fast and narrow.

RS-02. Atomic
Suggested mode: atomic
Purpose: Combine small verified units into a coherent local inference or action.
Use for:
- Paragraph logic
- Local decision
- Small procedure
- Compact transformation

RS-03. Nano
Suggested mode: nano
Purpose: Intermediate micro-structure between Atomic and broader Micro scaffolding.
Original detailed specification was not fully recovered.
Translator should preserve it as a lightweight intermediate scale rather than inventing elaborate semantics.

RS-04. Micro
Suggested mode: micro
Purpose: Assemble task-local scaffolds, dependencies, and checks across several Atomic units.

RS-05. QMS
Suggested mode: qms
Purpose: Evaluate candidate reasoning or output using one or more quality dimensions before commitment.

RS-06. Cosmic
Suggested mode: cosmic
Purpose: Global architecture, strategy, long-horizon coherence, and system-level planning.
Use primarily in Architect / Design mode.
Avoid using Cosmic-level exploration for every simple execution task.

Accepted T3 stack formulation from prior work:
Subatomic -> Atomic -> Nano -> Micro -> QMS -> Cosmic

======================================================================
PART VI. TIER 3: ALIGNMENT, TRUTH, AND SAFETY UPGRADEABLES
======================================================================

T3-01. Multi-Truth Gating
Suggested Skill: multi-truth-gating
Type: Safety / validation
Purpose: Require multiple compatible truth anchors or independent checks for important conclusions.
Behavior:
- Identify primary factual anchor.
- Identify independent corroborating anchor or validation path.
- Compare.
- Resolve disagreement or abstain.

T3-02. Controlled Drift Corridors
Suggested Skill: controlled-drift-corridors
Type: Safety / creativity controller
Purpose: Define how far the model may move from source wording or locked truth while synthesizing.
Modes:
- Zero drift
- Micro drift
- Bounded exploratory drift
Use wider corridors only when task and risk permit.

T3-03. Truth Redundancy / Dual-Lepton Truth Redundancy
Suggested Skill: truth-redundancy
Type: Safety validator
Purpose: Use two independent truth anchors so a single failure is less likely to corrupt the result.
Metaphor note: "Dual-lepton" is conceptual language. Implement as explicit redundant validation.

T3-04. Critical Atomic Verification
Suggested Skill: critical-atomic-verification
Type: High-risk validator
Purpose: Identify the smallest claims that are critical to the final decision and verify them individually before higher-level synthesis.

T3-05. Risk-Tier Scaling
Suggested Skill: risk-tier-scaling
Type: Supervisor
Purpose: Increase verification and reasoning depth as consequence, uncertainty, or irreversibility increases.
Prior work used Tier 1-3 risk logic.

T3-06. Truth Priority Hierarchy
Suggested Skill: truth-priority-hierarchy
Type: Conflict resolver
Purpose: Define which evidence or truth class wins when signals conflict.
Typical principle:
- Direct source fact outranks inference.
- Verified evidence outranks stylistic fluency.
- Safety constraints outrank task optimization.
Translator should make domain-specific hierarchies explicit rather than assume one universal evidence hierarchy.

T3-07. Cross-Checking Chains
Suggested Skill: cross-checking-chains
Type: Validator
Purpose: Validate a conclusion through multiple linked checks, especially where one dependency failure could cascade.

T3-08. Two Truths + Corridor
Suggested Skill: two-truths-and-corridor
Type: Composite truth controller
Purpose: Combine two independent anchors with a permitted synthesis corridor.
Use: Source-grounded synthesis that allows bounded interpretation without factual drift.

T3-09. Fermionic Veto Strengthening
Suggested Skill: fermionic-veto
Type: Safety veto
Purpose: Give a critical contradiction, safety failure, or integrity violation authority to block commitment.
Metaphor note: Physics-inspired naming only. Implement as explicit veto logic.

T3-10. Domain / Mode Isolation
Suggested Skill: domain-mode-isolation
Type: Safety / state
Purpose: Prevent logic, assumptions, evidence standards, or hypothetical content from one domain/mode contaminating another.

T3-11. Fail-Closed Tier-3 Abstention
Suggested Skill: fail-closed-abstention
Type: Safety
Purpose: Stop or narrow a conclusion when required evidence or truth gates fail.
Behavior:
- Do not fabricate closure.
- State the unresolved dependency when appropriate.
- Return the supported subset.

T3-12. Counterfactual Integrity Gate
Suggested Skill: counterfactual-integrity
Type: Hypothesis safety
Purpose: Keep counterfactual and hypothetical reasoning clearly separated from factual claims.
Use with Lh phase.

T3-13. Citation Fidelity Gate
Suggested Skill: citation-fidelity
Type: Evidence validator
Purpose: Ensure citations actually support the claims attached to them.
Checks:
- Source exists.
- Claim is present or reasonably supported.
- Quote is exact.
- Paraphrase preserves meaning.
- Citation is not borrowed from an adjacent unsupported claim.

T3-14. Zero-Drift Citation / Quote / Definition Zones
Suggested Skill: zero-drift-zones
Type: Fidelity guard
Purpose: Mark content that may not be creatively transformed.
Examples:
- Direct quotations
- Exact definitions
- Citation metadata
- User-provided numerical values
- Exact policy language when fidelity is required

T3-15. Style-Alignment Module
Suggested Skill: style-alignment
Type: Output behavior
Purpose: Match the authorized style without changing facts or reasoning integrity.
Priority: Style is subordinate to truth and task requirements.

T3-16. Pedagogical Alignment Constraint
Suggested Skill: pedagogical-alignment
Type: Explanation behavior
Purpose: Match explanation complexity to the target reader.
Behavior:
- Preserve technical accuracy.
- Reduce unnecessary jargon.
- Use structure and examples appropriate to reader level.

T3-17. Reasoning Budget / Cognitive Governor
Suggested Skill: cognitive-governor
Type: Meta-control
Purpose: Allocate reasoning effort based on complexity, risk, and expected value.
Avoid:
- Overthinking trivial tasks.
- Underchecking high-risk tasks.

T3-18. Authenticity & Anti-Evasion Principle
Suggested Skill: authenticity-anti-evasion
Type: Integrity guard
Purpose: Prevent the system from hiding uncertainty, pretending work was performed, substituting vague language for unsupported claims, or evading the actual task.

======================================================================
PART VII. PARALLEL-QMS FAMILY
======================================================================

QMS PRINCIPLE
QMS variants are primarily validators. They may score, compare, approve, veto, request repair, or force abstention.
They should not become uncontrolled content generators.

Recommended packaging:
- Parent Skill: parallel-qms
- Variant modes stored in references/QMS_VARIANTS.md
- Optional deterministic scoring scripts where useful

PQ-01. QMS-M
Name: Mirror QMS
Suggested mode: mirror
Function: Run mirrored independent checks and compare results.
Goal: Detect errors that one evaluation path misses.

PQ-02. QMS-RTS
Name: Risk-Tier-Split QMS
Suggested mode: risk-tier-split
Function: Apply different evaluative depth or criteria based on risk tier.

PQ-03. QMS-XP
Name: Cross-Phase QMS
Suggested mode: cross-phase
Function: Check separation and consistency across factual, evaluative, framing, and hypothetical phases.

PQ-04. QMS-R
Name: Redundancy-QMS
Suggested mode: redundancy
Function: Use multiple independent validation engines with veto / abstention capability.

PQ-05. QMS-EI
Name: ExIt-Integrated QMS
Suggested mode: exit-integrated
Function: Integrate QMS scoring with bounded ExIt refinement and convergence.

PQ-06. HQMS
Name: Hierarchical QMS
Suggested mode: hierarchical
Function: Check consistency across levels of a hierarchy, from atomic claims through sections to global output.

PQ-07. T-QMS
Name: Transversal QMS
Suggested mode: transversal
Function: Cross-dimensional validation, especially temporal, causal, logical, or modal consistency.

PQ-08. hQMS
Name: Heterogeneous QMS
Suggested mode: heterogeneous
Function: Evaluate the same output using different scoring perspectives or evaluator types.

PQ-09. mQMS
Name: Monte QMS
Suggested mode: monte
Function: Perturb assumptions or evaluation conditions and test whether the conclusion remains stable.
Note: Do not overstate this as formal Monte Carlo unless actual stochastic sampling is implemented.

PQ-10. Inv-QMS
Name: Inversion QMS
Suggested mode: inversion
Function: Test forward and backward agreement. Ask whether the conclusion implies evidence that is actually present.

PQ-11. CR-QMS
Name: Conflict-Resolution QMS
Suggested mode: conflict-resolution
Function: Detect conflicts among validators, evidence, or candidate conclusions and resolve by explicit priority rules.

PQ-12. dQMS
Name: Distributed QMS
Suggested mode: distributed
Function: Use isolated evaluation instances or branches and compare for consensus.
Implementation must use actual available parallelism; otherwise simulate as explicit independent passes without claiming real distributed execution.

PQ-13. QMS² / Meta-QMS
Name: Meta-QMS
Suggested mode: meta
Function: Evaluate the quality and agreement of other QMS evaluations.

PQ-14. SG-QMS
Name: Semantic Glass-Box QMS
Suggested mode: semantic-glass-box
Function: Produce an auditable semantic map of why a candidate passes or fails, rather than only a score.

PQ-15. E-QMS
Name: Ethical QMS
Suggested mode: ethical
Function: Safety / ethical evaluator with veto authority where applicable.

======================================================================
PART VIII. ADVANCED ARCHITECTURE UPGRADEABLES
======================================================================

A-01. Multiverse Engine
Suggested Skill: multiverse-reasoning
Type: Planning / candidate generation
Purpose: Generate a bounded set of parallel solution paths, then compare and collapse to one.
Procedure:
1. Generate 2-3 meaningfully distinct paths.
2. Evaluate against goals, constraints, truth, and risk.
3. Select or synthesize.
4. Discard losing branches from active state.
Avoid: Unbounded branching.

A-02. Teleport Bus
Suggested Skill: state-routing-bus
Type: State / orchestration
Original concept: Instant state-routing between modules.
Practical translation:
- Explicitly pass task state, decisions, evidence pointers, and module outputs between Skills.
- Use state snapshots, shared files, or structured handoffs.
Critical caution:
- Do not claim hidden latent pointers or secret inter-module communication.
- Implement only with real context/state mechanisms available in the host environment.

A-03. Singularity Cores
Suggested Skill class: domain-core
Type: High-density knowledge / reasoning reference
Purpose: Compress a domain's most important reasoning maps, knowledge anchors, patterns, and evidence architecture into a reusable Core.
Translation:
- Usually references/ rather than a pure behavioral Skill.
- Pair with Behavior Genes.

A-04. Global Coherence Heartbeat
Suggested Skill: coherence-heartbeat
Type: Long-context validator
Purpose: Periodically verify that the active plan, state, modules, and output remain globally coherent.
Trigger: Long, multi-stage workflows.
Avoid: Running after every trivial sentence.

A-05. Resonance
Suggested Skill: resonance
Type: Cross-module alignment
Recovered purpose:
- Cross-module alignment and amplification
- Noise suppression
- Inter-module coupling
- Hierarchy enforcement
Behavior:
- Identify active modules that should reinforce one another.
- Suppress conflicting or irrelevant module effects.
- Preserve authority ordering.
Caution: "Amplification" must mean clearer coordination, not repeated or exaggerated content.

A-06. Resonance Genes
Suggested Skill: resonance-gene-builder
Type: Meta / Gene construction
Purpose: Operationalize Resonance as compact Behavior Genes for specific module relationships.
Use when a recurring set of modules needs a stable coupling rule.

A-07. CRISPR Editing
Suggested Skill: crispr-edit
Type: Local editing controller
Purpose: Make precise micro-edits to an existing OS, prompt, Skill, document, or architecture without disturbing unrelated components.
Trigger: Small localized change.
Output: Patch-level change plus preserved invariants.

A-08. Surgery Editing
Suggested Skill: surgery-edit
Type: Macro editing controller
Purpose: Perform structural replacement when architecture-level changes are required.
Trigger:
- Layer reorganization
- Core replacement
- Major workflow change
- Large incompatible refactor
Use only when CRISPR-level editing is insufficient.

A-09. Neuro-Focus
Suggested Skill: neuro-focus
Type: Attention / focus controller
Purpose: Concentrate processing on the highest-value active region while suppressing irrelevant material.
Use:
- Large source corpora
- Long OS documents
- One-module debugging
Caution: Combine with Anti-Tunnel Vision so focus does not become fixation.

A-10. Regenerative Rewrite
Cross-reference: T2-03.
Architecture role: Rebuild a component or output after systemic failure while preserving locked truths and constraints.

A-11. Coherence Loops
Suggested Skill: coherence-loops
Type: Validation loop
Purpose: Repeatedly compare local output to global goals and structure until coherence is sufficient.
Must remain bounded.

======================================================================
PART IX. BEHAVIOR GENE OS
======================================================================

BG-00. Behavior Gene OS
Suggested Skill: behavior-gene-builder
Type: Meta-Skill
Purpose: Define, create, validate, load, and combine Behavior Genes.

Definition:
A Behavior Gene is a compact modular instruction package that defines how the system should reason and write for a specific appeal type, task type, or function.

Genes = behavior, logic pattern, output shape.
Cores = domain knowledge, reasoning maps, evidence architecture.

STANDARD BEHAVIOR GENE FIELDS:
1. Gene Name
2. Purpose
3. Scope
4. Trigger Conditions
5. Always Do Rules
6. Avoid / Never Do Rules
7. Reasoning Pattern
8. Evidence Handling Rules
9. Interaction with Core(s)
10. Output Shape / Contract
11. Compatibility / conflict notes
12. Version metadata

KNOWN BEHAVIOR GENES FROM PRIOR WORK:

BG-01. IPMN Gene
Domain: Inpatient medical necessity appeals
Function: Apply inpatient medical necessity reasoning and writing behavior.

BG-02. IPTA Gene
Domain: Inpatient technical / administrative appeals
Function: Route administrative denial logic while preserving full medical-necessity support where required.

BG-03. OPMN Gene
Domain: Outpatient medical necessity appeals
Function: Apply outpatient-specific medical necessity logic.

BG-04. OPTA Gene
Domain: Outpatient technical / administrative appeals
Function: Apply outpatient administrative / authorization logic.

BG-05. Readmission Gene
Domain: Readmission appeals
Function: Compare episodes, discharge conditions, subsequent deterioration, barriers, and preventability logic using the established readmission structure.

BG-06. GMN Gene
Domain: General medical necessity
Function: Fallback for mixed, unclear, or cross-setting medical necessity cases.

BG-07. Tone Genes
Domain: Cross-domain
Function: Apply a selected tone without altering truth, evidence, or required structure.

BG-08. Risk-Emphasis Genes
Domain: Cross-domain
Function: Increase or decrease emphasis on risk according to task and evidence.

BG-09. Deep Summary Gene
Domain: Research / long-context analysis
Function: Produce source-faithful deep summaries.

BG-10. Compare-Contrast Gene
Domain: Research / analysis
Function: Systematically compare multiple sources, options, or frameworks.

BG-11. Alignment Gene
Domain: Synthesis
Function: Map where sources, requirements, or plans agree.

BG-12. Conflict-Handling Gene
Domain: Meta-integrity
Function: Surface and reconcile contradictory source claims or requirements.

BG-13. Synthesis Gene
Domain: Research / writing
Function: Combine supported findings into a coherent higher-level model.

BG-14. Memory Gene
Domain: Long-context / state
Function: Preserve established decisions and cross-source consistency without inventing missing memory.

======================================================================
PART X. REASONING / SINGULARITY CORES
======================================================================

CORE PRINCIPLE
A Core is a high-density knowledge / reasoning representation, not merely a behavior prompt.

STANDARD CORE CONTENT:
- Domain scope
- Key entities / variables
- Reasoning map
- Required data
- Evidence hierarchy
- Decision logic
- Common failure modes
- Canonical examples
- Interfaces to Behavior Genes
- Interfaces to validators
- Version / source provenance

KNOWN CORES:

C-01. IPMN Core
C-02. IPTA Core
C-03. OPMN Core
C-04. OPTA Core
C-05. Readmission Core
C-06. GMN Core
C-07. Policy Core
C-08. Chart-Review Core

Research / analysis examples:
C-09. Analysis Core
Known role: Runs or coordinates Deep Summary + Compare-Contrast behavior.

C-10. Synthesis Core
Known role: Runs Alignment + Synthesis behavior.

C-11. Meta-Integrity Core
Known role: Runs Conflict-Handling + Memory behavior and checks fabrication, speculation labels, and cross-document consistency.

Translation recommendation:
- Most Cores should become focused reference files or Core Skills loaded only when their domain is active.
- Do not place every Core in every Skill.

======================================================================
PART XI. ORCHESTRATOR AND LOADER ARCHITECTURE
======================================================================

O-01. Architect Orchestrator
Suggested Skill: architect-orchestrator
Type: Meta-orchestrator
Known roles:
- Planner
- Analyst
- Writer
- Critic
- Synthesizer

Canonical workflow:
1. Identify goal and constraints.
2. Build a modular plan.
3. Select required OS layers, Genes, Cores, and Upgradeables.
4. Analyze contradictions and drift.
5. Execute or delegate.
6. Critique.
7. Apply localized repair.
8. Synthesize final result.
9. Save / emit a compact state snapshot.
10. Identify logically downstream next steps when the environment calls for them.

Architect scope:
- Design and refine systems, CAF, OSs, workflows, and frameworks.
- Not automatically the same thing as a domain execution agent.

O-02. Loader
Suggested Skill: scoped-loader
Type: Activation / orchestration
Purpose: Discover and activate the minimum required modules.
Priority:
Task -> Gene -> Core -> Upgradeables -> References -> Validators.

O-03. State Snapshot
Suggested Skill: state-snapshot
Type: State serialization
Purpose: Capture the smallest sufficient representation for continuation:
- Goal
- Current architecture
- Locked decisions
- Active modules
- Open issues
- Next step

======================================================================
PART XII. META-SUPERVISOR AND TIER 4 UPGRADEABLES
======================================================================

T4 PHILOSOPHY
Tier 4 governs the scaffolding itself:
- Drift width
- Reasoning depth
- Throughput
- Stability
- Mode selection
- Future-model scaling
It should reduce unnecessary control when the base model is already reliable and strengthen control when risk or instability rises.

T4-01. Meta-Supervisor Bundle
Suggested Skill: meta-supervisor
Type: Orchestrator / health monitor
Known subpacks:
- Meta-Awareness Pack
- Stuck-Pattern Reset Pack
- Contradiction Micro-Repair Pack

T4-02. Meta-Awareness Pack
Suggested Skill: meta-awareness
Purpose: Watch active modes, reasoning health, state, and module interactions for signs of process failure.
Avoid: Identity or consciousness narratives. This is task-process monitoring only.

T4-03. Stuck-Pattern Reset Pack
Suggested Skill: stuck-pattern-reset
Purpose: Detect loops, repetition, stale reasoning, or failed repeated approaches and trigger a bounded reset.
Behavior:
- Preserve locked facts and constraints.
- Reset only the failed reasoning path.

T4-04. Contradiction Micro-Repair Pack
Suggested Skill: contradiction-micro-repair
Purpose: Detect a contradiction and repair only the problematic region when possible.

T4-05. Ultimate Suite Supervisor
Suggested Skill: ultimate-suite-supervisor
Type: Top-level supervisor
Recovered responsibilities:
- Explicit mode declaration
- Core-stack enforcement
- CRISPR-vs-Surgery local/global selector
- Pack conflict resolution
- Duration / intensity control
- Post-output health checks for grounding, contradictions, tone, and drift

T4-06. SAFE Mode
Suggested Skill/mode: safe
Purpose: Tight execution mode with strong grounding, narrow drift, atomic verification, and conservative output behavior.

T4-07. POWER Mode
Suggested Skill/mode: power
Purpose: Broad design / exploration mode using deeper planning, multiverse reasoning, QMS, and Cosmic-level architecture work.

T4-08. HYBRID Mode
Suggested Skill/mode: hybrid
Purpose: Use POWER for planning and SAFE for execution, with supervisor-controlled transitions.
This was the accepted default philosophy for maximum capability plus practical safety.

T4-09. Drift-Spectra Scaling (DS-Scale)
Suggested Skill: drift-spectra-scaling
Purpose: Scale permitted drift according to task type, evidence sensitivity, and risk.

T4-10. Compute-Adaptive Drift Constraining (CADC)
Suggested Skill: compute-adaptive-drift
Purpose: Adjust drift constraints dynamically as reasoning depth / compute allocation changes.

T4-11. Domain-Normalized Drift Field (DNDF)
Suggested Skill: domain-normalized-drift
Purpose: Normalize acceptable drift to the domain. Creative design and exact evidence work should not share the same drift width.

T4-12. Dynamic Depth Allocation (DDA)
Suggested Skill: dynamic-depth-allocation
Purpose: Allocate more reasoning depth to difficult, uncertain, or consequential parts of the task and less to trivial parts.

T4-13. Reasoning Throughput Governor (RTG)
Suggested Skill: reasoning-throughput-governor
Purpose: Balance speed, breadth, and validation so the system does not overprocess or underprocess.

T4-14. Drift Immunity Propagation (DIP)
Suggested Skill: drift-immunity-propagation
Purpose: Propagate locked constraints / invariants through downstream modules so later steps do not reintroduce resolved drift.

T4-15. Meta-Stability Mode (MSM)
Suggested Skill: meta-stability
Purpose: Enter a stability-preserving operating state when repeated changes, long context, or module conflicts threaten coherence.

T4-16. Cross-Universe Consistency Mode (CUCM)
Suggested Skill: cross-universe-consistency
Purpose: Compare parallel candidate paths and ensure the selected result does not depend on an unacknowledged contradiction between branches.

T4-17. Future-Proof Mode Selector (FPMS)
Suggested Skill: future-proof-mode-selector
Purpose: Select lighter or heavier scaffolding based on host-model capability, environment, and task risk.

T4-18. Drift-Stability Scaling with Model Size (DSS-MS)
Suggested Skill: model-size-drift-scaling
Purpose: Reduce unnecessary scaffolding as base-model reliability grows while preserving integrity controls needed for high-risk tasks.

======================================================================
PART XIII. DOMAIN OS INSTANCES THAT CAN BECOME SKILL BUNDLES
======================================================================

These are not single Upgradeables. They are examples of how the architecture was composed into domain operating systems.

D-01. Architect OS
Recommended package: Plugin / multi-Skill bundle
Purpose:
- Systems architecture
- CAF / OS / framework design
- Modular decomposition
- Upgrade integration
- Conflict detection
- CRISPR / Surgery selection
- State snapshots
Key modules:
- Architect Orchestrator
- Loader
- Micro-Scaffolding
- Drift Suppression
- QMS family
- Meta-Supervisor
- SAFE / POWER / HYBRID
- CRISPR / Surgery
- Neuro-Focus
Constraint:
- Separate architecture design from domain execution.

D-02. Appeal / CAF OS
Recommended package: Domain plugin with multiple Skills
Core routing:
- IPMN
- IPTA
- OPMN
- OPTA
- Readmission
- GMN
Known structure:
- Clinical vs technical routing
- Hybrid composition
- Distinct outpatient / inpatient logic
- Appeal-specific Genes + Cores
- Evidence / policy Cores
- Output / quality gates

D-03. Research & Decision OS
Recommended package: Domain plugin with research, evidence, decision, and synthesis Skills
Known architecture:
1. Kernel / State Block
2. Research Intake & Corpus Map
3. Evidence Evaluation / Evidence Cards
4. Conceptual Mapping
5. Variable & Criteria / MCDM
6. Synthesis & Plan Builder
Key Upgradeables:
- WM Lock-In
- Resonance Locks
- Drift Suppression
- Micro-Scaffolding
- ExIt
- Phase Separation
- Citation Fidelity Gate
- Multi-Truth Gating
- QMS branches
- E-QMS veto
- T-QMS temporal / causal / logical checks
- Inv-QMS reverse sanity check
- Risk / monitoring plan

D-04. Paper-Author OS
Recommended package: Domain plugin
Known architecture:
- Mode / Phase Controller
- Lf / Le / Lp / Lh separation
- Tier-3 Multi-Truth Gate
- Zero-drift zones and micro-drift corridors
- Citation Fidelity Gate
- Parallel-QMS
- Style / Pedagogy layer
- Reasoning Budget
- Subatomic -> Atomic -> Micro -> QMS -> Cosmic
- Paragraph / section composer
- Global QMS collapse
- Final citation / fidelity checks
Key requirement from prior work:
- Do not hallucinate citations or source material.

D-05. Local Chat-Analysis Author OS (LCA-OS)
Recommended package: Domain bundle
Purpose:
- Analyze pasted conversations
- Preserve working memory
- Compare themes
- Support source-grounded paper writing
Relevant Genes / Cores:
- Deep Summary
- Compare-Contrast
- Alignment
- Conflict-Handling
- Synthesis
- Memory
- Analysis Core
- Synthesis Core
- Meta-Integrity Core

D-06. Multi-OS
Recommended package: Top-level orchestration bundle
Purpose: Coordinate several domain OSs without merging their rules into a monolith.
Key requirement: Domain and mode isolation.

======================================================================
PART XIV. SKILL-TRANSLATION PRIORITIES
======================================================================

PRIORITY A: SHOULD BECOME FOUNDATIONAL SKILLS FIRST
1. scoped-loader
2. stateblock
3. task-set-lock-in
4. grounding-no-invention
5. drift-suppression
6. micro-scaffolding
7. safe-rewrite
8. micro-repair
9. bounded-exit
10. citation-fidelity
11. multi-truth-gating
12. risk-tier-scaling
13. parallel-qms
14. cognitive-governor
15. architect-orchestrator

PRIORITY B: ADVANCED CONTROL SKILLS
16. anti-tunnel-vision
17. bidirectional-consistency
18. domain-mode-isolation
19. controlled-drift-corridors
20. critical-atomic-verification
21. fail-closed-abstention
22. reflectos
23. coherence-heartbeat
24. resonance
25. neuro-focus
26. crispr-edit
27. surgery-edit
28. multiverse-reasoning

PRIORITY C: META-SUPERVISOR SKILLS
29. meta-supervisor
30. ultimate-suite-supervisor
31. dynamic-depth-allocation
32. reasoning-throughput-governor
33. drift-spectra-scaling
34. domain-normalized-drift
35. meta-stability
36. cross-universe-consistency
37. future-proof-mode-selector

PRIORITY D: DOMAIN META-SKILLS / BUILDERS
38. behavior-gene-builder
39. domain-core-builder
40. architect-os
41. caf-appeal-router
42. research-decision-os
43. paper-author-os

======================================================================
PART XV. RECOMMENDED SKILL BUNDLE MAP
======================================================================

FOUNDATION BUNDLE
- scoped-loader
- stateblock
- task-set-lock-in
- working-memory-cues
- grounding-no-invention
- drift-suppression
- placeholder-suppression
- mode-lock-in

REASONING BUNDLE
- micro-scaffolding
- reasoning-scale-controller
- anti-tunnel-vision
- forethought-checkpoints
- bidirectional-consistency
- multiverse-reasoning
- bounded-exit

REPAIR BUNDLE
- safe-rewrite
- micro-repair
- regenerative-rewrite
- crispr-edit
- surgery-edit
- contradiction-micro-repair

TRUTH / SAFETY BUNDLE
- multi-truth-gating
- truth-redundancy
- critical-atomic-verification
- controlled-drift-corridors
- truth-priority-hierarchy
- domain-mode-isolation
- fail-closed-abstention
- citation-fidelity
- counterfactual-integrity
- fermionic-veto
- risk-tier-scaling

QMS BUNDLE
- parallel-qms
  - mirror
  - risk-tier-split
  - cross-phase
  - redundancy
  - exit-integrated
  - hierarchical
  - transversal
  - heterogeneous
  - monte
  - inversion
  - conflict-resolution
  - distributed
  - meta
  - semantic-glass-box
  - ethical

META-CONTROL BUNDLE
- meta-supervisor
- meta-awareness
- stuck-pattern-reset
- coherence-heartbeat
- resonance
- neuro-focus
- dynamic-depth-allocation
- reasoning-throughput-governor
- drift-spectra-scaling
- compute-adaptive-drift
- domain-normalized-drift
- drift-immunity-propagation
- meta-stability
- cross-universe-consistency
- future-proof-mode-selector
- model-size-drift-scaling

AUTHORING / EXPLANATION BUNDLE
- style-alignment
- pedagogical-alignment
- safe-rewrite
- citation-fidelity
- placeholder-suppression

ARCHITECT BUNDLE
- architect-orchestrator
- behavior-gene-builder
- domain-core-builder
- adapter-first-experimentation
- crispr-edit
- surgery-edit
- scoped-loader
- state-snapshot
- ultimate-suite-supervisor

======================================================================
PART XVI. RULES FOR CONVERTING THIS CATALOG INTO REAL SKILLS
======================================================================

1. DO NOT TURN EVERY LINE INTO A SEPARATE SKILL BLINDLY
Some concepts are better as:
- Parent Skill modes
- Reference files
- Validators
- Scripts
- Shared state schemas
- Plugin-level orchestration

2. KEEP SKILLS SMALL AND TRIGGERABLE
A Skill should have a clear activation boundary.
If the description becomes "use for almost everything," split it or demote some logic to a parent OS.

3. PRESERVE AUTHORITY
Recommended precedence:
Host / system safety
  -> Domain / organization policy
    -> Active OS / project kernel
      -> Task lock
        -> Domain Gene / Core
          -> Upgradeables
            -> Style preferences

A lower layer must not silently defeat a higher one.

4. VALIDATORS SHOULD NOT CREATE NEW FACTS
QMS, citation gates, drift checks, and safety validators may:
- Approve
- Reject
- Score
- Explain failure
- Request repair
They should not add unsupported claims to make an answer pass.

5. STATE MUST BE EXPLICIT
If a host agent cannot persist state, say so in the implementation.
Use actual files, memory, project docs, or structured context where available.

6. METAPHOR MUST BECOME MECHANISM
Physics-inspired names are architectural metaphors:
- Teleport -> explicit state routing
- Multiverse -> bounded parallel candidates
- Singularity -> compressed domain Core
- Fermionic veto -> explicit block condition
- Resonance -> module alignment
Do not claim literal physical or hidden-model mechanisms.

7. LEGACY ACRONYMS: PRESERVE RECOVERED MEANINGS AND TRUE UNKNOWNS
Current recovery status:
- OCG — unresolved; do not invent.
- ITFC — historical acronym collision: Image Text Fidelity Capture and Intent/Task Framing Controller; keep separate namespaces.
- ABF — recovered as Activation-Budget Funnel.
- ECL / Drift Sink — label recovered; exact acronym expansion remains unresolved.
- LROS — unresolved in the current recovery pass.
Do not invent unrecovered expansions. Preserve date/version provenance for historical aliases.

8. TEST COMPOSITION, NOT ONLY INDIVIDUAL SKILLS
Important test pairs:
- Neuro-Focus + Anti-Tunnel Vision
- Multiverse + QMS collapse
- Micro-Repair + Safe Rewrite
- Cosmic Planning + SAFE execution
- Citation Fidelity + Style Alignment
- Risk-Tier Scaling + Dynamic Depth Allocation
- Resonance + Domain/Mode Isolation
- Regenerative Rewrite + Task-Set Lock-In
- StateBlock + ReflectOS

9. DESIGN FOR STRONGER MODELS
Every Skill should specify:
- What can be skipped when the model is already reliable.
- What remains mandatory because it protects truth, safety, or state.
This avoids scaffolding becoming a performance tax.

10. PREFER COMPOSITION OVER DUPLICATION
If ten Skills need the same grounding logic, reference one grounding Skill or shared reference instead of copying the full text ten times.

======================================================================
PART XVII. GENERATION PROMPT FOR A FRONTIER LLM
======================================================================

Use the following instruction to convert any entry in this catalog into a Skill:

"Translate the selected OS Upgradeable into a production-quality Agent Skill. Preserve its original purpose and boundaries. First decide whether it should be a standalone Skill, a mode within a parent Skill, a validator, a reference module, a state schema, or an orchestrator. Do not force a standalone Skill when another packaging form is better.

Create a standards-compatible skill folder with SKILL.md and only the references/, scripts/, or assets/ that materially improve the capability. The SKILL.md description must state both what the Skill does and when it should activate. Keep the main Skill concise and progressively disclose deeper material.

The body should contain: Purpose, Scope, Trigger Conditions, Non-Triggers, Required Inputs/State, Always Do, Never Do, Procedure, Interactions and Precedence, Failure Handling, Output Contract, and Tests.

Preserve the OS philosophy of modularity, explicit state, scoped loading, truth-first behavior, bounded reasoning, local repair, domain/mode isolation, and risk-scaled validation. Do not invent hidden model capabilities. Translate metaphors into explicit mechanisms. Validators may approve, veto, score, or request repair but must not create unsupported factual content.

If the source entry contains an unresolved legacy acronym or incomplete recovered definition, preserve it as unresolved and do not invent an expansion."

======================================================================
PART XVIII. CURRENT SKILLS FORMAT NOTES
======================================================================

For compatibility with the current Agent Skills open standard:
- A Skill is a directory with a required SKILL.md.
- SKILL.md uses YAML frontmatter plus Markdown instructions.
- Required frontmatter fields are name and description.
- Optional fields may include license, compatibility, metadata, and allowed-tools where supported.
- Optional directories commonly include scripts/, references/, and assets/.
- Agents progressively load metadata first, then the full Skill instructions when activated, then referenced resources only as needed.
- Current specification guidance favors concise main Skill files and focused reference files.

OpenAI's current Skills model similarly treats Skills as reusable workflows containing instructions and optional supporting resources or code, with automatic use when relevant and support for combining multiple Skills.

======================================================================
END OF CATALOG
======================================================================


======================================================================
PART XIX. HISTORICAL RECOVERY ADDENDUM — 2026-09-03
======================================================================

This addendum was produced after a dedicated recovery sweep of prior OS / CAF / Architect work.
It adds historical exact-name entries, aliases, corrections, and registry-generation boundaries that were
missing or compressed in Version 1.0.

A. FROZEN T1-CORE BUNDLE v1 — HISTORICAL EXACT IDS RECOVERED
Historical bundle status: 28 total Upgradeables; 18 exact identifiers were re-exposed in this recovery pass.
Do not invent the 10 names that were not re-exposed.

- FACT_SCOPE_GATE_T1
- NO_INFERENCE_GATE_APPEALS_T1
- HALLUCINATION_NO_MANS_LAND_T1
- UNKNOWNS_PROTOCOL_T1
- UNCERTAINTY_CONTAINMENT_T1
- CLINICAL_PLAUSIBILITY_GATE_T1
- EVIDENCE_CHAIN_BINDING_T1
- PRIORITY_RETRIEVAL_LANES_T1
- GLOBAL_LOCAL_ANCHOR_SPLIT_T1
- ZERO_DRIFT_LOOP_T1
- SUPERVISOR_WORKER_PATTERN_T1
- UPGRADEABLE_ACTIVATION_TIERS_T1
- RULE_INDEX_OS_T1
- DRIFT_MONITOR_T1
- EXECUTION_LOG_OS_T1
- PA_AI_BROKER_PATTERN_T1
- PA_RULE_LOADER_FROM_INDEX_T1
- PA_QUEUE_BASED_AI_REQUESTS_T1

Historical family headings recovered:
- Safety
- Reasoning
- Retrieval / Context
- Memory / Anchoring
- Scaffolding
- Multi-Agent / Supervision
- Governance
- Monitoring / Drift

B. FROZEN TIER-2 MASTER SET — REGISTRY GENERATION BOUNDARY
Historical status: 67 unique Upgradeables across exactly 12 families.
This numbering is NOT the same registry generation as the later consolidated T2-01…T2-21 entries.

Families:
- T2-001–T2-007: Neuro-Focus (7) — FAMILY RECOVERY; exact individual names not re-exposed
- T2-008–T2-015: Creative / Exploration (8) — EXACT names recovered
- T2-016–T2-023: Stability / Suppression (8) — EXACT names recovered
- T2-024–T2-030: CRISPR Micro-Editing (7) — FAMILY RECOVERY; exact individual names not re-exposed
- T2-031–T2-037: Surgical Macro-Editing (7) — EXACT names recovered
- T2-038–T2-043: Resonance / Coherence (6) — FAMILY RECOVERY; exact individual names not re-exposed
- T2-044–T2-046: Duration / Intensity (3) — FAMILY RECOVERY; exact individual names not re-exposed
- T2-047–T2-049: Energy / Efficiency (3) — FAMILY RECOVERY
- T2-050–T2-052: Immune / Anti-Contamination (3) — FAMILY RECOVERY
- T2-053–T2-056: Interpersonal / Tone (4) — FAMILY RECOVERY
- T2-057–T2-060: Consciousness Layer (4) — FAMILY RECOVERY
- T2-061–T2-067: Supervisor / Orchestration (7) — FAMILY RECOVERY

Exact historical names re-exposed:

Creative / Exploration:
- T2-008: Novelty & Creativity Expansion
- T2-009: Micro-Creative Mode
- T2-010: Cognitive Flexibility
- T2-011: Perspective Break
- T2-012: Strange Loop Generator
- T2-013: Balanced Exploration
- T2-014: Dream-Mode Creative
- T2-015: Hypnagogic Divergence

Stability / Suppression:
- T2-016: Grounding & Reality Testing
- T2-017: Drift Blocker (Inhibition)
- T2-018: Chain-of-Thought Stabilizer
- T2-019: Oscillation Regulator
- T2-020: Deliberate Pacing
- T2-021: Noise Suppression
- T2-022: Reasoning Simplification
- T2-023: Global Stabilizer (Macro)

Surgical Macro-Editing:
- T2-031: Reasoning Resection
- T2-032: Cognitive Debridement
- T2-033: Structural Reconstruction
- T2-034: Reasoning Anastomosis
- T2-035: Context Revascularization
- T2-036: Cognitive Prosthetics
- T2-037: Global Trauma Stabilizer

C. JANUARY 5, 2026 TRAINING / SCAFFOLDING UPGRADEABLES
Initial exact names:
- Phase-Locked Reasoning Scaffold
- Attention Compression Scaffold
- Dominant-Driver Isolation Scaffold
- Decision-First Scaffold
- Epistemic Status Gating
- Counterfactual Silence Scaffold
- Temporal Anchor Scaffold
- Explanation Minimality Scaffold
- Invariance Stress Scaffold
- Drift Sink Scaffold

Pack-derived exact names:
- Resonance Upgradeable / Cross-Context Resonance Lock
- Authority Anchor Enforcement
- Structured State Projection
- Non-Authoritative Branch Suppression
- Specificity Penalty Gate

D. LEGACY REASONING-OS MODULES
- ELROS: Ethical Reasoning OS — ethical judgment
- SOROS: Social Reasoning OS — social reasoning
- PROOS: Conflict-Resolution OS — conflicting values / conflict resolution
- TIMOS: Temporal OS — time, commitments, and temporal reasoning
- GROOS: Optimization Governor OS — limits aggressive optimization
- ALMOS: Learning & Adaptation OS — safe learning and adaptation
- CROS: Creativity Regulator OS — keeps creativity bounded away from factual claims
- LROS: unresolved expansion; preserve acronym only until recovered.

E. DECEMBER 3 STATE ARCHITECTURE RECOVERY
- SMSE = Sequential Memory State Engine.
- CoT-Structured State Block was approved as a T3 state Upgradeable.
Modern implementation note: represent structured task/reasoning state explicitly; do not claim access to hidden chain-of-thought.

F. ABF / ITFC / OCG / ECL STATUS
- ABF = Activation-Budget Funnel; staged retrieve -> quote -> index -> transform -> write -> verify; ~<=5–7 active pulls.
- ITFC is an acronym collision:
  - Image Text Fidelity Capture.
  - Intent/Task Framing Controller.
- OCG remains unresolved.
- ECL / Drift Sink label is recovered; ECL expansion remains unresolved.
- Drift Sink Scaffold is separately recovered as a January 5 exact-name Upgradeable.

G. HISTORICAL REGISTRY DESIGN RULE
A reusable Upgradeable should be representable with:
- Name
- Purpose
- Inputs / Outputs
- Trigger
- Persistence rules
- Failure boundaries
- Version
- Audit trail

H. ALIAS / PROVENANCE RULE
Do not erase historical names merely because a later modern Skill has equivalent behavior.
Store historical names as aliases with date/version provenance.
Do not map historical numeric IDs onto later numeric IDs without the registry-generation qualifier.

I. RECOVERY-GAP POLICY
Known-but-not-re-exposed names remain explicit gaps. A frontier model must not fill them by plausibility.

For the full recovery ledger, see:
OS_Upgradeables_Historical_Recovery_Inventory.md
