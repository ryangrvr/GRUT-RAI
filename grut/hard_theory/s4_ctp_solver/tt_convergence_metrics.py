"""Convergence metrics for regularized TT inversion."""

from typing import Dict, List

import sympy as sp


def _get_sort_key(entry: Dict[str, object]) -> int:
    l_max = entry.get("l_max")
    return l_max if isinstance(l_max, int) else -1


def compute_tt_convergence_metrics(
    regularized_results: List[Dict[str, object]],
) -> Dict[str, object]:
    sorted_results = sorted(regularized_results, key=_get_sort_key)
    successive_differences: List[sp.Expr] = []
    relative_changes: List[sp.Expr] = []

    for prev, curr in zip(sorted_results, sorted_results[1:]):
        prev_sum = sp.sympify(prev.get("regularized_sum", 0))
        curr_sum = sp.sympify(curr.get("regularized_sum", 0))
        diff = curr_sum - prev_sum
        denom = sp.Abs(prev_sum) + sp.Integer(1)
        successive_differences.append(diff)
        relative_changes.append(sp.Abs(diff) / denom)

    cutoff_sum = None
    damping_sum = None
    zeta_present = False
    for entry in regularized_results:
        scheme = entry.get("scheme")
        if scheme == "cutoff":
            cutoff_sum = sp.sympify(entry.get("regularized_sum", 0))
        elif scheme == "exponential_damping":
            damping_sum = sp.sympify(entry.get("regularized_sum", 0))
        elif scheme == "zeta_placeholder":
            zeta_present = True

    if cutoff_sum is None or damping_sum is None:
        damping_sensitivity = "unknown"
    elif cutoff_sum == damping_sum:
        damping_sensitivity = "low"
    else:
        damping_sensitivity = "medium"

    if zeta_present and damping_sensitivity != "low":
        scheme_sensitivity = "medium"
    elif zeta_present:
        scheme_sensitivity = "low"
    else:
        scheme_sensitivity = "low"

    structure_preserved = all(
        entry.get("structure_preserved") is True for entry in regularized_results
    )

    return {
        "metrics_id": "tt_convergence_metrics",
        "successive_differences": successive_differences,
        "relative_changes": relative_changes,
        "damping_sensitivity": damping_sensitivity,
        "scheme_sensitivity": scheme_sensitivity,
        "structure_preserved": structure_preserved,
        "promotes_claims": False,
    }
