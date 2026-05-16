"""Stage 11E cross-partition finite-part consistency."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage10f_partition_consistency_audit import (
    run_stage10f_partition_consistency_audit,
)
from grut.hard_theory.s4_ctp_solver.stage11c_finite_part_benchmark_gate import (
    run_stage11c_finite_part_benchmark_gate,
)
from grut.hard_theory.s4_ctp_solver.stage11d_native_finite_part_attempt import (
    run_stage11d_native_finite_part_attempt,
)
from grut.hard_theory.s4_ctp_solver.cross_partition_finite_selector import (
    select_cross_partition_finite_partitions,
)
from grut.hard_theory.s4_ctp_solver.cross_partition_finite_engine import (
    run_cross_partition_finite_attempts,
)
from grut.hard_theory.s4_ctp_solver.cross_partition_finite_consistency import (
    check_cross_partition_finite_consistency,
)
from grut.hard_theory.s4_ctp_solver.cross_partition_finite_audit import (
    audit_cross_partition_finite_consistency,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage11e_cross_partition_finite_consistency() -> Dict[str, object]:
    stage10f = run_stage10f_partition_consistency_audit()
    stage11c = run_stage11c_finite_part_benchmark_gate()
    stage11d = run_stage11d_native_finite_part_attempt()

    selection = select_cross_partition_finite_partitions(stage10f, stage11c, stage11d)
    attempts = run_cross_partition_finite_attempts(selection.get("selected_partitions", []))
    consistency = check_cross_partition_finite_consistency(attempts.get("results", []))
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_cross_partition_finite_consistency(
        attempts.get("results", []), consistency, guard
    )

    return {
        "stage": "11E",
        "status": "cross_partition_finite_part_consistency",
        "partitions_attempted": attempts.get("attempted_count"),
        "consistent": consistency.get("consistent"),
        "amplitude_computed": False,
        "can_compute_c_final": False,
        "can_compute_c_cosmo": False,
        "can_compute_r": False,
        "can_extract": False,
        "promotes_claims": False,
        "stage10f": stage10f,
        "stage11c": stage11c,
        "stage11d": stage11d,
        "selection": selection,
        "attempts": attempts,
        "consistency": consistency,
        "audit": audit,
        "guard": guard,
    }
