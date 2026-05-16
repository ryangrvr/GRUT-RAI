"""Check cancellation readiness for candidate coefficient pairs."""

from typing import Dict


def check_r_cancellation(pair: Dict[str, object]) -> Dict[str, object]:
    numerator = pair.get("numerator", {})
    denominator = pair.get("denominator", {})

    num_ready = numerator.get("cancellation_ready", {})
    den_ready = denominator.get("cancellation_ready", {})

    required_keys = [
        "divergence_cancellation",
        "regulator_cancellation",
        "scheme_cancellation",
    ]

    if not isinstance(num_ready, dict) or not isinstance(den_ready, dict):
        return {
            "cancellation_valid": False,
            "reason": "cancellation_inputs_missing",
            "promotes_claims": False,
        }

    for key in required_keys:
        if key not in num_ready or key not in den_ready:
            return {
                "cancellation_valid": False,
                "reason": "cancellation_inputs_missing",
                "promotes_claims": False,
            }
        if not num_ready.get(key) or not den_ready.get(key):
            return {
                "cancellation_valid": False,
                "reason": f"{key}_failed",
                "promotes_claims": False,
            }

    return {
        "cancellation_valid": True,
        "reason": "cancellation_valid",
        "promotes_claims": False,
    }
