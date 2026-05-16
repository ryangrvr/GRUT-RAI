"""Audit for regularized integrand scaffold."""

from typing import Dict


def audit_regularized_integrand(
    result: Dict[str, object],
    validation: Dict[str, object],
) -> Dict[str, object]:
    validation_ok = validation.get("status") == "valid_regularized_scaffold"
    no_integration = result.get("integration_performed") is False
    no_amplitude = result.get("amplitude_computed") is False
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
                no_integration,
                no_amplitude,
                no_finite_parts,
                no_extraction,
                no_r_extract,
                guard_ok,
            ]
        )
        else "invalid"
    )

    return {
        "audit": "regularized_integrand_scaffold",
        "status": status,
        "can_advance_to_integration_dry_run": validation_ok,
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
    }
