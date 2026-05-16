"""Audit for diagram skeleton structural contractions."""

from typing import Dict


def audit_skeleton_contraction(
    result: Dict[str, object],
    constraint_check: Dict[str, object],
) -> Dict[str, object]:
    constraints_ok = constraint_check.get("status") == "valid"
    no_propagators = result.get("propagators_evaluated") is False
    no_loops = result.get("loops_evaluated") is False
    no_finite_parts = result.get("finite_part_computed") is False
    no_extraction = result.get("extraction_performed") is False
    no_r_extract = result.get("r_extracted") is False
    guard = result.get("guard", {})
    guard_ok = guard.get("guard") == "tensor_placeholder_guard"

    status = (
        "valid"
        if all(
            [
                constraints_ok,
                no_propagators,
                no_loops,
                no_finite_parts,
                no_extraction,
                no_r_extract,
                guard_ok,
            ]
        )
        else "invalid"
    )

    return {
        "audit": "diagram_skeleton",
        "status": status,
        "full_diagram_contracted": False,
        "structure_only": True,
        "can_advance_to_propagator_symbolics": constraints_ok,
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
    }
