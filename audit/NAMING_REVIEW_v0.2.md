# Plain-Language Naming Review

Status: recommendation only. No canonical slug, path, ID, or historical name is
changed by this review.

The recovered names are part of the repository's provenance, but many are hard
for a newcomer to interpret or search. The safest transition is to keep stable
canonical slugs and introduce clearer display names and searchable aliases.
Natural-language discovery can then improve without breaking links, recipes,
Skills, or downstream tooling.

## Recommended policy

- Treat `id` and `slug` as stable identity keys.
- Let a plain-language display name evolve independently.
- Preserve recovered terms in `historical_aliases`; add user-facing terms in
  `plain_aliases` and outcome-oriented examples in `task_phrases`.
- Do not migrate paths until a versioned redirect and deprecation mechanism
  exists. The items marked **future migration** are candidates, not approved
  renames.
- Make control nouns predictable: a **gate** decides, a **guard** prevents, a
  **check** observes, a **controller** adjusts, a **builder** constructs, a
  **mode** defines an operating regime, a **scaffold** is temporary, and a
  **supervisor** coordinates controls.
- Avoid unexplained acronyms, promotional guarantees, anthropomorphic language,
  and biological, physics, or fictional metaphors in primary display names.

## Future migration candidates

Use the proposed name as a display name and search alias now. Consider changing
the slug only after redirects are supported.

| Canonical slug | Proposed plain-language name |
|---|---|
| `cot-structured-state-block` | Auditable Reasoning State |
| `crispr-edit` | Precision Local System Edit |
| `cross-context-resonance-lock` | Cross-Context Relationship Guard |
| `cross-universe-consistency` | Alternative-Scenario Consistency Check |
| `drift-sink-scaffold` | Retired-Branch Quarantine |
| `fermionic-veto` | Non-Compensable Constraint Veto |
| `hybrid-mode` | Explore-Then-Commit Mode |
| `multi-truth-gating` | Independent Evidence Gate |
| `multiverse-reasoning` | Bounded Alternative Search |
| `neuro-focus` | Bounded Attention Focus |
| `phase-locked-reasoning-scaffold` | Stage-Separated Reasoning Scaffold |
| `power-mode` | Deep Exploration Mode |
| `reflectos` | Checkpointed Work Reflection |
| `resonance` | Cross-Module Coordination |
| `resonance-gene-builder` | Cross-Module Coordination Rule Builder |
| `safe-mode` | Conservative Execution Mode |
| `selfblock-auto-update` | Automatic Canonical-State Update |
| `state-routing-bus` | Task-State Handoff Router |
| `stateblock` | Canonical Task State |
| `surgery-edit` | Structural System Edit |
| `two-truths-and-corridor` | Dual-Source Bounded Synthesis |

These names carry the highest confusion risk. Terms such as CoT, CRISPR,
fermionic, multiverse, neuro, resonance, and surgery imply unrelated domains;
`power`, `safe`, and `future-proof` can also read as guarantees. Retaining them
as historical aliases preserves the recovered architecture without making
newcomers decode the metaphor first.

## Add a plain alias

| Canonical slug | Proposed plain-language name |
|---|---|
| `activation-budget-funnel` | Progressive Context Intake |
| `behavior-gene-builder` | Reusable Behavior Component Builder |
| `bounded-exit` | Bounded Iteration Stop Rule |
| `coherence-heartbeat` | Periodic Whole-Task Consistency Check |
| `domain-core-builder` | Shared Domain Knowledge Component Builder |
| `domain-normalized-drift` | Domain-Calibrated Change Tolerance |
| `drift-immunity-propagation` | Downstream Invariant Protection |
| `drift-spectra-scaling` | Content-Specific Change Tolerance |
| `parallel-qms` | Parallel Validation System |
| `sequential-memory-state-engine` | Ordered Memory-State Update Engine |
| `truth-redundancy` | Independent Evidence Redundancy |

The original terms remain useful to people who know the recovered framework,
but the proposed names better match task language. Acronyms such as ABF, DIP,
QMS, and SMSE should never trigger a search result without supporting context.

## Change the display name only

| Canonical slug | Proposed display name |
|---|---|
| `architect-orchestrator` | Modular System Design Orchestrator |
| `attention-compression-scaffold` | Temporary Focused-Context View |
| `authenticity-anti-evasion` | Capability and Completion Honesty Gate |
| `cognitive-governor` | Reasoning Effort Budget Controller |
| `compute-adaptive-drift` | Runtime-Adaptive Drift Checks |
| `controlled-drift-corridors` | Bounded Change Rules |
| `counterfactual-silence-scaffold` | No-Unrequested-Scenarios Guard |
| `critical-atomic-verification` | Critical Fact Verification |
| `dynamic-depth-allocation` | Per-Region Reasoning Depth |
| `epistemic-status-gating` | Evidence-Confidence Gate |
| `explanation-minimality-scaffold` | Minimum Sufficient Explanation |
| `future-proof-mode-selector` | Runtime Compatibility Mode Selector |
| `invariance-stress-scaffold` | Protected-Constraint Robustness Test |
| `meta-awareness` | Workflow Health Monitor |
| `meta-stability` | Stable-State Recovery Mode |
| `meta-supervisor` | Workflow Repair Supervisor |
| `micro-repair` | Minimal Local Correction |
| `model-size-drift-scaling` | Model-Capability Scaffolding Scale |
| `progressive-mode-shaping` | Explore-to-Execute Transition |
| `reasoning-scale-controller` | Task-Scope Reasoning Controller |
| `reasoning-throughput-governor` | Reasoning Efficiency Controller |
| `regenerative-rewrite` | Full-Structure Invariant-Preserving Rewrite |
| `specificity-penalty-gate` | Unsupported Precision Gate |
| `ultimate-suite-supervisor` | Suite-Wide Workflow Supervisor |
| `zero-drift-zones` | Immutable Content Zones |

## Names that are already serviceable

The remaining 39 canonical names are literal enough to retain:

`adapter-first-experimentation`, `anti-tunnel-vision`,
`authority-anchor-enforcement`, `bidirectional-consistency`,
`citation-fidelity`, `clarification-gateway`, `coherence-loops`,
`contradiction-micro-repair`, `counterfactual-integrity`,
`cross-checking-chains`, `decision-first-scaffold`,
`domain-mode-isolation`, `dominant-driver-isolation-scaffold`,
`drift-suppression`, `external-state-automation`,
`fail-closed-abstention`, `forethought-checkpoints`,
`grounding-no-invention`, `image-text-fidelity-capture`,
`micro-scaffolding`, `mode-lock-in`, `multi-layer-consistency`,
`non-authoritative-branch-suppression`, `pedagogical-alignment`,
`placeholder-suppression`, `risk-tier-scaling`, `safe-rewrite`,
`scoped-loader`, `stable-long-context`, `state-snapshot`,
`structured-refinement`, `structured-state-projection`,
`stuck-pattern-reset`, `style-alignment`, `task-set-lock-in`,
`temporal-anchor-scaffold`, `truth-priority-hierarchy`,
`working-memory-cues`, and `working-memory-lock-in`.

## Discovery implications

The proposed [`--task` discovery design](../docs/TASK_DISCOVERY_DESIGN.md) should
return the canonical slug, the matched alias, and a short reason. It should rank
exact IDs and slugs first, then plain aliases and task phrases, then historical
aliases, with fuzzy matching last. Closely related results should explain their
difference instead of silently choosing one.

Candidate discovery must not decide activation by itself. The final selection
still evaluates triggers, non-triggers, exclusions, source support, conflicts,
and task risk.
