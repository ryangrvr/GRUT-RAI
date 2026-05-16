"""Cross-check route implementations for Stage 3E."""

from dataclasses import dataclass
from typing import Dict, List

import sympy as sp

from grut.hard_theory.s4_ctp_solver.heat_kernel import scalar_heat_kernel_coefficients
from grut.hard_theory.s4_ctp_solver.s4_green_functions import scalar_green_truncated
from grut.hard_theory.s4_ctp_solver.flatspace_loop_checks import one_loop_scalar_bubble_structure


@dataclass(frozen=True)
class RouteResult:
    route: str
    quantity_id: str
    expression: sp.Expr
    status: str
    scheme: str
    regulator: str
    omitted_terms: List[str]
    can_promote: bool


def _result(
    route: str,
    quantity_id: str,
    expression: sp.Expr,
    status: str,
    scheme: str,
    regulator: str,
    omitted_terms: List[str],
) -> RouteResult:
    return RouteResult(
        route=route,
        quantity_id=quantity_id,
        expression=expression,
        status=status,
        scheme=scheme,
        regulator=regulator,
        omitted_terms=omitted_terms,
        can_promote=False,
    )


def compute_via_heat_kernel(quantity_id: str, parameters: Dict[str, object]) -> RouteResult:
    coeffs = scalar_heat_kernel_coefficients()
    expr = coeffs.a2 if quantity_id == "scalar_1loop_effective_action" else coeffs.a1
    return _result(
        "heat_kernel",
        quantity_id,
        expr,
        status="benchmark",
        scheme="ms_bar",
        regulator="dim_reg",
        omitted_terms=["higher heat-kernel terms"],
    )


def compute_via_spectral_sum(quantity_id: str, parameters: Dict[str, object]) -> RouteResult:
    radius = parameters.get("radius", sp.symbols("a", positive=True))
    trunc = scalar_green_truncated(max_l=3, radius=radius)
    expr = sp.Symbol(f"{quantity_id}_spectral_trunc_l_{trunc.max_l}")
    return _result(
        "spectral",
        quantity_id,
        expr,
        status="partial",
        scheme="ms_bar",
        regulator="dim_reg",
        omitted_terms=["spectral tail", "higher l modes"],
    )


def compute_via_flat_limit(quantity_id: str, parameters: Dict[str, object]) -> RouteResult:
    bubble = one_loop_scalar_bubble_structure()
    expr = sp.Symbol(f"{quantity_id}_flat_limit") + bubble.expression
    return _result(
        "flat_limit",
        quantity_id,
        expr,
        status="structural_only",
        scheme="ms_bar",
        regulator="dim_reg",
        omitted_terms=["curvature corrections"],
    )


def compute_via_ward_identity(quantity_id: str, parameters: Dict[str, object]) -> RouteResult:
    expr = sp.Symbol(f"{quantity_id}_ward_structure")
    return _result(
        "ward_identity",
        quantity_id,
        expr,
        status="structural_only",
        scheme="ms_bar",
        regulator="dim_reg",
        omitted_terms=["ward consistency proof", "tensor contractions"],
    )
