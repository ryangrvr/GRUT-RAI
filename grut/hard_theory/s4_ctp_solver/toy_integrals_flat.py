"""Flat-space toy integrals for Stage 4A benchmarks."""

from dataclasses import dataclass
from typing import Dict

import sympy as sp


@dataclass(frozen=True)
class ToyIntegralResult:
    expression: sp.Expr
    pole_structure: str
    finite_part_placeholder: sp.Expr
    regulator: str
    scheme: str
    status: str


def compute_scalar_bubble_integral(
    dimension: int, mass: sp.Expr, regulator: str
) -> ToyIntegralResult:
    eps = sp.symbols("epsilon")
    mu = sp.symbols("mu")
    finite = sp.Symbol("finite_bubble")
    expr = 1 / eps + sp.log(mu**2 / mass**2) + finite
    return ToyIntegralResult(
        expression=expr,
        pole_structure="1/epsilon",
        finite_part_placeholder=finite,
        regulator=regulator,
        scheme="ms_bar",
        status="benchmark_evaluated",
    )


def compute_scalar_tadpole_integral(
    dimension: int, mass: sp.Expr, regulator: str
) -> ToyIntegralResult:
    eps = sp.symbols("epsilon")
    mu = sp.symbols("mu")
    finite = sp.Symbol("finite_tadpole")
    expr = mass**2 * (1 / eps + sp.log(mu**2 / mass**2) + finite)
    return ToyIntegralResult(
        expression=expr,
        pole_structure="1/epsilon",
        finite_part_placeholder=finite,
        regulator=regulator,
        scheme="ms_bar",
        status="benchmark_evaluated",
    )
