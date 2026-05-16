from pathlib import Path

import sympy as sp

from grut.hard_theory.s4_ctp_solver.gate3_mathematica_import import (
    import_mathematica_coefficient,
)


_FIX = Path(__file__).resolve().parents[2] / "fixtures" / "gate3"


def test_blocked_fixture_imports_as_blocked() -> None:
    out = import_mathematica_coefficient(str(_FIX / "blocked_cosmo.json"))
    assert out["accepted"] is True
    assert out["result"].status == "blocked"
    assert out["result"].value is None


def test_valid_computed_fixture_imports() -> None:
    out = import_mathematica_coefficient(str(_FIX / "computed_cosmo_valid.json"))
    assert out["accepted"] is True
    assert out["result"].status == "computed"
    assert out["result"].finite_part is not None
    assert out["result"].finite_part == sp.Rational(28857, 25000)


def test_unresolved_computed_fixture_rejected() -> None:
    out = import_mathematica_coefficient(str(_FIX / "invalid_unresolved_computed.json"))
    assert out["accepted"] is False
    assert "computed_value_not_resolved_scalar" in out["errors"]
    assert "computed_finite_part_not_resolved_scalar" in out["errors"]


def test_missing_scheme_rejected() -> None:
    out = import_mathematica_coefficient(str(_FIX / "invalid_missing_scheme.json"))
    assert out["accepted"] is False
    assert "missing_scheme" in out["errors"]


def test_non_euler_channel_rejected() -> None:
    out = import_mathematica_coefficient(str(_FIX / "invalid_non_euler_channel.json"))
    assert out["accepted"] is False
    assert "non_euler_channel" in out["errors"]


def test_manual_target_matching_rejected() -> None:
    out = import_mathematica_coefficient(str(_FIX / "invalid_manual_target_matching.json"))
    assert out["accepted"] is False
    assert "manual_target_matching_true" in out["errors"]


def test_unprotected_rejected() -> None:
    out = import_mathematica_coefficient(str(_FIX / "invalid_unprotected.json"))
    assert out["accepted"] is False
    assert "unprotected_coefficient" in out["errors"]
