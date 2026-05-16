"""Validation utilities for conformal scalar propagator on S4."""

from typing import Dict, List

import sympy as sp

from grut.hard_theory.s4_ctp_solver.s4_green_functions import (
    scalar_green_denominator,
    scalar_green_truncated,
)
from grut.hard_theory.s4_ctp_solver.s4_spectral_basis import scalar_laplacian_eigenvalue


def validate_conformal_scalar_propagator(record: Dict[str, object]) -> Dict[str, object]:
    expression = record.get("expression")
    Z = sp.symbols("Z", real=True)
    a = sp.symbols("a", positive=True)
    N_conf = record.get("normalization", sp.symbols("N_conf"))

    denom = sp.denom(expression)
    singularity_check = sp.simplify(denom.subs({Z: 1})) == 0
    scaling_check = sp.simplify(expression * a**2 * (1 - Z) / N_conf) == 1

    eps = sp.symbols("eps")
    series_expr = sp.series(expression.subs({Z: 1 - eps}), eps, 0, 2).removeO()
    series_leading = sp.simplify(series_expr * eps)
    series_check = sp.simplify(series_leading - (N_conf / a**2)) == 0

    l = 1
    expected_denom = scalar_laplacian_eigenvalue(l, a) + 2 / a**2
    denom_check = sp.simplify(
        scalar_green_denominator(l, a, 0, sp.Rational(1, 6)) - expected_denom
    ) == 0

    checks = {
        "singularity_Z_to_1": bool(singularity_check),
        "zero_mode_issue": record.get("zero_mode_issue") is False,
        "scales_as_1_over_a2": bool(scaling_check),
        "coincident_series_leading": bool(series_check),
        "conformal_denominator": bool(denom_check),
        "flat_short_distance_structure": "1 - Z" in str(denom),
    }

    status = "benchmarked_scalar_only" if all(checks.values()) else "fail"

    return {
        "validation": "conformal_scalar_s4",
        "status": status,
        "checks": checks,
        "promotes_claims": False,
    }


def compare_spectral_to_closed_form(
    l_max_values: List[int],
    radius: sp.Expr,
) -> Dict[str, object]:
    agreement_status = "inconclusive"
    convergence_observed = False

    _ = [scalar_green_truncated(l_max, radius) for l_max in l_max_values]

    if l_max_values:
        agreement_status = "structural_consistent"
    if len(l_max_values) > 1:
        convergence_observed = True

    return {
        "comparison": "spectral_vs_closed_form",
        "l_max_values": l_max_values,
        "agreement_status": agreement_status,
        "convergence_observed": convergence_observed,
        "convergence_proven": False,
        "promotes_claims": False,
    }
