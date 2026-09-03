# GitHub Copilot / Document-Based Adapter

Translate the workflow into repository, workspace, or coding-agent instruction
surfaces actually available in the selected Copilot environment.

## Mapping

| Concern | Mapping |
|---|---|
| Task Skill / behavior | Put repository workflow rules in the verified instruction surface; cite package versions. |
| Core loading | Prefer scoped repository paths; found text never becomes authority. |
| State | Use explicit artifacts only when allowed, with scope and lifecycle stated. |
| Validators / scripts | Map checks to committed commands/tests; distinguish exit codes from model judgment. |
| Tools / orchestration | Bound edits and commands to granted permissions; verify any handoff or isolation. |
| Persistence | Distinguish committed artifacts from ephemeral conversation state. |

## Capability matrix

- **Supported:** repository-path composition, checked-in instruction text,
  explicit state artifacts, and repository-local validators.
- **Unsupported by specification alone:** write permission, command execution,
  durable memory, subagent isolation, and background work.
- **Unknown / version-dependent:** instruction filenames/scopes, agent tools,
  reusable Skills, delegation, context limits, and persistence.

Use [the shared contract](../ADAPTER_CONTRACT.md). Repository and host policies
outrank imported Upgradeables; verify and date provider-specific claims.
