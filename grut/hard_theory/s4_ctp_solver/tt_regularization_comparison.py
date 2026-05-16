"""Comparison across TT regularization schemes."""

from typing import Dict, List


def compare_regularization_results(results: List[Dict[str, object]]) -> Dict[str, object]:
    schemes = {result.get("scheme") for result in results}
    structure_preserved = all(result.get("structure_preserved") for result in results)
    scheme_sums = {
        result.get("scheme"): str(result.get("regularized_sum")) for result in results
    }
    cutoff_sum = scheme_sums.get("cutoff")
    damping_sum = scheme_sums.get("exponential_damping")
    scheme_contrast = cutoff_sum is not None and damping_sum is not None and cutoff_sum != damping_sum

    divergence_suppressed = scheme_contrast
    stability_improved = divergence_suppressed and structure_preserved
    best_scheme = (
        "exponential_damping" if stability_improved else "cutoff"
    )
    convergence_observed = False

    return {
        "stability_improved": stability_improved,
        "structure_preserved": structure_preserved,
        "divergence_suppressed": divergence_suppressed,
        "best_scheme": best_scheme,
        "convergence_observed": convergence_observed,
        "convergence_proven": False,
        "promotes_claims": False,
    }
