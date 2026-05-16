"""Audit for loop-integrand scaffold."""

from typing import Dict


def audit_loop_integrand_scaffold(
    integrand: Dict[str, object],
    validation: Dict[str, object],
) -> Dict[str, object]:
    validation_ok = validation.get("status") == "valid_integrand_scaffold"
    no_integration = integrand.get("integration_performed") is False
    no_propagators = integrand.get("propagators_evaluated") is False
    no_amplitude = integrand.get("amplitude_computed") is False
    no_finite_parts = integrand.get("finite_part_computed") is False
    guard = integrand.get("guard", {})
    guard_ok = guard.get("guard") == "tensor_placeholder_guard"

    status = (
        "valid"
        if all(
            [
                validation_ok,
                no_integration,
                no_propagators,
                no_amplitude,
                no_finite_parts,
                guard_ok,
            ]
        )
        else "invalid"
    )

    return {
        "audit": "loop_integrand_scaffold",
        "status": status,
        "can_advance_to_regularized_integrand": validation_ok,
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
    }
