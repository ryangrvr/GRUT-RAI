"""Audit for multi-subintegrand consistency checks."""

from typing import Dict, List


def audit_multi_subintegrand(
    attempts: Dict[str, object],
    comparison: Dict[str, object],
) -> Dict[str, object]:
    attempt_list: List[Dict[str, object]] = attempts.get("attempts", [])
    count_ok = 2 <= len(attempt_list) <= 3
    full_integrand_ok = all(attempt.get("full_integrand_used") is False for attempt in attempt_list)
    no_amplitude = attempts.get("amplitude_computed") is False
    no_finite_parts = attempts.get("finite_parts_computed") is False
    consistent = comparison.get("consistent") is True
    guard = comparison.get("guard", {})
    guard_ok = guard.get("guard") == "tensor_placeholder_guard"

    stable = all([count_ok, full_integrand_ok, no_amplitude, no_finite_parts, consistent, guard_ok])
    status = "valid" if stable else "invalid"

    return {
        "audit": "multi_subintegrand",
        "status": status,
        "can_advance_to_native_integrand_partition": stable and consistent,
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
    }
