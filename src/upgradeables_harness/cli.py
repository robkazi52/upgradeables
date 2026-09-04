"""Command-line interface for the Upgradeables project harness."""
from __future__ import annotations

import argparse
import importlib
import json
import os
import sys
from pathlib import Path

from .constants import HARNESS_VERSION
from .registry.load import load_manifest
from .resolver.explain import render_task
from .resolver.task import resolve_task


def _runtime_resolution(args):
    if args.resolution:
        return json.loads(Path(args.resolution).read_text(encoding="utf-8"))
    if not args.task:
        raise ValueError("provide task text or --resolution <json-file>")
    project = _find_project(args.project) if not args.no_project_profile else None
    return resolve_task(args.task, project=project, use_project_profile=not args.no_project_profile)


def command_runtime(args):
    from .runtime import RuntimeContext, compile as compile_runtime
    from .runtime.data import load_model_profiles
    from .runtime.render import render_plan

    if args.runtime_command == "profiles":
        profiles = load_model_profiles()["profiles"]
        if args.format == "json":
            print(json.dumps({"schema_version": "1.0.0", "profiles": profiles}, indent=2))
        else:
            for name, profile in profiles.items():
                print(f"{name}: {profile['default_level']} — {profile['description']}")
        return 0
    resolution = _runtime_resolution(args)
    project = _find_project(args.project) if not args.no_project_profile else None
    runtime_config = {}
    if project is not None:
        config_path = project / ".upgradeables" / "config.json"
        if config_path.is_file():
            runtime_config = json.loads(config_path.read_text(encoding="utf-8")).get("runtime", {})
    model_profile = args.model_profile or runtime_config.get("default_model_profile", "medium")
    max_directive_tokens = args.max_directive_tokens
    if max_directive_tokens is None:
        max_directive_tokens = runtime_config.get("max_directive_tokens", 500)
    context = RuntimeContext.from_value({
        "model_profile": model_profile,
        "max_directive_tokens": max_directive_tokens,
    })
    plan = compile_runtime(resolution, context)
    json_output = args.format == "json" or args.runtime_command == "plan"
    if json_output:
        print(json.dumps(plan, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        print(render_plan(plan, explain=args.runtime_command == "explain" or args.explain or args.format == "debug"), end="")
    return 0


def command_run(args):
    if args.run_adapter != "ollama":
        raise ValueError(f"unsupported run adapter: {args.run_adapter}")
    from .runtime.adapters.ollama import run_ollama

    project = _find_project(args.project) if not args.no_project_profile else None
    runtime_config = {}
    if project is not None:
        config_path = project / ".upgradeables" / "config.json"
        if config_path.is_file():
            runtime_config = json.loads(config_path.read_text(encoding="utf-8")).get("runtime", {})
    model_profile = args.model_profile or runtime_config.get("default_model_profile", "medium")
    max_directive_tokens = args.max_directive_tokens
    if max_directive_tokens is None:
        max_directive_tokens = runtime_config.get("max_directive_tokens", 500)
    base_instructions = args.base_instructions
    if args.base_instructions_file:
        base_instructions = Path(args.base_instructions_file).read_text(encoding="utf-8")
    options = json.loads(args.options_json) if args.options_json else {}
    if not isinstance(options, dict):
        raise ValueError("--options-json must contain a JSON object")

    result = run_ollama(
        model=args.model,
        task=args.task,
        endpoint=args.endpoint,
        project=project,
        model_profile=model_profile,
        max_directive_tokens=max_directive_tokens,
        base_instructions=base_instructions,
        options=options,
        timeout=args.timeout,
        output_root=args.output_root,
        dry_run=args.dry_run,
        use_project_profile=not args.no_project_profile,
    )
    if args.dry_run or args.format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    else:
        response = result["response"] or {}
        if response.get("response_text"):
            print(response["response_text"])
        if response.get("error"):
            print(
                f"upgradeables: Ollama {response['error']['kind']}: {response['error']['message']}",
                file=sys.stderr,
            )
        print(f"Artifacts: {result['artifact_directory']}", file=sys.stderr)
        for warning in result["runtime_plan"].get("warnings", []):
            print(f"Runtime warning: {warning}", file=sys.stderr)
    if args.dry_run:
        return 0
    response = result["response"] or {}
    return 1 if response.get("error") or response.get("partial") else 0


def command_eval(args):
    from .runtime.evals.report import summarize, write_report
    from .runtime.evals.runner import mock_adapter, prepare_experiment, run_experiment
    from .runtime.evals.suites import list_suites, load_suite

    if args.eval_command == "list-suites":
        suites = list_suites()
        if args.json:
            print(json.dumps({"suites": suites}, indent=2))
        else:
            for item in suites:
                print(f"{item['slug']}: {item['description']}")
        return 0
    if args.eval_command == "inspect-suite":
        suite = load_suite(args.slug)
        if args.json:
            print(json.dumps(suite, indent=2, sort_keys=True))
        else:
            print(f"{suite['slug']}: {suite['description']}")
            print(f"License: {suite['license']}")
            for item in suite["tasks"]:
                print(f"- {item['id']} [{item['family']}]")
        return 0
    if args.eval_command == "run":
        from .runtime.adapters.generic import AdapterRequestError, endpoint_type
        from .runtime.adapters.ollama import discover as discover_ollama
        from .runtime.evals.live import (
            create_live_adapter,
            validate_api_key_environment,
            validate_endpoint_origin,
        )

        adapter_name = args.adapter
        api_key = None
        endpoint = None
        if adapter_name == "mock":
            if args.model or args.endpoint or args.api_key_env:
                raise ValueError("--model, --endpoint, and --api-key-env are live-adapter options")
            model_id = "deterministic-fixture"
            evaluation_evidence = "mock"
            adapter = mock_adapter
        else:
            if not args.model:
                raise ValueError("live evaluation requires --model with an exact model identifier")
            endpoint_value = args.endpoint
            if endpoint_value is None and adapter_name == "ollama":
                endpoint_value = "http://127.0.0.1:11434"
            if endpoint_value is None:
                raise ValueError("openai-compatible evaluation requires an explicit --endpoint origin")
            endpoint = validate_endpoint_origin(endpoint_value, adapter_name)
            key_environment = validate_api_key_environment(args.api_key_env)
            if key_environment is not None:
                if adapter_name != "openai-compatible":
                    raise ValueError("--api-key-env is supported only for openai-compatible evaluation")
                api_key = os.environ.get(key_environment)
                if not api_key:
                    raise ValueError("configured API key environment variable is missing or empty")
            model_id = args.model
            location = endpoint_type(endpoint)
            evaluation_evidence = "local" if location in {"loopback", "private-network"} else "api"
            adapter = create_live_adapter(
                adapter_name,
                model=model_id,
                endpoint=endpoint,
                api_key=api_key,
                timeout=args.timeout,
            )
        experiment_id = args.experiment_id or f"{args.slug}-{adapter_name}"
        model_record = {"adapter": adapter_name, "model": model_id}
        if endpoint is not None:
            model_record.update({
                "endpoint_origin": endpoint,
                "endpoint_type": endpoint_type(endpoint),
            })
        manifest = {
            "schema_version": "1.0.0",
            "experiment_id": experiment_id,
            "suite": args.slug,
            "conditions": args.conditions,
            "model": model_record,
            "trials_per_task": args.trials,
            "temperature": 0,
            "seed_policy": "deterministic-mock" if adapter_name == "mock" else "provider-controlled-no-retry",
            "grader": "objective",
            "order_seed": args.order_seed,
            "model_profile": args.model_profile,
            "max_directive_tokens": args.max_directive_tokens,
            "generation_parameters": {"temperature": 0, "stream": False},
            "evaluation_evidence": evaluation_evidence,
            "network_policy": (
                "none" if adapter_name == "mock" else
                "explicit-read-only-preflight-then-single-attempts" if adapter_name == "ollama" else
                "explicit-single-attempts-no-preflight"
            ),
            "retry_policy": "none",
            "timeout_seconds": args.timeout if adapter_name != "mock" else None,
            "estimated_cost": {
                "value": None,
                "currency": None,
                "availability": "unavailable",
                "reason": "no verified provider pricing metadata is available",
            },
        }
        preview = prepare_experiment(manifest)
        if args.dry_run:
            output = {
                "status": "dry-run",
                "network_performed": False,
                "writes_performed": False,
                "adapter": adapter_name,
                "model_id": model_id,
                "endpoint_origin": endpoint,
                "task_ids": preview["task_ids"],
                "conditions": preview["manifest"]["conditions"],
                "trials_per_task": args.trials,
                "request_count_planned": preview["manifest"]["request_count_planned"],
                "fixed_resolution_availability": preview["fixed_resolution_availability"],
                "estimated_cost": preview["manifest"]["estimated_cost"],
                "configuration_hash": preview["manifest"]["configuration_hash"],
                "manifest": preview["manifest"],
            }
            if args.json:
                print(json.dumps(output, ensure_ascii=False, indent=2, sort_keys=True))
            else:
                print("Dry run: no network requests or experiment writes performed.")
                print(f"Suite: {args.slug}")
                print(f"Adapter: {adapter_name}")
                print(f"Model: {model_id}")
                if endpoint:
                    print(f"Endpoint: {endpoint}")
                print(f"Tasks: {len(preview['task_ids'])}")
                print(
                    f"Conditions ({len(preview['manifest']['conditions'])}): "
                    f"{', '.join(preview['manifest']['conditions'])}"
                )
                print(f"Trials per task: {args.trials}")
                print(f"Planned model requests: {preview['manifest']['request_count_planned']}")
                fixed = preview["fixed_resolution_availability"]
                print(f"Fixed resolutions: {fixed['available']}/{len(preview['task_ids'])} available")
                print("Estimated cost: unavailable")
                print(f"Configuration hash: {preview['manifest']['configuration_hash']}")
            return 0
        expected_target = Path(args.output_root) / experiment_id
        if expected_target.exists():
            raise FileExistsError(f"experiment directory already exists: {expected_target}")
        if adapter_name == "ollama":
            try:
                discovery = discover_ollama(
                    endpoint,
                    model_id,
                    timeout=min(args.timeout, 10),
                )
            except AdapterRequestError as error:
                raise ValueError(
                    f"Ollama preflight failed: {error.error['kind']}: {error.error['message']}"
                ) from error
            model_available = discovery["model_available"]["status"]
            if model_available != "supported":
                raise ValueError(
                    f"Ollama preflight failed: exact model {model_id!r} is not available; "
                    "install it explicitly before starting the experiment"
                )
            manifest["preflight"] = {
                "adapter": "ollama",
                "endpoint_type": discovery["endpoint_type"],
                "server_version": discovery["server_version"],
                "model_id": model_id,
                "model_available": model_available,
            }
        target = run_experiment(manifest, adapter, args.output_root)
        if args.json:
            completed = json.loads((target / "manifest.json").read_text(encoding="utf-8"))
            print(json.dumps({
                "experiment_directory": str(target),
                "manifest_hash": completed["manifest_hash"],
                "request_count_planned": completed["request_count_planned"],
                "request_count_completed": completed["request_count_completed"],
            }, indent=2, sort_keys=True))
        else:
            print(target)
        return 0

    target = Path(args.experiment)
    manifest_path = target / "manifest.json"
    results_path = target / "raw-results.jsonl"
    if not manifest_path.is_file() or not results_path.is_file():
        raise ValueError(f"not an evaluation experiment directory: {target}")
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    results = [json.loads(line) for line in results_path.read_text(encoding="utf-8").splitlines() if line]
    if args.eval_command == "report":
        summary = write_report(target, manifest, results)
    else:
        other = Path(args.experiment_b)
        other_results_path = other / "raw-results.jsonl"
        if not other_results_path.is_file():
            raise ValueError(f"not an evaluation experiment directory: {other}")
        other_results = [json.loads(line) for line in other_results_path.read_text(encoding="utf-8").splitlines() if line]
        summary_a = summarize(results)
        summary_b = summarize(other_results)
        summary = {
            "run_a": {"path": str(target), "summary": summary_a},
            "run_b": {"path": str(other), "summary": summary_b},
            "comparison_scope": "descriptive; verify matched manifests before causal interpretation",
        }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


def _lazy(module: str, function: str, args):
    try:
        handler = getattr(importlib.import_module(module), function)
    except (ImportError, AttributeError) as error:
        print(f"Command implementation unavailable: {module}.{function}: {error}", file=sys.stderr)
        return 2
    result = handler(args)
    return 0 if result is None else int(result)


def _find_project(start: str | None):
    if start:
        return Path(start)
    current = Path.cwd().resolve()
    for candidate in (current, *current.parents):
        if (candidate / ".upgradeables" / "project.json").is_file():
            return candidate
    return None


def command_task(args):
    project = _find_project(args.project) if not args.no_project_profile else None
    result = resolve_task(args.task, project=project,
                          use_project_profile=not args.no_project_profile)
    if args.record:
        if project is None:
            print("Task recording requires an initialized project; run `upgradeables init` first.", file=sys.stderr)
            return 2
        try:
            history = importlib.import_module("upgradeables_harness.skills.history")
            component_groups = (
                "required_by_recipe", "trigger_likely", "conditional", "optional",
                "needs_agent_evaluation",
            )
            event = {
                "raw_task": result["query"],
                "normalized_task": result["normalized_task"],
                "task_archetype": result["task"]["archetype"],
                "selected_recipe": result["best_recipe"]["slug"] if result["best_recipe"] else None,
                "candidate_components": [
                    item["slug"] for key in component_groups for item in result[key]
                ],
                "environment_modifiers": {
                    key: value for key, value in result["environment"].items() if value is not None
                },
                "authority_mode": "review" if result["environment"].get("review_only") else (
                    "edit" if result["environment"].get("editing_requested") else "unspecified"
                ),
                "component_composition": [
                    f"{item['slug']}@{item['version']}"
                    for item in result["required_by_recipe"] + result["trigger_likely"]
                ],
            }
            history.record_task_event(project, event, explicitly_requested=True)
        except (ImportError, AttributeError) as error:
            print(f"Task recording unavailable: {error}", file=sys.stderr)
            return 2
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        sys.stdout.write(render_task(result, explain=args.explain))
    return 0


def command_version(args):
    manifest = load_manifest()
    project = _find_project(args.project)
    lock_version = None
    if project:
        lock = project / ".upgradeables" / "lock.json"
        if lock.is_file():
            try:
                lock_version = json.loads(lock.read_text(encoding="utf-8")).get("registry_version")
            except (OSError, json.JSONDecodeError):
                lock_version = "invalid"
    result = {
        "harness_version": HARNESS_VERSION,
        "bundled_registry_version": manifest["registry_version"],
        "aggregate_registry_schema_version": manifest["aggregate_registry_schema_version"],
        "component_schema_version": manifest["component_schema_version"],
        "registry_commit": manifest["source_commit"],
        "project_lock": lock_version,
    }
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Upgradeables Harness: {result['harness_version']}")
        print(f"Bundled registry: {result['bundled_registry_version']}")
        print(f"Registry schemas: aggregate {result['aggregate_registry_schema_version']}; components {result['component_schema_version']}")
        print(f"Registry commit: {result['registry_commit']}")
        print(f"Project lock: {result['project_lock'] or 'none'}")
    return 0


def command_update(args):
    if args.apply:
        print("Registry update apply is not implemented in v0.4.0; pinned projects were not changed.", file=sys.stderr)
        return 2
    if not args.check:
        print("Use `upgradeables update --check`; network access is explicit.", file=sys.stderr)
        return 2
    from .registry.update import check_for_update
    try:
        result = check_for_update()
    except Exception as error:  # Network and protocol failures become explicit CLI errors.
        print(f"Registry update check failed: {error}", file=sys.stderr)
        return 1
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"Bundled registry: {result['current_registry_version']}")
        print(f"Remote registry: {result['remote_registry_version']}")
        print("Update available." if result["update_available"] else "No registry update detected.")
    return 0


def build_parser():
    parser = argparse.ArgumentParser(prog="upgradeables", description="Local-first Upgradeables project harness")
    parser.add_argument("--version", action="version", version=f"%(prog)s {HARNESS_VERSION}")
    commands = parser.add_subparsers(dest="command", required=True)

    init = commands.add_parser("init", help="initialize a project-local harness")
    init.add_argument("path", nargs="?")
    init.add_argument("--profile")
    init.add_argument("--no-detect", action="store_true")
    depth = init.add_mutually_exclusive_group()
    depth.add_argument("--minimal", action="store_true")
    depth.add_argument("--standard", action="store_true")
    depth.add_argument("--full", action="store_true")
    init.add_argument("--force", action="store_true")
    init.add_argument("--json", action="store_true")
    init.set_defaults(handler=lambda a: _lazy("upgradeables_harness.harness.init", "command_init", a))

    inspect = commands.add_parser("inspect", help="inspect project signals without executing code")
    inspect.add_argument("--project")
    inspect.add_argument("--json", action="store_true")
    inspect.set_defaults(handler=lambda a: _lazy("upgradeables_harness.project.inspect", "command_inspect", a))

    recommend = commands.add_parser("recommend", help="show project-level selection priors")
    recommend.add_argument("--project")
    recommend.add_argument("--json", action="store_true")
    recommend.set_defaults(handler=lambda a: _lazy("upgradeables_harness.project.profile", "command_recommend", a))

    task = commands.add_parser("task", help="resolve a natural-language task deterministically")
    task.add_argument("task")
    task.add_argument("--json", action="store_true")
    task.add_argument("--explain", action="store_true")
    task.add_argument("--project")
    task.add_argument("--no-project-profile", action="store_true")
    task.add_argument("--record", action="store_true")
    task.set_defaults(handler=command_task)

    runtime = commands.add_parser("runtime", help="compile selected Upgradeables into runtime controls")
    runtime_commands = runtime.add_subparsers(dest="runtime_command", required=True)
    for name in ("compile", "explain", "plan"):
        runtime_parser = runtime_commands.add_parser(name)
        runtime_parser.add_argument("task", nargs="?")
        runtime_parser.add_argument("--resolution")
        runtime_parser.add_argument("--project")
        runtime_parser.add_argument("--model-profile", choices=("small", "medium", "strong", "auto", "custom"))
        runtime_parser.add_argument("--max-directive-tokens", type=int)
        runtime_parser.add_argument("--format", choices=("text", "json", "agent-instructions", "debug"), default="text")
        runtime_parser.add_argument("--explain", action="store_true")
        runtime_parser.add_argument("--no-project-profile", action="store_true")
        runtime_parser.set_defaults(handler=command_runtime)
    profiles = runtime_commands.add_parser("profiles")
    profiles.add_argument("--format", choices=("text", "json"), default="text")
    profiles.set_defaults(handler=command_runtime)

    run = commands.add_parser("run", help="explicitly execute a compiled runtime plan")
    run_adapters = run.add_subparsers(dest="run_adapter", required=True)
    run_ollama = run_adapters.add_parser("ollama", help="run one task through native Ollama chat")
    run_ollama.add_argument("--model", required=True)
    run_ollama.add_argument("--task", required=True)
    run_ollama.add_argument("--endpoint", default="http://127.0.0.1:11434")
    run_ollama.add_argument("--project")
    run_ollama.add_argument("--model-profile", choices=("small", "medium", "strong", "auto", "custom"))
    run_ollama.add_argument("--max-directive-tokens", type=int)
    base = run_ollama.add_mutually_exclusive_group()
    base.add_argument("--base-instructions")
    base.add_argument("--base-instructions-file")
    run_ollama.add_argument("--options-json", help="Ollama options as one JSON object")
    run_ollama.add_argument("--timeout", type=float, default=60)
    run_ollama.add_argument("--output-root", default=".upgradeables/runs")
    run_ollama.add_argument("--dry-run", action="store_true")
    run_ollama.add_argument("--format", choices=("text", "json"), default="text")
    run_ollama.add_argument("--no-project-profile", action="store_true")
    run_ollama.set_defaults(handler=command_run)

    evaluation = commands.add_parser("eval", help="run offline-first runtime evaluations")
    eval_commands = evaluation.add_subparsers(dest="eval_command", required=True)
    list_eval = eval_commands.add_parser("list-suites")
    list_eval.add_argument("--json", action="store_true")
    list_eval.set_defaults(handler=command_eval)
    inspect_eval = eval_commands.add_parser("inspect-suite")
    inspect_eval.add_argument("slug")
    inspect_eval.add_argument("--json", action="store_true")
    inspect_eval.set_defaults(handler=command_eval)
    run_eval = eval_commands.add_parser("run")
    run_eval.add_argument("slug")
    run_eval.add_argument("--adapter", choices=("mock", "ollama", "openai-compatible"), default="mock")
    run_eval.add_argument("--model")
    run_eval.add_argument("--endpoint")
    run_eval.add_argument("--api-key-env")
    run_eval.add_argument("--timeout", type=float, default=60)
    run_eval.add_argument("--dry-run", action="store_true")
    run_eval.add_argument("--json", action="store_true")
    run_eval.add_argument("--experiment-id")
    run_eval.add_argument("--output-root", default=".evals/upgradeables")
    run_eval.add_argument(
        "--conditions", nargs="+",
        choices=("baseline", "static-full", "adaptive-fixed-resolution", "adaptive-end-to-end", "adaptive-runtime"),
        default=["baseline", "static-full", "adaptive-end-to-end"],
    )
    run_eval.add_argument("--trials", type=int, default=1)
    run_eval.add_argument("--order-seed", type=int, default=0)
    run_eval.add_argument("--model-profile", choices=("small", "medium", "strong", "auto", "custom"), default="medium")
    run_eval.add_argument("--max-directive-tokens", type=int, default=500)
    run_eval.set_defaults(handler=command_eval)
    eval_report = eval_commands.add_parser("report")
    eval_report.add_argument("experiment")
    eval_report.set_defaults(handler=command_eval)
    eval_compare = eval_commands.add_parser("compare")
    eval_compare.add_argument("experiment")
    eval_compare.add_argument("experiment_b")
    eval_compare.set_defaults(handler=command_eval)

    skill = commands.add_parser("skill", help="project Skill factory")
    skills = skill.add_subparsers(dest="skill_command", required=True)
    brief = skills.add_parser("brief")
    brief.add_argument("task")
    brief.add_argument("--project")
    brief.add_argument("--json", action="store_true")
    brief.set_defaults(handler=lambda a: _lazy("upgradeables_harness.skills.brief", "command_brief", a))
    scaffold = skills.add_parser("scaffold")
    scaffold.add_argument("slug")
    scaffold.add_argument("--task")
    scaffold.add_argument("--project")
    scaffold.add_argument("--force", action="store_true")
    scaffold.add_argument("--json", action="store_true")
    scaffold.set_defaults(handler=lambda a: _lazy("upgradeables_harness.skills.scaffold", "command_scaffold", a))
    listing = skills.add_parser("list")
    listing.add_argument("--project")
    listing.add_argument("--json", action="store_true")
    listing.set_defaults(handler=lambda a: _lazy("upgradeables_harness.skills.scaffold", "command_list", a))
    validate = skills.add_parser("validate")
    validate.add_argument("path")
    validate.add_argument("--draft", action="store_true")
    validate.add_argument("--json", action="store_true")
    validate.set_defaults(handler=lambda a: _lazy("upgradeables_harness.skills.validate", "command_validate", a))
    suggest = skills.add_parser("suggest")
    suggest.add_argument("--project")
    suggest.add_argument("--json", action="store_true")
    suggest.set_defaults(handler=lambda a: _lazy("upgradeables_harness.skills.suggest", "command_suggest", a))

    integrate = commands.add_parser("integrate", help="preview or manage agent instruction fragments")
    integrate.add_argument("provider", choices=("list", "codex", "claude", "copilot", "generic"))
    integrate.add_argument("--project")
    writes = integrate.add_mutually_exclusive_group()
    writes.add_argument("--write", action="store_true")
    writes.add_argument("--remove", action="store_true")
    integrate.add_argument("--json", action="store_true")
    integrate.set_defaults(handler=lambda a: _lazy("upgradeables_harness.agents.base", "command_integrate", a))

    doctor = commands.add_parser("doctor", help="diagnose project harness state")
    doctor.add_argument("--project")
    doctor.add_argument("--fix", action="store_true")
    doctor.add_argument("--json", action="store_true")
    doctor.set_defaults(handler=lambda a: _lazy("upgradeables_harness.harness.doctor", "command_doctor", a))

    update = commands.add_parser("update", help="explicitly check registry releases")
    update_mode = update.add_mutually_exclusive_group()
    update_mode.add_argument("--check", action="store_true")
    update_mode.add_argument("--apply", action="store_true")
    update.add_argument("--json", action="store_true")
    update.set_defaults(handler=command_update)

    version = commands.add_parser("version", help="show harness and registry versions")
    version.add_argument("--project")
    version.add_argument("--json", action="store_true")
    version.set_defaults(handler=command_version)
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.handler(args)
    except (OSError, ValueError, json.JSONDecodeError) as error:
        if getattr(args, "json", False):
            print(json.dumps({"error": str(error), "command": args.command}), file=sys.stderr)
        else:
            print(f"upgradeables: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
