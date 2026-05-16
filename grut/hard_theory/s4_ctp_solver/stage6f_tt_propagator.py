"""Stage 6F TT graviton propagator scaffold."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.s4_tt_operator import define_tt_operator
from grut.hard_theory.s4_ctp_solver.s4_tt_projector_extended import extend_tt_projector
from grut.hard_theory.s4_ctp_solver.s4_tt_propagator_scaffold import (
    build_tt_propagator_scaffold,
)
from grut.hard_theory.s4_ctp_solver.tt_propagator_validation import (
    validate_tt_scaffold,
)
from grut.hard_theory.s4_ctp_solver.tt_propagator_blocker_update import (
    update_tt_blocker_status,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage6f_tt_propagator() -> Dict[str, object]:
    operator = define_tt_operator()
    projector = extend_tt_projector()
    scaffold = build_tt_propagator_scaffold(operator, projector)
    validation = validate_tt_scaffold(scaffold, operator, projector)
    blocker_update = update_tt_blocker_status()
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())

    return {
        "stage": "6F",
        "status": "tt_propagator_scaffold",
        "tt_operator_defined": True,
        "projector_extended": True,
        "scaffold_built": True,
        "validated": validation["status"] == "structural_validated",
        "tt_propagator_inverted": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "operator": operator,
        "projector": projector,
        "scaffold": scaffold,
        "validation": validation,
        "blocker_update": blocker_update,
        "guard": guard,
    }
