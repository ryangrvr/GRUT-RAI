"""GRUT-RAI v4.1 — tests for TARGET 4 (power_spectrum_discriminant.py), CORRECTED after a second
adversarial pre-screen broke the first 'outward falsifier' four ways. The honest state: a POSITED
contrast real only at the endpoints, DEGENERATE with collisional spectrum width, one-sided in
falsifiability, entangled with ΛCDM — so it is OPEN, not a DERIVED falsifier. These tests pin the
degeneracy (the self-test that REFUSES to launder it) and the OPEN tier.
"""
from __future__ import annotations

import inspect
import numpy as np

from v4.targets import power_spectrum_discriminant as psd
from v4 import gate
from v4.registry import REGISTRY


def test_endpoint_contrast_is_real_only_at_extremes():
    """At the extremes the contrast holds: single-τ Maxwell breaks; a strict critical gel is flat."""
    assert psd._logslope_variation(psd._support_single_tau("collisional")) > 0.1
    assert psd._logslope_variation(psd._support_single_tau("free_streaming")) < 0.05


def test_discriminant_is_degenerate_with_spectrum_width():
    """The fatal P-C catch, banked as a self-test: a COLLISIONAL medium with a broad relaxation
    spectrum reads SCALE-FREE — so the binary discriminant is degenerate (single-τ is only the
    maximally-breaking endpoint). The 'check' here confirms the contrast is NOT robust."""
    assert psd.collisional_spectrum_variation(0) > 0.05      # single-τ breaks
    assert psd.collisional_spectrum_variation(7) < 0.05      # broad spectrum → scale-free
    assert psd.discriminant_breaks_with_spectrum_width() is True


def test_no_absolute_scale_exposed():
    """No physical scale anywhere: dimensionless k/k_star grid, no k_star attribute, no function
    ingests an observed scale (the c_s=c near-BAO value was excised, P-A)."""
    assert not hasattr(psd, "k_star") and not hasattr(psd, "K_STAR")
    assert np.isclose(np.median(np.log10(psd._K)), 0.0, atol=0.2)
    for _, fn in inspect.getmembers(psd, inspect.isfunction):
        params = " ".join(inspect.signature(fn).parameters).lower()
        assert not any(s in params for s in ("observed", "bao", "k_eq", "data"))


def test_branch_test_is_open_not_a_falsifier():
    """power_spectrum_branch_test is OPEN (demoted from a premature DERIVED), and its target names
    the (a)–(d) computations that would make it a real two-sided, ΛCDM-separable falsifier."""
    c = REGISTRY["power_spectrum_branch_test"]
    assert c.tier == gate.Tier.OPEN and c.check is None
    assert all(s in c.target for s in ("(a)", "(b)", "(c)", "(d)"))
    assert gate.validate(REGISTRY) == []
