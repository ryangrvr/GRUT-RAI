"""Stage 10E eligible partition dry-runs."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage10d_integrand_partition_map import (
    run_stage10d_integrand_partition_map,
)
from grut.hard_theory.s4_ctp_solver.eligible_partition_selector import (
    select_eligible_partitions,
)
from grut.hard_theory.s4_ctp_solver.eligible_partition_engine import (
    run_eligible_partition_dry_runs,
)
from grut.hard_theory.s4_ctp_solver.eligible_partition_consistency import (
    check_eligible_partition_consistency,
)
from grut.hard_theory.s4_ctp_solver.eligible_partition_audit import (
    audit_eligible_partition_dry_runs,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage10e_eligible_partition_dry_runs() -> Dict[str, object]:
    stage10d = run_stage10d_integrand_partition_map()
    selection = select_eligible_partitions(stage10d)

    scheme = stage10d.get("stage9c", {}).get("scheme", {})
    for partition in selection.get("selected_partitions", []):
        partition["scheme_id"] = scheme.get("scheme_id")
        partition["default_regulator"] = scheme.get("default_regulator")

    attempts = run_eligible_partition_dry_runs(selection.get("selected_partitions", []))
    consistency = check_eligible_partition_consistency(attempts)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_eligible_partition_dry_runs(selection, attempts, consistency, guard)

    return {
        "stage": "10E",
        "status": "eligible_partition_dry_runs",
        "eligible_attempted": attempts.get("attempted_count"),
        "blocked_skipped": selection.get("blocked_skipped"),
        "forbidden_skipped": selection.get("forbidden_skipped"),
        "finite_parts_computed": False,
        "amplitude_computed": False,
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "stage10d": stage10d,
        "selection": selection,
        "attempts": attempts,
        "consistency": consistency,
        "audit": audit,
        "guard": guard,
    }
