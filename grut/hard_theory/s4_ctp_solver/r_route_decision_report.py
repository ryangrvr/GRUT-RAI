"""Assemble the OR1 decision report for the R route."""

from typing import Dict, Optional


def _selected_route(
    candidate_routes: list[Dict[str, object]],
    selected_route_id: Optional[str],
) -> Optional[Dict[str, object]]:
    if not selected_route_id:
        return None
    for route in candidate_routes:
        if route.get("ratio_id") == selected_route_id:
            return route
    return None


def build_r_route_decision_report(
    definition_history: Dict[str, object],
    selection_audit: Dict[str, object],
    degeneracy_resolution: Dict[str, object],
) -> Dict[str, object]:
    candidate_routes = selection_audit.get("candidate_routes", [])
    selected_route_id = degeneracy_resolution.get("selected_route_id")
    selected_route = _selected_route(candidate_routes, selected_route_id)

    return {
        "stage": "OR1",
        "status": degeneracy_resolution.get("classification"),
        "r_definition_found": definition_history.get("r_definition_found"),
        "r_definition_source": definition_history.get("r_definition_source"),
        "candidate_routes": candidate_routes,
        "selected_route": selected_route,
        "unique_r_route_selected": degeneracy_resolution.get("unique_r_route_selected"),
        "can_advance_to_symbol_binding": degeneracy_resolution.get(
            "can_advance_to_symbol_binding"
        ),
        "can_compute_numeric_r": False,
        "can_claim_r": False,
        "blocking_reason": degeneracy_resolution.get("blocking_reason"),
        "next_required_action": degeneracy_resolution.get("next_required_action"),
        "promotes_claims": False,
    }
