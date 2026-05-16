from grut.hard_theory.s4_ctp_solver.stage12c_r6a_source_protection_requirements import (
    run_stage12c_r6a_source_protection_requirements,
)


def _registry(source_partitions):
    return {
        "candidate_buckets": {
            "c_final_candidate": {
                "candidate_id": "c_final_candidate_v1",
                "source_partitions": source_partitions,
            }
        }
    }


def _stage11e_with_sources(records):
    return {"attempts": {"results": records}}


def test_requirements_report_for_each_source(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r6a_source_protection_requirements.run_stage12c_r5_protected_source_audit",
        lambda: {
            "disqualifying_sources": [
                {"partition_id": "p1"},
                {"partition_id": "p2"},
            ],
            "c_final_reclassification_eligible": False,
        },
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r6a_source_protection_requirements.run_stage10d_integrand_partition_map",
        lambda: {"partitions": [{"partition_id": "p1"}, {"partition_id": "p2"}]},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r6a_source_protection_requirements.run_stage11e_cross_partition_finite_consistency",
        lambda: _stage11e_with_sources(
            [
                {"partition_id": "p1", "locality_class": "local"},
                {"partition_id": "p2", "locality_class": "local"},
            ]
        ),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r6a_source_protection_requirements.run_stage12a_coefficient_assembly_dry_run",
        lambda: {"registry": _registry(["p1", "p2"])},
    )

    report = run_stage12c_r6a_source_protection_requirements()
    assert report["sources_examined"] == 2
    assert len(report["sources"]) == 2
    assert report["c_final_reclassification_allowed"] is False


def test_no_source_reclassified_and_r_blocked(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r6a_source_protection_requirements.run_stage12c_r5_protected_source_audit",
        lambda: {"disqualifying_sources": [{"partition_id": "p1"}]},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r6a_source_protection_requirements.run_stage10d_integrand_partition_map",
        lambda: {"partitions": [{"partition_id": "p1"}]},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r6a_source_protection_requirements.run_stage11e_cross_partition_finite_consistency",
        lambda: _stage11e_with_sources(
            [
                {
                    "partition_id": "p1",
                    "locality_class": "local",
                    "protection_class": "local",
                    "invariant_class": "scheme_fragile",
                }
            ]
        ),
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage12c_r6a_source_protection_requirements.run_stage12a_coefficient_assembly_dry_run",
        lambda: {"registry": _registry(["p1"])},
    )

    report = run_stage12c_r6a_source_protection_requirements()
    assert report["r_computation_allowed"] is False
    assert report["promotes_claims"] is False
    assert report["c_final_reclassification_allowed"] is False

    for source in report["sources"]:
        assert source["can_be_reclassified_now"] is False
        assert source["promotes_claims"] is False
