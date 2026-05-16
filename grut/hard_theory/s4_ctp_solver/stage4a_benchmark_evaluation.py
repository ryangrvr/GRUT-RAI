"""Stage 4A benchmark evaluation gate."""

from typing import Dict, List

import sympy as sp

from grut.hard_theory.s4_ctp_solver.toy_integrals_flat import (
    compute_scalar_bubble_integral,
    compute_scalar_tadpole_integral,
)
from grut.hard_theory.s4_ctp_solver.toy_integrals_curved import (
    heat_kernel_trace_low_order,
)
from grut.hard_theory.s4_ctp_solver.evaluation_engine import (
    evaluate_with_benchmark_check,
)


def run_stage4a_benchmark_evaluation() -> Dict[str, object]:
    m = sp.symbols("m", positive=True)
    bubble = compute_scalar_bubble_integral(dimension=4, mass=m, regulator="dim_reg")
    tadpole = compute_scalar_tadpole_integral(dimension=4, mass=m, regulator="dim_reg")
    heat_trace = heat_kernel_trace_low_order()

    evaluations = [
        evaluate_with_benchmark_check(bubble, "scalar_1loop_bubble_flat"),
        evaluate_with_benchmark_check(tadpole, "scalar_tadpole_flat"),
        evaluate_with_benchmark_check(heat_trace, "heat_kernel_trace_low_order"),
    ]

    failures = [e["computation"] for e in evaluations if not e["matches_known_result"]]
    all_passed = len(failures) == 0

    return {
        "stage": "4A",
        "status": "benchmark_evaluation",
        "evaluations_run": len(evaluations),
        "all_passed": all_passed,
        "any_failures": failures,
        "can_attempt_partial_3loop": all_passed,
        "can_compute_full_3loop": False,
        "promotes_claims": False,
    }
