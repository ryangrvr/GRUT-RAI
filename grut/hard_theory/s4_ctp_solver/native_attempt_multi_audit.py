"""Multi-topology native attempt audit for Stage 5B."""

from typing import Dict, List


def audit_native_multi(
    results: List[Dict[str, object]],
    audits: List[Dict[str, object]],
    comparison: Dict[str, object],
) -> Dict[str, object]:
    all_valid = all(audit.get("status") == "valid_attempt" for audit in audits)
    comparison_ok = comparison.get("status") != "inconsistent"

    issues: List[str] = []
    if not all_valid:
        issues.append("invalid_individual_attempt")
    if not comparison_ok:
        issues.append("inconsistent_comparison")

    return {
        "audit": "native_multi",
        "status": "valid_multi_attempt" if all_valid and comparison_ok else "invalid_multi_attempt",
        "topologies_checked": len(results),
        "all_valid": all_valid,
        "issues": issues,
        "can_expand_to_tensor_depth": all_valid and comparison_ok,
        "can_compute_full_3loop": False,
        "promotes_claims": False,
    }
