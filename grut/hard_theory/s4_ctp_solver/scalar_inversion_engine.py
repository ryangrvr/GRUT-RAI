"""Scalar inversion engine for multiple spectral cutoffs."""

from typing import Dict, List

import sympy as sp

from grut.hard_theory.s4_ctp_solver.s4_scalar_spectral_inversion import (
    perform_scalar_spectral_inversion,
)


def run_scalar_inversion_engine(l_values: List[int]) -> Dict[str, object]:
    radius = sp.symbols("a", positive=True)
    results = [perform_scalar_spectral_inversion(l_max, radius) for l_max in l_values]

    return {
        "engine": "scalar_inversion_engine",
        "l_values": l_values,
        "results": results,
        "promotes_claims": False,
    }
