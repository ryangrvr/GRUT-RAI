from grut.hard_theory.s4_ctp_solver.stage_or6_symbolic_euler_extraction import (
    run_stage_or6_symbolic_euler_extraction,
)


def _binding(role_id, source_type, status="bound"):
    return {
        "role_id": role_id,
        "source_type": source_type,
        "kernel_id": source_type,
        "coefficient_symbol": "C_Euler_num" if role_id == "euler_numerator" else "C_Euler_den",
        "coefficient_value": None,
        "status": status,
        "blocking_reason": None,
        "promotes_claims": False,
    }


def _or4_report(stage_p7):
    return {
        "definition_domain": "round_s4_euler_anomaly_channel",
        "allowed_kernel_roles": [{"source_type": "R_log_box_R"}],
        "blocked_kernel_roles": [
            {"source_type": "Weyl_log_box_Weyl"},
            {"source_type": "Im_log_minus_box_i_epsilon"},
        ],
        "stage_or3": {"euler_channel_available": True},
        "stage_p7": stage_p7,
    }


def _stage_p7(protected=True):
    registered = [
        {
            "protected_source_candidate_id": "protected_R_log_box_R_candidate",
            "source_type": "R_log_box_R",
        }
    ]
    return {
        "scheme_protected_candidates": (
            [{"candidate_id": "protected_R_log_box_R_candidate"}] if protected else []
        ),
        "stage_p6": {"registered_candidates": registered},
    }


def _stage_p11_r2(regulator_class="matched_dimensional_symbolic_preserved"):
    return {
        "refreshed_ratios": [
            {
                "pair": {
                    "left": {"source_type": "R_log_box_R"},
                    "right": {"source_type": "R_log_box_R"},
                },
                "ratio_regulator_class": regulator_class,
            }
        ]
    }


def _install_common(
    monkeypatch,
    or4_report,
    or5_report,
    stage_p7,
    stage_p8,
    stage_p11_r2,
    or3_report=None,
):
    cached_or5 = {
        **or5_report,
        "stage_or4": or4_report,
        "stage_or3": or3_report or {"euler_channel_available": True},
        "stage_p7": stage_p7,
        "stage_p8": stage_p8,
        "stage_p11_r2": stage_p11_r2,
        "stage12b": {"stage": "12B"},
    }

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or6_symbolic_euler_extraction.run_stage_or5_euler_coefficient_symbol_binding",
        lambda: cached_or5,
    )


def test_symbolic_quotient_created(monkeypatch):
    stage_p7 = _stage_p7()
    or4_report = _or4_report(stage_p7)
    or5_report = {
        "bindings": [
            _binding("euler_numerator", "R_log_box_R"),
            _binding("euler_denominator", "R_log_box_R"),
        ]
    }
    stage_p8 = {"r_legal": True}
    stage_p11_r2 = _stage_p11_r2()

    _install_common(monkeypatch, or4_report, or5_report, stage_p7, stage_p8, stage_p11_r2)
    report = run_stage_or6_symbolic_euler_extraction(use_cached=True)

    assert report["symbolic_extraction_complete"] is True
    assert report["symbolic_ratio"]["symbolic_ratio_id"] == "R_Euler_symbolic"
    assert report["symbolic_ratio"]["numeric_value"] is None


def test_euler_only_route_enforced(monkeypatch):
    stage_p7 = _stage_p7()
    or4_report = _or4_report(stage_p7)
    or4_report["allowed_kernel_roles"] = []
    or5_report = {
        "bindings": [
            _binding("euler_numerator", "R_log_box_R"),
            _binding("euler_denominator", "R_log_box_R"),
        ]
    }
    stage_p8 = {"r_legal": True}
    stage_p11_r2 = _stage_p11_r2()

    _install_common(monkeypatch, or4_report, or5_report, stage_p7, stage_p8, stage_p11_r2)
    report = run_stage_or6_symbolic_euler_extraction(use_cached=True)

    assert report["projection_guard_passed"] is False
    assert report["symbolic_ratio"] is None


def test_weyl_rejected(monkeypatch):
    stage_p7 = _stage_p7()
    or4_report = _or4_report(stage_p7)
    or5_report = {
        "bindings": [
            _binding("euler_numerator", "R_log_box_R"),
            _binding("euler_denominator", "R_log_box_R"),
            _binding("disallowed_candidate", "Weyl_log_box_Weyl", status="blocked"),
        ]
    }
    stage_p8 = {"r_legal": True}
    stage_p11_r2 = _stage_p11_r2()

    _install_common(monkeypatch, or4_report, or5_report, stage_p7, stage_p8, stage_p11_r2)
    report = run_stage_or6_symbolic_euler_extraction(use_cached=True)

    assert report["scheme_guard_passed"] is False
    assert report["symbolic_ratio"] is None


def test_im_log_rejected(monkeypatch):
    stage_p7 = _stage_p7()
    or4_report = _or4_report(stage_p7)
    or5_report = {
        "bindings": [
            _binding("euler_numerator", "R_log_box_R"),
            _binding("euler_denominator", "R_log_box_R"),
            _binding("disallowed_candidate", "Im_log_minus_box_i_epsilon", status="blocked"),
        ]
    }
    stage_p8 = {"r_legal": True}
    stage_p11_r2 = _stage_p11_r2()

    _install_common(monkeypatch, or4_report, or5_report, stage_p7, stage_p8, stage_p11_r2)
    report = run_stage_or6_symbolic_euler_extraction(use_cached=True)

    assert report["scheme_guard_passed"] is False
    assert report["symbolic_ratio"] is None


def test_scheme_protection_required(monkeypatch):
    stage_p7 = _stage_p7(protected=False)
    or4_report = _or4_report(stage_p7)
    or5_report = {
        "bindings": [
            _binding("euler_numerator", "R_log_box_R"),
            _binding("euler_denominator", "R_log_box_R"),
        ]
    }
    stage_p8 = {"r_legal": True}
    stage_p11_r2 = _stage_p11_r2()

    _install_common(monkeypatch, or4_report, or5_report, stage_p7, stage_p8, stage_p11_r2)
    report = run_stage_or6_symbolic_euler_extraction(use_cached=True)

    assert report["scheme_guard_passed"] is False


def test_regulator_alignment_required(monkeypatch):
    stage_p7 = _stage_p7()
    or4_report = _or4_report(stage_p7)
    or5_report = {
        "bindings": [
            _binding("euler_numerator", "R_log_box_R"),
            _binding("euler_denominator", "R_log_box_R"),
        ]
    }
    stage_p8 = {"r_legal": True}
    stage_p11_r2 = _stage_p11_r2("regulator_mismatch_or_unresolved")

    _install_common(monkeypatch, or4_report, or5_report, stage_p7, stage_p8, stage_p11_r2)
    report = run_stage_or6_symbolic_euler_extraction(use_cached=True)

    assert report["scheme_guard_passed"] is False


def test_projection_alignment_required(monkeypatch):
    stage_p7 = _stage_p7()
    or4_report = _or4_report(stage_p7)
    or4_report["definition_domain"] = "invalid_domain"
    or5_report = {
        "bindings": [
            _binding("euler_numerator", "R_log_box_R"),
            _binding("euler_denominator", "R_log_box_R"),
        ]
    }
    stage_p8 = {"r_legal": True}
    stage_p11_r2 = _stage_p11_r2()

    _install_common(monkeypatch, or4_report, or5_report, stage_p7, stage_p8, stage_p11_r2)
    report = run_stage_or6_symbolic_euler_extraction(use_cached=True)


def test_cached_mode_skips_heavy_stages(monkeypatch):
    stage_p7 = _stage_p7()
    or4_report = _or4_report(stage_p7)
    or5_report = {
        "bindings": [
            _binding("euler_numerator", "R_log_box_R"),
            _binding("euler_denominator", "R_log_box_R"),
        ]
    }
    stage_p8 = {"r_legal": True}
    stage_p11_r2 = _stage_p11_r2()

    _install_common(monkeypatch, or4_report, or5_report, stage_p7, stage_p8, stage_p11_r2)

    def _unexpected_call():
        raise AssertionError("heavy stage called in cached mode")

    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or6_symbolic_euler_extraction.run_stage_p7_protected_scheme_injection",
        _unexpected_call,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or6_symbolic_euler_extraction.run_stage_p8_r_legality_with_protected_kernels",
        _unexpected_call,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or6_symbolic_euler_extraction.run_stage_p11_r2_equivalence_refresh",
        _unexpected_call,
    )

    report = run_stage_or6_symbolic_euler_extraction(use_cached=True)
    assert report["symbolic_extraction_complete"] is True

    # In cached mode with valid OR4 configuration, projection guard passes
    assert report["projection_guard_passed"] is True


def test_no_numeric_r_or_claims(monkeypatch):
    stage_p7 = _stage_p7()
    or4_report = _or4_report(stage_p7)
    or5_report = {
        "bindings": [
            _binding("euler_numerator", "R_log_box_R"),
            _binding("euler_denominator", "R_log_box_R"),
        ]
    }
    stage_p8 = {"r_legal": True}
    stage_p11_r2 = _stage_p11_r2()

    _install_common(monkeypatch, or4_report, or5_report, stage_p7, stage_p8, stage_p11_r2)
    report = run_stage_or6_symbolic_euler_extraction()

    assert report["can_compute_numeric_r"] is False
    assert report["can_claim_r"] is False
    assert report["promotes_claims"] is False
