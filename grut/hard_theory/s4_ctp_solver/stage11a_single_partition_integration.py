"""Stage 11A single partition integration attempt."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage10f_partition_consistency_audit import (
    run_stage10f_partition_consistency_audit,
)
from grut.hard_theory.s4_ctp_solver.single_partition_selector import (
    select_single_approved_partition,
)
from grut.hard_theory.s4_ctp_solver.single_partition_integration_engine import (
    run_single_partition_integration,
)
from grut.hard_theory.s4_ctp_solver.single_partition_behavior_check import (
    check_single_partition_behavior,
)
from grut.hard_theory.s4_ctp_solver.single_partition_audit import (
    audit_single_partition_integration,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage11a_single_partition_integration() -> Dict[str, object]:
    stage10f = run_stage10f_partition_consistency_audit()
    selection = select_single_approved_partition(stage10f)
    result = run_single_partition_integration(selection)
    behavior = check_single_partition_behavior(result)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_single_partition_integration(selection, result, behavior, guard)

    return {
        "stage": "11A",
        "status": "single_partition_integration_attempt",
        "partition_selected": True,
        "selected_count": selection.get("selected_count"),
        "integration_attempted": result.get("integration_attempted"),
        "finite_part_computed": False,
        "amplitude_computed": False,
        "regulator_active": result.get("regulator_active"),
        "can_advance_to_subtraction_dry_run": audit.get(
            "can_advance_to_subtraction_dry_run"
        ),
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "stage10f": stage10f,
        "selection": selection,
        "result": result,
        "behavior": behavior,
        "audit": audit,
        "guard": guard,
    }
