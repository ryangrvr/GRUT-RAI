"""Stage 4C curved S4 scalar subset evaluation."""

from typing import Dict, List

import sympy as sp

from grut.hard_theory.s4_ctp_solver.three_loop_subset_s4_scalar import (
    s4_scalar_subset_topologies,
)
from grut.hard_theory.s4_ctp_solver.s4_subset_evaluation_engine import (
    evaluate_s4_subset,
    run_consistency_checks,
)


def run_stage4c_s4_subset_evaluation() -> Dict[str, object]:
    radius = sp.symbols("a", positive=True)
    topologies = s4_scalar_subset_topologies(l_max=3)
    results = [evaluate_s4_subset(topo, radius) for topo in topologies]
    checks = [run_consistency_checks(result) for result in results]

    flat_consistent = all(
        any(check["status"] == "consistent" and check["check"] == "flat_limit" for check in group)
        for group in checks
    )

    spectral_runs = sum(1 for result in results if result.get("method") == "spectral_truncation")
    curvature_runs = sum(1 for result in results if result.get("method") == "curvature_expansion")

    return {
        "stage": "4C",
        "status": "curved_subset_evaluation",
        "topologies_evaluated": len(topologies),
        "spectral_runs": spectral_runs,
        "curvature_expansions": curvature_runs,
        "flat_limit_consistency": flat_consistent,
        "convergence_established": False,
        "can_attempt_tensor_subsets": flat_consistent,
        "can_compute_full_3loop": False,
        "promotes_claims": False,
    }
