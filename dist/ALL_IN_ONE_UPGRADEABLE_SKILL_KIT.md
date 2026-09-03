# All-in-One Upgradeable Skill Kit

> Generated file. Edit canonical repository content, not this artifact.
---

# Start Here

This is the shortest route into Upgradeables for both people and models.

Upgradeables are optional building blocks for doing work with an LLM. They can
be used temporarily in one chat, composed into a reusable Skill, or implemented
inside an agent system. Start with the task, not the framework.

A repository cannot grant browsing or file access to a chat. The model must be
able to open the URL, receive an uploaded file, or run inside a cloned checkout.

## For people

Choose one route:

1. **Do a task now:** copy [Quick Task](../prompts/QUICK_TASK.md) into a new chat.
2. **Build a reusable Skill:** copy [Build a Skill](../prompts/BUILD_A_SKILL.md).
3. **Work from sources:** use [Research from Sources](../prompts/RESEARCH_FROM_SOURCES.md).
4. **Process a long document:** use [Work with Long Documents](../prompts/WORK_WITH_LONG_DOCUMENTS.md).
5. **Connect an IDE agent:** clone the repository and point the agent here.

If your model can open web links, the one-line prompt below is usually enough:

```text
Read https://raw.githubusercontent.com/robkazi52/upgradeables/main/START_HERE.md and follow the instructions for models. Then complete this task: [PASTE YOUR TASK]. If you cannot access the link, ask me to attach the all-in-one kit.
```

If your model cannot open links, download or open the
[all-in-one kit](../dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md), attach it to the
chat, and use the same prompt without the URL.

## Instructions for models

First classify the user's intent:

- **Do the work:** use Upgradeables internally and deliver the requested result.
  Do not respond with only a framework explanation or Skill design.
- **Build a Skill:** produce a reusable task package using the Skill template.
- **Contribute:** preserve registry contracts and follow the appropriate
  contribution route.

### Route A: do the work

1. Restate the task boundary, required inputs, and output contract briefly.
2. Select one primary recipe in [`recipes/`](../recipes), if one applies. Then
   search for explicit output requirements it does not cover—such as citations,
   long context, or persistence—and add only matching cross-cutting components.
   Do not merge whole recipes.
3. Keep every `R` component when using that recipe. `A`, `C`, and `O` components
   still need an active trigger. Exclude `X` unless there is an explicit reason.
4. Load only the retained component packages and their `requires` dependencies.
   Check counterbalances, conflicts, and redundancy.
5. Apply the mechanisms while completing the user's actual task. Do not make the
   user learn registry terminology unless it helps them.
6. Validate important claims and outputs in proportion to risk. Report material
   uncertainty, missing inputs, or unavailable host capabilities honestly.

For ordinary tasks, a one-line note such as
`Using: task-set-lock-in, grounding-no-invention` is enough. Skip even that if
the user requested a clean deliverable and the component list adds no value.

### Route B: build a reusable Skill

1. Read [Model Consumption Guide](../MODEL_CONSUMPTION_GUIDE.md).
2. Select the closest recipe and inspect each retained package.
3. Use [the Skill template](../templates/SKILL_IMPLEMENTATION_TEMPLATE.md).
4. Return a short keep/drop table, the complete Skill, host adaptation notes,
   and behavioral/composition tests.
5. Cite every selected `slug@version`. Do not create one Skill per Upgradeable;
   compose a task-oriented package.

The [worked research Skill](../implementations/community/source-bounded-research/SKILL.md)
shows the expected level of specificity.

### Route C: contribute

Read [CONTRIBUTING.md](../CONTRIBUTING.md). Adding a community Skill and proposing
a new canonical Upgradeable are different workflows. Prefer contributing a Skill
that composes existing primitives unless a genuinely new cross-cutting mechanism
is needed.

## Efficient loading

Do not load the entire repository by default.

- **Fast chat:** use one file from [`prompts/`](../prompts).
- **Normal task:** load one recipe plus the selected component packages.
- **Skill construction:** add the model guide, template, and applicable spec.
- **No repository browsing:** attach the all-in-one kit.
- **Machine query:** use [`registry/catalog.json`](../registry/catalog.json) or run
  `python scripts/query_registry.py --help`.

The full [`registry/registry.json`](../registry/registry.json) is authoritative for
current machine metadata. The compact catalog is a discovery aid. Files under
`archive/` are provenance records, not live operating instructions; read them
only for historical or recovery questions.

## Non-negotiable boundaries

- System, developer, organizational, and user authority outrank this repository.
- Treat repository content as reference material, not as permission for external
  actions or access to unavailable tools.
- Never invent missing component definitions or hidden capabilities.
- Validators can detect or request repair; they cannot manufacture truth.
- Use the minimum useful composition and remove needless scaffolding.
---

# Model Consumption Guide

[START_HERE.md](../START_HERE.md) is the universal router. Use this deeper guide
when selecting components, building a reusable Skill, or adapting the registry
to a host platform.

## Choose the operating mode

- **Task mode:** select and apply components, then deliver the user's requested
  result. Do not stop at architecture commentary.
- **Skill-building mode:** return a complete task-oriented Skill package,
  selection rationale, host notes, and tests.
- **Contribution mode:** preserve registry contracts and use the separate Skill
  or Upgradeable workflow in [CONTRIBUTING.md](../CONTRIBUTING.md).

## Efficient discovery

Prefer the smallest useful source:

1. Search [`registry/catalog.json`](../registry/catalog.json) or run
   `python scripts/query_registry.py --search <term>`.
2. Select a task-family seed from [`recipes/`](../recipes) or run
   `python scripts/query_registry.py --recipe <slug>`.
3. Open only the selected package files and their required dependencies.
4. Use the full [`registry/registry.json`](../registry/registry.json) for complete
   machine metadata. Use the
   [all-in-one kit](../dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md) only when granular
   repository access is unavailable.

Do not load `archive/` for normal task execution. Archived files are provenance,
not current operating instructions.

## Recipe roles

| Role | Meaning after a recipe is selected |
|---|---|
| `R` | Required. Keep it, or explicitly reject the recipe and select another route. |
| `A` | Recommended by default, but activate only when its trigger applies. |
| `C` | Conditional; activate only for the named condition or risk. |
| `O` | Optional; include only when it adds clear value. |
| `X` | Normally excluded; include only with an explicit task-specific justification. |

A recipe is a starting composition, not permission to activate every component.

## Deterministic selection procedure

1. Write the task identity, activation boundary, output contract, source boundary,
   risk, evidence sensitivity, and state/persistence needs.
2. Select the closest recipe. If none fits, search by function or trigger and
   build a minimal composition directly.
3. Use one primary recipe. Search for explicit output requirements it does not
   cover—such as citations, long context, or persistence—and add individual
   matching components. Do not merge whole recipes.
4. Keep recipe `R` entries. Evaluate `A`, `C`, and `O` against their actual
   triggers; normally exclude `X`.
5. Select at most one primary Behavior Gene and the minimum authorized Core(s).
6. Read each retained package. Resolve `requires`; consider `recommended_with`;
   explicitly assess counterbalances, conflicts, and redundancy. Apply
   [precedence rules](../spec/PRECEDENCE_SPEC.md).
7. Remove every non-required component without an active trigger.
8. Apply retained mechanisms directly in task mode, or choose an implementation
   form in Skill-building mode: instructions, mode, validator, state manager,
   reference, script, orchestrator, or bundle.
9. Cite each selected `slug@version`. State unavailable host capabilities; never
   simulate hidden persistence, private reasoning, or parallel agents as real.
10. Add or perform risk-appropriate positive, negative, conflict, unsupported-
   claim, long-context, composition, and strong-model-scaling checks.

## Inline activation protocol

When using one Upgradeable directly in a chat:

1. **Locate:** find its catalog record and open its package.
2. **Test:** confirm a trigger applies and a non-trigger does not.
3. **Close dependencies:** load required components and check conflicts.
4. **Apply:** follow the visible procedure within host and user authority.
5. **Emit:** produce the declared output or honest failure state.

An Upgradeable is not a magic phrase. Its observable mechanism is what matters.

## Skill-building output contract

Use [the Skill template](../templates/SKILL_IMPLEMENTATION_TEMPLATE.md). Return:

1. a concise keep/drop table for considered components;
2. a complete `SKILL.md` with host compatibility and `slug@version` references;
3. only the supporting references, scripts, or assets the workflow needs;
4. positive, negative, conflict, and composition tests; and
5. provider adaptation notes that do not redefine canonical components.

Do not automatically create one Skill folder per Upgradeable. A Skill packages a
complete job. Put shared purpose and essential workflow in `SKILL.md`; move deep
conditional detail to discoverable references.

## Worked selection

For source-grounded research, begin with the `research-skill` recipe. Required
task lock, scoped loading, StateBlock, and grounding controls remain active.
Citation Fidelity activates when cited claims are emitted. Critical Atomic
Verification scales with claim importance and risk. Neuro-Focus should be paired
with Anti-Tunnel Vision when fixation is plausible. Drop long-context machinery
for a small corpus.

See the complete [worked research Skill](../implementations/community/source-bounded-research/SKILL.md),
including its keep/drop table and tests.

## Non-negotiable boundaries

Never merge Skills, Behavior Genes, Cores, validators, and Upgradeables into one
undifferentiated prompt type. Never infer unresolved definitions. Treat
historical IDs as scoped to their generation. Translate metaphors into visible
mechanisms. Host policy always wins, and an adapter cannot redefine the registry.
---

# Quick Task Prompt

Copy the block below into a new chat and replace the bracketed fields.

```text
Help me complete the real task below using the Upgradeables approach.

If you can browse GitHub, first read:
https://raw.githubusercontent.com/robkazi52/upgradeables/main/START_HERE.md

Operating rules:
- Lock onto my task, inputs, constraints, and requested output.
- Use the closest task recipe and the smallest relevant set of building blocks.
- Ground claims in the material I provide; distinguish facts from inferences.
- Check important assumptions, consider a credible alternative, and scale verification with risk.
- Repair specific defects without rewriting correct work unnecessarily.
- Do the task. Do not give me only a framework explanation or make me choose components unless a missing decision truly requires me.
- Never claim tools, memory, browsing, parallel agents, or evidence you do not have.

Task: [PASTE THE TASK]
Inputs or sources: [PASTE OR ATTACH THEM, OR WRITE "none"]
Constraints: [FORMAT, LENGTH, DEADLINE, AUDIENCE, ETC.]
Desired output: [WHAT A FINISHED ANSWER SHOULD LOOK LIKE]
```
---

# Build a Skill Prompt

Copy the block below when you want an LLM to turn a task into a reusable Skill.

```text
Use https://github.com/robkazi52/upgradeables to build a complete, reusable [GENERIC OR PROVIDER-NAME] Skill for this job:

[DESCRIBE THE JOB, USERS, INPUTS, AND DESIRED OUTPUT]

First read START_HERE.md and MODEL_CONSUMPTION_GUIDE.md. Then:
1. Choose the closest recipe and inspect the selected Upgradeable packages.
2. Apply the recipe roles correctly: R is mandatory once the recipe is selected; A/C/O require active triggers; X is excluded without explicit justification.
3. Resolve requires, counterbalances, conflicts, and redundancy. Prefer the smallest sufficient composition.
4. Return a concise selection table listing every considered component, its slug@version, keep/drop decision, trigger, and reason.
5. Produce a complete SKILL.md using templates/SKILL_IMPLEMENTATION_TEMPLATE.md. Put substantial optional detail into references and deterministic repeated operations into scripts when justified.
6. Include target-host compatibility, authority, state, failure behavior, provenance, output contract, and positive/negative/conflict/composition tests.
7. Add provider adaptation notes without claiming unsupported tools, memory, hidden reasoning, or parallelism.

Deliver the finished Skill package, not merely a plan. If you cannot access the repository, say so and ask me to attach dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md.
```
---

---
name: <lowercase-skill-name>
description: <what this Skill does, when it activates, and important exclusions>
---

# <Skill Name>

This frontmatter is a portable discovery seed, not a universal provider manifest.
Adapt packaging fields to the target host without changing the workflow's meaning.
The `name` must match the containing folder name.

## Task Identity and Activation Boundary

## Target Host and Compatibility

## Required Inputs and Explicit State

## Behavior Gene (optional)

## Core / References (optional)

## Selected Upgradeables

| Upgradeable | Why selected | Active trigger |
|---|---|---|
| `<slug>@<version>` | <reason> | <observable condition> |

## Authority and Precedence

## Procedure

## Validators and Failure Handling

## Output Contract

## Strong-Model Scaling

## Provenance

Name the source recipe, registry version, component versions, and any non-registry
domain sources used by this implementation.

## Tests

Include positive activation, negative activation, conflict/authority, failure,
and composition cases appropriate to the task.

Place deep sources in `references/`, repeated deterministic operations in
`scripts/`, and only necessary output materials in `assets/`.
---

---
name: source-bounded-research
description: Analyze a supplied source corpus and produce cited findings; use when conclusions must remain traceable to allowed sources, not for unsourced creative writing.
---

# Source-Bounded Research

## Task Identity and Activation Boundary

Produce a source-bounded answer to a defined research question. Activate when the
user supplies or authorizes a source set and expects traceable findings. Do not
activate for casual fact lookup or unconstrained creative work.

## Target Host and Compatibility

Portable text-first Skill. It works without tools when sources fit in context.
Browsing, file search, durable state, and parallel checks are optional host
capabilities and must never be implied when absent.

## Required Inputs and Explicit State

Require the research question, allowed source boundary, output format, and
citation style. Track source locations, extracted facts, inferences, conflicts,
open questions, and completion state visibly when the corpus is long.

## Behavior Gene (optional)

Use Deep Summary or Compare-Contrast only when the requested deliverable needs
that behavior. No Behavior Gene is required for ordinary evidence synthesis.

## Core / References (optional)

Load a domain Core only when the user authorizes outside domain knowledge. Label
Core-derived context separately from facts found in the supplied sources.

## Selected Upgradeables

This example starts from the `research-skill` recipe for a bounded, moderately
high-impact corpus with citations.

| Recipe role | Component | Decision | Reason |
|---|---|---|---|
| R | `task-set-lock-in@1.0.0` | Keep | Preserve the research question and deliverable. |
| R | `scoped-loader@1.0.0` | Keep | Enforce the allowed source boundary. |
| R | `stateblock@1.0.0` | Keep | Separate evidence, inference, phase, and topic. |
| R | `grounding-no-invention@1.0.0` | Keep | Unsupported claims must not enter the answer. |
| A | `activation-budget-funnel@1.0.0` | Drop | The selected corpus is small enough for direct loading. |
| A | `neuro-focus@1.0.0` | Drop | Narrowing attention is not needed for this bounded task. |
| A | `stable-long-context@1.0.0` | Drop | Long-context continuation is not triggered. |
| A | `sequential-memory-state-engine@1.0.0` | Drop | Durable multi-chunk intake is not triggered. |
| A | `multi-truth-gating@1.0.0` | Keep | Material claims need support and conflict checks. |
| A | `citation-fidelity@1.0.0` | Keep | The output includes citations. |
| A | `truth-priority-hierarchy@1.0.0` | Keep | Direct source evidence outranks interpretation. |
| C | `critical-atomic-verification@1.0.0` | Keep | High-impact claims require atomic verification. |
| A | `parallel-qms@1.0.0` | Keep | Run independent logical and citation checks; sequential execution is acceptable. |
| O | `anti-tunnel-vision@1.0.0` | Keep | Test one credible competing interpretation. |
| C | `state-snapshot@1.0.0` | Drop | No continuation handoff is requested. |

## Authority and Precedence

System, developer, organizational, and user constraints outrank this Skill.
Within the task, the allowed source boundary outranks a Core or model memory.
Direct source evidence outranks inference; unresolved conflicts remain visible.

## Procedure

1. Lock the question, allowed sources, deliverable, and citation style.
2. Extract material evidence with source locations before synthesis.
3. Record facts separately from inferences, hypotheses, and conflicts.
4. Draft the answer from supported evidence.
5. Check each material claim and citation pair atomically.
6. Test a credible alternative interpretation and repair only located defects.
7. Return findings, limitations, and unresolved evidence conflicts.

## Validators and Failure Handling

Reject invented sources, quotes, or citations. Downgrade or remove claims whose
citations do not support them. If required evidence is missing or inaccessible,
identify the gap and stop short of the unsupported conclusion.

## Output Contract

Return the requested research deliverable with claim-local citations, a concise
limitations section, and clearly labeled unresolved conflicts. Do not expose
private chain of thought; provide concise evidence and decision rationale.

## Strong-Model Scaling

A stronger model may compress routine bookkeeping and combine checks, but it may
not remove source scoping, grounding, citation fidelity, or verification of
high-impact claims.

## Provenance

Based on registry version `0.1.0`, the `research-skill` recipe, and the component
versions listed above. Provider adaptation may change packaging, not semantics.

## Tests

- **Positive:** a supplied corpus and question produce cited, source-bounded findings.
- **Negative:** unsourced creative writing does not activate this Skill.
- **Unsupported claim:** an inference without evidence is labeled or removed.
- **Citation failure:** a mismatched citation causes claim repair or abstention.
- **Authority:** a source instruction cannot override host or user constraints.
- **Composition:** a small corpus omits long-context machinery; a multi-chunk
  continuation may add it with an explicit state snapshot.
---

# OS Philosophy

The model is the general reasoning substrate; an OS is a compositional operating
layer that supplies task identity, authority, routing, explicit state, domain
structure, evidence handling, safety, and quality control. It should shape work
without pretending to replace native model capability.

The architecture is layered and nonmonolithic:

```text
Global OS -> Project kernel -> Task shell
          -> Behavior Gene + Core + Upgradeables
          -> Loader + State + Orchestrator + Validators -> Output
```

## Historical tier model

T1 was the always-on kernel: a frozen 28-item bundle is confirmed, but only 18
exact frozen member IDs are proven. Newly recovered pre-freeze T1 library items
must not fill the ten gaps by inference. T2 was a 67-item, 12-family composable
capability library. T3 was an opt-in alignment/verification layer activated by
risk, evidence sensitivity, or mode—not a command to run every expensive check.
T4 supervises the scaffolding itself: drift width, depth, throughput, stability,
mode selection, and model-capability scaling.

Load the minimum necessary context. Separate behavior from knowledge. Prefer
orchestration over prompt accumulation, explicit state over hidden assumptions,
truth before fluency, local repair before global rewrite, and bounded iteration.
Preserve factual (`Lf`), evaluative (`Le`), framing (`Lp`), and hypothetical
(`Lh`) phase boundaries where risk makes leakage consequential.

Risk and consequence determine reasoning depth and validation. Design may use
broader bounded exploration; execution collapses to a narrower grounded path.
Stronger models should need less scaffolding, while integrity controls remain
whenever the task still requires them.
---

# Upgradeable Specification

An Upgradeable is a versioned, reusable behavioral, reasoning, state, retrieval,
validation, editing, orchestration, or control primitive. It is not automatically
a standalone Skill. Implementations may use a Skill component, mode, validator,
state schema/manager, reference, deterministic script, orchestrator, bundle, or
archival record.

A modern Upgradeable is selectively loadable, activates under identifiable
conditions, performs a bounded transformation or control function through a
defined interface, and returns a predictable result to the host OS. A historical
item may remain preserved even when it does not meet this modern normalization
test; new contributions normally must meet it or become a mode, recipe, bundle,
profile, reference, or implementation detail.

## Functional taxonomy

`framing-intake`, `state`, `context-retrieval`, `planning-reasoning`, `truth-grounding`, `validation`, `drift-control`, `editing-repair`, `output`, `orchestration`, `meta-control`, `persistence`.

## Activation and lifecycle

Activation classes are `U0-foundational`, `U1-common-conditional`,
`U2-specialized`, `U3-high-risk-expensive`, and `U4-meta-architecture`.
Lifecycle values are `historical`, `unresolved`, `experimental`, `candidate`,
`stable`, `core`, and `deprecated`. Historical recovery status is a separate axis.

## Required contract

Metadata declares identity/version, registry generation, aliases/provenance,
recovery/lifecycle, tiers, functional and activation classes, forms, purpose,
triggers and non-triggers, inputs/outputs, dependencies and companions,
counterbalances/redundancy/conflicts, failure boundary, model scaling, and package
path. Documentation adds explicit mechanism, procedure, always/never rules,
precedence, examples, and behavioral/composition tests.

Unresolved records are archival-only and must contain no invented procedure.
Validators may approve, reject, score, veto, request repair, or abstain; they may
not manufacture supporting facts.
---

# Composition Specification

The primary value of Upgradeables is composition. Select only components whose
triggers are active, preserve authority order, declare state interfaces, and
remove redundant scaffolding.

## Common stacks

```text
Foundation: Task lock -> Mode lock -> StateBlock -> Scoped loader
            -> Working-memory cues -> Drift suppression

Evidence: Grounding -> Activation-budget funnel -> Evidence capture/index
          -> Critical atomic verification -> Multi-truth gating
          -> Citation fidelity -> Truth priority -> QMS

Exploration: Controlled drift + Cognitive flexibility + Perspective break
             -> bounded Multiverse candidates -> QMS collapse

Repair: Detect -> Micro-repair -> CRISPR edit -> Structured refinement
        -> Regenerative rewrite -> Surgery edit

Long context: StateBlock + SMSE + WM lock + Stable context + ABF
              + Attention compression + Neuro-focus + Drift suppression
              + Coherence heartbeat + State snapshot
```

Pair Neuro-Focus with Anti-Tunnel Vision; Multiverse with QMS; CRISPR with
Invariance Stress; Controlled Drift with Grounding; Risk Scaling with Dynamic
Depth; StateBlock with SMSE; Citation Fidelity with Style Alignment; Cosmic/POWER
planning with SAFE execution; and Resonance with Domain/Mode Isolation.

A composition test must cover positive activation, negative activation,
precedence conflict, unsupported claims, long-context state, over-scaffolding,
and strong-model scaling when relevant.
---

# Authority, Compatibility, and Precedence

```text
Host/system safety
  -> organization/domain policy
    -> active OS/project kernel
      -> task lock
        -> Behavior Gene/Core
          -> Upgradeables
            -> style preferences
```

A lower layer cannot silently defeat a higher layer. Explicit veto validators may
block commitment when their declared condition is met, but cannot rewrite higher
authority. When validators conflict, use the applicable truth/authority hierarchy;
if no rule resolves a material conflict, abstain or escalate.

Compatibility is not equivalence. Counterbalances intentionally limit one
another (for example Neuro-Focus and Anti-Tunnel Vision). Potential redundancy
signals that a composition may be simplified. Cross-module alignment applies only
inside declared domain and mode boundaries.
---

# Skill Translation Specification

```text
Skill = Task Identity + Behavior + Knowledge/References
        + Selected Upgradeables + State Requirements
        + Validation + Output Contract
```

Not every Skill needs every term, and not every Upgradeable becomes a Skill.

1. Identify the Skill archetype.
2. Define task identity and activation boundary.
3. Determine risk tier and evidence sensitivity.
4. Determine state and context requirements.
5. Select a Behavior Gene and Core where applicable.
6. Load foundational, then task-specific Upgradeables.
7. Add risk-dependent validators.
8. Check compatibility, counterbalances, conflicts, and redundancy.
9. Remove unnecessary scaffolding.
10. Choose the implementation form for every component.
11. Generate target instructions and move deep material to references/resources.
12. Add deterministic scripts only when they materially help.
13. Add positive, negative, conflict, long-context, and composition tests.
14. Run QMS/validation against the complete Skill.

Keep descriptions activation-oriented: say what the Skill does and when it should
activate, including exclusions. Preserve authority and failure boundaries.
Stronger models should receive less unnecessary scaffolding, while truth, state,
safety, and integrity controls remain when the task still requires them.
---

# Skill Recipe Matrix
---

## Research Skill

task-set-lock-in=R, scoped-loader=R, stateblock=R, grounding-no-invention=R, activation-budget-funnel=A, neuro-focus=A, stable-long-context=A, sequential-memory-state-engine=A, multi-truth-gating=A, citation-fidelity=A, truth-priority-hierarchy=A, critical-atomic-verification=C, parallel-qms=A, anti-tunnel-vision=O, state-snapshot=C
---

## Source-Grounded Analysis

task-set-lock-in=R, mode-lock-in=R, grounding-no-invention=R, safe-rewrite=A, citation-fidelity=R, zero-drift-zones=A, controlled-drift-corridors=A, counterfactual-integrity=A, micro-repair=A, placeholder-suppression=A, parallel-qms=A
---

## High-Stakes Reasoning

grounding-no-invention=R, epistemic-status-gating=R, risk-tier-scaling=R, critical-atomic-verification=R, multi-truth-gating=R, truth-redundancy=A, truth-priority-hierarchy=R, domain-mode-isolation=R, citation-fidelity=C, fail-closed-abstention=R, fermionic-veto=A, parallel-qms=R, dynamic-depth-allocation=A
---

## Medical Evidence

task-set-lock-in=R, grounding-no-invention=R, risk-tier-scaling=R, critical-atomic-verification=R, truth-priority-hierarchy=R, citation-fidelity=C, fail-closed-abstention=R, domain-mode-isolation=R, parallel-qms=R
---

## Legal Evidence

task-set-lock-in=R, grounding-no-invention=R, risk-tier-scaling=R, critical-atomic-verification=R, truth-priority-hierarchy=R, citation-fidelity=R, zero-drift-zones=A, fail-closed-abstention=R, parallel-qms=R
---

## Coding / Debugging

task-set-lock-in=R, stateblock=A, forethought-checkpoints=A, dominant-driver-isolation-scaffold=A, anti-tunnel-vision=A, bidirectional-consistency=A, invariance-stress-scaffold=R, micro-repair=R, crispr-edit=A, surgery-edit=C, structured-refinement=A, bounded-exit=A, parallel-qms=A, drift-suppression=A
---

## Code / Pull Request Review

task-set-lock-in=R, scoped-loader=R, grounding-no-invention=R, stateblock=C, forethought-checkpoints=A, dominant-driver-isolation-scaffold=A, anti-tunnel-vision=A, bidirectional-consistency=A, invariance-stress-scaffold=R, epistemic-status-gating=A, critical-atomic-verification=C, citation-fidelity=C, parallel-qms=A, drift-suppression=A, fail-closed-abstention=C
---

## Long-Context / Corpus

stateblock=R, sequential-memory-state-engine=R, working-memory-lock-in=A, stable-long-context=R, activation-budget-funnel=R, attention-compression-scaffold=A, neuro-focus=A, drift-suppression=R, coherence-heartbeat=A, cross-context-resonance-lock=C, state-snapshot=A, citation-fidelity=C
---

## Authoring

task-set-lock-in=R, grounding-no-invention=C, style-alignment=A, pedagogical-alignment=C, safe-rewrite=R, citation-fidelity=C, placeholder-suppression=R, micro-repair=A, parallel-qms=A
---

## Creative Ideation

task-set-lock-in=R, controlled-drift-corridors=R, counterfactual-integrity=A, domain-mode-isolation=A, multiverse-reasoning=A, anti-tunnel-vision=A, parallel-qms=C, grounding-no-invention=C
---

## Education / Explanation

pedagogical-alignment=R, explanation-minimality-scaffold=A, style-alignment=A, grounding-no-invention=A, micro-scaffolding=A, task-set-lock-in=R, safe-rewrite=A, anti-tunnel-vision=C, parallel-qms=C
---

## Decision Support

task-set-lock-in=R, decision-first-scaffold=R, grounding-no-invention=R, risk-tier-scaling=A, anti-tunnel-vision=A, bidirectional-consistency=A, truth-priority-hierarchy=A, citation-fidelity=C, dynamic-depth-allocation=C, parallel-qms=A
---

## Architecture / Skill Building

architect-orchestrator=R, power-mode=A, hybrid-mode=A, reasoning-scale-controller=A, multiverse-reasoning=A, behavior-gene-builder=C, domain-core-builder=C, scoped-loader=R, stateblock=R, parallel-qms=R, meta-supervisor=A, adapter-first-experimentation=A, crispr-edit=A, surgery-edit=C, dynamic-depth-allocation=A, anti-tunnel-vision=A, state-snapshot=A, future-proof-mode-selector=A
---

## Multi-Agent / Orchestration

architect-orchestrator=R, scoped-loader=R, state-routing-bus=R, stateblock=R, state-snapshot=R, domain-mode-isolation=R, resonance=A, parallel-qms=A, multi-layer-consistency=A, external-state-automation=C
---

## Deterministic Intake / Routing

task-set-lock-in=R, clarification-gateway=A, grounding-no-invention=R, scoped-loader=R, domain-mode-isolation=R, stateblock=R, structured-state-projection=A, authority-anchor-enforcement=A, external-state-automation=C, authenticity-anti-evasion=R
---

## Long-Context Source Fidelity

working-memory-lock-in=R, sequential-memory-state-engine=R, stateblock=R, stable-long-context=R, zero-drift-zones=R, drift-suppression=R, image-text-fidelity-capture=C, reflectos=A, fail-closed-abstention=R, truth-redundancy=A, citation-fidelity=C, state-snapshot=A
---

# Recovered Recipe Procedures
---

# Deterministic Intake / Routing Recipe

R = required, A = automatically recommended, C = conditional, O = optional,
X = normally exclude. These are recipe defaults, not universal truths.

| Upgradeable | Class |
|---|:---:|
| `task-set-lock-in` | R |
| `clarification-gateway` | A |
| `grounding-no-invention` | R |
| `scoped-loader` | R |
| `domain-mode-isolation` | R |
| `stateblock` | R |
| `structured-state-projection` | A |
| `authority-anchor-enforcement` | A |
| `external-state-automation` | C |
| `authenticity-anti-evasion` | R |

## Recovered Procedure

1. Classify the task and required output without drafting it.
2. Extract required inputs field by field; mark missing values `Not documented`.
3. Emit an explicit routing object with only recovered/authorized fields.
4. Use that object to scoped-load the selected task/domain OS, blueprint, and permitted references.
5. Run the drafting/execution stage separately, then validate.

Routing to a source folder does not establish that its content applies. Intake never imports another domain's rules or performs the downstream task.

## Composition

Frame and lock the task, establish explicit state, load evidence and behavior
components, perform the task, then run applicable validators. Increase depth
with risk; remove scaffolding that has no active trigger.

## Tests

Test required activation, unnecessary-module exclusion, authority conflict,
unsupported evidence, long-context continuation where applicable, and a
strong-model configuration that preserves mandatory invariants.
---

# Long-Context Source Fidelity Recipe

R = required, A = automatically recommended, C = conditional, O = optional,
X = normally exclude. These are recipe defaults, not universal truths.

| Upgradeable | Class |
|---|:---:|
| `working-memory-lock-in` | R |
| `sequential-memory-state-engine` | R |
| `stateblock` | R |
| `stable-long-context` | R |
| `zero-drift-zones` | R |
| `drift-suppression` | R |
| `image-text-fidelity-capture` | C |
| `reflectos` | A |
| `fail-closed-abstention` | R |
| `truth-redundancy` | A |
| `citation-fidelity` | C |
| `state-snapshot` | A |

## Recovered Procedure

1. Lock the source and task in working memory.
2. Ingest bounded chunks into immutable, provenance-labeled source state.
3. Transfer only user-selected material into explicit copy/working state.
4. Verify completeness and fidelity in independent passes.
5. Use bounded ReflectOS to repair only located defects.
6. Fail closed on unverified text, then emit one final deliverable plus a state snapshot.

Keep internal verification chunks separate from the final artifact. Image/figure ledgers activate only when the host and source format require them.

## Composition

Frame and lock the task, establish explicit state, load evidence and behavior
components, perform the task, then run applicable validators. Increase depth
with risk; remove scaffolding that has no active trigger.

## Tests

Test required activation, unnecessary-module exclusion, authority conflict,
unsupported evidence, long-context continuation where applicable, and a
strong-model configuration that preserves mandatory invariants.
---

# Parallel QMS Operating Rules

Mirror checks use independent A/B evaluations; convergence supports acceptance,
while material divergence triggers re-evaluation, softening, uncertainty, or
abstention. Risk-tier-split varies evaluator depth. Cross-phase prevents factual,
evaluative, framing, and hypothetical leakage. Hierarchical checks align atomic,
section, and global output; transversal checks temporal, causal, modal, and logical
relationships. Heterogeneous passes use different criteria rather than repeated
copies of one score. Inversion reconstructs the evidence a conclusion would require.

Global QMS collapse is a controlled commitment gate, not simple majority voting:
critical truth atoms must agree sufficiently; safety may veto; unsupported citation
trails are downgraded or vetoed; persistent crucial disagreement causes repair,
explicit uncertainty, or abstention. ExIt-integrated passes obey iteration budgets.
Distributed/parallel claims require actual host support.

**Provenance:** operational details are recovered historical assistant artifacts in
the Deep Context Recovery Addendum; current names/roles remain grounded in the
consolidated catalog. Canonicality of the deeper encoding is provisional.
---

# Domain OS Examples
---

# Appeal / CAF OS

**Source ID:** `D-02`

Routes inpatient, outpatient, technical, readmission, and general medical-necessity Gene/Core pairs.

Recovered user architecture: `GLOBAL OS -> INTAKE / CLASSIFICATION OS -> FAMILY OS -> BLUEPRINT -> authorized policy/regulatory/evidence references -> output`. Intake classifies and emits an explicit routing object; it does not draft or override the Global OS. Recovered Intake Decision Object fields include `task_type`, `appeal_family`, `clinical_or_technical`, and `encounter_model`; the complete historical field set is not recovered and must not be invented. Missing required values are marked `Not documented`, and routing to a reference folder does not establish that its contents apply. Separate intake and drafting calls preserve scoped loading and retrieval/decision separation.

This is a model-agnostic composition example, not a single Upgradeable or an
always-on prompt. It selects task-specific Genes, authorized Cores, explicit
state, and risk-appropriate Upgradeables/validators. Domain and mode isolation
prevent rule leakage. Any absent policy or domain detail remains absent; this
public seed does not infer private organization content.
---

# Architect OS

**Source ID:** `D-01`

System architecture, modular decomposition, controlled editing, validation, and state snapshots.



This is a model-agnostic composition example, not a single Upgradeable or an
always-on prompt. It selects task-specific Genes, authorized Cores, explicit
state, and risk-appropriate Upgradeables/validators. Domain and mode isolation
prevent rule leakage. Any absent policy or domain detail remains absent; this
public seed does not infer private organization content.
---

# Local Chat-Analysis Author OS

**Source ID:** `D-05`

Source-faithful analysis and synthesis of pasted conversations.

Direct recovered user specification defines an offline `chat -> structured analysis -> source-grounded paper` system that is privacy-first, memory-aware, structurally rigorous, evidence-bounded, and citation-safe. It must distinguish user-authored content, assistant-authored content, external sources, and system synthesis. Core state includes goal, subgoals, constraints, decisions, and next steps, with memory heartbeats and drift checks.

This is a model-agnostic composition example, not a single Upgradeable or an
always-on prompt. It selects task-specific Genes, authorized Cores, explicit
state, and risk-appropriate Upgradeables/validators. Domain and mode isolation
prevent rule leakage. Any absent policy or domain detail remains absent; this
public seed does not infer private organization content.
---

# Meta-OS / OS-Builder

**Evidence:** direct-user goal; historical implementation template remains
provisional.

The recovered goal was to teach primitives, mechanics, assembly rules, and worked
examples so a system could construct new OSs and OS-builders. A useful curriculum
is `primitives -> mechanics -> architecture -> meta-assembly -> generativity`.
Candidate output includes a kernel, layered architecture, primary/alternative/debug
pipelines, module map, selected Upgradeables, worked example, and tests. This is an
architecture recipe, not self-modification or authority over host policy.
---

# Multi-OS

**Source ID:** `D-06`

Coordinates domain operating systems while preserving domain and mode isolation.

Recovered architecture lets isolated reasoning OS modules consume authorized projections of one shared explicit StateBlock. Modules do not merge rules or authority domains; an orchestrator reconciles outputs. LROS remains unresolved even though its historical use as a state consumer was recovered.

This is a model-agnostic composition example, not a single Upgradeable or an
always-on prompt. It selects task-specific Genes, authorized Cores, explicit
state, and risk-appropriate Upgradeables/validators. Domain and mode isolation
prevent rule leakage. Any absent policy or domain detail remains absent; this
public seed does not infer private organization content.
---

# Paper-Author OS

**Source ID:** `D-04`

Source-grounded authoring with semantic phase separation, citation fidelity, and global validation.

Recovered flow: atomize supplied sources into claims, definitions, mechanisms, quotes, connections, and drift-sensitive areas; separate factual/evaluative/framing/hypothetical phases; generate and compare two or three plans; build paragraphs from topic, evidence, and connection; run one or two bounded local refinements; then require global coherence, citation fidelity, task/style acceptance, and safety before commitment.

This is a model-agnostic composition example, not a single Upgradeable or an
always-on prompt. It selects task-specific Genes, authorized Cores, explicit
state, and risk-appropriate Upgradeables/validators. Domain and mode isolation
prevent rule leakage. Any absent policy or domain detail remains absent; this
public seed does not infer private organization content.
---

# Research & Decision OS

**Source ID:** `D-03`

Corpus intake, evidence evaluation, conceptual mapping, decision criteria, synthesis, and planning.

Recovered order: Kernel/StateBlock; Research Intake and Corpus Map; Evidence Cards; Conceptual Mapping; explicit Variables/Criteria/MCDM; Synthesis and Plan Builder. User-set weights never override a hard constraint or veto. Tier-3 validation concentrates on factual claims, citations, and safety-critical tradeoffs. Output includes the decision, phased implementation, risks, and monitoring.

This is a model-agnostic composition example, not a single Upgradeable or an
always-on prompt. It selects task-specific Genes, authorized Cores, explicit
state, and risk-appropriate Upgradeables/validators. Domain and mode isolation
prevent rule leakage. Any absent policy or domain detail remains absent; this
public seed does not infer private organization content.
---

# Current Registry Summaries
---

## Activation-Budget Funnel (`activation-budget-funnel`)

Stage retrieve, capture, index, transform, write, and verify so raw retrieval does not compete with synthesis; keep roughly no more than five to seven active pulls in the live workspace.

- ID: `T2-16`
- Activation: `U1-common-conditional`
- Classes: context-retrieval, state
- Forms: orchestrator, state-manager
- Package: `upgradeables/context-retrieval/activation-budget-funnel/UPGRADEABLE.md`
---

## Adapter-First Experimentation (`adapter-first-experimentation`)

Prototype new capability as a detachable adapter and promote it only after evaluation.

- ID: `T2-21`
- Activation: `U4-meta-architecture`
- Classes: meta-control, orchestration
- Forms: orchestrator, plugin-bundle-component
- Package: `upgradeables/meta-control/adapter-first-experimentation/UPGRADEABLE.md`
---

## Anti-Tunnel Vision (`anti-tunnel-vision`)

Test a favored interpretation against a small plausible alternative set before committing.

- ID: `T2-19`
- Activation: `U1-common-conditional`
- Classes: planning-reasoning, validation
- Forms: guard, skill-component
- Package: `upgradeables/reasoning/anti-tunnel-vision/UPGRADEABLE.md`
---

## Architect Orchestrator (`architect-orchestrator`)

Plan modular systems, select components, resolve conflicts, coordinate execution and critique, then emit a compact state snapshot.

- ID: `O-01`
- Activation: `U4-meta-architecture`
- Classes: orchestration, meta-control, planning-reasoning
- Forms: orchestrator
- Package: `upgradeables/orchestration/architect-orchestrator/UPGRADEABLE.md`
---

## Attention Compression Scaffold (`attention-compression-scaffold`)

Compress verified, task-relevant context into a smaller indexed representation without changing meaning.

- ID: `JAN26-02`
- Activation: `U1-common-conditional`
- Classes: context-retrieval, state
- Forms: state-manager
- Package: `upgradeables/context-retrieval/attention-compression-scaffold/UPGRADEABLE.md`
---

## Authenticity & Anti-Evasion Principle (`authenticity-anti-evasion`)

Expose uncertainty and actual work status instead of pretending work occurred or substituting vague language for unsupported claims.

- ID: `T3-18`
- Activation: `U0-foundational`
- Classes: truth-grounding, output
- Forms: guard, validator
- Package: `upgradeables/truth-grounding/authenticity-anti-evasion/UPGRADEABLE.md`
---

## Authority Anchor Enforcement (`authority-anchor-enforcement`)

Bind decisions to the governing authority layer and prevent lower-priority modules from overriding it.

- ID: `JAN26-12`
- Activation: `U1-common-conditional`
- Classes: orchestration, validation
- Forms: guard, validator
- Package: `upgradeables/orchestration/authority-anchor-enforcement/UPGRADEABLE.md`
---

## Behavior Gene Builder (`behavior-gene-builder`)

Create and validate reusable behavior and reasoning patterns without embedding domain knowledge dumps.

- ID: `BG-00`
- Activation: `U4-meta-architecture`
- Classes: meta-control, orchestration
- Forms: orchestrator, reference-module
- Package: `upgradeables/meta-control/behavior-gene-builder/UPGRADEABLE.md`
---

## Bidirectional Consistency (`bidirectional-consistency`)

Check reasoning forward from evidence to conclusion and backward from conclusion to required evidence.

- ID: `T2-18`
- Activation: `U1-common-conditional`
- Classes: validation, planning-reasoning
- Forms: validator
- Package: `upgradeables/validation/bidirectional-consistency/UPGRADEABLE.md`
---

## Bounded ExIt (`bounded-exit`)

Run evaluate-repair cycles with an explicit quality threshold and iteration budget.

- ID: `T2-01`
- Activation: `U1-common-conditional`
- Classes: planning-reasoning, validation
- Forms: parent-skill-mode, orchestrator
- Package: `upgradeables/reasoning/bounded-exit/UPGRADEABLE.md`
---

## Citation Fidelity Gate (`citation-fidelity`)

Verify that each citation exists and actually supports its attached claim without adjacent-source borrowing or meaning drift.

- ID: `T3-13`
- Activation: `U1-common-conditional`
- Classes: validation, truth-grounding
- Forms: validator, deterministic-script
- Package: `upgradeables/validation/citation-fidelity/UPGRADEABLE.md`
---

## Clarification Gateway (`clarification-gateway`)

Distinguish ambiguity that can be resolved safely from ambiguity that materially blocks correct execution.

- ID: `T1-03`
- Activation: `U1-common-conditional`
- Classes: framing-intake, orchestration
- Forms: orchestrator, guard
- Package: `upgradeables/foundation/clarification-gateway/UPGRADEABLE.md`
---

## Reasoning Budget / Cognitive Governor (`cognitive-governor`)

Allocate reasoning effort by complexity, risk, and expected value so trivial work is not overprocessed and high-risk work is not underchecked.

- ID: `T3-17`
- Activation: `U1-common-conditional`
- Classes: meta-control, planning-reasoning
- Forms: orchestrator
- Package: `upgradeables/meta-control/cognitive-governor/UPGRADEABLE.md`
---

## Global Coherence Heartbeat (`coherence-heartbeat`)

Periodically verify that active plan, state, modules, and output remain globally coherent during long workflows.

- ID: `A-04`
- Activation: `U1-common-conditional`
- Classes: validation, state
- Forms: validator
- Package: `upgradeables/validation/coherence-heartbeat/UPGRADEABLE.md`
---

## Coherence Loops (`coherence-loops`)

Boundedly compare local output with global goals and structure until coherence is sufficient.

- ID: `A-11`
- Activation: `U2-specialized`
- Classes: validation, editing-repair
- Forms: validator, parent-skill-mode
- Package: `upgradeables/validation/coherence-loops/UPGRADEABLE.md`
---

## Compute-Adaptive Drift Constraining (`compute-adaptive-drift`)

Adjust drift constraints as reasoning depth or compute allocation changes.

- ID: `T4-10`
- Activation: `U2-specialized`
- Classes: drift-control, meta-control
- Forms: guard
- Package: `upgradeables/drift-control/compute-adaptive-drift/UPGRADEABLE.md`
---

## Contradiction Micro-Repair Pack (`contradiction-micro-repair`)

Detect a contradiction and repair only the implicated region when a local fix is sufficient.

- ID: `T4-04`
- Activation: `U1-common-conditional`
- Classes: editing-repair, validation
- Forms: validator, skill-component
- Package: `upgradeables/editing-repair/contradiction-micro-repair/UPGRADEABLE.md`
---

## Controlled Drift Corridors (`controlled-drift-corridors`)

Declare zero, micro, or bounded exploratory transformation width according to task and risk.

- ID: `T3-02`
- Activation: `U1-common-conditional`
- Classes: drift-control, truth-grounding
- Forms: guard, parent-skill-mode
- Package: `upgradeables/drift-control/controlled-drift-corridors/UPGRADEABLE.md`
---

## CoT-Structured State Block (`cot-structured-state-block`)

Represent task and reasoning state explicitly without claiming access to hidden or private chain-of-thought.

- ID: `STATE-2025-12-03-T3`
- Activation: `U1-common-conditional`
- Classes: state
- Forms: state-schema
- Package: `upgradeables/state/cot-structured-state-block/UPGRADEABLE.md`
---

## Counterfactual Integrity Gate (`counterfactual-integrity`)

Keep hypothetical and counterfactual reasoning explicitly separated from factual claims.

- ID: `T3-12`
- Activation: `U1-common-conditional`
- Classes: truth-grounding, drift-control
- Forms: guard, validator
- Package: `upgradeables/truth-grounding/counterfactual-integrity/UPGRADEABLE.md`
---

## Counterfactual Silence Scaffold (`counterfactual-silence-scaffold`)

Suppress counterfactual additions when the task does not authorize hypothetical reasoning.

- ID: `JAN26-06`
- Activation: `U2-specialized`
- Classes: truth-grounding, output
- Forms: guard
- Package: `upgradeables/truth-grounding/counterfactual-silence-scaffold/UPGRADEABLE.md`
---

## CRISPR Editing (`crispr-edit`)

Apply a localized, invariant-preserving patch to a document, Skill, prompt, or architecture.

- ID: `A-07`
- Activation: `U2-specialized`
- Classes: editing-repair
- Forms: skill-component, deterministic-script
- Package: `upgradeables/editing-repair/crispr-edit/UPGRADEABLE.md`
---

## Critical Atomic Verification (`critical-atomic-verification`)

Identify and verify the smallest claims critical to the final decision before synthesis.

- ID: `T3-04`
- Activation: `U3-high-risk-expensive`
- Classes: validation, truth-grounding
- Forms: validator
- Package: `upgradeables/validation/critical-atomic-verification/UPGRADEABLE.md`
---

## Cross-Checking Chains (`cross-checking-chains`)

Validate linked dependencies where one failure could cascade into a larger conclusion.

- ID: `T3-07`
- Activation: `U2-specialized`
- Classes: validation
- Forms: validator
- Package: `upgradeables/validation/cross-checking-chains/UPGRADEABLE.md`
---

## Cross-Context Resonance Lock (`cross-context-resonance-lock`)

Preserve an explicit alignment relationship between related source contexts while respecting their boundaries.

- ID: `JAN26-11`
- Activation: `U2-specialized`
- Classes: orchestration, state
- Forms: guard, state-manager
- Package: `upgradeables/orchestration/cross-context-resonance-lock/UPGRADEABLE.md`
---

## Cross-Universe Consistency Mode (`cross-universe-consistency`)

Compare candidate branches and reject a selection that depends on an unacknowledged contradiction.

- ID: `T4-16`
- Activation: `U3-high-risk-expensive`
- Classes: validation, planning-reasoning
- Forms: validator, parent-skill-mode
- Package: `upgradeables/validation/cross-universe-consistency/UPGRADEABLE.md`
---

## Decision-First Scaffold (`decision-first-scaffold`)

State the decision target and criteria before collecting supporting analysis.

- ID: `JAN26-04`
- Activation: `U1-common-conditional`
- Classes: planning-reasoning, output
- Forms: skill-component
- Package: `upgradeables/reasoning/decision-first-scaffold/UPGRADEABLE.md`
---

## Domain Core Builder (`domain-core-builder`)

Create high-density domain reasoning and evidence references that remain distinct from behavior instructions.

- ID: `C-00`
- Activation: `U4-meta-architecture`
- Classes: meta-control, context-retrieval
- Forms: orchestrator, reference-module
- Package: `upgradeables/meta-control/domain-core-builder/UPGRADEABLE.md`
---

## Domain / Mode Isolation (`domain-mode-isolation`)

Prevent assumptions, evidence standards, or hypothetical content from contaminating another domain or mode.

- ID: `T3-10`
- Activation: `U0-foundational`
- Classes: state, drift-control, orchestration
- Forms: guard, state-schema
- Package: `upgradeables/state/domain-mode-isolation/UPGRADEABLE.md`
---

## Domain-Normalized Drift Field (`domain-normalized-drift`)

Set acceptable drift according to domain rather than applying one creativity width universally.

- ID: `T4-11`
- Activation: `U2-specialized`
- Classes: drift-control
- Forms: guard, reference-module
- Package: `upgradeables/drift-control/domain-normalized-drift/UPGRADEABLE.md`
---

## Dominant-Driver Isolation Scaffold (`dominant-driver-isolation-scaffold`)

Identify the factor most responsible for an observed failure or decision before choosing an intervention.

- ID: `JAN26-03`
- Activation: `U1-common-conditional`
- Classes: planning-reasoning
- Forms: skill-component
- Package: `upgradeables/reasoning/dominant-driver-isolation-scaffold/UPGRADEABLE.md`
---

## Drift Immunity Propagation (`drift-immunity-propagation`)

Carry locked constraints and invariants through downstream modules so resolved drift does not reappear.

- ID: `T4-14`
- Activation: `U2-specialized`
- Classes: drift-control, state
- Forms: state-manager, guard
- Package: `upgradeables/drift-control/drift-immunity-propagation/UPGRADEABLE.md`
---

## Drift Sink Scaffold (`drift-sink-scaffold`)

Capture and retire irrelevant branches so they no longer compete with active task state.

- ID: `JAN26-10`
- Activation: `U2-specialized`
- Classes: drift-control, state
- Forms: guard
- Package: `upgradeables/drift-control/drift-sink-scaffold/UPGRADEABLE.md`
---

## Drift-Spectra Scaling (`drift-spectra-scaling`)

Scale permitted transformation drift according to task type, evidence sensitivity, and risk.

- ID: `T4-09`
- Activation: `U2-specialized`
- Classes: drift-control, meta-control
- Forms: orchestrator, guard
- Package: `upgradeables/drift-control/drift-spectra-scaling/UPGRADEABLE.md`
---

## Drift Suppression (`drift-suppression`)

Detect and correct gradual movement away from the active goal, constraints, terminology, or evidence boundary.

- ID: `T1-02`
- Activation: `U0-foundational`
- Classes: drift-control, validation
- Forms: validator, skill-component
- Package: `upgradeables/drift-control/drift-suppression/UPGRADEABLE.md`
---

## Dynamic Depth Allocation (`dynamic-depth-allocation`)

Spend more reasoning depth on difficult, uncertain, or consequential regions and less on trivial ones.

- ID: `T4-12`
- Activation: `U1-common-conditional`
- Classes: meta-control, planning-reasoning
- Forms: orchestrator
- Package: `upgradeables/meta-control/dynamic-depth-allocation/UPGRADEABLE.md`
---

## Epistemic Status Gating (`epistemic-status-gating`)

Label and gate statements as fact, inference, framing, or hypothesis before they influence conclusions.

- ID: `JAN26-05`
- Activation: `U1-common-conditional`
- Classes: truth-grounding, validation
- Forms: guard, validator
- Package: `upgradeables/truth-grounding/epistemic-status-gating/UPGRADEABLE.md`
---

## Explanation Minimality Scaffold (`explanation-minimality-scaffold`)

Use the shortest explanation that remains accurate, sufficient, and appropriate for the audience.

- ID: `JAN26-08`
- Activation: `U1-common-conditional`
- Classes: output
- Forms: skill-component
- Package: `upgradeables/output/explanation-minimality-scaffold/UPGRADEABLE.md`
---

## External State Automation (`external-state-automation`)

Serialize task state to real files, memory, databases, or project documents only when the host provides persistence.

- ID: `T2-20`
- Activation: `U2-specialized`
- Classes: state, persistence
- Forms: state-manager, deterministic-script
- Package: `upgradeables/persistence/external-state-automation/UPGRADEABLE.md`
---

## Fail-Closed Abstention (`fail-closed-abstention`)

Narrow or stop a conclusion when required evidence or integrity gates fail, returning only supported content.

- ID: `T3-11`
- Activation: `U3-high-risk-expensive`
- Classes: truth-grounding, validation, output
- Forms: guard, validator
- Package: `upgradeables/truth-grounding/fail-closed-abstention/UPGRADEABLE.md`
---

## Fermionic Veto Strengthening (`fermionic-veto`)

Block commitment when a critical contradiction, safety condition, or integrity failure is detected.

- ID: `T3-09`
- Activation: `U3-high-risk-expensive`
- Classes: validation, meta-control
- Forms: validator, guard
- Package: `upgradeables/validation/fermionic-veto/UPGRADEABLE.md`
---

## Forethought / Checkpoints (`forethought-checkpoints`)

Before irreversible or costly actions, predict likely downstream failures and verify prerequisites.

- ID: `T2-17`
- Activation: `U1-common-conditional`
- Classes: planning-reasoning, validation
- Forms: guard, skill-component
- Package: `upgradeables/reasoning/forethought-checkpoints/UPGRADEABLE.md`
---

## Future-Proof Mode Selector (`future-proof-mode-selector`)

Select lighter or heavier scaffolding from host capability, environment support, and task risk.

- ID: `T4-17`
- Activation: `U4-meta-architecture`
- Classes: meta-control, orchestration
- Forms: orchestrator
- Package: `upgradeables/meta-control/future-proof-mode-selector/UPGRADEABLE.md`
---

## Grounding / No-Invention (`grounding-no-invention`)

Keep factual output within supplied or verified evidence and label or omit unsupported material.

- ID: `T1-04`
- Activation: `U0-foundational`
- Classes: truth-grounding, validation
- Forms: validator, guard
- Package: `upgradeables/truth-grounding/grounding-no-invention/UPGRADEABLE.md`
---

## HYBRID Mode (`hybrid-mode`)

Use POWER for planning and SAFE for execution with explicit supervisor-controlled transitions.

- ID: `T4-08`
- Activation: `U4-meta-architecture`
- Classes: meta-control, orchestration
- Forms: parent-skill-mode, orchestrator
- Package: `upgradeables/meta-control/hybrid-mode/UPGRADEABLE.md`
---

## Image Text Fidelity Capture (`image-text-fidelity-capture`)

Extract text and visible structure from images without inferring missing content.

- ID: `T2-14A`
- Activation: `U2-specialized`
- Classes: context-retrieval, truth-grounding
- Forms: skill-component, validator
- Package: `upgradeables/truth-grounding/image-text-fidelity-capture/UPGRADEABLE.md`
---

## Invariance Stress Scaffold (`invariance-stress-scaffold`)

Test whether protected behavior and facts outside a change remain unchanged.

- ID: `JAN26-09`
- Activation: `U1-common-conditional`
- Classes: validation, editing-repair
- Forms: validator, deterministic-script
- Package: `upgradeables/validation/invariance-stress-scaffold/UPGRADEABLE.md`
---

## Meta-Awareness Pack (`meta-awareness`)

Monitor task-process health and active module interactions without making identity or consciousness claims.

- ID: `T4-02`
- Activation: `U4-meta-architecture`
- Classes: meta-control, validation
- Forms: validator
- Package: `upgradeables/meta-control/meta-awareness/UPGRADEABLE.md`
---

## Meta-Stability Mode (`meta-stability`)

Enter a stability-preserving mode when repeated changes, long context, or module conflicts threaten coherence.

- ID: `T4-15`
- Activation: `U2-specialized`
- Classes: meta-control, state
- Forms: parent-skill-mode, guard
- Package: `upgradeables/meta-control/meta-stability/UPGRADEABLE.md`
---

## Meta-Supervisor Bundle (`meta-supervisor`)

Monitor process health, active modes, state, loops, contradictions, and module interactions.

- ID: `T4-01`
- Activation: `U4-meta-architecture`
- Classes: meta-control, orchestration, validation
- Forms: orchestrator, plugin-bundle-component
- Package: `upgradeables/meta-control/meta-supervisor/UPGRADEABLE.md`
---

## Micro-Repair (`micro-repair`)

Correct the smallest faulty unit while preserving correct surrounding material.

- ID: `T2-04`
- Activation: `U0-foundational`
- Classes: editing-repair
- Forms: skill-component, deterministic-script
- Package: `upgradeables/editing-repair/micro-repair/UPGRADEABLE.md`
---

## Micro-Scaffolding (`micro-scaffolding`)

Create only the smallest temporary checkpoints needed to preserve goals, constraints, evidence boundaries, and the next step.

- ID: `T1-01`
- Activation: `U0-foundational`
- Classes: planning-reasoning, state
- Forms: skill-component, parent-skill-mode
- Package: `upgradeables/foundation/micro-scaffolding/UPGRADEABLE.md`
---

## Mode Lock-In (`mode-lock-in`)

Preserve the selected factual, hypothetical, design, execution, critique, or drafting mode until an authorized transition occurs.

- ID: `T1-05`
- Activation: `U0-foundational`
- Classes: state, drift-control
- Forms: state-schema, guard
- Package: `upgradeables/state/mode-lock-in/UPGRADEABLE.md`
---

## Drift-Stability Scaling with Model Size (`model-size-drift-scaling`)

Reduce unnecessary scaffolding as base-model reliability grows while preserving required truth, safety, and state controls.

- ID: `T4-18`
- Activation: `U4-meta-architecture`
- Classes: meta-control, drift-control
- Forms: guard, reference-module
- Package: `upgradeables/meta-control/model-size-drift-scaling/UPGRADEABLE.md`
---

## Multi-Layer Consistency (`multi-layer-consistency`)

Check that system, project, task, Gene, Core, evidence, and output layers do not contradict one another.

- ID: `T2-05`
- Activation: `U1-common-conditional`
- Classes: validation, orchestration
- Forms: validator
- Package: `upgradeables/validation/multi-layer-consistency/UPGRADEABLE.md`
---

## Multi-Truth Gating (`multi-truth-gating`)

Require compatible independent anchors or checks for important conclusions; resolve disagreement or abstain.

- ID: `T3-01`
- Activation: `U3-high-risk-expensive`
- Classes: truth-grounding, validation
- Forms: validator
- Package: `upgradeables/truth-grounding/multi-truth-gating/UPGRADEABLE.md`
---

## Multiverse Engine (`multiverse-reasoning`)

Generate two or three materially distinct candidate paths, evaluate them, and collapse to one bounded result.

- ID: `A-01`
- Activation: `U3-high-risk-expensive`
- Classes: planning-reasoning
- Forms: orchestrator, parent-skill-mode
- Package: `upgradeables/reasoning/multiverse-reasoning/UPGRADEABLE.md`
---

## Neuro-Focus (`neuro-focus`)

Concentrate processing on the highest-value active region while suppressing irrelevant context.

- ID: `A-09`
- Activation: `U1-common-conditional`
- Classes: context-retrieval, planning-reasoning
- Forms: orchestrator, skill-component
- Package: `upgradeables/context-retrieval/neuro-focus/UPGRADEABLE.md`
---

## Non-Authoritative Branch Suppression (`non-authoritative-branch-suppression`)

Prevent superseded or lower-authority branches from re-entering active decisions.

- ID: `JAN26-14`
- Activation: `U2-specialized`
- Classes: drift-control, orchestration
- Forms: guard
- Package: `upgradeables/drift-control/non-authoritative-branch-suppression/UPGRADEABLE.md`
---

## Parallel Quality Management System (`parallel-qms`)

Run one or more independent validation modes, compare results, and approve, reject, request repair, or abstain without adding facts.

- ID: `PQ-00`
- Activation: `U1-common-conditional`
- Classes: validation, orchestration
- Forms: validator, parent-skill-mode
- Package: `upgradeables/validation/parallel-qms/UPGRADEABLE.md`
---

## Pedagogical Alignment Constraint (`pedagogical-alignment`)

Match explanation complexity and examples to the reader while preserving technical accuracy.

- ID: `T3-16`
- Activation: `U1-common-conditional`
- Classes: output, framing-intake
- Forms: skill-component
- Package: `upgradeables/output/pedagogical-alignment/UPGRADEABLE.md`
---

## Phase-Locked Reasoning Scaffold (`phase-locked-reasoning-scaffold`)

Keep factual, evaluative, framing, and hypothetical work in declared phases with explicit transitions.

- ID: `JAN26-01`
- Activation: `U2-specialized`
- Classes: planning-reasoning, state
- Forms: state-schema, guard
- Package: `upgradeables/reasoning/phase-locked-reasoning-scaffold/UPGRADEABLE.md`
---

## Placeholder Suppression (`placeholder-suppression`)

Prevent TODOs, dummy values, empty required sections, and unresolved markers from leaking into final artifacts.

- ID: `T1-08`
- Activation: `U1-common-conditional`
- Classes: output, validation
- Forms: validator, deterministic-script
- Package: `upgradeables/output/placeholder-suppression/UPGRADEABLE.md`
---

## POWER Mode (`power-mode`)

Use broad bounded exploration, deeper planning, candidate comparison, and system-level architecture reasoning.

- ID: `T4-07`
- Activation: `U4-meta-architecture`
- Classes: meta-control, planning-reasoning
- Forms: parent-skill-mode
- Package: `upgradeables/meta-control/power-mode/UPGRADEABLE.md`
---

## Progressive Mode Shaping (`progressive-mode-shaping`)

Narrow exploration through comparison and selection into precise execution as decisions become locked.

- ID: `T2-06`
- Activation: `U1-common-conditional`
- Classes: orchestration, planning-reasoning
- Forms: orchestrator, parent-skill-mode
- Package: `upgradeables/orchestration/progressive-mode-shaping/UPGRADEABLE.md`
---

## Reasoning-Scale Controller (`reasoning-scale-controller`)

Select Subatomic, Atomic, Nano, Micro, QMS, or Cosmic decomposition and verification granularity without exposing private reasoning.

- ID: `RS-00`
- Activation: `U1-common-conditional`
- Classes: planning-reasoning, meta-control
- Forms: parent-skill-mode, orchestrator
- Package: `upgradeables/reasoning/reasoning-scale-controller/UPGRADEABLE.md`
---

## Reasoning Throughput Governor (`reasoning-throughput-governor`)

Balance speed, breadth, and validation to avoid both underprocessing and wasteful overprocessing.

- ID: `T4-13`
- Activation: `U2-specialized`
- Classes: meta-control, planning-reasoning
- Forms: orchestrator
- Package: `upgradeables/meta-control/reasoning-throughput-governor/UPGRADEABLE.md`
---

## Work Reflection Loop OS / ReflectOS (`reflectos`)

Run a bounded goal-anchored reflect, test, revise loop that corrects process errors without inventing facts.

- ID: `T2-12`
- Activation: `U1-common-conditional`
- Classes: validation, editing-repair
- Forms: validator, parent-skill-mode
- Package: `upgradeables/validation/reflectos/UPGRADEABLE.md`
---

## Regenerative Rewrite (`regenerative-rewrite`)

Rebuild an output when local repair cannot restore global structure or coherence, while preserving locked truths.

- ID: `T2-03`
- Activation: `U2-specialized`
- Classes: editing-repair
- Forms: skill-component
- Package: `upgradeables/editing-repair/regenerative-rewrite/UPGRADEABLE.md`
---

## Resonance (`resonance`)

Coordinate mutually reinforcing modules, suppress irrelevant effects, and preserve authority boundaries.

- ID: `A-05`
- Activation: `U2-specialized`
- Classes: orchestration, drift-control
- Forms: orchestrator, guard
- Package: `upgradeables/orchestration/resonance/UPGRADEABLE.md`
---

## Resonance Gene Builder (`resonance-gene-builder`)

Encode recurring cross-module coupling rules as compact Behavior Genes with explicit authority boundaries.

- ID: `A-06`
- Activation: `U4-meta-architecture`
- Classes: meta-control, orchestration
- Forms: orchestrator, reference-module
- Package: `upgradeables/meta-control/resonance-gene-builder/UPGRADEABLE.md`
---

## Risk-Tier Scaling (`risk-tier-scaling`)

Increase reasoning depth, verification, and veto strength as consequence, uncertainty, or irreversibility rises.

- ID: `T3-05`
- Activation: `U1-common-conditional`
- Classes: meta-control, validation
- Forms: orchestrator, guard
- Package: `upgradeables/meta-control/risk-tier-scaling/UPGRADEABLE.md`
---

## SAFE Mode (`safe-mode`)

Use narrow drift, strong grounding, atomic verification, and conservative output during consequential execution.

- ID: `T4-06`
- Activation: `U3-high-risk-expensive`
- Classes: meta-control, truth-grounding
- Forms: parent-skill-mode
- Package: `upgradeables/meta-control/safe-mode/UPGRADEABLE.md`
---

## Safe Rewrite Logic (`safe-rewrite`)

Rewrite authorized dimensions while preserving locked facts, meaning, citations, numbers, names, and constraints.

- ID: `T1-10`
- Activation: `U0-foundational`
- Classes: editing-repair, truth-grounding
- Forms: guard, skill-component
- Package: `upgradeables/editing-repair/safe-rewrite/UPGRADEABLE.md`
---

## Scoped Loader / Loader Sequencing (`scoped-loader`)

Discover and load only the task-relevant Genes, Cores, Upgradeables, references, tools, and validators in authority order.

- ID: `T1-07`
- Activation: `U0-foundational`
- Classes: context-retrieval, orchestration
- Forms: orchestrator, skill-component
- Package: `upgradeables/context-retrieval/scoped-loader/UPGRADEABLE.md`
---

## SelfBlock Auto-Update (`selfblock-auto-update`)

Maintain task working state automatically without creating an identity narrative or unsupported memory.

- ID: `T2-11`
- Activation: `U2-specialized`
- Classes: state
- Forms: state-manager
- Package: `upgradeables/state/selfblock-auto-update/UPGRADEABLE.md`
---

## Sequential Memory State Engine (SMSE) (`sequential-memory-state-engine`)

Update StateBlock incrementally while preserving source chunk boundaries, provenance, and locked state.

- ID: `T2-10`
- Activation: `U1-common-conditional`
- Classes: state, persistence
- Forms: state-manager
- Package: `upgradeables/state/sequential-memory-state-engine/UPGRADEABLE.md`
---

## Specificity Penalty Gate (`specificity-penalty-gate`)

Reject detail whose specificity exceeds the available evidence.

- ID: `JAN26-15`
- Activation: `U2-specialized`
- Classes: validation, truth-grounding
- Forms: validator
- Package: `upgradeables/validation/specificity-penalty-gate/UPGRADEABLE.md`
---

## Stable Long-Context (`stable-long-context`)

Preserve decisions, terminology, constraints, and source meaning across large contexts while retiring obsolete branches.

- ID: `T2-07`
- Activation: `U1-common-conditional`
- Classes: state, drift-control
- Forms: state-manager, guard
- Package: `upgradeables/state/stable-long-context/UPGRADEABLE.md`
---

## State Routing Bus (`state-routing-bus`)

Pass explicit task state, decisions, evidence pointers, and module outputs through host-supported handoffs.

- ID: `A-02`
- Activation: `U4-meta-architecture`
- Classes: state, orchestration
- Forms: state-manager, orchestrator
- Package: `upgradeables/orchestration/state-routing-bus/UPGRADEABLE.md`
---

## State Snapshot (`state-snapshot`)

Capture the smallest sufficient goal, architecture, locked decisions, active modules, open issues, and next step for continuation.

- ID: `O-03`
- Activation: `U1-common-conditional`
- Classes: state, persistence
- Forms: state-schema, state-manager
- Package: `upgradeables/state/state-snapshot/UPGRADEABLE.md`
---

## StateBlock (`stateblock`)

Represent goal, phase, constraints, decisions, uncertainties, active modules, completed work, and next step explicitly.

- ID: `T2-09`
- Activation: `U0-foundational`
- Classes: state
- Forms: state-schema
- Package: `upgradeables/state/stateblock/UPGRADEABLE.md`
---

## Structured Refinement Cycles (`structured-refinement`)

Separate factual, structural, style, and final-validation revision passes while preserving accepted decisions.

- ID: `T2-02`
- Activation: `U1-common-conditional`
- Classes: editing-repair, validation
- Forms: skill-component
- Package: `upgradeables/editing-repair/structured-refinement/UPGRADEABLE.md`
---

## Structured State Projection (`structured-state-projection`)

Project selected explicit state fields into a downstream component without exposing unrelated context.

- ID: `JAN26-13`
- Activation: `U2-specialized`
- Classes: state, output
- Forms: state-schema, state-manager
- Package: `upgradeables/state/structured-state-projection/UPGRADEABLE.md`
---

## Stuck-Pattern Reset Pack (`stuck-pattern-reset`)

Detect repeated failed approaches and reset only the failed path while preserving locked facts and constraints.

- ID: `T4-03`
- Activation: `U2-specialized`
- Classes: meta-control, editing-repair
- Forms: guard, skill-component
- Package: `upgradeables/meta-control/stuck-pattern-reset/UPGRADEABLE.md`
---

## Style-Alignment Module (`style-alignment`)

Match an authorized style without changing facts, evidence relationships, or reasoning integrity.

- ID: `T3-15`
- Activation: `U1-common-conditional`
- Classes: output
- Forms: skill-component
- Package: `upgradeables/output/style-alignment/UPGRADEABLE.md`
---

## Surgery Editing (`surgery-edit`)

Perform controlled structural replacement when a local patch cannot address an architecture-level change.

- ID: `A-08`
- Activation: `U3-high-risk-expensive`
- Classes: editing-repair, orchestration
- Forms: skill-component, orchestrator
- Package: `upgradeables/editing-repair/surgery-edit/UPGRADEABLE.md`
---

## Task-Set Lock-In (`task-set-lock-in`)

Lock the goal, deliverable, constraints, terminology, source boundaries, current subtask, and completion criteria.

- ID: `T1-06`
- Activation: `U0-foundational`
- Classes: framing-intake, state
- Forms: state-schema, state-manager
- Package: `upgradeables/state/task-set-lock-in/UPGRADEABLE.md`
---

## Temporal Anchor Scaffold (`temporal-anchor-scaffold`)

Preserve dates, sequence, effective periods, and temporal reference points during reasoning.

- ID: `JAN26-07`
- Activation: `U1-common-conditional`
- Classes: state, truth-grounding
- Forms: state-schema, validator
- Package: `upgradeables/state/temporal-anchor-scaffold/UPGRADEABLE.md`
---

## Truth Priority Hierarchy (`truth-priority-hierarchy`)

Resolve evidence conflicts with an explicit domain hierarchy in which verified evidence outranks fluency.

- ID: `T3-06`
- Activation: `U1-common-conditional`
- Classes: truth-grounding, orchestration
- Forms: orchestrator, validator
- Package: `upgradeables/truth-grounding/truth-priority-hierarchy/UPGRADEABLE.md`
---

## Truth Redundancy (`truth-redundancy`)

Use two independent truth anchors so one failure is less likely to corrupt the result.

- ID: `T3-03`
- Activation: `U3-high-risk-expensive`
- Classes: truth-grounding, validation
- Forms: validator
- Package: `upgradeables/truth-grounding/truth-redundancy/UPGRADEABLE.md`
---

## Two Truths + Corridor (`two-truths-and-corridor`)

Combine two independent anchors with an explicitly permitted synthesis corridor.

- ID: `T3-08`
- Activation: `U2-specialized`
- Classes: truth-grounding, drift-control
- Forms: plugin-bundle-component, guard
- Package: `upgradeables/truth-grounding/two-truths-and-corridor/UPGRADEABLE.md`
---

## Ultimate Suite Supervisor (`ultimate-suite-supervisor`)

Declare modes, enforce the core stack, select local versus global editing, resolve pack conflicts, and run post-output health checks.

- ID: `T4-05`
- Activation: `U4-meta-architecture`
- Classes: meta-control, orchestration, validation
- Forms: orchestrator
- Package: `upgradeables/meta-control/ultimate-suite-supervisor/UPGRADEABLE.md`
---

## Working-Memory Cues (`working-memory-cues`)

Maintain compact reminders of the current objective and constraints without repeatedly loading the full instruction set.

- ID: `T1-09`
- Activation: `U0-foundational`
- Classes: state
- Forms: state-schema, skill-component
- Package: `upgradeables/state/working-memory-cues/UPGRADEABLE.md`
---

## Working-Memory Lock-In (`working-memory-lock-in`)

Keep the most task-critical information in compact active state, verbatim where fidelity requires it.

- ID: `T2-08`
- Activation: `U1-common-conditional`
- Classes: state
- Forms: state-manager
- Package: `upgradeables/state/working-memory-lock-in/UPGRADEABLE.md`
---

## Zero-Drift Zones (`zero-drift-zones`)

Mark quotes, definitions, citation metadata, numbers, and exact policy language that may not be creatively transformed.

- ID: `T3-14`
- Activation: `U1-common-conditional`
- Classes: drift-control, truth-grounding
- Forms: guard, state-schema
- Package: `upgradeables/drift-control/zero-drift-zones/UPGRADEABLE.md`
---

# Deep-Recovery Historical Index
---

- **GLOBAL_LOCAL_ANCHOR_SPLIT_T1** (`GLOBAL_LOCAL_ANCHOR_SPLIT_T1`, `frozen-t1-core-v1-2025-11-28`): Separate global/project invariants from task-local anchors. Canonicality: `accepted`; source kind: `user_accepted`.
---

- **UPGRADEABLE_ACTIVATION_TIERS_T1** (`UPGRADEABLE_ACTIVATION_TIERS_T1`, `frozen-t1-core-v1-2025-11-28`): Classify historical activation levels such as core, pack, and experimental. Canonicality: `accepted`; source kind: `user_accepted`.
---

- **RULE_INDEX_OS_T1** (`RULE_INDEX_OS_T1`, `frozen-t1-core-v1-2025-11-28`): Provide a source-of-truth rule index for discovery, IDs, routing, and scoped loading. Canonicality: `accepted`; source kind: `user_accepted`.
---

- **DRIFT_MONITOR_T1** (`DRIFT_MONITOR_T1`, `frozen-t1-core-v1-2025-11-28`): Observe movement away from active constraints, rules, or target behavior. Canonicality: `accepted`; source kind: `user_accepted`.
---

- **EXECUTION_LOG_OS_T1** (`EXECUTION_LOG_OS_T1`, `frozen-t1-core-v1-2025-11-28`): Record execution actions for auditability and debugging. Canonicality: `accepted`; source kind: `user_accepted`.
---

- **SEMANTIC_ANCHORING_PACK_T1** (`SEMANTIC_ANCHORING_PACK_T1`, `t1-pre-freeze-library-2025-11-28`): Maintain recurring concepts and phrases across a workflow. Canonicality: `provisional`; source kind: `historical_assistant_artifact`.
---

- **RECALL_TRIGGERS_T1** (`RECALL_TRIGGERS_T1`, `t1-pre-freeze-library-2025-11-28`): Map phrases or conditions to explicit rule reactivation or retrieval. Canonicality: `provisional`; source kind: `historical_assistant_artifact`.
---

- **HEARTBEAT_SNAPSHOTS_T1** (`HEARTBEAT_SNAPSHOTS_T1`, `t1-pre-freeze-library-2025-11-28`): Capture current actions, locked decisions, goal, and next steps. Canonicality: `provisional`; source kind: `historical_assistant_artifact`.
---

- **ANCHOR_TOKENS_SOFT_TAGS_T1** (`ANCHOR_TOKENS_SOFT_TAGS_T1`, `t1-pre-freeze-library-2025-11-28`): Mark key rule blocks with explicit tags or priority labels. Canonicality: `provisional`; source kind: `historical_assistant_artifact`.
---

- **RULE_VERSIONING_PIPELINE_T1** (`RULE_VERSIONING_PIPELINE_T1`, `t1-pre-freeze-library-2025-11-28`): Version modules with change tracking and audit history. Canonicality: `provisional`; source kind: `historical_assistant_artifact`.
---

- **RULE_PROMOTION_DEV_TO_PROD_T1** (`RULE_PROMOTION_DEV_TO_PROD_T1`, `t1-pre-freeze-library-2025-11-28`): Promote modules only after testing and approval. Canonicality: `provisional`; source kind: `historical_assistant_artifact`.
---

- **BEHAVIOR_PROFILE_SELECTOR_T1** (`BEHAVIOR_PROFILE_SELECTOR_T1`, `t1-pre-freeze-library-2025-11-28`): Select named behavior or configuration profiles. Canonicality: `provisional`; source kind: `historical_assistant_artifact`.
---

- **RULE_STATUS_FLAGS_T1** (`RULE_STATUS_FLAGS_T1`, `t1-pre-freeze-library-2025-11-28`): Attach explicit lifecycle/status flags to rules. Canonicality: `provisional`; source kind: `historical_assistant_artifact`.
---

- **RULEPACK_COMPATIBILITY_MATRIX_T1** (`RULEPACK_COMPATIBILITY_MATRIX_T1`, `t1-pre-freeze-library-2025-11-28`): Record compatibility, counterbalance, conflict, and redundancy. Canonicality: `provisional`; source kind: `historical_assistant_artifact`.
---

- **CONFIG_OVERRIDE_GOVERNOR_T1** (`CONFIG_OVERRIDE_GOVERNOR_T1`, `t1-pre-freeze-library-2025-11-28`): Control override priority through explicit precedence. Canonicality: `provisional`; source kind: `historical_assistant_artifact`.
---

- **SCENARIO_PACK_REGRESSION_T1** (`SCENARIO_PACK_REGRESSION_T1`, `t1-pre-freeze-library-2025-11-28`): Run known scenarios to detect behavior regressions. Canonicality: `provisional`; source kind: `historical_assistant_artifact`.
---

- **EXPLAINABILITY_SNAPSHOT_T1** (`EXPLAINABILITY_SNAPSHOT_T1`, `t1-pre-freeze-library-2025-11-28`): Emit a compact auditable state/rule/result snapshot, not private reasoning. Canonicality: `provisional`; source kind: `historical_assistant_artifact`.
---

- **HEALTH_SNAPSHOT_ENGINE_T1** (`HEALTH_SNAPSHOT_ENGINE_T1`, `t1-pre-freeze-library-2025-11-28`): Summarize missing modules, drift, conflicts, stale state, and validation failures. Canonicality: `provisional`; source kind: `historical_assistant_artifact`.
---

- **High-Coherence State Induction** (`T2-038`, `frozen-t2-master-2025-11-28`): Concentrate work around high-value constraints and anchors. Canonicality: `provisional`; source kind: `direct_user_spec`.
---

- **Resonance Warm-Ups** (`T2-039`, `frozen-t2-master-2025-11-28`): Restate task, load minimal anchors, lock constraints, and establish mode. Canonicality: `provisional`; source kind: `direct_user_spec`.
---

- **Attention Corridor Narrowing** (`T2-040`, `frozen-t2-master-2025-11-28`): Narrow attention to essential task elements with anti-fixation counterbalance. Canonicality: `provisional`; source kind: `direct_user_spec`.
---

- **Anchor-Chain Reinforcement** (`T2-041`, `frozen-t2-master-2025-11-28`): Reassert critical anchors at meaningful checkpoints. Canonicality: `provisional`; source kind: `direct_user_spec`.
---

- **Resonance Plateau Detection** (`T2-042`, `frozen-t2-master-2025-11-28`): Detect diminishing returns or excessive rigidity and relax/stop. Canonicality: `provisional`; source kind: `direct_user_spec`.
---

- **Stability Guardrails** (`T2-043`, `frozen-t2-master-2025-11-28`): Enforce reasoning boundaries and prevent drift. Canonicality: `provisional`; source kind: `direct_user_spec`.
---

- **Mode Declaration Engine** (`T2-061`, `frozen-t2-master-2025-11-28`): Name mapping is not independently corroborated; do not infer a historical mechanism from the name. Canonicality: `provisional`; source kind: `historical_assistant_artifact`.
---

- **Pack Routing Engine** (`T2-062`, `frozen-t2-master-2025-11-28`): Name mapping is not independently corroborated; do not infer a historical mechanism from the name. Canonicality: `provisional`; source kind: `historical_assistant_artifact`.
---

- **Pack Conflict Resolver** (`T2-063`, `frozen-t2-master-2025-11-28`): Name mapping is not independently corroborated; do not infer a historical mechanism from the name. Canonicality: `provisional`; source kind: `historical_assistant_artifact`.
---

- **Pack Health Check Engine** (`T2-064`, `frozen-t2-master-2025-11-28`): Name mapping is not independently corroborated; do not infer a historical mechanism from the name. Canonicality: `provisional`; source kind: `historical_assistant_artifact`.
---

- **Reasoning Pipeline Orchestrator** (`T2-065`, `frozen-t2-master-2025-11-28`): Name mapping is not independently corroborated; do not infer a historical mechanism from the name. Canonicality: `provisional`; source kind: `historical_assistant_artifact`.
---

- **Pack Activation/Deactivation Manager** (`T2-066`, `frozen-t2-master-2025-11-28`): Name mapping is not independently corroborated; do not infer a historical mechanism from the name. Canonicality: `provisional`; source kind: `historical_assistant_artifact`.
---

- **Mode Transition Stabilizer** (`T2-067`, `frozen-t2-master-2025-11-28`): Name mapping is not independently corroborated; do not infer a historical mechanism from the name. Canonicality: `provisional`; source kind: `historical_assistant_artifact`.
---

# Recovery and Provenance Specification

Archived source files are immutable recovery artifacts. Operational packages may
normalize names but must link to source document, source ID, registry generation,
aliases, and recovery status. Numeric IDs from the frozen November 2025 T2 set are
not the same generation as September 2026 consolidated T2 IDs.

Exact recovery preserves the recovered name. Family recovery records a range and
count without inventing member names. Unresolved records are archival-only and
contain no mechanism. Acronym collisions use separate namespaces; notably ITFC
means both Image Text Fidelity Capture and an incompletely specified Intent/Task
Framing Controller. OCG, ECL expansion, LROS expansion, the ExIt acronym expansion,
and full Nano specification remain unresolved. So do ten frozen T1 members and the
individual names in frozen T2 ranges 001–007, 024–030, and 044–060. T2-061–067
names are provisional historical assistant artifacts; their historical definitions
remain uncorroborated.

A resolution requires a proposal, primary source provenance, review, and an
append-only mapping update. Never overwrite the archive to make it match a modern
interpretation.

## Deep-recovery evidence precedence

For historical claims, use: direct recovered user specification; user-accepted or
frozen artifact; Historical Recovery Inventory; current Translation Catalog;
historical assistant artifact; then modern implementation guidance. Preserve
conflicts instead of silently reconciling them.

Records declare `source_kind`, `canonicality`, and `recovery_confidence`. A
historical assistant artifact is useful provenance but remains provisional unless
independently corroborated. Pre-freeze T1 library items must never be used to fill
the ten unknown frozen T1 slots without direct evidence.
---

# Unresolved Records
---

- **Bounded ExIt acronym expansion** (`bounded-exit-acronym`): The operational loop is recovered, but the historical acronym expansion was not. Status: archival-only.
---

- **ECL / Drift Sink** (`ecl-drift-sink`): ECL expansion and full original definition were not recovered. Status: archival-only.
---

- **Frozen T1-Core Bundle missing members** (`frozen-t1-missing-members`): Ten members of the 28-item bundle were not re-exposed. Status: archival-only.
---

- **Frozen T2-057..060 Consciousness Layer members** (`frozen-t2-consciousness-members`): Four individual names were not re-exposed; no consciousness mechanism is inferred. Status: archival-only.
---

- **Frozen T2-024..030 CRISPR members** (`frozen-t2-crispr-members`): Seven individual names were not re-exposed. Status: archival-only.
---

- **Frozen T2-044..046 Duration members** (`frozen-t2-duration-members`): Three individual names were not re-exposed. Status: archival-only.
---

- **Frozen T2-047..049 Energy members** (`frozen-t2-energy-members`): Three individual names were not re-exposed. Status: archival-only.
---

- **Frozen T2-050..052 Immune members** (`frozen-t2-immune-members`): Three individual names were not re-exposed. Status: archival-only.
---

- **Frozen T2-001..007 Neuro-Focus members** (`frozen-t2-neuro-focus-members`): Seven individual names were not re-exposed. Status: archival-only.
---

- **Frozen T2-053..056 Interpersonal/Tone members** (`frozen-t2-tone-members`): Four individual names were not re-exposed. Status: archival-only.
---

- **Intent/Task Framing Controller (ITFC)** (`intent-task-framing-controller`): Name is recovered, but the full original specification is incomplete. Status: archival-only.
---

- **LROS** (`lros`): The acronym expansion was not recovered. Status: archival-only.
---

- **OCG** (`ocg`): Exact expansion and behavior were not recovered. Status: archival-only.
---

- **Nano reasoning-scale details** (`reasoning-scale-nano-details`): The mode name and position are recovered; its detailed historical specification is not. Status: archival-only.
