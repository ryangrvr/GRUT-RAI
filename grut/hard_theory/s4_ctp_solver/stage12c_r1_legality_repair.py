"""Stage 12C-R1 legality repair diagnostic."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage11e_cross_partition_finite_consistency import (
    run_stage11e_cross_partition_finite_consistency,
)
from grut.hard_theory.s4_ctp_solver.stage12a_coefficient_assembly_dry_run import (
    run_stage12a_coefficient_assembly_dry_run,
)
from grut.hard_theory.s4_ctp_solver.stage12b_scheme_stability_audit import (
    run_stage12b_scheme_stability_audit,
)
from grut.hard_theory.s4_ctp_solver.r_candidate_selector import (
    identify_r_candidate_pairs,
)
from grut.hard_theory.s4_ctp_solver.r_legality_repair_diagnostic import (
    diagnose_r_legality_repair,
)


def run_stage12c_r1_legality_repair() -> Dict[str, object]:
    stage11e = run_stage11e_cross_partition_finite_consistency()
    stage12a = run_stage12a_coefficient_assembly_dry_run()
    stage12b = run_stage12b_scheme_stability_audit()

    selections = identify_r_candidate_pairs(
        stage12b.get("classifications", {}),
        stage12a.get("registry", {}),
        stage11e,
    )
    candidate_pairs = selections.get("candidate_pairs", [])

    diagnostic = diagnose_r_legality_repair(stage12b.get("classifications", {}), candidate_pairs)
    return {
        **diagnostic,
        "stage12a": stage12a,
        "stage12b": stage12b,
        "stage11e": stage11e,
        "candidate_pairs": candidate_pairs,
        "promotes_claims": False,
    }
