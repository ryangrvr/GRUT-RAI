"""Evaluate tensor contraction readiness for TT sector."""

from typing import Dict, List


def evaluate_contraction_readiness(
    index_structure: Dict[str, object],
    rules: Dict[str, object],
    projector_check: Dict[str, object],
) -> Dict[str, object]:
    issues: List[str] = []
    missing_elements: List[str] = []

    if not index_structure.get("complete"):
        issues.append("incomplete_index_structure")
        missing_elements.append("index_pairing")
    if index_structure.get("free_indices"):
        issues.append("free_indices_present")
        missing_elements.append("free_indices_resolved")
    if not index_structure.get("tt_constraints_respected"):
        issues.append("tt_constraints_not_respected")
    if not projector_check.get("projector_consistency"):
        issues.append("projector_inconsistent")
        missing_elements.append("projector_consistency")

    readiness = "ready" if not issues else "not_ready"

    return {
        "readiness": readiness,
        "issues": issues,
        "missing_elements": missing_elements,
        "blocker_closed": False,
        "promotes_claims": False,
    }
