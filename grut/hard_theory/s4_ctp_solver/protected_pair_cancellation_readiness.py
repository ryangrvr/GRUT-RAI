"""Assess cancellation readiness for protected kernel pairs."""

from __future__ import annotations

from typing import Dict, List


def assess_protected_pair_cancellation_readiness(
    pair: Dict[str, object],
    structure_check: Dict[str, object],
) -> Dict[str, object]:
    failures: List[str] = []
    left = pair.get("left", {})
    right = pair.get("right", {})

    if structure_check.get("status") != "pass":
        failures.append("structure_check_failed")

    if not left.get("counterterm_nonmixing_verified") or not right.get(
        "counterterm_nonmixing_verified"
    ):
        failures.append("counterterm_nonmixing_unverified")

    if not left.get("finite_extractability") or not right.get("finite_extractability"):
        failures.append("finite_extractability_unavailable")

    if not left.get("regulator_class") or not right.get("regulator_class"):
        failures.append("regulator_class_missing")

    readiness = not failures
    return {
        "pair_id": pair.get("pair_id"),
        "cancellation_ready": readiness,
        "failures": failures,
        "promotes_claims": False,
    }
