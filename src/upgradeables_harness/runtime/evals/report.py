"""Descriptive, limitation-preserving evaluation reports."""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path
from statistics import median


def summarize(results: list[dict]) -> dict:
    grouped = defaultdict(list)
    for item in results:
        grouped[item["condition"]].append(item)
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
    paired = {}
    comparisons = {}
    if "baseline" in conditions and "adaptive-runtime" in conditions:
        comparison = _paired_comparison(task_scores, "adaptive-runtime", "baseline")
        paired["adaptive_minus_baseline_success_rate"] = comparison["mean_task_delta"]
        comparisons["adaptive-minus-baseline"] = comparison
    if "static-full" in conditions and "adaptive-runtime" in conditions:
        comparison = _paired_comparison(task_scores, "adaptive-runtime", "static-full")
        paired["adaptive_minus_static_full_success_rate"] = comparison["mean_task_delta"]
        comparisons["adaptive-minus-static-full"] = comparison
    return {
        "conditions": conditions,
        "paired_differences": paired,
        "paired_comparisons": comparisons,
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
    lines.extend(("", "## Limitations and negative results", ""))
    lines.extend(f"- {value}" for value in summary["limitations"])
    lines.extend(("", "Raw requests, responses, condition labels, and grader outputs remain in `raw-results.jsonl`.", ""))
    (target / "report.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")
    return summary
