# Project Skill Factory

The project Skill factory turns a recurring, project-specific job into a small,
reviewable `SKILL.md`. It uses the bundled `0.2.1` registry and the local project
profile. It does not call a model, browse the web, activate every suggested
component, or invent project-domain rules.

## Workflow

Initialize the standard harness, ask for a brief, and then scaffold a draft:

```bash
upgradeables init
upgradeables skill brief "review dependency updates for API compatibility"
upgradeables skill scaffold dependency-api-review \
  --task "review dependency updates for API compatibility"
upgradeables skill validate --draft \
  .upgradeables/skills/dependency-api-review/SKILL.md
```

The brief is selection guidance. Before keeping a component, confirm its
canonical trigger, non-trigger, compatibility, authority boundary, and necessity
for this particular job. Remove components that do not clear that check.

The scaffold deliberately contains `TODO` markers. Complete its activation and
non-activation boundaries, inputs, procedure, output contract, failure behavior,
and behavioral cases before final validation:

```bash
upgradeables skill validate \
  .upgradeables/skills/dependency-api-review/SKILL.md
upgradeables skill list
```

Draft validation accepts explicit placeholders and reports them as warnings.
Final validation rejects placeholders, unknown or unpinned Upgradeables, missing
behavioral cases, and incomplete boundaries. The repository-wide community Skill
validator remains available separately as `python scripts/validate_skill.py`.

## Project-local layout

```text
.upgradeables/
  project.json
  config.json
  skill-map.json
  skills/
    dependency-api-review/
      SKILL.md
      references/
      scripts/
      assets/
      tests/cases.json
```

`skill-map.json` records only project-local Skill identity, status, primary
recipe, and pinned components. A project Skill may refer to maintained local
contracts and conventions; a global community Skill should remain portable and
must not assume those project details.

## Optional repetition analysis

Task history is off by default. It is written only when
`record_task_events` is explicitly enabled in `.upgradeables/config.json` or the
caller explicitly requests recording. Events contain task metadata and outcomes,
not private chain-of-thought.

```bash
upgradeables task "review this API change" --record
upgradeables skill suggest
```

`skill suggest` performs deterministic workflow repetition analysis. It requires
repeated comparable events plus stable activation, input, procedure, and output
contracts. It never creates a Skill; it only proposes a next scaffold command.

## Machine-readable output

`skill brief`, `skill scaffold`, `skill list`, `skill validate`, and
`skill suggest` support `--json`. Their schemas live in `spec/harness/`.

See the synthetic [Python project example](../examples/harness/python-project/)
for a final project-local API compatibility review Skill.
