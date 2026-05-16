"""Divergence diagnostics for TT truncated inversion."""

from typing import Dict, List


def diagnose_tt_divergence(inversion_results: List[Dict[str, object]]) -> Dict[str, object]:
    l_values = [result.get("l_max") for result in inversion_results]

    if not l_values:
        divergence = "inconclusive"
        requires_regularization = False
    elif max(l_values) <= 5:
        divergence = "none"
        requires_regularization = False
    else:
        divergence = "mild"
        requires_regularization = True

    possible_causes = [
        "UV_growth",
        "degeneracy_scaling",
        "eigenvalue_behavior",
    ]

    return {
        "divergence": divergence,
        "requires_regularization": requires_regularization,
        "possible_causes": possible_causes,
        "promotes_claims": False,
    }
