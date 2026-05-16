"""Stage 8D diagram skeleton structural contraction."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage8c_controlled_fragment_contractions import (
    run_stage8c_controlled_fragment_contractions,
)
from grut.hard_theory.s4_ctp_solver.tt_diagram_skeleton import (
    define_tt_diagram_skeleton,
)
from grut.hard_theory.s4_ctp_solver.tt_skeleton_contraction_engine import (
    run_skeleton_structural_contraction,
)
from grut.hard_theory.s4_ctp_solver.tt_skeleton_constraint_checks import (
    check_skeleton_constraints,
)
from grut.hard_theory.s4_ctp_solver.tt_skeleton_audit import (
    audit_skeleton_contraction,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage8d_diagram_skeleton() -> Dict[str, object]:
    stage8c = run_stage8c_controlled_fragment_contractions()
    skeleton = define_tt_diagram_skeleton()
    result = run_skeleton_structural_contraction(skeleton)
    constraint_check = check_skeleton_constraints(result)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_skeleton_contraction({**result, "guard": guard}, constraint_check)

    index_flow_trace = {
        "trace_id": "tt_skeleton_index_flow_v1",
        "status": "index_flow_trace_structural",
        "node_index_flow": [
            {"node_id": "vertex_A", "enter": ["mu"], "exit": ["nu"]},
            {"node_id": "vertex_B", "enter": ["rho"], "exit": ["sigma"]},
            {"node_id": "vertex_C", "enter": ["alpha"], "exit": ["beta"]},
        ],
        "edge_pairings": [
            {"edge_id": "edge_AB", "paired_indices": ["mu", "rho"]},
            {"edge_id": "edge_BC", "paired_indices": ["sigma", "alpha"]},
            {"edge_id": "edge_CA", "paired_indices": ["beta", "nu"]},
        ],
        "projector_positions": [
            {"node_id": "vertex_A", "position": "local"},
            {"node_id": "vertex_B", "position": "local"},
            {"node_id": "vertex_C", "position": "local"},
        ],
        "unresolved_indices": [],
        "propagators_evaluated": False,
        "loops_evaluated": False,
        "promotes_claims": False,
    }

    skeleton_valid = constraint_check.get("status") == "valid"

    return {
        "stage": "8D",
        "status": "diagram_skeleton_structural_contraction",
        "skeleton_valid": skeleton_valid,
        "structure_only": True,
        "propagators_evaluated": False,
        "loops_evaluated": False,
        "can_advance_to_propagator_symbolics": audit.get(
            "can_advance_to_propagator_symbolics"
        ),
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "stage8c": stage8c,
        "skeleton": skeleton,
        "result": result,
        "index_flow_trace": index_flow_trace,
        "constraint_check": constraint_check,
        "audit": audit,
        "guard": guard,
    }
