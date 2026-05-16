"""Audit for a single partition integration attempt."""

from typing import Dict


def audit_single_partition_integration(
    selection: Dict[str, object],
    result: Dict[str, object],
    behavior: Dict[str, object],
    guard: Dict[str, object],
) -> Dict[str, object]:
    selected_one = selection.get("selected_count") == 1
    full_integrand_ok = selection.get("full_integrand") is False
    no_amplitude = result.get("amplitude_computed") is False
    no_finite_part = result.get("finite_part_computed") is False
    regulator_ok = result.get("regulator_active") is True
    no_r_extraction = result.get("r_extracted") is False
    behavior_ok = behavior.get("behavior_ok") is True
    guard_ok = guard.get("guard") == "tensor_placeholder_guard"

    status = (
        "valid"
        if all(
            [
                selected_one,
                full_integrand_ok,
                no_amplitude,
                no_finite_part,
                regulator_ok,
                no_r_extraction,
                guard_ok,
            ]
        )
        else "invalid"
    )

    return {
        "audit": "single_partition_integration",
        "status": status,
        "can_advance_to_subtraction_dry_run": status == "valid" and behavior_ok,
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
    }
