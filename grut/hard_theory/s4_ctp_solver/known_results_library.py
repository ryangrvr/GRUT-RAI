"""Known analytic results for Stage 4A toy benchmarks."""

from dataclasses import dataclass
from typing import Dict

import sympy as sp


@dataclass(frozen=True)
class KnownResult:
    result_expression: sp.Expr
    regulator: str
    scheme: str
    source_note: str
    expected_behavior: str


def known_results_library() -> Dict[str, KnownResult]:
    eps = sp.symbols("epsilon")
    mu = sp.symbols("mu")
    m = sp.symbols("m")
    R = sp.symbols("R")
    finite_bubble = sp.Symbol("finite_bubble")
    finite_tadpole = sp.Symbol("finite_tadpole")

    return {
        "scalar_1loop_bubble_flat": KnownResult(
            result_expression=1 / eps + sp.log(mu**2 / m**2) + finite_bubble,
            regulator="dim_reg",
            scheme="ms_bar",
            source_note="flat-space scalar bubble (standard)",
            expected_behavior="pole_log_structure",
        ),
        "scalar_tadpole_flat": KnownResult(
            result_expression=m**2 * (1 / eps + sp.log(mu**2 / m**2) + finite_tadpole),
            regulator="dim_reg",
            scheme="ms_bar",
            source_note="flat-space scalar tadpole (standard)",
            expected_behavior="pole_log_structure_mass_scaled",
        ),
        "dim_reg_pole": KnownResult(
            result_expression=1 / eps,
            regulator="dim_reg",
            scheme="ms_bar",
            source_note="dimensional regularization pole",
            expected_behavior="pole_only",
        ),
        "log_divergence": KnownResult(
            result_expression=sp.log(mu**2 / m**2),
            regulator="dim_reg",
            scheme="ms_bar",
            source_note="log divergence structure",
            expected_behavior="log_only",
        ),
        "heat_kernel_trace_low_order": KnownResult(
            result_expression=1 + R / 6,
            regulator="none",
            scheme="none",
            source_note="heat-kernel trace low order",
            expected_behavior="a0_a1",
        ),
    }
