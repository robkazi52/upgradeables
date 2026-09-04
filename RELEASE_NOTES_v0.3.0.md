# Upgradeables v0.3.0 — Project Harness and Skill Factory

This release adds a local-first project harness that lets people and agents use
the Upgradeables library without loading the full registry into every task.

## What changed

- Installable `upgradeables` CLI with no third-party runtime dependencies.
- Shallow, non-executing project inspection and ten deterministic project profiles.
- Natural-language task resolution using task archetypes, failure modes,
  environment modifiers, recipe roles, and a complexity ceiling.
- Project-local `.upgradeables/` maps, configuration, exact version locks, and
  concise agent fragments for Codex, Claude Code, Copilot, and generic agents.
- Explicit, idempotent managed-block integration that preserves host instructions.
- Project Skill briefs, scaffolds, maps, draft/final validation, opt-in task
  history, and conservative recurring-workflow suggestions.
- `doctor`, reproducible packaged registry data, stable JSON schemas, examples,
  and clean-install CI on Python 3.11 and 3.12.

## Research-first selection layer

- 8/8 research tracks completed from 61 unique source URLs.
- 15 task archetypes, 36 failure modes, 37 environment/capability signals, six
  complexity levels, and 17 composition-prior rules.
- 96/96 operational Upgradeables reviewed and mapped; none missing or unreviewed.
- Independent synthesis review: `RESEARCH_GATE = PASS`.

These mappings are candidate-selection priors. They do not automatically activate
components or claim that the components improve every model or task.

## Validation

- 112 deterministic unit and integration tests passed.
- 96 semantic packages and 576 behavior cases passed existing validation.
- 1,189 internal links passed.
- Wheel and source distribution built successfully.
- GitHub package/install jobs passed on Python 3.11 and 3.12.
- A GitHub-installed release-candidate smoke test passed project inspection,
  repeat initialization, task resolution, managed integration, Skill creation,
  validation, and `doctor`.

## Install

After this release is published:

```bash
pipx install git+https://github.com/robkazi52/upgradeables.git@v0.3.0
```

Then, inside a project:

```bash
upgradeables init
upgradeables integrate codex --write
upgradeables task "review this pull request for regressions"
```

The harness creates selection aids; it does not permanently enable every
recommended Upgradeable.

## Compatibility and limitations

Canonical Upgradeable slugs, paths, and package versions remain unchanged. The
bundled operational registry is v0.2.1, while the harness is v0.3.0.

There is no PyPI publication, hidden model call, telemetry, hidden memory, MCP
server, IDE plugin, or automatic registry-update application in this release.
Those are separate future decisions rather than incomplete background behavior.

## Release assets

- `upgradeables_registry-0.3.0-py3-none-any.whl`
- `upgradeables_registry-0.3.0.tar.gz`
- `ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md`
- `registry.json`
- `registry.yaml`
- `upgradeable_task_priors.json`
- `SELECTION_ONTOLOGY_REVIEW_v0.3.md`
- `SHA256SUMS_v0.3.0.txt`
