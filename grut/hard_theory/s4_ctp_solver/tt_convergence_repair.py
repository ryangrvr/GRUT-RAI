"""Evaluate convergence repair status for TT inversion."""

from typing import Dict, Optional

import sympy as sp


def _safe_float(value: object) -> Optional[float]:
    expr = sp.sympify(value)
    if getattr(expr, "free_symbols", None):
        return None
    try:
        return float(expr.evalf())
    except (TypeError, ValueError):
        return None


def evaluate_convergence_repair(
    metrics: Dict[str, object], thresholds: Dict[str, object]
) -> Dict[str, object]:
    if thresholds.get("structure_required") and not metrics.get("structure_preserved"):
        return {
            "repair_status": "failed",
            "blocker": "insufficient_convergence_control",
            "convergence_observed": False,
            "convergence_proven": False,
            "blocker_closed": False,
            "reason": "Tensor structure not preserved across cutoffs.",
            "promotes_claims": False,
        }

    relative_changes = metrics.get("relative_changes", [])
    threshold = thresholds.get("relative_change_threshold", 0.05)
    numeric_changes = [_safe_float(change) for change in relative_changes]
    changes_ok = (
        bool(relative_changes)
        and all(value is not None and value <= threshold for value in numeric_changes)
    )

    scheme_sensitivity = metrics.get("scheme_sensitivity")
    scheme_ok = scheme_sensitivity in {"low", "medium"}

    if changes_ok and scheme_ok:
        repair_status = "partial_repair"
        convergence_observed = True
        reason = "Relative changes and scheme sensitivity meet partial thresholds."
    else:
        repair_status = "open"
        convergence_observed = False
        reason = "Convergence control thresholds not met."

    return {
        "repair_status": repair_status,
        "blocker": "insufficient_convergence_control",
        "convergence_observed": convergence_observed,
        "convergence_proven": False,
        "blocker_closed": False,
        "reason": reason,
        "promotes_claims": False,
    }
