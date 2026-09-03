# Education / Explanation — Runtime Pack

Purpose: Explain a subject for a defined learner and objective without sacrificing domain accuracy.

Task family: teaching, tutoring, and audience-adapted explanation

Activation boundary: Use when an explanation must be adapted to a named learner, objective, and prerequisite level while retaining domain accuracy.

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
| R | `pedagogical-alignment@1.1.0` — Pedagogical Alignment Constraint | an audience or teaching level is known |
| A | `explanation-minimality-scaffold@1.1.0` — Minimum Sufficient Explanation | verbosity can obscure the answer |
| A | `style-alignment@1.1.0` — Style-Alignment Module | a style or voice is specified |
| A | `grounding-no-invention@1.1.0` — Grounding / No-Invention | work relies on documents, data, external facts, or consequential claims |
| A | `micro-scaffolding@1.1.0` — Micro-Scaffolding | multi-step or high-constraint work |
| R | `task-set-lock-in@1.1.0` — Task-Set Lock-In | multi-step work begins or scope changes |
| A | `safe-rewrite@1.1.0` — Safe Rewrite Logic | paraphrasing, polishing, or format conversion |
| C | `anti-tunnel-vision@1.1.0` — Anti-Tunnel Vision | premature fixation could hide credible alternatives |
| C | `parallel-qms@1.1.0` — Parallel Validation System | a composed workflow needs structured quality evaluation |

## Runtime component cards

### R — Pedagogical Alignment Constraint

Purpose: Make correct content learnable and usable for a specified audience without diluting claims or inventing simplifications.

Activate when: an audience or teaching level is known.

Do not use when: the audience and purpose cannot be inferred and the choice materially changes content; exact legal or technical wording must remain verbatim.

Requires: none.

#### Runtime mechanism

Build a compact audience model—known prerequisites, target capability, jargon tolerance, and action context—then choose the smallest conceptual steps that bridge from that model to the target. Define or replace jargon at first use, order prerequisite before dependent ideas, add an example only where it resolves a likely misconception, and run an accuracy-backcheck against the unsimplified claim.

#### Procedure

1. Identify the reader's likely starting knowledge and the capability they need after reading.
2. List prerequisites and terms that the explanation currently assumes.
3. Sequence content from familiar anchor through the minimum conceptual bridge to the target.
4. Define necessary jargon or replace it with accurate plain language; add a representative example where abstraction alone is likely to fail.
5. Back-check every simplification, analogy, and example against the original technical claim and retain important limitations.

#### Guardrails

- Mandatory even on strong models: internal prerequisite model; accuracy back-check; boundary-preserving simplification.
- Conflict/precedence: Accuracy, scope, and uncertainty outrank ease of explanation; Exact source language is preserved in quoted or zero-drift zones and explained around rather than rewritten.
- Stop or fail when: oversimplification; undefined jargon.

Full package and provenance: [`pedagogical-alignment`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/output/pedagogical-alignment/UPGRADEABLE.md).

### A — Minimum Sufficient Explanation

Recovered name: Explanation Minimality Scaffold

Purpose: Remove explanatory material that does not change comprehension, verification, decision, or safe execution while retaining required rationale and caveats.

Activate when: verbosity can obscure the answer.

Do not use when: the user requests a tutorial or exhaustive rationale; high-stakes action requires full assumptions and warnings.

Requires: none.

#### Runtime mechanism

Set an explanation contract consisting of the outcome, the minimum causal or evidentiary bridge, required caveats, and the next action. Draft those blocks first, then test every additional sentence with a deletion probe: if removal does not impair correctness, comprehension, verification, safety, or actionability for the target reader, delete it. This mechanism is modern; only the exact historical scaffold name was recovered.

#### Procedure

1. Identify the reader, requested depth, decision or action, and risk tier.
2. List mandatory explanation blocks: answer, indispensable why, evidence or method needed for trust, caveats, and next action.
3. Draft one compact block for each mandatory need.
4. Run a deletion probe sentence by sentence against correctness, comprehension, verification, safety, and actionability.
5. Restore any deleted bridge whose absence creates a knowledge jump; stop when remaining content is necessary or explicitly requested.

#### Guardrails

- Mandatory even on strong models: reader-and-risk calibration; mandatory-block check; deletion probe.
- Conflict/precedence: User-requested detail and risk-mandated disclosure override brevity; When a deletion creates ambiguity about scope, uncertainty, or authority, restore the qualifying content.
- Stop or fail when: terse but unactionable output; missing causal bridge.

Full package and provenance: [`explanation-minimality-scaffold`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/output/explanation-minimality-scaffold/UPGRADEABLE.md).

### A — Style-Alignment Module

Purpose: Make artifacts consistent with audience, publication, or organizational style while keeping truth and requirements dominant.

Activate when: a style or voice is specified.

Do not use when: the requested style impersonates a living person or conflicts with policy; exact quoted language must remain untouched.

Requires: none.

#### Runtime mechanism

Translate the authorized style request into an observable style vector—tone, formality, sentence rhythm, vocabulary level, structure, formatting, and disallowed tendencies—while extracting a separate semantic invariant ledger. Transform surface choices toward the style vector, protect quoted and zero-drift zones, then score both conformance and semantic preservation; truth, task, and citation constraints veto any stylistic gain.

#### Procedure

1. Extract the authorized style source and convert it into observable positive and negative constraints.
2. Lock facts, reasoning relations, requirements, citations, uncertainty, and exact-text zones.
3. Revise diction, rhythm, organization, and formatting only where the style contract permits.
4. Compare the result against the style vector using representative passages rather than vague resemblance.
5. Run a semantic and citation diff; revert any stylistic change that alters truth, logic, or attribution.

#### Guardrails

- Mandatory even on strong models: explicit target dimensions; truth and task veto; semantic and citation back-check.
- Conflict/precedence: Truth, safety, citation fidelity, and explicit task constraints outrank the style guide; Exact quotations and legally controlled text are excluded from stylistic transformation.
- Stop or fail when: fact drift for tone; vague imitation.

Full package and provenance: [`style-alignment`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/output/style-alignment/UPGRADEABLE.md).

### A — Grounding / No-Invention

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

### A — Micro-Scaffolding

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

### A — Safe Rewrite Logic

Purpose: Make paraphrase, polish, tone, or formatting safe by treating content atoms as invariants rather than suggestions.

Activate when: paraphrasing, polishing, or format conversion.

Do not use when: the user asks to change substantive meaning; the source is internally contradictory and needs adjudication.

Requires: none.

#### Runtime mechanism

Extract a before-state ledger of factual and constraint atoms, mark the dimensions authorized to change, perform the rewrite only along those dimensions, then compare names, numbers, dates, quotes, citations, modality, requirements, and causal claims. Any atom difference not explicitly authorized is reverted or surfaced for approval.

#### Procedure

1. Identify authorized change dimensions such as tone, length, format, or reading level.
2. Extract locked atoms: claims, entities, numbers, dates, quotations, citations, requirements, negations, and uncertainty markers.
3. Rewrite without adding evidence or changing the locked atoms.
4. Diff the rewritten artifact against the atom ledger and inspect citation-to-claim fit.
5. Restore unauthorized changes and report any requested transformation that cannot preserve meaning.

#### Guardrails

- Mandatory even on strong models: internal atom extraction; authorized-dimension discipline; post-rewrite names/numbers/dates/quotes/citations check.
- Conflict/precedence: Truth and locked constraints outrank requested style; If shortening would remove a required qualification, keep the qualification or report the conflict.
- Stop or fail when: semantic drift; citation drift.

Full package and provenance: [`safe-rewrite`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/editing-repair/safe-rewrite/UPGRADEABLE.md).

### C — Anti-Tunnel Vision

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

Full package and provenance: [`parallel-qms`](https://github.com/robkazi52/upgradeables/blob/main/upgradeables/validation/parallel-qms/UPGRADEABLE.md).
