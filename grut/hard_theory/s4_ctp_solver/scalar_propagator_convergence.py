"""Convergence diagnostics for scalar spectral truncation."""

from typing import Dict, List


def diagnose_scalar_spectral_convergence(l_max_values: List[int]) -> Dict[str, object]:
    trend = "insufficient_data"
    if len(l_max_values) > 1:
        trend = "no_proof"

    return {
        "diagnostic": "scalar_spectral_convergence",
        "status": "diagnostic_only",
        "trend": trend,
        "convergence_proven": False,
        "missing_for_proof": [
            "uniform convergence bound",
            "coincident-limit regularization",
            "renormalized distribution treatment",
        ],
        "promotes_claims": False,
    }
