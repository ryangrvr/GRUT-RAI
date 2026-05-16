"""Consistency checks for eligible partition dry-runs."""

from typing import Dict, List


def check_eligible_partition_consistency(attempts: Dict[str, object]) -> Dict[str, object]:
    issues: List[str] = []
    attempt_list = attempts.get("attempts", [])

    if not all(attempt.get("regulator_present") is True for attempt in attempt_list):
        issues.append("regulator_missing")

    if any(attempt.get("result") == "finite_constant" for attempt in attempt_list):
        issues.append("simplified_to_finite_constant")

    if any(attempt.get("amplitude_computed") is True for attempt in attempt_list):
        issues.append("amplitude_computed")

    scheme_ids = {attempt.get("scheme_id") for attempt in attempt_list}
    if len(scheme_ids) > 1:
        issues.append("scheme_id_mismatch")

    default_regs = {attempt.get("default_regulator") for attempt in attempt_list}
    if len(default_regs) > 1:
        issues.append("default_regulator_mismatch")

    return {
        "consistent": not issues,
        "issues": issues,
        "promotes_claims": False,
    }
