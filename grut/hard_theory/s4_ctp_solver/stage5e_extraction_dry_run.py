"""Stage 5E legal extraction criteria and dry-run report."""

from typing import Dict, List

from grut.hard_theory.s4_ctp_solver.extraction_criteria import (
    define_extraction_criteria,
)
from grut.hard_theory.s4_ctp_solver.extraction_requirement_mapper import (
    map_blockers_to_requirements,
)
from grut.hard_theory.s4_ctp_solver.extraction_dry_run import (
    perform_extraction_dry_run,
)
from grut.hard_theory.s4_ctp_solver.extraction_readiness_audit import (
    audit_extraction_readiness,
)
from grut.hard_theory.s4_ctp_solver.stage5d_candidate_readiness import (
    run_stage5d_candidate_readiness,
)


def run_stage5e_extraction_dry_run() -> Dict[str, object]:
    stage5d = run_stage5d_candidate_readiness()
    criteria = define_extraction_criteria()

    candidates = stage5d.get("candidates", [])
    blockers_list = stage5d.get("blockers", [])

    requirement_maps: List[Dict[str, object]] = []
    dry_runs: List[Dict[str, object]] = []
    audits: List[Dict[str, object]] = []

    for candidate in candidates:
        blockers = next(
            (
                entry
                for entry in blockers_list
                if entry.get("candidate_id") == candidate.get("candidate_id")
            ),
            {"candidate_id": candidate.get("candidate_id", "unknown_candidate"), "blockers": []},
        )
        requirement_maps.append(map_blockers_to_requirements(blockers))
        dry_runs.append(perform_extraction_dry_run(candidate))
        audits.append(audit_extraction_readiness(candidate, criteria))

    return {
        "stage": "5E",
        "status": "extraction_dry_run",
        "candidates_processed": len(candidates),
        "any_extraction_allowed": False,
        "all_blocked": True,
        "next_steps": [
            "compute finite parts",
            "establish convergence",
            "resolve tensor contractions",
            "fix scheme alignment",
            "verify Ward identities",
            "independent replication",
        ],
        "promotes_claims": False,
        "criteria": criteria,
        "guard": stage5d.get("guard"),
        "requirements": requirement_maps,
        "dry_runs": dry_runs,
        "audits": audits,
    }
