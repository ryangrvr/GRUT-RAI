"""Heat-kernel / Seeley-DeWitt coefficients for Stage 2 benchmarks."""

from dataclasses import dataclass
from typing import Dict

import sympy as sp

R = sp.symbols("R")
RICCI2 = sp.symbols("R_mu_nu_R_mu_nu")
RIEMANN2 = sp.symbols("R_mu_nu_rho_sigma_R_mu_nu_rho_sigma")
BOX_R = sp.symbols("box_R")


@dataclass(frozen=True)
class HeatKernelCoefficients:
    a0: sp.Expr
    a1: sp.Expr
    a2: sp.Expr


def scalar_heat_kernel_coefficients() -> HeatKernelCoefficients:
    """Return a0, a1, a2 for a minimal scalar Laplacian.

    Uses standard coefficients:
        a0 = 1
        a1 = R/6
        a2 = (1/180) * (Riemann2 - Ricci2 + (5/2) R^2 - 6 boxR)
    """
    a0 = sp.Integer(1)
    a1 = R / 6
    a2 = (sp.Rational(1, 180) * (RIEMANN2 - RICCI2 + sp.Rational(5, 2) * R**2 - 6 * BOX_R))
    return HeatKernelCoefficients(a0=a0, a1=a1, a2=a2)


def s4_invariants(radius_a: sp.Expr) -> Dict[sp.Symbol, sp.Expr]:
    """Return S4 constant-curvature invariants for substitution."""
    return {
        R: 12 / radius_a**2,
        RICCI2: 36 / radius_a**4,
        RIEMANN2: 24 / radius_a**4,
        BOX_R: 0,
    }


def euler_density_s4(radius_a: sp.Expr) -> sp.Expr:
    """Euler density E4 on S4: Riemann2 - 4 Ricci2 + R^2."""
    subs = s4_invariants(radius_a)
    return (RIEMANN2 - 4 * RICCI2 + R**2).subs(subs)
