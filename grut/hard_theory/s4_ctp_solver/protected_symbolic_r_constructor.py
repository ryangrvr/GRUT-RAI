"""Build symbolic R structure from protected kernel pair."""

from typing import Dict


def build_protected_symbolic_r(pair: Dict[str, object]) -> Dict[str, object]:
    left = pair.get("left", {})
    right = pair.get("right", {})

    return {
        "symbolic_ratio": "R_symbolic_protected",
        "pair_id": pair.get("pair_id"),
        "numerator": {
            "candidate_id": left.get("candidate_id"),
            "source_type": left.get("source_type"),
            "kernel_id": left.get("kernel_id"),
            "regulator_class": left.get("regulator_class"),
            "nonlocal_form_present": left.get("nonlocal_form_present"),
            "counterterm_nonmixing_verified": left.get(
                "counterterm_nonmixing_verified"
            ),
            "finite_extractability": left.get("finite_extractability"),
        },
        "denominator": {
            "candidate_id": right.get("candidate_id"),
            "source_type": right.get("source_type"),
            "kernel_id": right.get("kernel_id"),
            "regulator_class": right.get("regulator_class"),
            "nonlocal_form_present": right.get("nonlocal_form_present"),
            "counterterm_nonmixing_verified": right.get(
                "counterterm_nonmixing_verified"
            ),
            "finite_extractability": right.get("finite_extractability"),
        },
        "scheme_protected": True,
        "regulator_class": left.get("regulator_class"),
        "promotes_claims": False,
    }
