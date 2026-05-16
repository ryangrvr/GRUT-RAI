"""Consistency checks for cross-partition finite-part attempts."""

from typing import Dict, List


_FORBIDDEN_NAMES = {"C_Final", "C_Cosmo", "R"}


def check_cross_partition_finite_consistency(
    results: List[Dict[str, object]],
) -> Dict[str, object]:
    issues: List[str] = []

    if not results:
        issues.append("no_partitions_selected")

    scheme_ids = {result.get("scheme_id") for result in results}
    scheme_ids.discard(None)
    if len(scheme_ids) > 1:
        issues.append("scheme_id_mismatch")

    default_regs = {result.get("default_regulator") for result in results}
    default_regs.discard(None)
    if len(default_regs) > 1:
        issues.append("default_regulator_mismatch")

    if any(result.get("finite_part_status") != "candidate_partition_level" for result in results):
        issues.append("finite_part_status_mismatch")

    if any(result.get("coefficient_name") in _FORBIDDEN_NAMES for result in results):
        issues.append("forbidden_coefficient_name")

    if any(result.get("amplitude_computed") is True for result in results):
        issues.append("amplitude_computed")

    return {
        "consistent": not issues,
        "issues": issues,
        "promotes_claims": False,
    }
