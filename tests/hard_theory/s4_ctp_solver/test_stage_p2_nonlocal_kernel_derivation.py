from grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_kernel_derivation import (
    run_stage_p2_nonlocal_kernel_derivation,
)


def test_targets_defined():
    report = run_stage_p2_nonlocal_kernel_derivation()
    assert report["kernels_attempted"] > 0


def test_scaffold_only_targets_do_not_pass(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_kernel_derivation.run_stageN2_imaginary_causal_sector_audit",
        lambda: {
            "candidate_sources": [
                {
                    "term": "Im log(-Box - i epsilon)",
                    "scaffold_only": True,
                    "indicators": {"imaginary_log": True, "keldysh_ctp": True},
                }
            ]
        },
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_kernel_derivation.run_stage9c_regularized_integrand",
        lambda: {"regularization_attached": True},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_kernel_derivation.run_stage11b_subtraction_dry_run",
        lambda: {"regulator_removed": False},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_kernel_derivation.run_stage12g_r_route_terminal_audit",
        lambda: {"terminal_package": {}},
    )

    report = run_stage_p2_nonlocal_kernel_derivation()
    assert report["protected_source_derived"] is False


def test_missing_regulator_fails(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_kernel_derivation.run_stage9c_regularized_integrand",
        lambda: {},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_kernel_derivation.run_stage11b_subtraction_dry_run",
        lambda: {},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_kernel_derivation.run_stageN2_imaginary_causal_sector_audit",
        lambda: {"candidate_sources": []},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_kernel_derivation.run_stage12g_r_route_terminal_audit",
        lambda: {"terminal_package": {}},
    )

    report = run_stage_p2_nonlocal_kernel_derivation()
    assert report["failed_kernels"]
    for entry in report["failed_kernels"]:
        assert entry["regulator_check"]["status"] == "fail"


def test_missing_ward_ctp_fails(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_kernel_derivation.run_stageN2_imaginary_causal_sector_audit",
        lambda: {"candidate_sources": []},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_kernel_derivation.run_stage9c_regularized_integrand",
        lambda: {"regularization_attached": True},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_kernel_derivation.run_stage11b_subtraction_dry_run",
        lambda: {"regulator_removed": False},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_kernel_derivation.run_stage12g_r_route_terminal_audit",
        lambda: {},
    )

    report = run_stage_p2_nonlocal_kernel_derivation()
    assert report["failed_kernels"]
    for entry in report["failed_kernels"]:
        assert entry["ward_ctp_check"]["status"] == "fail"


def test_acceptance_requires_all_conditions(monkeypatch):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_kernel_derivation.run_stageN2_imaginary_causal_sector_audit",
        lambda: {
            "candidate_sources": [
                {
                    "term": "Im log(-Box - i epsilon)",
                    "scaffold_only": False,
                    "indicators": {"imaginary_log": True, "keldysh_ctp": True},
                }
            ]
        },
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_kernel_derivation.run_stage9c_regularized_integrand",
        lambda: {"regularization_attached": True},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_kernel_derivation.run_stage11b_subtraction_dry_run",
        lambda: {"regulator_removed": False},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p2_nonlocal_kernel_derivation.run_stage12g_r_route_terminal_audit",
        lambda: {"terminal_package": {}},
    )

    report = run_stage_p2_nonlocal_kernel_derivation()
    assert report["protected_source_derived"] is False


def test_no_r_or_claims():
    report = run_stage_p2_nonlocal_kernel_derivation()
    assert report["r_computation_allowed"] is False
    assert report["promotes_claims"] is False
