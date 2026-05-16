"""Closed-form conformal scalar propagator on S4 (structural)."""

from typing import Dict

import sympy as sp


def build_conformal_scalar_propagator_closed_form() -> Dict[str, object]:
    Z = sp.symbols("Z", real=True)
    a = sp.symbols("a", positive=True)
    N_conf = sp.symbols("N_conf")
    expression = N_conf / (a**2 * (1 - Z))

    return {
        "propagator_id": "s4_conformal_scalar_closed_form",
        "field": "scalar",
        "coupling": "conformal",
        "background": "S4",
        "expression": expression,
        "normalization": N_conf,
        "singularities": ["coincident_point_Z_to_1"],
        "zero_mode_issue": False,
        "status": "closed_form_benchmarked_scalar_only",
        "promotes_claims": False,
    }
