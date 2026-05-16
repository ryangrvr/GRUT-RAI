"""Audit coefficient assembly dry-run."""

from typing import Dict


def audit_coefficient_assembly_dry_run(
    assembly: Dict[str, object],
    guard: Dict[str, object],
) -> Dict[str, object]:
    no_physical = assembly.get("physical_coefficients_computed") is False
    no_c_final = assembly.get("c_final_computed") is False
    no_c_cosmo = assembly.get("c_cosmo_computed") is False
    no_r = assembly.get("r_computed") is False
    guard_ok = guard.get("guard") == "tensor_placeholder_guard"

    status = (
        "valid" if all([no_physical, no_c_final, no_c_cosmo, no_r, guard_ok]) else "invalid"
    )

    return {
        "audit": "coefficient_assembly_dry_run",
        "status": status,
        "can_advance_to_scheme_stability_audit": status == "valid",
        "can_compute_c_final": False,
        "can_compute_c_cosmo": False,
        "can_compute_r": False,
        "can_extract": False,
        "promotes_claims": False,
    }
