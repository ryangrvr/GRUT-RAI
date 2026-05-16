"""Selection rule for S4 Euler-anomaly projection routes."""

from typing import Dict, List


def _projection_map(kernel_projections: List[Dict[str, object]]) -> Dict[str, Dict[str, object]]:
    mapping: Dict[str, Dict[str, object]] = {}
    for entry in kernel_projections:
        source_type = entry.get("source_type")
        if source_type:
            mapping[source_type] = entry
    return mapping


def _route_id(ratio: Dict[str, object]) -> str:
    return ratio.get("ratio_id") or "unknown_ratio"


def select_euler_projection_route(
    ratios: List[Dict[str, object]],
    kernel_projections: List[Dict[str, object]],
    ctp_to_euler_bridge: bool = False,
    off_shell_continuation: bool = False,
) -> Dict[str, object]:
    projections = _projection_map(kernel_projections)
    evaluated_routes: List[Dict[str, object]] = []
    selected: List[Dict[str, object]] = []

    for ratio in ratios:
        pair = ratio.get("pair", {})
        left = pair.get("left", {})
        right = pair.get("right", {})
        numerator = left.get("source_type")
        denominator = right.get("source_type")

        numerator_proj = projections.get(numerator, {})
        denominator_proj = projections.get(denominator, {})

        numerator_euler = numerator_proj.get("projects_to_euler_channel") is True
        denominator_euler = denominator_proj.get("projects_to_euler_channel") is True
        numerator_weyl = numerator_proj.get("projects_to_weyl_channel") is True
        denominator_weyl = denominator_proj.get("projects_to_weyl_channel") is True

        numerator_survives = numerator_proj.get("survives_on_s4") is True
        denominator_survives = denominator_proj.get("survives_on_s4") is True

        blocking_reason = None
        selected_by_rule = False

        if (numerator_weyl or denominator_weyl) and not off_shell_continuation:
            if not numerator_survives or not denominator_survives:
                blocking_reason = "weyl_zero_on_s4"
        elif numerator_euler and denominator_euler:
            selected_by_rule = True
        elif ctp_to_euler_bridge:
            if numerator_euler or denominator_euler:
                selected_by_rule = True
            else:
                blocking_reason = "ctp_to_euler_bridge_missing"
        else:
            blocking_reason = "euler_alignment_missing"

        evaluated = {
            "route_id": _route_id(ratio),
            "numerator_source_type": numerator,
            "denominator_source_type": denominator,
            "selected_by_rule": selected_by_rule,
            "blocking_reason": blocking_reason,
            "promotes_claims": False,
        }
        evaluated_routes.append(evaluated)

        if selected_by_rule:
            selected.append(ratio)

    if len(selected) == 1:
        return {
            "selected_route": selected[0],
            "unique_route_selected": True,
            "blocking_reason": None,
            "evaluated_routes": evaluated_routes,
            "promotes_claims": False,
        }

    if len(selected) > 1:
        return {
            "selected_route": None,
            "unique_route_selected": False,
            "blocking_reason": "multiple_euler_routes",
            "evaluated_routes": evaluated_routes,
            "promotes_claims": False,
        }

    return {
        "selected_route": None,
        "unique_route_selected": False,
        "blocking_reason": "no_euler_route_selected",
        "evaluated_routes": evaluated_routes,
        "promotes_claims": False,
    }
