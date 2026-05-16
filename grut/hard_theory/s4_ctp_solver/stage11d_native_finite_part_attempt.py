"""Stage 11D native finite-part attempt."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage11a_single_partition_integration import (
    run_stage11a_single_partition_integration,
)
from grut.hard_theory.s4_ctp_solver.stage11b_subtraction_dry_run import (
    run_stage11b_subtraction_dry_run,
)
from grut.hard_theory.s4_ctp_solver.stage11c_finite_part_benchmark_gate import (
    run_stage11c_finite_part_benchmark_gate,
)
from grut.hard_theory.s4_ctp_solver.native_finite_part_selector import (
    select_native_partition_for_finite_part,
)
from grut.hard_theory.s4_ctp_solver.native_finite_part_extractor import (
    attempt_native_partition_finite_part,
)
from grut.hard_theory.s4_ctp_solver.native_finite_part_validation import (
    validate_native_finite_part_attempt,
)
from grut.hard_theory.s4_ctp_solver.native_finite_part_audit import (
    audit_native_finite_part_attempt,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage11d_native_finite_part_attempt() -> Dict[str, object]:
    stage11a = run_stage11a_single_partition_integration()
    stage11b = run_stage11b_subtraction_dry_run()
    stage11c = run_stage11c_finite_part_benchmark_gate()

    selection = select_native_partition_for_finite_part(stage11a, stage11b, stage11c)
    result = attempt_native_partition_finite_part(selection)
    validation = validate_native_finite_part_attempt(result)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_native_finite_part_attempt(result, validation, guard)

    return {
        "stage": "11D",
        "status": "native_partition_finite_part_attempt",
        "partition_count": 1,
        "finite_part_attempted": result.get("finite_part_attempted"),
        "coefficient_scope": result.get("coefficient_scope"),
        "amplitude_computed": result.get("amplitude_computed"),
        "can_compute_c_final": False,
        "can_compute_c_cosmo": False,
        "can_compute_r": False,
        "can_extract": False,
        "promotes_claims": False,
        "stage11a": stage11a,
        "stage11b": stage11b,
        "stage11c": stage11c,
        "selection": selection,
        "result": result,
        "validation": validation,
        "audit": audit,
        "guard": guard,
    }
