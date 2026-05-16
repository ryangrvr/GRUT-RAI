"""Stage N2 imaginary/causal sector audit."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage6a_scheme_alignment import (
    run_stage6a_scheme_alignment,
)
from grut.hard_theory.s4_ctp_solver.stage5d_candidate_readiness import (
    run_stage5d_candidate_readiness,
)
from grut.hard_theory.s4_ctp_solver.imaginary_causal_sector_scan import (
    find_imaginary_causal_sources,
)


def run_stageN2_imaginary_causal_sector_audit() -> Dict[str, object]:
    stage6a = run_stage6a_scheme_alignment()
    stage5d = run_stage5d_candidate_readiness()

    scan = find_imaginary_causal_sources(stage6a.get("report", {}), stage5d)
    protected_sources_found = scan.get("protected_sources_found", 0)

    return {
        "stage": "N2",
        "status": "imaginary_causal_sector_audit",
        "protected_sources_found": protected_sources_found,
        "candidate_sources": scan.get("candidate_sources", []),
        "can_build_second_protected_coefficient": protected_sources_found >= 2,
        "r_computation_allowed": False,
        "promotes_claims": False,
        "stage6a": stage6a,
        "stage5d": stage5d,
    }
