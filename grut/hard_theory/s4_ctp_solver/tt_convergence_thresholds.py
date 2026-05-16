"""Threshold definitions for convergence control."""

from typing import Dict


def define_convergence_thresholds() -> Dict[str, object]:
    return {
        "relative_change_threshold": 0.05,
        "scheme_sensitivity_threshold": "low_or_medium",
        "structure_required": True,
        "proof_required_for_full_closure": True,
        "promotes_claims": False,
    }
