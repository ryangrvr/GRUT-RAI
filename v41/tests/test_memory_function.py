"""GRUT-RAI v4.1 — tests for TARGET 1 (K̃(ω) reduction). Proves the machinery is
real (matches the analytic anchor), that the verdict is a functional of J(ω), and
that deriving τ_K from GRUT's actual content RAISES (J(ω) unspecified) — i.e. the
module does not launder a number the way v4 did.
"""
from __future__ import annotations

import numpy as np
import pytest

from v41.targets import memory_function as mf


def test_ohmic_drude_matches_analytic_kernel():
    """γ(t) for Ohmic–Drude J = ηω/(1+(ω/Ωc)²) must equal ηΩc·e^{−Ωc t}."""
    eta, Oc = 1.0, 1.0
    t = np.linspace(0, 6, 40)
    num = mf.memory_kernel_from_J(mf.ohmic_drude_J(eta, Oc), t, wmax=200.0)
    ana = eta * Oc * np.exp(-Oc * t)
    assert np.max(np.abs(num - ana) / (ana + 1e-12)) < 0.02


def test_tauK_is_inverse_cutoff():
    """τ_K = 1/Ω_c for the Ohmic–Drude bath (the verified anchor)."""
    for Oc in (0.5, 2.0, 10.0):
        tauK = mf.tau_K_from_J(mf.ohmic_drude_J(Omega_c=Oc), omega_scale=Oc)
        assert abs(tauK - 1.0 / Oc) / (1.0 / Oc) < 0.10


def test_verdict_flips_with_bath_bandwidth():
    """The decider is J(ω)'s low-frequency weight: broadband ⇒ fast, narrowband ⇒ slow.
    Same machinery, opposite verdicts — so J(ω) is genuinely decisive (and unspecified)."""
    tau0 = 1.0
    fast = mf.tau_K_from_J(mf.ohmic_drude_J(Omega_c=100.0), omega_scale=100.0)
    slow = mf.tau_K_from_J(mf.ohmic_drude_J(Omega_c=0.1), omega_scale=0.1)
    assert "FAST" in mf.verdict(fast, tau0)
    assert "SLOW" in mf.verdict(slow, tau0)


def test_grut_bath_raises_not_launders():
    """Deriving τ_K from GRUT's actual content must RAISE (J(ω) unspecified), never
    return a number — the anti-circularity rule."""
    with pytest.raises(NotImplementedError):
        mf.grut_bath_spectral_density()
    with pytest.raises(NotImplementedError):
        mf.compute_tauK_from_bath()
