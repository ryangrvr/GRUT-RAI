"""Structural comparison checks for ghost/vector spectral inversion."""

from typing import Dict, List

import sympy as sp

from grut.hard_theory.s4_ctp_solver.s4_ghost_operator import define_ghost_operator


def compare_ghost_vector_structure(
    results: List[Dict[str, object]],
) -> Dict[str, object]:
    delta = sp.symbols("delta_mu_nu")
    expected_operator = define_ghost_operator()["structure"]

    vector_index_ok = all(
        sp.sympify(result.get("expression", sp.Integer(0))).has(delta)
        for result in results
    )
    ghost_operator_ok = all(
        result.get("ghost_operator", {}).get("structure") == expected_operator
        for result in results
    )
    vector_structure_ok = all(
        result.get("vector_harmonics", {}).get("structure") == "vector_harmonics"
        for result in results
    )
    cutoff_stable = all(
        result.get("status") == "partial_vector_sum" for result in results
    )

    scalar_collapse_detected = not (vector_index_ok and vector_structure_ok)

    if not ghost_operator_ok or scalar_collapse_detected:
        status = "fail"
    elif cutoff_stable and vector_index_ok:
        status = "structurally_consistent"
    else:
        status = "inconclusive"

    convergence_observed = cutoff_stable and len(results) > 1

    return {
        "comparison": "ghost_vector_structure",
        "status": status,
        "scalar_collapse_detected": scalar_collapse_detected,
        "convergence_observed": convergence_observed,
        "convergence_proven": False,
        "promotes_claims": False,
    }
