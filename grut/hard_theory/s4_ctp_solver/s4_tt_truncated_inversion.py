"""TT truncated spectral inversion on S4 (partial attempt)."""

from typing import Dict

import sympy as sp

from grut.hard_theory.s4_ctp_solver.s4_tt_degeneracies import define_tt_degeneracies
from grut.hard_theory.s4_ctp_solver.s4_tt_eigenvalues import define_tt_eigenvalues
from grut.hard_theory.s4_ctp_solver.s4_tt_projector_extended import extend_tt_projector


def perform_tt_truncated_inversion(l_max: int, radius: sp.Expr) -> Dict[str, object]:
    l_symbol = sp.symbols("l", integer=True, nonnegative=True)
    eigenvalues = define_tt_eigenvalues()
    degeneracies = define_tt_degeneracies()
    projector = extend_tt_projector()

    eigenvalue_expr = eigenvalues["expression"].subs({sp.symbols("a"): radius})
    degeneracy_expr = degeneracies["expression"]
    projector_symbol = sp.Function("P_TT")

    terms = []
    for l_value in range(2, l_max + 1):
        eigenvalue_l = eigenvalue_expr.subs({l_symbol: l_value})
        degeneracy_l = degeneracy_expr.subs({l_symbol: l_value})
        if sp.simplify(eigenvalue_l) == 0:
            continue
        terms.append(degeneracy_l / eigenvalue_l * projector_symbol(l_value))

    expression = sp.Add(*terms) if terms else sp.Integer(0)

    return {
        "inversion_id": "tt_truncated",
        "l_max": l_max,
        "radius": radius,
        "expression": expression,
        "eigenvalues": eigenvalues,
        "degeneracies": degeneracies,
        "projector": projector,
        "status": "partial_attempt",
        "structure": "tensor_preserved",
        "promotes_claims": False,
    }
