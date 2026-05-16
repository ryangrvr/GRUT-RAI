from grut.hard_theory.s4_ctp_solver.r_legality_rerun_after_metadata import (
    rerun_legality_after_metadata,
)
from grut.hard_theory.s4_ctp_solver.stage12c_r4_rerun_legality_after_metadata import (
    run_stage12c_r4_rerun_legality_after_metadata,
)


def _candidate_pair(eligible: bool, compatible: bool) -> dict:
    pair = {
        "numerator": {"candidate_key": "n1"},
        "denominator": {"candidate_key": "d1"},
        "scheme_stable": True,
        "nonlocal_or_anomaly_protected": True,
        "renorm_structure_shared": True,
    }
    pair["selection_status"] = "eligible" if eligible else "rejected"
    pair["reason"] = "eligible_pair" if eligible else "scheme_stability_failed"
    return pair


def test_refuses_to_proceed_if_metadata_incomplete():
    report = rerun_legality_after_metadata({"metadata_completed": False})
    assert report["metadata_completed"] is False
    assert report["candidate_pairs_examined"] == 0
    assert report["r_legal"] is False
    assert report["remaining_blockers"] == ["metadata_incomplete"]


def test_pair_selection_reruns(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.r_legality_rerun_after_metadata.classify_coefficient_candidates",
        lambda registry: {"classifications": []},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.r_legality_rerun_after_metadata.audit_scheme_stability",
        lambda classifications, rules: {"all_r_inputs_stable": True},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.r_legality_rerun_after_metadata.identify_r_candidate_pairs",
        lambda classifications, registry, stage11e: {"candidate_pairs": [_candidate_pair(True, True)]},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.r_legality_rerun_after_metadata.check_r_structure_compatibility",
        lambda pair: {"compatible": True},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.r_legality_rerun_after_metadata.check_r_cancellation",
        lambda pair: {"cancellation_valid": True},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.r_legality_rerun_after_metadata.audit_r_legality_inputs",
        lambda pair, structural, cancellation: {"status": "valid"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.r_legality_rerun_after_metadata.decide_r_legality",
        lambda pair, structural, cancellation, audit: {"r_legal": True},
    )

    report = rerun_legality_after_metadata({"metadata_completed": True, "registry": {}})
    assert report["candidate_pairs_examined"] == 1


def test_missing_metadata_not_present_when_complete(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.r_legality_rerun_after_metadata.classify_coefficient_candidates",
        lambda registry: {"classifications": []},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.r_legality_rerun_after_metadata.audit_scheme_stability",
        lambda classifications, rules: {"all_r_inputs_stable": True},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.r_legality_rerun_after_metadata.identify_r_candidate_pairs",
        lambda classifications, registry, stage11e: {"candidate_pairs": []},
    )

    report = rerun_legality_after_metadata({"metadata_completed": True, "registry": {}})
    assert "metadata_incomplete" not in report["remaining_blockers"]


def test_valid_pairs_only_when_stable_and_structural(monkeypatch):
    pairs = [_candidate_pair(True, True), _candidate_pair(True, False)]

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.r_legality_rerun_after_metadata.classify_coefficient_candidates",
        lambda registry: {"classifications": []},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.r_legality_rerun_after_metadata.audit_scheme_stability",
        lambda classifications, rules: {"all_r_inputs_stable": True},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.r_legality_rerun_after_metadata.identify_r_candidate_pairs",
        lambda classifications, registry, stage11e: {"candidate_pairs": pairs},
    )

    def _structural(pair):
        return {"compatible": pair is pairs[0]}

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.r_legality_rerun_after_metadata.check_r_structure_compatibility",
        _structural,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.r_legality_rerun_after_metadata.check_r_cancellation",
        lambda pair: {"cancellation_valid": True},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.r_legality_rerun_after_metadata.audit_r_legality_inputs",
        lambda pair, structural, cancellation: {"status": "valid"},
    )

    def _decision(pair, structural, cancellation, audit):
        return {"r_legal": structural.get("compatible") is True, "reason": "structure"}

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.r_legality_rerun_after_metadata.decide_r_legality",
        _decision,
    )

    report = rerun_legality_after_metadata({"metadata_completed": True, "registry": {}})
    assert len(report["valid_pairs"]) == 1
    assert report["r_computation_allowed"] is False


def test_no_r_computation():
    report = rerun_legality_after_metadata({"metadata_completed": False})
    assert report["r_computation_allowed"] is False


def test_no_claim_promotion():
    report = rerun_legality_after_metadata({"metadata_completed": False})
    assert report["promotes_claims"] is False


def test_runner(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r4_rerun_legality_after_metadata.run_stage12c_r3_complete_missing_metadata",
        lambda: {"metadata_completed": False},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r4_rerun_legality_after_metadata.run_stage12a_coefficient_assembly_dry_run",
        lambda: {"registry": {}},
    )

    report = run_stage12c_r4_rerun_legality_after_metadata()
    assert report["status"] == "rerun_legality_after_metadata"
    assert report["r_computation_allowed"] is False
