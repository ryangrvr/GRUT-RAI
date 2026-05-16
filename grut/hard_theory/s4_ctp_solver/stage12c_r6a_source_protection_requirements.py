"""Stage 12C-R6A source protection requirements report."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage12c_r5_protected_source_audit import (
    run_stage12c_r5_protected_source_audit,
)
from grut.hard_theory.s4_ctp_solver.stage10d_integrand_partition_map import (
    run_stage10d_integrand_partition_map,
)
from grut.hard_theory.s4_ctp_solver.stage11e_cross_partition_finite_consistency import (
    run_stage11e_cross_partition_finite_consistency,
)
from grut.hard_theory.s4_ctp_solver.stage12a_coefficient_assembly_dry_run import (
    run_stage12a_coefficient_assembly_dry_run,
)
from grut.hard_theory.s4_ctp_solver.source_protection_gap_report import (
    build_source_protection_gap_report,
)


def run_stage12c_r6a_source_protection_requirements() -> Dict[str, object]:
    stage12c_r5 = run_stage12c_r5_protected_source_audit()
    stage10d = run_stage10d_integrand_partition_map()
    stage11e = run_stage11e_cross_partition_finite_consistency()
    stage12a = run_stage12a_coefficient_assembly_dry_run()

    gaps = build_source_protection_gap_report(stage12c_r5, stage10d, stage11e, stage12a)
    sources = gaps.get("sources", [])
    sources_reclassifiable = [
        entry for entry in sources if entry.get("can_be_reclassified_now") is True
    ]

    c_final_allowed = (
        stage12c_r5.get("c_final_reclassification_eligible") is True
        and len(sources) > 0
        and len(sources_reclassifiable) == len(sources)
    )

    return {
        "stage": "12C-R6A",
        "status": "source_protection_requirements_report",
        "sources_examined": len(sources),
        "sources_reclassifiable_now": len(sources_reclassifiable),
        "c_final_reclassification_allowed": c_final_allowed,
        "r_computation_allowed": False,
        "next_required_action": "derive_or_identify_nonlocal_anomaly_protected_source",
        "promotes_claims": False,
        "sources": sources,
        "stage12c_r5": stage12c_r5,
        "stage10d": stage10d,
        "stage11e": stage11e,
        "stage12a": stage12a,
        "gap_report": gaps,
    }
