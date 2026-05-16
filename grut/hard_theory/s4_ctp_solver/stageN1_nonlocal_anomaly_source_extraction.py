"""Stage N1 nonlocal anomaly-channel source extraction report."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage6a_scheme_alignment import (
    run_stage6a_scheme_alignment,
)
from grut.hard_theory.s4_ctp_solver.stage5d_candidate_readiness import (
    run_stage5d_candidate_readiness,
)
from grut.hard_theory.s4_ctp_solver.nonlocal_anomaly_source_scan import (
    find_nonlocal_anomaly_sources,
)


def run_stageN1_nonlocal_anomaly_source_extraction() -> Dict[str, object]:
    stage6a = run_stage6a_scheme_alignment()
    stage5d = run_stage5d_candidate_readiness()

    report = find_nonlocal_anomaly_sources(stage6a.get("report", {}), stage5d)
    protected_sources_found = report.get("protected_sources_found", 0)

    return {
        "stage": "N1",
        "status": "nonlocal_anomaly_source_extraction",
        "protected_sources_found": protected_sources_found,
        "candidate_sources": report.get("candidate_sources", []),
        "can_build_second_protected_coefficient": protected_sources_found >= 2,
        "r_computation_allowed": False,
        "promotes_claims": False,
        "stage6a": stage6a,
        "stage5d": stage5d,
    }
