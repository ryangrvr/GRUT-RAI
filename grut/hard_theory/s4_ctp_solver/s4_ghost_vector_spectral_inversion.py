"""Ghost/vector spectral inversion on S4 (partial sum benchmark)."""

from typing import Dict, List

import sympy as sp

from grut.hard_theory.s4_ctp_solver.s4_ghost_operator import define_ghost_operator
from grut.hard_theory.s4_ctp_solver.s4_harmonic_spectra import define_s4_harmonic_spectra
from grut.hard_theory.s4_ctp_solver.s4_vector_harmonics import (
    build_vector_harmonics_structure,
)


def _select_vector_modes(
    vector_modes: List[Dict[str, object]], l_max: int
) -> List[Dict[str, object]]:
    return [mode for mode in vector_modes if mode.get("l", 0) <= l_max]


def perform_ghost_vector_spectral_inversion(
    l_max: int, radius: sp.Expr
) -> Dict[str, object]:
    ghost_operator = define_ghost_operator()
    vector_harmonics = build_vector_harmonics_structure()
    spectra = define_s4_harmonic_spectra()
    vector_modes = _select_vector_modes(spectra["vector_modes"], l_max)

    delta = sp.symbols("delta_mu_nu")
    Z = sp.symbols("Z", real=True)
    terms = []

    for mode in vector_modes:
        eigenvalue = mode["eigenvalue"]
        l_value = mode["l"]
        mode_label = mode["mode"]
        degeneracy = sp.Symbol(f"d_vector_{mode_label}_{l_value}")
        harmonic = sp.Function("V_l")(l_value, Z)
        if sp.simplify(eigenvalue) == 0:
            continue
        terms.append(degeneracy / eigenvalue * harmonic)

    expression = delta * sp.Add(*terms) if terms else sp.Integer(0)

    return {
        "inversion_id": "ghost_vector_spectral_partial",
        "l_max": l_max,
        "radius": radius,
        "expression": expression,
        "vector_eigenvalues": vector_modes,
        "ghost_operator": ghost_operator,
        "vector_harmonics": vector_harmonics,
        "status": "partial_vector_sum",
        "sector": "ghost_vector",
        "promotes_claims": False,
    }
