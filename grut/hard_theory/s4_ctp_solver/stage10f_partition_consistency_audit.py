"""Stage 10F partition consistency audit."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.partition_consistency_collector import (
    collect_partition_attempts,
)
from grut.hard_theory.s4_ctp_solver.partition_scheme_consistency import (
    check_partition_scheme_consistency,
)
from grut.hard_theory.s4_ctp_solver.partition_regulator_consistency import (
    check_partition_regulator_consistency,
)
from grut.hard_theory.s4_ctp_solver.partition_consistency_audit import (
    audit_partition_consistency,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage10f_partition_consistency_audit() -> Dict[str, object]:
    collected = collect_partition_attempts()
    attempts = collected.get("collected_attempts", [])
    scheme_check = check_partition_scheme_consistency(attempts)
    regulator_check = check_partition_regulator_consistency(attempts)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_partition_consistency(collected, scheme_check, regulator_check, guard)

    return {
        "stage": "10F",
        "status": "partition_consistency_audit",
        "attempts_collected": len(attempts),
        "scheme_consistent": scheme_check.get("scheme_consistent"),
        "regulator_consistent": regulator_check.get("regulator_consistent"),
        "new_integrations_performed": False,
        "can_advance_to_single_partition_integration": audit.get(
            "can_advance_to_single_partition_integration"
        ),
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "collected": collected,
        "scheme_check": scheme_check,
        "regulator_check": regulator_check,
        "audit": audit,
        "guard": guard,
    }
