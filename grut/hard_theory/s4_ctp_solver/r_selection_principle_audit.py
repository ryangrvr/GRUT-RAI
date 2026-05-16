"""Audit non-manual selection principles for R-route candidates."""

from typing import Dict, List, Optional


_SOURCE_PROFILE = {
    "Im_log_minus_box_i_epsilon": {
        "role": "imaginary_causal_anomaly",
        "physical_meaning": "imaginary/causal CTP sector",
        "kernel_family": "imaginary_log_kernel",
        "causal_relation": "imaginary",
    },
    "R_log_box_R": {
        "role": "curvature_trace",
        "physical_meaning": "curvature trace sector",
        "kernel_family": "curvature_log_kernel",
        "causal_relation": "curvature",
    },
    "Weyl_log_box_Weyl": {
        "role": "curvature_weyl",
        "physical_meaning": "curvature Weyl sector",
        "kernel_family": "curvature_log_kernel",
        "causal_relation": "curvature",
    },
}


def _source_profile(source_type: Optional[str]) -> Dict[str, object]:
    if not source_type:
        return {
            "role": "unknown",
            "physical_meaning": "unknown",
            "kernel_family": "unknown",
            "causal_relation": "unknown",
        }
    return _SOURCE_PROFILE.get(
        source_type,
        {
            "role": "unknown",
            "physical_meaning": "unknown",
            "kernel_family": "unknown",
            "causal_relation": "unknown",
        },
    )


def _scheme_class(left: Dict[str, object], right: Dict[str, object]) -> str:
    if left.get("scheme_protected") and right.get("scheme_protected"):
        return "scheme_protected"
    return "scheme_fragile_or_unknown"


def _causal_relation(left: Dict[str, object], right: Dict[str, object]) -> str:
    left_rel = left.get("causal_relation")
    right_rel = right.get("causal_relation")
    if left_rel == "imaginary" and right_rel == "curvature":
        return "imaginary_over_curvature"
    if left_rel == "curvature" and right_rel == "imaginary":
        return "curvature_over_imaginary"
    if left_rel == right_rel:
        return f"{left_rel}_over_{right_rel}"
    return "unknown"


def _definition_matches_route(
    definition: Dict[str, object],
    numerator_source: Optional[str],
    denominator_source: Optional[str],
) -> bool:
    mapping = definition.get("source_type_mapping")
    if not isinstance(mapping, dict):
        return False
    return (
        mapping.get("numerator_source_type") == numerator_source
        and mapping.get("denominator_source_type") == denominator_source
    )


def _route_from_ratio(
    ratio: Dict[str, object],
    definitions: List[Dict[str, object]],
    selected_ratio_ids: List[str],
) -> Dict[str, object]:
    pair = ratio.get("pair", {})
    left = pair.get("left", {})
    right = pair.get("right", {})

    numerator_source = left.get("source_type")
    denominator_source = right.get("source_type")

    numerator_profile = _source_profile(numerator_source)
    denominator_profile = _source_profile(denominator_source)

    definition_match = any(
        _definition_matches_route(definition, numerator_source, denominator_source)
        for definition in definitions
    )

    selected_by_rule = ratio.get("ratio_id") in selected_ratio_ids

    non_manual_reason = None
    if definition_match:
        non_manual_reason = "r_definition_source_mapping"
    elif selected_by_rule:
        non_manual_reason = "p11_r3_selection_rule"

    regulator_class = (
        ratio.get("symbolic_r", {}).get("regulator_class")
        or left.get("regulator_class")
        or right.get("regulator_class")
    )

    scheme_class = _scheme_class(left, right)
    causal_relation = _causal_relation(numerator_profile, denominator_profile)

    return {
        "ratio_id": ratio.get("ratio_id"),
        "numerator_source_type": numerator_source,
        "denominator_source_type": denominator_source,
        "numerator_role": numerator_profile.get("role"),
        "denominator_role": denominator_profile.get("role"),
        "numerator_physical_meaning": numerator_profile.get("physical_meaning"),
        "denominator_physical_meaning": denominator_profile.get("physical_meaning"),
        "source_family": {
            "numerator": left.get("source_family"),
            "denominator": right.get("source_family"),
        },
        "kernel_family": {
            "numerator": numerator_profile.get("kernel_family"),
            "denominator": denominator_profile.get("kernel_family"),
        },
        "regulator_class": regulator_class,
        "scheme_class": scheme_class,
        "causal_curvature_relation": causal_relation,
        "definition_match": definition_match,
        "non_manual_reason": non_manual_reason,
        "promotes_claims": False,
    }


def build_r_selection_principle_audit(
    ratios: List[Dict[str, object]],
    definition_history: Dict[str, object],
    selection_report: Dict[str, object],
) -> Dict[str, object]:
    definitions = definition_history.get("definitions", [])
    selected_ratio_ids = selection_report.get("selected_ratio_ids", [])

    candidate_routes = [
        _route_from_ratio(ratio, definitions, selected_ratio_ids) for ratio in ratios
    ]

    definition_mapping_found = any(route.get("definition_match") for route in candidate_routes)
    non_manual_reason_found = any(route.get("non_manual_reason") for route in candidate_routes)

    audit_status = "pass" if candidate_routes else "blocked"
    blocking_reasons: List[str] = []
    if not candidate_routes:
        blocking_reasons.append("no_candidate_routes")

    return {
        "candidate_routes": candidate_routes,
        "selection_rule_found": selection_report.get("selection_rule_found") is True,
        "selected_route_ids": list(selected_ratio_ids),
        "definition_mapping_found": definition_mapping_found,
        "non_manual_reason_found": non_manual_reason_found,
        "audit": {
            "status": audit_status,
            "blocking_reasons": blocking_reasons,
            "promotes_claims": False,
        },
        "promotes_claims": False,
    }
