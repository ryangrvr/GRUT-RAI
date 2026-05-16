"""Audit for scalar spectral inversion benchmark."""

from typing import Dict, List


def audit_scalar_inversion(results: Dict[str, object]) -> Dict[str, object]:
    inversion_results = results.get("results", [])
    sector_ok = all(result.get("sector") == "scalar" for result in inversion_results)

    limitations: List[str] = [
        "finite_l_max",
        "no uniform convergence proof",
        "coincident singularity not fully resolved",
    ]

    status = "valid_benchmark" if sector_ok else "invalid"

    return {
        "audit": "scalar_inversion",
        "status": status,
        "convergence_observed": results.get("convergence_observed", False),
        "limitations": limitations,
        "promotes_claims": False,
    }
