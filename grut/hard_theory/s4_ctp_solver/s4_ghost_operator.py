"""Ghost operator definition on S4 (structural)."""

from typing import Dict

import sympy as sp


def define_ghost_operator() -> Dict[str, object]:
    R = sp.symbols("R")
    delta = sp.symbols("delta_mu_nu")
    laplacian = sp.symbols("Box_g")
    alpha = sp.symbols("alpha")
    structure = -laplacian * delta + alpha * R * delta

    return {
        "operator_id": "s4_fp_ghost_operator",
        "type": "vector_ghost",
        "background": "S4",
        "structure": structure,
        "gauge": "de_donder_placeholder",
        "status": "defined_not_inverted",
        "promotes_claims": False,
    }
