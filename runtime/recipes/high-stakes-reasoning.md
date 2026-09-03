# High-Stakes Reasoning — Runtime Pack

Purpose: Evaluate consequential claims with proportionate evidence, uncertainty, verification, and abstention controls.

Task family: consequential evidence evaluation and decision support

Activation boundary: Use when an error could materially affect safety, health, rights, finances, or an irreversible action and the necessary evidence can be inspected.

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
| R | `grounding-no-invention@1.1.0` — Grounding / No-Invention | work relies on documents, data, external facts, or consequential claims |
| R | `epistemic-status-gating@1.1.0` — Evidence-Confidence Gate | claims of mixed certainty are present |
| R | `risk-tier-scaling@1.1.0` — Risk-Tier Scaling | task risk varies or must be classified |
| R | `critical-atomic-verification@1.1.0` — Critical Fact Verification | small factual errors could change the outcome |
| R | `multi-truth-gating@1.1.0` — Independent Evidence Gate | an important conclusion rests on fragile evidence |
| A | `truth-redundancy@1.1.0` — Independent Evidence Redundancy | a consequential claim can be independently checked |
| R | `truth-priority-hierarchy@1.1.0` — Truth Priority Hierarchy | evidence classes or authorities conflict |
| R | `domain-mode-isolation@1.1.0` — Domain / Mode Isolation | multiple domains or semantic modes coexist |
| C | `citation-fidelity@1.1.0` — Citation Fidelity Gate | output contains citations or source-attributed claims |
| R | `fail-closed-abstention@1.1.0` — Fail-Closed Abstention | required evidence cannot be verified |
| A | `fermionic-veto@1.1.0` — Non-Compensable Constraint Veto | a defined critical condition must have veto authority |
| R | `parallel-qms@1.1.0` — Parallel Validation System | a composed workflow needs structured quality evaluation |
| A | `dynamic-depth-allocation@1.1.0` — Per-Region Reasoning Depth | task regions vary in difficulty or risk |

## Runtime component cards

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

### R — Evidence-Confidence Gate

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

### R — Risk-Tier Scaling

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

Full package and provenance: [`risk-tier-scaling`](../../upgradeables/meta-control/risk-tier-scaling/UPGRADEABLE.md).

### R — Critical Fact Verification

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

### R — Independent Evidence Gate

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

### A — Independent Evidence Redundancy

Recovered name: Truth Redundancy

Purpose: Reduce single-point truth failure before high-impact synthesis or decision-making.

Activate when: a consequential claim can be independently checked.

Do not use when: the claim is low risk and an authoritative primary source is decisive; a second anchor would merely repeat the first source.

Requires: none.

#### Runtime mechanism

For a selected truth atom, establish two evidence or validation anchors whose failure modes are meaningfully independent. Record provenance and the proposition each anchor supports; the pair is then passed to a gate or resolver rather than treated as automatic proof.

#### Procedure

1. Identify the consequential truth atom.
2. Select the primary anchor and record its failure mode.
3. Select a second anchor with a distinct source or validation path.
4. Verify that the second does not merely derive from the first.
5. Record each anchor's supported scope and hand the pair to Multi-Truth Gating.

#### Guardrails

- Mandatory even on strong models: when redundancy is claimed, the anchors must be genuinely independent.
- Conflict/precedence: Independence is invalid if both anchors share the same unverified upstream source; A safety veto still controls even when two non-safety anchors agree.
- Stop or fail when: If no genuinely independent second anchor is available, report that limitation and do not claim redundant verification.

Full package and provenance: [`truth-redundancy`](../../upgradeables/truth-grounding/truth-redundancy/UPGRADEABLE.md).

### R — Truth Priority Hierarchy

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

Full package and provenance: [`domain-mode-isolation`](../../upgradeables/state/domain-mode-isolation/UPGRADEABLE.md).

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

### R — Fail-Closed Abstention

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

### A — Non-Compensable Constraint Veto

Recovered name: Fermionic Veto Strengthening

Purpose: Preserve non-compensable constraints during aggregation and synthesis.

Activate when: a defined critical condition must have veto authority.

Do not use when: the alleged defect is merely a soft preference; the veto predicate cannot be defined or evidenced.

Requires: none.

#### Runtime mechanism

Declare a narrow set of exclusion predicates before scoring. Evaluate them independently of aggregate quality; if any predicate is evidenced, quarantine the candidate and require removal of the disqualifying state plus revalidation. The fermionic metaphor is operational only: incompatible states do not share the certified result, and the veto is never diluted by votes or averages.

#### Procedure

1. Define non-compensable predicates and required evidence.
2. Run veto checks independently from quality scoring.
3. Record the exact predicate, evidence, and affected candidate.
4. Exclude or quarantine any triggered candidate.
5. Permit repair only if the disqualifying state is removed rather than relabeled.

#### Guardrails

- Mandatory even on strong models: independent hard-constraint check whenever aggregate scoring is used.
- Conflict/precedence: Verified veto evidence outranks aggregate score or validator majority; If veto evidence conflicts, quarantine pending targeted adjudication rather than silently clearing it.
- Stop or fail when: Do not certify or execute a candidate while a verified non-compensable predicate remains active.

Full package and provenance: [`fermionic-veto`](../../upgradeables/validation/fermionic-veto/UPGRADEABLE.md).

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
