"""Propagator ingredient benchmarks for Stage 3B."""

from typing import Dict

import sympy as sp

from grut.hard_theory.s4_ctp_solver.s4_green_functions import scalar_green_denominator


def benchmark_scalar_conformal_s4(radius: sp.Expr) -> Dict[str, object]:
    denom_l0 = scalar_green_denominator(0, radius, mass_sq=0, xi=sp.Rational(1, 6))
    target = 2 / radius**2
    status = "benchmarked" if sp.simplify(denom_l0 - target) == 0 else "warning"
    reason = "conformal denominator matches 2/a^2" if status == "benchmarked" else "mismatch"
    return {
        "benchmark": "scalar_conformal_s4",
        "status": status,
        "promotes_stage": False,
        "reason": reason,
    }


def benchmark_scalar_minimal_zero_mode_warning(radius: sp.Expr) -> Dict[str, object]:
    denom_l0 = scalar_green_denominator(0, radius, mass_sq=0, xi=0)
    status = "warning" if sp.simplify(denom_l0) == 0 else "benchmarked"
    reason = "minimal massless scalar has l=0 zero mode" if status == "warning" else "no zero mode"
    return {
        "benchmark": "scalar_minimal_zero_mode",
        "status": status,
        "promotes_stage": False,
        "reason": reason,
    }


def benchmark_flat_large_radius_limit_structure() -> Dict[str, object]:
    return {
        "benchmark": "flat_large_radius_limit",
        "status": "structural_only",
        "promotes_stage": False,
        "reason": "flat-limit structure only; no evaluation",
    }
