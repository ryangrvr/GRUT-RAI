"""Audit for TT regularized inversion."""

from typing import Dict, List


def audit_regularized_inversion(results: Dict[str, object]) -> Dict[str, object]:
    regularized = results.get("regularized", [])
    comparison = results.get("comparison", {})

    no_extraction = all(
        entry.get("status") == "regularized_partial" for entry in regularized
    )
    structure_ok = comparison.get("structure_preserved") is True
    no_convergence_claim = comparison.get("convergence_proven") is False
    no_r_extraction = "R" not in str(regularized)

    limitations: List[str] = [
        "finite cutoff",
        "scheme dependence",
        "no renormalization performed",
    ]

    status = (
        "valid"
        if all([no_extraction, structure_ok, no_convergence_claim, no_r_extraction])
        else "invalid"
    )

    return {
        "audit": "tt_regularization",
        "status": status,
        "limitations": limitations,
        "promotes_claims": False,
    }
