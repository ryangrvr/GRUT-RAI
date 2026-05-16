"""Regulator consistency checks across partition attempts."""

from typing import Dict, List


def check_partition_regulator_consistency(attempts: List[Dict[str, object]]) -> Dict[str, object]:
    issues: List[str] = []

    regulator_present = [attempt.get("regulator_present") for attempt in attempts]
    if any(present is not True for present in regulator_present):
        issues.append("regulator_missing")

    default_regs = {attempt.get("default_regulator") for attempt in attempts}
    default_regs.discard(None)
    if len(default_regs) > 1:
        issues.append("default_regulator_mismatch")

    regulator_removed = any(present is False for present in regulator_present)

    return {
        "regulator_consistent": not issues,
        "regulator_removed": regulator_removed,
        "issues": issues,
        "promotes_claims": False,
    }
