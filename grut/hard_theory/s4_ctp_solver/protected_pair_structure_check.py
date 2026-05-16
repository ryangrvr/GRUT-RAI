"""Check structural compatibility for protected kernel pairs."""

from __future__ import annotations

from typing import Dict, List


def _compatible_regulator(left: Dict[str, object], right: Dict[str, object]) -> bool:
    left_reg = left.get("regulator_class")
    right_reg = right.get("regulator_class")
    if left_reg == "unknown" or right_reg == "unknown":
        return True
    return left_reg == right_reg


def _compatible_source_family(left: Dict[str, object], right: Dict[str, object]) -> bool:
    return left.get("source_family") == right.get("source_family")


def check_protected_pair_structure(
    pair: Dict[str, object],
    stage_p4: Dict[str, object],
    stage_p5: Dict[str, object],
) -> Dict[str, object]:
    failures: List[str] = []
    left = pair.get("left", {})
    right = pair.get("right", {})

    if not left.get("scheme_protected") or not right.get("scheme_protected"):
        failures.append("scheme_protected_required")

    if left.get("coefficient_value") is not None or right.get("coefficient_value") is not None:
        failures.append("coefficient_value_present")

    if not _compatible_regulator(left, right):
        failures.append("regulator_incompatible")

    if not _compatible_source_family(left, right):
        failures.append("source_family_incompatible")

    for candidate in (left, right):
        if candidate.get("nonlocal_form_present") is not True:
            failures.append("nonlocal_form_missing")

    return {
        "pair_id": pair.get("pair_id"),
        "status": "pass" if not failures else "fail",
        "failures": failures,
        "promotes_claims": False,
    }
