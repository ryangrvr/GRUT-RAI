"""GRUT-RAI v4.1 — TARGET 2B: exhaust α's antecedent (the IR-carrier question).

Target 2 banked the CONSEQUENT: a/c = 1/3 (robust, scheme-independent). α = 1/3 follows IFF the
conformal (Riegert, spin-0) mode is the IR carrier of the vacuum response. Target 2 left α as a
PROVISIONAL anchor on ONE route (the projector lean) plus a freedom argument — weaker than
single-pole's TWO-route anchor. This module runs the missing second route (the anomaly channel)
and asks: does GRUT's action FORCE the conformal mode into the carrier role, or merely PERMIT it?

THE GUARD (α's value is known, so the inverted-laundering risk is acute): this task does NOT
re-derive a/c = 1/3 (banked, out of scope — its reappearance would be a reverse-fit tell). The
carrier question is logically PRIOR to and INDEPENDENT of the value. Route 2 is assessed by
FORCES-vs-PERMITS, never by "it yields 1/3 so it must be the carrier."

────────────────────────────────────────────────────────────────────────────────────────
OUTCOME: (C) — THE ANOMALY PERMITS BUT DOES NOT FORCE THE CONFORMAL CARRIER. The carrier role
is free data. α stays ANCHOR — now on TWO exhausted routes (linear + anomaly), symmetric with
single-pole, on EARNED grounds. The de-anchor condition is named and is tensioned by GRUT's own Q.

ROUTE 1 — LINEAR / PROJECTOR (verified first-hand; a real lean AGAINST the antecedent):
  The TT projector that gives μ_linear = 1 genuinely ANNIHILATES the conformal (trace) mode and
  the longitudinal mode (‖P^TT·(trace)‖, ‖P^TT·(long)‖ ≈ 0), while a spin-2 mode SURVIVES. This
  is a true projection of the spin-0 conformal mode, not gauge-fixing: the trace mode is in the
  kernel of the traceless projector by construction. So at LINEAR order the carrier is spin-2 and
  the conformal mode is not. SCOPE: this is a linear-sector statement; it does not by itself bind
  the anomaly sector (Route 2), which is a one-loop / non-linear effect outside the projector.

ROUTE 2 — ANOMALY / NON-LINEAR (the crux; assessed FORCES-vs-PERMITS, not by the value):
  For the conformal mode to be the IR CARRIER it must PROPAGATE. The anomaly induces the Riegert
  action, whose σ kinetic term is 4th-order (Paneitz Δ₄ ~ □²). A 4th-order propagator factorizes,
       1/[p²(p²+M²)] = (1/M²)[ 1/p²  −  1/(p²+M²) ],
  into a healthy pole (residue +1/M²) AND a GHOST pole (residue −1/M²) — an Ostrogradsky ghost
  (negative norm ⇒ Im χ < 0 ⇒ Q-violation, the SAME leg as propagating_relic_no_go). So a clean
  PROPAGATING conformal carrier is Q-forbidden. The anomaly therefore does NOT FORCE σ into the
  carrier role; the most it does is PERMIT it under the contested Antoniadis–Mottola reading,
  where the conformal factor is a non-standard (dim-0, logarithmic) "conformalon" claimed to
  evade the ghost. That evasion is an extra dynamical assumption GRUT does not establish — and it
  runs INTO GRUT's own Q-unitarity. Additionally, in the IR the 2-derivative Einstein term
  generically dominates the 4-derivative anomaly term, so even the IR-DOMINANCE the carrier role
  needs is contested, not forced.

CONJUNCTION ⇒ (C): linear projects the conformal mode OUT; the anomaly PERMITS it (at most,
contested) but does NOT FORCE it, and the forcing route is Q-tensioned. The carrier identity is
FREE DATA. α is an ANCHOR on two exhausted routes — the asymmetry with single-pole is fixed.

DE-ANCHOR CONDITION (named, as required): GRUT would have to establish a LEGITIMATE, non-ghost,
propagating conformal mode (an Antoniadis–Mottola conformalon) that DOMINATES the bare Einstein
action in the IR. This conflicts with GRUT's Q-unitarity (4th-order ⇒ ghost), so it is not merely
unestablished but structurally tensioned. Only resolving that in GRUT's favor would graduate α.

A UNIFICATION (emergent, flagged as an observation — not a new theorem): GRUT's Q-unitarity (no
new propagating vacuum pole — the relic-no-go leg) is what keeps BOTH spine parameters anchors.
Deriving single-pole's "fast" verdict would need to exclude a propagating dark pole; deriving α
would need a propagating conformal mode. Both are new propagating vacuum d.o.f. that Q forbids.
The same minimalism that powers GRUT's no-gos also blocks the derivation of its two foundational
parameters — so they are anchors not by accident but by GRUT's own central prohibition.
"""
from __future__ import annotations

import numpy as np


# ── ROUTE 1 — the linear projector annihilates the conformal mode ─────────────────────────
def _ptt_apply(M: np.ndarray, n: np.ndarray) -> np.ndarray:
    """Spatial transverse-traceless projection of a symmetric 2-tensor M:
    P^TT_{ij,kl} = T_ik T_jl − ½ T_ij T_kl, with transverse T = I − n⊗n."""
    T = np.eye(3) - np.outer(n, n)
    return T @ M @ T - 0.5 * T * np.trace(T @ M @ T)


def conformal_mode_projected_out(n=(0.3, -0.5, 0.8)) -> dict:
    """ROUTE 1: confirm the TT projector annihilates the conformal (trace) and longitudinal
    modes while a spin-2 mode survives — so the LINEAR carrier is spin-2, not the conformal mode."""
    n = np.asarray(n, float); n = n / np.linalg.norm(n)
    trace_mode = np.eye(3)                       # pure trace = the conformal mode
    long_mode = np.outer(n, n)                   # longitudinal scalar mode
    spin2 = np.array([[0., 1., 0.], [1., 0., 0.], [0., 0., 0.]])
    return {"conformal_trace_norm": float(np.linalg.norm(_ptt_apply(trace_mode, n))),
            "longitudinal_norm": float(np.linalg.norm(_ptt_apply(long_mode, n))),
            "spin2_survives_norm": float(np.linalg.norm(_ptt_apply(spin2, n))),
            "lean": "conformal mode projected OUT at linear order; carrier is spin-2"}


# ── ROUTE 2 — a propagating conformal carrier needs the ghostly 4th-order kinetic term ────
def riegert_propagator_residues(M2: float = 1.0) -> dict:
    """ROUTE 2: the 4th-order Riegert/Paneitz propagator 1/[p²(p²+M²)] partial-fractions into a
    healthy pole and a GHOST pole (opposite residues). A propagating conformal mode is therefore
    Ostrogradsky-ghostly ⇒ Im χ<0 ⇒ Q-forbidden (same leg as the relic no-go)."""
    return {"healthy_pole_residue": +1.0 / M2, "ghost_pole_residue": -1.0 / M2,
            "has_ghost": True,
            "consequence": "propagating conformal carrier ⇒ negative-norm pole ⇒ Im χ<0 ⇒ Q-violation"}


def riegert_partial_fraction_check(M2: float = 1.0) -> bool:
    """Verify 1/[p²(p²+M²)] = (1/M²)[1/p² − 1/(p²+M²)] (the ghost decomposition is exact)."""
    for p2 in (0.5, 2.0, 10.0):
        full = 1.0 / (p2 * (p2 + M2))
        pf = (1.0 / M2) * (1.0 / p2 - 1.0 / (p2 + M2))
        if abs(full - pf) > 1e-12:
            return False
    return True


def anomaly_forces_or_permits() -> dict:
    """ROUTE 2 verdict: FORCES vs PERMITS, assessed independently of the value 1/3."""
    return {
        "to_be_carrier_must_propagate": True,
        "propagating_needs_4th_order_kinetic": "Riegert/Paneitz Δ₄ ~ □²",
        "4th_order_carries_ghost": riegert_propagator_residues()["has_ghost"],
        "Q_forbids_clean_carrier": True,
        "permits_under": "contested Antoniadis–Mottola conformalon (non-standard dim-0 mode "
                         "claimed to evade the ghost) — an extra assumption GRUT does not establish",
        "ir_dominance_contested": "in the IR the 2-derivative Einstein term generically dominates "
                                  "the 4-derivative anomaly term",
        "verdict": "PERMITS (at most, contested) — does NOT FORCE the conformal carrier",
    }


def routes_conjunction() -> dict:
    """Route 1 ∧ Route 2 ⇒ (C): carrier identity is free data; α is ANCHOR on two routes."""
    r1 = conformal_mode_projected_out()
    r2 = anomaly_forces_or_permits()
    return {"route1_linear": "conformal mode projected OUT (carrier spin-2); verified",
            "route1_norms": {k: r1[k] for k in ("conformal_trace_norm", "longitudinal_norm", "spin2_survives_norm")},
            "route2_anomaly": r2["verdict"],
            "outcome": "(C) — anomaly permits but does not force; carrier identity is FREE DATA",
            "alpha_tier": "ANCHOR on two exhausted routes (symmetric with single-pole)"}


def grut_forces_conformal_carrier(*_a, **_k):
    """RAISE. GRUT's action does not FORCE the conformal mode into the IR-carrier role. Route 1
    (linear) projects it out; Route 2 (anomaly) permits it only under the contested non-ghost
    conformalon reading, which conflicts with GRUT's Q-unitarity. The carrier role is free data,
    so α is an ANCHOR. De-anchor condition: a legitimate non-ghost conformal mode dominating the
    IR — tensioned by Q (4th-order ⇒ Ostrogradsky ghost)."""
    raise NotImplementedError(
        "GRUT does not FORCE the conformal Riegert mode as the IR carrier. Linear: the TT "
        "projector annihilates it (carrier is spin-2). Anomaly: a propagating conformal carrier "
        "needs the 4th-order Riegert kinetic term, which carries an Ostrogradsky ghost (Im χ<0 ⇒ "
        "Q-violation, the relic-no-go leg). The anomaly PERMITS (contested AM conformalon) but does "
        "not FORCE it. Carrier identity is FREE DATA ⇒ α is an ANCHOR. De-anchor: establish a "
        "legitimate non-ghost conformalon dominating the IR — which GRUT's Q tensions."
    )


def status() -> dict:
    return {
        "target": "2B — exhaust α's antecedent (the IR-carrier question)",
        "outcome": "(C): anomaly PERMITS but does NOT FORCE the conformal carrier; carrier identity is free data",
        "route1_linear": "conformal/trace mode projected OUT by the TT projector (verified); carrier is spin-2",
        "route2_anomaly": "a propagating conformal carrier needs the 4th-order Riegert kinetic term ⇒ "
                          "Ostrogradsky ghost ⇒ Q-forbidden; permitted only by the contested AM conformalon",
        "alpha_tier": "ANCHOR — UPGRADED to two-route grade (linear + anomaly), symmetric with single-pole",
        "de_anchor_condition": "establish a legitimate non-ghost conformal mode dominating the IR "
                               "(Antoniadis–Mottola) — structurally tensioned by GRUT's Q-unitarity",
        "unification": "Q-unitarity (no new propagating vacuum pole) keeps BOTH spine parameters anchors: "
                       "deriving single-pole needs a propagating dark pole, deriving α needs a propagating "
                       "conformal mode — both forbidden by the same minimalism that powers GRUT's no-gos",
        "scope": "Route 1 is linear-sector; Route 2 rests on the standard (Ostrogradsky) reading of the "
                 "4th-order kinetic term — the AM camp contests it, which is exactly the de-anchor opening",
    }


if __name__ == "__main__":
    print("TARGET 2B — exhaust α's antecedent (IR-carrier question).  OUTCOME: (C).\n")
    print("ROUTE 1 — linear projector (does the TT projector annihilate the conformal mode?):")
    r1 = conformal_mode_projected_out()
    print(f"   ‖P^TT(conformal/trace)‖ = {r1['conformal_trace_norm']:.2e}   "
          f"‖P^TT(longitudinal)‖ = {r1['longitudinal_norm']:.2e}   (annihilated)")
    print(f"   ‖P^TT(spin-2)‖ = {r1['spin2_survives_norm']:.3f}  (SURVIVES) → carrier is spin-2")
    print("\nROUTE 2 — anomaly channel (does a propagating conformal carrier carry a ghost?):")
    res = riegert_propagator_residues()
    print(f"   4th-order propagator residues: healthy={res['healthy_pole_residue']:+.1f}, "
          f"ghost={res['ghost_pole_residue']:+.1f}  (partial-fraction exact: {riegert_partial_fraction_check()})")
    print(f"   verdict: {anomaly_forces_or_permits()['verdict']}")
    print("\nCONJUNCTION:")
    c = routes_conjunction()
    print(f"   {c['outcome']}")
    print(f"   α: {c['alpha_tier']}")
    print("\nThe missing datum (the action does not force it):")
    try:
        grut_forces_conformal_carrier()
    except NotImplementedError as e:
        print("   RAISE:", e)
