from pathlib import Path

from grut.hard_theory.s4_ctp_solver.gate3_import_and_classify import (
    run_gate3_import_and_classify,
)


_FIX = Path(__file__).resolve().parents[2] / "fixtures" / "gate3"


def test_import_and_classify_blocked_when_one_blocked() -> None:
    out = run_gate3_import_and_classify(
        cosmo_json_path=str(_FIX / "blocked_cosmo.json"),
        final_json_path=str(_FIX / "computed_final_valid.json"),
    )
    assert out["classification"]["classification"] == "blocked"


def test_import_and_classify_computed_candidate_for_two_valid_with_replication() -> None:
    out = run_gate3_import_and_classify(
        cosmo_json_path=str(_FIX / "computed_cosmo_valid.json"),
        final_json_path=str(_FIX / "computed_final_valid.json"),
        replicated=True,
    )
    assert out["landing"]["accepted"] is True
    assert out["classification"]["classification"] == "computed_candidate"


def test_import_and_classify_rejects_invalid_fixture() -> None:
    out = run_gate3_import_and_classify(
        cosmo_json_path=str(_FIX / "invalid_missing_scheme.json"),
        final_json_path=str(_FIX / "computed_final_valid.json"),
    )
    assert out["landing"]["accepted"] is False
    assert out["classification"]["classification"] == "blocked"


def test_raw_target_value_allowed_only_with_full_metadata() -> None:
    # The manual-target fixture must be rejected.
    out = run_gate3_import_and_classify(
        cosmo_json_path=str(_FIX / "invalid_manual_target_matching.json"),
        final_json_path=str(_FIX / "computed_final_valid.json"),
    )
    assert out["landing"]["accepted"] is False
    assert out["classification"]["classification"] == "blocked"


def test_no_target_number_construction_path() -> None:
    out = run_gate3_import_and_classify(
        cosmo_json_path=str(_FIX / "computed_cosmo_valid.json"),
        final_json_path=str(_FIX / "computed_final_valid.json"),
        replicated=False,
    )
    # With valid coefficients but no replication, route must not auto-promote.
    assert out["classification"]["classification"] in {"needs_replication", "computed_candidate"}
    assert out["promotes_claims"] is False
