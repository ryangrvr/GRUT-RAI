"""Prioritization logic for finite-part repair items."""

from typing import Dict, List

_PRIORITY_ORDER = [
    "insufficient_convergence_control",
    "tensor_contractions_not_resolved",
    "scheme_incomplete",
    "unmapped_divergence",
    "instability_detected",
    "structure_breakdown",
    "independent_replication_missing",
]


def prioritize_repairs(repair_items: List[Dict[str, object]]) -> Dict[str, object]:
    order_map = {blocker: idx for idx, blocker in enumerate(_PRIORITY_ORDER)}
    sorted_items = sorted(
        repair_items,
        key=lambda item: order_map.get(item.get("blocker"), len(_PRIORITY_ORDER)),
    )

    priority_queue = [item["repair_id"] for item in sorted_items]
    top_priority = sorted_items[0]["repair_id"] if sorted_items else ""
    reason = (
        "Prioritized by convergence control, tensor readiness, and scheme coverage."
        if top_priority
        else "No repair items provided."
    )

    return {
        "priority_queue": priority_queue,
        "top_priority": top_priority,
        "reason": reason,
        "promotes_claims": False,
    }
