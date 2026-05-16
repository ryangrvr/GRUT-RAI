"""Audit for propagator symbolic attachments."""

from typing import Dict


def audit_propagator_attachment(
    attachment_result: Dict[str, object],
    validation: Dict[str, object],
) -> Dict[str, object]:
    validation_ok = validation.get("status") == "valid_attachment"
    no_propagators = attachment_result.get("propagators_evaluated") is False
    no_loops = attachment_result.get("loops_evaluated") is False
    no_finite_parts = attachment_result.get("finite_part_computed") is False
    no_extraction = attachment_result.get("extraction_performed") is False
    no_r_extract = attachment_result.get("r_extracted") is False
    guard = attachment_result.get("guard", {})
    guard_ok = guard.get("guard") == "tensor_placeholder_guard"

    status = (
        "valid"
        if all(
            [
                validation_ok,
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
        "audit": "propagator_symbolic_attachment",
        "status": status,
        "can_advance_to_loop_integrand_assembly": validation_ok,
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
    }
