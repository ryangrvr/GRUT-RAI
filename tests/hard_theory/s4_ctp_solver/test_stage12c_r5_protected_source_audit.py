from grut.hard_theory.s4_ctp_solver.stage12c_r5_protected_source_audit import (
    run_stage12c_r5_protected_source_audit,
)


def _registry(source_partitions, regulator_status="symbolic_regulator_preserved"):
    return {
        "candidate_buckets": {
            "c_final_candidate": {
                "candidate_id": "c_final_candidate_v1",
                "source_partitions": source_partitions,
                "regulator_dependence_class": regulator_status,
            }
        }
    }


def _stage11e_with_sources(records):
    return {"attempts": {"results": records}}


def test_c_final_not_eligible_with_local_sources(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r5_protected_source_audit.run_stage12a_coefficient_assembly_dry_run",
        lambda: {"registry": _registry(["p1"])},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r5_protected_source_audit.run_stage12b_scheme_stability_audit",
        lambda: {"classifications": []},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r5_protected_source_audit.run_stage11e_cross_partition_finite_consistency",
        lambda: _stage11e_with_sources(
            [
                {
                    "partition_id": "p1",
                    "locality_class": "local",
                    "protection_class": "local",
                    "invariant_class": "scheme_fragile",
                    "regulator_dependence_class": "symbolic_regulator_preserved",
                }
            ]
        ),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r5_protected_source_audit.run_stage12c_r3_complete_missing_metadata",
        lambda: {"registry": _registry(["p1"])},
    )

    report = run_stage12c_r5_protected_source_audit()
    assert report["c_final_reclassification_eligible"] is False
    assert report["disqualifying_sources"]


def test_c_final_eligible_only_when_all_sources_protected(monkeypatch):
    records = [
        {
            "partition_id": "p1",
            "locality_class": "nonlocal",
            "protection_class": "anomaly_protected",
            "invariant_class": "scheme_protected",
            "regulator_dependence_class": "symbolic_regulator_preserved",
        },
        {
            "partition_id": "p2",
            "locality_class": "nonlocal",
            "protection_class": "anomaly_protected",
            "invariant_class": "scheme_protected",
            "regulator_dependence_class": "symbolic_regulator_preserved",
        },
    ]

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r5_protected_source_audit.run_stage12a_coefficient_assembly_dry_run",
        lambda: {"registry": _registry(["p1", "p2"])},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r5_protected_source_audit.run_stage12b_scheme_stability_audit",
        lambda: {"classifications": []},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r5_protected_source_audit.run_stage11e_cross_partition_finite_consistency",
        lambda: _stage11e_with_sources(records),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r5_protected_source_audit.run_stage12c_r3_complete_missing_metadata",
        lambda: {"registry": _registry(["p1", "p2"])},
    )

    report = run_stage12c_r5_protected_source_audit()
    assert report["c_final_reclassification_eligible"] is True
    assert report["disqualifying_sources"] == []


def test_no_r_computation_or_claim_promotion(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r5_protected_source_audit.run_stage12a_coefficient_assembly_dry_run",
        lambda: {"registry": _registry([])},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r5_protected_source_audit.run_stage12b_scheme_stability_audit",
        lambda: {"classifications": []},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r5_protected_source_audit.run_stage11e_cross_partition_finite_consistency",
        lambda: _stage11e_with_sources([]),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r5_protected_source_audit.run_stage12c_r3_complete_missing_metadata",
        lambda: {"registry": _registry([])},
    )

    report = run_stage12c_r5_protected_source_audit()
    assert report["r_computation_allowed"] is False
    assert report["promotes_claims"] is False
