# Software engineering and coding-agent tasks

Research track B for the v0.3 selection ontology. Sources were reviewed on
2026-09-03.

## Scope and evidence labels

This note covers repository understanding, implementation, repair, review,
testing, refactoring, migration, dependency changes, architecture, and
issue-to-patch workflows.

- **Evidence** is directly supported by a linked benchmark paper or official
  provider/platform document.
- **Synthesis** is a proposed Upgradeables ontology or resolver rule. It should
  not be read as an empirical performance claim about an Upgradeable.
- Coding benchmarks sample particular workflows. They do not constitute a full
  software-engineering taxonomy or prove production readiness.

## Source-grounded findings

### Repository work is more than code generation

**Evidence.** SWE-bench frames issue resolution as receiving a repository and
issue description, then producing a patch. Its tasks often require coordinating
changes across functions, classes, and files, interacting with an execution
environment, and managing long context. [B1]

**Evidence.** RepoBench separates repository-level work into retrieval of
cross-file context, code completion using that context, and an end-to-end
retrieval-plus-completion pipeline. [B2]

**Synthesis.** `repository-understanding` and `change-execution` should be
distinct archetypes or phases. A task may request explanation, localization, or
impact analysis without authorizing a patch.

### Issue quality and the test oracle materially affect solvability

**Evidence.** OpenAI's SWE-bench Verified review screened tasks for
underspecified issue descriptions and tests that reject valid solutions. The
resulting subset was human-validated for scope and test fitness. [B3]

**Evidence.** OpenAI later reported that SWE-bench Verified no longer provided a
clean frontier signal because of benchmark contamination and flawed tasks. This
does not erase the issue-to-patch workflow; it shows that task specification and
evaluation quality are separate variables from model ability. [B4]

**Synthesis.** The resolver should detect `underspecified_task` and
`weak_oracle`. Passing available tests is evidence, not proof that the requested
behavior and invariants are satisfied. When requirements and tests conflict,
the system should expose the conflict rather than silently optimize for one.

### Effective coding loops separate exploration, planning, editing, and verification

**Evidence.** Anthropic documents an “explore, plan, code, commit” pattern and a
test-driven loop that first establishes failing tests, then implements and
iterates until tests pass. It warns that skipping exploration and planning can
cause premature coding. [B5]

**Evidence.** The SWE-agent paper describes recurring higher-order operations
such as reproducing an issue, localizing faulty code, proposing edits, and
verifying the result. [B6]

**Synthesis.** These are pipeline stages shared by several coding archetypes,
not a single mandatory recipe. A trivial explicit edit may skip diagnosis;
review-only work must stop before mutation; an unreproduced bug may still permit
a narrowly justified fix, but the uncertainty must remain visible.

### Good delegated tasks are bounded and testable

**Evidence.** GitHub recommends giving coding agents a clear problem, acceptance
criteria, and change scope. It names bugs, UI changes, test coverage,
documentation, accessibility, and technical debt as reasonable starting tasks,
while flagging broad refactors, deep legacy/domain dependencies, sensitive
production work, and ambiguous requirements as poor candidates for lightly
supervised delegation. [B7]

**Synthesis.** Scope clarity, acceptance criteria, domain dependence, and
criticality should influence complexity and escalation. They should not be
encoded only as keywords in recipe ranking.

### Code review is a separate, normally read-only task

**Evidence.** GitHub describes code review as identifying issues and suggesting
fixes, but states that automated review can miss defects or produce false
positives and should be supplemented with human review. It also distinguishes
review from applying a suggested change. [B8] [B9]

**Synthesis.** `code-review` must set `review_only=true` unless remediation is
explicitly requested. Findings should be grounded in changed lines plus relevant
repository context, ranked by impact, and kept separate from edits.

### Context and environment are part of the task

**Evidence.** Anthropic recommends repository-local instructions for build and
test commands, important files, style, and repository conventions. GitHub also
recommends repository custom instructions and notes that large or complex
changes are harder for automated review. [B5] [B8]

**Evidence.** GitHub's cloud-agent security design constrains branch writes,
credentials, and who can invoke an agent, and requires human review before
merge. [B10]

**Synthesis.** The same textual request can require different priors depending
on tests, build tools, repository instructions, branch permissions, context
size, and risk. Capability and permission must remain separate fields.

## Proposed normalized software task archetypes

All entries below are **synthesis**.

| Archetype | Goal | Typical output | Important boundary |
|---|---|---|---|
| `repository-understanding` | Explain structure, behavior, ownership, or dependencies | grounded explanation, map, impact trace | Read-only; no patch implied |
| `code-localization` | Identify code relevant to a symptom or requested change | candidate files/symbols and evidence | Does not claim root cause by itself |
| `bug-diagnosis` | Reproduce and explain a defect's cause | reproduction status, causal account, affected scope | Diagnosis does not authorize repair |
| `localized-repair` | Fix a bounded defect with minimal collateral change | patch plus validation | Preserve unrelated behavior and scope |
| `feature-implementation` | Add specified behavior | implementation, tests, documentation as required | Needs acceptance criteria; avoid incidental redesign |
| `test-engineering` | Add, repair, or assess automated tests | tests, fixtures, coverage rationale | Tests must target behavior rather than mirror implementation |
| `code-review` | Find defects/regressions in a diff or PR | prioritized findings with locations and rationale | Read-only unless remediation is requested |
| `behavior-preserving-refactor` | Change internal structure without intended behavior change | refactor plus invariance evidence | Behavioral invariants are primary |
| `migration-compatibility-change` | Move versions, APIs, schemas, platforms, or frameworks | staged changes and compatibility evidence | Requires explicit old/new contract and rollback concerns |
| `dependency-change` | Add, remove, or update a dependency | manifest/lock changes, impact and verification | Network, supply-chain, license, and transitive effects matter |
| `documentation-maintenance` | Align developer/user documentation with software | bounded documentation change | Do not invent behavior absent from code/spec |
| `architecture-design` | Propose structural/system changes and trade-offs | decision record or design | No implementation authority by default |
| `issue-to-patch` | Execute the full issue workflow | reproduction/localization, patch, tests, summary | Composite agent workflow; not the default for every edit |
| `release-integration` | Prepare or validate a change for merging/release | CI status, release artifacts, handoff | External pushes/deployments need explicit authority |

### Necessary distinctions

- `bug-diagnosis` versus `localized-repair`: “find why” is not “change it.”
- `code-review` versus `localized-repair`: “suggest a fix” is not permission to
  apply it.
- `feature-implementation` versus `architecture-design`: implementation follows
  stated requirements; design establishes the structure or contracts.
- `behavior-preserving-refactor` versus feature work: refactoring has an
  explicit no-intended-behavior-change invariant.
- `migration-compatibility-change` versus dependency change: a dependency bump
  can be local, while migration emphasizes coordinated contract transition.
- `test-engineering` can be primary or supporting. Do not classify every task
  that needs validation as a test-authoring task.
- `issue-to-patch` is a composite execution form spanning understanding,
  localization, modification, and validation.

## Recurring failure patterns

The following are **synthesis categories** grounded in the observed task and
platform constraints above.

| Failure-mode candidate | Observable signals | Selection implication |
|---|---|---|
| `problem-misread` | Patch solves a nearby behavior, not the stated issue | Lock acceptance criteria and restate intended behavior |
| `underspecified-task` | Missing expected behavior, inputs, or completion criteria | Ask targeted questions or preserve alternatives |
| `context-mislocalization` | Agent reads or edits irrelevant files/symbols | Search relationships and cite localization evidence |
| `premature-edit` | Code changes begin before understanding/reproduction | Promote bounded exploration for non-trivial tasks |
| `surface-repair` | Symptom disappears but cause or adjacent paths remain | Verify causal path and related cases |
| `incomplete-change-coverage` | One file changes while dependent contracts remain stale | Trace callers, tests, docs, schemas, and configuration as applicable |
| `over-editing` | Unrelated cleanup/refactor increases diff and risk | Enforce minimal repair and protected scope |
| `under-editing` | Patch omits required coordinated changes | Verify impact surface without expanding to unrelated work |
| `test-overfitting` | Implementation passes narrow tests but violates general behavior | Add behavioral/edge invariants and independent checks |
| `test-oracle-mismatch` | Tests conflict with issue or reject valid behavior | Surface the mismatch; do not silently rewrite requirements |
| `regression-or-invariant-loss` | Existing behavior/API changes unintentionally | Run relevant regressions and explicit invariance checks |
| `environment-assumption` | Wrong build command, dependency, platform, or service assumed | Read project instructions and report unavailable prerequisites |
| `review-false-positive` | Finding lacks executable or code-grounded support | Require location, impact path, and confidence/evidence |
| `review-false-negative` | Diff-only review misses cross-file consequences | Load targeted surrounding contracts and tests |
| `authority-scope-violation` | Review task edits files or agent pushes/deploys without request | Treat read/write/push/deploy as separate permissions |
| `weak-verification` | “Fixed” asserted from syntax or one test alone | Match validation depth to change risk |
| `state-loss` | Long task forgets decisions, failures, or remaining work | Persist explicit task state and handoff artifacts |

## Environment modifiers

All entries are **synthesis recommendations**.

| Modifier | Resolver effect |
|---|---|
| `review_only` | Hard-exclude editing, commit, push, and remediation components |
| `editing_requested` | Permit repository mutation within named scope |
| `tests_available` | Promote executable validation; do not assume the test oracle is complete |
| `reproduction_available` | Promote diagnosis/reproduction before repair |
| `acceptance_criteria_present` | Raise implementation confidence and provide completion checks |
| `large_repository` / `long_context` | Promote scoped retrieval and explicit state, not whole-repo ingestion |
| `multi_file_contract` | Promote impact tracing and coordinated validation |
| `repository_instructions_present` | Load build/test/style commands before acting |
| `shell_available` | Enables inspection/tests; does not imply writes or unsafe command authority |
| `network_available` | Enables dependency/docs retrieval; absence constrains installation and lookup |
| `dependency_change` | Promote manifest/lock consistency and transitive-impact checks |
| `public_api_or_schema` | Promote compatibility and migration validation |
| `security_sensitive` / `production_critical` | Raise review, human oversight, and fail-closed behavior |
| `visual_target` | Permit screenshot/render comparison for UI work |
| `ci_available` | Adds independent evidence but does not replace targeted local checks |
| `branch_write_allowed` | Permits bounded commits to an allowed branch only |
| `push_or_merge_requested` | Separately authorizes external state change; human review remains appropriate |
| `cross_repository` | Raise context and coordination complexity; avoid casual autonomous delegation |
| `domain_knowledge_required` | Lower automation confidence or request authoritative references |

## Complexity implications

This mapping is **synthesis**, informed by benchmark task structure and provider
guidance.

| Task shape | Default ceiling | Conditions that raise it | Controls that are normally excessive |
|---|---|---|---|
| Explicit one-line rename/format change | L0-L1 | Protected generated files or broad occurrences | Branching, orchestration, architecture review |
| Repository question/localization | L1-L2 | Cross-file call graph, unfamiliar large repository | Editing pipeline |
| Local reproducible bug fix | L1-L2 | Ambiguous cause, several dependent modules | Multi-agent work by default |
| Feature with clear acceptance criteria | L2-L3 | Cross-service/API/schema effects | Full orchestration for a local function |
| Test authoring | L1-L2 | Integration/e2e environment, flaky behavior | Architecture redesign |
| Code review | L1-L3 | Security, complex logic, cross-service changes | Mutation unless requested |
| Behavior-preserving refactor | L2-L3 | Large surface or weak regression suite | Feature ideation |
| Migration/dependency transition | L2-L4 | Multi-service rollout, external tooling, rollback | Broad creative branching after contracts are fixed |
| Long issue-to-patch loop | L3-L4 | Adaptive tool use, repeated execution, large context | L5 unless work is cleanly separable |
| Cross-repository program | L4-L5 | Independent workstreams and explicit synthesis | Unbounded parallel agents |

High stakes raises validation and approval requirements. It does not
automatically require more agents.

## Ontology recommendations for synthesis

1. Model coding work with both a primary archetype and phase state:
   `inspect -> localize -> reproduce/diagnose -> plan -> edit -> verify ->
   handoff`.
2. Permit phase skipping when structurally appropriate; do not burden a trivial
   exact edit with a diagnosis ritual.
3. Encode `review_only`, `editing_requested`, `commit_requested`,
   `push_requested`, and `deploy_requested` as separate authority flags.
4. Make task specification quality and test-oracle quality explicit failure
   signals.
5. Give explicit wording and acceptance criteria more weight than the project's
   general software profile.
6. Use repository context selectively: changed code, direct callers/callees,
   contracts, tests, and instructions before expanding further.
7. For repair, prioritize minimum sufficient change plus regression evidence;
   for refactor, prioritize behavior invariance; for review, prioritize grounded
   findings and non-mutation.
8. Treat code review findings as uncertain claims requiring location and impact
   support; neither silence nor fluent comments prove correctness.
9. Do not use a SWE-bench score as evidence that an agent can safely handle
   arbitrary repositories, domains, or production actions.
10. Promote a project Skill when a coding workflow recurs with stable project
    commands, boundaries, references, and output checks—not merely because a
    task category repeats.

## Suggested archetype-to-recipe priors

These are **design hypotheses for later synthesis and testing**, not final
activation rules.

| Archetype | Likely primary recipe | Important exclusions/conditions |
|---|---|---|
| `bug-diagnosis` | `coding-debugging` | Exclude editing when diagnosis-only |
| `localized-repair` | `coding-debugging` | Require explicit edit authority and preserve invariants |
| `code-review` | `code-review` | Editing remains conditional/off |
| `repository-understanding` | `long-context-source-fidelity` or minimal direct path | Prefer no heavy recipe for small scoped questions |
| `architecture-design` | `architecture-skill-building` | Implementation conditional on explicit request |
| `test-engineering` | `coding-debugging` or minimal controlled path | Avoid treating tests as complete specification |
| `behavior-preserving-refactor` | `coding-debugging` with stronger invariance priors | Feature expansion excluded |
| `migration-compatibility-change` | coding plus architecture candidate | Raise compatibility and rollback controls |
| `documentation-maintenance` | `writing-revision` | Ground claims in repository behavior |

## Sources

- **[B1]** Jimenez et al., [SWE-bench: Can Language Models Resolve Real-World GitHub Issues?](https://arxiv.org/abs/2310.06770), ICLR 2024.
- **[B2]** Liu, Xu, and McAuley, [RepoBench: Benchmarking Repository-Level Code Auto-Completion Systems](https://arxiv.org/abs/2306.03091), 2023.
- **[B3]** OpenAI, [Introducing SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/), updated 2025.
- **[B4]** OpenAI, [Why SWE-bench Verified no longer measures frontier coding capabilities](https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/), accessed 2026-09-03.
- **[B5]** Anthropic, [Claude Code: Best practices for agentic coding](https://www.anthropic.com/engineering/claude-code-best-practices), 2025.
- **[B6]** Yang et al., [SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering](https://arxiv.org/abs/2405.15793), NeurIPS 2024.
- **[B7]** GitHub Docs, [Best practices for using GitHub Copilot to work on tasks](https://docs.github.com/en/copilot/using-github-copilot/using-copilot-coding-agent-to-work-on-tasks/best-practices-for-using-copilot-to-work-on-tasks), accessed 2026-09-03.
- **[B8]** GitHub Docs, [About GitHub Copilot code review](https://docs.github.com/en/copilot/concepts/agents/code-review), accessed 2026-09-03.
- **[B9]** GitHub Docs, [Application card: GitHub Copilot Agents](https://docs.github.com/en/copilot/responsible-use/agents), accessed 2026-09-03.
- **[B10]** GitHub Docs, [Risks and mitigations for GitHub Copilot cloud agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/risks-and-mitigations), accessed 2026-09-03.

