"""Validate tensor-origin and regulator metadata completion."""

from typing import Dict, List


def validate_candidate_metadata_r3(registry: Dict[str, object]) -> Dict[str, object]:
    missing_fields: List[str] = []
    invalid_regulator_removed = False

    candidate_buckets = registry.get("candidate_buckets", {})
    for candidate in candidate_buckets.values():
        if not isinstance(candidate, dict):
            continue

        if candidate.get("tensor_origin_class") is None:
            missing_fields.append("tensor_origin_class")
        if candidate.get("regulator_dependence_class") is None:
            missing_fields.append("regulator_dependence_class")
        if candidate.get("regulator_dependence_class") == "invalid_regulator_removed":
            invalid_regulator_removed = True

    valid = not missing_fields and not invalid_regulator_removed

    return {
        "valid": valid,
        "missing_fields": sorted(set(missing_fields)),
        "invalid_regulator_removed": invalid_regulator_removed,
        "promotes_claims": False,
    }
