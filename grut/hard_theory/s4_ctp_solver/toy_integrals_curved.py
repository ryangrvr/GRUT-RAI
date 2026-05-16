"""Curved-space toy integrals for Stage 4A benchmarks."""

from dataclasses import dataclass
from typing import Dict

import sympy as sp

from grut.hard_theory.s4_ctp_solver.heat_kernel import scalar_heat_kernel_coefficients
from grut.hard_theory.s4_ctp_solver.s4_green_functions import scalar_green_truncated


@dataclass(frozen=True)
class CurvedToyResult:
    expression: sp.Expr
    status: str
    truncation: str
    metadata: Dict[str, object]


def heat_kernel_trace_low_order(radius: sp.Expr | None = None) -> CurvedToyResult:
    coeffs = scalar_heat_kernel_coefficients()
    R = sp.symbols("R")
    expr = coeffs.a0 + coeffs.a1
    if radius is not None:
        R_value = 12 / radius**2
        expr = expr.subs({sp.symbols("R"): R_value})
    return CurvedToyResult(
        expression=expr,
        status="benchmark_evaluated",
        truncation="a0+a1",
        metadata={"radius": radius, "R_symbol": R},
    )


def curvature_corrected_propagator_expansion(radius: sp.Expr) -> CurvedToyResult:
    p2 = sp.symbols("p2")
    R = 12 / radius**2
    alpha = sp.Symbol("alpha_R")
    expr = 1 / p2 + alpha * R
    return CurvedToyResult(
        expression=expr,
        status="partial_benchmark",
        truncation="O(R)",
        metadata={"radius": radius},
    )


def s4_scalar_mode_sum_truncation(max_l: int, radius: sp.Expr) -> CurvedToyResult:
    trunc = scalar_green_truncated(max_l=max_l, radius=radius)
    expr = sp.Symbol(f"spectral_sum_trunc_l_{max_l}")
    return CurvedToyResult(
        expression=expr,
        status="partial_benchmark",
        truncation=f"l<={max_l}",
        metadata={"radius": radius, "max_l": trunc.max_l},
    )
