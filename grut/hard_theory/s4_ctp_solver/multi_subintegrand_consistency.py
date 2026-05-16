"""Consistency checks across multiple sub-integrand attempts."""

from typing import Dict, List


def compare_subintegrand_behaviors(attempts: Dict[str, object]) -> Dict[str, object]:
    issues: List[str] = []
    attempt_list = attempts.get("attempts", [])

    regulators_ok = all(attempt.get("regulator_present") is True for attempt in attempt_list)
    if not regulators_ok:
        issues.append("regulator_missing")

    finite_constant = any(attempt.get("result") == "finite_constant" for attempt in attempt_list)
    if finite_constant:
        issues.append("simplified_to_finite_constant")

    divergence_keys = {attempt.get("result") for attempt in attempt_list}
    if len(divergence_keys) > 1:
        issues.append("divergence_behavior_mismatch")

    scheme_ids = {attempt.get("scheme_id") for attempt in attempt_list}
    if len(scheme_ids) > 1:
        issues.append("scheme_id_mismatch")

    default_regs = {attempt.get("default_regulator") for attempt in attempt_list}
    if len(default_regs) > 1:
        issues.append("default_regulator_mismatch")

    consistent = not issues

    return {
        "comparison": "multi_subintegrand_behavior",
        "consistent": consistent,
        "issues": issues,
        "promotes_claims": False,
    }
