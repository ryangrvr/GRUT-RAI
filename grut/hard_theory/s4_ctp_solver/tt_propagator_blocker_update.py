"""Blocker update for TT propagator scaffold status."""

from typing import Dict


def update_tt_blocker_status() -> Dict[str, object]:
    return {
        "blocker": "full_S4_propagator_missing",
        "scalar_conformal_subproblem": "partially_closed",
        "ghost_subproblem": "partially_closed",
        "harmonic_sector": "benchmarked",
        "tt_propagator_scaffold": "constructed",
        "tt_propagator_inverted": "open",
        "overall_blocker_closed": False,
        "promotes_claims": False,
    }
