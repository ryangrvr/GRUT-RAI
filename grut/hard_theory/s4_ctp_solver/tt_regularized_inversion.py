"""Regularized TT spectral inversion (partial)."""

from typing import Dict

import sympy as sp

from grut.hard_theory.s4_ctp_solver.s4_tt_degeneracies import define_tt_degeneracies
from grut.hard_theory.s4_ctp_solver.s4_tt_eigenvalues import define_tt_eigenvalues
from grut.hard_theory.s4_ctp_solver.s4_tt_projector_extended import extend_tt_projector


def perform_regularized_tt_inversion(
    l_max: int, epsilon: sp.Expr, scheme: str
) -> Dict[str, object]:
    l_symbol = sp.symbols("l", integer=True, nonnegative=True)
    eigenvalues = define_tt_eigenvalues()
    degeneracies = define_tt_degeneracies()
    projector = extend_tt_projector()

    eigenvalue_expr = eigenvalues["expression"]
    degeneracy_expr = degeneracies["expression"]
    projector_symbol = sp.Function("P_TT")

    terms = []
    if scheme in {"cutoff", "exponential_damping"}:
        for l_value in range(2, l_max + 1):
            eigenvalue_l = eigenvalue_expr.subs({l_symbol: l_value})
            degeneracy_l = degeneracy_expr.subs({l_symbol: l_value})
            if sp.simplify(eigenvalue_l) == 0:
                continue
            weight = sp.Integer(1)
            if scheme == "exponential_damping":
                weight = sp.exp(-epsilon * l_value)
            terms.append(weight * degeneracy_l / eigenvalue_l * projector_symbol(l_value))
        regularized_sum = sp.Add(*terms) if terms else sp.Integer(0)
    elif scheme == "zeta_placeholder":
        zeta_placeholder = sp.Symbol("zeta_regularization_placeholder")
        regularized_sum = zeta_placeholder * projector_symbol(l_symbol)
    else:
        regularized_sum = sp.Integer(0)

    structure_preserved = sp.sympify(regularized_sum).has(projector_symbol)

    return {
        "scheme": scheme,
        "l_max": l_max,
        "epsilon": epsilon,
        "regularized_sum": regularized_sum,
        "structure_preserved": structure_preserved,
        "status": "regularized_partial",
        "promotes_claims": False,
    }
