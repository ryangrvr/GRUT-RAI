"""Stage P9 controlled symbolic R attempt."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.stage_p8_r_legality_with_protected_kernels import (
    run_stage_p8_r_legality_with_protected_kernels,
)
from grut.hard_theory.s4_ctp_solver.protected_symbolic_r_constructor import (
    build_protected_symbolic_r,
)
from grut.hard_theory.s4_ctp_solver.protected_symbolic_r_checks import (
    check_protected_symbolic_ratio_topology,
    check_protected_symbolic_cancellation,
    check_protected_symbolic_regulator_independence,
    check_protected_symbolic_pair_consistency,
)


def run_stage_p9_controlled_symbolic_r_attempt() -> Dict[str, object]:
    stage_p8 = run_stage_p8_r_legality_with_protected_kernels()
    valid_pairs = stage_p8.get("valid_pairs", [])

    symbolic_candidates: List[Dict[str, object]] = []
    blocked_pairs: List[Dict[str, object]] = []

    for entry in valid_pairs:
        pair = entry.get("pair", entry)
        topology = check_protected_symbolic_ratio_topology(pair)
        cancellation = check_protected_symbolic_cancellation(pair)
        regulator = check_protected_symbolic_regulator_independence(pair)
        consistency = check_protected_symbolic_pair_consistency(pair)

        record = {
            "pair": pair,
            "topology": topology,
            "cancellation": cancellation,
            "regulator": regulator,
            "consistency": consistency,
            "promotes_claims": False,
        }

        if all(
            check.get("status") == "pass"
            for check in (topology, cancellation, regulator, consistency)
        ):
            record["symbolic_r"] = build_protected_symbolic_r(pair)
            symbolic_candidates.append(record)
        else:
            blocked_pairs.append(record)

    r_symbolic_ready = bool(symbolic_candidates)
    next_action = (
        "review_symbolic_r_consistency"
        if r_symbolic_ready
        else "repair_symbolic_r_topology"
    )

    return {
        "stage": "P9",
        "status": "controlled_symbolic_r_attempt",
        "symbolic_pairs_examined": len(valid_pairs),
        "symbolic_candidates": symbolic_candidates,
        "blocked_pairs": blocked_pairs,
        "r_symbolic_ready": r_symbolic_ready,
        "r_computation_allowed": False,
        "next_required_action": next_action,
        "promotes_claims": False,
        "stage_p8": stage_p8,
    }
