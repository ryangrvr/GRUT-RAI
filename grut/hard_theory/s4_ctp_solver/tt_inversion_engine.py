"""TT truncated inversion engine for multiple cutoffs."""

from typing import Dict, List

import sympy as sp

from grut.hard_theory.s4_ctp_solver.s4_tt_truncated_inversion import (
    perform_tt_truncated_inversion,
)


def run_tt_inversion_engine(l_values: List[int]) -> Dict[str, object]:
    radius = sp.symbols("a", positive=True)
    results = [perform_tt_truncated_inversion(l_max, radius) for l_max in l_values]

    return {
        "engine": "tt_inversion_engine",
        "l_values": l_values,
        "results": results,
        "promotes_claims": False,
    }
