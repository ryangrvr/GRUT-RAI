"""Audit for finite-part benchmark gate."""

from typing import Dict, List


def audit_finite_part_benchmark(
    results: List[Dict[str, object]],
    comparisons: List[Dict[str, object]],
    guard: Dict[str, object],
) -> Dict[str, object]:
    native_ok = all(result.get("native_input_used") is False for result in results)
    comparisons_ok = all(
        comparison.get("comparison_status") == "benchmark_pass" for comparison in comparisons
    )
    guard_ok = guard.get("guard") == "tensor_placeholder_guard"

    status = "valid" if all([native_ok, comparisons_ok, guard_ok]) else "invalid"

    return {
        "audit": "finite_part_benchmark",
        "status": status,
        "can_advance_to_native_finite_part_attempt": status == "valid" and comparisons_ok,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
    }
