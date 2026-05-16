"""Protected quotient selection rule evaluation."""

from typing import Dict, List, Set


def _ratio_id(ratio: Dict[str, object]) -> str:
    ratio_id = ratio.get("ratio_id")
    if ratio_id:
        return str(ratio_id)
    pair = ratio.get("pair", {})
    left = pair.get("left", {})
    right = pair.get("right", {})
    return f"{left.get('candidate_id')}__{right.get('candidate_id')}"


def _source_type(pair: Dict[str, object], side: str) -> str:
    return str(pair.get(side, {}).get("source_type") or "")


def _has_im_log(pair: Dict[str, object]) -> bool:
    return "im_log" in _source_type(pair, "left").lower() or "im_log" in _source_type(
        pair, "right"
    ).lower()


def _is_curvature_only(pair: Dict[str, object]) -> bool:
    left = _source_type(pair, "left").lower()
    right = _source_type(pair, "right").lower()
    curvature = {"r_log_box_r", "weyl_log_box_weyl"}
    return left in curvature and right in curvature


def _is_im_curvature_mix(pair: Dict[str, object]) -> bool:
    left = _source_type(pair, "left").lower()
    right = _source_type(pair, "right").lower()
    return ("im_log" in left and ("r_log" in right or "weyl_log" in right)) or (
        "im_log" in right and ("r_log" in left or "weyl_log" in left)
    )


def rule_ctp_causal_priority(
    ratios: List[Dict[str, object]],
    assumptions: Dict[str, object],
) -> Dict[str, object]:
    applicable = bool(assumptions.get("ctp_causal_priority"))
    selected: List[str] = []
    rejected: List[str] = []

    if not applicable:
        return {
            "rule_id": "ctp_causal_priority",
            "applicable": False,
            "selected_ratio_ids": [],
            "rejected_ratio_ids": [],
            "reason": "ctp_priority_not_enabled",
            "manual_choice": False,
            "promotes_claims": False,
        }

    if not assumptions.get("r_definition"):
        return {
            "rule_id": "ctp_causal_priority",
            "applicable": True,
            "selected_ratio_ids": [],
            "rejected_ratio_ids": [],
            "reason": "r_definition_missing",
            "manual_choice": False,
            "promotes_claims": False,
        }

    for ratio in ratios:
        pair = ratio.get("pair", {})
        ratio_id = _ratio_id(ratio)
        if _has_im_log(pair):
            selected.append(ratio_id)
        else:
            rejected.append(ratio_id)

    return {
        "rule_id": "ctp_causal_priority",
        "applicable": True,
        "selected_ratio_ids": selected,
        "rejected_ratio_ids": rejected,
        "reason": "ctp_priority_applied",
        "manual_choice": False,
        "promotes_claims": False,
    }


def rule_curvature_sector_purity(
    ratios: List[Dict[str, object]],
    assumptions: Dict[str, object],
) -> Dict[str, object]:
    applicable = bool(assumptions.get("curvature_sector_target"))
    selected: List[str] = []
    rejected: List[str] = []

    if not applicable:
        return {
            "rule_id": "curvature_sector_purity",
            "applicable": False,
            "selected_ratio_ids": [],
            "rejected_ratio_ids": [],
            "reason": "curvature_target_not_enabled",
            "manual_choice": False,
            "promotes_claims": False,
        }

    for ratio in ratios:
        ratio_id = _ratio_id(ratio)
        if _is_curvature_only(ratio.get("pair", {})):
            selected.append(ratio_id)
        else:
            rejected.append(ratio_id)

    return {
        "rule_id": "curvature_sector_purity",
        "applicable": True,
        "selected_ratio_ids": selected,
        "rejected_ratio_ids": rejected,
        "reason": "curvature_only_required",
        "manual_choice": False,
        "promotes_claims": False,
    }


def rule_same_family_rejection(
    ratios: List[Dict[str, object]],
    assumptions: Dict[str, object],
) -> Dict[str, object]:
    mapping_exists = bool(assumptions.get("imaginary_real_bridge"))
    rejected: List[str] = []

    for ratio in ratios:
        pair = ratio.get("pair", {})
        if _is_im_curvature_mix(pair) and not mapping_exists:
            rejected.append(_ratio_id(ratio))

    return {
        "rule_id": "same_family_rejection",
        "applicable": True,
        "selected_ratio_ids": [],
        "rejected_ratio_ids": rejected,
        "reason": "imaginary_curvature_mapping_required",
        "manual_choice": False,
        "promotes_claims": False,
    }


def rule_imaginary_real_bridge(
    ratios: List[Dict[str, object]],
    assumptions: Dict[str, object],
) -> Dict[str, object]:
    applicable = bool(assumptions.get("imaginary_real_bridge"))
    selected: List[str] = []
    rejected: List[str] = []

    if not applicable:
        return {
            "rule_id": "imaginary_real_bridge",
            "applicable": False,
            "selected_ratio_ids": [],
            "rejected_ratio_ids": [],
            "reason": "ctp_to_curvature_projection_missing",
            "manual_choice": False,
            "promotes_claims": False,
        }

    for ratio in ratios:
        pair = ratio.get("pair", {})
        ratio_id = _ratio_id(ratio)
        if _is_im_curvature_mix(pair):
            selected.append(ratio_id)
        else:
            rejected.append(ratio_id)

    return {
        "rule_id": "imaginary_real_bridge",
        "applicable": True,
        "selected_ratio_ids": selected,
        "rejected_ratio_ids": rejected,
        "reason": "ctp_to_curvature_projection_present",
        "manual_choice": False,
        "promotes_claims": False,
    }


def rule_r_definition(
    ratios: List[Dict[str, object]],
    assumptions: Dict[str, object],
) -> Dict[str, object]:
    r_definition = assumptions.get("r_definition")
    if not isinstance(r_definition, dict):
        return {
            "rule_id": "r_definition",
            "applicable": False,
            "selected_ratio_ids": [],
            "rejected_ratio_ids": [],
            "reason": "r_definition_missing",
            "manual_choice": False,
            "promotes_claims": False,
        }

    numerator = str(r_definition.get("numerator_source_type") or "")
    denominator = str(r_definition.get("denominator_source_type") or "")
    if not numerator or not denominator:
        return {
            "rule_id": "r_definition",
            "applicable": False,
            "selected_ratio_ids": [],
            "rejected_ratio_ids": [],
            "reason": "r_definition_incomplete",
            "manual_choice": False,
            "promotes_claims": False,
        }

    selected: List[str] = []
    rejected: List[str] = []
    for ratio in ratios:
        pair = ratio.get("pair", {})
        left = _source_type(pair, "left")
        right = _source_type(pair, "right")
        ratio_id = _ratio_id(ratio)
        if left == numerator and right == denominator:
            selected.append(ratio_id)
        else:
            rejected.append(ratio_id)

    return {
        "rule_id": "r_definition",
        "applicable": True,
        "selected_ratio_ids": selected,
        "rejected_ratio_ids": rejected,
        "reason": "r_definition_applied",
        "manual_choice": False,
        "promotes_claims": False,
    }


def evaluate_selection_rules(
    ratios: List[Dict[str, object]],
    assumptions: Dict[str, object],
) -> List[Dict[str, object]]:
    return [
        rule_ctp_causal_priority(ratios, assumptions),
        rule_curvature_sector_purity(ratios, assumptions),
        rule_same_family_rejection(ratios, assumptions),
        rule_imaginary_real_bridge(ratios, assumptions),
        rule_r_definition(ratios, assumptions),
    ]


def collect_ratio_ids(ratios: List[Dict[str, object]]) -> List[str]:
    seen: Set[str] = set()
    ordered: List[str] = []
    for ratio in ratios:
        ratio_id = _ratio_id(ratio)
        if ratio_id not in seen:
            seen.add(ratio_id)
            ordered.append(ratio_id)
    return ordered
