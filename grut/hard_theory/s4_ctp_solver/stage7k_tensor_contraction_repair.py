"""Stage 7K tensor contraction structure repair."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage7j_tensor_contraction_readiness import (
    run_stage7j_tensor_contraction_readiness,
)
from grut.hard_theory.s4_ctp_solver.tt_index_repair import (
    repair_tt_index_structure,
)
from grut.hard_theory.s4_ctp_solver.tt_projector_repair import (
    repair_tt_projector_placement,
)
from grut.hard_theory.s4_ctp_solver.tt_contraction_ordering import (
    define_contraction_ordering_protocol,
)
from grut.hard_theory.s4_ctp_solver.tt_contraction_repair_audit import (
    audit_tensor_contraction_repair,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage7k_tensor_contraction_repair() -> Dict[str, object]:
    readiness = run_stage7j_tensor_contraction_readiness()
    index_repair = repair_tt_index_structure(readiness)
    projector_repair = repair_tt_projector_placement(readiness)
    ordering_protocol = define_contraction_ordering_protocol()
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_tensor_contraction_repair(
        index_repair, projector_repair, ordering_protocol, guard
    )

    return {
        "stage": "7K",
        "status": "tensor_contraction_repair",
        "repair_status": index_repair.get("status"),
        "future_sandbox_allowed": audit.get("future_sandbox_allowed"),
        "blocker_closed": False,
        "contractions_performed": False,
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "readiness": readiness,
        "index_repair": index_repair,
        "projector_repair": projector_repair,
        "ordering_protocol": ordering_protocol,
        "audit": audit,
        "guard": guard,
    }
