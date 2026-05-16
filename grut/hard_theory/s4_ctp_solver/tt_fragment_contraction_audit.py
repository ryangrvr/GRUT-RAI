"""Audit for controlled fragment contractions."""

from typing import Dict


def audit_controlled_fragment_contraction(
    result: Dict[str, object],
    validation: Dict[str, object],
) -> Dict[str, object]:
    validation_ok = validation.get("status") == "valid_fragment"
    controlled_only = result.get("contraction_scope") == "controlled_fragment_only"
    no_propagator = result.get("propagator_evaluated") is False
    no_full_diagram = result.get("full_diagram_contracted") is False
    no_finite_parts = result.get("finite_part_computed") is False
    no_extraction = result.get("extraction_performed") is False
    no_r_extract = result.get("r_extracted") is False
    guard = result.get("guard", {})
    guard_ok = guard.get("guard") == "tensor_placeholder_guard"

    status = (
        "valid"
        if all(
            [
                validation_ok,
                controlled_only,
                no_propagator,
                no_full_diagram,
                no_finite_parts,
                no_extraction,
                no_r_extract,
                guard_ok,
            ]
        )
        else "invalid"
    )

    return {
        "audit": "controlled_fragment_contraction",
        "status": status,
        "controlled_fragment_contractions_performed": True,
        "full_contractions_performed": False,
        "can_advance_to_single_diagram_skeleton": validation_ok,
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
    }
