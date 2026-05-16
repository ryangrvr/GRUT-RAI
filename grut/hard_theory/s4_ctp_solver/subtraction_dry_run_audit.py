"""Audit the divergence subtraction dry-run plan."""

from typing import Dict


def audit_subtraction_dry_run(
    plan: Dict[str, object],
    mapping: Dict[str, object],
    guard: Dict[str, object],
) -> Dict[str, object]:
    subtractions_ok = plan.get("subtractions_performed") is False
    regulator_ok = plan.get("regulator_removed") is False
    finite_ok = plan.get("finite_part_computed") is False
    amplitude_ok = plan.get("amplitude_computed", False) is False
    guard_ok = guard.get("guard") == "tensor_placeholder_guard"

    status = (
        "valid" if all([subtractions_ok, regulator_ok, finite_ok, amplitude_ok, guard_ok]) else "invalid"
    )
    can_advance = not mapping.get("unmapped_divergences")

    return {
        "audit": "divergence_subtraction_dry_run",
        "status": status,
        "can_advance_to_finite_part_benchmark": status == "valid" and can_advance,
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
    }
