"""Classify protected symbolic ratio candidates."""

from typing import Dict, Iterable, List, Set


_FORBIDDEN_VALUE_KEYS: Set[str] = {
    "coefficient_value",
    "numeric_value",
    "ratio_value",
    "r_value",
}


def _collect_nonnull_keys(payload: Dict[str, object], keys: Iterable[str]) -> List[str]:
    violations: List[str] = []
    for key in keys:
        if payload.get(key) is not None:
            violations.append(key)
    return violations


def _has_local_fragile_source(candidate: Dict[str, object]) -> bool:
    source_family = (candidate.get("source_family") or "").lower()
    if not source_family:
        return False
    return source_family != "nonlocal_kernel"


def _ratio_id(pair: Dict[str, object]) -> str:
    pair_id = pair.get("pair_id")
    if pair_id:
        return str(pair_id)
    left = pair.get("left", {})
    right = pair.get("right", {})
    return f"{left.get('candidate_id')}__{right.get('candidate_id')}"


def classify_symbolic_ratio(
    candidate_entry: Dict[str, object],
    scheme_protected_candidates: List[Dict[str, object]],
    readiness_candidates: List[Dict[str, object]],
) -> Dict[str, object]:
    pair = candidate_entry.get("pair", {})
    symbolic_r = candidate_entry.get("symbolic_r")
    left = pair.get("left", {})
    right = pair.get("right", {})

    ratio_id = _ratio_id(pair)
    reasons: List[str] = []
    invalid_reasons: List[str] = []

    if candidate_entry.get("promotes_claims") is True:
        invalid_reasons.append("promotes_claims")

    if not symbolic_r or not symbolic_r.get("numerator") or not symbolic_r.get("denominator"):
        invalid_reasons.append("symbolic_ratio_missing")

    for candidate in (left, right):
        if not isinstance(candidate, dict):
            invalid_reasons.append("pair_incomplete")
            break
        invalid_reasons.extend(_collect_nonnull_keys(candidate, _FORBIDDEN_VALUE_KEYS))

    scheme_ids = {entry.get("candidate_id") for entry in scheme_protected_candidates}
    if left.get("candidate_id") not in scheme_ids or right.get("candidate_id") not in scheme_ids:
        reasons.append("scheme_protected_required")

    if _has_local_fragile_source(left) or _has_local_fragile_source(right):
        reasons.append("local_fragile_source_contamination")

    left_reg = left.get("regulator_class")
    right_reg = right.get("regulator_class")
    regulator_mismatch = False
    if not left_reg or not right_reg:
        regulator_mismatch = True
        reasons.append("regulator_class_missing")
    elif left_reg != right_reg:
        regulator_mismatch = True
        reasons.append("regulator_class_mismatch")

    readiness_sources = {entry.get("source_type") for entry in readiness_candidates}
    if left.get("source_type") not in readiness_sources or right.get("source_type") not in readiness_sources:
        reasons.append("readiness_missing")

    cancellation_ready = (
        left.get("counterterm_nonmixing_verified")
        and right.get("counterterm_nonmixing_verified")
        and left.get("finite_extractability")
        and right.get("finite_extractability")
    )
    if not cancellation_ready:
        reasons.append("cancellation_unverified")

    if left.get("coefficient_value") is not None or right.get("coefficient_value") is not None:
        invalid_reasons.append("coefficient_value_present")

    if invalid_reasons:
        classification = "invalid_symbolic_ratio"
        reasons = sorted(set(reasons + invalid_reasons))
    elif regulator_mismatch:
        classification = "blocked_by_regulator_residual"
    elif "cancellation_unverified" in reasons or "readiness_missing" in reasons:
        classification = "blocked_by_cancellation_failure"
    elif "scheme_protected_required" in reasons or "local_fragile_source_contamination" in reasons:
        classification = "blocked_by_pair_incompatibility"
    elif left_reg == "unknown" or right_reg == "unknown":
        classification = "ambiguous_symbolic_ratio"
    else:
        classification = "valid_symbolic_ratio_candidate"

    return {
        "ratio_id": ratio_id,
        "classification": classification,
        "reasons": sorted(set(reasons)) if reasons else [],
        "pair": pair,
        "symbolic_r": symbolic_r,
        "promotes_claims": False,
    }
