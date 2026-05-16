"""Audit for TT truncated inversion attempt."""

from typing import Dict, List


def audit_tt_inversion(results: Dict[str, object]) -> Dict[str, object]:
    inversion_results = results.get("results", [])
    comparison = results.get("comparison", {})
    guard = results.get("guard", {})

    no_extraction = all(
        result.get("status") == "partial_attempt" for result in inversion_results
    )
    no_closure_claim = all(
        result.get("structure") == "tensor_preserved" for result in inversion_results
    )
    no_convergence_claim = comparison.get("convergence_observed") is False
    guard_ok = guard.get("status") == "pass"

    limitations: List[str] = [
        "finite_l_max",
        "truncated_tt_sum_only",
        "no TT closure claims",
        "no convergence proof",
    ]

    status = (
        "valid_benchmark"
        if all([no_extraction, no_closure_claim, no_convergence_claim, guard_ok])
        else "invalid"
    )

    return {
        "audit": "tt_truncated_inversion",
        "status": status,
        "limitations": limitations,
        "promotes_claims": False,
    }
