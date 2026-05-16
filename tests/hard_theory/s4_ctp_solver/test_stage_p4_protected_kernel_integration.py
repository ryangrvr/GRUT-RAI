from grut.hard_theory.s4_ctp_solver.stage_p4_protected_kernel_integration import (
    run_stage_p4_protected_kernel_integration,
)


def _p2_entry(source_type: str) -> dict:
    return {
        "source_type": source_type,
        "candidate": {
            "source_type": source_type,
            "expected_nonlocal_form": "",
            "status": "scaffold_only",
            "derivation_kind": "scaffold",
            "nonlocal_form_present": False,
            "scaffold_only": True,
            "local_counterterm_nonmixing_checked": False,
            "finite_coefficient_extractable": False,
            "promotes_claims": False,
        },
        "regulator_check": {"status": "pass"},
        "ward_ctp_check": {"status": "pass"},
        "acceptance": {"accepted": False, "failures": ["scaffold_only"]},
        "promotes_claims": False,
    }


def _p3_candidate(target: str, form: str) -> dict:
    return {
        "target": target,
        "candidate": {
            "kernel_id": f"{target}_candidate",
            "nonlocal_form": form,
            "coefficient": "symbolic_uncomputed",
            "source": "p3",
            "scaffold_only": False,
            "finite_extractability": False,
            "protected_source_claimed": False,
            "promotes_claims": False,
        },
        "validation": {"status": "pass"},
        "promotes_claims": False,
    }


def test_p4_does_not_mutate_p2(monkeypatch):
    p2_report = {
        "accepted_kernels": [],
        "failed_kernels": [_p2_entry("Im_log_minus_box_i_epsilon")],
    }
    p3_report = {"candidates_constructed": []}

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p4_protected_kernel_integration.run_stage_p2_nonlocal_kernel_derivation",
        lambda: p2_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p4_protected_kernel_integration.run_stage_p3_nonlocal_form_construction",
        lambda: p3_report,
    )

    _ = run_stage_p4_protected_kernel_integration()
    assert p2_report["failed_kernels"][0]["candidate"]["scaffold_only"] is True


def test_p3_candidates_consumed_im_log(monkeypatch):
    p2_report = {
        "accepted_kernels": [],
        "failed_kernels": [_p2_entry("Im_log_minus_box_i_epsilon")],
    }
    p3_report = {
        "candidates_constructed": [
            _p3_candidate("Im_log_minus_box_i_epsilon", "Im log(-Box - i epsilon)")
        ]
    }

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p4_protected_kernel_integration.run_stage_p2_nonlocal_kernel_derivation",
        lambda: p2_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p4_protected_kernel_integration.run_stage_p3_nonlocal_form_construction",
        lambda: p3_report,
    )

    report = run_stage_p4_protected_kernel_integration()
    integrated = report["integrated_candidates"][0]
    candidate = integrated["candidate"]
    assert candidate["status"] == "symbolic_candidate"
    assert candidate["scaffold_only"] is False
    assert candidate["coefficient"] == "symbolic_uncomputed"
    assert candidate["finite_coefficient_extractable"] is False
    failures = report["remaining_failures"][0]["failures"]
    assert "scaffold_only" not in failures
    assert "nonlocal_form_missing" not in failures
    assert "counterterm_nonmixing_unchecked" in failures
    assert "finite_extractability_unavailable" in failures


def test_r_log_weyl_candidates_symbolic(monkeypatch):
    p2_report = {
        "accepted_kernels": [],
        "failed_kernels": [
            _p2_entry("R_log_box_R"),
            _p2_entry("Weyl_log_box_Weyl"),
        ],
    }
    p3_report = {
        "candidates_constructed": [
            _p3_candidate("R_log_box_R", "R log(Box) R"),
            _p3_candidate("Weyl_log_box_Weyl", "Weyl log(Box) Weyl"),
        ]
    }

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p4_protected_kernel_integration.run_stage_p2_nonlocal_kernel_derivation",
        lambda: p2_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p4_protected_kernel_integration.run_stage_p3_nonlocal_form_construction",
        lambda: p3_report,
    )

    report = run_stage_p4_protected_kernel_integration()
    failures_by_source = {
        entry["source_type"]: entry["failures"]
        for entry in report["remaining_failures"]
    }
    assert "nonlocal_form_missing" not in failures_by_source["R_log_box_R"]
    assert "scaffold_only" not in failures_by_source["R_log_box_R"]
    assert "nonlocal_form_missing" not in failures_by_source["Weyl_log_box_Weyl"]
    assert "scaffold_only" not in failures_by_source["Weyl_log_box_Weyl"]


def test_p4_flags_no_claims(monkeypatch):
    p2_report = {
        "accepted_kernels": [],
        "failed_kernels": [_p2_entry("Im_log_minus_box_i_epsilon")],
    }
    p3_report = {
        "candidates_constructed": [
            _p3_candidate("Im_log_minus_box_i_epsilon", "Im log(-Box - i epsilon)")
        ]
    }

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p4_protected_kernel_integration.run_stage_p2_nonlocal_kernel_derivation",
        lambda: p2_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p4_protected_kernel_integration.run_stage_p3_nonlocal_form_construction",
        lambda: p3_report,
    )

    report = run_stage_p4_protected_kernel_integration()
    assert report["protected_source_derived"] is False
    assert report["r_computation_allowed"] is False
    assert report["promotes_claims"] is False
    for entry in report["integrated_candidates"]:
        assert entry["promotes_claims"] is False
        assert entry["candidate"]["promotes_claims"] is False
