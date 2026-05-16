"""Spectral and curvature expansions for Stage 4C subsets."""

from typing import Dict, List

import sympy as sp

from grut.hard_theory.s4_ctp_solver.s4_spectral_basis import (
    scalar_harmonic_degeneracy,
)
from grut.hard_theory.s4_ctp_solver.s4_green_functions import scalar_green_denominator
from grut.hard_theory.s4_ctp_solver.heat_kernel import scalar_heat_kernel_coefficients
from grut.hard_theory.s4_ctp_solver.three_loop_subset_s4_scalar import S4SubsetTopology


def evaluate_s4_subset_via_spectral(
    topology: S4SubsetTopology, l_max: int, radius: sp.Expr
) -> Dict[str, object]:
    m = sp.symbols("m")
    xi = sp.Rational(1, 6)
    terms = []
    for l in range(l_max + 1):
        degeneracy = scalar_harmonic_degeneracy(l)
        denom = scalar_green_denominator(l, radius, mass_sq=m**2, xi=xi)
        terms.append(sp.Mul(degeneracy, 1 / denom, evaluate=False))

    expr = sp.Add(*terms, evaluate=False)

    return {
        "topology_id": topology.topology_id,
        "method": "spectral_truncation",
        "l_max": l_max,
        "expression": expr,
        "convergence_status": "partial",
        "omitted_terms": ["spectral tail", "higher modes"],
        "status": "partial_curved_subset",
        "promotes_claims": False,
        "flat_limit_reference": "stage4b_scalar_subset",
    }


def evaluate_s4_subset_via_curvature_expansion(
    topology: S4SubsetTopology, order: int, radius: sp.Expr
) -> Dict[str, object]:
    coeffs = scalar_heat_kernel_coefficients()
    R = 12 / radius**2
    expr = coeffs.a0 + coeffs.a1 * R
    if order >= 2:
        expr += coeffs.a2 * R**2

    return {
        "topology_id": topology.topology_id,
        "method": "curvature_expansion",
        "order": order,
        "expression": expr,
        "status": "curvature_expansion_partial",
        "omitted_terms": ["higher curvature terms"],
        "promotes_claims": False,
        "flat_limit_reference": "stage4b_scalar_subset",
    }
