"""Stage 7B ghost/vector spectral inversion benchmark on S4."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.ghost_vector_inversion_engine import (
    run_ghost_vector_inversion_engine,
)
from grut.hard_theory.s4_ctp_solver.ghost_vector_inversion_comparison import (
    compare_ghost_vector_structure,
)
from grut.hard_theory.s4_ctp_solver.ghost_vector_inversion_audit import (
    audit_ghost_vector_inversion,
)
from grut.hard_theory.s4_ctp_solver.s4_ghost_operator import define_ghost_operator
from grut.hard_theory.s4_ctp_solver.s4_vector_harmonics import (
    build_vector_harmonics_structure,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage7b_ghost_vector_inversion() -> Dict[str, object]:
    l_values: List[int] = [5, 10, 20, 50]
    ghost_operator = define_ghost_operator()
    vector_harmonics = build_vector_harmonics_structure()

    inversion = run_ghost_vector_inversion_engine(l_values)
    comparison = compare_ghost_vector_structure(inversion["results"])
    audit_input = {**inversion, "comparison": comparison}
    audit = audit_ghost_vector_inversion(audit_input)

    can_apply_to_tt = (
        comparison["status"] == "structurally_consistent"
        and not comparison["scalar_collapse_detected"]
        and audit["status"] == "valid_benchmark"
    )

    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())

    return {
        "stage": "7B",
        "status": "ghost_vector_inversion_benchmark",
        "inversion_performed": True,
        "tt_inversion_performed": False,
        "scalar_collapse_detected": comparison["scalar_collapse_detected"],
        "convergence_observed": comparison["convergence_observed"],
        "convergence_proven": False,
        "can_apply_to_tt": can_apply_to_tt,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "ghost_operator": ghost_operator,
        "vector_harmonics": vector_harmonics,
        "inversion": inversion,
        "comparison": comparison,
        "audit": audit,
        "guard": guard,
    }
