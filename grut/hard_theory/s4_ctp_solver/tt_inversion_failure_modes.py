"""Failure mode classification for TT truncated inversion."""

from typing import Dict


def classify_tt_failure_modes(results: Dict[str, object]) -> Dict[str, object]:
    stability = results.get("stability", {})
    divergence = results.get("divergence", {})
    comparison = results.get("comparison", {})

    if comparison.get("collapse_detected"):
        failure_mode = "tensor_structure_breakdown"
        confidence = "high"
        explanation = "Tensor structure failed preservation checks."
    elif divergence.get("divergence") == "mild":
        failure_mode = "divergence_ladder"
        confidence = "medium"
        explanation = "Truncated sums suggest mild divergence without regularization."
    elif stability.get("stability") == "unstable":
        failure_mode = "spectral_instability"
        confidence = "medium"
        explanation = "Results vary with cutoff selection."
    else:
        failure_mode = "no_failure"
        confidence = "low"
        explanation = "No explicit failure detected under truncated diagnostics."

    return {
        "failure_mode": failure_mode,
        "confidence": confidence,
        "explanation": explanation,
        "promotes_claims": False,
    }
