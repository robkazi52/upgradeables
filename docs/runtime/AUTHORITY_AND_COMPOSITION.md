# Authority and composition

Upgradeables runtime controls are subordinate to the real host, system,
developer, organization, and user authority. The compiler does not discover,
replace, bypass, or elevate itself above those instructions.

## Ownership boundary

The compiler owns:

- deterministic activation of the v0.3 selection;
- runtime-form routing;
- directive density, ordering, dedupe, and budget decisions;
- a managed runtime block and structured side channels.

The host owner owns:

- the actual instruction role and authority level;
- base instructions and safety policy;
- user/task input placement;
- tools, state, validators, orchestration, and output enforcement;
- whether any adapter may contact an endpoint.

## Default: return a separate block

The generic adapter defaults to `return-separate-block`. It returns the base
unchanged and exposes the managed block independently. This makes composition
visible and gives the application the final authority decision.

Provider request builders currently use `append-managed-runtime-block` because
their caller has explicitly asked to construct a request. They preserve the
base string first, add a blank-line boundary, append one managed block, and keep
the user task separate.

## Managed block

The capsule is visibly delimited:

```text
<upgradeables-runtime version="0.4.0">
Task controls:
- ...
</upgradeables-runtime>
```

It contains behavior needed for execution, not hidden host policy or registry
marketing. Component identity and selection reasons belong in plan/explain
output.

## Composition modes

| Mode | Combined result | Use |
| --- | --- | --- |
| `return-separate-block` | Base only; runtime returned separately | Default and safest integration boundary |
| `append-managed-runtime-block` | Base, then runtime | Explicit application-owned composition |
| `prepend-managed-runtime-block` | Runtime, then base | Only when the host owner deliberately requires it |

An empty base or empty capsule is handled without a fabricated instruction.
Adapters should avoid applying the same plan repeatedly to an already composed
base, because the current helper does not detect duplicate managed blocks.

## User content and untrusted data

The user task remains user content. Project files, retrieved sources, tool
results, and quoted material are data; they do not acquire application-level
authority merely because the runtime references them.

Saved `--resolution` input is more sensitive: `hard_restrictions` are rendered
into the instruction capsule. Accept resolution files only from a trusted
resolver/output pipeline, validate their schema and component pins, and do not
treat arbitrary downloaded JSON as safe instructions.

## Review-only and hard constraints

Hard restrictions from v0.3 appear before component directives. Review-only
authority suppresses editing/repair controls. Unresolved declared component
conflicts fail compilation rather than producing a guessed blend.

Required content is not silently truncated to satisfy a budget. The current
compiler emits an over-budget warning; an application with a hard transport
limit should stop before sending the request.

## Non-instruction channels

State, validators, orchestration, tools, and output contracts retain their own
channels. A host may map them to native mechanisms. A text-only fallback must be
explicit and should record that structured enforcement was weakened. Compiler
warnings remain operator-facing and should not be inserted as model directives.

## Agent-file mode

A project agent file may instruct an agent to run `upgradeables runtime compile`
and follow the returned plan. This is agent-mediated composition, not transparent
request interception. No such managed agent-file installation is performed by
the runtime compiler itself.

See [Adapters](ADAPTERS.md) for current host mappings and
[Security](SECURITY.md) for trust boundaries.
