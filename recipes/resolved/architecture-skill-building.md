# Architecture / Skill Building — Resolved Recipe

Generated discovery view. For normal execution, load the compact
[runtime recipe pack](../../runtime/recipes/architecture-skill-building.md) instead of full packages.
See the [source recipe notes](../architecture-skill-building.md) for composition and tests.

`R` stays required after selecting this recipe. `A`, `C`, and `O` require an
active trigger. `X` is excluded without explicit justification.

| Role | Component | Trigger summary | Requires |
|:---:|---|---|---|
| R | [Modular System Design Orchestrator (`architect-orchestrator@1.1.0`)](../../upgradeables/orchestration/architect-orchestrator/UPGRADEABLE.md) | designing or refactoring a Skill, OS, framework, or workflow | — |
| A | [Deep Exploration Mode (`power-mode@1.1.0`)](../../upgradeables/meta-control/power-mode/UPGRADEABLE.md) | architecture or design benefits from broad exploration | — |
| A | [Explore-Then-Commit Mode (`hybrid-mode@1.1.0`)](../../upgradeables/meta-control/hybrid-mode/UPGRADEABLE.md) | work includes both broad design and grounded execution | — |
| A | [Task-Scope Reasoning Controller (`reasoning-scale-controller@1.1.0`)](../../upgradeables/reasoning/reasoning-scale-controller/UPGRADEABLE.md) | task complexity or risk requires depth selection | — |
| A | [Bounded Alternative Search (`multiverse-reasoning@1.1.0`)](../../upgradeables/reasoning/multiverse-reasoning/UPGRADEABLE.md) | competing hypotheses or designs would add value | — |
| C | [Reusable Behavior Component Builder (`behavior-gene-builder@1.1.0`)](../../upgradeables/meta-control/behavior-gene-builder/UPGRADEABLE.md) | a recurring task family needs reusable behavior | — |
| C | [Shared Domain Knowledge Component Builder (`domain-core-builder@1.1.0`)](../../upgradeables/meta-control/domain-core-builder/UPGRADEABLE.md) | a recurring domain needs structured knowledge and decision logic | — |
| R | [Scoped Loader / Loader Sequencing (`scoped-loader@1.1.0`)](../../upgradeables/context-retrieval/scoped-loader/UPGRADEABLE.md) | a modular workflow has multiple available components | — |
| R | [Canonical Task State (`stateblock@1.1.0`)](../../upgradeables/state/stateblock/UPGRADEABLE.md) | work spans multiple steps or components | — |
| R | [Parallel Validation System (`parallel-qms@1.1.0`)](../../upgradeables/validation/parallel-qms/UPGRADEABLE.md) | a composed workflow needs structured quality evaluation | — |
| A | [Workflow Repair Supervisor (`meta-supervisor@1.1.0`)](../../upgradeables/meta-control/meta-supervisor/UPGRADEABLE.md) | complex scaffolding itself needs supervision | — |
| A | [Adapter-First Experimentation (`adapter-first-experimentation@1.1.0`)](../../upgradeables/meta-control/adapter-first-experimentation/UPGRADEABLE.md) | a new capability may destabilize a base workflow | — |
| A | [Precision Local System Edit (`crispr-edit@1.1.0`)](../../upgradeables/editing-repair/crispr-edit/UPGRADEABLE.md) | a change is small and local | — |
| C | [Structural System Edit (`surgery-edit@1.1.0`)](../../upgradeables/editing-repair/surgery-edit/UPGRADEABLE.md) | layers, Cores, or workflows require major replacement | — |
| A | [Per-Region Reasoning Depth (`dynamic-depth-allocation@1.1.0`)](../../upgradeables/meta-control/dynamic-depth-allocation/UPGRADEABLE.md) | task regions vary in difficulty or risk | — |
| A | [Anti-Tunnel Vision (`anti-tunnel-vision@1.1.0`)](../../upgradeables/reasoning/anti-tunnel-vision/UPGRADEABLE.md) | premature fixation could hide credible alternatives | — |
| A | [State Snapshot (`state-snapshot@1.1.0`)](../../upgradeables/state/state-snapshot/UPGRADEABLE.md) | a workflow pauses, hands off, or persists | — |
| A | [Runtime Compatibility Mode Selector (`future-proof-mode-selector@1.1.0`)](../../upgradeables/meta-control/future-proof-mode-selector/UPGRADEABLE.md) | an implementation targets models with different capabilities | — |

Do not merge whole recipes. Add individual cross-cutting components only for
explicit requirements the primary recipe does not cover.
