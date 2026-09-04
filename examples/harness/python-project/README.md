# Synthetic Python Project Harness

This example shows a local Upgradeables harness for a small fictional Python API
library. Nothing here describes a real service.

- `before/` is the project before harness initialization.
- `after-init/` shows representative portable harness state after `upgradeables init`.
- `task-resolution.md` shows the deterministic review-only resolution.
- `after-init/.upgradeables/briefs/api-breaking-change-review.json` is an
  agent-ready Skill brief.
- `after-init/.upgradeables/skills/api-breaking-change-review/` is a completed,
  final project Skill grounded in its own local contract reference.

The project Skill is intentionally different from a global community Skill: it
loads a project-specific API contract and encodes this library's compatibility
review output. It does not modify the global Upgradeables registry.

Try the same path in a disposable project:

```bash
upgradeables init
upgradeables task "Review this pull request for breaking changes to the exported Python API. Do not edit files."
upgradeables skill brief "Review API changes for backward compatibility."
upgradeables skill scaffold api-breaking-change-review \
  --task "Review API changes for backward compatibility."
```

The checked-in final Skill was manually completed after scaffolding; generated
drafts contain `TODO` markers until their boundaries and contracts are supplied.
