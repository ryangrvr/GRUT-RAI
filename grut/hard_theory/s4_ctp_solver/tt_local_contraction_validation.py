"""Validation for local tensor contractions."""

from typing import Dict, List


def validate_local_contraction(result: Dict[str, object]) -> Dict[str, object]:
    issues: List[str] = []
    fragment = result.get("fragment", {})

    if fragment.get("allowed_by_sandbox") is not True:
        issues.append("fragment_not_allowed_by_sandbox")
    if fragment.get("scope") != "local_only":
        issues.append("fragment_scope_not_local")
    if fragment.get("requires_propagator") is not False:
        issues.append("fragment_requires_propagator")
    if fragment.get("requires_full_diagram") is not False:
        issues.append("fragment_requires_full_diagram")

    if result.get("contraction_scope") != "local_only":
        issues.append("contraction_scope_not_local")
    if result.get("propagator_evaluated") is not False:
        issues.append("propagator_evaluated")
    if result.get("full_diagram_contracted") is not False:
        issues.append("full_diagram_contracted")
    if result.get("finite_part_computed") is not False:
        issues.append("finite_part_computed")
    if result.get("r_extracted") is not False:
        issues.append("r_extracted")
    if result.get("unresolved_free_indices"):
        issues.append("unresolved_free_indices")

    status = "valid_local" if not issues else "invalid_local"

    return {
        "validation": "local_contraction",
        "status": status,
        "issues": issues,
        "promotes_claims": False,
    }
