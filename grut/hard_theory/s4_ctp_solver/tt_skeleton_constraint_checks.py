"""Constraint checks for skeleton structural contractions."""

from typing import Dict, List


def check_skeleton_constraints(result: Dict[str, object]) -> Dict[str, object]:
    issues: List[str] = []
    skeleton = result.get("skeleton", {})

    if result.get("index_flow_resolved") is not True:
        issues.append("index_flow_unresolved")

    if result.get("projectors_preserved") is not True:
        issues.append("projectors_not_preserved")

    if result.get("tt_constraints_preserved") is not True:
        issues.append("tt_constraints_not_preserved")

    if result.get("propagators_evaluated") is not False:
        issues.append("propagators_evaluated")

    if result.get("loops_evaluated") is not False:
        issues.append("loops_evaluated")

    if result.get("finite_part_computed") is not False:
        issues.append("finite_part_computed")

    if result.get("extraction_performed") is not False:
        issues.append("extraction_performed")

    if result.get("r_extracted") is not False:
        issues.append("r_extracted")

    if skeleton.get("projectors_present") is not True:
        issues.append("projectors_missing")

    if not skeleton.get("nodes"):
        issues.append("nodes_missing")

    if not skeleton.get("edges"):
        issues.append("edges_missing")

    status = "valid" if not issues else "invalid"

    return {
        "constraint_check": "skeleton",
        "status": status,
        "issues": issues,
        "promotes_claims": False,
    }
