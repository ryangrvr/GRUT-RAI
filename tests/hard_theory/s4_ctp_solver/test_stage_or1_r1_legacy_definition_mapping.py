from grut.hard_theory.s4_ctp_solver.stage_or1_r1_legacy_definition_mapping import (
    run_stage_or1_r1_legacy_definition_mapping,
)


def _registered_candidate(source_type: str, kernel_id: str, coefficient_value=None) -> dict:
    return {
        "protected_source_candidate_id": f"protected_{source_type}_candidate",
        "source_type": source_type,
        "kernel_id": kernel_id,
        "nonlocal_form_present": True,
        "counterterm_nonmixing_verified": True,
        "finite_extractability": True,
        "coefficient_value": coefficient_value,
    }


def _stage_p7_report(candidates):
    return {
        "scheme_protected_candidates": [
            {"candidate_id": entry["protected_source_candidate_id"], "classification": "scheme_protected"}
            for entry in candidates
        ],
        "stage_p6": {"registered_candidates": candidates},
    }


def _definition_history(definitions):
    return {
        "r_definition_found": True,
        "definition_status": "ok",
        "definitions": definitions,
        "r_definition_source": "unit_test",
    }


def _legacy_definition(numerator_role: str, denominator_role: str, text: str):
    return {
        "definition_id": f"legacy_{numerator_role}_over_{denominator_role}",
        "definition_text": text,
        "numerator_role": numerator_role,
        "denominator_role": denominator_role,
        "signed": False,
        "source_refs": ["unit_test"],
    }


def _install_common(monkeypatch, stage_p7_report, definition_history):
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or1_r1_legacy_definition_mapping.run_stage_or1_resolve_r_route",
        lambda: {"stage": "OR1"},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or1_r1_legacy_definition_mapping.build_r_definition_history",
        lambda: definition_history,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or1_r1_legacy_definition_mapping.run_stage12a_coefficient_assembly_dry_run",
        lambda: {"registry": {"candidate_buckets": {}}},
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or1_r1_legacy_definition_mapping.run_stage_p7_protected_scheme_injection",
        lambda: stage_p7_report,
    )
    monkeypatch.setattr(
        "grut.hard_theory.s4_ctp_solver.stage_or1_r1_legacy_definition_mapping.run_stage_p11_r2_equivalence_refresh",
        lambda: {"equivalence_classes": []},
    )


def test_blocks_c_cosmo_without_kernel(monkeypatch):
    candidates = [
        _registered_candidate("R_log_box_R", "r_log"),
        _registered_candidate("Weyl_log_box_Weyl", "w_log"),
    ]
    stage_p7_report = _stage_p7_report(candidates)
    definition_history = _definition_history(
        [_legacy_definition("C_Cosmo", "C_Final", "C_Cosmo / C_Final")]
    )

    _install_common(monkeypatch, stage_p7_report, definition_history)

    report = run_stage_or1_r1_legacy_definition_mapping()
    assert report["mapping_complete"] is False
    assert any(
        entry.get("blocking_reason") == "c_cosmo_mapping_missing"
        for entry in report["blocked_routes"]
    )


def test_maps_c_final_only_to_allowed_kernels(monkeypatch):
    candidates = [
        _registered_candidate("Im_log_minus_box_i_epsilon", "im_log"),
        _registered_candidate("R_log_box_R", "r_log"),
        _registered_candidate("Weyl_log_box_Weyl", "w_log"),
    ]
    stage_p7_report = _stage_p7_report(candidates)
    definition_history = _definition_history(
        [_legacy_definition("C_Final", "C_Cosmo", "C_Final / C_Cosmo")]
    )

    _install_common(monkeypatch, stage_p7_report, definition_history)
    report = run_stage_or1_r1_legacy_definition_mapping()

    role_assignments = report["role_assignments"]
    c_final_sources = {entry.get("source_type") for entry in role_assignments["c_final_candidates"]}
    assert "R_log_box_R" in c_final_sources
    assert "Weyl_log_box_Weyl" in c_final_sources
    assert "Im_log_minus_box_i_epsilon" not in c_final_sources


def test_im_log_not_mapped_to_c_final(monkeypatch):
    candidates = [_registered_candidate("Im_log_minus_box_i_epsilon", "im_log")]
    stage_p7_report = _stage_p7_report(candidates)
    definition_history = _definition_history(
        [_legacy_definition("C_Final", "C_Cosmo", "C_Final / C_Cosmo")]
    )

    _install_common(monkeypatch, stage_p7_report, definition_history)
    report = run_stage_or1_r1_legacy_definition_mapping()
    assert report["role_assignments"]["c_final_candidates"] == []


def test_no_manual_selection_or_claims(monkeypatch):
    candidates = [_registered_candidate("R_log_box_R", "r_log")]
    stage_p7_report = _stage_p7_report(candidates)
    definition_history = _definition_history(
        [_legacy_definition("C_Final", "C_Cosmo", "C_Final / C_Cosmo")]
    )

    _install_common(monkeypatch, stage_p7_report, definition_history)
    report = run_stage_or1_r1_legacy_definition_mapping()

    assert report["unique_route_selected"] is False
    assert report["can_compute_numeric_r"] is False
    assert report["can_claim_r"] is False
    assert report["promotes_claims"] is False
    assert report["audit"]["status"] == "pass"
