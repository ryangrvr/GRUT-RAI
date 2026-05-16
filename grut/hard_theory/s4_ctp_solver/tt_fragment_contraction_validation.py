"""Validation for controlled fragment contractions."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.tt_contraction_ordering import (
    define_contraction_ordering_protocol,
)
from grut.hard_theory.s4_ctp_solver.tt_fragment_contraction_engine import (
    LOCAL_OPERATIONS,
)


def validate_controlled_fragment_contraction(result: Dict[str, object]) -> Dict[str, object]:
    issues: List[str] = []
    fragment = result.get("fragment", {})
    ordering = define_contraction_ordering_protocol()
    ordering_steps = ordering.get("steps", [])

    if fragment.get("allowed_by_stage8b") is not True:
        issues.append("fragment_not_allowed_by_stage8b")
    if fragment.get("scope") != "controlled_fragment_only":
        issues.append("fragment_scope_not_controlled")
    if fragment.get("requires_propagator") is not False:
        issues.append("fragment_requires_propagator")
    if fragment.get("requires_full_diagram") is not False:
        issues.append("fragment_requires_full_diagram")
    if not fragment.get("local_fragments"):
        issues.append("fragment_missing_local_fragments")

    if result.get("contraction_scope") != "controlled_fragment_only":
        issues.append("contraction_scope_not_controlled")

    operations = result.get("operations_applied", [])
    allowed_operations = set(LOCAL_OPERATIONS) | set(ordering_steps)
    for op in operations:
        if op not in allowed_operations:
            issues.append(f"operation_not_allowed:{op}")

    if result.get("ordering_protocol_id") != ordering.get("protocol_id"):
        issues.append("ordering_protocol_mismatch")
    if result.get("ordering_protocol_followed") is not True:
        issues.append("ordering_protocol_not_followed")
    for step in ordering_steps:
        if step not in operations:
            issues.append(f"ordering_step_missing:{step}")

    if result.get("projector_preserved") is not True:
        issues.append("projector_not_preserved")
    if result.get("tt_constraints_preserved") is not True:
        issues.append("tt_constraints_not_preserved")

    if result.get("propagator_evaluated") is not False:
        issues.append("propagator_evaluated")
    if result.get("full_diagram_contracted") is not False:
        issues.append("full_diagram_contracted")
    if result.get("finite_part_computed") is not False:
        issues.append("finite_part_computed")
    if result.get("extraction_performed") is not False:
        issues.append("extraction_performed")
    if result.get("r_extracted") is not False:
        issues.append("r_extracted")

    status = "valid_fragment" if not issues else "invalid_fragment"

    return {
        "validation": "controlled_fragment_contraction",
        "status": status,
        "issues": issues,
        "promotes_claims": False,
    }
