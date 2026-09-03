# Upgradeables Open-Source Repository — Codex / Fable Build Handoff

**Handoff version:** 1.0  
**Prepared:** 2026-09-03  
**Default repository name:** `upgradeables`  
**Execution environment:** Windows PowerShell, local Git repository, GitHub via GitHub CLI when available  
**Primary goal:** Convert the supplied OS / CAF / Upgradeables source material into a production-quality, model-agnostic, open-source repository that any frontier LLM or agent developer can use to understand, compose, extend, test, and translate Upgradeables into Skills or agent workflows.

---

# 0. EXECUTION DIRECTIVE

You are the implementation agent.

Do **not** treat this handoff as a brainstorming document. Execute it as a repository-build specification.

The user has three source documents that must be treated as the repository seed corpus:

1. `OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged(1).md`
2. `OS_Upgradeables_Historical_Recovery_Inventory(1).md`
3. `OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md`

The third document is a dedicated deep historical-context recovery pass. It contains operational details, prior user-authored OS specifications, historical assistant artifacts, additional pre-freeze T1 modules, deeper SMSE/QMS workflows, exact recovered Resonance-family names, and explicit provenance confidence rules that were not fully represented in the first two files.

They should be located in, or copied into, the working directory before repository generation.

If equivalent filenames without `(1)` exist, inspect both and use the user's supplied/current versions. Do not silently merge conflicting versions. Preserve source provenance.

The repository must be useful even to a frontier model that has never seen the original conversations.

The repository must make the following distinction explicit:

> **OS = compositional operating framework**  
> **Skill = task-oriented implementation package**  
> **Upgradeable = reusable behavioral, reasoning, state, retrieval, validation, editing, orchestration, or control primitive that may be composed into many Skills**  
> **Behavior Gene = reusable task/domain behavior and reasoning pattern**  
> **Core = high-density domain knowledge/reasoning/evidence reference**  
> **Validator = component that checks, scores, vetoes, or requests repair without inventing supporting facts**  
> **Orchestrator = component that selects, sequences, coordinates, and resolves authority among modules**

Do not collapse these concepts into a single prompt type.

---

# 1. NON-NEGOTIABLE SOURCE-INTEGRITY RULES

These rules have precedence over convenience.

## 1.1 Preserve the historical recovery ledger

The historical recovery inventory is an archival source-of-truth ledger.

Copy it into the repository substantially unchanged, preferably byte-for-byte, under:

`archive/source/OS_Upgradeables_Historical_Recovery_Inventory.md`

Do not normalize historical IDs.

Do not rename historical concepts in the archival copy.

Do not erase aliases.

Do not reuse old numeric IDs for newer registry generations.

Do not infer missing expansions.

## 1.2 Preserve unresolved concepts as unresolved

Known unresolved or incomplete concepts must **not** receive invented definitions.

Examples include, based on the supplied source corpus:

- `OCG`
- `LROS` expansion
- `ECL` expansion
- unrecovered members of historical frozen families
- incomplete historical specification of the Intent/Task Framing Controller sense of `ITFC`

Use explicit metadata such as:

```yaml
recovery_status: unresolved
operational_status: archival_only
```

A future contributor may resolve an item only through a documented proposal with source provenance.

## 1.3 Preserve acronym collisions

`ITFC` has at least two recovered historical meanings and must not be merged:

- Image Text Fidelity Capture
- Intent/Task Framing Controller

Use distinct canonical slugs and preserve `legacy_acronym: ITFC`.

## 1.4 Preserve registry-generation boundaries

Historical T1/T2 numbering and later consolidated T1/T2 numbering are not guaranteed to refer to the same registry generation.

Never map numeric IDs merely because they look similar.

Every legacy ID must retain provenance metadata such as:

```yaml
registry_generation: frozen-t2-2025-11-28
historical_id: T2-016
```

## 1.5 Metaphor must become mechanism

Physics-, biological-, neurological-, or surgical-inspired labels are architectural metaphors.

Examples:

- Teleport Bus -> explicit state routing
- Multiverse -> bounded parallel candidate generation
- Singularity Core -> compressed domain reasoning/reference core
- Fermionic Veto -> explicit block/veto condition
- Resonance -> explicit cross-module alignment/coupling
- CRISPR Editing -> localized, invariant-preserving modification
- Surgery Editing -> structural/global replacement

Do not claim hidden channels, literal physical mechanisms, consciousness, secret latent pointers, or access to private chain-of-thought.

## 1.6 Validators do not manufacture truth

QMS, citation checks, contradiction gates, drift gates, and other validators may:

- approve;
- reject;
- score;
- identify defects;
- request repair;
- trigger abstention;
- choose between supported candidates.

They must not add unsupported factual content to make an answer pass.

---

## 1.7 Deep-recovery provenance precedence

The Deep Context Recovery Addendum introduces evidence classes that MUST be preserved during normalization.

For historical claims, use this priority:

1. direct recovered user-authored specification;
2. explicitly user-accepted/frozen historical artifact;
3. Historical Recovery Inventory;
4. current Translation Catalog normalization;
5. historical assistant-generated artifact;
6. modern implementation recommendation.

Do not silently promote a historical assistant artifact to user-confirmed canonical status.

Use metadata sufficient to distinguish at least:

```yaml
source_kind:
  - direct_user_spec
  - user_accepted
  - historical_assistant_artifact
  - current_consolidated_catalog
  - historical_recovery_inventory

canonicality:
  - canonical
  - accepted
  - provisional
  - historical_only
  - unresolved

recovery_confidence:
  - high
  - medium
  - low
```

Important newly recovered material to ingest includes:

- pre-freeze T1 Memory/Anchoring modules;
- pre-freeze T1 Governance modules;
- additional T1 Monitoring/Observability modules;
- exact T2-038–T2-043 Resonance/Coherence names;
- provisional historical-artifact mappings for T2-061–T2-067;
- the eight-stage SMSE workflow;
- T2 state vs T3 structured reasoning-state separation;
- deeper QMS convergence/veto/collapse rules;
- direct-user LCA-OS identity/goals;
- detailed Paper-Author, Research & Decision, and CAF Intake compositions;
- historical OS-builder / Meta-OS concepts.

Do not use newly recovered pre-freeze T1 modules to fill the ten unknown frozen `T1-CORE-BUNDLE v1` slots unless frozen membership is directly established.

# 2. REPOSITORY IDENTITY

Use the working title:

# Upgradeables

Recommended short description:

> An open, model-agnostic registry of composable reasoning, state, validation, retrieval, editing, orchestration, and behavioral primitives for building AI Skills and agent workflows.

Avoid branding the repository as a prompt collection.

The project should communicate that Upgradeables are **composable primitives / cognitive middleware**, not merely prompts.

Possible README language:

> Skills define jobs.  
> Behavior Genes define how a system behaves for a class of tasks.  
> Cores define domain reasoning and evidence knowledge.  
> Upgradeables define reusable capabilities and controls.  
> Validators enforce integrity.  
> Orchestrators compose them.  
> OS bundles create complete operating environments.

---

# 3. LICENSE AND OPEN-SOURCE DEFAULT

Unless the working directory already contains a user-selected license, use:

`Apache-2.0`

Reason: permissive reuse with explicit patent provisions and broad compatibility for software, schemas, scripts, and documentation.

Do not invent a trademark policy.

Add a note to `GOVERNANCE.md` that project naming/trademark governance may be added separately if the ecosystem develops.

---

# 4. TARGET REPOSITORY STRUCTURE

Create at minimum:

```text
upgradeables/
│
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── GOVERNANCE.md
├── CODE_OF_CONDUCT.md
├── CHANGELOG.md
├── SECURITY.md
├── ROADMAP.md
├── CITATION.cff
├── .gitignore
│
├── spec/
│   ├── OS_PHILOSOPHY.md
│   ├── UPGRADEABLE_SPEC.md
│   ├── COMPOSITION_SPEC.md
│   ├── PRECEDENCE_SPEC.md
│   ├── VERSIONING_SPEC.md
│   ├── RECOVERY_AND_PROVENANCE_SPEC.md
│   └── SKILL_TRANSLATION_SPEC.md
│
├── registry/
│   ├── registry.yaml
│   ├── registry.json
│   ├── schema/
│   │   ├── upgradeable.schema.json
│   │   ├── bundle.schema.json
│   │   └── recipe.schema.json
│   ├── current/
│   ├── historical/
│   └── unresolved/
│
├── upgradeables/
│   ├── foundation/
│   ├── state/
│   ├── context-retrieval/
│   ├── reasoning/
│   ├── truth-grounding/
│   ├── validation/
│   ├── drift-control/
│   ├── editing-repair/
│   ├── output/
│   ├── orchestration/
│   ├── meta-control/
│   └── persistence/
│
├── genes/
│   ├── README.md
│   └── examples/
│
├── cores/
│   ├── README.md
│   └── examples/
│
├── bundles/
│   ├── foundation/
│   ├── reasoning/
│   ├── repair/
│   ├── truth-safety/
│   ├── qms/
│   ├── meta-control/
│   ├── authoring/
│   └── architect/
│
├── recipes/
│   ├── research-skill.md
│   ├── source-grounded-analysis.md
│   ├── high-stakes-reasoning.md
│   ├── medical-evidence.md
│   ├── legal-evidence.md
│   ├── coding-debugging.md
│   ├── long-context-corpus.md
│   ├── authoring.md
│   ├── creative-ideation.md
│   ├── education-explanation.md
│   ├── decision-support.md
│   ├── architecture-skill-building.md
│   └── multi-agent-orchestration.md
│
├── domain-os/
│   ├── architect-os.md
│   ├── appeal-caf-os.md
│   ├── research-decision-os.md
│   ├── paper-author-os.md
│   ├── local-chat-analysis-author-os.md
│   └── multi-os.md
│
├── templates/
│   ├── UPGRADEABLE_TEMPLATE.md
│   ├── UPGRADEABLE_PROPOSAL_TEMPLATE.md
│   ├── BEHAVIOR_GENE_TEMPLATE.md
│   ├── CORE_TEMPLATE.md
│   ├── BUNDLE_TEMPLATE.md
│   ├── SKILL_RECIPE_TEMPLATE.md
│   └── COMPOSITION_TEST_TEMPLATE.md
│
├── proposals/
│   ├── README.md
│   ├── experimental/
│   ├── candidate/
│   ├── accepted/
│   ├── rejected/
│   └── archived/
│
├── implementations/
│   ├── README.md
│   ├── generic/
│   ├── openai/
│   ├── anthropic/
│   ├── google/
│   └── local-models/
│
├── scripts/
│   ├── build_registry.py
│   ├── validate_registry.py
│   ├── validate_upgradeable.py
│   ├── build_all_in_one.py
│   └── check_links.py
│
├── tests/
│   ├── fixtures/
│   ├── test_registry.py
│   ├── test_schema.py
│   ├── test_unique_ids.py
│   ├── test_alias_collisions.py
│   └── test_build_all_in_one.py
│
├── dist/
│   └── ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md
│
├── archive/
│   ├── README.md
│   └── source/
│       ├── OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md
│       ├── OS_Upgradeables_Historical_Recovery_Inventory.md
│       └── OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md
│
├── .github/
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.yml
│   │   ├── new_upgradeable.yml
│   │   └── documentation.yml
│   ├── PULL_REQUEST_TEMPLATE.md
│   └── workflows/
│       └── validate.yml
│
└── pyproject.toml
```

The precise folder layout may be adjusted if a cleaner implementation is found, but preserve the architectural separation.

---

# 5. CORE DESIGN PRINCIPLE

Use this conceptual equation throughout the specification:

```text
Skill =
    Task Identity
  + Behavior
  + Knowledge / References
  + Selected Upgradeables
  + State Requirements
  + Validation
  + Output Contract
```

Not every Skill requires every term.

Do not convert every Upgradeable into a standalone Skill.

Each Upgradeable should declare one or more recommended implementation forms:

- standalone skill;
- parent-skill mode;
- validator / guard;
- state schema;
- state manager;
- reference module;
- deterministic script;
- orchestrator;
- plugin/bundle component;
- archival concept.

---

# 6. FUNCTIONAL TAXONOMY

Retain historical tiers, but add an orthogonal functional taxonomy.

Use at least:

1. `framing-intake`
2. `state`
3. `context-retrieval`
4. `planning-reasoning`
5. `truth-grounding`
6. `validation`
7. `drift-control`
8. `editing-repair`
9. `output`
10. `orchestration`
11. `meta-control`
12. `persistence`

An Upgradeable may belong to more than one functional class.

Historical T1/T2/T3/T4 tier labels are provenance/architecture labels and must not be overwritten by this taxonomy.

---

# 7. ACTIVATION CLASSIFICATION

Every operational Upgradeable should receive an activation classification.

Use:

- `U0-foundational` — baseline candidate for most serious workflows
- `U1-common-conditional` — commonly useful when task conditions match
- `U2-specialized` — relevant to specific workflow families
- `U3-high-risk-expensive` — stronger controls or higher-cost reasoning
- `U4-meta-architecture` — primarily orchestrators, skill builders, supervisors, or architecture design

This classification is new operational metadata and must be labeled as a modern implementation layer, not historical provenance.

---

# 8. MATURITY / LIFECYCLE MODEL

Use the following operational lifecycle:

- `historical`
- `unresolved`
- `experimental`
- `candidate`
- `stable`
- `core`
- `deprecated`

Historical recovery state is separate from modern lifecycle state.

Example:

```yaml
recovery_status: exact_recovery
lifecycle_status: stable
```

or:

```yaml
recovery_status: unresolved
lifecycle_status: historical
```

Do not mark all seed Upgradeables as `core`.

Use `stable` for well-defined recovered components unless the source specifically establishes stronger canonical status.

---

# 9. STANDARD UPGRADEABLE PACKAGE

Each normalized operational Upgradeable should live in its own directory.

Example:

```text
upgradeables/validation/citation-fidelity/
├── UPGRADEABLE.md
├── metadata.yaml
├── examples/
│   └── basic.md
└── tests/
    └── composition.md
```

Do not create fake examples for concepts whose definition is unresolved.

## 9.1 Required metadata

Use a schema broadly equivalent to:

```yaml
id: T3-13
slug: citation-fidelity
display_name: Citation Fidelity Gate
version: 1.0.0

registry_generation: consolidated-2026-09
historical_ids: []
historical_aliases: []

recovery_status: exact_recovery
lifecycle_status: stable

tiers:
  - T3

functional_classes:
  - validation
  - truth-grounding

activation_class: U1-common-conditional

implementation_forms:
  - validator
  - skill-component

purpose: >
  Ensure that a citation actually supports the claim attached to it.

problem_solved: >
  Prevent citation laundering, adjacent-source borrowing, unsupported
  attribution, and meaning drift.

recommended_skill_types:
  - research
  - academic-authoring
  - medical-evidence
  - legal-evidence
  - policy-analysis
  - source-grounded-analysis

usually_not_needed_for:
  - pure-creative-writing-without-sources

triggers:
  - output contains citations
  - source-supported factual claims determine conclusions

non_triggers:
  - no external or supplied source claims are being cited

requires: []
recommended_with:
  - grounding-no-invention
  - critical-atomic-verification
  - multi-truth-gating
  - zero-drift-zones

counterbalances: []
potentially_redundant_with: []

inputs:
  - claim
  - citation
  - supporting source passage

outputs:
  - pass
  - fail
  - repair-required
  - unverifiable

strong_model_scaling:
  skippable_steps: []
  mandatory_invariants:
    - citation must actually support attached claim

failure_boundary:
  - if support cannot be verified, do not certify the citation

provenance:
  source_document: OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged
  notes: ""
```

Adapt field names if needed, but keep the conceptual coverage.

---

# 10. STANDARD `UPGRADEABLE.md`

Each operational Upgradeable should contain:

1. Name
2. Summary
3. Purpose
4. Problem Solved
5. Scope
6. Trigger Conditions
7. Non-Triggers
8. Inputs / Required State
9. Outputs / Produced State
10. Mechanism
11. Procedure
12. Always-Do Rules
13. Never-Do / Avoid Rules
14. Interaction Rules
15. Compatible Upgradeables
16. Counterbalancing Upgradeables
17. Potential Redundancy
18. Conflict / Precedence Rules
19. Failure Boundary
20. Strong-Model Scaling
21. Recommended Skill Types
22. Example Composition
23. Tests
24. Provenance / Historical Aliases

Do not pad weakly recovered concepts to fill every field.

Use explicit `Unknown / not recovered` fields where necessary.

---

# 11. BEHAVIOR GENES AND CORES

Do not flatten Genes and Cores into Upgradeables.

## Behavior Gene

A Behavior Gene defines how a workflow reasons/writes for a recurring task family.

At minimum describe:

- name;
- purpose;
- scope;
- triggers;
- always-do rules;
- never-do rules;
- reasoning pattern;
- evidence handling;
- Core interfaces;
- output contract;
- compatibility;
- version metadata.

Create seed examples for the recovered Gene families, including:

- IPMN Gene
- IPTA Gene
- OPMN Gene
- OPTA Gene
- Readmission Gene
- GMN Gene
- Tone Genes
- Risk-Emphasis Genes
- Deep Summary Gene
- Compare-Contrast Gene
- Alignment Gene
- Conflict-Handling Gene
- Synthesis Gene
- Memory Gene

## Core

A Core is a high-density domain/reasoning/evidence reference.

Describe:

- scope;
- entities / variables;
- reasoning map;
- required data;
- evidence hierarchy;
- decision logic;
- failure modes;
- examples;
- Gene interfaces;
- validator interfaces;
- source provenance.

Create seed Core descriptions only to the detail actually supported by the source documents.

Recovered Core families include:

- IPMN Core
- IPTA Core
- OPMN Core
- OPTA Core
- Readmission Core
- GMN Core
- Policy Core
- Chart-Review Core
- Analysis Core
- Synthesis Core
- Meta-Integrity Core

Do not invent detailed domain content that is absent from the source corpus.

---

# 12. COMPOSITION SPECIFICATION

Create `spec/COMPOSITION_SPEC.md`.

It must explain that the primary value of Upgradeables is composition.

Formalize common composition patterns.

## 12.1 Foundation stack

Example:

```text
Task-Set Lock-In
        ↓
Mode Lock-In
        ↓
StateBlock
        ↓
Scoped Loader
        ↓
Working-Memory Cues
        ↓
Drift Suppression
```

## 12.2 Grounded evidence stack

Example:

```text
Grounding / No-Invention
        ↓
Activation-Budget Funnel
        ↓
Evidence Capture / Indexing
        ↓
Critical Atomic Verification
        ↓
Multi-Truth Gating
        ↓
Citation Fidelity
        ↓
Truth Priority Hierarchy
        ↓
QMS
```

## 12.3 Creative exploration stack

Example:

```text
Controlled Drift Corridor
      +
Cognitive Flexibility
      +
Perspective Break
      +
Balanced Exploration
      ↓
Multiverse Engine
      ↓
QMS Collapse
```

Balance with:

- Creativity Regulator OS / equivalent bounded creativity control;
- Grounding;
- Counterfactual Integrity;
- Domain / Mode Isolation.

## 12.4 Repair escalation stack

Use smallest intervention first:

```text
Detect defect
    ↓
Micro-Repair
    ↓
CRISPR Edit
    ↓
Structured Refinement
    ↓
Regenerative Rewrite
    ↓
Surgery Edit
```

## 12.5 Long-context stack

Compose concepts such as:

- StateBlock
- SMSE
- Working-Memory Lock-In
- Stable Long Context
- Activation-Budget Funnel
- Attention Compression
- Neuro-Focus
- Drift Suppression
- Coherence Heartbeat
- Resonance / Cross-Context Resonance
- State Snapshot

## 12.6 Architecture / design stack

Compose:

- Architect Orchestrator
- POWER or HYBRID mode
- Cosmic reasoning
- Multiverse
- Behavior Gene Builder
- Domain Core Builder
- Loader
- StateBlock
- QMS
- Meta-Supervisor
- Adapter-First Experimentation
- CRISPR
- Surgery
- Dynamic Depth Allocation
- Anti-Tunnel Vision
- State Snapshot

---

# 13. COMPATIBILITY / COUNTERBALANCE RULES

Create `spec/PRECEDENCE_SPEC.md` and include a compatibility section.

At minimum formalize these pairings:

### Neuro-Focus + Anti-Tunnel Vision

Focus strongly on the highest-value region while periodically checking whether focus has become fixation.

### Multiverse + QMS

Generate bounded alternative candidates, then compare and collapse.

### CRISPR + Invariance Stress

Make localized modifications and test whether protected behavior outside the patch remained unchanged.

### Controlled Drift + Grounding

Allow bounded transformation or creativity while protecting factual invariants.

### Risk-Tier Scaling + Dynamic Depth Allocation

Use risk to influence how much reasoning and validation effort is allocated.

### StateBlock + SMSE

StateBlock is the explicit state representation; SMSE is a sequential update/preservation mechanism.

### Micro-Repair + Regenerative Rewrite

Prefer localized correction; escalate to global reconstruction only when local repair cannot restore coherence.

### Citation Fidelity + Style Alignment

Stylistic polish may not change the meaning or support relationship of cited claims.

### Cosmic Planning + SAFE Execution

Broad design exploration should collapse into narrow, grounded execution when committing factual or consequential output.

### Resonance + Domain/Mode Isolation

Modules may reinforce one another only inside explicit authority and domain boundaries.

---

# 14. AUTHORITY AND PRECEDENCE

Use the recovered architecture as the basis for an explicit precedence model.

Recommended default:

```text
Host / system safety
  ↓
Organization / domain policy
  ↓
Active OS / project kernel
  ↓
Task lock
  ↓
Behavior Gene / Core
  ↓
Upgradeables
  ↓
Style preferences
```

A lower layer must not silently defeat a higher layer.

Validators with explicit veto authority may block output when their conditions are met, but may not rewrite higher-authority rules.

---

# 15. SKILL-TYPE RECIPE MATRIX

Create `recipes/` documents and a machine-readable mapping in the registry.

Every recipe should classify Upgradeables as:

- `R` = required for that recipe
- `A` = automatically recommended
- `C` = conditional
- `O` = optional enhancement
- `X` = normally exclude

These are recipe recommendations, not universal truths.

## 15.1 Research Skill

Seed with:

Foundation:
- Task-Set Lock-In
- Scoped Loader
- StateBlock
- Grounding / No-Invention

Highly recommended:
- Activation-Budget Funnel
- Neuro-Focus
- Stable Long Context
- SMSE
- Multi-Truth Gating
- Citation Fidelity
- Truth Priority Hierarchy
- Critical Atomic Verification

Validation:
- Mirror QMS
- Inversion QMS
- Transversal QMS
- Conflict-Resolution QMS when evidence conflicts

Long-running:
- Coherence Heartbeat
- State Snapshot
- Working-Memory Lock-In

Optional:
- Multiverse for competing hypotheses
- Anti-Tunnel Vision
- Invariance Stress

## 15.2 Source-Grounded / Academic Authoring

Seed with:

- Task Lock
- Mode Lock
- Grounding
- Style Alignment
- Pedagogical Alignment
- Explanation Minimality
- Controlled Drift Corridors
- Safe Rewrite
- Citation Fidelity
- Zero-Drift Zones
- semantic phase separation
- Counterfactual Integrity
- Micro-Repair
- Placeholder Suppression
- QMS

## 15.3 High-Stakes Reasoning

Examples: medical, legal, financial, policy, safety-critical evidence work.

Seed with:

- Grounding / No-Invention
- Epistemic Status Gating
- Risk-Tier Scaling
- Critical Atomic Verification
- Multi-Truth Gating
- Truth Redundancy
- Truth Priority Hierarchy
- Domain / Mode Isolation
- Citation Fidelity when sources are used
- Fail-Closed Abstention
- explicit veto logic
- QMS
- Drift Suppression
- Dynamic Depth Allocation

## 15.4 Coding / Debugging

This is a modern application recipe inferred from the mechanisms, not a claim that the original historical architecture explicitly defined a coding Skill.

Seed with:

- Task-Set Lock-In
- StateBlock
- Forethought / Checkpoints
- Dominant-Driver Isolation
- Anti-Tunnel Vision
- Bidirectional Consistency
- Invariance Stress Scaffold
- Micro-Repair
- CRISPR Editing
- Surgery Editing
- Structured Refinement
- Bounded ExIt
- QMS
- Drift Suppression

Interpretation:
- CRISPR = localized patch
- Surgery = architectural refactor
- Invariance Stress = regression/invariant verification
- Micro-Repair = smallest sufficient fix
- Regenerative Rewrite = rebuild broken subsystem

Label this mapping as `modern application guidance`.

## 15.5 Long-Context / Corpus Analysis

Seed with:

- StateBlock
- SMSE
- Working-Memory Lock-In
- Stable Long Context
- Activation-Budget Funnel
- Attention Compression
- Neuro-Focus
- Drift Suppression
- Coherence Heartbeat
- Cross-Context Resonance
- State Snapshot
- Citation Fidelity when source claims are emitted

## 15.6 Creative / Ideation

Seed with recovered creative-family concepts where operational definitions are sufficient:

- Novelty & Creativity Expansion
- Micro-Creative Mode
- Cognitive Flexibility
- Perspective Break
- Strange Loop Generator
- Balanced Exploration
- Dream-Mode Creative
- Hypnagogic Divergence
- Multiverse Engine

Balance with:

- Controlled Drift Corridors
- CROS / creativity regulator concept
- Counterfactual Integrity
- Domain / Mode Isolation
- QMS collapse

Clearly distinguish historical names with sparse recovered definitions from fully operationalized concepts.

## 15.7 Architecture / Skill Building

Seed with:

- Architect Orchestrator
- POWER / HYBRID
- reasoning-scale controller / Cosmic
- Multiverse
- Behavior Gene Builder
- Domain Core Builder
- Scoped Loader
- StateBlock
- Parallel QMS
- Meta-Supervisor
- Adapter-First Experimentation
- CRISPR
- Surgery
- Dynamic Depth Allocation
- Anti-Tunnel Vision
- State Snapshot
- Future-Proof Mode Selector

## 15.8 Education / Explanation

Seed with:

- Pedagogical Alignment
- Explanation Minimality
- Style Alignment
- Grounding
- Micro-Scaffolding
- Task-Set Lock-In
- Safe Rewrite
- Anti-Tunnel Vision where conceptual alternatives matter
- QMS for correctness-sensitive teaching

## 15.9 Multi-Agent / Orchestration

Seed with:

- Architect Orchestrator
- Scoped Loader
- State Routing Bus
- StateBlock
- State Snapshot
- Supervisor / Worker pattern where supported
- Domain / Mode Isolation
- Resonance
- QMS
- conflict handling
- execution logging
- explicit external state automation where real persistence exists

Never claim actual multi-agent parallelism unless the host environment provides it.

---

# 16. PARALLEL-QMS PACKAGING

Do not create fifteen unrelated full Skills unless implementation evidence justifies it.

Preferred structure:

```text
bundles/qms/
├── README.md
├── QMS_VARIANTS.md
└── metadata.yaml
```

Treat `parallel-qms` as a parent validator family with named modes including recovered variants:

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

If true distributed/parallel execution is unavailable, define the mode as independent passes without claiming distributed execution.

Do not overstate Monte QMS as mathematically formal Monte Carlo unless stochastic sampling is actually implemented.

---

# 17. REASONING-SCALE CONTROLLER

Represent:

`Subatomic -> Atomic -> Nano -> Micro -> QMS -> Cosmic`

Prefer one parent conceptual controller or reference with modes rather than six independent top-level Skills.

Preserve the source caveat that Nano's historical detailed specification was not fully recovered.

Do not expose or request private chain-of-thought.

Interpret scale as **task decomposition / verification granularity / planning depth**, not hidden reasoning transcript access.

---

# 18. SEED BUNDLES

Build at least the following curated bundles from the source material.

## Foundation

- scoped-loader
- stateblock
- task-set-lock-in
- working-memory-cues
- grounding-no-invention
- drift-suppression
- placeholder-suppression
- mode-lock-in

## Reasoning

- micro-scaffolding
- reasoning-scale-controller
- anti-tunnel-vision
- forethought-checkpoints
- bidirectional-consistency
- multiverse-reasoning
- bounded-exit

## Repair

- safe-rewrite
- micro-repair
- regenerative-rewrite
- crispr-edit
- surgery-edit
- contradiction-micro-repair

## Truth / Safety

- multi-truth-gating
- truth-redundancy
- critical-atomic-verification
- controlled-drift-corridors
- truth-priority-hierarchy
- domain-mode-isolation
- fail-closed-abstention
- citation-fidelity
- counterfactual-integrity
- explicit veto / fermionic-veto
- risk-tier-scaling

## Meta-Control

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

## Authoring

- style-alignment
- pedagogical-alignment
- safe-rewrite
- citation-fidelity
- placeholder-suppression

## Architect

- architect-orchestrator
- behavior-gene-builder
- domain-core-builder
- adapter-first-experimentation
- crispr-edit
- surgery-edit
- scoped-loader
- state-snapshot
- ultimate-suite-supervisor

---

# 19. DOMAIN OS SEED DOCUMENTS

Create model-agnostic descriptions for the recovered domain OS families:

- Architect OS
- Appeal / CAF OS
- Research & Decision OS
- Paper-Author OS
- Local Chat-Analysis Author OS
- Multi-OS

These are examples of how primitives compose into domain operating systems.

Do not turn private or organization-specific appeal content into public factual policy unless that content is actually present in the supplied source and appropriate to publish.

The repo's architectural value should not depend on one domain.

---

# 20. CONTRIBUTION MODEL

Anyone may:

- fork;
- experiment;
- propose new Upgradeables;
- propose modes;
- improve implementations;
- add tests;
- add Skill recipes;
- add bundles;
- add model-specific implementations.

Canonical registry changes require review.

## 20.1 Proposal lifecycle

Use:

```text
Idea
  ↓
Proposal
  ↓
Experimental
  ↓
Candidate
  ↓
Stable
  ↓
Core (rare, broad, foundational)
```

Possible terminal states:

- rejected
- deprecated
- archived
- historical

## 20.2 Prior-art requirement

Every new Upgradeable proposal must identify:

```text
Closest existing Upgradeables:
- ...

Difference:
...

Why composition of existing Upgradeables is insufficient:
...

Why this should be a new primitive rather than:
- a mode;
- recipe;
- bundle;
- validator configuration;
- reference module;
- implementation detail.
```

This is mandatory.

Avoid duplicate-by-renaming.

## 20.3 Upgradeable proposal template

Require:

- proposed name;
- purpose;
- problem solved;
- prior art;
- trigger;
- non-trigger;
- inputs;
- outputs;
- mechanism;
- procedure;
- always-do;
- never-do;
- failure boundary;
- compatible Upgradeables;
- counterbalances;
- conflicts;
- recommended Skill types;
- example;
- tests;
- limitations;
- implementation form;
- provenance / external references if any.

---

# 21. GOVERNANCE

Create a lightweight maintainer-led governance model suitable for a new open-source project.

Initial principles:

1. Anyone may propose.
2. Canonical registry changes require review.
3. Historical provenance cannot be silently rewritten.
4. Unresolved historical concepts may only be resolved with evidence.
5. New primitives require prior-art comparison.
6. Tests and explicit mechanism are preferred over attractive naming.
7. Model-specific implementations must remain separate from model-agnostic specification.
8. Safety/host restrictions always override repo-level behaviors.
9. Deprecation should preserve discoverable historical lineage.
10. Stable IDs should not be reassigned.

Do not fabricate named maintainers beyond the repository owner.

---

# 22. VERSIONING

Use semantic versioning for the overall repository/specification where practical.

Each Upgradeable package should have a version independent of the repository version.

Identity rules:

- cosmetic documentation corrections -> patch;
- compatible procedure/metadata improvement -> minor;
- behavior-breaking or contract-breaking change -> major;
- changing canonical identity -> normally create migration/alias rather than silently replacing identity.

Historical IDs are immutable provenance keys.

Modern slugs may have aliases but should not be recycled for unrelated concepts.

---

# 23. MACHINE-READABLE REGISTRY

Create both:

- `registry/registry.yaml`
- `registry/registry.json`

Generate JSON from YAML rather than maintaining two divergent hand-edited sources if practical.

The registry should include:

- canonical slug;
- display name;
- IDs;
- historical aliases;
- recovery status;
- lifecycle status;
- functional class;
- activation class;
- tier;
- implementation forms;
- recommended Skill types;
- dependencies;
- recommended companions;
- counterbalances;
- conflicts;
- source package path;
- provenance.

Do not make the top-level registry the only source of truth. Individual `metadata.yaml` files should remain independently inspectable.

---

# 24. JSON SCHEMA

Create JSON Schema validation for at least:

- Upgradeable metadata;
- bundle metadata;
- recipe metadata.

Required validations should include:

- non-empty unique slug;
- allowed lifecycle values;
- allowed recovery values;
- allowed activation classes;
- allowed functional classes;
- valid relative package path;
- unresolved items cannot claim unsupported procedures;
- aliases must not collide ambiguously without collision metadata.

---

# 25. AUTOMATED VALIDATION

Use Python for portable validation unless the repository environment already has a better justified standard.

Create scripts/tests that detect:

1. duplicate canonical IDs;
2. duplicate slugs;
3. ambiguous alias collisions;
4. broken dependency references;
5. nonexistent package paths;
6. invalid lifecycle values;
7. invalid recovery status;
8. unresolved entries containing invented operational procedures;
9. registry YAML/JSON divergence;
10. broken internal Markdown links where practical;
11. missing required metadata;
12. bundle references to unknown Upgradeables;
13. recipe references to unknown Upgradeables.

Use deterministic validation whenever possible.

---

# 26. CI

Create a simple GitHub Actions workflow that runs on pull request and push.

At minimum:

- install Python;
- install project/test dependencies;
- validate schemas;
- rebuild registry JSON;
- run tests;
- fail on unexpected registry diff;
- build the all-in-one artifact.

Avoid unnecessary heavyweight infrastructure.

---

# 27. ALL-IN-ONE GENERATED ARTIFACT

Create:

`dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md`

This must be generated by script from canonical repository content.

Purpose:

- portable ingestion by frontier models;
- single-file reference when a repository cannot be mounted;
- human-readable architecture overview.

Do not make the all-in-one file the editable source of truth.

Include:

1. project philosophy;
2. terminology;
3. Upgradeable specification;
4. functional taxonomy;
5. composition guidance;
6. recipe matrix;
7. current registry summaries;
8. historical/provenance rules;
9. Skill-builder procedure.

Keep unresolved entries explicitly unresolved.

---

# 28. SKILL BUILDER PROCEDURE

Create a model-agnostic `spec/SKILL_TRANSLATION_SPEC.md`.

A frontier model should follow approximately:

```text
1. Identify Skill archetype.
2. Define task identity and activation boundary.
3. Determine risk tier.
4. Determine evidence sensitivity.
5. Determine state/context requirements.
6. Select Behavior Gene if applicable.
7. Select Core/reference material if applicable.
8. Load foundational Upgradeables.
9. Add task-specific Upgradeables.
10. Add risk-dependent validators.
11. Check compatibility, counterbalances, and redundancy.
12. Remove unnecessary scaffolding.
13. Determine implementation form for each component.
14. Generate target Skill instructions.
15. Move deep material into references/resources.
16. Add deterministic scripts when they materially help.
17. Add positive, negative, conflict, long-context, and composition tests.
18. Run QMS / validation against the finished Skill.
```

Include the architectural principle:

> Stronger models should receive less unnecessary scaffolding, while truth, state, safety, and integrity controls remain when the task still requires them.

---

# 29. MODEL-SPECIFIC IMPLEMENTATIONS

Keep the specification model-agnostic.

Use `implementations/` for model-specific mappings.

## 29.1 Generic

Describe how to translate Upgradeables into:

- system instructions;
- task prompts;
- state schemas;
- validators;
- scripts;
- references;
- agent graphs.

## 29.2 OpenAI

Create a concise implementation note showing how an Upgradeable may map into a modern Skill package such as:

```text
skill-folder/
├── SKILL.md
├── references/
├── scripts/
└── assets/
```

Do not assume every Upgradeable becomes a separate Skill folder.

Do not hard-code fast-changing platform claims into the model-agnostic specification.

## 29.3 Other model providers

Create placeholders/framework notes only where needed.

Do not invent provider-specific capabilities.

Label implementation guides as adapter layers that may evolve independently.

---

# 30. README REQUIREMENTS

The README should answer, quickly:

1. What is an Upgradeable?
2. What problem does this repo solve?
3. How is it different from a prompt library?
4. How is an Upgradeable different from a Skill?
5. What are Behavior Genes?
6. What are Cores?
7. How do I browse the registry?
8. How do I build a Skill from Upgradeables?
9. How do I propose a new Upgradeable?
10. How are historical concepts preserved?
11. How can a model/tool consume the machine-readable registry?
12. How can contributors run validation locally?

Include a concise architecture diagram.

Example:

```text
Host Model
    ↓
OS / Skill Bundle
    ↓
Task Shell
 ┌───────────────┬─────────────┬──────────────┐
 ↓               ↓             ↓              ↓
Behavior Gene   Core      Upgradeables      State
 └───────────────┴──────┬──────┴──────────────┘
                        ↓
                   Validators
                        ↓
                     Output
```

---

# 31. HISTORICAL ARCHIVE

Copy the user's two seed source documents to `archive/source/`.

Create `archive/README.md` explaining:

- these documents are recovery/source artifacts;
- operational registry entries may normalize names into slugs;
- archival historical names remain preserved;
- unresolved concepts are intentionally not guessed;
- historical numeric IDs may belong to different generations;
- the operational registry should link back to provenance.

The historical archive should remain readable even if the modern registry evolves.

---

# 32. SEED REGISTRY POPULATION

Important: **Do not stop after creating directories and templates.**

Populate the initial repository using the supplied catalog.

At minimum operationalize the well-defined consolidated entries in the source catalog, including:

- Tier 1 core reliability Upgradeables;
- consolidated Tier 2 reasoning/state/repair Upgradeables;
- reasoning-scale stack;
- Tier 3 truth/alignment/safety Upgradeables;
- Parallel-QMS family;
- advanced architecture Upgradeables;
- Behavior Gene framework and recovered Genes;
- Core framework and recovered Cores;
- orchestrator/loader/state architecture;
- Tier 4/meta-supervisor family;
- domain OS examples.

Historical sparse-recovery items should be indexed, but do not invent full mechanisms.

For large conversion work:

1. parse the source headings;
2. create a conversion ledger;
3. track source entry -> destination package;
4. identify aliases versus distinct mechanisms;
5. flag ambiguous mappings rather than guessing;
6. validate that no recovered canonical current entry disappears.

Create a temporary build report if useful, then either retain it under `archive/` or summarize it in the initial release notes.

---

# 33. INITIAL REGISTRY PRIORITY

If the full historical corpus is too large to operationalize in a single pass, prioritize in this order **without omitting the archival records**:

## Priority A — foundational operational primitives

- scoped-loader
- stateblock
- task-set-lock-in
- grounding-no-invention
- drift-suppression
- micro-scaffolding
- safe-rewrite
- micro-repair
- bounded-exit
- citation-fidelity
- multi-truth-gating
- risk-tier-scaling
- parallel-qms
- cognitive-governor
- architect-orchestrator

## Priority B — advanced controls

- anti-tunnel-vision
- bidirectional-consistency
- domain-mode-isolation
- controlled-drift-corridors
- critical-atomic-verification
- fail-closed-abstention
- reflectos
- coherence-heartbeat
- resonance
- neuro-focus
- crispr-edit
- surgery-edit
- multiverse-reasoning

## Priority C — meta-supervisor

- meta-supervisor
- ultimate-suite-supervisor
- dynamic-depth-allocation
- reasoning-throughput-governor
- drift-spectra-scaling
- domain-normalized-drift
- meta-stability
- cross-universe-consistency
- future-proof-mode-selector

## Priority D — meta-builders / OS bundles

- behavior-gene-builder
- domain-core-builder
- architect-os
- caf-appeal-router / CAF OS architecture
- research-decision-os
- paper-author-os

But aim to populate all fully recovered entries where feasible.

---

# 34. CONTRIBUTION TEST PHILOSOPHY

Do not test only whether a component description is syntactically valid.

Support behavioral/composition test cases.

Examples:

### Positive trigger
Does the Upgradeable activate where intended?

### Negative trigger
Does it stay inactive when unnecessary?

### Conflict
Does precedence resolve conflicting modules correctly?

### Long context
Does state remain coherent?

### Unsupported claim
Does grounding/citation validation fail safely?

### Composition
Do complementary Upgradeables work together?

### Over-scaffolding
Can optional machinery be omitted for simple tasks?

### Strong-model scaling
Does the spec distinguish skippable scaffolding from mandatory invariants?

---

# 35. PROPOSAL / ISSUE TEMPLATES

Create GitHub issue forms for:

## New Upgradeable

Fields should require:

- proposed name;
- problem;
- existing prior art;
- why composition is insufficient;
- trigger;
- mechanism;
- failure boundary;
- tests;
- recommended implementation form.

## Bug / specification inconsistency

Capture:

- affected component;
- expected behavior;
- observed problem;
- version;
- proposed correction.

## Documentation / recipe contribution

Capture:

- affected recipe/spec;
- rationale;
- which Upgradeables are involved;
- whether this changes behavior or documentation only.

---

# 36. PULL REQUEST TEMPLATE

Require contributors to check:

- [ ] I searched for duplicate concepts.
- [ ] I compared against the closest existing Upgradeables.
- [ ] I preserved provenance.
- [ ] I did not invent unresolved historical definitions.
- [ ] I added/updated tests.
- [ ] I updated machine-readable metadata.
- [ ] I documented conflicts/counterbalances.
- [ ] I classified whether this is a primitive, mode, recipe, bundle, reference, or implementation.
- [ ] I ran repository validation.

---

# 37. SECURITY / SAFETY SCOPE

`SECURITY.md` should focus on repository vulnerabilities and harmful implementation errors.

Do not position the Upgradeables framework as bypassing host-model safety.

Explicitly state:

> Upgradeables operate beneath host/system policy authority. They are not a mechanism to override model-provider or application safety controls.

---

# 38. DOCUMENTATION STYLE

Use clear technical prose.

Avoid unnecessary mythology in explanations even when preserving historical metaphor names.

Preferred pattern:

```text
Historical name:
Fermionic Veto Strengthening

Operational interpretation:
An explicit veto gate that blocks commitment when a critical contradiction,
safety condition, or integrity failure is detected.
```

Preserve creative names as provenance/identity while making mechanisms auditable.

---

# 39. REPOSITORY BUILD QUALITY BAR

Before initial publication, verify:

- README is useful without opening source archive;
- all major architecture terms are defined;
- source documents are preserved;
- no unresolved acronym has been fabricated;
- machine-readable registry validates;
- registry JSON is reproducibly generated;
- at least foundational Upgradeables have full packages;
- Skill-type recipes exist;
- composition rules exist;
- contribution/governance rules exist;
- tests pass;
- CI passes locally where possible;
- `dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md` builds;
- internal links resolve;
- no generated temporary files are accidentally committed;
- repository contains no secrets or credentials;
- Git status is clean after commit.

---

# 40. GIT / GITHUB EXECUTION

Use Git locally.

Detect prerequisites:

```powershell
git --version
gh --version
gh auth status
python --version
```

If `git` is missing, stop repository publication and clearly report the missing prerequisite.

If `gh` is missing or unauthenticated, still complete the entire local repository, commits, validation, and release-ready state. Do not discard work.

## 40.1 Initialize

From the parent working directory:

```powershell
New-Item -ItemType Directory -Path upgradeables -Force | Out-Null
Set-Location upgradeables
git init
```

If the repo already exists, inspect it before modifying anything and preserve unrelated work.

## 40.2 Default branch

Prefer:

```powershell
git branch -M main
```

## 40.3 Initial commit

After validation:

```powershell
git add .
git status
git commit -m "Initial open-source Upgradeables registry"
```

## 40.4 Publish with GitHub CLI

If GitHub CLI is installed and authenticated, create the public repository from the current folder.

Preferred intent:

```text
repository: upgradeables
visibility: public
source: current directory
remote: origin
push: yes
```

Use the currently installed `gh repo create` syntax rather than assuming an outdated flag set.

Do not overwrite an existing remote repository without confirming its identity.

If `upgradeables` is unavailable under the user's GitHub account, do not silently choose a substantially different project identity. Use a minimally modified safe alternative or leave local repo ready and report the naming conflict.

---

# 41. GITHUB DESCRIPTION / TOPICS

Suggested repository description:

> Model-agnostic composable primitives for building AI Skills, reasoning workflows, validators, state systems, and agent architectures.

Suggested topics if appropriate:

- ai
- llm
- agents
- agent-skills
- reasoning
- prompt-engineering
- ai-safety
- ai-tools
- orchestration
- open-source
- llm-agents

Do not add misleading claims such as AGI, consciousness, or guaranteed reasoning improvement.

---

# 42. OPTIONAL INITIAL RELEASE

If the repository is successfully published and GitHub CLI supports it cleanly, optionally prepare a `v0.1.0` release only after the initial repository content is complete and validation passes.

Release title suggestion:

`Upgradeables v0.1.0 — Initial Open Registry`

Do not create a release merely for an empty scaffold.

---

# 43. SOURCE-TO-REGISTRY TRACEABILITY

Create a traceability artifact such as:

`archive/SOURCE_TO_REGISTRY_MAP.md`

For each major recovered item, record:

```text
Source Name
Source ID
Registry Generation
Recovery Status
Modern Slug
Destination
Disposition:
- operationalized
- alias
- historical-only
- unresolved
- merged-as-mode
- bundled
```

This is critical for preventing historical material from disappearing during normalization.

---

# 44. DUPLICATION / MERGE RULES

When two source concepts overlap:

## Exact same concept/name
Do not duplicate.

## Historical alias / evolved label
Preserve alias and provenance.

## Same acronym, different meaning
Split namespaces.

## Same family, different registry generation
Preserve both historical identities.

## Variant of same mechanism
Prefer parent + mode.

## Composition of existing primitives
Prefer a recipe or bundle.

## Materially distinct mechanism
Create a new Upgradeable candidate.

When uncertain, preserve source identity and mark the mapping as unresolved rather than forcing a merge.

---

# 45. STRONGER-MODEL SCALING

Every mature Upgradeable should ideally declare:

```yaml
strong_model_scaling:
  may_skip:
    - ...
  keep_mandatory:
    - ...
```

Purpose:

Avoid turning scaffolding into a permanent performance tax.

Examples:

- detailed micro-scaffolding may be unnecessary for trivial tasks;
- truth/source fidelity remains important when factual stakes are high;
- state controls remain important when context is long or externally persisted;
- citation verification remains mandatory when citation correctness matters.

---

# 46. WHAT NOT TO DO

Do not:

- turn the source into one giant `SKILL.md`;
- create hundreds of thin duplicate Skills;
- erase Behavior Gene / Core distinctions;
- invent missing historical definitions;
- fabricate original dates or provenance;
- silently merge registry generations;
- claim access to hidden chain-of-thought;
- claim actual parallel agents if only sequential passes exist;
- claim persistence when no storage mechanism exists;
- let validators generate unsupported facts;
- use metaphors as implementation explanations;
- make all Upgradeables always-on;
- treat the project as a benchmark claiming proven model improvement unless evidence is later added;
- commit credentials, GitHub tokens, API keys, or local user paths;
- publish organization/private domain data accidentally;
- rewrite the archival source files merely for formatting consistency.

---

# 47. COMPLETION REPORT

At the end of execution, report to the user:

1. local repository path;
2. GitHub repository URL if published;
3. number of operational Upgradeable packages created;
4. number of historical-only entries indexed;
5. number of unresolved entries preserved;
6. registry validation result;
7. test result;
8. CI configuration created;
9. generated all-in-one artifact path;
10. any source ambiguities intentionally left unresolved;
11. recommended next 3 repository-development priorities.

Do not claim completion if only the folder skeleton was created.

---

# 48. ACCEPTANCE CRITERIA

The build is successful when a fresh frontier LLM or human developer can clone the repository and answer all of these without reading the original private conversations:

- What is an Upgradeable?
- How is it different from a Skill?
- How is it different from a Behavior Gene or Core?
- Which Upgradeables are useful for a research Skill?
- Which are useful for coding/debugging?
- Which are useful for high-stakes evidence work?
- Which components counterbalance one another?
- How should I compose them?
- Which components are historical or unresolved?
- How do I propose a new Upgradeable?
- How do I avoid duplicating an existing primitive?
- How can I generate a target Skill from selected Upgradeables?
- How can software query the registry?
- How can I validate a contribution?

The repository should function as both:

1. **a human-readable open specification/library**, and
2. **a machine-readable component registry suitable for agent/Skill tooling**.

---

# 49. IMMEDIATE FIRST ACTIONS FOR THE IMPLEMENTATION AGENT

Execute in this order:

1. Locate the three source Markdown files.
2. Read all three completely before normalizing architecture.
3. Create a source-to-registry conversion ledger.
4. Initialize the repository.
5. Preserve the source files under `archive/source/`.
6. Write the specification documents.
7. Define schemas and metadata conventions.
8. Populate foundational/current Upgradeables.
9. Index historical aliases, generations, families, and unresolved entries.
10. Build recipe and composition documents.
11. Build machine-readable registry.
12. Add scripts/tests.
13. Add GitHub contribution/governance files.
14. Generate the all-in-one artifact.
15. Run validation/tests.
16. Review `git diff` and source traceability.
17. Commit.
18. Publish to GitHub if `gh` is authenticated.
19. Return the completion report.

---

# 50. FINAL ARCHITECTURAL NORTH STAR

The project should evolve toward this model:

```text
                    OS PHILOSOPHY
                         │
                         ▼
                 SKILL BUILDER SPEC
                         │
              ┌──────────┴───────────┐
              ▼                      ▼
        Skill Type Recipe     Upgradeable Registry
              │                      │
              └──────────┬───────────┘
                         ▼
                 Composition Layer
                         │
       ┌─────────────────┼─────────────────┐
       ▼                 ▼                 ▼
 Behavior Gene      Domain Core       Upgradeables
       │                 │                 │
       └─────────────────┼─────────────────┘
                         ▼
                    Validators
                         │
                         ▼
             Skill / Agent Workflow
```

The open-source contribution model should expand the registry without destroying that distinction.

The goal is not to preserve every historical metaphor as sacred implementation.

The goal is to preserve provenance while translating useful concepts into explicit, modular, testable, composable mechanisms.

**Build the repository accordingly.**
