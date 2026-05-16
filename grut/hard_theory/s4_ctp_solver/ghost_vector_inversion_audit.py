"""Audit for ghost/vector spectral inversion benchmark."""

from typing import Dict, List


def audit_ghost_vector_inversion(results: Dict[str, object]) -> Dict[str, object]:
    inversion_results = results.get("results", [])
    comparison = results.get("comparison", {})

    sector_ok = all(
        result.get("sector") == "ghost_vector" for result in inversion_results
    )
    vector_only_ok = all(
        result.get("vector_harmonics", {}).get("structure") == "vector_harmonics"
        for result in inversion_results
    )
    no_tt_usage = all(
        "tt" not in str(result).lower() for result in inversion_results
    )
    no_extraction = all(
        result.get("status") == "partial_vector_sum" for result in inversion_results
    )
    no_scalar_collapse = not comparison.get("scalar_collapse_detected", True)
    convergence_not_overstated = comparison.get("convergence_proven") is False

    limitations: List[str] = [
        "finite_l_max",
        "vector eigenvalues structural unless benchmarked",
        "no full vector propagator closure",
        "no uniform convergence proof",
    ]

    status = (
        "valid_benchmark"
        if all(
            [
                sector_ok,
                vector_only_ok,
                no_tt_usage,
                no_extraction,
                no_scalar_collapse,
                convergence_not_overstated,
            ]
        )
        else "invalid"
    )

    return {
        "audit": "ghost_vector_inversion",
        "status": status,
        "limitations": limitations,
        "promotes_claims": False,
    }
