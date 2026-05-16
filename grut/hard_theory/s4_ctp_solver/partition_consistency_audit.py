"""Audit for partition consistency checks."""

from typing import Dict


def audit_partition_consistency(
    collected: Dict[str, object],
    scheme_check: Dict[str, object],
    regulator_check: Dict[str, object],
    guard: Dict[str, object],
) -> Dict[str, object]:
    attempts = collected.get("collected_attempts", [])
    no_new_integrations = collected.get("new_integrations_performed") is False
    no_amplitude = all(attempt.get("amplitude_computed") is False for attempt in attempts)
    no_finite_parts = all(attempt.get("finite_part_computed") is False for attempt in attempts)
    no_extraction = True
    scheme_ok = scheme_check.get("scheme_consistent") is True
    regulator_ok = regulator_check.get("regulator_consistent") is True
    guard_ok = guard.get("guard") == "tensor_placeholder_guard"

    consistent = scheme_ok and regulator_ok
    status = (
        "valid"
        if all([no_new_integrations, no_amplitude, no_finite_parts, no_extraction, guard_ok])
        else "invalid"
    )

    return {
        "audit": "partition_consistency",
        "status": status,
        "consistent": consistent,
        "can_advance_to_single_partition_integration": consistent,
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
    }
