"""Behavior checks for a single partition integration attempt."""

from typing import Dict, List


def check_single_partition_behavior(result: Dict[str, object]) -> Dict[str, object]:
    issues: List[str] = []
    if result.get("regulator_active") is not True:
        issues.append("regulator_inactive")
    if result.get("divergence_structure") != "symbolic_divergence":
        issues.append("divergence_structure_missing")
    if result.get("amplitude_computed") is True:
        issues.append("amplitude_computed")
    if result.get("scheme_id") is None:
        issues.append("missing_scheme_id")
    if result.get("default_regulator") is None:
        issues.append("missing_default_regulator")
    if result.get("result") == "finite_constant":
        issues.append("simplified_to_finite_constant")

    return {
        "behavior_ok": not issues,
        "issues": issues,
        "promotes_claims": False,
    }
