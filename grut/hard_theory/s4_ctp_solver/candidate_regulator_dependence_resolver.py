"""Resolve regulator_dependence_class for coefficient candidates."""

from typing import Dict


def _regulator_status(stage9c: Dict[str, object], stage9d: Dict[str, object]) -> str:
    if not stage9c:
        return "regulator_metadata_missing"

    regularization_attached = stage9c.get("regularization_attached")
    plan_summary = stage9d.get("plan_summary", {}) if isinstance(stage9d, dict) else {}
    default_regulator = plan_summary.get("default_regulator")

    if regularization_attached is True and default_regulator:
        return "symbolic_regulator_preserved"
    if regularization_attached is False:
        return "invalid_regulator_removed"
    return "regulator_metadata_missing"


def apply_regulator_dependence_metadata(
    registry: Dict[str, object],
    stage9c: Dict[str, object],
    stage9d: Dict[str, object],
) -> Dict[str, object]:
    status = _regulator_status(stage9c, stage9d)
    candidate_buckets = registry.get("candidate_buckets", {})
    for candidate in candidate_buckets.values():
        if not isinstance(candidate, dict):
            continue
        candidate["regulator_dependence_class"] = status
    return registry
