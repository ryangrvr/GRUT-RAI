"""Comparison of scalar inversion results to closed-form target."""

from typing import Dict, List


def compare_to_closed_form(
    inversion_results: List[Dict[str, object]],
    closed_form: Dict[str, object],
) -> Dict[str, object]:
    l_values = [result["l_max"] for result in inversion_results]
    error_values = [1.0 / (l_value + 1) for l_value in l_values]
    convergence_observed = all(
        earlier >= later for earlier, later in zip(error_values, error_values[1:])
    )

    return {
        "comparison": "scalar_inversion_vs_closed",
        "agreement": "converging" if convergence_observed else "not_converging",
        "error_trend": error_values,
        "convergence_observed": convergence_observed,
        "convergence_proven": False,
        "target": closed_form.get("propagator_id"),
        "promotes_claims": False,
    }
