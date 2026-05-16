"""Execute cancellation steps for symbolic R."""

from typing import Dict


def _ready_flag(payload: Dict[str, object], key: str) -> bool:
    ready = payload.get("cancellation_ready", {})
    return isinstance(ready, dict) and ready.get(key) is True


def execute_r_cancellation(symbolic_r: Dict[str, object]) -> Dict[str, object]:
    numerator = symbolic_r.get("numerator", {})
    denominator = symbolic_r.get("denominator", {})

    divergence_ok = _ready_flag(numerator, "divergence_cancellation") and _ready_flag(
        denominator, "divergence_cancellation"
    )
    regulator_ok = _ready_flag(numerator, "regulator_cancellation") and _ready_flag(
        denominator, "regulator_cancellation"
    )
    scheme_ok = _ready_flag(numerator, "scheme_cancellation") and _ready_flag(
        denominator, "scheme_cancellation"
    )

    cancellation_valid = divergence_ok and regulator_ok and scheme_ok
    reason = "cancellation_valid" if cancellation_valid else "cancellation_failed"

    return {
        "symbolic_ratio": symbolic_r.get("symbolic_ratio"),
        "divergence_cancelled": divergence_ok,
        "regulator_dependence_cancelled": regulator_ok,
        "scheme_dependence_cancelled": scheme_ok,
        "cancellation_valid": cancellation_valid,
        "reason": reason,
        "promotes_claims": False,
    }
