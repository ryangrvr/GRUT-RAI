"""Audit a native finite-part attempt."""

from typing import Dict


def audit_native_finite_part_attempt(
    result: Dict[str, object],
    validation: Dict[str, object],
    guard: Dict[str, object],
) -> Dict[str, object]:
    one_partition = result.get("coefficient_scope") == "single_partition_only"
    no_amplitude = result.get("amplitude_computed") is False
    no_r_extraction = result.get("r_extraction_attempted") is False
    validation_ok = validation.get("status") == "valid_candidate_partition_level"
    guard_ok = guard.get("guard") == "tensor_placeholder_guard"

    status = (
        "valid"
        if all([one_partition, no_amplitude, no_r_extraction, guard_ok, validation_ok])
        else "invalid"
    )

    return {
        "audit": "native_partition_finite_part_attempt",
        "status": status,
        "can_advance_to_cross_partition_finite_part": status == "valid" and validation_ok,
        "can_compute_c_final": False,
        "can_compute_c_cosmo": False,
        "can_compute_r": False,
        "can_extract": False,
        "promotes_claims": False,
    }
