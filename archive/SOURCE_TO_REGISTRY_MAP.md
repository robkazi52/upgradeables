# Source-to-Registry Map

This append-oriented ledger records how recovered items were normalized.

## v0.2 semantic traceability review

All 96 baseline operational rows were re-reviewed against all three immutable
source documents. Each package now carries structured `source_refs`; its
recovery decision, interpretation boundary, and exact source headings are in
[`audit/source-notes/`](../audit/source-notes/). The complete disposition table
is [`OPERATIONAL_PACKAGE_REVIEW_v0.2.md`](../audit/OPERATIONAL_PACKAGE_REVIEW_v0.2.md).
No historical line number was invented.

| Source name | Source ID | Registry generation | Recovery | Modern slug / destination | Disposition |
|---|---|---|---|---|---|
| Micro-Scaffolding | `T1-01` | `consolidated-2026-09` | `exact_recovery` | [`micro-scaffolding`](../upgradeables/foundation/micro-scaffolding/UPGRADEABLE.md) | operationalized |
| Drift Suppression | `T1-02` | `consolidated-2026-09` | `exact_recovery` | [`drift-suppression`](../upgradeables/drift-control/drift-suppression/UPGRADEABLE.md) | operationalized |
| Clarification Gateway | `T1-03` | `consolidated-2026-09` | `exact_recovery` | [`clarification-gateway`](../upgradeables/foundation/clarification-gateway/UPGRADEABLE.md) | operationalized |
| Grounding / No-Invention | `T1-04` | `consolidated-2026-09` | `exact_recovery` | [`grounding-no-invention`](../upgradeables/truth-grounding/grounding-no-invention/UPGRADEABLE.md) | operationalized |
| Mode Lock-In | `T1-05` | `consolidated-2026-09` | `exact_recovery` | [`mode-lock-in`](../upgradeables/state/mode-lock-in/UPGRADEABLE.md) | operationalized |
| Task-Set Lock-In | `T1-06` | `consolidated-2026-09` | `exact_recovery` | [`task-set-lock-in`](../upgradeables/state/task-set-lock-in/UPGRADEABLE.md) | operationalized |
| Scoped Loader / Loader Sequencing | `T1-07` | `consolidated-2026-09` | `exact_recovery` | [`scoped-loader`](../upgradeables/context-retrieval/scoped-loader/UPGRADEABLE.md) | operationalized |
| Scoped Loader / Loader Sequencing cross-reference | `O-02` | source-specific | `exact_recovery` | [`scoped-loader`](../upgradeables/context-retrieval/scoped-loader/UPGRADEABLE.md) | alias |
| Placeholder Suppression | `T1-08` | `consolidated-2026-09` | `exact_recovery` | [`placeholder-suppression`](../upgradeables/output/placeholder-suppression/UPGRADEABLE.md) | operationalized |
| Working-Memory Cues | `T1-09` | `consolidated-2026-09` | `exact_recovery` | [`working-memory-cues`](../upgradeables/state/working-memory-cues/UPGRADEABLE.md) | operationalized |
| Safe Rewrite Logic | `T1-10` | `consolidated-2026-09` | `exact_recovery` | [`safe-rewrite`](../upgradeables/editing-repair/safe-rewrite/UPGRADEABLE.md) | operationalized |
| Bounded ExIt | `T2-01` | `consolidated-2026-09` | `exact_recovery` | [`bounded-exit`](../upgradeables/reasoning/bounded-exit/UPGRADEABLE.md) | operationalized |
| Structured Refinement Cycles | `T2-02` | `consolidated-2026-09` | `exact_recovery` | [`structured-refinement`](../upgradeables/editing-repair/structured-refinement/UPGRADEABLE.md) | operationalized |
| Regenerative Rewrite | `T2-03` | `consolidated-2026-09` | `exact_recovery` | [`regenerative-rewrite`](../upgradeables/editing-repair/regenerative-rewrite/UPGRADEABLE.md) | operationalized |
| Regenerative Rewrite cross-reference | `A-10` | source-specific | `exact_recovery` | [`regenerative-rewrite`](../upgradeables/editing-repair/regenerative-rewrite/UPGRADEABLE.md) | alias |
| Micro-Repair | `T2-04` | `consolidated-2026-09` | `exact_recovery` | [`micro-repair`](../upgradeables/editing-repair/micro-repair/UPGRADEABLE.md) | operationalized |
| Multi-Layer Consistency | `T2-05` | `consolidated-2026-09` | `exact_recovery` | [`multi-layer-consistency`](../upgradeables/validation/multi-layer-consistency/UPGRADEABLE.md) | operationalized |
| Progressive Mode Shaping | `T2-06` | `consolidated-2026-09` | `exact_recovery` | [`progressive-mode-shaping`](../upgradeables/orchestration/progressive-mode-shaping/UPGRADEABLE.md) | operationalized |
| Stable Long-Context | `T2-07` | `consolidated-2026-09` | `exact_recovery` | [`stable-long-context`](../upgradeables/state/stable-long-context/UPGRADEABLE.md) | operationalized |
| Working-Memory Lock-In | `T2-08` | `consolidated-2026-09` | `exact_recovery` | [`working-memory-lock-in`](../upgradeables/state/working-memory-lock-in/UPGRADEABLE.md) | operationalized |
| StateBlock | `T2-09` | `consolidated-2026-09` | `exact_recovery` | [`stateblock`](../upgradeables/state/stateblock/UPGRADEABLE.md) | operationalized |
| CoT-Structured State Block | `STATE-2025-12-03-T3` | `consolidated-2026-09` | `exact_recovery` | [`cot-structured-state-block`](../upgradeables/state/cot-structured-state-block/UPGRADEABLE.md) | operationalized |
| Sequential Memory State Engine (SMSE) | `T2-10` | `consolidated-2026-09` | `exact_recovery` | [`sequential-memory-state-engine`](../upgradeables/state/sequential-memory-state-engine/UPGRADEABLE.md) | operationalized |
| SelfBlock Auto-Update | `T2-11` | `consolidated-2026-09` | `exact_recovery` | [`selfblock-auto-update`](../upgradeables/state/selfblock-auto-update/UPGRADEABLE.md) | operationalized |
| Work Reflection Loop OS / ReflectOS | `T2-12` | `consolidated-2026-09` | `exact_recovery` | [`reflectos`](../upgradeables/validation/reflectos/UPGRADEABLE.md) | operationalized |
| Image Text Fidelity Capture | `T2-14A` | `consolidated-2026-09` | `exact_recovery` | [`image-text-fidelity-capture`](../upgradeables/truth-grounding/image-text-fidelity-capture/UPGRADEABLE.md) | operationalized |
| Activation-Budget Funnel | `T2-16` | `consolidated-2026-09` | `exact_recovery` | [`activation-budget-funnel`](../upgradeables/context-retrieval/activation-budget-funnel/UPGRADEABLE.md) | operationalized |
| Forethought / Checkpoints | `T2-17` | `consolidated-2026-09` | `exact_recovery` | [`forethought-checkpoints`](../upgradeables/reasoning/forethought-checkpoints/UPGRADEABLE.md) | operationalized |
| Bidirectional Consistency | `T2-18` | `consolidated-2026-09` | `exact_recovery` | [`bidirectional-consistency`](../upgradeables/validation/bidirectional-consistency/UPGRADEABLE.md) | operationalized |
| Anti-Tunnel Vision | `T2-19` | `consolidated-2026-09` | `exact_recovery` | [`anti-tunnel-vision`](../upgradeables/reasoning/anti-tunnel-vision/UPGRADEABLE.md) | operationalized |
| External State Automation | `T2-20` | `consolidated-2026-09` | `exact_recovery` | [`external-state-automation`](../upgradeables/persistence/external-state-automation/UPGRADEABLE.md) | operationalized |
| Adapter-First Experimentation | `T2-21` | `consolidated-2026-09` | `exact_recovery` | [`adapter-first-experimentation`](../upgradeables/meta-control/adapter-first-experimentation/UPGRADEABLE.md) | operationalized |
| Reasoning-Scale Controller | `RS-00` | `consolidated-2026-09` | `exact_recovery` | [`reasoning-scale-controller`](../upgradeables/reasoning/reasoning-scale-controller/UPGRADEABLE.md) | operationalized |
| Multi-Truth Gating | `T3-01` | `consolidated-2026-09` | `exact_recovery` | [`multi-truth-gating`](../upgradeables/truth-grounding/multi-truth-gating/UPGRADEABLE.md) | operationalized |
| Controlled Drift Corridors | `T3-02` | `consolidated-2026-09` | `exact_recovery` | [`controlled-drift-corridors`](../upgradeables/drift-control/controlled-drift-corridors/UPGRADEABLE.md) | operationalized |
| Truth Redundancy | `T3-03` | `consolidated-2026-09` | `exact_recovery` | [`truth-redundancy`](../upgradeables/truth-grounding/truth-redundancy/UPGRADEABLE.md) | operationalized |
| Critical Atomic Verification | `T3-04` | `consolidated-2026-09` | `exact_recovery` | [`critical-atomic-verification`](../upgradeables/validation/critical-atomic-verification/UPGRADEABLE.md) | operationalized |
| Risk-Tier Scaling | `T3-05` | `consolidated-2026-09` | `exact_recovery` | [`risk-tier-scaling`](../upgradeables/meta-control/risk-tier-scaling/UPGRADEABLE.md) | operationalized |
| Truth Priority Hierarchy | `T3-06` | `consolidated-2026-09` | `exact_recovery` | [`truth-priority-hierarchy`](../upgradeables/truth-grounding/truth-priority-hierarchy/UPGRADEABLE.md) | operationalized |
| Cross-Checking Chains | `T3-07` | `consolidated-2026-09` | `exact_recovery` | [`cross-checking-chains`](../upgradeables/validation/cross-checking-chains/UPGRADEABLE.md) | operationalized |
| Two Truths + Corridor | `T3-08` | `consolidated-2026-09` | `exact_recovery` | [`two-truths-and-corridor`](../upgradeables/truth-grounding/two-truths-and-corridor/UPGRADEABLE.md) | operationalized |
| Fermionic Veto Strengthening | `T3-09` | `consolidated-2026-09` | `exact_recovery` | [`fermionic-veto`](../upgradeables/validation/fermionic-veto/UPGRADEABLE.md) | operationalized |
| Domain / Mode Isolation | `T3-10` | `consolidated-2026-09` | `exact_recovery` | [`domain-mode-isolation`](../upgradeables/state/domain-mode-isolation/UPGRADEABLE.md) | operationalized |
| Fail-Closed Abstention | `T3-11` | `consolidated-2026-09` | `exact_recovery` | [`fail-closed-abstention`](../upgradeables/truth-grounding/fail-closed-abstention/UPGRADEABLE.md) | operationalized |
| Counterfactual Integrity Gate | `T3-12` | `consolidated-2026-09` | `exact_recovery` | [`counterfactual-integrity`](../upgradeables/truth-grounding/counterfactual-integrity/UPGRADEABLE.md) | operationalized |
| Citation Fidelity Gate | `T3-13` | `consolidated-2026-09` | `exact_recovery` | [`citation-fidelity`](../upgradeables/validation/citation-fidelity/UPGRADEABLE.md) | operationalized |
| Zero-Drift Zones | `T3-14` | `consolidated-2026-09` | `exact_recovery` | [`zero-drift-zones`](../upgradeables/drift-control/zero-drift-zones/UPGRADEABLE.md) | operationalized |
| Style-Alignment Module | `T3-15` | `consolidated-2026-09` | `exact_recovery` | [`style-alignment`](../upgradeables/output/style-alignment/UPGRADEABLE.md) | operationalized |
| Pedagogical Alignment Constraint | `T3-16` | `consolidated-2026-09` | `exact_recovery` | [`pedagogical-alignment`](../upgradeables/output/pedagogical-alignment/UPGRADEABLE.md) | operationalized |
| Reasoning Budget / Cognitive Governor | `T3-17` | `consolidated-2026-09` | `exact_recovery` | [`cognitive-governor`](../upgradeables/meta-control/cognitive-governor/UPGRADEABLE.md) | operationalized |
| Authenticity & Anti-Evasion Principle | `T3-18` | `consolidated-2026-09` | `exact_recovery` | [`authenticity-anti-evasion`](../upgradeables/truth-grounding/authenticity-anti-evasion/UPGRADEABLE.md) | operationalized |
| Parallel Quality Management System | `PQ-00` | `consolidated-2026-09` | `exact_recovery` | [`parallel-qms`](../upgradeables/validation/parallel-qms/UPGRADEABLE.md) | operationalized |
| Multiverse Engine | `A-01` | `consolidated-2026-09` | `exact_recovery` | [`multiverse-reasoning`](../upgradeables/reasoning/multiverse-reasoning/UPGRADEABLE.md) | operationalized |
| State Routing Bus | `A-02` | `consolidated-2026-09` | `exact_recovery` | [`state-routing-bus`](../upgradeables/orchestration/state-routing-bus/UPGRADEABLE.md) | operationalized |
| Global Coherence Heartbeat | `A-04` | `consolidated-2026-09` | `exact_recovery` | [`coherence-heartbeat`](../upgradeables/validation/coherence-heartbeat/UPGRADEABLE.md) | operationalized |
| Resonance | `A-05` | `consolidated-2026-09` | `exact_recovery` | [`resonance`](../upgradeables/orchestration/resonance/UPGRADEABLE.md) | operationalized |
| Resonance Gene Builder | `A-06` | `consolidated-2026-09` | `exact_recovery` | [`resonance-gene-builder`](../upgradeables/meta-control/resonance-gene-builder/UPGRADEABLE.md) | operationalized |
| CRISPR Editing | `A-07` | `consolidated-2026-09` | `exact_recovery` | [`crispr-edit`](../upgradeables/editing-repair/crispr-edit/UPGRADEABLE.md) | operationalized |
| Surgery Editing | `A-08` | `consolidated-2026-09` | `exact_recovery` | [`surgery-edit`](../upgradeables/editing-repair/surgery-edit/UPGRADEABLE.md) | operationalized |
| Neuro-Focus | `A-09` | `consolidated-2026-09` | `exact_recovery` | [`neuro-focus`](../upgradeables/context-retrieval/neuro-focus/UPGRADEABLE.md) | operationalized |
| Coherence Loops | `A-11` | `consolidated-2026-09` | `exact_recovery` | [`coherence-loops`](../upgradeables/validation/coherence-loops/UPGRADEABLE.md) | operationalized |
| Behavior Gene Builder | `BG-00` | `consolidated-2026-09` | `exact_recovery` | [`behavior-gene-builder`](../upgradeables/meta-control/behavior-gene-builder/UPGRADEABLE.md) | operationalized |
| Domain Core Builder | `C-00` | `consolidated-2026-09` | `exact_recovery` | [`domain-core-builder`](../upgradeables/meta-control/domain-core-builder/UPGRADEABLE.md) | operationalized |
| Architect Orchestrator | `O-01` | `consolidated-2026-09` | `exact_recovery` | [`architect-orchestrator`](../upgradeables/orchestration/architect-orchestrator/UPGRADEABLE.md) | operationalized |
| State Snapshot | `O-03` | `consolidated-2026-09` | `exact_recovery` | [`state-snapshot`](../upgradeables/state/state-snapshot/UPGRADEABLE.md) | operationalized |
| Meta-Supervisor Bundle | `T4-01` | `consolidated-2026-09` | `exact_recovery` | [`meta-supervisor`](../upgradeables/meta-control/meta-supervisor/UPGRADEABLE.md) | operationalized |
| Meta-Awareness Pack | `T4-02` | `consolidated-2026-09` | `exact_recovery` | [`meta-awareness`](../upgradeables/meta-control/meta-awareness/UPGRADEABLE.md) | operationalized |
| Stuck-Pattern Reset Pack | `T4-03` | `consolidated-2026-09` | `exact_recovery` | [`stuck-pattern-reset`](../upgradeables/meta-control/stuck-pattern-reset/UPGRADEABLE.md) | operationalized |
| Contradiction Micro-Repair Pack | `T4-04` | `consolidated-2026-09` | `exact_recovery` | [`contradiction-micro-repair`](../upgradeables/editing-repair/contradiction-micro-repair/UPGRADEABLE.md) | operationalized |
| Ultimate Suite Supervisor | `T4-05` | `consolidated-2026-09` | `exact_recovery` | [`ultimate-suite-supervisor`](../upgradeables/meta-control/ultimate-suite-supervisor/UPGRADEABLE.md) | operationalized |
| SAFE Mode | `T4-06` | `consolidated-2026-09` | `exact_recovery` | [`safe-mode`](../upgradeables/meta-control/safe-mode/UPGRADEABLE.md) | operationalized |
| POWER Mode | `T4-07` | `consolidated-2026-09` | `exact_recovery` | [`power-mode`](../upgradeables/meta-control/power-mode/UPGRADEABLE.md) | operationalized |
| HYBRID Mode | `T4-08` | `consolidated-2026-09` | `exact_recovery` | [`hybrid-mode`](../upgradeables/meta-control/hybrid-mode/UPGRADEABLE.md) | operationalized |
| Drift-Spectra Scaling | `T4-09` | `consolidated-2026-09` | `exact_recovery` | [`drift-spectra-scaling`](../upgradeables/drift-control/drift-spectra-scaling/UPGRADEABLE.md) | operationalized |
| Compute-Adaptive Drift Constraining | `T4-10` | `consolidated-2026-09` | `exact_recovery` | [`compute-adaptive-drift`](../upgradeables/drift-control/compute-adaptive-drift/UPGRADEABLE.md) | operationalized |
| Domain-Normalized Drift Field | `T4-11` | `consolidated-2026-09` | `exact_recovery` | [`domain-normalized-drift`](../upgradeables/drift-control/domain-normalized-drift/UPGRADEABLE.md) | operationalized |
| Dynamic Depth Allocation | `T4-12` | `consolidated-2026-09` | `exact_recovery` | [`dynamic-depth-allocation`](../upgradeables/meta-control/dynamic-depth-allocation/UPGRADEABLE.md) | operationalized |
| Reasoning Throughput Governor | `T4-13` | `consolidated-2026-09` | `exact_recovery` | [`reasoning-throughput-governor`](../upgradeables/meta-control/reasoning-throughput-governor/UPGRADEABLE.md) | operationalized |
| Drift Immunity Propagation | `T4-14` | `consolidated-2026-09` | `exact_recovery` | [`drift-immunity-propagation`](../upgradeables/drift-control/drift-immunity-propagation/UPGRADEABLE.md) | operationalized |
| Meta-Stability Mode | `T4-15` | `consolidated-2026-09` | `exact_recovery` | [`meta-stability`](../upgradeables/meta-control/meta-stability/UPGRADEABLE.md) | operationalized |
| Cross-Universe Consistency Mode | `T4-16` | `consolidated-2026-09` | `exact_recovery` | [`cross-universe-consistency`](../upgradeables/validation/cross-universe-consistency/UPGRADEABLE.md) | operationalized |
| Future-Proof Mode Selector | `T4-17` | `consolidated-2026-09` | `exact_recovery` | [`future-proof-mode-selector`](../upgradeables/meta-control/future-proof-mode-selector/UPGRADEABLE.md) | operationalized |
| Drift-Stability Scaling with Model Size | `T4-18` | `consolidated-2026-09` | `exact_recovery` | [`model-size-drift-scaling`](../upgradeables/meta-control/model-size-drift-scaling/UPGRADEABLE.md) | operationalized |
| Phase-Locked Reasoning Scaffold | `JAN26-01` | `training-scaffolding-2026-01-05` | `partial_recovery` | [`phase-locked-reasoning-scaffold`](../upgradeables/reasoning/phase-locked-reasoning-scaffold/UPGRADEABLE.md) | operationalized |
| Attention Compression Scaffold | `JAN26-02` | `training-scaffolding-2026-01-05` | `partial_recovery` | [`attention-compression-scaffold`](../upgradeables/context-retrieval/attention-compression-scaffold/UPGRADEABLE.md) | operationalized |
| Dominant-Driver Isolation Scaffold | `JAN26-03` | `training-scaffolding-2026-01-05` | `partial_recovery` | [`dominant-driver-isolation-scaffold`](../upgradeables/reasoning/dominant-driver-isolation-scaffold/UPGRADEABLE.md) | operationalized |
| Decision-First Scaffold | `JAN26-04` | `training-scaffolding-2026-01-05` | `partial_recovery` | [`decision-first-scaffold`](../upgradeables/reasoning/decision-first-scaffold/UPGRADEABLE.md) | operationalized |
| Epistemic Status Gating | `JAN26-05` | `training-scaffolding-2026-01-05` | `partial_recovery` | [`epistemic-status-gating`](../upgradeables/truth-grounding/epistemic-status-gating/UPGRADEABLE.md) | operationalized |
| Counterfactual Silence Scaffold | `JAN26-06` | `training-scaffolding-2026-01-05` | `partial_recovery` | [`counterfactual-silence-scaffold`](../upgradeables/truth-grounding/counterfactual-silence-scaffold/UPGRADEABLE.md) | operationalized |
| Temporal Anchor Scaffold | `JAN26-07` | `training-scaffolding-2026-01-05` | `partial_recovery` | [`temporal-anchor-scaffold`](../upgradeables/state/temporal-anchor-scaffold/UPGRADEABLE.md) | operationalized |
| Explanation Minimality Scaffold | `JAN26-08` | `training-scaffolding-2026-01-05` | `partial_recovery` | [`explanation-minimality-scaffold`](../upgradeables/output/explanation-minimality-scaffold/UPGRADEABLE.md) | operationalized |
| Invariance Stress Scaffold | `JAN26-09` | `training-scaffolding-2026-01-05` | `partial_recovery` | [`invariance-stress-scaffold`](../upgradeables/validation/invariance-stress-scaffold/UPGRADEABLE.md) | operationalized |
| Drift Sink Scaffold | `JAN26-10` | `training-scaffolding-2026-01-05` | `partial_recovery` | [`drift-sink-scaffold`](../upgradeables/drift-control/drift-sink-scaffold/UPGRADEABLE.md) | operationalized |
| Cross-Context Resonance Lock | `JAN26-11` | `training-scaffolding-2026-01-05` | `partial_recovery` | [`cross-context-resonance-lock`](../upgradeables/orchestration/cross-context-resonance-lock/UPGRADEABLE.md) | operationalized |
| Authority Anchor Enforcement | `JAN26-12` | `training-scaffolding-2026-01-05` | `partial_recovery` | [`authority-anchor-enforcement`](../upgradeables/orchestration/authority-anchor-enforcement/UPGRADEABLE.md) | operationalized |
| Structured State Projection | `JAN26-13` | `training-scaffolding-2026-01-05` | `partial_recovery` | [`structured-state-projection`](../upgradeables/state/structured-state-projection/UPGRADEABLE.md) | operationalized |
| Non-Authoritative Branch Suppression | `JAN26-14` | `training-scaffolding-2026-01-05` | `partial_recovery` | [`non-authoritative-branch-suppression`](../upgradeables/drift-control/non-authoritative-branch-suppression/UPGRADEABLE.md) | operationalized |
| Specificity Penalty Gate | `JAN26-15` | `training-scaffolding-2026-01-05` | `partial_recovery` | [`specificity-penalty-gate`](../upgradeables/validation/specificity-penalty-gate/UPGRADEABLE.md) | operationalized |
| Singularity Cores | `A-03` | consolidated-2026-09 | `exact_recovery` | [`cores/`](../cores/) | merged-as-framework |
| Mirror QMS | `PQ-01` | consolidated-2026-09 | `exact_recovery` | [`mirror`](../bundles/qms/QMS_VARIANTS.md) | merged-as-mode |
| Risk-Tier-Split QMS | `PQ-02` | consolidated-2026-09 | `exact_recovery` | [`risk-tier-split`](../bundles/qms/QMS_VARIANTS.md) | merged-as-mode |
| Cross-Phase QMS | `PQ-03` | consolidated-2026-09 | `exact_recovery` | [`cross-phase`](../bundles/qms/QMS_VARIANTS.md) | merged-as-mode |
| Redundancy-QMS | `PQ-04` | consolidated-2026-09 | `exact_recovery` | [`redundancy`](../bundles/qms/QMS_VARIANTS.md) | merged-as-mode |
| ExIt-Integrated QMS | `PQ-05` | consolidated-2026-09 | `exact_recovery` | [`exit-integrated`](../bundles/qms/QMS_VARIANTS.md) | merged-as-mode |
| Hierarchical QMS | `PQ-06` | consolidated-2026-09 | `exact_recovery` | [`hierarchical`](../bundles/qms/QMS_VARIANTS.md) | merged-as-mode |
| Transversal QMS | `PQ-07` | consolidated-2026-09 | `exact_recovery` | [`transversal`](../bundles/qms/QMS_VARIANTS.md) | merged-as-mode |
| Heterogeneous QMS | `PQ-08` | consolidated-2026-09 | `exact_recovery` | [`heterogeneous`](../bundles/qms/QMS_VARIANTS.md) | merged-as-mode |
| Monte QMS | `PQ-09` | consolidated-2026-09 | `exact_recovery` | [`monte`](../bundles/qms/QMS_VARIANTS.md) | merged-as-mode |
| Inversion QMS | `PQ-10` | consolidated-2026-09 | `exact_recovery` | [`inversion`](../bundles/qms/QMS_VARIANTS.md) | merged-as-mode |
| Conflict-Resolution QMS | `PQ-11` | consolidated-2026-09 | `exact_recovery` | [`conflict-resolution`](../bundles/qms/QMS_VARIANTS.md) | merged-as-mode |
| Distributed QMS | `PQ-12` | consolidated-2026-09 | `exact_recovery` | [`distributed`](../bundles/qms/QMS_VARIANTS.md) | merged-as-mode |
| Meta-QMS | `PQ-13` | consolidated-2026-09 | `exact_recovery` | [`meta`](../bundles/qms/QMS_VARIANTS.md) | merged-as-mode |
| Semantic Glass-Box QMS | `PQ-14` | consolidated-2026-09 | `exact_recovery` | [`semantic-glass-box`](../bundles/qms/QMS_VARIANTS.md) | merged-as-mode |
| Ethical QMS | `PQ-15` | consolidated-2026-09 | `exact_recovery` | [`ethical`](../bundles/qms/QMS_VARIANTS.md) | merged-as-mode |
| IPMN Gene | `BG-01` | consolidated-2026-09 | `exact_recovery` | [`ipmn`](../genes/examples/ipmn.md) | behavior-gene |
| IPTA Gene | `BG-02` | consolidated-2026-09 | `exact_recovery` | [`ipta`](../genes/examples/ipta.md) | behavior-gene |
| OPMN Gene | `BG-03` | consolidated-2026-09 | `exact_recovery` | [`opmn`](../genes/examples/opmn.md) | behavior-gene |
| OPTA Gene | `BG-04` | consolidated-2026-09 | `exact_recovery` | [`opta`](../genes/examples/opta.md) | behavior-gene |
| Readmission Gene | `BG-05` | consolidated-2026-09 | `exact_recovery` | [`readmission`](../genes/examples/readmission.md) | behavior-gene |
| GMN Gene | `BG-06` | consolidated-2026-09 | `exact_recovery` | [`gmn`](../genes/examples/gmn.md) | behavior-gene |
| Tone Genes | `BG-07` | consolidated-2026-09 | `exact_recovery` | [`tone`](../genes/examples/tone.md) | behavior-gene |
| Risk-Emphasis Genes | `BG-08` | consolidated-2026-09 | `exact_recovery` | [`risk-emphasis`](../genes/examples/risk-emphasis.md) | behavior-gene |
| Deep Summary Gene | `BG-09` | consolidated-2026-09 | `exact_recovery` | [`deep-summary`](../genes/examples/deep-summary.md) | behavior-gene |
| Compare-Contrast Gene | `BG-10` | consolidated-2026-09 | `exact_recovery` | [`compare-contrast`](../genes/examples/compare-contrast.md) | behavior-gene |
| Alignment Gene | `BG-11` | consolidated-2026-09 | `exact_recovery` | [`alignment`](../genes/examples/alignment.md) | behavior-gene |
| Conflict-Handling Gene | `BG-12` | consolidated-2026-09 | `exact_recovery` | [`conflict-handling`](../genes/examples/conflict-handling.md) | behavior-gene |
| Synthesis Gene | `BG-13` | consolidated-2026-09 | `exact_recovery` | [`synthesis`](../genes/examples/synthesis.md) | behavior-gene |
| Memory Gene | `BG-14` | consolidated-2026-09 | `exact_recovery` | [`memory`](../genes/examples/memory.md) | behavior-gene |
| IPMN Core | `C-01` | consolidated-2026-09 | `exact_recovery` | [`ipmn`](../cores/examples/ipmn.md) | core-reference |
| IPTA Core | `C-02` | consolidated-2026-09 | `exact_recovery` | [`ipta`](../cores/examples/ipta.md) | core-reference |
| OPMN Core | `C-03` | consolidated-2026-09 | `exact_recovery` | [`opmn`](../cores/examples/opmn.md) | core-reference |
| OPTA Core | `C-04` | consolidated-2026-09 | `exact_recovery` | [`opta`](../cores/examples/opta.md) | core-reference |
| Readmission Core | `C-05` | consolidated-2026-09 | `exact_recovery` | [`readmission`](../cores/examples/readmission.md) | core-reference |
| GMN Core | `C-06` | consolidated-2026-09 | `exact_recovery` | [`gmn`](../cores/examples/gmn.md) | core-reference |
| Policy Core | `C-07` | consolidated-2026-09 | `exact_recovery` | [`policy`](../cores/examples/policy.md) | core-reference |
| Chart-Review Core | `C-08` | consolidated-2026-09 | `exact_recovery` | [`chart-review`](../cores/examples/chart-review.md) | core-reference |
| Analysis Core | `C-09` | consolidated-2026-09 | `exact_recovery` | [`analysis`](../cores/examples/analysis.md) | core-reference |
| Synthesis Core | `C-10` | consolidated-2026-09 | `exact_recovery` | [`synthesis`](../cores/examples/synthesis.md) | core-reference |
| Meta-Integrity Core | `C-11` | consolidated-2026-09 | `exact_recovery` | [`meta-integrity`](../cores/examples/meta-integrity.md) | core-reference |
| Architect OS | `D-01` | consolidated-2026-09 | `exact_recovery` | [`architect-os`](../domain-os/architect-os.md) | bundled |
| Appeal / CAF OS | `D-02` | consolidated-2026-09 | `exact_recovery` | [`appeal-caf-os`](../domain-os/appeal-caf-os.md) | bundled |
| Research & Decision OS | `D-03` | consolidated-2026-09 | `exact_recovery` | [`research-decision-os`](../domain-os/research-decision-os.md) | bundled |
| Paper-Author OS | `D-04` | consolidated-2026-09 | `exact_recovery` | [`paper-author-os`](../domain-os/paper-author-os.md) | bundled |
| Local Chat-Analysis Author OS | `D-05` | consolidated-2026-09 | `exact_recovery` | [`local-chat-analysis-author-os`](../domain-os/local-chat-analysis-author-os.md) | bundled |
| Multi-OS | `D-06` | consolidated-2026-09 | `exact_recovery` | [`multi-os`](../domain-os/multi-os.md) | bundled |
| Meta-OS / OS-Builder | `META-OS-HIST` | deep-recovery-2026-09 | `mixed A/B evidence` | [`meta-os-builder`](../domain-os/meta-os-builder.md) | bundled-provisional |
| FACT_SCOPE_GATE_T1 | `FACT_SCOPE_GATE_T1` | `frozen-t1-core-v1-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| NO_INFERENCE_GATE_APPEALS_T1 | `NO_INFERENCE_GATE_APPEALS_T1` | `frozen-t1-core-v1-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| HALLUCINATION_NO_MANS_LAND_T1 | `HALLUCINATION_NO_MANS_LAND_T1` | `frozen-t1-core-v1-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| UNKNOWNS_PROTOCOL_T1 | `UNKNOWNS_PROTOCOL_T1` | `frozen-t1-core-v1-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| UNCERTAINTY_CONTAINMENT_T1 | `UNCERTAINTY_CONTAINMENT_T1` | `frozen-t1-core-v1-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| CLINICAL_PLAUSIBILITY_GATE_T1 | `CLINICAL_PLAUSIBILITY_GATE_T1` | `frozen-t1-core-v1-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| EVIDENCE_CHAIN_BINDING_T1 | `EVIDENCE_CHAIN_BINDING_T1` | `frozen-t1-core-v1-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| PRIORITY_RETRIEVAL_LANES_T1 | `PRIORITY_RETRIEVAL_LANES_T1` | `frozen-t1-core-v1-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| GLOBAL_LOCAL_ANCHOR_SPLIT_T1 | `GLOBAL_LOCAL_ANCHOR_SPLIT_T1` | `frozen-t1-core-v1-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| ZERO_DRIFT_LOOP_T1 | `ZERO_DRIFT_LOOP_T1` | `frozen-t1-core-v1-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| SUPERVISOR_WORKER_PATTERN_T1 | `SUPERVISOR_WORKER_PATTERN_T1` | `frozen-t1-core-v1-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| UPGRADEABLE_ACTIVATION_TIERS_T1 | `UPGRADEABLE_ACTIVATION_TIERS_T1` | `frozen-t1-core-v1-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| RULE_INDEX_OS_T1 | `RULE_INDEX_OS_T1` | `frozen-t1-core-v1-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| DRIFT_MONITOR_T1 | `DRIFT_MONITOR_T1` | `frozen-t1-core-v1-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| EXECUTION_LOG_OS_T1 | `EXECUTION_LOG_OS_T1` | `frozen-t1-core-v1-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| PA_AI_BROKER_PATTERN_T1 | `PA_AI_BROKER_PATTERN_T1` | `frozen-t1-core-v1-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| PA_RULE_LOADER_FROM_INDEX_T1 | `PA_RULE_LOADER_FROM_INDEX_T1` | `frozen-t1-core-v1-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| PA_QUEUE_BASED_AI_REQUESTS_T1 | `PA_QUEUE_BASED_AI_REQUESTS_T1` | `frozen-t1-core-v1-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Novelty & Creativity Expansion | `T2-008` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Micro-Creative Mode | `T2-009` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Cognitive Flexibility | `T2-010` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Perspective Break | `T2-011` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Strange Loop Generator | `T2-012` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Balanced Exploration | `T2-013` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Dream-Mode Creative | `T2-014` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Hypnagogic Divergence | `T2-015` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Grounding & Reality Testing | `T2-016` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Drift Blocker (Inhibition) | `T2-017` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Chain-of-Thought Stabilizer | `T2-018` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Oscillation Regulator | `T2-019` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Deliberate Pacing | `T2-020` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Noise Suppression | `T2-021` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Reasoning Simplification | `T2-022` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Global Stabilizer (Macro) | `T2-023` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Reasoning Resection | `T2-031` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Cognitive Debridement | `T2-032` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Structural Reconstruction | `T2-033` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Reasoning Anastomosis | `T2-034` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Context Revascularization | `T2-035` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Cognitive Prosthetics | `T2-036` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Global Trauma Stabilizer | `T2-037` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Ethical Reasoning OS | `ELROS` | `legacy-reasoning-os` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Social Reasoning OS | `SOROS` | `legacy-reasoning-os` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Conflict-Resolution OS | `PROOS` | `legacy-reasoning-os` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Temporal OS | `TIMOS` | `legacy-reasoning-os` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Optimization Governor OS | `GROOS` | `legacy-reasoning-os` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Learning & Adaptation OS | `ALMOS` | `legacy-reasoning-os` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Creativity Regulator OS | `CROS` | `legacy-reasoning-os` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| GLOBAL OS | `GLOBAL-OS` | `historical-domain-os` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| INTAKE OS | `INTAKE-OS` | `historical-domain-os` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| OPMN Family OS | `OPMN-FAMILY-OS` | `historical-domain-os` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| OPMN Blueprint | `OPMN-BLUEPRINT` | `historical-domain-os` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| CAF routing: IPMN/IPTA/OPMN/OPTA/READM/GMN | `CAF-ROUTING` | `historical-domain-os` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Safety | `family:safety` | `frozen-t1-core-v1-2025-11-28` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Reasoning | `family:reasoning` | `frozen-t1-core-v1-2025-11-28` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Retrieval / Context | `family:retrieval-context` | `frozen-t1-core-v1-2025-11-28` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Memory / Anchoring | `family:memory-anchoring` | `frozen-t1-core-v1-2025-11-28` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Scaffolding | `family:scaffolding` | `frozen-t1-core-v1-2025-11-28` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Multi-Agent / Supervision | `family:multi-agent-supervision` | `frozen-t1-core-v1-2025-11-28` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Governance | `family:governance` | `frozen-t1-core-v1-2025-11-28` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Monitoring / Drift | `family:monitoring-drift` | `frozen-t1-core-v1-2025-11-28` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Neuro-Focus | `T2-001..007` | `frozen-t2-master-2025-11-28` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Creative / Exploration | `T2-008..015` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Stability / Suppression | `T2-016..023` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| CRISPR Micro-Editing | `T2-024..030` | `frozen-t2-master-2025-11-28` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Surgical Macro-Editing | `T2-031..037` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Resonance / Coherence | `T2-038..043` | `frozen-t2-master-2025-11-28` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Duration / Intensity | `T2-044..046` | `frozen-t2-master-2025-11-28` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Energy / Efficiency | `T2-047..049` | `frozen-t2-master-2025-11-28` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Immune / Anti-Contamination | `T2-050..052` | `frozen-t2-master-2025-11-28` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Interpersonal / Tone | `T2-053..056` | `frozen-t2-master-2025-11-28` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Consciousness Layer | `T2-057..060` | `frozen-t2-master-2025-11-28` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Supervisor / Orchestration | `T2-061..067` | `frozen-t2-master-2025-11-28` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Primary Scaffolding | `classification:primary_scaffolding` | `training-scaffolding-2026-01-05` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| Micro-Scaffolding | `classification:micro_scaffolding` | `training-scaffolding-2026-01-05` | `family_recovery` | [`registry/historical/index.yaml`](../registry/historical/index.yaml) | historical_only |
| SEMANTIC_ANCHORING_PACK_T1 | `SEMANTIC_ANCHORING_PACK_T1` | `t1-pre-freeze-library-2025-11-28` | `historical_artifact` | [`registry/historical/t1-pre-freeze-library/index.yaml`](../registry/historical/t1-pre-freeze-library/index.yaml) | historical_only |
| RECALL_TRIGGERS_T1 | `RECALL_TRIGGERS_T1` | `t1-pre-freeze-library-2025-11-28` | `historical_artifact` | [`registry/historical/t1-pre-freeze-library/index.yaml`](../registry/historical/t1-pre-freeze-library/index.yaml) | historical_only |
| HEARTBEAT_SNAPSHOTS_T1 | `HEARTBEAT_SNAPSHOTS_T1` | `t1-pre-freeze-library-2025-11-28` | `historical_artifact` | [`registry/historical/t1-pre-freeze-library/index.yaml`](../registry/historical/t1-pre-freeze-library/index.yaml) | historical_only |
| ANCHOR_TOKENS_SOFT_TAGS_T1 | `ANCHOR_TOKENS_SOFT_TAGS_T1` | `t1-pre-freeze-library-2025-11-28` | `historical_artifact` | [`registry/historical/t1-pre-freeze-library/index.yaml`](../registry/historical/t1-pre-freeze-library/index.yaml) | historical_only |
| RULE_VERSIONING_PIPELINE_T1 | `RULE_VERSIONING_PIPELINE_T1` | `t1-pre-freeze-library-2025-11-28` | `historical_artifact` | [`registry/historical/t1-pre-freeze-library/index.yaml`](../registry/historical/t1-pre-freeze-library/index.yaml) | historical_only |
| RULE_PROMOTION_DEV_TO_PROD_T1 | `RULE_PROMOTION_DEV_TO_PROD_T1` | `t1-pre-freeze-library-2025-11-28` | `historical_artifact` | [`registry/historical/t1-pre-freeze-library/index.yaml`](../registry/historical/t1-pre-freeze-library/index.yaml) | historical_only |
| BEHAVIOR_PROFILE_SELECTOR_T1 | `BEHAVIOR_PROFILE_SELECTOR_T1` | `t1-pre-freeze-library-2025-11-28` | `historical_artifact` | [`registry/historical/t1-pre-freeze-library/index.yaml`](../registry/historical/t1-pre-freeze-library/index.yaml) | historical_only |
| RULE_STATUS_FLAGS_T1 | `RULE_STATUS_FLAGS_T1` | `t1-pre-freeze-library-2025-11-28` | `historical_artifact` | [`registry/historical/t1-pre-freeze-library/index.yaml`](../registry/historical/t1-pre-freeze-library/index.yaml) | historical_only |
| RULEPACK_COMPATIBILITY_MATRIX_T1 | `RULEPACK_COMPATIBILITY_MATRIX_T1` | `t1-pre-freeze-library-2025-11-28` | `historical_artifact` | [`registry/historical/t1-pre-freeze-library/index.yaml`](../registry/historical/t1-pre-freeze-library/index.yaml) | historical_only |
| CONFIG_OVERRIDE_GOVERNOR_T1 | `CONFIG_OVERRIDE_GOVERNOR_T1` | `t1-pre-freeze-library-2025-11-28` | `historical_artifact` | [`registry/historical/t1-pre-freeze-library/index.yaml`](../registry/historical/t1-pre-freeze-library/index.yaml) | historical_only |
| SCENARIO_PACK_REGRESSION_T1 | `SCENARIO_PACK_REGRESSION_T1` | `t1-pre-freeze-library-2025-11-28` | `historical_artifact` | [`registry/historical/t1-pre-freeze-library/index.yaml`](../registry/historical/t1-pre-freeze-library/index.yaml) | historical_only |
| EXPLAINABILITY_SNAPSHOT_T1 | `EXPLAINABILITY_SNAPSHOT_T1` | `t1-pre-freeze-library-2025-11-28` | `historical_artifact` | [`registry/historical/t1-pre-freeze-library/index.yaml`](../registry/historical/t1-pre-freeze-library/index.yaml) | historical_only |
| HEALTH_SNAPSHOT_ENGINE_T1 | `HEALTH_SNAPSHOT_ENGINE_T1` | `t1-pre-freeze-library-2025-11-28` | `historical_artifact` | [`registry/historical/t1-pre-freeze-library/index.yaml`](../registry/historical/t1-pre-freeze-library/index.yaml) | historical_only |
| High-Coherence State Induction | `T2-038` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/frozen-t2-resonance/index.yaml`](../registry/historical/frozen-t2-resonance/index.yaml) | historical_only |
| Resonance Warm-Ups | `T2-039` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/frozen-t2-resonance/index.yaml`](../registry/historical/frozen-t2-resonance/index.yaml) | historical_only |
| Attention Corridor Narrowing | `T2-040` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/frozen-t2-resonance/index.yaml`](../registry/historical/frozen-t2-resonance/index.yaml) | historical_only |
| Anchor-Chain Reinforcement | `T2-041` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/frozen-t2-resonance/index.yaml`](../registry/historical/frozen-t2-resonance/index.yaml) | historical_only |
| Resonance Plateau Detection | `T2-042` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/frozen-t2-resonance/index.yaml`](../registry/historical/frozen-t2-resonance/index.yaml) | historical_only |
| Stability Guardrails | `T2-043` | `frozen-t2-master-2025-11-28` | `exact_recovery` | [`registry/historical/frozen-t2-resonance/index.yaml`](../registry/historical/frozen-t2-resonance/index.yaml) | historical_only |
| Mode Declaration Engine | `T2-061` | `frozen-t2-master-2025-11-28` | `historical_artifact` | [`registry/historical/frozen-t2-supervisor-provisional/index.yaml`](../registry/historical/frozen-t2-supervisor-provisional/index.yaml) | historical_only |
| Pack Routing Engine | `T2-062` | `frozen-t2-master-2025-11-28` | `historical_artifact` | [`registry/historical/frozen-t2-supervisor-provisional/index.yaml`](../registry/historical/frozen-t2-supervisor-provisional/index.yaml) | historical_only |
| Pack Conflict Resolver | `T2-063` | `frozen-t2-master-2025-11-28` | `historical_artifact` | [`registry/historical/frozen-t2-supervisor-provisional/index.yaml`](../registry/historical/frozen-t2-supervisor-provisional/index.yaml) | historical_only |
| Pack Health Check Engine | `T2-064` | `frozen-t2-master-2025-11-28` | `historical_artifact` | [`registry/historical/frozen-t2-supervisor-provisional/index.yaml`](../registry/historical/frozen-t2-supervisor-provisional/index.yaml) | historical_only |
| Reasoning Pipeline Orchestrator | `T2-065` | `frozen-t2-master-2025-11-28` | `historical_artifact` | [`registry/historical/frozen-t2-supervisor-provisional/index.yaml`](../registry/historical/frozen-t2-supervisor-provisional/index.yaml) | historical_only |
| Pack Activation/Deactivation Manager | `T2-066` | `frozen-t2-master-2025-11-28` | `historical_artifact` | [`registry/historical/frozen-t2-supervisor-provisional/index.yaml`](../registry/historical/frozen-t2-supervisor-provisional/index.yaml) | historical_only |
| Mode Transition Stabilizer | `T2-067` | `frozen-t2-master-2025-11-28` | `historical_artifact` | [`registry/historical/frozen-t2-supervisor-provisional/index.yaml`](../registry/historical/frozen-t2-supervisor-provisional/index.yaml) | historical_only |
| OCG | not fully recovered | source-specific | `unresolved` | [`ocg`](../registry/unresolved/ocg.yaml) | unresolved |
| ECL / Drift Sink | not fully recovered | source-specific | `unresolved` | [`ecl-drift-sink`](../registry/unresolved/ecl-drift-sink.yaml) | unresolved |
| LROS | not fully recovered | source-specific | `unresolved` | [`lros`](../registry/unresolved/lros.yaml) | unresolved |
| Intent/Task Framing Controller (ITFC) | not fully recovered | source-specific | `unresolved` | [`intent-task-framing-controller`](../registry/unresolved/intent-task-framing-controller.yaml) | unresolved |
| Frozen T1-Core Bundle missing members | not fully recovered | source-specific | `unresolved` | [`frozen-t1-missing-members`](../registry/unresolved/frozen-t1-missing-members.yaml) | unresolved |
| Frozen T2-001..007 Neuro-Focus members | not fully recovered | source-specific | `unresolved` | [`frozen-t2-neuro-focus-members`](../registry/unresolved/frozen-t2-neuro-focus-members.yaml) | unresolved |
| Frozen T2-024..030 CRISPR members | not fully recovered | source-specific | `unresolved` | [`frozen-t2-crispr-members`](../registry/unresolved/frozen-t2-crispr-members.yaml) | unresolved |
| Frozen T2-044..046 Duration members | not fully recovered | source-specific | `unresolved` | [`frozen-t2-duration-members`](../registry/unresolved/frozen-t2-duration-members.yaml) | unresolved |
| Frozen T2-047..049 Energy members | not fully recovered | source-specific | `unresolved` | [`frozen-t2-energy-members`](../registry/unresolved/frozen-t2-energy-members.yaml) | unresolved |
| Frozen T2-050..052 Immune members | not fully recovered | source-specific | `unresolved` | [`frozen-t2-immune-members`](../registry/unresolved/frozen-t2-immune-members.yaml) | unresolved |
| Frozen T2-053..056 Interpersonal/Tone members | not fully recovered | source-specific | `unresolved` | [`frozen-t2-tone-members`](../registry/unresolved/frozen-t2-tone-members.yaml) | unresolved |
| Frozen T2-057..060 Consciousness Layer members | not fully recovered | source-specific | `unresolved` | [`frozen-t2-consciousness-members`](../registry/unresolved/frozen-t2-consciousness-members.yaml) | unresolved |
| Nano reasoning-scale details | not fully recovered | source-specific | `unresolved` | [`reasoning-scale-nano-details`](../registry/unresolved/reasoning-scale-nano-details.yaml) | unresolved |
| Bounded ExIt acronym expansion | not fully recovered | source-specific | `unresolved` | [`bounded-exit-acronym`](../registry/unresolved/bounded-exit-acronym.yaml) | unresolved |
