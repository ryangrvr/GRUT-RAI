"""Map physical intent onto protected quotient routes."""

from typing import Dict, List, Tuple


def _route_key(route: Dict[str, object]) -> Tuple[str, str]:
    return (
        route.get("numerator_source_type") or "",
        route.get("denominator_source_type") or "",
    )


def _mapped_pairs(legacy_mapping: Dict[str, object]) -> List[Tuple[str, str]]:
    pairs: List[Tuple[str, str]] = []
    for route in legacy_mapping.get("mapped_routes", []):
        if route.get("mapping_status") != "complete":
            continue
        for numerator in route.get("mapped_numerator_candidates", []):
            for denominator in route.get("mapped_denominator_candidates", []):
                num_source = numerator.get("source_type")
                den_source = denominator.get("source_type")
                if num_source and den_source:
                    pairs.append((num_source, den_source))
    return pairs


def _is_im_log_route(route: Dict[str, object]) -> bool:
    return "Im_log_minus_box_i_epsilon" in {
        route.get("numerator_source_type"),
        route.get("denominator_source_type"),
    }


def _is_curvature_route(route: Dict[str, object]) -> bool:
    sources = {
        route.get("numerator_source_type"),
        route.get("denominator_source_type"),
    }
    return sources.issubset({"R_log_box_R", "Weyl_log_box_Weyl"})


def map_routes_to_physical_intent(
    intent: Dict[str, object],
    routes: List[Dict[str, object]],
    legacy_mapping: Dict[str, object],
) -> List[Dict[str, object]]:
    intent_class = intent.get("intent_classification")
    explicit_roles = intent.get("explicit_roles") is True
    mapped_pairs = _mapped_pairs(legacy_mapping)

    evaluations: List[Dict[str, object]] = []

    for route in routes:
        route_id = route.get("ratio_id") or "unknown_route"
        role_match = _route_key(route) in mapped_pairs
        physical_match = False
        blocking_reason = None

        if intent_class == "conflicting":
            blocking_reason = "intent_conflicting"
        elif intent_class == "undefined_or_ambiguous":
            blocking_reason = "intent_ambiguous"
        elif intent_class == "anomaly_final_cosmological_ratio":
            if not role_match:
                blocking_reason = "c_cosmo_mapping_missing"
            else:
                physical_match = True
        elif intent_class == "causal_ctp_response_ratio":
            if not explicit_roles:
                blocking_reason = "explicit_roles_missing"
            elif not _is_im_log_route(route):
                blocking_reason = "route_not_causal_ctp"
            else:
                physical_match = True
        elif intent_class == "curvature_anomaly_ratio":
            if not explicit_roles:
                blocking_reason = "explicit_roles_missing"
            elif not _is_curvature_route(route):
                blocking_reason = "route_not_curvature_ratio"
            else:
                physical_match = True
        else:
            blocking_reason = "intent_unhandled"

        evaluations.append(
            {
                "route_id": route_id,
                "physical_match": physical_match,
                "role_match": role_match,
                "source_support": intent.get("source_support", []),
                "blocking_reason": blocking_reason,
                "promotes_claims": False,
            }
        )

    return evaluations
