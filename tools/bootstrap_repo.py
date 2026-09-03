"""Build the initial Upgradeables repository from curated recovery data.

Run once for repository seeding. Maintainers edit generated canonical files afterward;
normal ongoing builds use scripts/build_registry.py and scripts/build_all_in_one.py.
"""

from __future__ import annotations

import json
import re
import shutil
import textwrap
from pathlib import Path

from catalog_data import (
    CORES, DOMAIN_OS, ENTRIES, FUNCTIONAL_CLASSES, GENES, HISTORICAL_T1,
    HISTORICAL_T2, LEGACY_OS, PREFREEZE_T1, QMS_MODES, RESONANCE_T2,
    SUPERVISOR_T2, UNRESOLVED,
)

ROOT = Path(__file__).resolve().parents[1]
SOURCE_DOC = "OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md"
HISTORY_DOC = "OS_Upgradeables_Historical_Recovery_Inventory.md"
ADDENDUM_DOC = "OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md"
BUILD_SPEC_DOC = "UPGRADEABLES_GITHUB_REPO_HANDOFF_v2_DEEP_RECOVERY.md"


def clean(value: str) -> str:
    # Interpolated multiline fragments may start at column zero and defeat dedent.
    # Remove the static template's first-line indent from every line that has it,
    # leaving already-unindented interpolations untouched.
    lines = value.strip("\n").splitlines()
    first = next((line for line in lines if line.strip()), "")
    margin = len(first) - len(first.lstrip())
    prefix = " " * margin
    if margin:
        lines = [line[margin:] if line.startswith(prefix) else line for line in lines]
    return "\n".join(lines).strip() + "\n"


def write(relative: str, content: str) -> None:
    path = ROOT / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(clean(content), encoding="utf-8", newline="\n")


def write_json(relative: str, data: object) -> None:
    write(relative, json.dumps(data, indent=2, ensure_ascii=False, sort_keys=False))


def linkify_slug(slug: str) -> str:
    entry = next(item for item in ENTRIES if item["slug"] == slug)
    return f"[`{slug}`]({entry['package_path']})"


def build_entry_metadata() -> None:
    by_slug = {item["slug"]: item for item in ENTRIES}
    for item in ENTRIES:
        item["version"] = "1.0.0"
        item["registry_generation"] = "consolidated-2026-09" if not item["id"].startswith("JAN26") else "training-scaffolding-2026-01-05"
        historical_id_map = {
            "scoped-loader": ["O-02"],
            "regenerative-rewrite": ["A-10"],
        }
        item["historical_ids"] = historical_id_map.get(item["slug"], [])
        item["usually_not_needed_for"] = ["simple tasks where the trigger condition is absent"]
        item["non_triggers"] = ["the declared trigger is absent or the control would add no material value"]
        classes = set(item["functional_classes"])
        forms = set(item["implementation_forms"])
        if "validator" in forms:
            item["inputs"] = ["candidate output or claim", "applicable evidence, constraints, and invariants"]
            item["outputs"] = ["pass", "fail", "repair-required", "unverifiable"]
            item["failure_boundary"] = ["if the applicable condition cannot be checked, do not certify the candidate"]
        elif "state-schema" in forms or "state-manager" in forms:
            item["inputs"] = ["current explicit task state", "authorized state update or source event"]
            item["outputs"] = ["updated explicit state", "conflict or unavailable-persistence status"]
            item["failure_boundary"] = ["do not claim state was retained or persisted without a real host-visible mechanism"]
        elif "editing-repair" in classes:
            item["inputs"] = ["source artifact", "authorized change request", "protected facts and invariants"]
            item["outputs"] = ["bounded patch or revised artifact", "preservation and validation status"]
            item["failure_boundary"] = ["escalate the repair class or stop when protected invariants cannot be preserved"]
        elif "orchestrator" in forms:
            item["inputs"] = ["locked task state", "available component manifests and authority rules"]
            item["outputs"] = ["bounded activation or routing plan", "explicit component state and unresolved conflicts"]
            item["failure_boundary"] = ["do not activate unavailable components or silently resolve an authority conflict"]
        elif "context-retrieval" in classes:
            item["inputs"] = ["task-scoped query", "available source/module inventory"]
            item["outputs"] = ["bounded selected context with provenance", "missing-context status"]
            item["failure_boundary"] = ["do not present unavailable or unverified context as retrieved evidence"]
        else:
            item["inputs"] = ["locked task goal and constraints", "relevant source or workflow state"]
            item["outputs"] = ["bounded component result", "explicit uncertainty or failure status when applicable"]
        item["strong_model_scaling"] = {
            "may_skip": ["verbose intermediate scaffolding when the host model is reliable and the task is simple"],
            "keep_mandatory": ["truth, state, safety, and integrity invariants whenever the task still requires them"],
        }
        item.setdefault("failure_boundary", ["do not claim success when required evidence, state, host capability, or validation is unavailable"])
        item["conflicts"] = []
        item["provenance"] = {
            "source_document": SOURCE_DOC,
            "source_id": item["id"],
            "source_date": "2026-09-03",
            "source_kind": "current_consolidated_catalog",
            "canonicality": "canonical",
            "recovery_confidence": "high",
            "notes": item.pop("notes", ""),
        }
        if item["lifecycle_status"] == "stable" and item["tiers"][0] in {"A", "BG", "C", "T4"}:
            item["lifecycle_status"] = "candidate"
        if item["id"].startswith("JAN26"):
            item["recovery_status"] = "partial_recovery"
            item["provenance"].update({"source_document":HISTORY_DOC, "source_kind":"historical_recovery_inventory", "canonicality":"provisional", "recovery_confidence":"medium"})
            inference_note = "Exact name recovery; operational mechanism is a conservative modern interpretation."
            item["provenance"]["notes"] = " ".join(filter(None, [item["provenance"]["notes"], inference_note]))
        if item["slug"] == "cot-structured-state-block":
            item["provenance"].update({"source_document":HISTORY_DOC, "source_kind":"user_accepted", "canonicality":"accepted", "recovery_confidence":"high"})
        item["supersedes"] = []
        item["superseded_by"] = []
        item["package_path"] = f"upgradeables/{item['category']}/{item['slug']}/UPGRADEABLE.md"
        item["schema_version"] = "1.0.0"
        if item["recommended_skill_types"] == ["general-agent-workflow"]:
            inferred = {"general-agent-workflow"}
            classes = set(item["functional_classes"])
            if classes & {"truth-grounding", "validation"}:
                inferred.update({"research", "source-grounded-analysis", "high-stakes-reasoning"})
            if classes & {"editing-repair", "output"}:
                inferred.update({"authoring", "coding-debugging"})
            if classes & {"state", "context-retrieval", "persistence"}:
                inferred.add("long-context-corpus")
            if classes & {"orchestration", "meta-control"}:
                inferred.update({"architecture-skill-building", "multi-agent-orchestration"})
            item["recommended_skill_types"] = sorted(inferred)

        if item["slug"] == "citation-fidelity":
            item["inputs"] = ["claim", "citation", "supporting source passage"]
            item["outputs"] = ["pass", "fail", "repair-required", "unverifiable"]
            item["strong_model_scaling"] = {
                "may_skip": [],
                "keep_mandatory": ["a citation must actually support its attached claim"],
            }
            item["failure_boundary"] = ["if support cannot be verified, do not certify the citation"]
        elif item["slug"] == "grounding-no-invention":
            item["inputs"] = ["candidate factual claims", "supplied or verified evidence boundary"]
            item["outputs"] = ["supported claims", "labeled inference", "omitted/uncertain unsupported claims"]
            item["failure_boundary"] = ["when an essential claim lacks support, fail closed instead of filling the gap"]

    # Avoid dangling companion links while retaining only operational relationships.
    known = set(by_slug)
    for item in ENTRIES:
        for key in ("requires", "recommended_with", "counterbalances", "potentially_redundant_with", "conflicts"):
            item[key] = [slug for slug in item[key] if slug in known]


build_entry_metadata()


README = f"""
# Upgradeables

An open, model-agnostic registry of composable reasoning, state, validation,
retrieval, editing, orchestration, and behavioral primitives for building AI
Skills and agent workflows.

> Skills define jobs. Behavior Genes define how a system behaves for a class of
> tasks. Cores define domain reasoning and evidence knowledge. Upgradeables
> define reusable capabilities and controls. Validators enforce integrity.
> Orchestrators compose them. OS bundles create complete operating environments.

This is not a prompt library and does not claim guaranteed model improvement.
It is a specification, registry, and contribution system for turning reusable
architecture into explicit, auditable mechanisms.

## The short version

An **Upgradeable** is a reusable primitive with an activation boundary, inputs,
outputs, mechanism, failure boundary, compatibility rules, and tests. A **Skill**
is a task-oriented implementation package assembled from task identity, behavior,
knowledge, selected Upgradeables, state, validation, and an output contract.

```text
Host model / system policy
            |
       OS or Skill bundle
            |
         Task shell
     +------+------+------+
     |             |      |
Behavior Gene    Core  Upgradeables <-> Explicit state
     +-------------+------+
                   |
               Validators
                   |
                 Output
```

| Concept | Responsibility |
|---|---|
| OS | Compositional operating environment and authority layer |
| Skill | A task-oriented package that performs a job |
| Upgradeable | A reusable cross-cutting capability or control |
| Behavior Gene | A recurring behavior and reasoning pattern |
| Core | High-density domain reasoning, evidence, and reference material |
| Validator | Checks, scores, vetoes, or requests repair; never manufactures truth |
| Orchestrator | Selects, sequences, coordinates, and resolves module authority |

## Use the registry

- Browse [{len(ENTRIES)} operational packages](upgradeables/) by functional area.
- Query [`registry/registry.json`](registry/registry.json) from any JSON-capable tool.
- Use [`registry/registry.yaml`](registry/registry.yaml) where YAML is preferred. It
  is emitted as a JSON-compatible YAML subset so builds require only Python.
- Start from a [Skill recipe](recipes/) or a curated [bundle](bundles/).
- Give a frontier model the repository URL plus [`MODEL_CONSUMPTION_GUIDE.md`](MODEL_CONSUMPTION_GUIDE.md),
  or ingest the generated [all-in-one kit](dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md).

Example query:

```python
import json
from pathlib import Path

    registry = json.loads(Path("registry/registry.json").read_text(encoding="utf-8"))
    research = next(
        recipe["classifications"] for recipe in registry["recipes"]
        if recipe["slug"] == "research-skill"
    )
```

## Build a Skill

1. Choose the Skill archetype, task boundary, risk tier, evidence sensitivity, and
   state needs.
2. Select a Behavior Gene and Core only when the task needs them.
3. Load foundational and task-specific Upgradeables.
4. Add risk-appropriate validators and check dependencies, counterbalances,
   conflicts, and redundancy.
5. Remove unnecessary scaffolding, choose an implementation form for each
   component, and generate the target Skill package.
6. Add positive, negative, conflict, long-context, and composition tests.

The complete procedure is in [Skill Translation](spec/SKILL_TRANSLATION_SPEC.md).
Provider mappings are adapter layers under [`implementations/`](implementations/).

## Contribute

Community additions are welcome: new primitives, modes, recipes, bundles, tests,
and provider-specific Skill implementations. Before proposing a primitive, search
the registry and explain why existing composition is insufficient. Start with
[CONTRIBUTING.md](CONTRIBUTING.md) and the [proposal template](templates/UPGRADEABLE_PROPOSAL_TEMPLATE.md).

Historical names and IDs are never silently rewritten. The three canonical source
documents are preserved byte-for-byte in [`archive/source/`](archive/source/), and
the [source map](archive/SOURCE_TO_REGISTRY_MAP.md) records normalization decisions.
Unresolved concepts remain explicitly unresolved.

## Validate locally

Requires Python 3.11+ and no runtime dependencies:

```bash
python scripts/build_registry.py --check
python scripts/validate_registry.py
python -m unittest discover -s tests -v
python scripts/build_all_in_one.py --check
python scripts/check_links.py
```

To rebuild generated artifacts, omit `--check` from the build commands.

## Authority and safety

Upgradeables operate beneath host/system policy authority. They cannot provide
hidden memory, hidden channels, private chain-of-thought access, or safety bypasses.
Parallel and persistent behavior must correspond to real host capabilities.

Licensed under [Apache-2.0](LICENSE).
"""


def root_docs() -> None:
    write("README.md", README)
    write("MODEL_CONSUMPTION_GUIDE.md", """
    # Model Consumption Guide

    This is the execution entrypoint for an LLM or coding agent given the repository.
    Read `spec/SKILL_TRANSLATION_SPEC.md`, `spec/PRECEDENCE_SPEC.md`, and
    `registry/registry.json`; use `recipes/recipes.json` to select a task-family seed.

    ## Deterministic selection procedure

    1. Write the task identity, activation boundary, output contract, source boundary,
       risk, evidence sensitivity, and state/persistence needs.
    2. Select the closest recipe. Start with its R entries, evaluate A entries, include
       C/O only when their own triggers match, and normally exclude X.
    3. Select at most one primary Behavior Gene and the minimum authorized Core(s).
    4. Read each selected package's metadata. Resolve `requires`; consider
       `recommended_with`; explicitly assess counterbalances, conflicts, and potential
       redundancy. Preserve the precedence specification.
    5. Remove every component without an active trigger. Do not turn the recipe into an
       always-on stack.
    6. Choose an implementation form for each retained component: instructions, mode,
       validator, state schema/manager, reference, script, orchestrator, or bundle.
    7. Copy `templates/SKILL_IMPLEMENTATION_TEMPLATE.md` into the target Skill folder.
       Put deep content in `references/`, deterministic checks in `scripts/`, and only
       necessary output materials in `assets/`.
    8. Cite each selected slug and version. State unavailable host capabilities; never
       simulate hidden persistence, private reasoning, or parallel agents as real.
    9. Add positive, negative, conflict, unsupported-claim, long-context, composition,
       and strong-model-scaling tests as applicable. Run the repository validators.

    ## Worked selection

    For a source-grounded research Skill, read the `research-skill` recipe. Retain the
    required task lock, loader, StateBlock, and grounding controls. Citation Fidelity
    activates only when emitting cited claims. Multi-Truth Gating and Critical Atomic
    Verification scale with claim importance/risk. Neuro-Focus should be counterbalanced
    by Anti-Tunnel Vision when fixation is plausible. The worked output is at
    `implementations/community/source-bounded-research/SKILL.md`.

    ## Non-negotiable output contract

    Never merge Skills, Behavior Genes, Cores, validators, and Upgradeables into one
    prompt type. Never infer unresolved definitions. Treat historical IDs as scoped to
    their generation. Translate metaphors into visible mechanisms. A provider adapter
    may evolve but cannot redefine the canonical registry.
    """)
    write("AGENTS.md", """
    # Agent Guide

    Before editing, read `MODEL_CONSUMPTION_GUIDE.md`, the relevant file under `spec/`,
    and `registry/registry.json`. Preserve archived sources and registry generations.
    Prefer composition over duplicate primitives; unresolved concepts stay archival.
    Use `templates/SKILL_IMPLEMENTATION_TEMPLATE.md` for community Skills. After any
    change, run every validation command listed in `README.md`.
    """)
    write("llms.txt", """
    # Upgradeables model entrypoint
    README.md
    MODEL_CONSUMPTION_GUIDE.md
    spec/SKILL_TRANSLATION_SPEC.md
    spec/COMPOSITION_SPEC.md
    spec/PRECEDENCE_SPEC.md
    registry/registry.json
    recipes/recipes.json
    dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md
    # Never invent unresolved historical meanings. Host policy always wins.
    """)
    write(".gitignore", """
    __pycache__/
    *.py[cod]
    .pytest_cache/
    .coverage
    htmlcov/
    .venv/
    venv/
    .idea/
    .vscode/
    .DS_Store
    Thumbs.db
    *.tmp
    *.log
    """)
    write("CHANGELOG.md", """
    # Changelog

    All notable changes follow Keep a Changelog and Semantic Versioning.

    ## [0.1.0] - 2026-09-03

    ### Added

    - Initial model-agnostic specification and operational registry.
    - Historical archive, recovery ledger, and source-to-registry map.
    - Behavior Gene, Core, bundle, recipe, implementation, and domain OS layers.
    - Deterministic registry, validation, tests, CI, and all-in-one build.
    """)
    write("ROADMAP.md", """
    # Roadmap

    ## Near term

    1. Independent review of every source-to-registry mapping and historical alias.
    2. More executable behavioral/composition fixtures and evaluator adapters.
    3. Community-authored provider integrations and example Skill packages.

    ## Later

    - Evidence-backed evaluations without claiming universal model improvement.
    - Versioned migrations and signed release artifacts.
    - Provenance proposals for currently unresolved historical concepts.
    """)
    write("SECURITY.md", """
    # Security Policy

    Report vulnerabilities through GitHub's private vulnerability reporting feature
    when available. Do not open a public issue containing credentials, exploit
    details, private data, or a working safety bypass.

    In scope are code-execution flaws in repository scripts, schema/validator bugs
    that admit harmful configurations, path traversal, secret exposure, and unsafe
    implementation guidance. Conceptual disagreements belong in normal issues.

    Upgradeables operate beneath host/system policy authority. They are not a
    mechanism to override model-provider or application safety controls.
    """)
    write("GOVERNANCE.md", """
    # Governance

    Upgradeables uses lightweight maintainer-led governance. Anyone may propose a
    change; canonical registry changes require review. Review prioritizes explicit
    mechanisms, tests, source provenance, interoperability, and non-duplication.

    Stable IDs are never reassigned. Historical provenance cannot be silently
    rewritten, and unresolved history may be resolved only through evidence-backed
    proposals. Deprecation preserves discoverable lineage. Provider adapters evolve
    separately from the model-agnostic specification. Host safety always has higher
    authority.

    `core` status is rare and requires broad demonstrated utility. Maintainers may
    reject a new primitive when a mode, recipe, bundle, reference, or composition
    already expresses it. Project naming or trademark governance may be introduced
    separately if an ecosystem develops; this document creates no trademark policy.

    Contributors propose a slug but do not allocate a canonical ID. Maintainers assign
    the ID and registry generation when accepting a proposal, after collision and
    provenance review. Deprecation requires a retained record, reason, replacement or
    explicit lack of replacement, `superseded_by`/alias metadata, migration note, and
    a release-note entry. Emergency security fixes may merge before normal review but
    receive retrospective provenance and validation.
    """)
    write("CONTRIBUTING.md", """
    # Contributing

    Contributions may add primitives, modes, recipes, bundles, tests, documentation,
    or model/provider adapters. Search `registry/registry.json` first. A new primitive
    must name its closest prior art, explain the material difference, and show why
    composition is insufficient.

    1. Fork and branch from `main`.
    2. Copy the appropriate template from `templates/`.
    3. Add or update machine-readable metadata and provenance.
    4. Add positive, negative, conflict, and composition tests as applicable.
    5. Run every command in README's validation section.
    6. Open a pull request using the checklist.

    Do not invent missing history, reuse IDs, collapse acronym collisions, claim host
    capabilities that are not present, or let a validator add unsupported facts.
    By contributing, you agree that your contribution is licensed under Apache-2.0.
    """)
    write("CODE_OF_CONDUCT.md", """
    # Code of Conduct

    We pledge to make participation welcoming and harassment-free regardless of
    background, identity, experience, or viewpoint. Be respectful, accept
    constructive feedback, focus criticism on ideas and mechanisms, and protect
    private information. Harassment, threats, discriminatory language, sustained
    disruption, and publication of others' private information are unacceptable.

    Maintainers may edit, remove, or reject contributions and may temporarily or
    permanently restrict participation for conduct that is inappropriate, harmful,
    or threatening. Report conduct concerns privately to the repository owner using
    the contact mechanism on their GitHub profile. Maintainers will respond fairly
    and protect reporter privacy as far as practical.

    This policy is adapted from Contributor Covenant 2.1:
    https://www.contributor-covenant.org/version/2/1/code_of_conduct/
    """)
    write("CITATION.cff", """
    cff-version: 1.2.0
    message: "If you use Upgradeables, cite this repository."
    title: "Upgradeables: A Model-Agnostic Registry of Composable AI Primitives"
    type: software
    version: 0.1.0
    date-released: 2026-09-03
    authors:
      - name: "Upgradeables contributors"
    license: Apache-2.0
    repository-code: "https://github.com/robkazi52/upgradeables"
    """)
    write("pyproject.toml", """
    [project]
    name = "upgradeables-registry"
    version = "0.1.0"
    description = "Validation and build tooling for the Upgradeables registry"
    requires-python = ">=3.11"
    license = "Apache-2.0"
    dependencies = []

    [tool.pytest.ini_options]
    testpaths = ["tests"]
    """)
    write("LICENSE", APACHE_LICENSE)


APACHE_LICENSE = r"""
Apache License
Version 2.0, January 2004
http://www.apache.org/licenses/

TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

1. Definitions.

"License" shall mean the terms and conditions for use, reproduction, and
distribution as defined by Sections 1 through 9 of this document.

"Licensor" shall mean the copyright owner or entity authorized by the
copyright owner that is granting the License.

"Legal Entity" shall mean the union of the acting entity and all other
entities that control, are controlled by, or are under common control with
that entity. For the purposes of this definition, "control" means (i) the
power, direct or indirect, to cause the direction or management of such
entity, whether by contract or otherwise, or (ii) ownership of fifty percent
(50%) or more of the outstanding shares, or (iii) beneficial ownership of
such entity.

"You" (or "Your") shall mean an individual or Legal Entity exercising
permissions granted by this License.

"Source" form shall mean the preferred form for making modifications,
including but not limited to software source code, documentation source, and
configuration files.

"Object" form shall mean any form resulting from mechanical transformation
or translation of a Source form, including but not limited to compiled object
code, generated documentation, and conversions to other media types.

"Work" shall mean the work of authorship, whether in Source or Object form,
made available under the License, as indicated by a copyright notice that is
included in or attached to the work (an example is provided in the Appendix
below).

"Derivative Works" shall mean any work, whether in Source or Object form,
that is based on (or derived from) the Work and for which the editorial
revisions, annotations, elaborations, or other modifications represent, as a
whole, an original work of authorship. For the purposes of this License,
Derivative Works shall not include works that remain separable from, or merely
link (or bind by name) to the interfaces of, the Work and Derivative Works
thereof.

"Contribution" shall mean any work of authorship, including the original
version of the Work and any modifications or additions to that Work or
Derivative Works thereof, that is intentionally submitted to Licensor for
inclusion in the Work by the copyright owner or by an individual or Legal
Entity authorized to submit on behalf of the copyright owner. For the purposes
of this definition, "submitted" means any form of electronic, verbal, or
written communication sent to the Licensor or its representatives, including
but not limited to communication on electronic mailing lists, source code
control systems, and issue tracking systems that are managed by, or on behalf
of, the Licensor for the purpose of discussing and improving the Work, but
excluding communication that is conspicuously marked or otherwise designated
in writing by the copyright owner as "Not a Contribution."

"Contributor" shall mean Licensor and any individual or Legal Entity on
behalf of whom a Contribution has been received by Licensor and subsequently
incorporated within the Work.

2. Grant of Copyright License. Subject to the terms and conditions of this
License, each Contributor hereby grants to You a perpetual, worldwide,
non-exclusive, no-charge, royalty-free, irrevocable copyright license to
reproduce, prepare Derivative Works of, publicly display, publicly perform,
sublicense, and distribute the Work and such Derivative Works in Source or
Object form.

3. Grant of Patent License. Subject to the terms and conditions of this
License, each Contributor hereby grants to You a perpetual, worldwide,
non-exclusive, no-charge, royalty-free, irrevocable (except as stated in this
section) patent license to make, have made, use, offer to sell, sell, import,
and otherwise transfer the Work, where such license applies only to those
patent claims licensable by such Contributor that are necessarily infringed by
their Contribution(s) alone or by combination of their Contribution(s) with
the Work to which such Contribution(s) was submitted. If You institute patent
litigation against any entity (including a cross-claim or counterclaim in a
lawsuit) alleging that the Work or a Contribution incorporated within the Work
constitutes direct or contributory patent infringement, then any patent
licenses granted to You under this License for that Work shall terminate as of
the date such litigation is filed.

4. Redistribution. You may reproduce and distribute copies of the Work or
Derivative Works thereof in any medium, with or without modifications, and in
Source or Object form, provided that You meet the following conditions:

(a) You must give any other recipients of the Work or Derivative Works a copy
of this License; and

(b) You must cause any modified files to carry prominent notices stating that
You changed the files; and

(c) You must retain, in the Source form of any Derivative Works that You
distribute, all copyright, patent, trademark, and attribution notices from the
Source form of the Work, excluding those notices that do not pertain to any
part of the Derivative Works; and

(d) If the Work includes a "NOTICE" text file as part of its distribution,
then any Derivative Works that You distribute must include a readable copy of
the attribution notices contained within such NOTICE file, excluding those
notices that do not pertain to any part of the Derivative Works, in at least
one of the following places: within a NOTICE text file distributed as part of
the Derivative Works; within the Source form or documentation, if provided
along with the Derivative Works; or, within a display generated by the
Derivative Works, if and wherever such third-party notices normally appear.
The contents of the NOTICE file are for informational purposes only and do not
modify the License. You may add Your own attribution notices within Derivative
Works that You distribute, alongside or as an addendum to the NOTICE text from
the Work, provided that such additional attribution notices cannot be
construed as modifying the License.

You may add Your own copyright statement to Your modifications and may provide
additional or different license terms and conditions for use, reproduction, or
distribution of Your modifications, or for any such Derivative Works as a
whole, provided Your use, reproduction, and distribution of the Work otherwise
complies with the conditions stated in this License.

5. Submission of Contributions. Unless You explicitly state otherwise, any
Contribution intentionally submitted for inclusion in the Work by You to the
Licensor shall be under the terms and conditions of this License, without any
additional terms or conditions. Notwithstanding the above, nothing herein
shall supersede or modify the terms of any separate license agreement you may
have executed with Licensor regarding such Contributions.

6. Trademarks. This License does not grant permission to use the trade names,
trademarks, service marks, or product names of the Licensor, except as required
for reasonable and customary use in describing the origin of the Work and
reproducing the content of the NOTICE file.

7. Disclaimer of Warranty. Unless required by applicable law or agreed to in
writing, Licensor provides the Work (and each Contributor provides its
Contributions) on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
KIND, either express or implied, including, without limitation, any warranties
or conditions of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
PARTICULAR PURPOSE. You are solely responsible for determining the
appropriateness of using or redistributing the Work and assume any risks
associated with Your exercise of permissions under this License.

8. Limitation of Liability. In no event and under no legal theory, whether in
tort (including negligence), contract, or otherwise, unless required by
applicable law (such as deliberate and grossly negligent acts) or agreed to in
writing, shall any Contributor be liable to You for damages, including any
direct, indirect, special, incidental, or consequential damages of any
character arising as a result of this License or out of the use or inability to
use the Work (including but not limited to damages for loss of goodwill, work
stoppage, computer failure or malfunction, or any and all other commercial
damages or losses), even if such Contributor has been advised of the
possibility of such damages.

9. Accepting Warranty or Additional Liability. While redistributing the Work
or Derivative Works thereof, You may choose to offer, and charge a fee for,
acceptance of support, warranty, indemnity, or other liability obligations
and/or rights consistent with this License. However, in accepting such
obligations, You may act only on Your own behalf and on Your sole
responsibility, not on behalf of any other Contributor, and only if You agree
to indemnify, defend, and hold each Contributor harmless for any liability
incurred by, or claims asserted against, such Contributor by reason of your
accepting any such warranty or additional liability.

END OF TERMS AND CONDITIONS

APPENDIX: How to apply the Apache License to your work.

To apply the Apache License to your work, attach the following boilerplate
notice, with the fields enclosed by brackets "[]" replaced with your own
identifying information. (Don't include the brackets!) The text should be
enclosed in the appropriate comment syntax for the file format. We also
recommend that a file or class name and description of purpose be included on
the same "printed page" as the copyright notice for easier identification
within third-party archives.

Copyright [yyyy] [name of copyright owner]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


def spec_docs() -> None:
    write("spec/OS_PHILOSOPHY.md", """
    # OS Philosophy

    The model is the general reasoning substrate; an OS is a compositional operating
    layer that supplies task identity, authority, routing, explicit state, domain
    structure, evidence handling, safety, and quality control. It should shape work
    without pretending to replace native model capability.

    The architecture is layered and nonmonolithic:

    ```text
    Global OS -> Project kernel -> Task shell
              -> Behavior Gene + Core + Upgradeables
              -> Loader + State + Orchestrator + Validators -> Output
    ```

    ## Historical tier model

    T1 was the always-on kernel: a frozen 28-item bundle is confirmed, but only 18
    exact frozen member IDs are proven. Newly recovered pre-freeze T1 library items
    must not fill the ten gaps by inference. T2 was a 67-item, 12-family composable
    capability library. T3 was an opt-in alignment/verification layer activated by
    risk, evidence sensitivity, or mode—not a command to run every expensive check.
    T4 supervises the scaffolding itself: drift width, depth, throughput, stability,
    mode selection, and model-capability scaling.

    Load the minimum necessary context. Separate behavior from knowledge. Prefer
    orchestration over prompt accumulation, explicit state over hidden assumptions,
    truth before fluency, local repair before global rewrite, and bounded iteration.
    Preserve factual (`Lf`), evaluative (`Le`), framing (`Lp`), and hypothetical
    (`Lh`) phase boundaries where risk makes leakage consequential.

    Risk and consequence determine reasoning depth and validation. Design may use
    broader bounded exploration; execution collapses to a narrower grounded path.
    Stronger models should need less scaffolding, while integrity controls remain
    whenever the task still requires them.
    """)
    write("spec/UPGRADEABLE_SPEC.md", f"""
    # Upgradeable Specification

    An Upgradeable is a versioned, reusable behavioral, reasoning, state, retrieval,
    validation, editing, orchestration, or control primitive. It is not automatically
    a standalone Skill. Implementations may use a Skill component, mode, validator,
    state schema/manager, reference, deterministic script, orchestrator, bundle, or
    archival record.

    A modern Upgradeable is selectively loadable, activates under identifiable
    conditions, performs a bounded transformation or control function through a
    defined interface, and returns a predictable result to the host OS. A historical
    item may remain preserved even when it does not meet this modern normalization
    test; new contributions normally must meet it or become a mode, recipe, bundle,
    profile, reference, or implementation detail.

    ## Functional taxonomy

    {', '.join(f'`{x}`' for x in FUNCTIONAL_CLASSES)}.

    ## Activation and lifecycle

    Activation classes are `U0-foundational`, `U1-common-conditional`,
    `U2-specialized`, `U3-high-risk-expensive`, and `U4-meta-architecture`.
    Lifecycle values are `historical`, `unresolved`, `experimental`, `candidate`,
    `stable`, `core`, and `deprecated`. Historical recovery status is a separate axis.

    ## Required contract

    Metadata declares identity/version, registry generation, aliases/provenance,
    recovery/lifecycle, tiers, functional and activation classes, forms, purpose,
    triggers and non-triggers, inputs/outputs, dependencies and companions,
    counterbalances/redundancy/conflicts, failure boundary, model scaling, and package
    path. Documentation adds explicit mechanism, procedure, always/never rules,
    precedence, examples, and behavioral/composition tests.

    Unresolved records are archival-only and must contain no invented procedure.
    Validators may approve, reject, score, veto, request repair, or abstain; they may
    not manufacture supporting facts.
    """)
    write("spec/COMPOSITION_SPEC.md", """
    # Composition Specification

    The primary value of Upgradeables is composition. Select only components whose
    triggers are active, preserve authority order, declare state interfaces, and
    remove redundant scaffolding.

    ## Common stacks

    ```text
    Foundation: Task lock -> Mode lock -> StateBlock -> Scoped loader
                -> Working-memory cues -> Drift suppression

    Evidence: Grounding -> Activation-budget funnel -> Evidence capture/index
              -> Critical atomic verification -> Multi-truth gating
              -> Citation fidelity -> Truth priority -> QMS

    Exploration: Controlled drift + Cognitive flexibility + Perspective break
                 -> bounded Multiverse candidates -> QMS collapse

    Repair: Detect -> Micro-repair -> CRISPR edit -> Structured refinement
            -> Regenerative rewrite -> Surgery edit

    Long context: StateBlock + SMSE + WM lock + Stable context + ABF
                  + Attention compression + Neuro-focus + Drift suppression
                  + Coherence heartbeat + State snapshot
    ```

    Pair Neuro-Focus with Anti-Tunnel Vision; Multiverse with QMS; CRISPR with
    Invariance Stress; Controlled Drift with Grounding; Risk Scaling with Dynamic
    Depth; StateBlock with SMSE; Citation Fidelity with Style Alignment; Cosmic/POWER
    planning with SAFE execution; and Resonance with Domain/Mode Isolation.

    A composition test must cover positive activation, negative activation,
    precedence conflict, unsupported claims, long-context state, over-scaffolding,
    and strong-model scaling when relevant.
    """)
    write("spec/PRECEDENCE_SPEC.md", """
    # Authority, Compatibility, and Precedence

    ```text
    Host/system safety
      -> organization/domain policy
        -> active OS/project kernel
          -> task lock
            -> Behavior Gene/Core
              -> Upgradeables
                -> style preferences
    ```

    A lower layer cannot silently defeat a higher layer. Explicit veto validators may
    block commitment when their declared condition is met, but cannot rewrite higher
    authority. When validators conflict, use the applicable truth/authority hierarchy;
    if no rule resolves a material conflict, abstain or escalate.

    Compatibility is not equivalence. Counterbalances intentionally limit one
    another (for example Neuro-Focus and Anti-Tunnel Vision). Potential redundancy
    signals that a composition may be simplified. Cross-module alignment applies only
    inside declared domain and mode boundaries.
    """)
    write("spec/VERSIONING_SPEC.md", """
    # Versioning Specification

    The repository and each operational package use Semantic Versioning where
    practical. Cosmetic corrections are patch changes; compatible procedure or
    metadata improvements are minor; contract-breaking behavior changes are major.
    Identity changes normally create a migration and alias.

    Historical IDs are immutable provenance keys scoped to their registry generation.
    Modern slugs must not be recycled for unrelated concepts. Deprecation retains the
    record, aliases, replacement, and migration guidance.
    """)
    write("spec/RECOVERY_AND_PROVENANCE_SPEC.md", """
    # Recovery and Provenance Specification

    Archived source files are immutable recovery artifacts. Operational packages may
    normalize names but must link to source document, source ID, registry generation,
    aliases, and recovery status. Numeric IDs from the frozen November 2025 T2 set are
    not the same generation as September 2026 consolidated T2 IDs.

    Exact recovery preserves the recovered name. Family recovery records a range and
    count without inventing member names. Unresolved records are archival-only and
    contain no mechanism. Acronym collisions use separate namespaces; notably ITFC
    means both Image Text Fidelity Capture and an incompletely specified Intent/Task
    Framing Controller. OCG, ECL expansion, LROS expansion, the ExIt acronym expansion,
    and full Nano specification remain unresolved. So do ten frozen T1 members and the
    individual names in frozen T2 ranges 001–007, 024–030, and 044–060. T2-061–067
    names are provisional historical assistant artifacts; their historical definitions
    remain uncorroborated.

    A resolution requires a proposal, primary source provenance, review, and an
    append-only mapping update. Never overwrite the archive to make it match a modern
    interpretation.

    ## Deep-recovery evidence precedence

    For historical claims, use: direct recovered user specification; user-accepted or
    frozen artifact; Historical Recovery Inventory; current Translation Catalog;
    historical assistant artifact; then modern implementation guidance. Preserve
    conflicts instead of silently reconciling them.

    Records declare `source_kind`, `canonicality`, and `recovery_confidence`. A
    historical assistant artifact is useful provenance but remains provisional unless
    independently corroborated. Pre-freeze T1 library items must never be used to fill
    the ten unknown frozen T1 slots without direct evidence.
    """)
    write("spec/SKILL_TRANSLATION_SPEC.md", """
    # Skill Translation Specification

    ```text
    Skill = Task Identity + Behavior + Knowledge/References
            + Selected Upgradeables + State Requirements
            + Validation + Output Contract
    ```

    Not every Skill needs every term, and not every Upgradeable becomes a Skill.

    1. Identify the Skill archetype.
    2. Define task identity and activation boundary.
    3. Determine risk tier and evidence sensitivity.
    4. Determine state and context requirements.
    5. Select a Behavior Gene and Core where applicable.
    6. Load foundational, then task-specific Upgradeables.
    7. Add risk-dependent validators.
    8. Check compatibility, counterbalances, conflicts, and redundancy.
    9. Remove unnecessary scaffolding.
    10. Choose the implementation form for every component.
    11. Generate target instructions and move deep material to references/resources.
    12. Add deterministic scripts only when they materially help.
    13. Add positive, negative, conflict, long-context, and composition tests.
    14. Run QMS/validation against the complete Skill.

    Keep descriptions activation-oriented: say what the Skill does and when it should
    activate, including exclusions. Preserve authority and failure boundaries.
    Stronger models should receive less unnecessary scaffolding, while truth, state,
    safety, and integrity controls remain when the task still requires them.
    """)


def templates() -> None:
    docs = {
        "UPGRADEABLE_TEMPLATE.md": """# <Display Name>\n\nSummary and purpose.\n\n## Scope\n## Trigger Conditions\n## Non-Triggers\n## Inputs / Required State\n## Outputs / Produced State\n## Mechanism\n## Procedure\n## Always-Do Rules\n## Never-Do / Avoid Rules\n## Interaction Rules\n## Compatible Upgradeables\n## Counterbalancing Upgradeables\n## Potential Redundancy\n## Conflict / Precedence Rules\n## Failure Boundary\n## Strong-Model Scaling\n## Recommended Skill Types\n## Example Composition\n## Tests\n## Provenance / Historical Aliases\n""",
        "UPGRADEABLE_PROPOSAL_TEMPLATE.md": """# Upgradeable proposal: <name>\n\n## Purpose and problem solved\n## Closest prior art\n## Material difference\n## Why composition/mode/recipe/bundle/reference is insufficient\n## Trigger and non-trigger\n## Inputs and outputs\n## Explicit mechanism and procedure\n## Always / never rules\n## Failure boundary\n## Compatibility, counterbalances, conflicts, and redundancy\n## Recommended Skill types and implementation form\n## Example and tests\n## Limitations\n## Provenance / external references\n""",
        "BEHAVIOR_GENE_TEMPLATE.md": """# <Behavior Gene>\n\nVersion: 0.1.0\n\n## Purpose and scope\n## Triggers\n## Always do\n## Never do\n## Reasoning pattern\n## Evidence handling\n## Core interfaces\n## Output contract\n## Compatibility and conflicts\n## Provenance\n""",
        "CORE_TEMPLATE.md": """# <Core>\n\nVersion: 0.1.0\n\n## Scope\n## Entities / variables\n## Reasoning map\n## Required data\n## Evidence hierarchy\n## Decision logic\n## Failure modes\n## Examples\n## Gene interfaces\n## Validator interfaces\n## Source provenance\n""",
        "BUNDLE_TEMPLATE.md": """# <Bundle>\n\n## Purpose and trigger\n## Components and load order\n## Required / optional modules\n## State contract\n## Conflicts and precedence\n## Failure behavior\n## Composition tests\n""",
        "SKILL_RECIPE_TEMPLATE.md": """# <Skill recipe>\n\n## Task identity and boundary\n## Risk / evidence profile\n## Gene and Core selection\n## Matrix (R/A/C/O/X)\n## Composition order\n## Output contract\n## Tests and scaling\n""",
        "COMPOSITION_TEST_TEMPLATE.md": """# Composition test\n\n## Components\n## Initial state\n## Positive trigger\n## Negative trigger\n## Conflict / expected precedence\n## Long-context case\n## Unsupported-claim case\n## Over-scaffolding case\n## Expected result\n""",
        "SKILL_IMPLEMENTATION_TEMPLATE.md": """---\nname: <lowercase-skill-name>\ndescription: <what this Skill does, exactly when it activates, and exclusions>\n---\n\n# <Skill Name>\n\n## Task Identity and Activation Boundary\n## Required Inputs and Explicit State\n## Behavior Gene (optional)\n## Core / References (optional)\n## Selected Upgradeables\n- `<slug>@<version>` — <why selected and trigger>\n## Authority and Precedence\n## Procedure\n## Validators and Failure Handling\n## Output Contract\n## Strong-Model Scaling\n## Tests\n\nPlace deep sources in `references/`, deterministic operations in `scripts/`, and only necessary output assets in `assets/`.\n""",
    }
    for name, body in docs.items():
        write(f"templates/{name}", body)


def package_docs() -> None:
    for item in ENTRIES:
        package_dir = Path(item["package_path"]).parent
        metadata = {key: item[key] for key in (
            "schema_version", "id", "slug", "display_name", "version",
            "registry_generation", "historical_ids", "historical_aliases",
            "recovery_status", "lifecycle_status", "tiers", "functional_classes",
            "activation_class", "implementation_forms", "purpose",
            "recommended_skill_types", "usually_not_needed_for", "triggers",
            "non_triggers", "requires", "recommended_with", "counterbalances",
            "potentially_redundant_with", "conflicts", "inputs", "outputs",
            "strong_model_scaling", "failure_boundary", "supersedes", "superseded_by", "package_path", "provenance",
        )}
        write_json(str(package_dir / "metadata.yaml"), metadata)
        compatible = item["recommended_with"] or ["None declared"]
        counter = item["counterbalances"] or ["None declared"]
        redundant = item["potentially_redundant_with"] or ["None declared"]
        aliases = item["historical_aliases"] or ["None"]
        may_skip_text = "; ".join(item["strong_model_scaling"]["may_skip"]) or "nothing; the invariant remains active whenever citations are emitted"
        mandatory_text = "; ".join(item["strong_model_scaling"]["keep_mandatory"])
        if item["slug"] == "sequential-memory-state-engine":
            mechanism_text = "Process bounded source chunks through fact extraction, compartment routing, state growth, explicit reasoning hooks, canonical working memory, drift guard, and working-memory heartbeat snapshots."
            procedure = ["Ingest one bounded source chunk.", "Extract only explicit facts with source provenance.", "Route facts to the correct topic/domain compartment.", "Grow state for genuinely new topics without overwriting locked compartments.", "Expose explicit state-field hooks to downstream reasoning modules.", "Treat StateBlock as canonical working memory for this workflow.", "Reject or flag reasoning unsupported by source/state.", "Refresh locks, focus, drift status, and a continuation snapshot at meaningful heartbeats."]
        elif item["slug"] == "cot-structured-state-block":
            mechanism_text = "Store explicit, auditable reasoning-state atoms such as InputFacts, Inference, Phase, and Topic; apply phase separation, topic isolation, truth gates, and risk-dependent vetoes without recording private chain-of-thought."
            procedure = ["Capture source-backed InputFacts.", "Record only concise task-relevant inferences with epistemic status.", "Label semantic Phase and Topic.", "Apply domain/topic isolation and high-risk truth gates.", "Return an auditable state object or fail-closed status."]
        elif item["slug"] == "bounded-exit":
            mechanism_text = "Evaluate the current output, select the highest-value defect, repair it, and stop at a quality threshold, iteration budget, or diminishing-return boundary. The ExIt acronym expansion remains unresolved."
            procedure = ["Evaluate against the locked goal and output contract.", "Identify the highest-value remaining defect.", "Apply the smallest sufficient repair.", "Re-evaluate the changed result.", "Stop when the threshold, budget, or diminishing-return rule is met."]
        elif item["slug"] == "citation-fidelity":
            mechanism_text = "Bind each claim to its cited source passage; verify source existence, exact quotes, paraphrase meaning, and that support was not borrowed from an adjacent claim. Return a status without rewriting evidence."
            procedure = ["Split the output into cited claims.", "Locate the cited source passage for each claim.", "Compare the claim or quote with that passage for direct support and preserved meaning.", "Return pass, fail, repair-required, or unverifiable for each claim.", "Do not certify the output while a material citation is failed or unverifiable."]
        elif "validator" in item["implementation_forms"]:
            mechanism_text = "Evaluate the candidate against declared evidence, constraints, and invariants, then return a status or veto. Inspection never supplies missing facts."
            procedure = ["Confirm the trigger and governing criteria.", "Identify the candidate units that require checking.", "Evaluate each unit against available evidence and invariants.", "Return pass, fail, repair-required, or unverifiable with defect locations.", "Block certification when the failure boundary is reached."]
        elif "state-schema" in item["implementation_forms"] or "state-manager" in item["implementation_forms"]:
            mechanism_text = "Represent or update task state through explicit host-visible fields. Reconcile changes with locked state and record unavailable persistence honestly."
            procedure = ["Read the current explicit state and authority rules.", "Validate the proposed update against locked fields and provenance.", "Apply only authorized field changes.", "Retire or mark superseded state without erasing provenance.", "Emit the updated state or a conflict/unavailable-persistence status."]
        elif "editing-repair" in item["functional_classes"]:
            mechanism_text = "Classify the defect and apply the smallest authorized edit that can restore correctness while protecting facts, citations, and invariants."
            procedure = ["Locate and classify the defect.", "Lock surrounding facts and invariants.", "Apply the smallest sufficient repair class.", "Compare the result with the source and requested change.", "Escalate or stop if the protected invariants cannot be preserved."]
        elif "orchestrator" in item["implementation_forms"]:
            mechanism_text = "Select and sequence only available components whose triggers match, pass explicit state between them, and resolve authority before execution."
            procedure = ["Confirm task identity, risk, and authority.", "Inspect available component manifests and triggers.", "Select the minimum sufficient composition and load order.", "Pass explicit bounded state through the selected interfaces.", "Emit the plan/result plus unresolved conflicts and unavailable capabilities."]
        else:
            mechanism_text = "Apply the named behavior as an explicit, bounded control over the declared input and state, then record the result or failure status."
            procedure = ["Confirm the task lock, authority layer, and trigger.", "Read only the required state and evidence.", "Apply the documented bounded behavior.", "Check protected truth, state, safety, and output invariants.", "Emit the result or an explicit unsupported/blocked status."]
        procedure_text = "\n".join(f"{number}. {step}" for number, step in enumerate(procedure, 1))
        write(str(package_dir / "UPGRADEABLE.md"), f"""
        # {item['display_name']}

        ## Summary

        {item['purpose']}

        ## Purpose

        Provide a reusable `{item['implementation_forms'][0]}` mechanism rather than
        a complete task identity or monolithic prompt.

        ## Problem Solved

        Prevents the workflow failure implied by the trigger while keeping the
        intervention bounded and inspectable.

        ## Scope

        Functional classes: {', '.join(item['functional_classes'])}. Activation:
        `{item['activation_class']}`. This modern classification is not a historical tier.

        ## Trigger Conditions

        {chr(10).join('- ' + value for value in item['triggers'])}

        ## Non-Triggers

        {chr(10).join('- ' + value for value in item['non_triggers'])}

        ## Inputs / Required State

        {chr(10).join('- ' + value for value in item['inputs'])}

        ## Outputs / Produced State

        {chr(10).join('- ' + value for value in item['outputs'])}

        ## Mechanism

        {mechanism_text}

        The name is architectural identity, not a claim of a physical, biological,
        hidden, or private-reasoning mechanism.

        ## Procedure

        {procedure_text}

        ## Always-Do Rules

        - Preserve higher-authority instructions and locked facts.
        - Label assumptions and unavailable host capabilities.
        - Keep activation proportional to risk and value.

        ## Never-Do / Avoid Rules

        - Do not invent evidence, hidden state, persistence, or execution.
        - Do not remain active when the trigger is absent.
        - Do not expose or require private chain-of-thought.

        ## Interaction Rules

        Load after the task boundary is known. Validators inspect or veto but do not
        author supporting facts. State changes must use explicit state mechanisms.

        ## Compatible Upgradeables

        {chr(10).join('- `' + value + '`' for value in compatible)}

        ## Counterbalancing Upgradeables

        {chr(10).join('- `' + value + '`' for value in counter)}

        ## Potential Redundancy

        {chr(10).join('- `' + value + '`' for value in redundant)}

        ## Conflict / Precedence Rules

        Host/system safety, domain policy, the active OS, and the task lock take
        precedence. On an unresolved material conflict, narrow, abstain, or escalate.

        ## Failure Boundary

        {chr(10).join('- ' + value for value in item['failure_boundary'])}

        ## Strong-Model Scaling

        May skip: {may_skip_text}.
        Keep mandatory: {mandatory_text}.

        ## Recommended Skill Types

        {chr(10).join('- `' + value + '`' for value in item['recommended_skill_types'])}

        ## Example Composition

        Activate `{item['slug']}` only after task framing, combine it with the declared
        compatible controls, then validate its output before final commitment.

        ## Tests

        See [`tests/composition.md`](tests/composition.md) for positive, negative,
        conflict, and scaling cases.

        ## Provenance / Historical Aliases

        Source ID: `{item['id']}` in `{SOURCE_DOC}`. Registry generation:
        `{item['registry_generation']}`. Aliases: {', '.join(aliases)}.
        {item['provenance']['notes']}
        """)
        write(str(package_dir / "examples/basic.md"), f"""
        # Basic composition example

        **Situation:** {item['triggers'][0]}.

        **Composition:** establish a task lock, activate `{item['slug']}`, preserve
        explicit state and evidence boundaries, then pass the result through the
        workflow's applicable validator.

        **Expected:** the component performs only its documented purpose and reports
        uncertainty or failure instead of manufacturing missing support.
        """)
        write(str(package_dir / "tests/composition.md"), f"""
        # Composition tests

        - **Positive:** given `{item['triggers'][0]}`, the component activates and
          emits a bounded result/status.
        - **Negative:** on a simple task without the trigger, the component stays
          inactive and adds no scaffolding.
        - **Conflict:** a lower-priority style or component instruction cannot override
          host policy, domain policy, or the task lock.
        - **Integrity:** absent evidence or host capability is reported, not invented.
        - **Scaling:** a capable host may omit verbose scaffolding but must retain any
          task-required truth, state, safety, and integrity invariant.
        """)


def genes_and_cores() -> None:
    write("genes/README.md", """
    # Behavior Genes

    A Behavior Gene defines how a workflow reasons and writes for a recurring task
    family. It is not a knowledge dump or an entire Skill. A Gene declares triggers,
    always/never rules, reasoning pattern, evidence handling, Core interfaces, output
    contract, compatibility, and version/provenance.

    The examples here preserve recovered family scope only. Medical/appeal Genes do
    not contain clinical policy or organization-specific criteria; an implementation
    must supply an authorized, versioned Core and applicable validators.
    """)
    for identifier, slug, name, purpose in GENES:
        domain_limited = slug in {"ipmn", "ipta", "opmn", "opta", "readmission", "gmn"}
        write(f"genes/examples/{slug}.md", f"""
        # {name}

        **Version:** 0.1.0  
        **Source ID:** `{identifier}`  
        **Recovery:** exact family/name recovery; seed description only

        ## Purpose and Scope

        {purpose} {'This public seed intentionally contains no clinical criteria or private policy.' if domain_limited else ''}

        ## Triggers

        Activate only when the task is explicitly within this behavior family and the
        required evidence/Core is available.

        ## Always Do

        Preserve task lock, evidence boundaries, provenance, uncertainty labels, and
        the selected Core's authority.

        ## Never Do

        Do not invent domain rules, evidence, memory, or conclusions. Do not substitute
        this behavior pattern for an authorized knowledge Core.

        ## Reasoning Pattern and Evidence Handling

        Frame the task, retrieve only relevant Core material, apply the named behavior,
        separate fact from inference, and validate the output before commitment.

        ## Core Interfaces

        Use the corresponding domain Core where one exists; otherwise declare the
        required reference interface explicitly.

        ## Output Contract

        Emit a source-bounded result in the task's requested form, including material
        uncertainty and unresolved conflicts.

        ## Compatibility

        Compatible with grounding, state, domain/mode isolation, and risk-appropriate
        validators. Higher authority always wins.
        """)
    write_json("genes/index.json", {"schema_version":"1.0.0", "behavior_genes":[
        {"id":identifier, "slug":slug, "display_name":name, "purpose":purpose,
         "path":f"genes/examples/{slug}.md", "source_kind":"current_consolidated_catalog",
         "canonicality":"canonical", "recovery_confidence":"high"} for identifier, slug, name, purpose in GENES
    ]})

    write("cores/README.md", """
    # Cores

    A Core is a high-density domain reasoning, evidence, and reference module. It
    defines scope, variables, reasoning map, data requirements, evidence hierarchy,
    decision logic, failure modes, examples, and Gene/validator interfaces. It is not
    a behavior prompt.

    These seed descriptors preserve recovered Core identities but do not invent the
    absent domain content. Contributors may add content only with publishable source
    provenance and domain review.
    """)
    for identifier, slug, name, purpose in CORES:
        write(f"cores/examples/{slug}.md", f"""
        # {name}

        **Version:** 0.1.0  
        **Source ID:** `{identifier}`  
        **Recovery:** recovered identity/role; detailed domain content not recovered

        ## Scope

        {purpose}

        ## Entities, Variables, and Required Data

        Unknown / not recovered in the canonical corpus. An implementation must define
        them from authorized, versioned, citable sources.

        ## Reasoning Map, Evidence Hierarchy, and Decision Logic

        Unknown / not recovered. Do not infer domain rules from the Core name.

        ## Failure Modes

        Missing or stale source material, unsupported specificity, cross-domain
        contamination, and use without the matching Behavior Gene.

        ## Examples

        No factual domain example is supplied because the source corpus does not
        contain enough detail to create one safely.

        ## Interfaces

        Pair with the corresponding Gene where available, Grounding / No-Invention,
        Citation Fidelity when sources are cited, and risk-appropriate QMS modes.

        ## Source Provenance

        `{SOURCE_DOC}`, `{identifier}`.
        """)
    write_json("cores/index.json", {"schema_version":"1.0.0", "cores":[
        {"id":identifier, "slug":slug, "display_name":name, "purpose":purpose,
         "path":f"cores/examples/{slug}.md", "source_kind":"current_consolidated_catalog",
         "canonicality":"canonical", "recovery_confidence":"high"} for identifier, slug, name, purpose in CORES
    ]})


def qms_and_bundles() -> None:
    qms_rows = "\n".join(f"| `{identifier}` | `{slug}` | {name} | {purpose} |" for identifier, slug, name, purpose in QMS_MODES)
    write("bundles/qms/README.md", """
    # Parallel QMS

    Parallel QMS is one validator family with named modes, not fifteen unrelated
    authoring Skills. A mode may approve, reject, score, veto, request repair, or
    abstain. It cannot add unsupported facts. "Parallel" means real isolated execution
    only when the host supplies it; otherwise use clearly labeled independent passes.

    See [QMS variants](QMS_VARIANTS.md) and [operating rules](OPERATING_RULES.md).
    """)
    write("bundles/qms/QMS_VARIANTS.md", f"""
    # QMS Variants

    | Source ID | Mode | Name | Operational interpretation |
    |---|---|---|---|
    {qms_rows}

    Monte QMS is assumption perturbation unless stochastic sampling is actually
    implemented. Distributed QMS must not claim distributed execution without a host
    mechanism. All modes inherit the parent validator's no-invention boundary.
    """)
    write("bundles/qms/OPERATING_RULES.md", """
    # Parallel QMS Operating Rules

    Mirror checks use independent A/B evaluations; convergence supports acceptance,
    while material divergence triggers re-evaluation, softening, uncertainty, or
    abstention. Risk-tier-split varies evaluator depth. Cross-phase prevents factual,
    evaluative, framing, and hypothetical leakage. Hierarchical checks align atomic,
    section, and global output; transversal checks temporal, causal, modal, and logical
    relationships. Heterogeneous passes use different criteria rather than repeated
    copies of one score. Inversion reconstructs the evidence a conclusion would require.

    Global QMS collapse is a controlled commitment gate, not simple majority voting:
    critical truth atoms must agree sufficiently; safety may veto; unsupported citation
    trails are downgraded or vetoed; persistent crucial disagreement causes repair,
    explicit uncertainty, or abstention. ExIt-integrated passes obey iteration budgets.
    Distributed/parallel claims require actual host support.

    **Provenance:** operational details are recovered historical assistant artifacts in
    the Deep Context Recovery Addendum; current names/roles remain grounded in the
    consolidated catalog. Canonicality of the deeper encoding is provisional.
    """)
    write_json("bundles/qms/metadata.yaml", {
        "schema_version": "1.0.0", "slug": "parallel-qms", "display_name": "Parallel QMS",
        "version": "1.0.0", "purpose": "Compose named validation modes under one bounded family.",
        "components": ["parallel-qms"], "modes": [slug for _, slug, _, _ in QMS_MODES],
        "load_order": ["parallel-qms"],
    })
    write_json("registry/qms_modes.json", {"schema_version":"1.0.0", "modes":[
        {"id":identifier, "slug":slug, "display_name":name, "purpose":purpose,
         "source_kind":"current_consolidated_catalog", "canonicality":"canonical",
         "recovery_confidence":"high", "deep_operating_detail_source":ADDENDUM_DOC,
         "deep_detail_canonicality":"provisional"}
        for identifier, slug, name, purpose in QMS_MODES
    ]})

    bundle_defs = {
        "foundation": ["scoped-loader", "stateblock", "task-set-lock-in", "working-memory-cues", "grounding-no-invention", "drift-suppression", "placeholder-suppression", "mode-lock-in"],
        "reasoning": ["micro-scaffolding", "reasoning-scale-controller", "anti-tunnel-vision", "forethought-checkpoints", "bidirectional-consistency", "multiverse-reasoning", "bounded-exit"],
        "repair": ["safe-rewrite", "micro-repair", "regenerative-rewrite", "crispr-edit", "surgery-edit", "contradiction-micro-repair"],
        "truth-safety": ["multi-truth-gating", "truth-redundancy", "critical-atomic-verification", "controlled-drift-corridors", "truth-priority-hierarchy", "domain-mode-isolation", "fail-closed-abstention", "citation-fidelity", "counterfactual-integrity", "fermionic-veto", "risk-tier-scaling"],
        "meta-control": ["meta-supervisor", "meta-awareness", "stuck-pattern-reset", "coherence-heartbeat", "resonance", "neuro-focus", "dynamic-depth-allocation", "reasoning-throughput-governor", "drift-spectra-scaling", "compute-adaptive-drift", "domain-normalized-drift", "drift-immunity-propagation", "meta-stability", "cross-universe-consistency", "future-proof-mode-selector", "model-size-drift-scaling"],
        "authoring": ["style-alignment", "pedagogical-alignment", "safe-rewrite", "citation-fidelity", "placeholder-suppression"],
        "architect": ["architect-orchestrator", "behavior-gene-builder", "domain-core-builder", "adapter-first-experimentation", "crispr-edit", "surgery-edit", "scoped-loader", "state-snapshot", "ultimate-suite-supervisor"],
    }
    for slug, components in bundle_defs.items():
        title = slug.replace("-", " ").title()
        write_json(f"bundles/{slug}/metadata.yaml", {
            "schema_version": "1.0.0", "slug": slug, "display_name": f"{title} Bundle",
            "version": "1.0.0", "purpose": f"Curated {title.lower()} composition from recovered architecture.",
            "components": components, "load_order": components,
        })
        links = "\n".join(
            f"- [`{component}`](../../{next(item for item in ENTRIES if item['slug'] == component)['package_path']})"
            for component in components
        )
        write(f"bundles/{slug}/README.md", f"""
        # {title} Bundle

        A curated composition, not an always-on monolith. Activate components only
        when their individual triggers apply and preserve repository precedence.

        ## Components and default load order

        {links}

        ## Composition boundary

        Remove redundant or inactive controls. Validators do not add facts. Any state,
        persistence, or parallel execution must be backed by a real host mechanism.
        """)
    write("bundles/README.md", """
    # Bundle Index

    Bundles are curated compositions, not new primitives: [Foundation](foundation/),
    [Reasoning](reasoning/), [Repair](repair/), [Truth/Safety](truth-safety/),
    [Parallel QMS](qms/), [Meta-Control](meta-control/), [Authoring](authoring/), and
    [Architect](architect/). Inspect each component's trigger before activation.
    """)


def recipe_docs() -> None:
    recipes = {
        "research-skill": ("Research Skill", {"task-set-lock-in":"R", "scoped-loader":"R", "stateblock":"R", "grounding-no-invention":"R", "activation-budget-funnel":"A", "neuro-focus":"A", "stable-long-context":"A", "sequential-memory-state-engine":"A", "multi-truth-gating":"A", "citation-fidelity":"A", "truth-priority-hierarchy":"A", "critical-atomic-verification":"C", "parallel-qms":"A", "anti-tunnel-vision":"O", "state-snapshot":"C"}),
        "source-grounded-analysis": ("Source-Grounded Analysis", {"task-set-lock-in":"R", "mode-lock-in":"R", "grounding-no-invention":"R", "safe-rewrite":"A", "citation-fidelity":"R", "zero-drift-zones":"A", "controlled-drift-corridors":"A", "counterfactual-integrity":"A", "micro-repair":"A", "placeholder-suppression":"A", "parallel-qms":"A"}),
        "high-stakes-reasoning": ("High-Stakes Reasoning", {"grounding-no-invention":"R", "epistemic-status-gating":"R", "risk-tier-scaling":"R", "critical-atomic-verification":"R", "multi-truth-gating":"R", "truth-redundancy":"A", "truth-priority-hierarchy":"R", "domain-mode-isolation":"R", "citation-fidelity":"C", "fail-closed-abstention":"R", "fermionic-veto":"A", "parallel-qms":"R", "dynamic-depth-allocation":"A"}),
        "medical-evidence": ("Medical Evidence", {"task-set-lock-in":"R", "grounding-no-invention":"R", "risk-tier-scaling":"R", "critical-atomic-verification":"R", "truth-priority-hierarchy":"R", "citation-fidelity":"C", "fail-closed-abstention":"R", "domain-mode-isolation":"R", "parallel-qms":"R"}),
        "legal-evidence": ("Legal Evidence", {"task-set-lock-in":"R", "grounding-no-invention":"R", "risk-tier-scaling":"R", "critical-atomic-verification":"R", "truth-priority-hierarchy":"R", "citation-fidelity":"R", "zero-drift-zones":"A", "fail-closed-abstention":"R", "parallel-qms":"R"}),
        "coding-debugging": ("Coding / Debugging", {"task-set-lock-in":"R", "stateblock":"A", "forethought-checkpoints":"A", "dominant-driver-isolation-scaffold":"A", "anti-tunnel-vision":"A", "bidirectional-consistency":"A", "invariance-stress-scaffold":"R", "micro-repair":"R", "crispr-edit":"A", "surgery-edit":"C", "structured-refinement":"A", "bounded-exit":"A", "parallel-qms":"A", "drift-suppression":"A"}),
        "long-context-corpus": ("Long-Context / Corpus", {"stateblock":"R", "sequential-memory-state-engine":"R", "working-memory-lock-in":"A", "stable-long-context":"R", "activation-budget-funnel":"R", "attention-compression-scaffold":"A", "neuro-focus":"A", "drift-suppression":"R", "coherence-heartbeat":"A", "cross-context-resonance-lock":"C", "state-snapshot":"A", "citation-fidelity":"C"}),
        "authoring": ("Authoring", {"task-set-lock-in":"R", "grounding-no-invention":"C", "style-alignment":"A", "pedagogical-alignment":"C", "safe-rewrite":"R", "citation-fidelity":"C", "placeholder-suppression":"R", "micro-repair":"A", "parallel-qms":"A"}),
        "creative-ideation": ("Creative Ideation", {"task-set-lock-in":"R", "controlled-drift-corridors":"R", "counterfactual-integrity":"A", "domain-mode-isolation":"A", "multiverse-reasoning":"A", "anti-tunnel-vision":"A", "parallel-qms":"C", "grounding-no-invention":"C"}),
        "education-explanation": ("Education / Explanation", {"pedagogical-alignment":"R", "explanation-minimality-scaffold":"A", "style-alignment":"A", "grounding-no-invention":"A", "micro-scaffolding":"A", "task-set-lock-in":"R", "safe-rewrite":"A", "anti-tunnel-vision":"C", "parallel-qms":"C"}),
        "decision-support": ("Decision Support", {"task-set-lock-in":"R", "decision-first-scaffold":"R", "grounding-no-invention":"R", "risk-tier-scaling":"A", "anti-tunnel-vision":"A", "bidirectional-consistency":"A", "truth-priority-hierarchy":"A", "dynamic-depth-allocation":"C", "parallel-qms":"A"}),
        "architecture-skill-building": ("Architecture / Skill Building", {"architect-orchestrator":"R", "power-mode":"A", "hybrid-mode":"A", "reasoning-scale-controller":"A", "multiverse-reasoning":"A", "behavior-gene-builder":"C", "domain-core-builder":"C", "scoped-loader":"R", "stateblock":"R", "parallel-qms":"R", "meta-supervisor":"A", "adapter-first-experimentation":"A", "crispr-edit":"A", "surgery-edit":"C", "dynamic-depth-allocation":"A", "anti-tunnel-vision":"A", "state-snapshot":"A", "future-proof-mode-selector":"A"}),
        "multi-agent-orchestration": ("Multi-Agent / Orchestration", {"architect-orchestrator":"R", "scoped-loader":"R", "state-routing-bus":"R", "stateblock":"R", "state-snapshot":"R", "domain-mode-isolation":"R", "resonance":"A", "parallel-qms":"A", "multi-layer-consistency":"A", "external-state-automation":"C"}),
        "deterministic-intake-routing": ("Deterministic Intake / Routing", {"task-set-lock-in":"R", "clarification-gateway":"A", "grounding-no-invention":"R", "scoped-loader":"R", "domain-mode-isolation":"R", "stateblock":"R", "structured-state-projection":"A", "authority-anchor-enforcement":"A", "external-state-automation":"C", "authenticity-anti-evasion":"R"}),
        "long-context-source-fidelity": ("Long-Context Source Fidelity", {"working-memory-lock-in":"R", "sequential-memory-state-engine":"R", "stateblock":"R", "stable-long-context":"R", "zero-drift-zones":"R", "drift-suppression":"R", "image-text-fidelity-capture":"C", "reflectos":"A", "fail-closed-abstention":"R", "truth-redundancy":"A", "citation-fidelity":"C", "state-snapshot":"A"}),
    }
    recovered_recipe_guidance = {
        "deterministic-intake-routing": """## Recovered Procedure\n\n1. Classify the task and required output without drafting it.\n2. Extract required inputs field by field; mark missing values `Not documented`.\n3. Emit an explicit routing object with only recovered/authorized fields.\n4. Use that object to scoped-load the selected task/domain OS, blueprint, and permitted references.\n5. Run the drafting/execution stage separately, then validate.\n\nRouting to a source folder does not establish that its content applies. Intake never imports another domain's rules or performs the downstream task.""",
        "long-context-source-fidelity": """## Recovered Procedure\n\n1. Lock the source and task in working memory.\n2. Ingest bounded chunks into immutable, provenance-labeled source state.\n3. Transfer only user-selected material into explicit copy/working state.\n4. Verify completeness and fidelity in independent passes.\n5. Use bounded ReflectOS to repair only located defects.\n6. Fail closed on unverified text, then emit one final deliverable plus a state snapshot.\n\nKeep internal verification chunks separate from the final artifact. Image/figure ledgers activate only when the host and source format require them.""",
    }
    recipe_items = []
    for slug, (name, selections) in recipes.items():
        item = {
            "schema_version": "1.0.0", "slug": slug, "display_name": name,
            "version": "1.0.0", "purpose": f"Seed composition for {name.lower()} workflows.",
            "classifications": selections,
            "provenance": {"source_document":SOURCE_DOC, "source_kind":"modern_implementation_recommendation", "canonicality":"provisional", "recovery_confidence":"medium"},
        }
        if slug in {"deterministic-intake-routing", "long-context-source-fidelity"}:
            item["provenance"] = {"source_document":ADDENDUM_DOC, "source_kind":"historical_use_case_mapping", "canonicality":"provisional", "recovery_confidence":"high"}
        recipe_items.append(item)
        rows = "\n".join(f"| `{component}` | {role} |" for component, role in selections.items())
        inference = " This recipe is modern application guidance inferred from recovered mechanisms." if slug == "coding-debugging" else ""
        guidance = recovered_recipe_guidance.get(slug, "")
        write(f"recipes/{slug}.md", f"""
        # {name} Recipe

        R = required, A = automatically recommended, C = conditional, O = optional,
        X = normally exclude. These are recipe defaults, not universal truths.{inference}

        | Upgradeable | Class |
        |---|:---:|
        {rows}

        {guidance}

        ## Composition

        Frame and lock the task, establish explicit state, load evidence and behavior
        components, perform the task, then run applicable validators. Increase depth
        with risk; remove scaffolding that has no active trigger.

        ## Tests

        Test required activation, unnecessary-module exclusion, authority conflict,
        unsupported evidence, long-context continuation where applicable, and a
        strong-model configuration that preserves mandatory invariants.
        """)
    write_json("recipes/recipes.json", {"schema_version": "1.0.0", "recipes": recipe_items})
    links = "\n".join(f"- [{item['display_name']}]({item['slug']}.md)" for item in recipe_items)
    write("recipes/README.md", f"""
    # Skill Recipe Index

    Recipes classify component defaults as required (R), automatically recommended
    (A), conditional (C), optional (O), or normally excluded (X). They are starting
    points; apply each component's trigger and remove needless scaffolding.

    {links}
    """)


def domain_and_implementations() -> None:
    recovered_details = {
        "appeal-caf-os": """Recovered user architecture: `GLOBAL OS -> INTAKE / CLASSIFICATION OS -> FAMILY OS -> BLUEPRINT -> authorized policy/regulatory/evidence references -> output`. Intake classifies and emits an explicit routing object; it does not draft or override the Global OS. Recovered Intake Decision Object fields include `task_type`, `appeal_family`, `clinical_or_technical`, and `encounter_model`; the complete historical field set is not recovered and must not be invented. Missing required values are marked `Not documented`, and routing to a reference folder does not establish that its contents apply. Separate intake and drafting calls preserve scoped loading and retrieval/decision separation.""",
        "research-decision-os": """Recovered order: Kernel/StateBlock; Research Intake and Corpus Map; Evidence Cards; Conceptual Mapping; explicit Variables/Criteria/MCDM; Synthesis and Plan Builder. User-set weights never override a hard constraint or veto. Tier-3 validation concentrates on factual claims, citations, and safety-critical tradeoffs. Output includes the decision, phased implementation, risks, and monitoring.""",
        "paper-author-os": """Recovered flow: atomize supplied sources into claims, definitions, mechanisms, quotes, connections, and drift-sensitive areas; separate factual/evaluative/framing/hypothetical phases; generate and compare two or three plans; build paragraphs from topic, evidence, and connection; run one or two bounded local refinements; then require global coherence, citation fidelity, task/style acceptance, and safety before commitment.""",
        "local-chat-analysis-author-os": """Direct recovered user specification defines an offline `chat -> structured analysis -> source-grounded paper` system that is privacy-first, memory-aware, structurally rigorous, evidence-bounded, and citation-safe. It must distinguish user-authored content, assistant-authored content, external sources, and system synthesis. Core state includes goal, subgoals, constraints, decisions, and next steps, with memory heartbeats and drift checks.""",
        "multi-os": """Recovered architecture lets isolated reasoning OS modules consume authorized projections of one shared explicit StateBlock. Modules do not merge rules or authority domains; an orchestrator reconciles outputs. LROS remains unresolved even though its historical use as a state consumer was recovered.""",
    }
    for identifier, slug, name, purpose in DOMAIN_OS:
        write(f"domain-os/{slug}.md", f"""
        # {name}

        **Source ID:** `{identifier}`

        {purpose}

        {recovered_details.get(slug, '')}

        This is a model-agnostic composition example, not a single Upgradeable or an
        always-on prompt. It selects task-specific Genes, authorized Cores, explicit
        state, and risk-appropriate Upgradeables/validators. Domain and mode isolation
        prevent rule leakage. Any absent policy or domain detail remains absent; this
        public seed does not infer private organization content.
        """)
    domain_evidence = {
        "appeal-caf-os": ("direct_user_spec", "accepted", "high"),
        "local-chat-analysis-author-os": ("direct_user_spec", "accepted", "high"),
        "research-decision-os": ("direct_user_spec", "provisional", "high"),
        "paper-author-os": ("direct_user_spec", "provisional", "high"),
        "multi-os": ("historical_assistant_artifact", "provisional", "medium"),
    }
    write_json("domain-os/index.json", {"schema_version":"1.0.0", "domain_os":[
        {"id":identifier, "slug":slug, "display_name":name, "purpose":purpose,
         "historical_aliases":["LCA-OS"] if slug == "local-chat-analysis-author-os" else [],
         "path":f"domain-os/{slug}.md", "source_kind":domain_evidence.get(slug, ("current_consolidated_catalog", "canonical", "high"))[0],
         "canonicality":domain_evidence.get(slug, ("current_consolidated_catalog", "canonical", "high"))[1],
         "recovery_confidence":domain_evidence.get(slug, ("current_consolidated_catalog", "canonical", "high"))[2],
         "detail_source_kind":"historical_assistant_artifact" if slug in {"research-decision-os", "paper-author-os"} else domain_evidence.get(slug, ("current_consolidated_catalog", "canonical", "high"))[0],
         "detail_canonicality":"provisional" if slug in recovered_details else "canonical"} for identifier, slug, name, purpose in DOMAIN_OS
    ] + [{"id":"META-OS-HIST", "slug":"meta-os-builder", "display_name":"Meta-OS / OS-Builder", "purpose":"Compose new OS architectures from explicit primitives and assembly rules.", "historical_aliases":[], "path":"domain-os/meta-os-builder.md", "source_kind":"direct_user_spec", "canonicality":"provisional", "recovery_confidence":"medium", "template_source_kind":"historical_assistant_artifact", "template_canonicality":"provisional"}]})
    write("domain-os/meta-os-builder.md", """
    # Meta-OS / OS-Builder

    **Evidence:** direct-user goal; historical implementation template remains
    provisional.

    The recovered goal was to teach primitives, mechanics, assembly rules, and worked
    examples so a system could construct new OSs and OS-builders. A useful curriculum
    is `primitives -> mechanics -> architecture -> meta-assembly -> generativity`.
    Candidate output includes a kernel, layered architecture, primary/alternative/debug
    pipelines, module map, selected Upgradeables, worked example, and tests. This is an
    architecture recipe, not self-modification or authority over host policy.
    """)
    write("implementations/README.md", """
    # Implementation Adapters

    The specification is model-agnostic. These folders map it to host instructions,
    state schemas, validators, scripts, references, agent graphs, and Skill packages.
    Adapter behavior may evolve without rewriting canonical Upgradeable identity.
    Implement only capabilities the host actually provides.
    """)
    write("implementations/generic/README.md", """
    # Generic Adapter

    Map task identity and invariant controls to highest-authority instructions; map
    behavior to focused task instructions; Cores to versioned references; StateBlock
    to a typed object or durable store; validators to read-only checks; deterministic
    operations to scripts; and orchestrators to explicit state transitions or graphs.
    Preserve package versions and emit which components actually activated.
    """)
    write("implementations/openai/README.md", """
    # OpenAI Adapter Note

    A modern Skill package may use `SKILL.md` plus optional `references/`, `scripts/`,
    and `assets/`. Translate a complete task workflow into a Skill; do not create one
    Skill folder per Upgradeable automatically. Keep the main file concise, put deep
    Cores/references outside it, and retain host/system policy precedence. Confirm
    current platform requirements before publishing an adapter.
    """)
    for provider in ("anthropic", "google", "local-models"):
        name = provider.replace("-", " ").title()
        write(f"implementations/{provider}/README.md", f"""
        # {name} Adapter Framework

        This placeholder defines no provider capability. Contributors should map the
        model-agnostic contract to documented host instructions, tools, state,
        validators, and packaging; cite the applicable platform version and never
        claim persistence, parallelism, or safety authority the host does not provide.
        """)
    write("implementations/github-copilot/README.md", """
    # GitHub Copilot / Document-Based Adapter

    Use explicit repository documents and deterministic load order: global/project
    instructions, intake/task classification, task-specific Skill or domain OS,
    output blueprint, then selected references. Store state in visible files or host
    facilities. Prefer scoped hooks over rigid “say only” prompts, and do not assume
    self-modification, hidden memory, or unavailable orchestration. The repository's
    `.github/copilot-instructions.md` is the discovery entrypoint.
    """)
    write("implementations/community/README.md", """
    # Community Skill Implementations

    Community members may contribute complete task-oriented Skill packages here or in
    provider folders. Each implementation must list the registry slugs/versions it
    composes, its host compatibility, activation boundary, state contract, failure
    behavior, tests, and source provenance. Provider-specific packages are adapters;
    they do not redefine canonical Upgradeables.
    """)
    write("implementations/community/source-bounded-research/SKILL.md", """
    ---
    name: source-bounded-research
    description: Analyze a supplied source corpus and produce cited findings; use when conclusions must remain traceable to provided sources, not for unsourced creative writing.
    ---

    # Source-Bounded Research

    Lock the research question, source boundary, deliverable, and citation style. Use
    the Deep Summary or Compare-Contrast Gene when applicable; load an authorized Core
    only if domain knowledge is required. Compose `task-set-lock-in@1.0.0`,
    `scoped-loader@1.0.0`, `stateblock@1.0.0`, `grounding-no-invention@1.0.0`, and
    `citation-fidelity@1.0.0`; add other research-recipe components only when triggered.

    Capture evidence with provenance before synthesis. Separate fact, inference,
    framing, and hypothesis. For each material citation, check that the cited passage
    supports the attached claim. Return findings, limitations, and unresolved evidence
    conflicts. Never fabricate a source, quote, or missing fact.

    Tests: reject unsupported citations; stay inactive for unsourced creative writing;
    preserve the research question across a long corpus; let host policy override every
    component; omit optional scaffolding on a simple one-source lookup.
    """)

    write("upgradeables/README.md", """
    # Operational Upgradeables

    Packages are grouped by their primary functional class. Each directory contains
    canonical `metadata.yaml`, human-readable `UPGRADEABLE.md`, an example, and
    composition tests. Use `registry/registry.json` for search across all groups.
    Categories are organizational; `functional_classes` is the authoritative
    multi-valued taxonomy.
    """)


def archive_and_indexes() -> None:
    for stale in (ROOT / "registry/unresolved").glob("*.yaml"):
        stale.unlink()
    write("archive/README.md", """
    # Historical Archive

    The files under `source/` are immutable recovery/source artifacts copied from the
    user's canonical corpus. Operational registry entries may normalize names into
    slugs, but historical names and registry-generation boundaries remain preserved.

    Unknown expansions and unrecovered family members are intentionally not guessed.
    A modern equivalence is a traceability decision, never a retroactive rename. Use
    `SOURCE_TO_REGISTRY_MAP.md` to audit dispositions and `registry/unresolved/` for
    structured gaps. The archive remains authoritative for what was recovered even as
    operational packages evolve.

    `build-spec/` preserves the latest repository-build handoff separately from the
    source corpus because it governs construction rather than historical content.
    """)
    historical = []
    for name in HISTORICAL_T1:
        historical.append({
            "historical_id": name, "display_name": name,
            "registry_generation": "frozen-t1-core-v1-2025-11-28",
            "recovery_status": "exact_recovery", "disposition": "historical_only",
            "source_document": HISTORY_DOC,
        })
    for identifier, name in HISTORICAL_T2:
        historical.append({
            "historical_id": identifier, "display_name": name,
            "registry_generation": "frozen-t2-master-2025-11-28",
            "recovery_status": "exact_recovery", "disposition": "historical_only",
            "source_document": HISTORY_DOC,
        })
    for acronym, name, purpose in LEGACY_OS:
        historical.append({
            "historical_id": acronym, "display_name": name,
            "registry_generation": "legacy-reasoning-os",
            "recovery_status": "exact_recovery", "disposition": "historical_only",
            "recovered_purpose": purpose, "source_document": HISTORY_DOC,
        })
    historical.extend([
        {"historical_id":"GLOBAL-OS", "display_name":"GLOBAL OS", "registry_generation":"historical-domain-os", "recovery_status":"family_recovery", "disposition":"historical_only", "source_document":HISTORY_DOC},
        {"historical_id":"INTAKE-OS", "display_name":"INTAKE OS", "registry_generation":"historical-domain-os", "recovery_status":"family_recovery", "disposition":"historical_only", "source_document":HISTORY_DOC},
        {"historical_id":"OPMN-FAMILY-OS", "display_name":"OPMN Family OS", "registry_generation":"historical-domain-os", "recovery_status":"family_recovery", "disposition":"historical_only", "source_document":HISTORY_DOC},
        {"historical_id":"OPMN-BLUEPRINT", "display_name":"OPMN Blueprint", "registry_generation":"historical-domain-os", "recovery_status":"family_recovery", "disposition":"historical_only", "source_document":HISTORY_DOC},
        {"historical_id":"CAF-ROUTING", "display_name":"CAF routing: IPMN/IPTA/OPMN/OPTA/READM/GMN", "registry_generation":"historical-domain-os", "recovery_status":"family_recovery", "disposition":"historical_only", "source_document":HISTORY_DOC},
    ])
    for family in ["Safety", "Reasoning", "Retrieval / Context", "Memory / Anchoring", "Scaffolding", "Multi-Agent / Supervision", "Governance", "Monitoring / Drift"]:
        historical.append({"historical_id":f"family:{re.sub(r'[^a-z0-9]+', '-', family.lower()).strip('-')}", "display_name":family, "registry_generation":"frozen-t1-core-v1-2025-11-28", "recovery_status":"family_recovery", "disposition":"historical_only", "source_document":HISTORY_DOC})
    frozen_t2_families = [
        ("T2-001..007", "Neuro-Focus", 7, "family_recovery"),
        ("T2-008..015", "Creative / Exploration", 8, "exact_recovery"),
        ("T2-016..023", "Stability / Suppression", 8, "exact_recovery"),
        ("T2-024..030", "CRISPR Micro-Editing", 7, "family_recovery"),
        ("T2-031..037", "Surgical Macro-Editing", 7, "exact_recovery"),
        ("T2-038..043", "Resonance / Coherence", 6, "family_recovery"),
        ("T2-044..046", "Duration / Intensity", 3, "family_recovery"),
        ("T2-047..049", "Energy / Efficiency", 3, "family_recovery"),
        ("T2-050..052", "Immune / Anti-Contamination", 3, "family_recovery"),
        ("T2-053..056", "Interpersonal / Tone", 4, "family_recovery"),
        ("T2-057..060", "Consciousness Layer", 4, "family_recovery"),
        ("T2-061..067", "Supervisor / Orchestration", 7, "family_recovery"),
    ]
    for identifier, family, count, status in frozen_t2_families:
        historical.append({"historical_id":identifier, "display_name":family, "member_count":count, "registry_generation":"frozen-t2-master-2025-11-28", "recovery_status":status, "disposition":"historical_only", "source_document":HISTORY_DOC})
    for name in ("Primary Scaffolding", "Micro-Scaffolding"):
        historical.append({"historical_id":f"classification:{name.lower().replace('-', '_').replace(' ', '_')}", "display_name":name, "registry_generation":"training-scaffolding-2026-01-05", "recovery_status":"family_recovery", "disposition":"historical_only", "source_document":HISTORY_DOC})
    prefreeze_records = []
    for identifier, purpose in PREFREEZE_T1:
        record = {"historical_id":identifier, "display_name":identifier, "registry_generation":"t1-pre-freeze-library-2025-11-28", "recovery_status":"historical_artifact", "disposition":"historical_only", "recovered_purpose":purpose, "source_document":ADDENDUM_DOC, "source_kind":"historical_assistant_artifact", "canonicality":"provisional", "recovery_confidence":"medium", "index_path":"registry/historical/t1-pre-freeze-library/index.yaml"}
        if identifier in {"EXPLAINABILITY_SNAPSHOT_T1", "HEALTH_SNAPSHOT_ENGINE_T1"}:
            record["known_gap"] = "The complete original snapshot schema was not recovered."
        prefreeze_records.append(record)
        historical.append(record)
    write_json("registry/historical/t1-pre-freeze-library/index.yaml", {"schema_version":"1.0.0", "records":prefreeze_records, "warning":"These are pre-freeze library items; frozen membership is not established."})

    resonance_records = []
    for identifier, name, purpose, mapping in RESONANCE_T2:
        record = {"historical_id":identifier, "display_name":name, "registry_generation":"frozen-t2-master-2025-11-28", "recovery_status":"exact_recovery", "disposition":"historical_only", "recovered_purpose":purpose, "modern_relationship":mapping, "source_document":ADDENDUM_DOC, "source_kind":"direct_user_spec", "canonicality":"provisional", "recovery_confidence":"high", "identity_source_kind":"direct_user_spec", "identity_canonicality":"accepted", "operational_detail_source_kind":"historical_assistant_artifact", "operational_detail_canonicality":"provisional", "index_path":"registry/historical/frozen-t2-resonance/index.yaml"}
        resonance_records.append(record)
        historical.append(record)
    write_json("registry/historical/frozen-t2-resonance/index.yaml", {"schema_version":"1.0.0", "records":resonance_records})

    supervisor_records = []
    for identifier, name in SUPERVISOR_T2:
        record = {"historical_id":identifier, "display_name":name, "registry_generation":"frozen-t2-master-2025-11-28", "recovery_status":"historical_artifact", "disposition":"historical_only", "source_document":ADDENDUM_DOC, "source_kind":"historical_assistant_artifact", "canonicality":"provisional", "recovery_confidence":"medium", "notes":"Name mapping is not independently corroborated; do not infer a historical mechanism from the name.", "index_path":"registry/historical/frozen-t2-supervisor-provisional/index.yaml"}
        supervisor_records.append(record)
        historical.append(record)
    write_json("registry/historical/frozen-t2-supervisor-provisional/index.yaml", {"schema_version":"1.0.0", "records":supervisor_records})

    recovered_role_enrichment = {
        "GLOBAL_LOCAL_ANCHOR_SPLIT_T1":"Separate global/project invariants from task-local anchors.",
        "UPGRADEABLE_ACTIVATION_TIERS_T1":"Classify historical activation levels such as core, pack, and experimental.",
        "RULE_INDEX_OS_T1":"Provide a source-of-truth rule index for discovery, IDs, routing, and scoped loading.",
        "DRIFT_MONITOR_T1":"Observe movement away from active constraints, rules, or target behavior.",
        "EXECUTION_LOG_OS_T1":"Record execution actions for auditability and debugging.",
    }
    for record in historical:
        frozen = record["registry_generation"].startswith("frozen-")
        if record["historical_id"] in recovered_role_enrichment:
            record["recovered_purpose"] = recovered_role_enrichment[record["historical_id"]]
            record["additional_context_source"] = ADDENDUM_DOC
            record["operational_detail_source_kind"] = "historical_assistant_artifact"
            record["operational_detail_canonicality"] = "provisional"
        record.setdefault("source_date", "2026-09-03")
        record.setdefault("source_kind", "user_accepted" if frozen else "historical_recovery_inventory")
        record.setdefault("canonicality", "accepted" if frozen else "historical_only")
        record.setdefault("recovery_confidence", "high" if record["recovery_status"] == "exact_recovery" else "medium")
        record.setdefault("historical_aliases", [])
        record.setdefault("supersedes", [])
        record.setdefault("superseded_by", [])
    write_json("registry/historical/t1-pre-freeze-library/index.yaml", {"schema_version":"1.0.0", "records":prefreeze_records, "warning":"These are pre-freeze library items; frozen membership is not established."})
    write_json("registry/historical/frozen-t2-resonance/index.yaml", {"schema_version":"1.0.0", "records":resonance_records})
    write_json("registry/historical/frozen-t2-supervisor-provisional/index.yaml", {"schema_version":"1.0.0", "records":supervisor_records})
    write_json("registry/historical/index.yaml", {"schema_version":"1.0.0", "records":historical})
    for slug, name, gap in UNRESOLVED:
        source_ids = {"ocg":"T2-13", "intent-task-framing-controller":"T2-14B", "ecl-drift-sink":"T2-15", "bounded-exit-acronym":"T2-01"}
        record = {
            "schema_version": "1.0.0", "slug": slug, "display_name": name,
            "recovery_status": "unresolved", "lifecycle_status": "historical",
            "operational_status": "archival_only", "known_gap": gap,
            "source_document": HISTORY_DOC,
            "source_id": source_ids.get(slug, "not individually recovered"),
            "source_date": "2026-09-03", "source_kind":"historical_recovery_inventory",
            "canonicality":"unresolved", "recovery_confidence":"low",
            "supersedes":[], "superseded_by":[],
            "resolution_requirements": ["documented proposal", "source provenance", "maintainer review"],
        }
        if slug == "intent-task-framing-controller":
            record.update({"legacy_acronym":"ITFC", "collision_namespace":"itfc-intent-task-framing", "distinct_from":"image-text-fidelity-capture"})
        write_json(f"registry/unresolved/{slug}.yaml", record)
    # Human-readable unresolved index.
    unresolved_rows = "\n".join(f"| `{slug}` | {name} | {gap} |" for slug, name, gap in UNRESOLVED)
    write("registry/unresolved/README.md", f"""
    # Unresolved Recovery Records

    These records are archival-only. They have no operational procedure and cannot
    be activated until an evidence-backed proposal resolves them.

    | Slug | Recovered label | Known gap |
    |---|---|---|
    {unresolved_rows}
    """)
    write("registry/current/README.md", """
    # Current Registry

    Canonical operational metadata lives beside each package under `upgradeables/`.
    The top-level registry files are deterministic indexes built from those files.
    """)
    write("registry/historical/README.md", """
    # Historical Index

    `index.yaml` preserves exact-name and family-only records that are not promoted to
    current operational packages. IDs are meaningful only inside their declared
    registry generation.
    """)

    lines = [
        "# Source-to-Registry Map", "",
        "This append-oriented ledger records how recovered items were normalized.", "",
        "| Source name | Source ID | Registry generation | Recovery | Modern slug / destination | Disposition |",
        "|---|---|---|---|---|---|",
    ]
    for item in ENTRIES:
        lines.append(f"| {item['display_name']} | `{item['id']}` | `{item['registry_generation']}` | `{item['recovery_status']}` | [`{item['slug']}`](../{item['package_path']}) | operationalized |")
        for historical_id in item["historical_ids"]:
            lines.append(f"| {item['display_name']} cross-reference | `{historical_id}` | source-specific | `{item['recovery_status']}` | [`{item['slug']}`](../{item['package_path']}) | alias |")
    lines.append("| Singularity Cores | `A-03` | consolidated-2026-09 | `exact_recovery` | [`cores/`](../cores/) | merged-as-framework |")
    for identifier, slug, name, purpose in QMS_MODES:
        lines.append(f"| {name} | `{identifier}` | consolidated-2026-09 | `exact_recovery` | [`{slug}`](../bundles/qms/QMS_VARIANTS.md) | merged-as-mode |")
    for identifier, slug, name, purpose in GENES:
        lines.append(f"| {name} | `{identifier}` | consolidated-2026-09 | `exact_recovery` | [`{slug}`](../genes/examples/{slug}.md) | behavior-gene |")
    for identifier, slug, name, purpose in CORES:
        lines.append(f"| {name} | `{identifier}` | consolidated-2026-09 | `exact_recovery` | [`{slug}`](../cores/examples/{slug}.md) | core-reference |")
    for identifier, slug, name, purpose in DOMAIN_OS:
        lines.append(f"| {name} | `{identifier}` | consolidated-2026-09 | `exact_recovery` | [`{slug}`](../domain-os/{slug}.md) | bundled |")
    lines.append("| Meta-OS / OS-Builder | `META-OS-HIST` | deep-recovery-2026-09 | `mixed A/B evidence` | [`meta-os-builder`](../domain-os/meta-os-builder.md) | bundled-provisional |")
    for record in historical:
        destination = record.get("index_path", "registry/historical/index.yaml")
        lines.append(f"| {record['display_name']} | `{record['historical_id']}` | `{record['registry_generation']}` | `{record['recovery_status']}` | [`{destination}`](../{destination}) | {record['disposition']} |")
    for slug, name, gap in UNRESOLVED:
        lines.append(f"| {name} | not fully recovered | source-specific | `unresolved` | [`{slug}`](../registry/unresolved/{slug}.yaml) | unresolved |")
    write("archive/SOURCE_TO_REGISTRY_MAP.md", "\n".join(lines))


def schema_docs() -> None:
    common_status = {
        "recovery": ["exact_recovery", "partial_recovery", "family_recovery", "historical_artifact", "unresolved", "modern_inference"],
        "lifecycle": ["historical", "unresolved", "experimental", "candidate", "stable", "core", "deprecated"],
        "activation": ["U0-foundational", "U1-common-conditional", "U2-specialized", "U3-high-risk-expensive", "U4-meta-architecture"],
    }
    upgradeable_schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": "https://upgradeables.dev/schema/upgradeable.schema.json",
        "title": "Upgradeable metadata", "type": "object",
        "required": ["schema_version", "id", "slug", "display_name", "version", "registry_generation", "recovery_status", "lifecycle_status", "tiers", "functional_classes", "activation_class", "implementation_forms", "purpose", "triggers", "non_triggers", "requires", "recommended_with", "counterbalances", "potentially_redundant_with", "conflicts", "inputs", "outputs", "strong_model_scaling", "failure_boundary", "supersedes", "superseded_by", "package_path", "provenance"],
        "properties": {
            "slug": {"type":"string", "pattern":"^[a-z0-9]+(?:-[a-z0-9]+)*$", "minLength":1},
            "id": {"type":"string", "minLength":1},
            "display_name": {"type":"string", "minLength":1},
            "version": {"type":"string", "pattern":"^\\d+\\.\\d+\\.\\d+$"},
            "recovery_status": {"enum":common_status["recovery"]},
            "lifecycle_status": {"enum":common_status["lifecycle"]},
            "activation_class": {"enum":common_status["activation"]},
            "functional_classes": {"type":"array", "minItems":1, "uniqueItems":True, "items":{"enum":FUNCTIONAL_CLASSES}},
            "package_path": {"type":"string", "pattern":"^upgradeables/.+/UPGRADEABLE\\.md$"},
            "strong_model_scaling": {"type":"object", "required":["may_skip", "keep_mandatory"]},
        },
        "additionalProperties": True,
    }
    for key in ("schema_version", "id", "display_name", "version", "registry_generation", "activation_class", "purpose", "package_path"):
        upgradeable_schema["properties"].setdefault(key, {"type":"string", "minLength":1})
    for key in ("historical_ids", "historical_aliases", "tiers", "functional_classes", "implementation_forms", "recommended_skill_types", "usually_not_needed_for", "triggers", "non_triggers", "requires", "recommended_with", "counterbalances", "potentially_redundant_with", "conflicts", "inputs", "outputs", "failure_boundary", "supersedes", "superseded_by"):
        upgradeable_schema["properties"].setdefault(key, {"type":"array", "items":{"type":"string"}, "uniqueItems":True})
    upgradeable_schema["properties"]["provenance"] = {"type":"object", "required":["source_document", "source_id", "source_date", "source_kind", "canonicality", "recovery_confidence", "notes"], "properties":{"source_kind":{"enum":["direct_user_spec","user_accepted","historical_assistant_artifact","current_consolidated_catalog","historical_recovery_inventory","modern_implementation_recommendation"]}, "canonicality":{"enum":["canonical","accepted","provisional","historical_only","unresolved"]}, "recovery_confidence":{"enum":["high","medium","low"]}}}
    bundle_schema = {
        "$schema":"https://json-schema.org/draft/2020-12/schema", "title":"Bundle metadata", "type":"object",
        "required":["schema_version","slug","display_name","version","purpose","components","load_order"],
        "properties":{"schema_version":{"type":"string"}, "slug":{"type":"string","pattern":"^[a-z0-9]+(?:-[a-z0-9]+)*$"}, "display_name":{"type":"string","minLength":1}, "version":{"type":"string","pattern":"^\\d+\\.\\d+\\.\\d+$"}, "purpose":{"type":"string","minLength":1}, "components":{"type":"array","minItems":1,"uniqueItems":True,"items":{"type":"string"}}, "load_order":{"type":"array","minItems":1,"items":{"type":"string"}}},
    }
    recipe_schema = {
        "$schema":"https://json-schema.org/draft/2020-12/schema", "title":"Recipe metadata", "type":"object",
        "required":["schema_version","slug","display_name","version","purpose","classifications"],
        "properties":{"schema_version":{"type":"string"}, "slug":{"type":"string","pattern":"^[a-z0-9]+(?:-[a-z0-9]+)*$"}, "display_name":{"type":"string","minLength":1}, "version":{"type":"string","pattern":"^\\d+\\.\\d+\\.\\d+$"}, "purpose":{"type":"string","minLength":1}, "classifications":{"type":"object","minProperties":1,"additionalProperties":{"enum":["R","A","C","O","X"]}}},
    }
    write_json("registry/schema/upgradeable.schema.json", upgradeable_schema)
    write_json("registry/schema/bundle.schema.json", bundle_schema)
    write_json("registry/schema/recipe.schema.json", recipe_schema)


def proposal_docs() -> None:
    write("proposals/README.md", """
    # Proposals

    Lifecycle: Idea -> Proposal -> Experimental -> Candidate -> Stable -> Core (rare).
    Terminal states include rejected, deprecated, archived, and historical. Begin from
    the proposal template and include prior art, mechanism, failure boundary, tests,
    implementation form, and provenance. Maintainer review is required for canonical
    registry changes.
    """)
    for folder in ("experimental", "candidate", "accepted", "rejected", "archived"):
        write(f"proposals/{folder}/.gitkeep", "")
    write("tools/README.md", """
    # Seed Build Tooling

    `bootstrap_repo.py` and `catalog_data.py` record the initial curated conversion.
    They overwrite generated seed content and require `--force`; do not use them for
    normal contributions. Edit canonical packages directly, then run the deterministic
    scripts under `scripts/` to rebuild indexes and artifacts.
    """)


def github_docs() -> None:
    write(".github/PULL_REQUEST_TEMPLATE.md", """
    ## Summary

    ## Checklist

    - [ ] I searched for duplicate concepts.
    - [ ] I compared against the closest existing Upgradeables.
    - [ ] I preserved provenance.
    - [ ] I did not invent unresolved historical definitions.
    - [ ] I added or updated tests.
    - [ ] I updated machine-readable metadata.
    - [ ] I documented conflicts and counterbalances.
    - [ ] I classified this as a primitive, mode, recipe, bundle, reference, or implementation.
    - [ ] I ran repository validation.
    """)
    write(".github/ISSUE_TEMPLATE/bug_report.yml", """
    name: Bug or specification inconsistency
    description: Report a defect in behavior, schema, tooling, or documentation
    title: "[Bug]: "
    labels: [bug]
    body:
      - type: input
        id: component
        attributes: {label: Affected component}
        validations: {required: true}
      - type: textarea
        id: expected
        attributes: {label: Expected behavior}
        validations: {required: true}
      - type: textarea
        id: observed
        attributes: {label: Observed problem}
        validations: {required: true}
      - type: input
        id: version
        attributes: {label: Version}
        validations: {required: true}
      - type: textarea
        id: correction
        attributes: {label: Proposed correction}
    """)
    write(".github/ISSUE_TEMPLATE/new_upgradeable.yml", """
    name: New Upgradeable proposal
    description: Propose a new composable primitive after checking prior art
    title: "[Proposal]: "
    labels: [proposal]
    body:
      - type: input
        id: name
        attributes: {label: Proposed name}
        validations: {required: true}
      - type: textarea
        id: problem
        attributes: {label: Problem solved}
        validations: {required: true}
      - type: textarea
        id: prior_art
        attributes: {label: Existing prior art and closest Upgradeables}
        validations: {required: true}
      - type: textarea
        id: composition
        attributes: {label: Why composition is insufficient}
        validations: {required: true}
      - type: textarea
        id: trigger
        attributes: {label: Trigger and non-trigger}
        validations: {required: true}
      - type: textarea
        id: mechanism
        attributes: {label: Explicit mechanism}
        validations: {required: true}
      - type: textarea
        id: boundary
        attributes: {label: Failure boundary}
        validations: {required: true}
      - type: textarea
        id: tests
        attributes: {label: Behavioral and composition tests}
        validations: {required: true}
      - type: dropdown
        id: form
        attributes:
          label: Recommended implementation form
          options: [Skill component, Parent-skill mode, Validator or guard, State schema or manager, Reference module, Deterministic script, Orchestrator, Bundle component]
        validations: {required: true}
    """)
    write(".github/ISSUE_TEMPLATE/documentation.yml", """
    name: Documentation or recipe contribution
    description: Improve a specification, recipe, or guide
    title: "[Docs]: "
    labels: [documentation]
    body:
      - type: input
        id: affected
        attributes: {label: Affected recipe or specification}
        validations: {required: true}
      - type: textarea
        id: rationale
        attributes: {label: Rationale}
        validations: {required: true}
      - type: textarea
        id: components
        attributes: {label: Upgradeables involved}
      - type: dropdown
        id: change_type
        attributes: {label: Change type, options: [Documentation only, Behavior change]}
        validations: {required: true}
    """)
    write(".github/ISSUE_TEMPLATE/new_skill.yml", """
    name: Community Skill implementation
    description: Propose a task-oriented Skill composed from registry entries
    title: "[Skill]: "
    labels: [implementation]
    body:
      - type: input
        id: name
        attributes: {label: Skill name}
        validations: {required: true}
      - type: textarea
        id: boundary
        attributes: {label: Task and activation boundary}
        validations: {required: true}
      - type: textarea
        id: components
        attributes: {label: Upgradeable slugs and versions}
        validations: {required: true}
      - type: textarea
        id: gene_core
        attributes: {label: Behavior Gene, Core, and source provenance}
      - type: textarea
        id: host
        attributes: {label: Host compatibility and state/tool requirements}
        validations: {required: true}
      - type: textarea
        id: tests
        attributes: {label: Tests and failure behavior}
        validations: {required: true}
    """)
    write(".github/copilot-instructions.md", """
    # Copilot instructions for Upgradeables

    Read `MODEL_CONSUMPTION_GUIDE.md`, the relevant specification, and
    `registry/registry.json` before proposing a component. Preserve Skill/Gene/Core/
    Upgradeable distinctions, registry generations, and unresolved gaps. Prefer
    composition to duplicate primitives. Run all repository validators after edits.
    """)
    write(".github/workflows/validate.yml", """
    name: Validate
    on:
      push:
      pull_request:
    permissions:
      contents: read
    jobs:
      validate:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4
          - uses: actions/setup-python@v5
            with:
              python-version: "3.12"
          - run: python scripts/build_registry.py --check
          - run: python scripts/validate_registry.py
          - run: python -m unittest discover -s tests -v
          - run: python scripts/build_all_in_one.py --check
          - run: python scripts/check_links.py
    """)


def tooling_and_tests() -> None:
    write("scripts/build_registry.py", r'''
    """Build deterministic top-level registries from package metadata."""
    from __future__ import annotations
    import argparse
    import json
    import sys
    from pathlib import Path

    ROOT = Path(__file__).resolve().parents[1]

    def load(path: Path):
        return json.loads(path.read_text(encoding="utf-8"))

    def payload():
        entries = [load(path) for path in ROOT.glob("upgradeables/*/*/metadata.yaml")]
        entries.sort(key=lambda item: item["slug"])
        historical = load(ROOT / "registry/historical/index.yaml")["records"]
        unresolved = [load(path) for path in ROOT.glob("registry/unresolved/*.yaml")]
        unresolved.sort(key=lambda item: item["slug"])
        recipes = load(ROOT / "recipes/recipes.json")["recipes"]
        return {
            "schema_version": "1.0.0",
            "registry_version": "0.1.0",
            "generated_from": "upgradeables/*/*/metadata.yaml",
            "source_corpus": [
                "archive/source/OS_Upgradeable_to_Skills_Translation_Catalog_v2_Recovery_Merged.md",
                "archive/source/OS_Upgradeables_Historical_Recovery_Inventory.md",
                "archive/source/OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md",
            ],
            "historical_source_precedence": [
                "direct_user_spec", "user_accepted", "historical_recovery_inventory",
                "current_consolidated_catalog", "historical_assistant_artifact",
                "modern_implementation_recommendation",
            ],
            "upgradeables": entries,
            "historical_records": historical,
            "unresolved_records": unresolved,
            "recipes": recipes,
            "qms_modes": load(ROOT / "registry/qms_modes.json")["modes"],
            "behavior_genes": load(ROOT / "genes/index.json")["behavior_genes"],
            "cores": load(ROOT / "cores/index.json")["cores"],
            "domain_os": load(ROOT / "domain-os/index.json")["domain_os"],
        }

    def render(data):
        # JSON is a strict YAML 1.2 subset: one deterministic serializer, two formats.
        return json.dumps(data, ensure_ascii=False, indent=2) + "\n"

    def main():
        parser = argparse.ArgumentParser()
        parser.add_argument("--check", action="store_true")
        args = parser.parse_args()
        expected = render(payload())
        targets = [ROOT / "registry/registry.yaml", ROOT / "registry/registry.json"]
        if args.check:
            stale = [str(path.relative_to(ROOT)) for path in targets if not path.exists() or path.read_text(encoding="utf-8") != expected]
            if stale:
                print("stale generated registry: " + ", ".join(stale), file=sys.stderr)
                return 1
            print(f"registry build check: OK ({len(payload()['upgradeables'])} operational entries)")
            return 0
        for path in targets:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(expected, encoding="utf-8", newline="\n")
        print(f"built registry with {len(payload()['upgradeables'])} operational entries")
        return 0

    if __name__ == "__main__":
        raise SystemExit(main())
    ''')
    write("scripts/validate_registry.py", r'''
    """Dependency-free semantic validation for the Upgradeables registry."""
    from __future__ import annotations
    import json
    import re
    import sys
    from pathlib import Path

    ROOT = Path(__file__).resolve().parents[1]
    ALLOWED_RECOVERY = {"exact_recovery", "partial_recovery", "family_recovery", "historical_artifact", "unresolved", "modern_inference"}
    ALLOWED_LIFECYCLE = {"historical", "unresolved", "experimental", "candidate", "stable", "core", "deprecated"}
    ALLOWED_ACTIVATION = {"U0-foundational", "U1-common-conditional", "U2-specialized", "U3-high-risk-expensive", "U4-meta-architecture"}
    ALLOWED_FUNCTIONS = {"framing-intake", "state", "context-retrieval", "planning-reasoning", "truth-grounding", "validation", "drift-control", "editing-repair", "output", "orchestration", "meta-control", "persistence"}
    ALLOWED_SOURCE_KINDS = {"direct_user_spec", "user_accepted", "historical_assistant_artifact", "current_consolidated_catalog", "historical_recovery_inventory", "modern_implementation_recommendation"}
    ALLOWED_CANONICALITY = {"canonical", "accepted", "provisional", "historical_only", "unresolved"}
    ALLOWED_CONFIDENCE = {"high", "medium", "low"}
    REQUIRED = {"id", "slug", "display_name", "version", "registry_generation", "recovery_status", "lifecycle_status", "tiers", "functional_classes", "activation_class", "implementation_forms", "purpose", "triggers", "non_triggers", "requires", "recommended_with", "counterbalances", "potentially_redundant_with", "conflicts", "inputs", "outputs", "strong_model_scaling", "failure_boundary", "supersedes", "superseded_by", "package_path", "provenance"}

    def load(path):
        return json.loads(path.read_text(encoding="utf-8"))

    def validate():
        errors = []
        yaml_data = load(ROOT / "registry/registry.yaml")
        json_data = load(ROOT / "registry/registry.json")
        if yaml_data != json_data:
            errors.append("registry YAML/JSON divergence")
        entries = json_data.get("upgradeables", [])
        slugs = [entry.get("slug") for entry in entries]
        ids = [entry.get("id") for entry in entries]
        if len(slugs) != len(set(slugs)):
            errors.append("duplicate canonical slug")
        if len(ids) != len(set(ids)):
            errors.append("duplicate canonical ID")
        known = set(slugs)
        aliases = {}
        for entry in entries:
            missing = REQUIRED - set(entry)
            if missing:
                errors.append(f"{entry.get('slug')}: missing {sorted(missing)}")
            slug = entry.get("slug", "")
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug):
                errors.append(f"{slug}: invalid slug")
            if entry.get("recovery_status") not in ALLOWED_RECOVERY:
                errors.append(f"{slug}: invalid recovery status")
            if entry.get("lifecycle_status") not in ALLOWED_LIFECYCLE:
                errors.append(f"{slug}: invalid lifecycle")
            if entry.get("activation_class") not in ALLOWED_ACTIVATION:
                errors.append(f"{slug}: invalid activation class")
            if not set(entry.get("functional_classes", [])) <= ALLOWED_FUNCTIONS:
                errors.append(f"{slug}: invalid functional class")
            package = ROOT / entry.get("package_path", "__missing__")
            raw_package = Path(entry.get("package_path", ""))
            if raw_package.is_absolute() or ".." in raw_package.parts:
                errors.append(f"{slug}: unsafe package path {entry.get('package_path')}")
            if not package.is_file():
                errors.append(f"{slug}: nonexistent package path {entry.get('package_path')}")
            metadata = package.parent / "metadata.yaml"
            if not metadata.is_file() or load(metadata) != entry:
                errors.append(f"{slug}: package metadata differs from registry")
            expected_package = metadata.parent / "UPGRADEABLE.md"
            if package.resolve() != expected_package.resolve():
                errors.append(f"{slug}: package path does not match metadata directory")
            for key in ("tiers", "functional_classes", "implementation_forms", "triggers", "non_triggers", "requires", "recommended_with", "counterbalances", "potentially_redundant_with", "conflicts", "inputs", "outputs", "failure_boundary"):
                if not isinstance(entry.get(key), list):
                    errors.append(f"{slug}: {key} must be an array")
            for key in ("display_name", "purpose", "registry_generation"):
                if not isinstance(entry.get(key), str) or not entry.get(key, "").strip():
                    errors.append(f"{slug}: {key} must be non-empty text")
            if not re.fullmatch(r"\d+\.\d+\.\d+", entry.get("version", "")):
                errors.append(f"{slug}: invalid semantic version")
            scaling = entry.get("strong_model_scaling")
            if not isinstance(scaling, dict) or not isinstance(scaling.get("may_skip"), list) or not isinstance(scaling.get("keep_mandatory"), list) or not scaling.get("keep_mandatory"):
                errors.append(f"{slug}: invalid strong_model_scaling")
            provenance = entry.get("provenance")
            provenance_keys = {"source_document", "source_id", "source_date", "source_kind", "canonicality", "recovery_confidence", "notes"}
            if not isinstance(provenance, dict) or not provenance_keys <= set(provenance):
                errors.append(f"{slug}: incomplete provenance metadata")
            elif provenance["source_kind"] not in ALLOWED_SOURCE_KINDS or provenance["canonicality"] not in ALLOWED_CANONICALITY or provenance["recovery_confidence"] not in ALLOWED_CONFIDENCE:
                errors.append(f"{slug}: invalid provenance classification")
            for key in ("requires", "recommended_with", "counterbalances", "potentially_redundant_with", "conflicts"):
                for ref in entry.get(key, []):
                    if ref not in known:
                        errors.append(f"{slug}: broken {key} reference {ref}")
            for alias in entry.get("historical_aliases", []):
                aliases.setdefault(alias.casefold(), set()).add(slug)
        for alias, owners in aliases.items():
            if len(owners) > 1:
                errors.append(f"ambiguous alias collision {alias}: {sorted(owners)}")

        for path in ROOT.glob("registry/unresolved/*.yaml"):
            record = load(path)
            if record.get("recovery_status") != "unresolved" or record.get("operational_status") != "archival_only":
                errors.append(f"{path.name}: unresolved record status invalid")
            forbidden = {"procedure", "mechanism", "triggers", "outputs"} & set(record)
            if forbidden:
                errors.append(f"{path.name}: unresolved record invents operational fields {sorted(forbidden)}")

        for path in ROOT.glob("bundles/*/metadata.yaml"):
            bundle = load(path)
            for key in ("slug", "display_name", "version", "purpose"):
                if not isinstance(bundle.get(key), str) or not bundle.get(key).strip():
                    errors.append(f"{path.parent.name}: invalid {key}")
            if not isinstance(bundle.get("components"), list) or not bundle.get("components"):
                errors.append(f"{path.parent.name}: components must be a non-empty array")
            for ref in bundle.get("components", []):
                if ref not in known:
                    errors.append(f"{path.parent.name}: unknown bundle component {ref}")
            if set(bundle.get("load_order", [])) != set(bundle.get("components", [])):
                errors.append(f"{path.parent.name}: load order/component mismatch")

        recipes = load(ROOT / "recipes/recipes.json")["recipes"]
        for recipe in recipes:
            if not isinstance(recipe.get("classifications"), dict) or not recipe.get("classifications"):
                errors.append(f"{recipe.get('slug')}: classifications must be a non-empty object")
            for ref, role in recipe.get("classifications", {}).items():
                if ref not in known:
                    errors.append(f"{recipe['slug']}: unknown recipe component {ref}")
                if role not in {"R", "A", "C", "O", "X"}:
                    errors.append(f"{recipe['slug']}: invalid recipe role {role}")
        # Explicit recovery invariants.
        unresolved_slugs = {item["slug"] for item in json_data.get("unresolved_records", [])}
        for slug in {"ocg", "ecl-drift-sink", "lros", "intent-task-framing-controller"}:
            if slug not in unresolved_slugs:
                errors.append(f"missing required unresolved record {slug}")
        itfc = next((item for item in entries if item["slug"] == "image-text-fidelity-capture"), None)
        if not itfc or "ITFC" not in itfc.get("historical_aliases", []):
            errors.append("Image Text Fidelity Capture does not preserve ITFC alias")
        return errors, len(entries), len(json_data.get("historical_records", [])), len(json_data.get("unresolved_records", []))

    def main():
        errors, operational, historical, unresolved = validate()
        if errors:
            print("registry validation: FAILED", file=sys.stderr)
            for error in errors:
                print("- " + error, file=sys.stderr)
            return 1
        print(f"registry validation: OK ({operational} operational, {historical} historical-only, {unresolved} unresolved records)")
        return 0

    if __name__ == "__main__":
        raise SystemExit(main())
    ''')
    write("scripts/validate_upgradeable.py", r'''
    """Validate one JSON-compatible metadata.yaml package."""
    import json
    import re
    import sys
    from pathlib import Path

    def main():
        if len(sys.argv) != 2:
            print("usage: validate_upgradeable.py path/to/metadata.yaml", file=sys.stderr)
            return 2
        path = Path(sys.argv[1])
        data = json.loads(path.read_text(encoding="utf-8"))
        required = {"id", "slug", "display_name", "version", "registry_generation", "recovery_status", "lifecycle_status", "functional_classes", "activation_class", "implementation_forms", "purpose", "triggers", "non_triggers", "requires", "recommended_with", "counterbalances", "potentially_redundant_with", "conflicts", "inputs", "outputs", "strong_model_scaling", "failure_boundary", "supersedes", "superseded_by", "package_path", "provenance"}
        missing = required - set(data)
        array_fields = {"functional_classes", "implementation_forms", "triggers", "non_triggers", "requires", "recommended_with", "counterbalances", "potentially_redundant_with", "conflicts", "inputs", "outputs", "failure_boundary", "supersedes", "superseded_by"}
        bad_arrays = sorted(key for key in array_fields if not isinstance(data.get(key), list))
        bad = bool(missing or bad_arrays or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", data.get("slug", "")) or not re.fullmatch(r"\d+\.\d+\.\d+", data.get("version", "")))
        if bad:
            print(f"invalid metadata; missing={sorted(missing)} bad_arrays={bad_arrays}", file=sys.stderr)
            return 1
        print(f"{data['slug']}: OK")
        return 0
    if __name__ == "__main__":
        raise SystemExit(main())
    ''')
    write("scripts/build_all_in_one.py", r'''
    """Build the portable all-in-one kit from canonical repository content."""
    from __future__ import annotations
    import argparse
    import json
    import sys
    from pathlib import Path

    ROOT = Path(__file__).resolve().parents[1]
    TARGET = ROOT / "dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md"

    def render():
        sections = [
            "# All-in-One Upgradeable Skill Kit\n\n> Generated file. Edit canonical repository content, not this artifact.\n",
        ]
        for path in ["spec/OS_PHILOSOPHY.md", "spec/UPGRADEABLE_SPEC.md", "spec/COMPOSITION_SPEC.md", "spec/PRECEDENCE_SPEC.md", "spec/SKILL_TRANSLATION_SPEC.md"]:
            sections.append((ROOT / path).read_text(encoding="utf-8"))
        sections.append("# Skill Recipe Matrix\n")
        recipes = json.loads((ROOT / "recipes/recipes.json").read_text(encoding="utf-8"))["recipes"]
        for recipe in recipes:
            roles = ", ".join(f"{slug}={role}" for slug, role in recipe["classifications"].items())
            sections.append(f"## {recipe['display_name']}\n\n{roles}\n")
        sections.append("# Recovered Recipe Procedures\n")
        for path in ["recipes/deterministic-intake-routing.md", "recipes/long-context-source-fidelity.md"]:
            sections.append((ROOT / path).read_text(encoding="utf-8"))
        sections.append((ROOT / "bundles/qms/OPERATING_RULES.md").read_text(encoding="utf-8"))
        sections.append("# Domain OS Examples\n")
        for path in sorted((ROOT / "domain-os").glob("*.md")):
            sections.append(path.read_text(encoding="utf-8"))
        registry = json.loads((ROOT / "registry/registry.json").read_text(encoding="utf-8"))
        sections.append("# Current Registry Summaries\n")
        for item in registry["upgradeables"]:
            sections.append(f"## {item['display_name']} (`{item['slug']}`)\n\n{item['purpose']}\n\n- ID: `{item['id']}`\n- Activation: `{item['activation_class']}`\n- Classes: {', '.join(item['functional_classes'])}\n- Forms: {', '.join(item['implementation_forms'])}\n- Package: `{item['package_path']}`\n")
        sections.append("# Deep-Recovery Historical Index\n")
        for item in registry["historical_records"]:
            if item.get("source_document") == "OS_Upgradeables_Deep_Context_Recovery_Addendum_2026-09-03.md" or item.get("additional_context_source"):
                sections.append(f"- **{item['display_name']}** (`{item['historical_id']}`, `{item['registry_generation']}`): {item.get('recovered_purpose', item.get('notes', 'historical record'))} Canonicality: `{item['canonicality']}`; source kind: `{item['source_kind']}`.\n")
        sections.append((ROOT / "spec/RECOVERY_AND_PROVENANCE_SPEC.md").read_text(encoding="utf-8"))
        sections.append("# Unresolved Records\n")
        for item in registry["unresolved_records"]:
            sections.append(f"- **{item['display_name']}** (`{item['slug']}`): {item['known_gap']} Status: archival-only.\n")
        return "\n---\n\n".join(section.strip() for section in sections) + "\n"

    def main():
        parser = argparse.ArgumentParser()
        parser.add_argument("--check", action="store_true")
        args = parser.parse_args()
        expected = render()
        if args.check:
            if not TARGET.exists() or TARGET.read_text(encoding="utf-8") != expected:
                print("all-in-one artifact is stale", file=sys.stderr)
                return 1
            print("all-in-one build check: OK")
            return 0
        TARGET.parent.mkdir(parents=True, exist_ok=True)
        TARGET.write_text(expected, encoding="utf-8", newline="\n")
        print(f"built {TARGET.relative_to(ROOT)}")
        return 0
    if __name__ == "__main__":
        raise SystemExit(main())
    ''')
    write("scripts/check_links.py", r'''
    """Check local Markdown links without network access."""
    from __future__ import annotations
    import re
    from pathlib import Path

    ROOT = Path(__file__).resolve().parents[1]
    LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)]+)\)")

    def main():
        broken = []
        checked = 0
        for document in ROOT.rglob("*.md"):
            if ".git" in document.parts:
                continue
            text = document.read_text(encoding="utf-8")
            for raw in LINK.findall(text):
                target = raw.strip().split()[0].strip("<>")
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                path_part = target.split("#", 1)[0]
                if not path_part:
                    continue
                checked += 1
                resolved = (document.parent / path_part).resolve()
                try:
                    resolved.relative_to(ROOT.resolve())
                except ValueError:
                    broken.append(f"{document.relative_to(ROOT)} -> {target} (escapes repository)")
                    continue
                if not resolved.exists():
                    broken.append(f"{document.relative_to(ROOT)} -> {target}")
        if broken:
            print("broken internal links:")
            for item in broken:
                print("- " + item)
            return 1
        print(f"internal link check: OK ({checked} links)")
        return 0
    if __name__ == "__main__":
        raise SystemExit(main())
    ''')

    write("tests/test_registry.py", r'''
    import json
    import unittest
    from pathlib import Path
    ROOT = Path(__file__).resolve().parents[1]
    class RegistryTests(unittest.TestCase):
        @classmethod
        def setUpClass(cls):
            cls.data = json.loads((ROOT / "registry/registry.json").read_text(encoding="utf-8"))
        def test_populated(self):
            self.assertGreaterEqual(len(self.data["upgradeables"]), 70)
        def test_package_paths(self):
            for item in self.data["upgradeables"]:
                self.assertTrue((ROOT / item["package_path"]).is_file(), item["slug"])
        def test_dependencies_resolve(self):
            known = {item["slug"] for item in self.data["upgradeables"]}
            for item in self.data["upgradeables"]:
                for key in ("requires", "recommended_with", "counterbalances", "potentially_redundant_with", "conflicts"):
                    self.assertLessEqual(set(item[key]), known)
    ''')
    write("tests/test_schema.py", r'''
    import json
    import subprocess
    import sys
    import unittest
    from pathlib import Path
    ROOT = Path(__file__).resolve().parents[1]
    class SchemaTests(unittest.TestCase):
        def test_schema_files_are_valid_json(self):
            for path in (ROOT / "registry/schema").glob("*.json"):
                data = json.loads(path.read_text(encoding="utf-8"))
                self.assertEqual(data["type"], "object")
                self.assertIn("required", data)
        def test_every_metadata_has_required_schema_keys(self):
            required = set(json.loads((ROOT / "registry/schema/upgradeable.schema.json").read_text(encoding="utf-8"))["required"])
            for path in ROOT.glob("upgradeables/*/*/metadata.yaml"):
                self.assertLessEqual(required, set(json.loads(path.read_text(encoding="utf-8"))), str(path))
        def test_invalid_fixture_is_rejected(self):
            result = subprocess.run([sys.executable, "scripts/validate_upgradeable.py", "tests/fixtures/invalid_metadata.json"], cwd=ROOT, capture_output=True, text=True)
            self.assertNotEqual(result.returncode, 0)
    ''')
    write("tests/test_unique_ids.py", r'''
    import re
    import json
    import unittest
    from pathlib import Path
    ROOT = Path(__file__).resolve().parents[1]
    class IdentityTests(unittest.TestCase):
        def test_unique_ids_and_slugs(self):
            items = json.loads((ROOT / "registry/registry.json").read_text(encoding="utf-8"))["upgradeables"]
            self.assertEqual(len(items), len({x["id"] for x in items}))
            self.assertEqual(len(items), len({x["slug"] for x in items}))
        def test_registry_generations_separate(self):
            data = json.loads((ROOT / "registry/registry.json").read_text(encoding="utf-8"))
            members = [x for x in data["historical_records"] if x["registry_generation"] == "frozen-t2-master-2025-11-28" and re.fullmatch(r"T2-\d{3}", x["historical_id"])]
            original = [x for x in members if x["source_document"] == "OS_Upgradeables_Historical_Recovery_Inventory.md"]
            resonance = [x for x in members if x["source_kind"] == "direct_user_spec"]
            provisional = [x for x in members if x["source_kind"] == "historical_assistant_artifact"]
            self.assertEqual((len(original), len(resonance), len(provisional)), (23, 6, 7))
            self.assertTrue(all(x["canonicality"] == "provisional" for x in provisional))
        def test_deep_recovery_does_not_fill_frozen_t1_gaps(self):
            data = json.loads((ROOT / "registry/registry.json").read_text(encoding="utf-8"))
            prefreeze = [x for x in data["historical_records"] if x["registry_generation"] == "t1-pre-freeze-library-2025-11-28"]
            self.assertEqual(len(prefreeze), 13)
            self.assertTrue(all(x["canonicality"] == "provisional" for x in prefreeze))
            unresolved = {x["slug"] for x in data["unresolved_records"]}
            self.assertNotIn("frozen-t2-resonance-members", unresolved)
            self.assertNotIn("frozen-t2-supervisor-members", unresolved)
    ''')
    write("tests/test_alias_collisions.py", r'''
    import json
    import unittest
    from pathlib import Path
    ROOT = Path(__file__).resolve().parents[1]
    class AliasTests(unittest.TestCase):
        def test_operational_aliases_are_unambiguous(self):
            items = json.loads((ROOT / "registry/registry.json").read_text(encoding="utf-8"))["upgradeables"]
            owners = {}
            for item in items:
                for alias in item["historical_aliases"]:
                    owners.setdefault(alias.casefold(), set()).add(item["slug"])
            self.assertFalse({alias: values for alias, values in owners.items() if len(values) > 1})
        def test_itfc_collision_is_split(self):
            data = json.loads((ROOT / "registry/registry.json").read_text(encoding="utf-8"))
            current = {x["slug"]: x for x in data["upgradeables"]}
            unresolved = {x["slug"]: x for x in data["unresolved_records"]}
            self.assertIn("ITFC", current["image-text-fidelity-capture"]["historical_aliases"])
            self.assertIn("intent-task-framing-controller", unresolved)
            self.assertEqual(unresolved["intent-task-framing-controller"]["operational_status"], "archival_only")
    ''')
    write("tests/test_build_all_in_one.py", r'''
    import subprocess
    import sys
    import unittest
    from pathlib import Path
    ROOT = Path(__file__).resolve().parents[1]
    class BuildTests(unittest.TestCase):
        def test_registry_is_reproducible(self):
            result = subprocess.run([sys.executable, "scripts/build_registry.py", "--check"], cwd=ROOT)
            self.assertEqual(result.returncode, 0)
        def test_all_in_one_is_reproducible(self):
            result = subprocess.run([sys.executable, "scripts/build_all_in_one.py", "--check"], cwd=ROOT)
            self.assertEqual(result.returncode, 0)
        def test_all_in_one_has_core_sections(self):
            text = (ROOT / "dist/ALL_IN_ONE_UPGRADEABLE_SKILL_KIT.md").read_text(encoding="utf-8")
            for heading in ("OS Philosophy", "Upgradeable Specification", "Skill Recipe Matrix", "Current Registry Summaries", "Unresolved Records"):
                self.assertIn(heading, text)
    ''')
    write("tests/test_archive_integrity.py", r'''
    import hashlib
    import unittest
    from pathlib import Path
    ROOT = Path(__file__).resolve().parents[1]
    class ArchiveTests(unittest.TestCase):
        def test_archived_sources_match_manifest(self):
            for line in (ROOT / "archive/SOURCE_SHA256SUMS").read_text(encoding="utf-8").splitlines():
                digest, relative = line.split("  ", 1)
                actual = hashlib.sha256((ROOT / relative).read_bytes()).hexdigest()
                self.assertEqual(digest, actual, relative)
    ''')
    write("tests/test_markdown_rendering.py", r'''
    import re
    import unittest
    from pathlib import Path
    ROOT = Path(__file__).resolve().parents[1]
    class MarkdownRenderingTests(unittest.TestCase):
        def test_generated_headings_are_not_code_indented(self):
            targets = list(ROOT.glob("upgradeables/*/*/UPGRADEABLE.md")) + list((ROOT / "recipes").glob("*.md")) + list((ROOT / "bundles").glob("*/README.md"))
            bad = []
            for path in targets:
                for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                    if re.match(r" {4,}#{1,6} ", line):
                        bad.append(f"{path.relative_to(ROOT)}:{number}")
            self.assertFalse(bad, "indented headings render as code: " + ", ".join(bad[:20]))
    ''')
    write_json("tests/fixtures/invalid_metadata.json", {"id":"BAD", "slug":"Not Valid", "version":"one", "triggers":"wrong type"})


def build_manifest_and_report() -> None:
    import hashlib
    source_paths = [
        ROOT / "archive/source" / SOURCE_DOC,
        ROOT / "archive/source" / HISTORY_DOC,
        ROOT / "archive/source" / ADDENDUM_DOC,
        ROOT / "archive/build-spec" / BUILD_SPEC_DOC,
    ]
    manifest = []
    for path in source_paths:
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        manifest.append(f"{digest}  {path.relative_to(ROOT).as_posix()}")
    write("archive/SOURCE_SHA256SUMS", "\n".join(manifest))
    historical_count = len(json.loads((ROOT / "registry/historical/index.yaml").read_text(encoding="utf-8"))["records"])
    write("archive/BUILD_REPORT.md", f"""
    # Initial Conversion Report

    - Operational Upgradeable packages: {len(ENTRIES)}
    - Historical-only index records: {historical_count}
    - Explicit unresolved records: {len(UNRESOLVED)}
    - Behavior Gene seed descriptors: {len(GENES)}
    - Core seed descriptors: {len(CORES)}
    - Domain OS examples: {len(DOMAIN_OS) + 1}
    - QMS modes retained under one parent: {len(QMS_MODES)}

    The frozen 2025 registry generations remain separate from the 2026 consolidated
    IDs. Deep Recovery Pass 2.0 adds provenance classes, pre-freeze T1 records, exact
    T2-038..043 names, provisional T2-061..067 names, and deeper operating references.
    Sparse records are not padded with invented mechanisms. ITFC is split, and
    OCG/ECL/LROS/ExIt expansion remain unresolved.
    """)


def run_builds() -> None:
    import subprocess
    import sys
    subprocess.run([sys.executable, str(ROOT / "scripts/build_registry.py")], cwd=ROOT, check=True)
    subprocess.run([sys.executable, str(ROOT / "scripts/build_all_in_one.py")], cwd=ROOT, check=True)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Destructively regenerate the initial seed repository.")
    parser.add_argument("--force", action="store_true", help="acknowledge overwrite of generated seed content")
    args = parser.parse_args()
    if not args.force:
        raise SystemExit("Refusing to overwrite seed content without --force. See tools/README.md.")
    root_docs()
    spec_docs()
    templates()
    package_docs()
    genes_and_cores()
    qms_and_bundles()
    recipe_docs()
    domain_and_implementations()
    archive_and_indexes()
    schema_docs()
    proposal_docs()
    github_docs()
    tooling_and_tests()
    build_manifest_and_report()
    run_builds()
