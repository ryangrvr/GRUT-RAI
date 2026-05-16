"""S4 scalar spectral basis utilities for Stage 3B benchmarks."""

from dataclasses import dataclass

import sympy as sp


@dataclass(frozen=True)
class ScalarSpectralMode:
    l: int
    radius: sp.Expr
    eigenvalue: sp.Expr
    degeneracy: sp.Expr


def scalar_laplacian_eigenvalue(l: int, radius: sp.Expr) -> sp.Expr:
    """Return scalar Laplacian eigenvalue on S4: l(l+3)/a^2."""
    return sp.Integer(l) * (l + 3) / radius**2


def scalar_harmonic_degeneracy(l: int) -> sp.Expr:
    """Return scalar harmonic degeneracy on S4."""
    return sp.Rational(1, 6) * (2 * l + 3) * (l + 2) * (l + 1)


def scalar_spectral_mode_record(l: int, radius: sp.Expr) -> ScalarSpectralMode:
    """Return spectral data record for scalar harmonics."""
    return ScalarSpectralMode(
        l=l,
        radius=radius,
        eigenvalue=scalar_laplacian_eigenvalue(l, radius),
        degeneracy=scalar_harmonic_degeneracy(l),
    )
