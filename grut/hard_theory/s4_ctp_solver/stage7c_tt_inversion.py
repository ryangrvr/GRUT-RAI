"""Stage 7C TT truncated spectral inversion attempt on S4."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.s4_tt_operator import define_tt_operator
from grut.hard_theory.s4_ctp_solver.s4_tt_projector_extended import extend_tt_projector
from grut.hard_theory.s4_ctp_solver.s4_tt_inversion_strategy import (
    define_spectral_inversion_strategy,
)
from grut.hard_theory.s4_ctp_solver.tt_inversion_engine import run_tt_inversion_engine
from grut.hard_theory.s4_ctp_solver.tt_inversion_comparison import (
    compare_tt_truncated_structure,
)
from grut.hard_theory.s4_ctp_solver.tt_inversion_audit import audit_tt_inversion
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage7c_tt_inversion() -> Dict[str, object]:
    l_values: List[int] = [3, 5, 10]
    operator = define_tt_operator()
    projector = extend_tt_projector()
    strategy = define_spectral_inversion_strategy()

    inversion = run_tt_inversion_engine(l_values)
    comparison = compare_tt_truncated_structure(inversion["results"])
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_tt_inversion({**inversion, "comparison": comparison, "guard": guard})

    return {
        "stage": "7C",
        "status": "tt_truncated_inversion_attempt",
        "inversion_performed": True,
        "convergence_observed": False,
        "tensor_structure_preserved": comparison["structure_valid"],
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "operator": operator,
        "projector": projector,
        "strategy": strategy,
        "inversion": inversion,
        "comparison": comparison,
        "audit": audit,
        "guard": guard,
    }
