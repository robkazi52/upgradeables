"""Descriptive, limitation-preserving evaluation reports."""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from statistics import median

from .conditions import canonical_condition


def summarize(results: list[dict]) -> dict:
    grouped = defaultdict(list)
    alias_seen = False
    for item in results:
        condition = canonical_condition(item["condition"])
        alias_seen = alias_seen or item["condition"] == "adaptive-runtime"
        grouped[condition].append(item)
    conditions = {}
    task_scores = defaultdict(lambda: defaultdict(list))
    for condition, items in sorted(grouped.items()):
        graded = [item for item in items if item["grade"].get("status", "graded") == "graded"]
        successes = sum(item["grade"]["success"] is True for item in graded)
        for item in graded:
            task_scores[condition][item["task_id"]].append(float(item["grade"]["score"]))
        conditions[condition] = {
            "observations": len(items),
            "graded_observations": len(graded),
            "ungraded_observations": len(items) - len(graded),
            "tasks": len({item["task_id"] for item in items}),
            "successes": successes,
            "success_rate": successes / len(graded) if graded else None,
            "mean_score": (
                sum(float(item["grade"]["score"]) for item in graded) / len(graded)
                if graded else None
            ),
            "mean_output_characters": (
                sum(len(item["raw_response"]) for item in items if isinstance(item.get("raw_response"), str))
                / len(items)
                if items else None
            ),
            "mean_directive_tokens": sum(item["directive_token_estimate"] for item in items) / len(items) if items else None,
            "observation_statuses": dict(sorted(_counts(item.get("observation_status", "completed") for item in items).items())),
        }
    if alias_seen and "adaptive-end-to-end" in conditions:
        conditions["adaptive-runtime"] = conditions["adaptive-end-to-end"]
    paired: dict[str, float | None] = {}
    comparisons = {}

    def add_comparison(name: str, treatment: str, comparator: str, paired_name: str) -> None:
        if treatment not in conditions or comparator not in conditions:
            return
        comparison = _paired_comparison(task_scores, treatment, comparator)
        paired[paired_name] = comparison["mean_task_delta"]
        comparisons[name] = comparison

    add_comparison(
        "adaptive-fixed-resolution-minus-baseline",
        "adaptive-fixed-resolution",
        "baseline",
        "adaptive_fixed_resolution_minus_baseline_mean_task_score",
    )
    add_comparison(
        "adaptive-end-to-end-minus-adaptive-fixed-resolution",
        "adaptive-end-to-end",
        "adaptive-fixed-resolution",
        "adaptive_end_to_end_minus_fixed_resolution_mean_task_score",
    )
    add_comparison(
        "adaptive-end-to-end-minus-baseline",
        "adaptive-end-to-end",
        "baseline",
        "adaptive_end_to_end_minus_baseline_mean_task_score",
    )
    add_comparison(
        "adaptive-fixed-resolution-minus-static-full",
        "adaptive-fixed-resolution",
        "static-full",
        "adaptive_fixed_resolution_minus_static_full_mean_task_score",
    )
    add_comparison(
        "adaptive-end-to-end-minus-static-full",
        "adaptive-end-to-end",
        "static-full",
        "adaptive_end_to_end_minus_static_full_mean_task_score",
    )
    if alias_seen and "adaptive-end-to-end-minus-baseline" in comparisons:
        paired["adaptive_minus_baseline_success_rate"] = comparisons[
            "adaptive-end-to-end-minus-baseline"
        ]["mean_task_delta"]
        comparisons["adaptive-minus-baseline"] = comparisons["adaptive-end-to-end-minus-baseline"]
    if alias_seen and "adaptive-end-to-end-minus-static-full" in comparisons:
        paired["adaptive_minus_static_full_success_rate"] = comparisons[
            "adaptive-end-to-end-minus-static-full"
        ]["mean_task_delta"]
        comparisons["adaptive-minus-static-full"] = comparisons["adaptive-end-to-end-minus-static-full"]
    return {
        "conditions": conditions,
        "paired_differences": paired,
        "paired_comparisons": comparisons,
        "selection_vs_runtime_attribution": _selection_vs_runtime_attribution(task_scores),
    }


def _counts(values) -> dict:
    result = defaultdict(int)
    for value in values:
        result[value] += 1
    return result


def _paired_comparison(task_scores: dict, treatment: str, comparator: str) -> dict:
    task_ids = sorted(set(task_scores[treatment]) & set(task_scores[comparator]))
    deltas = {
        task_id: (
            sum(task_scores[treatment][task_id]) / len(task_scores[treatment][task_id])
            - sum(task_scores[comparator][task_id]) / len(task_scores[comparator][task_id])
        )
        for task_id in task_ids
    }
    values = list(deltas.values())
    return {
        "treatment": treatment,
        "comparator": comparator,
        "paired_tasks": len(values),
        "mean_task_delta": sum(values) / len(values) if values else None,
        "median_task_delta": median(values) if values else None,
        "improved_tasks": sum(value > 0 for value in values),
        "tied_tasks": sum(value == 0 for value in values),
        "regressed_tasks": sum(value < 0 for value in values),
        "per_task": deltas,
    }


def _mean_task_scores(task_scores: dict, condition: str) -> dict[str, float]:
    return {
        task_id: sum(values) / len(values)
        for task_id, values in task_scores.get(condition, {}).items()
        if values
    }


def _attribution_label(runtime_delta: float, selection_delta: float) -> str:
    if runtime_delta > 0 and selection_delta > 0:
        return "both-helped"
    if runtime_delta < 0 and selection_delta < 0:
        return "both-hurt"
    if runtime_delta > 0 and selection_delta == 0:
        return "runtime-helped"
    if runtime_delta < 0 and selection_delta == 0:
        return "runtime-hurt"
    if runtime_delta == 0 and selection_delta > 0:
        return "resolver-helped"
    if runtime_delta == 0 and selection_delta < 0:
        return "resolver-hurt"
    return "mixed/tied"


def _selection_vs_runtime_attribution(task_scores: dict) -> dict:
    baseline = _mean_task_scores(task_scores, "baseline")
    fixed = _mean_task_scores(task_scores, "adaptive-fixed-resolution")
    end_to_end = _mean_task_scores(task_scores, "adaptive-end-to-end")
    task_ids = sorted(set(baseline) & set(fixed) & set(end_to_end))
    per_task = {}
    labels = defaultdict(int)
    for task_id in task_ids:
        runtime_delta = fixed[task_id] - baseline[task_id]
        selection_delta = end_to_end[task_id] - fixed[task_id]
        label = _attribution_label(runtime_delta, selection_delta)
        labels[label] += 1
        per_task[task_id] = {
            "baseline_score": baseline[task_id],
            "fixed_resolution_score": fixed[task_id],
            "end_to_end_score": end_to_end[task_id],
            "runtime_delta_with_selection_fixed": runtime_delta,
            "selection_delta_end_to_end_minus_fixed": selection_delta,
            "total_delta_end_to_end_minus_baseline": end_to_end[task_id] - baseline[task_id],
            "descriptive_label": label,
        }
    return {
        "interpretation": (
            "Descriptive score decomposition only: fixed-minus-baseline holds the saved selection fixed; "
            "end-to-end-minus-fixed varies TaskResolution source. Labels do not establish a causal mechanism."
        ),
        "paired_tasks": len(task_ids),
        "label_counts": dict(sorted(labels.items())),
        "per_task": per_task,
    }


def write_report(directory: str | Path, manifest: dict, results: list[dict]) -> dict:
    target = Path(directory)
    summary = summarize(results)
    summary.update({
        "schema_version": "1.0.0",
        "experiment_id": manifest["experiment_id"],
        "suite": manifest["suite"],
        "limitations": [
            "Descriptive results from this bounded suite do not establish general model equivalence.",
            "Mock-adapter results validate harness plumbing only and are not model-quality evidence."
            if manifest["model"].get("adapter") == "mock" else
            "Model outputs can be nondeterministic; task-level paired results and raw observations are retained.",
        ],
    })
    (target / "summary.json").write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    lines = [
        f"# Runtime evaluation: {manifest['experiment_id']}", "",
        f"- Suite: `{manifest['suite']}`",
        f"- Model: `{manifest['model'].get('model', 'unknown')}` via `{manifest['model'].get('adapter', 'unknown')}`",
        f"- Tasks: {len({item['task_id'] for item in results})}",
        f"- Trials: {len(results)} observations", "",
        "## Conditions", "",
    ]
    for condition, values in summary["conditions"].items():
        rate = "not available" if values["success_rate"] is None else f"{values['success_rate']:.3f}"
        lines.append(
            f"- {condition}: {values['successes']}/{values['graded_observations']} "
            f"graded objective successes ({rate}); {values['ungraded_observations']} ungraded"
        )
    if summary["paired_comparisons"]:
        lines.extend(("", "## Task-level paired comparisons", ""))
        for name, values in summary["paired_comparisons"].items():
            delta = values["mean_task_delta"]
            rendered = "not available" if delta is None else f"{delta:+.3f}"
            lines.append(
                f"- {name}: mean task delta {rendered} across {values['paired_tasks']} paired tasks "
                f"({values['improved_tasks']} improved, {values['tied_tasks']} tied, "
                f"{values['regressed_tasks']} regressed)"
            )
    attribution = summary["selection_vs_runtime_attribution"]
    if attribution["per_task"]:
        lines.extend((
            "",
            "## Selection vs Runtime Attribution",
            "",
            attribution["interpretation"],
            "",
            "| Task | Baseline | Fixed resolution | End to end | Runtime delta | Selection delta | Descriptive label |",
            "| --- | ---: | ---: | ---: | ---: | ---: | --- |",
        ))
        for task_id, values in attribution["per_task"].items():
            lines.append(
                f"| `{task_id}` | {values['baseline_score']:.3f} | "
                f"{values['fixed_resolution_score']:.3f} | {values['end_to_end_score']:.3f} | "
                f"{values['runtime_delta_with_selection_fixed']:+.3f} | "
                f"{values['selection_delta_end_to_end_minus_fixed']:+.3f} | "
                f"`{values['descriptive_label']}` |"
            )
    lines.extend(("", "## Limitations and negative results", ""))
    lines.extend(f"- {value}" for value in summary["limitations"])
    lines.extend(("", "Raw requests, responses, condition labels, and grader outputs remain in `raw-results.jsonl`.", ""))
    (target / "report.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")
    return summary
