from grut.hard_theory.s4_ctp_solver.r_legality_repair_diagnostic import (
    diagnose_r_legality_repair,
)
from grut.hard_theory.s4_ctp_solver.stage12c_r1_legality_repair import (
    run_stage12c_r1_legality_repair,
)


def _pair(candidate_key, protection_class="local", renorm_shared=True):
    return {
        "numerator": {
            "candidate_key": f"{candidate_key}_num",
            "classification": "scheme_fragile",
            "protection_class": protection_class,
            "renorm_structure_id": "scheme_v1:reg_v1",
        },
        "denominator": {
            "candidate_key": f"{candidate_key}_den",
            "classification": "scheme_protected",
            "protection_class": "nonlocal",
            "renorm_structure_id": "scheme_v1:reg_v1",
        },
        "renorm_structure_shared": renorm_shared,
    }


def test_diagnostic_categorizes_failures(monkeypatch):
    candidate_pairs = [_pair("a"), _pair("b", renorm_shared=False)]
    classifications = {
        "classifications": [
            {"candidate_key": "a_num", "classification": "scheme_fragile"},
            {"candidate_key": "a_den", "classification": "scheme_protected"},
        ]
    }

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.r_legality_repair_diagnostic.check_r_structure_compatibility",
        lambda pair: {"compatible": False, "reason": "renorm_structure_mismatch"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.r_legality_repair_diagnostic.check_r_cancellation",
        lambda pair: {"cancellation_valid": False},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.r_legality_repair_diagnostic.audit_r_legality_inputs",
        lambda pair, structural, cancellation: {"status": "valid"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.r_legality_repair_diagnostic.decide_r_legality",
        lambda pair, structural, cancellation, audit: {"r_legal": False, "reason": "scheme_stability_failed"},
    )

    report = diagnose_r_legality_repair(classifications, candidate_pairs)
    assert report["candidate_pairs_examined"] == 2
    assert "numerator_scheme_fragile" in report["failure_reasons"]
    assert "mixed_local_nonlocal" in report["failure_reasons"]
    assert "renormalization_mismatch" in report["failure_reasons"]
    assert "cancellation_failure" in report["failure_reasons"]
    assert report["minimal_repair"] == "isolate nonlocal source"


def test_stage12c_r1_runner(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r1_legality_repair.run_stage11e_cross_partition_finite_consistency",
        lambda: {},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r1_legality_repair.run_stage12a_coefficient_assembly_dry_run",
        lambda: {"registry": {}},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r1_legality_repair.run_stage12b_scheme_stability_audit",
        lambda: {"classifications": {}},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r1_legality_repair.identify_r_candidate_pairs",
        lambda *args, **kwargs: {"candidate_pairs": []},
    )

    report = run_stage12c_r1_legality_repair()
    assert report["status"] == "r_legality_repair_diagnostic"
    assert report["r_computation_allowed"] is False


def test_package_imports_cleanly():
    import grut.hard_theory.s4_ctp_solver as pkg

    assert pkg.S4CTPPipeline is not None
