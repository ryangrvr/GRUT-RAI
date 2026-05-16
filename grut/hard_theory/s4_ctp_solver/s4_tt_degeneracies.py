"""TT degeneracy structure for S4 (structural)."""

from typing import Dict

import sympy as sp


def define_tt_degeneracies() -> Dict[str, object]:
    l = sp.symbols("l", integer=True, nonnegative=True)
    deg_tt = sp.Function("deg_TT")(l)

    return {
        "degeneracies_id": "s4_tt_degeneracies",
        "expression": deg_tt,
        "depends_on": ["l"],
        "status": "structural_placeholder",
        "promotes_claims": False,
    }
