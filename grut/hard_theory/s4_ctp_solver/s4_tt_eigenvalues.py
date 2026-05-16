"""TT eigenvalue structure for S4 (structural)."""

from typing import Dict

import sympy as sp


def define_tt_eigenvalues() -> Dict[str, object]:
    l = sp.symbols("l", integer=True, nonnegative=True)
    a = sp.symbols("a", positive=True)
    c_tt = sp.symbols("c_tt")
    expression = (l * (l + 3) + c_tt) / a**2

    return {
        "eigenvalues_id": "s4_tt_eigenvalues",
        "expression": expression,
        "depends_on": ["l", "a"],
        "status": "defined_not_summed",
        "promotes_claims": False,
    }
