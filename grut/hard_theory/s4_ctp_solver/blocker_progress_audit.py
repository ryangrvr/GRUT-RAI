"""Progress audit for multi-blocker closure harness."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.blocker_registry import register_blockers


def run_blocker_progress_audit() -> Dict[str, object]:
    blockers: List[Dict[str, object]] = register_blockers()
    closed = [blocker for blocker in blockers if blocker["closure_status"] == "closed"]

    return {
        "stage": "6B",
        "status": "multi_blocker_closure_harness",
        "blockers_registered": len(blockers),
        "blockers_closed": len(closed),
        "can_extract": False,
        "can_compute_r": False,
        "can_promote_r_route": False,
        "promotes_claims": False,
        "blockers": blockers,
    }
