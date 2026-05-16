"""Stage P7 protected source scheme injection."""

from typing import Dict

from grut.hard_theory.s4_ctp_solver.stage_p6_protected_source_registration import (
    run_stage_p6_protected_source_registration,
)
from grut.hard_theory.s4_ctp_solver.stage12b_scheme_stability_audit import (
    run_stage12b_scheme_stability_audit,
)
from grut.hard_theory.s4_ctp_solver.stage12a_coefficient_assembly_dry_run import (
    run_stage12a_coefficient_assembly_dry_run,
)
from grut.hard_theory.s4_ctp_solver.stage12c_r_legality_gate import (
    run_stage12c_r_legality_gate,
)
from grut.hard_theory.s4_ctp_solver.protected_source_scheme_injection import (
    inject_protected_sources,
)
from grut.hard_theory.s4_ctp_solver.protected_source_scheme_classifier import (
    classify_protected_scheme_candidates,
)
from grut.hard_theory.s4_ctp_solver.protected_source_scheme_audit import (
    audit_protected_source_scheme_injection,
)
from grut.hard_theory.s4_ctp_solver.scheme_stability_rules import (
    define_scheme_stability_rules,
)
from grut.hard_theory.s4_ctp_solver.scheme_stability_audit import (
    audit_scheme_stability,
)


def run_stage_p7_protected_scheme_injection() -> Dict[str, object]:
    stage_p6 = run_stage_p6_protected_source_registration()
    stage12b = run_stage12b_scheme_stability_audit()
    stage12a = run_stage12a_coefficient_assembly_dry_run()
    stage12c = run_stage12c_r_legality_gate()

    injected = inject_protected_sources(stage_p6)

    rules = define_scheme_stability_rules()
    classifications = classify_protected_scheme_candidates(injected, rules)
    scheme_audit = audit_scheme_stability(classifications, rules)

    scheme_protected_candidates = scheme_audit.get("stable_candidates", [])
    scheme_protected_count = len(scheme_protected_candidates)

    injection_audit = audit_protected_source_scheme_injection(injected, stage_p6)

    return {
        "stage": "P7",
        "status": "protected_source_scheme_injection",
        "injected_count": len(injected),
        "scheme_protected_count": scheme_protected_count,
        "scheme_protected_candidates": scheme_protected_candidates,
        "rerun_12c_legality_recommended": scheme_protected_count >= 2,
        "r_computation_allowed": False,
        "promotes_claims": False,
        "injection_audit": injection_audit,
        "classifications": classifications,
        "scheme_audit": scheme_audit,
        "stage_p6": stage_p6,
        "stage12b": stage12b,
        "stage12a": stage12a,
        "stage12c": stage12c,
    }
