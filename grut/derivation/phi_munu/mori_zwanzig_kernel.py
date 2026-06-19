"""Spectrum Program — Phase III: the Mori–Zwanzig memory function.

This closes the load-bearing gap left by Phase I/II. The Spectrum Program had
shown that coupling RELAXATIONAL variables never makes a dark-capable pole, but
it chose the first-order (single-pole) constitutive law τ₀ż+z=z_target by
*covariantization fiat* (retarded_kernel_frw.py FORK 1) rather than by computing
the one object that can carry extra poles: the Mori–Zwanzig (MZ) memory function.
The frontier question "WHY is the responsive vacuum first-order?" is answered here.

THE GENERALIZED LANGEVIN EQUATION (single slow responsive variable z, the TT
memory; for a single variable the streaming term iΩ = ⟨ż z*⟩/⟨|z|²⟩ = 0 in a
stationary state):

    ż(t) = − ∫₀ᵗ K(t−s) z(s) ds + F(t),     χ(ω) ∝ 1/(K̃(ω) − iω)

where K(t) is the memory kernel and (2nd FDT) K(t) = ⟨F(0)F(t)⟩/⟨|z|²⟩ is the
autocorrelation of the ORTHOGONAL (fast) force F — so K(t)'s correlation time
τ_K is, by the very construction of the slow/fast projection, the FAST/micro
timescale: τ_K ≪ τ₀.

MARKOVIAN LIMIT (K̃(ω) ≈ K̃(0) = 1/τ₀ on the slow timescale):
    χ(ω) ∝ 1/(1/τ₀ − iω) ∝ 1/(1 − iωτ₀)     →  the SINGLE GRUT pole at ω = −i/τ₀.
So first-order-ness is the MARKOVIAN limit, with control parameter τ_K/τ₀.

FIRST NON-MARKOVIAN LEVEL (give the kernel its own one-pole memory,
K̃(ω) = (1/τ₀)/(1 − iωτ_K)) — the next rung of Mori's continued fraction:
    χ(ω) ∝ (1 − iωτ_K) / (1 − iωτ₀ − ω²·τ₀τ_K)
This is EXACTLY the second-order (inertial) kernel of pole_spectrum.py with
    τ₁² = τ₀ τ_K.
Its two poles go OFF the imaginary axis (oscillatory/massive ⇒ "dark-capable")
iff 4τ₁² > τ₀², i.e. iff

    τ_K > τ₀ / 4        (the memory kernel SLOWER than ¼ the relaxation time).

THE THEOREM. A genuine slow variable has τ_K ≪ τ₀ (that separation is what makes
it slow and what defines the MZ projection). Then τ_K > τ₀/4 is violated, the two
poles are BOTH on the −i axis (overdamped, massless, relaxational), and the
non-Markovian pole sits at the FAST scale ω ≈ −i/τ_K — and is further suppressed
in χ by the numerator zero at the same point (near pole–zero cancellation). So the
MZ hierarchy, for the responsive vacuum, produces NO dark-capable (off-axis,
long-lived, particle-like) pole: it produces one slow relaxational pole plus fast
on-axis corrections. The single-pole vacuum is the controlled consequence of the
τ_micro ≪ τ₀ hierarchy, not a fiat.

This is the DYNAMICAL face of the Ostrogradsky+Q/FDT pincer (see pole_spectrum.py
and GRUT_V3_SPECTRUM_PROGRAM.md): the only way to an off-axis pole is τ_K > τ₀/4 —
a memory kernel that is itself slow/resonant, i.e. a coherent (non-dissipative)
microscopic medium with its own internal dynamics. That is a NEW postulate
(a microscopic medium with massive excitations) = a foundational extension, not
anything the dissipative responsive vacuum generates.

Convention matches pole_spectrum.classify_poles: D(ω) coefficients in DESCENDING
powers of ω; a pole is stable/causal iff it lies in the lower half ω-plane.
"""

from __future__ import annotations

from typing import Dict, List

import numpy as np

from grut.derivation.phi_munu.pole_spectrum import classify_poles, admits_dark_capable_mode

_TOL = 1e-9

# GRUT scales (anchored): τ₀ gravitational relaxation; τ_micro the thermal/micro
# correlation time (the irreducible floor — tau_hierarchy_decision.py, Option B).
TAU0_SECONDS = 41.9e6 * 3.156e7        # ≈ 1.32e15 s
TAU_MICRO_SECONDS = 1.4e-19            # ≈ thermal ħ/(k_B T) micro time


def markovian_limit(tau0: float = 1.0) -> List[Dict]:
    """K̃(ω)=1/τ₀ (delta-correlated memory) ⇒ χ=1/(1−iωτ₀): ONE relaxational pole.
    This is GRUT's first-order constitutive law as the MZ Markovian limit."""
    return classify_poles([-1j * tau0, 1.0])


def second_level(tau0: float = 1.0, tauK: float = 1e-3) -> List[Dict]:
    """First non-Markovian rung: K̃(ω)=(1/τ₀)/(1−iωτ_K) ⇒
        χ ∝ (1−iωτ_K)/(1 − iωτ₀ − ω²·τ₀τ_K),  τ₁²=τ₀τ_K.
    Returns the poles (zeros of the denominator)."""
    return classify_poles([-(tau0 * tauK), -1j * tau0, 1.0])


def off_axis_threshold(tau0: float = 1.0) -> float:
    """The critical memory time: poles go off-axis (oscillatory/dark-capable) iff
    τ_K > τ₀/4 (from 4τ₁²>τ₀² with τ₁²=τ₀τ_K)."""
    return tau0 / 4.0


def is_overdamped(tau0: float, tauK: float) -> bool:
    """True iff the second-level kernel is overdamped — both poles ON the −i axis
    (relaxational, no oscillation) — i.e. iff τ_K ≤ τ₀/4. This is pole LOCATION
    (on- vs off-axis), distinct from dark-capability (which also needs the
    off-axis pole to be long-lived, width ≪ mass)."""
    return not any(p["kind"] == "massive" for p in second_level(tau0, tauK))


def slow_fast_separation_forbids_dark(tau_micro: float = TAU_MICRO_SECONDS,
                                      tau0: float = TAU0_SECONDS) -> bool:
    """THE THEOREM. For a genuine slow variable (τ_micro ≪ τ₀), the MZ memory
    function produces NO dark-capable pole: τ_K=τ_micro ≪ τ₀/4 ⇒ overdamped ⇒
    only on-axis (relaxational, massless) poles. Returns True when the hierarchy
    forbids a dark mode."""
    return tau_micro < off_axis_threshold(tau0) and is_overdamped(tau0, tau_micro)


def fast_pole_is_suppressed(tau0: float = 1.0, tauK: float = 1e-3) -> bool:
    """The non-Markovian (fast) pole at ω≈−i/τ_K is nearly cancelled in χ by the
    numerator zero at the same point: the physical slow response stays single-pole
    to O(τ_K/τ₀). Checks that |χ_2nd(ω)| matches the Markovian |χ_1st(ω)| across
    the slow band ω∈[0, 1/τ₀·few] to O(τ_K/τ₀)."""
    w = np.linspace(0.0, 5.0 / tau0, 400)
    chi1 = 1.0 / (1.0 - 1j * w * tau0)
    chi2 = (1.0 - 1j * w * tauK) / (1.0 - 1j * w * tau0 - (w ** 2) * tau0 * tauK)
    rel = np.max(np.abs(chi2 - chi1) / np.abs(chi1))
    return bool(rel < 10.0 * (tauK / tau0) + 1e-12)


def verify() -> Dict[str, bool]:
    """Self-test Phase III (the Mori–Zwanzig derivation of first-order-ness)."""
    # Markovian limit reproduces the single GRUT relaxational pole.
    ml = markovian_limit(1.0)
    leg1 = len(ml) == 1 and ml[0]["kind"] == "relaxational" and ml[0]["stable"]

    # Second level reduces to the Markovian single pole as τ_K → 0 (one finite pole
    # near −i/τ₀; the other runs off to −i∞).
    sl_small = second_level(1.0, 1e-9)
    finite = [p for p in sl_small if p["width"] < 1e3]
    leg2 = len(finite) == 1 and abs(finite[0]["omega"] + 1j) < 1e-3

    # The off-axis threshold is exactly τ₀/4.
    leg3 = is_overdamped(1.0, 0.24) and not is_overdamped(1.0, 0.26)
    leg4 = abs(off_axis_threshold(1.0) - 0.25) < _TOL

    # A slow variable (τ_K ≪ τ₀/4) is overdamped: two ON-AXIS poles, no dark mode.
    leg5 = is_overdamped(1.0, 1e-3) and not admits_dark_capable_mode(second_level(1.0, 1e-3))
    # while a memory kernel MUCH slower than the variable (τ_K ≫ τ₀, a resonant
    # medium) WOULD give a long-lived dark pole — the foundational-extension
    # escape, not anything the dissipative vacuum generates.
    leg6 = admits_dark_capable_mode(second_level(1.0, 1e4))

    # THE THEOREM at GRUT's actual hierarchy: no dark mode from MZ.
    leg7 = slow_fast_separation_forbids_dark()

    # The fast non-Markovian pole is suppressed in χ ⇒ effective single-pole.
    leg8 = fast_pole_is_suppressed(1.0, 1e-3)

    return {
        "markovian_limit_is_single_grut_pole":      bool(leg1),
        "second_level_reduces_to_markovian":        bool(leg2),
        "off_axis_only_when_memory_slow":           bool(leg3),
        "off_axis_threshold_is_tau0_over_4":        bool(leg4),
        "slow_variable_is_overdamped_no_dark_mode": bool(leg5),
        "resonant_kernel_would_give_dark_pole":     bool(leg6),
        "grut_hierarchy_forbids_dark_mode":         bool(leg7),
        "fast_pole_suppressed_effective_single":    bool(leg8),
    }


if __name__ == "__main__":
    print("Spectrum Program — Phase III: Mori–Zwanzig memory function\n")
    print(f"GRUT hierarchy: τ_micro/τ₀ = {TAU_MICRO_SECONDS/TAU0_SECONDS:.3e}  (≪ 1/4)\n")
    print("Markovian limit χ=1/(1−iωτ₀):")
    for p in markovian_limit():
        print(f"   ω={p['omega']:+.3f}  {p['kind']}  stable={p['stable']}")
    print("\nSecond level, slow variable (τ_K/τ₀=1e-3): poles")
    for p in second_level(1.0, 1e-3):
        print(f"   ω={p['omega']:+.4g}  {p['kind']}  stable={p['stable']}")
    print(f"\noff-axis threshold τ_K = τ₀/4 = {off_axis_threshold():.3f}")
    print("\nverify():")
    for k, v in verify().items():
        print(f"   {k:42s}: {v}")
