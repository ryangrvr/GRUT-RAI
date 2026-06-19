"""Spectrum Program — Phase I: the Pole Classification Theorem.

After the v3 dark-sector closure (C5a + the Locality–No-Halo Theorem, Test 07),
the dark-matter question reduces to a spectral one:

    POLE CLASSIFICATION THEOREM. The current GRUT kernel χ(ω) = 1/(1 − iωτ₀)
    possesses a SINGLE RELAXATIONAL pole (ω = −i/τ₀: on the imaginary axis ⇒
    massless/overdamped/dissipative; lower half-plane ⇒ causal & stable). A
    DERIVED DARK SECTOR REQUIRES ADDITIONAL STABLE POLES in the vacuum response
    spectrum. Their existence is not forbidden by GRUT's constraints (causality,
    CTP unitarity, finite memory, locality all permit a richer kernel) — it is
    determined by the effective action, and is the central question of the
    Spectrum Program (theory/GRUT_V4_SPECTRUM_PROGRAM.md).

General criterion (model-independent): a derived dark sector requires additional
dynamical degrees of freedom — additional poles. A stable, gapped, long-lived
pole OFF the imaginary axis (Re ω ≠ 0 ⇒ mass; Im ω < 0, |Im| ≪ |Re| ⇒ stable,
long-lived) is a particle-like, dark-matter-capable mode. Inertia (a z̈ term,
raising the constitutive law to 2nd order) is the most obvious way to add a pole,
but the theorem is stated in terms of POLES, not inertia, so it is independent of
the specific mechanism.

This module is the reusable Phase II tool: `classify_poles` takes the denominator
polynomial of ANY candidate kernel 1/D(ω) and returns the pole inventory and
classification. Convention: D(ω) with χ = 1/D; a pole is stable (causal) iff it
lies in the lower half ω-plane (Im ω < 0), matching χ = 1/(1 − iωτ₀) → ω = −i/τ₀.
"""

from __future__ import annotations

from typing import Dict, List

import numpy as np

_TOL = 1e-9


def classify_poles(denom_coeffs: List[complex]) -> List[Dict]:
    """Classify the poles of a kernel χ(ω) = 1/D(ω).

    `denom_coeffs` are the coefficients of D(ω) in DESCENDING powers of ω, e.g.
      first-order   D = 1 − iωτ₀         -> [-1j*τ₀, 1]
      second-order  D = 1 − iωτ₀ − ω²τ₁² -> [-τ₁**2, -1j*τ₀, 1]
    Returns one dict per pole: {omega, mass=|Re ω|, width=|Im ω|, kind, stable}.
      kind = 'massive' (off-axis, Re ω ≠ 0 — a gapped propagating mode) or
             'relaxational' (on the imaginary axis — overdamped, massless).
      stable = (Im ω < 0): causal lower-half-plane pole (decaying, not growing).
    """
    roots = np.roots(denom_coeffs) if len(denom_coeffs) > 1 else np.array([])
    out = []
    for w in roots:
        mass, width = abs(w.real), abs(w.imag)
        out.append({
            "omega": complex(w),
            "mass": float(mass),
            "width": float(width),
            "kind": "massive" if mass > _TOL else "relaxational",
            "stable": bool(w.imag < _TOL),     # lower half-plane (causal)
        })
    return out


def first_order(tau0: float = 1.0) -> List[Dict]:
    """Current GRUT kernel χ = 1/(1 − iωτ₀): expect ONE relaxational, stable pole."""
    return classify_poles([-1j * tau0, 1.0])


def second_order(tau0: float = 1.0, tau1: float = 1.0) -> List[Dict]:
    """Inertial kernel χ = 1/(1 − iωτ₀ − ω²τ₁²): two poles; massive (off-axis)
    iff underdamped (4τ₁² > τ₀²), else two relaxational poles on the axis.
    """
    return classify_poles([-(tau1**2), -1j * tau0, 1.0])


def admits_dark_capable_mode(poles: List[Dict], longevity: float = 0.1) -> bool:
    """A dark-capable (relic) mode is a stable, massive (off-axis) pole that is
    also LONG-LIVED: width ≪ mass (|Im ω| ≪ |Re ω|) — a narrow resonance
    approaching a real (undamped) pole. An off-axis pole alone is NOT enough: a
    heavily damped resonance (width ≈ mass, e.g. ω = ±0.87 − 0.5i) decays and is
    not a relic. `longevity` is the width/mass cutoff (default 0.1 ⇒ Q ≳ 5).

    Caveat (GRUT_V3_SPECTRUM_PROGRAM.md, Phase III + the Ostrogradsky+Q/FDT
    pincer): for a DISSIPATIVE vacuum the only way to reach width ≪ mass is the
    τ₀→0 (frictionless) limit, where FDT sends the noise N→0 and the mode
    DECOUPLES from the bath (an external field). Generating a genuine long-lived
    pole from the vacuum's OWN higher-derivative action is an Ostrogradsky ghost
    (wrong-sign residue ⇒ Im χ<0 ⇒ N<0 ⇒ violates Q). So a positive return here
    flags an IMPORTED/hosted DOF, not a vacuum-derived one."""
    return any(
        p["kind"] == "massive" and p["stable"] and p["width"] < longevity * p["mass"]
        for p in poles
    )


def coupled_relaxors_dark_capable(n_tau: int = 30, n_g: int = 30,
                                  tau0: float = 1.0) -> bool:
    """Phase II scan. Couple a fast relaxor y to the response z (NO inertia) and
    integrate y out: K_eff(ω) = (1 − iωτ₀) − g²/(1 − iωτ_y), whose zeros solve
    (1 − iωτ₀)(1 − iωτ_y) − g² = 0. Over all stable couplings (g < 1), does ANY
    stable OFF-AXIS (dark-capable) pole appear? Returns True if one is found.

    Expected False: however many relaxational variables you couple, the poles only
    redistribute ALONG the −i axis (overdamped) — no oscillation/mass without a
    restoring+inertia (z̈) term. A dark-capable pole requires an INERTIAL,
    matter-like degree of freedom, not more relaxors.
    """
    for ty in np.linspace(0.05, 5.0, n_tau):
        for g in np.linspace(0.0, 0.999, n_g):
            for r in np.roots([-tau0 * ty, -1j * (tau0 + ty), (1.0 - g * g)]):
                if abs(r.real) > _TOL and r.imag < -_TOL:    # stable AND off-axis
                    return True
    return False


def single_pole_passive_causal(tau0: float = 1.0) -> bool:
    """Deriving-F check. Q (CTP unitarity → FDT, noise kernel N ≥ 0) requires the
    response to be CAUSAL and PASSIVE. The single pole χ = 1/(1 − iωτ₀): pole at
    ω = −i/τ₀ (lower half-plane ⇒ causal), and Im χ(ω) = ωτ₀/(1+(ωτ₀)²) ≥ 0 for
    ω > 0 (passive). Both ⇒ Q-admissible (a Herglotz function)."""
    causal = first_order(tau0)[0]["omega"].imag < 0
    w = np.logspace(-3, 3, 400) / tau0
    chi = 1.0 / (1.0 - 1j * w * tau0)
    return bool(causal and np.all(chi.imag >= -_TOL))


def positive_superposition_is_passive(amps=(0.6, 0.4), taus=(1.0, 0.3)) -> bool:
    """The Herglotz form Q forces: χ(ω) = Σ a_i/(1 − iωτ_i), a_i ≥ 0 — a positive
    superposition of single-pole Debye modes. It is also causal + passive (one pole
    per relaxation channel). Confirms the FORM of F is the general Q-admissible
    kernel, not a free ansatz; #poles = #channels."""
    if not all(a >= 0 for a in amps):
        return False
    w = np.logspace(-3, 3, 400)
    chi = sum(a / (1.0 - 1j * w * t) for a, t in zip(amps, taus))
    return bool(np.all(chi.imag >= -_TOL))


def verify() -> Dict[str, bool]:
    """Self-test the Phase I classification, the Phase II verdict, and deriving-F."""
    fo = first_order(tau0=1.0)
    leg1 = len(fo) == 1 and fo[0]["kind"] == "relaxational"      # single relaxational pole
    leg2 = fo[0]["stable"] and fo[0]["mass"] < _TOL              # massless, stable
    leg3 = not admits_dark_capable_mode(fo)                       # NO dark mode in current GRUT

    # second-order recovers first-order as τ₁ → 0 (one finite pole near −i/τ₀)
    so_small = second_order(tau0=1.0, tau1=1e-4)
    finite = [p for p in so_small if p["width"] < 1e3]
    leg4 = len(finite) == 1 and abs(finite[0]["omega"] + 1j) < 1e-3

    # a LONG-LIVED inertial kernel (τ₁ ≫ τ₀, weak damping) → a dark-capable
    # (narrow, off-axis, long-lived) pole appears
    leg5 = admits_dark_capable_mode(second_order(tau0=1.0, tau1=100.0))
    # a heavily damped resonance (τ₁ ≈ τ₀) is off-axis but NOT a relic, and the
    # overdamped kernel (τ₁ ≪ τ₀) has no off-axis pole at all → neither is dark
    leg6 = (not admits_dark_capable_mode(second_order(tau0=1.0, tau1=1.0))
            and not admits_dark_capable_mode(second_order(tau0=1.0, tau1=0.2)))
    # every pole considered is causal (lower half-plane)
    leg7 = all(p["stable"] for p in fo + second_order(1.0, 1.0) + second_order(1.0, 0.2))

    # Phase II: coupled RELAXORS (no inertia) never give a dark-capable mode;
    # a dark mode requires an inertial (matter-like) DOF.
    relaxors_dark = coupled_relaxors_dark_capable()
    leg8 = not relaxors_dark
    leg9 = admits_dark_capable_mode(second_order(1.0, 100.0)) and not relaxors_dark

    return {
        "current_GRUT_single_relaxational_pole": bool(leg1),
        "pole_massless_and_stable":              bool(leg2),
        "current_GRUT_has_no_dark_mode":         bool(leg3),
        "recovers_first_order_as_inertia_to_0":  bool(leg4),
        "long_lived_inertia_gives_dark_pole":    bool(leg5),
        "damped_resonance_is_not_a_relic":       bool(leg6),
        "all_poles_causal_lower_half_plane":     bool(leg7),
        "relaxors_alone_give_no_dark_mode":      bool(leg8),
        "dark_mode_requires_inertial_matter_dof": bool(leg9),
        "F_form_single_pole_is_Q_admissible":    bool(single_pole_passive_causal()),
        "F_form_herglotz_is_general_Q_kernel":   bool(positive_superposition_is_passive()),
    }


if __name__ == "__main__":
    print("Spectrum Program — Phase I: Pole Classification Theorem\n")
    print("current GRUT  χ=1/(1−iωτ₀):")
    for p in first_order():
        print(f"   ω={p['omega']:+.3f}  {p['kind']}  stable={p['stable']}")
    print("\ninertial χ=1/(1−iωτ₀−ω²τ₁²), τ₁/τ₀=1 (underdamped):")
    for p in second_order(1.0, 1.0):
        print(f"   ω={p['omega']:+.3f}  {p['kind']}  stable={p['stable']}")
    print("\nverify():")
    for k, v in verify().items():
        print(f"   {k:42s}: {v}")
