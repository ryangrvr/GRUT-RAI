"""Blocker update for ghost propagator subproblem."""

from typing import Dict


def update_ghost_blocker_status() -> Dict[str, object]:
    return {
        "blocker": "full_S4_propagator_missing",
        "scalar_conformal_subproblem": "partially_closed",
        "ghost_subproblem": "partially_closed",
        "tt_graviton_propagator": "open",
        "vector_tensor_modes": "open",
        "overall_blocker_closed": False,
        "promotes_claims": False,
    }
