"""Collect partition attempts for consistency auditing."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.stage10c_multi_subintegrand_consistency import (
    run_stage10c_multi_subintegrand_consistency,
)
from grut.hard_theory.s4_ctp_solver.stage10e_eligible_partition_dry_runs import (
    run_stage10e_eligible_partition_dry_runs,
)


def collect_partition_attempts() -> Dict[str, object]:
    stage10c = run_stage10c_multi_subintegrand_consistency()
    stage10e = run_stage10e_eligible_partition_dry_runs()

    collected: List[Dict[str, object]] = []
    for attempt in stage10c.get("attempts", {}).get("attempts", []):
        collected.append({**attempt, "source_stage": "10C"})
    for attempt in stage10e.get("attempts", {}).get("attempts", []):
        collected.append({**attempt, "source_stage": "10E"})

    return {
        "collected_attempts": collected,
        "source_stages": ["10C", "10E"],
        "new_integrations_performed": False,
        "promotes_claims": False,
    }
