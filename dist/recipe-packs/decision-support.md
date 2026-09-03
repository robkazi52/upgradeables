# Decision Support — Runtime Pack

Purpose: Compare consequential options against explicit criteria and evidence without presenting generated choices as facts.

Task family: option comparison, trade-off analysis, and recommendation support

Activation boundary: Use when a user must compare consequential options against explicit criteria and evidence without turning generated candidates into facts.

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

Use Citation Fidelity when a recommendation must cite source material. A
Compare-Contrast Behavior Gene may guide the side-by-side analysis, but it does
not replace decision controls. Parallel QMS may be implemented as sequential,
independent evidence, citation, and logic checks when real parallelism is absent.

## Output contract

Return decision criteria and method, a side-by-side evidence comparison, the
recommendation, claim-local citations when requested, material tradeoffs,
missing information, and uncertainty or sensitivity that could change the result.

## Component routing

| Role | Component | Activate when |
|:---:|---|---|
| R | `task-set-lock-in@1.1.0` — Task-Set Lock-In | multi-step work begins or scope changes |
| R | `decision-first-scaffold@1.1.0` — Decision-First Scaffold | analysis risks becoming directionless before commitment |
| R | `grounding-no-invention@1.1.0` — Grounding / No-Invention | work relies on documents, data, external facts, or consequential claims |
| A | `risk-tier-scaling@1.1.0` — Risk-Tier Scaling | task risk varies or must be classified |
| A | `anti-tunnel-vision@1.1.0` — Anti-Tunnel Vision | premature fixation could hide credible alternatives |
| A | `bidirectional-consistency@1.1.0` — Bidirectional Consistency | causal, logical, quantitative, or evidence claims are central |
| A | `truth-priority-hierarchy@1.1.0` — Truth Priority Hierarchy | evidence classes or authorities conflict |
| C | `citation-fidelity@1.1.0` — Citation Fidelity Gate | output contains citations or source-attributed claims |
| C | `dynamic-depth-allocation@1.1.0` — Per-Region Reasoning Depth | task regions vary in difficulty or risk |
| A | `parallel-qms@1.1.0` — Parallel Validation System | a composed workflow needs structured quality evaluation |

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

### R — Decision-First Scaffold

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

### A — Risk-Tier Scaling

Purpose: Apply proportionate rigor so low-risk tasks remain efficient and high-risk claims or actions receive stronger evidence and fail-closed handling.

Activate when: task risk varies or must be classified.

Do not use when: a binding protocol already specifies the exact controls; the task is harmless and fully reversible.

Requires: none.

#### Runtime mechanism

Classify the whole task and any higher-risk subregions using consequence, uncertainty, reversibility, scope of impact, and evidence quality. Map the result to explicit control floors: light single-path checks for routine work, stronger source and consistency checks for material work, and independent verification, hard vetoes, checkpointing, and fail-closed behavior for high-risk work. Reclassify when new evidence raises or lowers risk.

#### Procedure

1. Identify potential harms, affected parties, uncertainty, reversibility, and blast radius.
2. Assign a risk tier to the task and separately to any exceptional subregion.
3. Select the tier's mandatory reasoning, evidence, independent-check, and veto controls.
4. Fund those controls through Cognitive Governor and route depth with DDA.
5. Reassess risk before irreversible action and whenever new evidence changes consequence or uncertainty.

#### Guardrails

- Mandatory even on strong models: consequence and uncertainty assessment; high-risk independent checks; hard veto and fail-closed behavior.
- Conflict/precedence: A required tier cannot be lowered because of cost or deadline; When tier controls cannot be completed, return blocked or abstain.
- Stop or fail when: domain-label risk; budget-driven downgrading.

Full package and provenance: [`risk-tier-scaling`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/meta-control/risk-tier-scaling/UPGRADEABLE.md).

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

Full package and provenance: [`truth-priority-hierarchy`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/truth-grounding/truth-priority-hierarchy/UPGRADEABLE.md).

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

Full package and provenance: [`citation-fidelity`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/validation/citation-fidelity/UPGRADEABLE.md).

### C — Per-Region Reasoning Depth

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

Full package and provenance: [`dynamic-depth-allocation`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/meta-control/dynamic-depth-allocation/UPGRADEABLE.md).

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
