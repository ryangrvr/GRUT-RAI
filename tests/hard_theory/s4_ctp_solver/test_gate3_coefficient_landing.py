from grut.hard_theory.s4_ctp_solver.gate3_coefficient_landing import (
    land_gate3_coefficients,
)
from grut.hard_theory.s4_ctp_solver.gate3_euler_coefficient_extraction import (
    EulerCoefficientResult,
)
import sympy as sp


def _blocked_euler(name: str) -> EulerCoefficientResult:
    return EulerCoefficientResult(
        coefficient_name=name,
        channel="Euler",
        value=None,
        epsilon_pole=None,
        finite_part=None,
        scheme="OR4-approved",
        regulator="D=4-2epsilon",
        protected=True,
        status="blocked",
        blocker="test",
        local_vs_nonlocal_role="protected_nonlocal_R_log_box_R",
        round_s4_projection=True,
        euler_only_condition_w2_zero=True,
        massless_or_conformal_limit="massless-minimal",
        manual_target_matched=False,
        provenance="test",
    )


def test_rejects_raw_numeric_r() -> None:
    out = land_gate3_coefficients(
        cosmo=_blocked_euler("C_Euler_cosmo"),
        final=_blocked_euler("C_Euler_final"),
        raw_r_value=1.1547,
    )
    assert out["accepted"] is False
    assert out["reason"] == "raw_hard_coded_r_rejected"


def test_rejects_missing_scheme_metadata() -> None:
    bad = EulerCoefficientResult(
        coefficient_name="C_Euler_cosmo",
        channel="Euler",
        value=None,
        epsilon_pole=None,
        finite_part=None,
        scheme="",
        regulator="D=4-2epsilon",
        protected=True,
        status="blocked",
        blocker="test",
        local_vs_nonlocal_role="protected_nonlocal_R_log_box_R",
        round_s4_projection=True,
        euler_only_condition_w2_zero=True,
        massless_or_conformal_limit="massless-minimal",
        manual_target_matched=False,
        provenance="test",
    )
    out = land_gate3_coefficients(cosmo=bad, final=_blocked_euler("C_Euler_final"))
    assert out["accepted"] is False
    assert out["reason"] == "missing_scheme_metadata"


def test_rejects_non_euler_channel() -> None:
    bad = EulerCoefficientResult(
        coefficient_name="C_Euler_cosmo",
        channel="Weyl",
        value=None,
        epsilon_pole=None,
        finite_part=None,
        scheme="OR4-approved",
        regulator="D=4-2epsilon",
        protected=False,
        status="blocked",
        blocker="test",
        local_vs_nonlocal_role="weyl_log_box_weyl",
        round_s4_projection=True,
        euler_only_condition_w2_zero=True,
        massless_or_conformal_limit="massless-minimal",
        manual_target_matched=False,
        provenance="test",
    )
    out = land_gate3_coefficients(cosmo=bad, final=_blocked_euler("C_Euler_final"))
    assert out["accepted"] is False
    assert out["reason"] == "non_euler_channel_rejected"


def test_rejects_im_log_channel_without_projection() -> None:
    bad = EulerCoefficientResult(
        coefficient_name="C_Euler_cosmo",
        channel="Im-log",
        value=None,
        epsilon_pole=None,
        finite_part=None,
        scheme="OR4-approved",
        regulator="D=4-2epsilon",
        protected=False,
        status="blocked",
        blocker="ctp projection missing",
        local_vs_nonlocal_role="im_log_causal_channel",
        round_s4_projection=False,
        euler_only_condition_w2_zero=True,
        massless_or_conformal_limit="massless-minimal",
        manual_target_matched=False,
        provenance="test",
    )
    out = land_gate3_coefficients(cosmo=bad, final=_blocked_euler("C_Euler_final"))
    assert out["accepted"] is False
    assert out["reason"] == "non_euler_channel_rejected"


def test_weyl_channel_rejected_on_round_s4() -> None:
    bad = EulerCoefficientResult(
        coefficient_name="C_Euler_final",
        channel="Weyl",
        value=None,
        epsilon_pole=None,
        finite_part=None,
        scheme="OR4-approved",
        regulator="D=4-2epsilon",
        protected=False,
        status="blocked",
        blocker="W^2=0 on round S4",
        local_vs_nonlocal_role="weyl_log_box_weyl",
        round_s4_projection=True,
        euler_only_condition_w2_zero=True,
        massless_or_conformal_limit="massless-minimal",
        manual_target_matched=False,
        provenance="test",
    )
    out = land_gate3_coefficients(cosmo=_blocked_euler("C_Euler_cosmo"), final=bad)
    assert out["accepted"] is False
    assert out["reason"] == "non_euler_channel_rejected"


def test_rejects_unresolved_computed_expression() -> None:
    bad = EulerCoefficientResult(
        coefficient_name="C_Euler_cosmo",
        channel="Euler",
        value=sp.Integral(sp.Symbol("x"), (sp.Symbol("x"), 0, 1)),
        epsilon_pole=sp.Integer(0),
        finite_part=sp.Symbol("hplus") + sp.Integer(1),
        scheme="OR4-approved",
        regulator="D=4-2epsilon",
        protected=True,
        status="computed",
        blocker=None,
        local_vs_nonlocal_role="protected_nonlocal_R_log_box_R",
        round_s4_projection=True,
        euler_only_condition_w2_zero=True,
        massless_or_conformal_limit="imported_from_mathematica",
        manual_target_matched=False,
        provenance="test",
    )
    out = land_gate3_coefficients(cosmo=bad, final=_blocked_euler("C_Euler_final"))
    assert out["accepted"] is False
    assert out["reason"] == "computed_value_not_resolved_scalar"
