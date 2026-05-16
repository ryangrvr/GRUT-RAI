"""Acceptance checks for nonlocal kernel derivation attempts."""

from typing import Dict, List


def evaluate_kernel_acceptance(
    derived: Dict[str, object],
    regulator_check: Dict[str, object],
    ward_ctp_check: Dict[str, object],
) -> Dict[str, object]:
    failures: List[str] = []

    if not derived.get("nonlocal_form_present"):
        failures.append("nonlocal_form_missing")
    if derived.get("scaffold_only"):
        failures.append("scaffold_only")
    if regulator_check.get("status") != "pass":
        failures.append("regulator_check_failed")
    if ward_ctp_check.get("status") != "pass":
        failures.append("ward_ctp_check_failed")
    if not derived.get("local_counterterm_nonmixing_checked"):
        failures.append("counterterm_nonmixing_unchecked")
    if not derived.get("finite_coefficient_extractable"):
        failures.append("finite_extractability_unavailable")

    accepted = not failures
    return {
        "accepted": accepted,
        "failures": failures,
        "promotes_claims": False,
    }
