"""Regulator cancellation checks for nonlocal kernel attempts."""

from typing import Dict


def check_regulator_cancellation(stage9c: Dict[str, object], stage11b: Dict[str, object]) -> Dict[str, object]:
    regularization_attached = stage9c.get("regularization_attached")
    regulator_removed = stage11b.get("regulator_removed")

    if regularization_attached is None or regulator_removed is None:
        return {
            "status": "fail",
            "reason": "regulator_metadata_missing",
            "promotes_claims": False,
        }

    if regularization_attached is True and regulator_removed is False:
        return {
            "status": "pass",
            "reason": "regulator_preserved_for_cancellation",
            "promotes_claims": False,
        }

    if regulator_removed is True:
        return {
            "status": "fail",
            "reason": "regulator_removed_before_cancellation",
            "promotes_claims": False,
        }

    return {
        "status": "fail",
        "reason": "regulator_status_unknown",
        "promotes_claims": False,
    }
