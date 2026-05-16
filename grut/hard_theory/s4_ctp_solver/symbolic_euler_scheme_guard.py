"""Scheme guard for OR6 symbolic Euler extraction."""

from typing import Dict, List, Optional


def _binding_by_role(bindings: List[Dict[str, object]], role_id: str) -> Optional[Dict[str, object]]:
    for entry in bindings:
        if entry.get("role_id") == role_id:
            return entry
    return None


def _scheme_protected_sources(stage_p7: Dict[str, object]) -> List[str]:
    protected_ids = {
        entry.get("candidate_id")
        for entry in stage_p7.get("scheme_protected_candidates", [])
    }
    stage_p6 = stage_p7.get("stage_p6", {})
    registered = stage_p6.get("registered_candidates", [])

    protected_sources: List[str] = []
    for entry in registered:
        candidate_id = entry.get("protected_source_candidate_id")
        if candidate_id in protected_ids:
            source_type = entry.get("source_type")
            if source_type:
                protected_sources.append(source_type)

    return protected_sources


def _ratio_regulator_class(
    stage_p11_r2: Dict[str, object],
    numerator_source: Optional[str],
    denominator_source: Optional[str],
) -> Optional[str]:
    for ratio in stage_p11_r2.get("refreshed_ratios", []):
        pair = ratio.get("pair", {})
        left = pair.get("left", {})
        right = pair.get("right", {})
        if (
            left.get("source_type") == numerator_source
            and right.get("source_type") == denominator_source
        ):
            return ratio.get("ratio_regulator_class")
    return None


def evaluate_scheme_guard(
    bindings: List[Dict[str, object]],
    stage_p7: Dict[str, object],
    stage_p8: Dict[str, object],
    stage_p11_r2: Dict[str, object],
    projection_domain: str,
) -> Dict[str, object]:
    failures: List[str] = []

    numerator = _binding_by_role(bindings, "euler_numerator")
    denominator = _binding_by_role(bindings, "euler_denominator")

    if not numerator or not denominator:
        failures.append("binding_missing")
        return {
            "scheme_guard_passed": False,
            "scheme_failures": failures,
            "regulator_class": None,
            "projection_domain": projection_domain,
            "promotes_claims": False,
        }

    if numerator.get("status") != "bound" or denominator.get("status") != "bound":
        failures.append("binding_incomplete")

    if numerator.get("coefficient_value") is not None or denominator.get("coefficient_value") is not None:
        failures.append("coefficient_value_present")

    blocked_sources = {"Weyl_log_box_Weyl", "Im_log_minus_box_i_epsilon"}
    binding_sources = {entry.get("source_type") for entry in bindings if entry.get("source_type")}
    if binding_sources.intersection(blocked_sources):
        failures.append("non_euler_route_contamination")

    protected_sources = set(_scheme_protected_sources(stage_p7))
    if numerator.get("source_type") not in protected_sources:
        failures.append("numerator_not_scheme_protected")
    if denominator.get("source_type") not in protected_sources:
        failures.append("denominator_not_scheme_protected")

    if stage_p8.get("r_legal") is not True:
        failures.append("protected_legality_missing")

    ratio_regulator_class = _ratio_regulator_class(
        stage_p11_r2,
        numerator.get("source_type"),
        denominator.get("source_type"),
    )
    if ratio_regulator_class != "matched_dimensional_symbolic_preserved":
        failures.append("regulator_mismatch")

    if projection_domain != "round_s4_euler_channel":
        failures.append("projection_domain_mismatch")

    regulator_class = (
        "dimensional_regularization_symbolic_preserved"
        if not failures
        else None
    )

    return {
        "scheme_guard_passed": not failures,
        "scheme_failures": failures,
        "regulator_class": regulator_class,
        "projection_domain": projection_domain,
        "promotes_claims": False,
    }


def check_symbolic_euler_scheme_guard(quotient: Dict[str, object]) -> Dict[str, object]:
    failures: List[str] = []

    if quotient.get("scheme_protected") is not True:
        failures.append("scheme_protection_missing")
    if quotient.get("regulator_class") != "dimensional_regularization_symbolic_preserved":
        failures.append("regulator_mismatch")
    if quotient.get("projection_domain") != "round_s4_euler_channel":
        failures.append("projection_domain_mismatch")
    if quotient.get("numeric_value") is not None:
        failures.append("numeric_value_present")

    return {
        "scheme_guard_passed": not failures,
        "scheme_failures": failures,
        "promotes_claims": False,
    }
