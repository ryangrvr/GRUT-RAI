"""Audit for native sub-integrand dry run."""

from typing import Dict


def audit_native_subintegrand_run(
    result: Dict[str, object],
    checks: Dict[str, object],
    guard: Dict[str, object],
) -> Dict[str, object]:
    regulator_ok = result.get("regulator_present") is True
    no_finite_part = result.get("finite_part_computed") is False
    no_amplitude = result.get("amplitude_computed") is False
    native_ok = result.get("native_integrand_used") is True
    full_ok = result.get("full_integrand_used") is False
    behavior_ok = checks.get("behavior_ok") is True
    guard_ok = guard.get("guard") == "tensor_placeholder_guard"

    stable = all([regulator_ok, no_finite_part, no_amplitude, native_ok, full_ok, behavior_ok, guard_ok])
    status = "valid" if stable else "invalid"

    return {
        "audit": "native_subintegrand",
        "status": status,
        "can_advance_to_multi_subintegrand": stable,
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
    }
