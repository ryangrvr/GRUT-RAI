"""Stage 5C tensor-native attempt gate."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.native_attempt_tensor_deep import (
    select_tensor_native_topology,
)
from grut.hard_theory.s4_ctp_solver.tensor_flow_tracking import track_tensor_index_flow
from grut.hard_theory.s4_ctp_solver.tensor_constraint_engine import apply_tensor_constraints
from grut.hard_theory.s4_ctp_solver.tensor_native_checks import (
    check_tensor_flow_consistency,
    check_tensor_scalar_alignment,
    check_tensor_ward_consistency,
    check_tensor_scheme_integrity,
)
from grut.hard_theory.s4_ctp_solver.native_attempt_pipeline import run_native_attempt_pipeline
from grut.hard_theory.s4_ctp_solver.native_attempt_evaluation import evaluate_native_attempt
from grut.hard_theory.s4_ctp_solver.tensor_native_report import render_tensor_native_report
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)
from grut.hard_theory.s4_ctp_solver.ctp_imaginary_scaffold import (
    emit_imaginary_causal_scaffold,
)


def evaluate_tensor_native_attempt() -> Dict[str, object]:
    topology = select_tensor_native_topology()
    _ = run_native_attempt_pipeline(topology, {})
    base = evaluate_native_attempt(topology)

    flow = track_tensor_index_flow(topology)
    constraints = apply_tensor_constraints(flow)

    return {
        "topology_id": topology.topology_id,
        "tensor_flow": flow,
        "constraint_status": constraints,
        "combined_structure": "tensor_native_structure_placeholder",
        "ctp_imaginary_scaffold": emit_imaginary_causal_scaffold(),
        "divergence_structure": base["divergence_structure"],
        "finite_part": "not_computed",
        "status": "native_attempt_internal_tensor",
        "limitations": [
            "no explicit tensor propagator",
            "no contraction closure",
            "no convergence proof",
        ],
        "scheme_metadata": {"scheme": "ms_bar", "regulator": "dim_reg"},
        "promotes_claims": False,
    }


def run_stage5c_tensor_native() -> Dict[str, object]:
    result = evaluate_tensor_native_attempt()

    flow_check = check_tensor_flow_consistency(result)
    scalar_check = check_tensor_scalar_alignment(result)
    ward_check = check_tensor_ward_consistency(result)
    scheme_check = check_tensor_scheme_integrity(result)

    guard = enforce_tensor_placeholder_guard(result)

    consistent = all(
        check["status"] in {"consistent", "inconclusive"}
        for check in (flow_check, scalar_check, ward_check, scheme_check)
    )

    return {
        "stage": "5C",
        "status": "tensor_native_attempt",
        "topology_attempted": 1,
        "tensor_flow_tracked": True,
        "constraints_applied": True,
        "ward_consistent": ward_check["status"] != "inconsistent",
        "scheme_integrity": scheme_check["status"] != "inconsistent",
        "any_tensor_evaluated": False,
        "can_attempt_candidate_extraction": consistent and guard["status"] == "pass",
        "can_compute_full_3loop": False,
        "promotes_claims": False,
        "guard": guard,
        "report": render_tensor_native_report(
            {
                **result,
                "can_attempt_candidate_extraction": consistent and guard["status"] == "pass",
            }
        ),
    }
