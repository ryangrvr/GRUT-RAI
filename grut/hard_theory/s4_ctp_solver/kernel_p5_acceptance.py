"""P5 readiness acceptance checks for nonlocal kernels."""

from __future__ import annotations

from typing import Dict, List


def evaluate_p5_acceptance(
    candidate: Dict[str, object],
    nonmixing_report: Dict[str, object],
    finite_report: Dict[str, object],
    r_computation_allowed: bool,
) -> Dict[str, object]:
    failures: List[str] = []

    if not nonmixing_report.get("counterterm_nonmixing_verified"):
        failures.append("counterterm_nonmixing_unchecked")
    if not finite_report.get("finite_extractability"):
        failures.append("finite_extractability_unavailable")
    if finite_report.get("coefficient_value") is not None:
        failures.append("coefficient_value_present")
    if r_computation_allowed:
        failures.append("r_computation_disallowed")

    accepted = not failures
    return {
        "kernel_id": candidate.get("kernel_id"),
        "accepted_readiness": accepted,
        "remaining_failures": failures,
        "protected_source_derived": False,
        "promotes_claims": False,
    }
