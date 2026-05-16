"""Scalar Green-function spectral representations on S4 (truncated)."""

from dataclasses import dataclass
from typing import List

import sympy as sp

from grut.hard_theory.s4_ctp_solver.s4_spectral_basis import (
    scalar_laplacian_eigenvalue,
    scalar_harmonic_degeneracy,
)


@dataclass(frozen=True)
class ScalarGreenTruncation:
    max_l: int
    radius: sp.Expr
    mass_sq: sp.Expr
    xi: sp.Expr
    terms: List[dict]
    truncation_error_status: str
    status: str


def scalar_green_denominator(l: int, radius: sp.Expr, mass_sq: sp.Expr, xi: sp.Expr) -> sp.Expr:
    """Return denominator lambda_l + m^2 + xi R for scalar Green function."""
    R = 12 / radius**2
    return scalar_laplacian_eigenvalue(l, radius) + mass_sq + xi * R


def scalar_green_spectral_terms(
    max_l: int,
    radius: sp.Expr,
    mass_sq: sp.Expr = 0,
    xi: sp.Expr = sp.Rational(1, 6),
) -> List[dict]:
    """Return truncated spectral terms for scalar Green function on S4."""
    cos_gamma = sp.symbols("cos_gamma")
    terms = []
    for l in range(max_l + 1):
        denom = scalar_green_denominator(l, radius, mass_sq, xi)
        terms.append(
            {
                "l": l,
                "degeneracy": scalar_harmonic_degeneracy(l),
                "denominator": denom,
                "C_l": sp.Function("C_l")(l, cos_gamma),
            }
        )
    return terms


def scalar_green_truncated(
    max_l: int,
    radius: sp.Expr,
    mass_sq: sp.Expr = 0,
    xi: sp.Expr = sp.Rational(1, 6),
) -> ScalarGreenTruncation:
    """Return a truncated spectral representation (no closed-form claim)."""
    return ScalarGreenTruncation(
        max_l=max_l,
        radius=radius,
        mass_sq=mass_sq,
        xi=xi,
        terms=scalar_green_spectral_terms(max_l, radius, mass_sq, xi),
        truncation_error_status="not_bounded",
        status="truncated_spectral_representation",
    )
