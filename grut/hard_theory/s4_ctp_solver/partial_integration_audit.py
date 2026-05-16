"""Audit for controlled partial integration benchmarks."""

from typing import Dict, List


def audit_partial_integration(
    results: List[Dict[str, object]],
    comparisons: List[Dict[str, object]],
    guard: Dict[str, object],
) -> Dict[str, object]:
    benchmarks_only = all(result.get("native_integrand_used") is False for result in results)
    no_coefficients = True
    guard_ok = guard.get("guard") == "tensor_placeholder_guard"
    comparisons_ok = all(
        comparison.get("comparison_status") == "benchmark_pass" for comparison in comparisons
    )

    status = (
        "valid"
        if all([benchmarks_only, no_coefficients, guard_ok, comparisons_ok])
        else "invalid"
    )

    return {
        "audit": "partial_integration_benchmark",
        "status": status,
        "can_advance_to_native_subintegral_dry_run": comparisons_ok,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
    }
