"""Stage 7H finite-part blocker repair plan."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage7g_finite_part_audit import (
    run_stage7g_finite_part_audit,
)
from grut.hard_theory.s4_ctp_solver.finite_part_repair_registry import (
    build_finite_part_repair_registry,
)
from grut.hard_theory.s4_ctp_solver.finite_part_repair_prioritizer import (
    prioritize_repairs,
)
from grut.hard_theory.s4_ctp_solver.finite_part_repair_plan import (
    generate_repair_plan,
)
from grut.hard_theory.s4_ctp_solver.finite_part_repair_audit import (
    audit_repair_plan,
)
from grut.hard_theory.s4_ctp_solver.stage5c_tensor_native import (
    evaluate_tensor_native_attempt,
)
from grut.hard_theory.s4_ctp_solver.tensor_placeholder_guard import (
    enforce_tensor_placeholder_guard,
)


def run_stage7h_finite_part_repair_plan() -> Dict[str, object]:
    stage7g = run_stage7g_finite_part_audit()
    blockers = stage7g.get("blockers", [])

    registry = build_finite_part_repair_registry(blockers)
    prioritization = prioritize_repairs(registry["repairs"])
    plan = generate_repair_plan(prioritization["priority_queue"], registry["repairs"])
    audit = audit_repair_plan(plan)
    guard = enforce_tensor_placeholder_guard(evaluate_tensor_native_attempt())

    return {
        "stage": "7H",
        "status": "finite_part_blocker_repair_plan",
        "blockers_covered": not audit.get("missing_blockers"),
        "top_priority": prioritization.get("top_priority"),
        "repairs_started": False,
        "can_compute_finite_parts": False,
        "can_extract": False,
        "can_compute_r": False,
        "promotes_claims": False,
        "stage7g": stage7g,
        "registry": registry,
        "prioritization": prioritization,
        "plan": plan,
        "audit": audit,
        "guard": guard,
    }
