"""GRUT-RAI v4.1 — tests for TARGET 2B (carrier_identity.py): α's antecedent on two routes.
Encode the (C) result: Route 1 (linear) projects the conformal mode out; Route 2 (anomaly) a
propagating conformal carrier needs the 4th-order kinetic term that carries an Ostrogradsky
ghost (Q-forbidden) — so the anomaly PERMITS but does not FORCE; the carrier role is free data.
The value 1/3 is deliberately NOT touched here (it is banked; reaching for it would be reverse-fit).
"""
from __future__ import annotations

import pytest

from v4.targets import carrier_identity as ci


def test_route1_conformal_mode_projected_out():
    """Route 1: the TT projector annihilates the conformal (trace) and longitudinal modes,
    while a spin-2 mode survives ⇒ the linear carrier is spin-2, not the conformal mode."""
    r = ci.conformal_mode_projected_out()
    assert r["conformal_trace_norm"] < 1e-12
    assert r["longitudinal_norm"] < 1e-12
    assert r["spin2_survives_norm"] > 0.1


def test_route2_propagating_carrier_carries_ghost():
    """Route 2: the 4th-order Riegert propagator has a healthy pole AND a ghost pole (opposite
    residues) ⇒ a propagating conformal carrier is Ostrogradsky-ghostly ⇒ Q-forbidden."""
    res = ci.riegert_propagator_residues(M2=2.0)
    assert res["healthy_pole_residue"] > 0
    assert res["ghost_pole_residue"] < 0           # the ghost: negative norm
    assert res["has_ghost"] is True
    assert ci.riegert_partial_fraction_check(M2=2.0)   # the decomposition is exact


def test_route2_anomaly_permits_not_forces():
    """Route 2 verdict: the anomaly does not FORCE the conformal carrier (it permits at most)."""
    v = ci.anomaly_forces_or_permits()
    assert v["4th_order_carries_ghost"] is True
    assert v["Q_forbids_clean_carrier"] is True
    assert "PERMITS" in v["verdict"] and "NOT FORCE" in v["verdict"]


def test_conjunction_is_outcome_C():
    """Both routes ⇒ (C): carrier identity is free data; α is ANCHOR on two exhausted routes."""
    c = ci.routes_conjunction()
    assert "(C)" in c["outcome"]
    assert "free data" in c["outcome"].lower()
    assert "two exhausted routes" in c["alpha_tier"]


def test_value_one_third_not_referenced():
    """Inverted-laundering guard: 2B must NOT reach for 1/3 (it is banked in Target 2). Its
    appearance anywhere in this module's reported strings would be a reverse-fit tell."""
    blob = " ".join(str(v) for v in ci.status().values())
    blob += " ".join(str(v) for v in ci.routes_conjunction().values())
    assert "1/3" not in blob and "0.333" not in blob


def test_grut_does_not_force_carrier_raises():
    """GRUT does not FORCE the conformal carrier — it RAISES (the carrier role is free data)."""
    with pytest.raises(NotImplementedError):
        ci.grut_forces_conformal_carrier()
