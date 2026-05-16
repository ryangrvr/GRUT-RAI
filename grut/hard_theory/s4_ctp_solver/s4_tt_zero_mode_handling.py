"""Zero-mode handling strategy for TT modes on S4."""

from typing import Dict, List


def define_zero_mode_strategy() -> Dict[str, object]:
    problem_modes: List[str] = ["l=0", "l=1"]
    return {
        "zero_mode_id": "s4_tt_zero_modes",
        "problem_modes": problem_modes,
        "handling_strategy": [
            "project_out_gauge_modes",
            "exclude_non_invertible_modes",
        ],
        "status": "defined_not_applied",
        "promotes_claims": False,
    }
