"""Stability diagnostics for TT truncated inversion."""

from typing import Dict, List


def analyze_tt_stability(inversion_results: List[Dict[str, object]]) -> Dict[str, object]:
    l_values = [result.get("l_max") for result in inversion_results]
    unique_l = sorted({l_value for l_value in l_values if isinstance(l_value, int)})
    structure_preserved = all(
        result.get("structure") == "tensor_preserved" for result in inversion_results
    )
    status_consistent = len({result.get("status") for result in inversion_results}) == 1

    if not unique_l:
        sensitivity = "unknown"
        stability = "inconclusive"
    elif len(unique_l) < 2:
        sensitivity = "unknown"
        stability = "inconclusive"
    elif status_consistent and structure_preserved:
        sensitivity = "low"
        stability = "stable"
    else:
        sensitivity = "high"
        stability = "unstable"

    return {
        "stability": stability,
        "sensitivity_to_lmax": sensitivity,
        "structure_preserved": structure_preserved,
        "promotes_claims": False,
    }
