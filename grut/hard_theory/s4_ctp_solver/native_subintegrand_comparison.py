"""Sanity checks for native sub-integrand dry runs."""

from typing import Dict, List


def check_subintegrand_behavior(result: Dict[str, object]) -> Dict[str, object]:
    issues: List[str] = []
    if result.get("regulator_present") is not True:
        issues.append("regulator_missing")
    if result.get("finite_part_computed") is True:
        issues.append("finite_part_computed")
    if result.get("amplitude_computed") is True:
        issues.append("amplitude_computed")
    if result.get("result") == "finite_constant":
        issues.append("simplified_to_finite_constant")

    behavior_ok = not issues

    return {
        "behavior_ok": behavior_ok,
        "issues": issues,
        "promotes_claims": False,
    }
