# Medical Evidence — Runtime Pack

Purpose: Synthesize medical evidence with applicability, uncertainty, and professional-review boundaries.

Task family: medical literature and clinical-evidence synthesis

Activation boundary: Use for source-backed medical evidence synthesis where claim scope, uncertainty, and abstention matter; it does not replace clinical diagnosis or treatment.

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
| R | `grounding-no-invention@1.1.0` — Grounding / No-Invention | work relies on documents, data, external facts, or consequential claims |
| R | `risk-tier-scaling@1.1.0` — Risk-Tier Scaling | task risk varies or must be classified |
| R | `critical-atomic-verification@1.1.0` — Critical Fact Verification | small factual errors could change the outcome |
| R | `truth-priority-hierarchy@1.1.0` — Truth Priority Hierarchy | evidence classes or authorities conflict |
| C | `citation-fidelity@1.1.0` — Citation Fidelity Gate | output contains citations or source-attributed claims |
| R | `fail-closed-abstention@1.1.0` — Fail-Closed Abstention | required evidence cannot be verified |
| R | `domain-mode-isolation@1.1.0` — Domain / Mode Isolation | multiple domains or semantic modes coexist |
| R | `parallel-qms@1.1.0` — Parallel Validation System | a composed workflow needs structured quality evaluation |

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
