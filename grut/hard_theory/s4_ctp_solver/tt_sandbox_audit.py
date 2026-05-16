"""Audit for the tensor contraction sandbox stage."""

from typing import Dict


def audit_tensor_contraction_sandbox(
    results: Dict[str, object],
    validation: Dict[str, object],
) -> Dict[str, object]:
    validation_ok = validation.get("status") == "valid_sandbox"
    no_full_contractions = results.get("full_contractions_performed") is False
    no_propagators = results.get("propagators_evaluated") is False
    no_finite_parts = results.get("finite_parts_computed") is False
    no_extraction = results.get("extraction_performed") is False
    no_r_extract = results.get("r_extracted") is False
    guard = results.get("guard", {})
    guard_ok = guard.get("guard") == "tensor_placeholder_guard"

    status = (
        "valid"
        if all(
            [
                validation_ok,
                no_full_contractions,
                no_propagators,
                no_finite_parts,
                no_extraction,
                no_r_extract,
                guard_ok,
            ]
        )
        else "invalid"
    )

    return {
        "audit": "tensor_contraction_sandbox",
        "status": status,
        "can_advance_to_limited_contractions": validation_ok,
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
    }
