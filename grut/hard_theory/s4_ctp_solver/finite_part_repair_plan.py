"""Repair plan generation for finite-part blockers."""

from typing import Dict, List


def generate_repair_plan(
    priority_queue: List[str],
    repair_items: List[Dict[str, object]],
) -> Dict[str, object]:
    repair_map = {item["repair_id"]: item for item in repair_items}
    steps: List[Dict[str, object]] = []

    for idx, repair_id in enumerate(priority_queue, start=1):
        item = repair_map[repair_id]
        steps.append(
            {
                "step": idx,
                "repair_id": repair_id,
                "action": item["required_action"],
                "completion_test": item["completion_test"],
                "dependencies": list(item["dependencies"]),
                "allowed_next_stage": "stage7g_finite_part_audit",
            }
        )

    return {
        "plan_id": "finite_part_repair_plan_v1",
        "steps": steps,
        "blockers": [item["blocker"] for item in repair_items],
        "can_compute_finite_parts_after_plan": False,
        "promotes_claims": False,
    }
