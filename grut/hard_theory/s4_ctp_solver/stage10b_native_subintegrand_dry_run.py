"""Stage 10B native sub-integrand dry run."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage9c_regularized_integrand import (
    run_stage9c_regularized_integrand,
)
from grut.hard_theory.s4_ctp_solver.native_subintegrand_selector import (
    select_native_subintegrand,
)
from grut.hard_theory.s4_ctp_solver.native_subintegrand_engine import (
    run_native_subintegrand_integration,
)
from grut.hard_theory.s4_ctp_solver.native_subintegrand_comparison import (
    check_subintegrand_behavior,
)
from grut.hard_theory.s4_ctp_solver.native_subintegrand_audit import (
    audit_native_subintegrand_run,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage10b_native_subintegrand_dry_run() -> Dict[str, object]:
    stage9c = run_stage9c_regularized_integrand()
    integrand = stage9c.get("stage9b", {}).get("integrand", {})
    subintegrand = select_native_subintegrand(integrand)
    result = run_native_subintegrand_integration(subintegrand)
    checks = check_subintegrand_behavior(result)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())
    audit = audit_native_subintegrand_run(result, checks, guard)

    return {
        "stage": "10B",
        "status": "native_subintegrand_dry_run",
        "integration_attempted": True,
        "finite_part_computed": False,
        "native_integrand_used": True,
        "full_integrand_used": False,
        "can_advance_to_multi_subintegrand": audit.get("can_advance_to_multi_subintegrand"),
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "stage9c": stage9c,
        "subintegrand": subintegrand,
        "result": result,
        "checks": checks,
        "audit": audit,
        "guard": guard,
    }
