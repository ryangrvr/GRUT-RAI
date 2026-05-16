"""Scalar spectral inversion on S4 (partial sum benchmark)."""

from typing import Dict

import sympy as sp

from grut.hard_theory.s4_ctp_solver.s4_spectral_basis import (
    scalar_harmonic_degeneracy,
    scalar_laplacian_eigenvalue,
)


def perform_scalar_spectral_inversion(l_max: int, radius: sp.Expr) -> Dict[str, object]:
    Z = sp.symbols("Z", real=True)
    terms = []
    for l in range(l_max + 1):
        eigenvalue = scalar_laplacian_eigenvalue(l, radius)
        degeneracy = scalar_harmonic_degeneracy(l)
        if sp.simplify(eigenvalue) == 0:
            continue
        harmonic = sp.Function("C_l")(l, Z)
        terms.append(degeneracy / eigenvalue * harmonic)

    expression = sp.Add(*terms) if terms else sp.Integer(0)

    return {
        "inversion_id": "scalar_spectral_partial",
        "l_max": l_max,
        "radius": radius,
        "expression": expression,
        "status": "partial_sum",
        "sector": "scalar",
        "promotes_claims": False,
    }
