"""TT graviton operator definition on S4 (structural)."""

from typing import Dict

import sympy as sp


def define_tt_operator() -> Dict[str, object]:
    R = sp.symbols("R")
    laplacian = sp.symbols("Box_g")
    h = sp.symbols("h_mu_nu")
    alpha = sp.symbols("alpha")
    structure = -laplacian * h + alpha * R * h

    return {
        "operator_id": "s4_tt_operator",
        "field": "graviton",
        "type": "rank_2_tensor",
        "background": "S4",
        "structure": structure,
        "status": "defined_not_inverted",
        "promotes_claims": False,
    }
