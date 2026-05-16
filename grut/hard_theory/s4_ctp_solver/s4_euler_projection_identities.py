"""S4 Euler-anomaly projection identities."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.heat_kernel import euler_density_s4, s4_invariants
import sympy as sp


def build_s4_euler_identities() -> Dict[str, object]:
    radius = sp.symbols("a", positive=True)
    invariants = s4_invariants(radius)
    euler_density = euler_density_s4(radius)

    return {
        "s4_conformally_flat": True,
        "s4_weyl_zero": True,
        "euler_density_survives": True,
        "constant_curvature": True,
        "invariants": invariants,
        "euler_density": euler_density,
        "promotes_claims": False,
    }
