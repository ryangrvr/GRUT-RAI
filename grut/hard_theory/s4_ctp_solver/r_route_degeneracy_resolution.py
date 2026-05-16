"""Resolve degeneracy across candidate R routes."""

from typing import Dict, Optional


def _blocked_result(classification: str, blocking_reason: str, next_action: str) -> Dict[str, object]:
    return {
        "classification": classification,
        "unique_r_route_selected": False,
        "selected_route_id": None,
        "blocking_reason": blocking_reason,
        "next_required_action": next_action,
        "can_advance_to_symbol_binding": False,
        "promotes_claims": False,
    }


def resolve_r_route_degeneracy(
    selection_audit: Dict[str, object],
    definition_history: Dict[str, object],
    equivalence_report: Optional[Dict[str, object]] = None,
) -> Dict[str, object]:
    candidate_routes = selection_audit.get("candidate_routes", [])
    selected_route_ids = selection_audit.get("selected_route_ids", [])

    if not candidate_routes:
        return _blocked_result(
            "no_valid_r_route",
            "no_candidate_routes",
            "repair_protected_kernel_pipeline",
        )

    if definition_history.get("r_definition_found") is not True:
        return _blocked_result(
            "r_definition_missing",
            "missing_prior_definition",
            "locate_or_define_r_definition",
        )

    if definition_history.get("definition_status") == "ambiguous":
        return _blocked_result(
            "r_definition_missing",
            "r_definition_ambiguous",
            "resolve_r_definition_scope",
        )

    if len(selected_route_ids) == 1:
        return {
            "classification": "unique_r_route_selected",
            "unique_r_route_selected": True,
            "selected_route_id": selected_route_ids[0],
            "blocking_reason": None,
            "next_required_action": "advance_to_symbol_binding",
            "can_advance_to_symbol_binding": True,
            "promotes_claims": False,
        }

    if selection_audit.get("definition_mapping_found") is not True:
        return _blocked_result(
            "r_requires_new_physics_derivation",
            "missing_ctp_to_curvature_projection",
            "define_ctp_to_curvature_projection",
        )

    if equivalence_report and equivalence_report.get("unique_equivalence_class_exists") is False:
        return _blocked_result(
            "multiple_valid_routes_no_selection_principle",
            "multiple_inequivalent_protected_sectors",
            "define_r_selection_principle",
        )

    return _blocked_result(
        "multiple_valid_routes_no_selection_principle",
        "multiple_valid_routes_no_selection_principle",
        "define_r_selection_principle",
    )
