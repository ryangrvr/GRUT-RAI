"""Audit for cross-partition finite-part consistency."""

from typing import Dict, List


_FORBIDDEN_NAMES = {"C_Final", "C_Cosmo", "R"}


def audit_cross_partition_finite_consistency(
    results: List[Dict[str, object]],
    consistency: Dict[str, object],
    guard: Dict[str, object],
) -> Dict[str, object]:
    no_amplitude = all(result.get("amplitude_computed") is False for result in results)
    no_c_final = all(result.get("c_final_computed") is False for result in results)
    no_c_cosmo = all(result.get("c_cosmo_computed") is False for result in results)
    no_r = all(result.get("r_extraction_attempted") is False for result in results)
    no_forbidden_names = all(
        result.get("coefficient_name") not in _FORBIDDEN_NAMES for result in results
    )
    guard_ok = guard.get("guard") == "tensor_placeholder_guard"

    status = (
        "valid"
        if all([no_amplitude, no_c_final, no_c_cosmo, no_r, no_forbidden_names, guard_ok])
        else "invalid"
    )

    return {
        "status": status,
        "can_advance_to_coefficient_assembly_dry_run": status == "valid" and consistency.get("consistent") is True,
        "can_compute_c_final": False,
        "can_compute_c_cosmo": False,
        "can_compute_r": False,
        "can_extract": False,
        "promotes_claims": False,
    }
