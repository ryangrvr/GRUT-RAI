"""Validate a native finite-part attempt result."""

from typing import Dict, List


_FORBIDDEN_NAMES = {"C_Final", "C_Cosmo", "R"}


def validate_native_finite_part_attempt(result: Dict[str, object]) -> Dict[str, object]:
    issues: List[str] = []
    if result.get("coefficient_scope") != "single_partition_only":
        issues.append("invalid_scope")
    if result.get("amplitude_computed") is True:
        issues.append("amplitude_computed")
    if result.get("coefficient_name") in _FORBIDDEN_NAMES:
        issues.append("forbidden_coefficient_name")
    if result.get("scheme_id") is None:
        issues.append("missing_scheme_id")
    if result.get("default_regulator") is None:
        issues.append("missing_default_regulator")

    status = "valid_candidate_partition_level" if not issues else "invalid"

    return {
        "validation": "native_partition_finite_part",
        "status": status,
        "issues": issues,
        "promotes_claims": False,
    }
