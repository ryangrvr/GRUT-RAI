"""GRUT-RAI v4.1 — tests for TARGET 1B (bath_spectrum.py). These encode the results that
SURVIVED the adversarial panel: the verdict is set by the IR exponent (scale separation is
shape-dependent, NOT a one-sided 'fast' bound); the discrete dark relic is FDT-forbidden;
and the action's missing object (the IR exponent s) RAISES rather than being assumed.
"""
from __future__ import annotations

import numpy as np
import pytest

from v4.targets import bath_spectrum as bs
from v4.targets import memory_function as mf


def test_ir_exponent_decides_not_scale_separation():
    """Same micro-scale UV cutoff, opposite verdicts: Ohmic-or-stiffer (s≥1) FAST, sub-Ohmic
    (s<1) SLOW. This is the refutation of 'scale separation ⇒ fast' (panel C1)."""
    rows = {r["s"]: r for r in bs.ir_exponent_decides()}
    assert "FAST" in rows[3.0]["verdict"] and "FAST" in rows[1.0]["verdict"]
    assert "SLOW" in rows[0.5]["verdict"] and "SLOW" in rows[0.0]["verdict"] and "SLOW" in rows[-0.5]["verdict"]
    # the s>=1 tails are negligible; the s<1 tails carry real weight at 50 tau0
    assert rows[1.0]["tail_residual_at_50tau0"] < bs.FAST_RESIDUAL_TOL
    assert rows[0.0]["tail_residual_at_50tau0"] > 0.5


def test_subohmic_slow_is_window_robust():
    """A sub-Ohmic bath (s=0.5) is SLOW by the residual discriminant on ANY reasonable window
    — a property of J. The 1/e time, by contrast, is window-dependent here (inf vs ~0.09), which
    is precisely why the verdict is read from the residual, not the 1/e metric (panel C1/C2)."""
    J = bs.power_law_bath(0.5, 100.0)
    r50 = bs.tail_residual(J, 1.0, wmax=800.0, tmax_over_t0=50.0)
    r100 = bs.tail_residual(J, 1.0, wmax=800.0, tmax_over_t0=100.0)
    assert r50 > bs.FAST_RESIDUAL_TOL and r100 > bs.FAST_RESIDUAL_TOL   # SLOW on both windows


def test_tauK_functional_is_scale_independent():
    """tau_K_functional is a property of J alone (fixed tau0-referenced window), unlike the
    fragile tau_K_from_J whose verdict depends on the asserted omega_scale (panel C1 bug)."""
    J = mf.ohmic_drude_J(Omega_c=1.0)
    a = mf.tau_K_functional(J, t0=1.0, wmax=400.0, tmax_over_t0=12.0, nw=40000, nt=1500)
    b = mf.tau_K_functional(J, t0=1.0, wmax=800.0, tmax_over_t0=12.0, nw=60000, nt=1500)  # different grid, same J
    assert abs(a - b) / a < 0.05
    # the fragile estimator, by contrast, flips with the asserted scale
    hi = mf.tau_K_from_J(J, omega_scale=100.0)
    lo = mf.tau_K_from_J(J, omega_scale=1.0)
    assert (hi < 0.25) and (lo > 0.25)             # same bath, FAST then SLOW → demonstrably fragile


def test_critical_damping_at_quarter():
    """tau_K = tau0/4 is the overdamped→underdamped boundary of the single-channel chi_mem
    (Q=1/2). Conditional on that ansatz (panel C2), but exact within it."""
    rows = {r["tauK_over_tau0"]: r for r in bs.critical_damping_point()}
    assert rows[0.24]["max_abs_re_pole"] < 1e-9    # overdamped just below
    assert rows[0.26]["max_abs_re_pole"] > 1e-3    # rings just above
    assert abs(rows[0.25]["Q"] - 0.5) < 1e-9       # tau0/4 ⇔ Q=1/2


def test_fdt_positivity_forbids_relic():
    """Im chi_mem(w>0) ≥ 0 (passive) only for tau_K ≤ tau0; a relic-grade Q≥5 (tau_K≳25 tau0)
    is FDT-non-passive — a second, independent gate on the slow case (panel C4 bonus)."""
    rows = {r["tauK_over_tau0"]: r for r in bs.fdt_gate()}
    assert rows[0.5]["passive"] and rows[1.0]["passive"]
    assert not rows[1.1]["passive"] and not rows[25.0]["passive"]
    assert abs(rows[25.0]["Q"] - 5.0) < 1e-9       # the relic threshold sits deep in non-passive


def test_threshold_far_above_hubble():
    """The verdict threshold 4/tau0 sits ~10^3 above the Hubble frequency, so curved-space
    effects (which live at ~H0) do not naturally deposit weight there (panel C3)."""
    h = bs.threshold_vs_hubble()
    assert 300 < h["inv_tau0_over_H0"] < 400
    assert h["threshold_4_over_tau0_over_H0"] > 1000


def test_grut_ir_tail_raises_not_assumes():
    """The action's missing object (the IR exponent s) RAISES — it is not assumed. The
    anti-circularity rule, one level deeper than Target 1."""
    with pytest.raises(NotImplementedError):
        bs.grut_ir_tail()
