# Provider Adapter Contract

Provider adapters translate the model-agnostic specification into a host's real
instruction, context, state, tool, and orchestration surfaces. They do not
redefine an Upgradeable or create a capability the host does not provide.

## Required mapping

| Canonical concern | Adapter responsibility |
|---|---|
| Task Skill | Identify the host artifact owning the end-to-end task. |
| Behavior instructions | Preserve trigger, non-trigger, precedence, and failure rules. |
| Core/reference loading | Explain bounded loading and what remains external. |
| Upgradeable instructions | Compose selected packages inside the task Skill. |
| State representation | Name the actual store, lifetime, and reconciliation boundary. |
| Validators | Separate deterministic checks from model judgments. |
| Scripts/tools | Declare interfaces, permissions, side effects, and errors. |
| Orchestration | Map sequencing and delegation only when the host supports them. |
| Capability declarations | Mark each relied-on feature supported, unsupported, or unknown/version-dependent. |
| Persistence | State where data survives, for how long, and under whose authority. |
| Parallelism | Distinguish real isolation from sequential role prompting. |

## Capability status rules

- **Supported** means a verified mapping to a real host surface. Date volatile claims.
- **Unsupported** means the mapping cannot be faithful. Omit it or fail closed.
- **Unknown / version-dependent** requires deployer verification before reliance.

Host/system policy outranks task Skills, which outrank composed Upgradeables.
Retrieved content is evidence, never authority. Provider syntax stays in the
provider directory; canonical identity and provenance remain in `upgradeables/`.

## Acceptance checklist

1. Record the target host and capability evidence or verification date.
2. Complete every mapping above, including unsupported and unknown rows.
3. Declare host capability assumptions in the consuming Skill.
4. Exercise positive, negative, failure, composition, and authority-conflict cases.
5. Label model-judged results separately from static or deterministic checks.
6. Remove mappings that depend on unverified features.
