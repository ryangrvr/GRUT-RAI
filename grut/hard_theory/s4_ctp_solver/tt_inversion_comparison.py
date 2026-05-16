"""Structural comparison checks for TT truncated inversion."""

from typing import Dict, List

import sympy as sp


def _expression_has(expr: object, symbol: sp.Expr) -> bool:
    return sp.sympify(expr).has(symbol)


def compare_tt_truncated_structure(
    results: List[Dict[str, object]],
) -> Dict[str, object]:
    p_tt = sp.Function("P_TT")
    c_l = sp.Function("C_l")
    v_l = sp.Function("V_l")

    tensor_structure_ok = all(
        _expression_has(result.get("expression", 0), p_tt) for result in results
    )
    scalar_collapse = any(
        _expression_has(result.get("expression", 0), c_l) for result in results
    )
    vector_collapse = any(
        _expression_has(result.get("expression", 0), v_l) for result in results
    )

    projector_ok = all(
        result.get("projector", {}).get("projector_id") == "tt_projector_extended"
        for result in results
    )

    collapse_detected = scalar_collapse or vector_collapse or not tensor_structure_ok
    structure_valid = tensor_structure_ok and projector_ok and not collapse_detected

    return {
        "structure_valid": structure_valid,
        "collapse_detected": collapse_detected,
        "convergence_observed": False,
        "promotes_claims": False,
    }
