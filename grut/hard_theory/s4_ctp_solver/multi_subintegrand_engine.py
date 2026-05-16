"""Run controlled integration attempts for multiple sub-integrands."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.native_subintegrand_engine import (
    run_native_subintegrand_integration,
)


def run_multi_subintegrand_attempt(
    subintegrands: List[Dict[str, object]],
) -> Dict[str, object]:
    attempts: List[Dict[str, object]] = []
    for subintegrand in subintegrands:
        result = run_native_subintegrand_integration(subintegrand)
        attempt = {
            **result,
            "scheme_id": subintegrand.get("scheme_id"),
            "default_regulator": subintegrand.get("default_regulator"),
        }
        attempts.append(attempt)

    all_regulated = all(attempt.get("regulator_present") is True for attempt in attempts)

    return {
        "attempts": attempts,
        "all_regulated": all_regulated,
        "finite_parts_computed": False,
        "amplitude_computed": False,
        "status": "multi_subintegrand_attempt",
        "promotes_claims": False,
    }
