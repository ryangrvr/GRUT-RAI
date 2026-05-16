"""Stage OR2 physical interpretation constraint for R-route selection."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.stage_or1_resolve_r_route import (
    run_stage_or1_resolve_r_route,
)
from grut.hard_theory.s4_ctp_solver.stage_or1_r1_legacy_definition_mapping import (
    run_stage_or1_r1_legacy_definition_mapping,
)
from grut.hard_theory.s4_ctp_solver.r_physical_intent_sources import (
    load_physical_intent_sources,
)
from grut.hard_theory.s4_ctp_solver.r_physical_role_extractor import (
    extract_physical_intent,
)
from grut.hard_theory.s4_ctp_solver.r_route_physical_mapping import (
    map_routes_to_physical_intent,
)
from grut.hard_theory.s4_ctp_solver.r_physical_constraint_audit import (
    audit_physical_constraint,
)


def _candidate_routes(or1_report: Dict[str, object]) -> List[Dict[str, object]]:
    routes = or1_report.get("candidate_routes", [])
    return list(routes)


def _select_unique_route(
    route_evaluations: List[Dict[str, object]],
    routes: List[Dict[str, object]],
) -> Dict[str, object]:
    matches = [
        evaluation
        for evaluation in route_evaluations
        if evaluation.get("physical_match") is True and evaluation.get("role_match") is True
    ]

    if len(matches) == 1:
        match_id = matches[0].get("route_id")
        selected = None
        for route in routes:
            if route.get("ratio_id") == match_id:
                selected = route
                break
        return {
            "unique_route_selected": True,
            "selected_route": selected,
            "blocking_reason": None,
            "next_required_action": "advance_to_symbol_binding",
        }

    if len(matches) > 1:
        return {
            "unique_route_selected": False,
            "selected_route": None,
            "blocking_reason": "multiple_matching_routes",
            "next_required_action": "resolve_source_conflict",
        }

    return {
        "unique_route_selected": False,
        "selected_route": None,
        "blocking_reason": "no_route_selected",
        "next_required_action": "write_explicit_r_definition",
    }


def run_stage_or2_physical_interpretation_constraint() -> Dict[str, object]:
    or1_report = run_stage_or1_resolve_r_route()
    or1_r1_report = run_stage_or1_r1_legacy_definition_mapping()

    statements = load_physical_intent_sources()
    intent = extract_physical_intent(statements)

    routes = _candidate_routes(or1_report)
    route_evaluations = map_routes_to_physical_intent(intent, routes, or1_r1_report)

    selection = _select_unique_route(route_evaluations, routes)
    audit = audit_physical_constraint(route_evaluations, intent)

    return {
        "stage": "OR2",
        "status": "physical_interpretation_constraint",
        "intent_classification": intent.get("intent_classification"),
        "selected_route": selection.get("selected_route"),
        "unique_route_selected": selection.get("unique_route_selected"),
        "blocking_reason": selection.get("blocking_reason"),
        "next_required_action": selection.get("next_required_action"),
        "can_compute_numeric_r": False,
        "can_claim_r": False,
        "promotes_claims": False,
        "intent_statements": statements,
        "route_evaluations": route_evaluations,
        "audit": audit,
        "stage_or1": or1_report,
        "stage_or1_r1": or1_r1_report,
    }
