"""Stage 12G R-route terminal audit package."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage12a_coefficient_assembly_dry_run import (
    run_stage12a_coefficient_assembly_dry_run,
)
from grut.hard_theory.s4_ctp_solver.stage12b_scheme_stability_audit import (
    run_stage12b_scheme_stability_audit,
)
from grut.hard_theory.s4_ctp_solver.stage12c_r_legality_gate import (
    run_stage12c_r_legality_gate,
)
from grut.hard_theory.s4_ctp_solver.stage12d_r_extraction_attempt import (
    run_stage12d_r_extraction_attempt,
)
from grut.hard_theory.s4_ctp_solver.stage12e_r_result_classification import (
    run_stage12e_r_result_classification,
)
from grut.hard_theory.s4_ctp_solver.stage12f_r_status_report import (
    run_stage12f_r_status_report,
)
from grut.hard_theory.s4_ctp_solver.r_route_blocker_ledger import (
    build_r_route_blocker_ledger,
)
from grut.hard_theory.s4_ctp_solver.r_route_terminal_audit import (
    build_r_route_terminal_audit,
)
from grut.hard_theory.s4_ctp_solver.r_route_terminal_report import (
    build_r_route_terminal_report,
)


def run_stage12g_r_route_terminal_audit() -> Dict[str, object]:
    stage12a = run_stage12a_coefficient_assembly_dry_run()
    stage12b = run_stage12b_scheme_stability_audit()
    stage12c = run_stage12c_r_legality_gate()
    stage12d = run_stage12d_r_extraction_attempt()
    stage12e = run_stage12e_r_result_classification()
    stage12f = run_stage12f_r_status_report()

    ledger = build_r_route_blocker_ledger(stage12c, stage12d, stage12e, stage12f)
    package = build_r_route_terminal_audit(
        stage12a,
        stage12b,
        stage12c,
        stage12d,
        stage12e,
        stage12f,
        ledger,
    )
    report = build_r_route_terminal_report(stage12e, stage12f, ledger)

    return {
        **report,
        "terminal_package": package,
        "stage12a": stage12a,
        "stage12b": stage12b,
        "stage12c": stage12c,
        "stage12d": stage12d,
        "stage12e": stage12e,
        "stage12f": stage12f,
        "ledger": ledger,
        "promotes_claims": False,
    }
