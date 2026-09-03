# Model Consumption Guide

[START_HERE.md](START_HERE.md) is the universal router. Use this deeper guide
when selecting components, building a reusable Skill, or adapting the registry
to a host platform.

## Choose the operating mode

- **Task mode:** select and apply components, then deliver the user's requested
  result. Do not stop at architecture commentary.
- **Skill-building mode:** return a complete task-oriented Skill package,
  selection rationale, host notes, and tests.
- **Contribution mode:** preserve registry contracts and use the separate Skill
  or Upgradeable workflow in [CONTRIBUTING.md](CONTRIBUTING.md).

## Efficient discovery

Prefer the smallest useful source:

1. Search [`registry/catalog.json`](registry/catalog.json) or run
   `python scripts/query_registry.py --search <term>`.
2. Select a task-family seed from [`recipes/`](recipes/) or run
   `python scripts/query_registry.py --recipe <slug>`.
3. Open only the selected package files and their required dependencies.
4. Use the full [`registry/registry.json`](registry/registry.json) for complete
   machine metadata. Use the
   [all-in-one kit](dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md) only when granular
   repository access is unavailable.

Do not load `archive/` for normal task execution. Archived files are provenance,
not current operating instructions.

Before activation, inspect `os_role`, `pipeline_stages`, `best_fit_tasks`,
`avoid_when`, `mechanism_basis`, counterbalances, and potential redundancy. Do
not activate an Upgradeable solely because its name seems relevant; confirm its
trigger, OS placement, task fit, and exclusion conditions. When a mechanism basis
is `modern-interpretation` or `provisional`, do not present that implementation
as the recovered historical definition.

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
   [precedence rules](spec/PRECEDENCE_SPEC.md).
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

Use [the Skill template](templates/SKILL_IMPLEMENTATION_TEMPLATE.md). Return:

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

See the complete [worked research Skill](implementations/community/source-bounded-research/SKILL.md),
including its keep/drop table and tests.

## Preliminary empirical design signal

An author-reported ARC session compared code-shaped prompt architectures with
shorter directives targeting concrete failures. In its supplied ARC-AGI-2 table,
the directive-oriented v5+ condition matched or exceeded the elaborate v4
condition on three of five tasks. The sample is small, raw runs are not archived,
and other supplied totals are unreconciled, so treat this as a design hypothesis—not
as proof that one prompt style or Upgradeable composition is universally superior.

Prefer the minimum control that targets an observed failure:

1. Name the concrete execution error that must be prevented.
2. Require falsification before commitment when premature selection is the risk.
3. Add stepwise construction checks when the model knows the rule but may apply it
   incorrectly.

Do not prescribe hidden reasoning steps or simulate an operating system when a
short directive preserves the needed invariant. See the
[ARC evidence report](evidence/arc-agi-benchmarks.md) for supplied figures,
discrepancies, and reproduction gaps.

## Non-negotiable boundaries

Never merge Skills, Behavior Genes, Cores, validators, and Upgradeables into one
undifferentiated prompt type. Never infer unresolved definitions. Treat
historical IDs as scoped to their generation. Translate metaphors into visible
mechanisms. Host policy always wins, and an adapter cannot redefine the registry.
