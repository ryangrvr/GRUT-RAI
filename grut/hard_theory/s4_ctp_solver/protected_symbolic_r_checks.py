"""Symbolic checks for protected R construction."""

from typing import Dict, List


def check_protected_symbolic_ratio_topology(pair: Dict[str, object]) -> Dict[str, object]:
    failures: List[str] = []
    left = pair.get("left", {})
    right = pair.get("right", {})

    if not left or not right:
        failures.append("pair_incomplete")

    if left.get("candidate_id") == right.get("candidate_id"):
        failures.append("pair_candidates_identical")

    if not left.get("scheme_protected") or not right.get("scheme_protected"):
        failures.append("scheme_protected_required")

    if left.get("coefficient_value") is not None or right.get("coefficient_value") is not None:
        failures.append("coefficient_value_present")

    if left.get("nonlocal_form_present") is not True:
        failures.append("left_nonlocal_form_missing")

    if right.get("nonlocal_form_present") is not True:
        failures.append("right_nonlocal_form_missing")

    if left.get("source_family") != right.get("source_family"):
        failures.append("source_family_incompatible")

    status = "pass" if not failures else "fail"
    return {
        "status": status,
        "failures": failures,
        "pair_id": pair.get("pair_id"),
        "promotes_claims": False,
    }


def check_protected_symbolic_cancellation(pair: Dict[str, object]) -> Dict[str, object]:
    failures: List[str] = []
    left = pair.get("left", {})
    right = pair.get("right", {})

    if not left.get("counterterm_nonmixing_verified") or not right.get(
        "counterterm_nonmixing_verified"
    ):
        failures.append("counterterm_nonmixing_unverified")

    if not left.get("finite_extractability") or not right.get("finite_extractability"):
        failures.append("finite_extractability_unavailable")

    status = "pass" if not failures else "fail"
    return {
        "status": status,
        "failures": failures,
        "pair_id": pair.get("pair_id"),
        "promotes_claims": False,
    }


def check_protected_symbolic_regulator_independence(
    pair: Dict[str, object],
) -> Dict[str, object]:
    failures: List[str] = []
    warnings: List[str] = []
    left = pair.get("left", {})
    right = pair.get("right", {})

    left_reg = left.get("regulator_class")
    right_reg = right.get("regulator_class")

    if not left_reg or not right_reg:
        failures.append("regulator_class_missing")
    elif left_reg != right_reg:
        failures.append("regulator_class_mismatch")
    elif left_reg == "unknown":
        warnings.append("regulator_class_unknown")

    status = "pass" if not failures else "fail"
    return {
        "status": status,
        "failures": failures,
        "warnings": warnings,
        "pair_id": pair.get("pair_id"),
        "promotes_claims": False,
    }


def check_protected_symbolic_pair_consistency(
    pair: Dict[str, object],
) -> Dict[str, object]:
    failures: List[str] = []
    left = pair.get("left", {})
    right = pair.get("right", {})

    if left.get("source_type") == right.get("source_type"):
        failures.append("pair_source_types_identical")

    if left.get("kernel_id") == right.get("kernel_id"):
        failures.append("pair_kernel_ids_identical")

    status = "pass" if not failures else "fail"
    return {
        "status": status,
        "failures": failures,
        "pair_id": pair.get("pair_id"),
        "promotes_claims": False,
    }
