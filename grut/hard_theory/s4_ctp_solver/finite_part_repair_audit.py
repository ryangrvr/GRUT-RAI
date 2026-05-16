"""Audit for finite-part repair plan."""

from typing import Dict, List


def audit_repair_plan(plan: Dict[str, object]) -> Dict[str, object]:
    steps = plan.get("steps", [])
    covered_blockers = [
        step.get("repair_id", "").replace("repair_", "") for step in steps
    ]
    plan_blockers = plan.get("blockers", [])
    missing_blockers = [
        blocker for blocker in plan_blockers if blocker not in covered_blockers
    ]

    dependencies_present = all(
        isinstance(step.get("dependencies"), list) for step in steps
    )
    no_repairs_complete = True
    for step in steps:
        if step.get("status") == "complete":
            no_repairs_complete = False
            break

    status = (
        "valid_plan"
        if not missing_blockers
        and dependencies_present
        and no_repairs_complete
        and plan.get("can_compute_finite_parts_after_plan") is False
        else "invalid_plan"
    )

    return {
        "audit": "finite_part_repair_plan",
        "status": status,
        "covered_blockers": covered_blockers,
        "missing_blockers": missing_blockers,
        "can_compute_finite_parts": False,
        "promotes_claims": False,
    }
