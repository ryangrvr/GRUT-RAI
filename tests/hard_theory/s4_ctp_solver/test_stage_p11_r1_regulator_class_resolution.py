from grut.hard_theory.s4_ctp_solver.stage_p11_r1_regulator_class_resolution import (
    run_stage_p11_r1_regulator_class_resolution,
)


def _p7_report(registered_candidates):
    return {"stage_p6": {"registered_candidates": registered_candidates}}


def _p9_report(entries):
    return {"symbolic_candidates": entries, "blocked_pairs": []}


def _stage9c(default_regulator=None, scheme_id=None):
    return {
        "scheme": {
            "default_regulator": default_regulator,
            "scheme_id": scheme_id,
        }
    }


def _stage10f(regulator_present=True, regulator_removed=False):
    return {
        "collected": {
            "collected_attempts": [
                {"regulator_present": regulator_present},
            ]
        },
        "regulator_check": {
            "regulator_removed": regulator_removed,
        },
    }


def _pair(left_overrides=None, right_overrides=None):
    left = {
        "candidate_id": "protected_Im_log_minus_box_i_epsilon_candidate",
        "source_type": "Im_log_minus_box_i_epsilon",
        "coefficient_value": None,
    }
    right = {
        "candidate_id": "protected_R_log_box_R_candidate",
        "source_type": "R_log_box_R",
        "coefficient_value": None,
    }
    if left_overrides:
        left.update(left_overrides)
    if right_overrides:
        right.update(right_overrides)
    return {"pair_id": "pair_a", "left": left, "right": right}


def _symbolic_entry(pair, extra=None):
    entry = {
        "pair": pair,
        "symbolic_r": {"symbolic_ratio": "R_symbolic_protected"},
        "promotes_claims": False,
    }
    if extra:
        entry.update(extra)
    return entry


def _install(monkeypatch, stage_p7, stage_p9, stage9c, stage10f):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p11_r1_regulator_class_resolution.run_stage_p7_protected_scheme_injection",
        lambda: stage_p7,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p11_r1_regulator_class_resolution.run_stage_p8_r_legality_with_protected_kernels",
        lambda: {"valid_pairs": []},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p11_r1_regulator_class_resolution.run_stage_p9_controlled_symbolic_r_attempt",
        lambda: stage_p9,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p11_r1_regulator_class_resolution.run_stage_p10_symbolic_ratio_classification",
        lambda: {"status": "symbolic_ratio_classification"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p11_r1_regulator_class_resolution.run_stage9c_regularized_integrand",
        lambda: stage9c,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_p11_r1_regulator_class_resolution.run_stage10f_partition_consistency_audit",
        lambda: stage10f,
    )


def test_assigns_dimensional_symbolic_class(monkeypatch):
    registered = [
        {
            "protected_source_candidate_id": "protected_Im_log_minus_box_i_epsilon_candidate",
            "source_type": "Im_log_minus_box_i_epsilon",
            "kernel_id": "Im_log_minus_box_i_epsilon_kernel",
        },
        {
            "protected_source_candidate_id": "protected_R_log_box_R_candidate",
            "source_type": "R_log_box_R",
            "kernel_id": "R_log_box_R_kernel",
        },
    ]
    pair = _pair()
    entry = _symbolic_entry(pair)

    _install(
        monkeypatch,
        _p7_report(registered),
        _p9_report([entry]),
        _stage9c("dimensional_regularization_placeholder", "integrand_regularization_v1"),
        _stage10f(regulator_present=True, regulator_removed=False),
    )

    report = run_stage_p11_r1_regulator_class_resolution()
    assert report["regulator_classes_resolved"] is True
    assert report["ratio_regulator_classes"][0]["ratio_regulator_class"] == "matched_dimensional_symbolic_preserved"


def test_unresolved_when_metadata_missing(monkeypatch):
    registered = [
        {
            "protected_source_candidate_id": "protected_Im_log_minus_box_i_epsilon_candidate",
            "source_type": "Im_log_minus_box_i_epsilon",
            "kernel_id": "Im_log_minus_box_i_epsilon_kernel",
        }
    ]
    pair = _pair()
    entry = _symbolic_entry(pair)

    _install(
        monkeypatch,
        _p7_report(registered),
        _p9_report([entry]),
        _stage9c("dimensional_regularization_placeholder", "integrand_regularization_v1"),
        _stage10f(regulator_present=False, regulator_removed=False),
    )

    report = run_stage_p11_r1_regulator_class_resolution()
    assert report["regulator_classes_resolved"] is False
    assert report["ratio_regulator_classes"][0]["ratio_regulator_class"] == "regulator_mismatch_or_unresolved"


def test_ratio_inherits_only_when_matched(monkeypatch):
    registered = [
        {
            "protected_source_candidate_id": "protected_Im_log_minus_box_i_epsilon_candidate",
            "source_type": "Im_log_minus_box_i_epsilon",
            "kernel_id": "Im_log_minus_box_i_epsilon_kernel",
        }
    ]
    pair = _pair(right_overrides={"source_type": "Weyl_log_box_Weyl"})
    entry = _symbolic_entry(pair)

    _install(
        monkeypatch,
        _p7_report(registered),
        _p9_report([entry]),
        _stage9c("dimensional_regularization_placeholder", "integrand_regularization_v1"),
        _stage10f(regulator_present=True, regulator_removed=False),
    )

    report = run_stage_p11_r1_regulator_class_resolution()
    assert report["ratio_regulator_classes"][0]["ratio_regulator_class"] == "regulator_mismatch_or_unresolved"


def test_no_coefficient_values(monkeypatch):
    registered = [
        {
            "protected_source_candidate_id": "protected_Im_log_minus_box_i_epsilon_candidate",
            "source_type": "Im_log_minus_box_i_epsilon",
            "kernel_id": "Im_log_minus_box_i_epsilon_kernel",
        }
    ]
    pair = _pair(left_overrides={"coefficient_value": "bad"})
    entry = _symbolic_entry(pair)

    _install(
        monkeypatch,
        _p7_report(registered),
        _p9_report([entry]),
        _stage9c("dimensional_regularization_placeholder", "integrand_regularization_v1"),
        _stage10f(regulator_present=True, regulator_removed=False),
    )

    report = run_stage_p11_r1_regulator_class_resolution()
    assert report["regulator_classes_resolved"] is False
    assert report["audit"]["status"] == "invalid"


def test_no_numeric_r_or_claims(monkeypatch):
    registered = [
        {
            "protected_source_candidate_id": "protected_Im_log_minus_box_i_epsilon_candidate",
            "source_type": "Im_log_minus_box_i_epsilon",
            "kernel_id": "Im_log_minus_box_i_epsilon_kernel",
        }
    ]
    pair = _pair()
    entry = _symbolic_entry(pair, extra={"symbolic_r": {"r_value": 1}})

    _install(
        monkeypatch,
        _p7_report(registered),
        _p9_report([entry]),
        _stage9c("dimensional_regularization_placeholder", "integrand_regularization_v1"),
        _stage10f(regulator_present=True, regulator_removed=False),
    )

    report = run_stage_p11_r1_regulator_class_resolution()
    assert report["can_compute_numeric_r"] is False
    assert report["can_claim_r"] is False
    assert report["promotes_claims"] is False
    assert report["audit"]["status"] == "invalid"
