"""Koide circulant unification — frontier #1 partial result (June 2026).

Sharpens the open three-flavor z_target problem (V7 §29) and CORRECTS the V7
"Spectral Koide" conjecture. This is genuine progress on the flavor frontier,
NOT a closure: it reduces the sector to a single structural input and states the
precise remaining open target. See theory/KOIDE_AMPLITUDE_UNIFICATION.md.

═══════════════════════════════════════════════════════════════════════════
SETUP — the circulant (Z₃) Koide parameterization
═══════════════════════════════════════════════════════════════════════════
For N generations, the square-root masses are written as a circulant vector

    √m_k = M_0 (1 + A cos(θ + 2πk/N)),   k = 0 … N-1

with M_0 the scale, θ the phase (mass ratios), and A the oscillation amplitude.
The Koide invariant is K = (Σ m_k) / (Σ √m_k)².

═══════════════════════════════════════════════════════════════════════════
RESULT 1 — the V7 "Spectral Koide" conjecture is OVERSTATED
═══════════════════════════════════════════════════════════════════════════
V7 §29 conjectures that K = 2/3 is "FORCED by the Z₃ cyclic structure." It is not.
Summing the circulant series (Σcos = 0, Σcos² = N/2 for N ≥ 3) gives, for ANY θ,

    ┌─────────────────────────────────────────┐
    │   K_N(A) = (1 + A²/2) / N                │   (theta-independent)
    └─────────────────────────────────────────┘

So Z₃ fixes the FORM (θ-independence) but NOT the value: K_3 ranges over all of
(1/3, ∞) as A varies. The Koide value K_3 = 2/3 requires the SPECIFIC amplitude

    A = √2     ⟺     √m makes a 45° angle with the democratic axis (1,1,1).

The amplitude — not the Z₃ symmetry — carries the physics. (Nature sits at
A = 1.41420, vs √2 = 1.41421, from the measured charged-lepton masses.)

═══════════════════════════════════════════════════════════════════════════
RESULT 2 — both candidate identities collapse to ONE input: A² = N − 1
═══════════════════════════════════════════════════════════════════════════
v2 carried two separate candidate identities: K = 2/3 (Koide) and
θ = K·α_vac = 2/9 (the phase). They are NOT independent. Posit the single
structural relation

    ┌─────────────────────────────────────────┐
    │   A² = N − 1        (α_vac = 1/N)        │
    └─────────────────────────────────────────┘

i.e. the oscillation variance equals the number of non-zero circulant modes
(equipartition of the N−1 oscillating Fourier modes about a unit mean), equal to
1/α_vac − 1. Then BOTH observables follow:

    K   = (1 + A²/2)/N        = (N + 1)/(2N)      → 2/3   at N = 3
    θ   = K · α_vac = K/N      = (N + 1)/(2N²)     → 2/9   at N = 3

So K = 2/3 and θ = 2/9 are two faces of A² = N − 1. The flavor sector's two
"coincidences" reduce to one.

═══════════════════════════════════════════════════════════════════════════
STATUS — what is closed, what remains open
═══════════════════════════════════════════════════════════════════════════
PROVEN (this module, tested): K_N(A) = (1+A²/2)/N; K=2/3 ⟺ A=√2; A²=N−1 ⟹
(K, θ) = ((N+1)/2N, (N+1)/2N²) = (2/3, 2/9) at N=3.

CANDIDATE (not derived from S_CTP): A² = N − 1 itself. It is well-motivated
(equipartition; A² = 1/α_vac − 1) but is an identity, like θ = 2/9 was — now
unified with it, not separately postulated.

SHARPENED OPEN TARGET (the actual frontier): does the three-flavor CTP fixed
point F_spatial[z*] = 0 land on the A² = N − 1 (45°) cone? If yes, K = 2/3 and
θ = 2/9 are theorems, not coincidences. This reduces the vague "derive the
flavor z_target" (V7 §29 "missing object") to ONE number: the amplitude.

STILL OUT OF REACH: M_0 (the absolute mass scale) — the dimensional-anchor gap
(GRUT constants give μ_0 = ℏ/τ_0 ~ 10⁻³¹ eV, 30 orders below GeV) is untouched
by this result and remains a separate honest-negative.

═══════════════════════════════════════════════════════════════════════════
FIXED-POINT DERIVATION ATTEMPT — NO-GO (June 2026)
═══════════════════════════════════════════════════════════════════════════
We then asked the sharper question: does the GRUT self-referential constitutive
fixed point FORCE A²=N−1 (turning K=2/3, θ=2/9 from candidates into theorems)?
The honest answer is NO. Three findings (all verified, fixed_point_amplitude_nogo):

  (1) Symmetry does not fix the amplitude. The Z₃-invariant Landau potential has
      critical point ρ* = −a₂/(2b): the amplitude is a function of the potential
      COEFFICIENTS, not fixed by Z₃. (Z₃ + gradient flow give the form, not the value.)
  (2) GRUT's own impedance gives the WRONG value. The natural self-referential
      balance — response = α_vac × drive, i.e. structured/democratic power
      2ρ = α_vac = 1/N — yields K = (1+1/N)/N = 4/9 at N=3, NOT 2/3. The Koide
      amplitude A=√2 is ~4.24× the impedance α_vac=1/3; GRUT's impedance is far
      too small to be its source.
  (3) Koide requires equipartition (2ρ = 1, structured power = democratic power,
      "impedance 1"), which is NOT GRUT's α_vac = 1/3. A linear self-consistency
      gives only pure modes (K=1/3 or 1), never the mixture; the ζ₀:ζ₁ ratio that
      gives K=2/3 needs nonlinear potential coefficients = the SM Yukawa input.

CONCLUSION: K=2/3 and θ=2/9 are NOT derivable from the GRUT constitutive fixed
point. They remain CANDIDATE IDENTITIES (not theorems). The amplitude is
irreducibly Yukawa-input — consistent with V7 §29 ("GRUT hosts, does not generate,
the Yukawas"). The earlier hope that the fixed point would close it is RETRACTED.

SURVIVING COINCIDENCE (recorded as such, NOT a derivation): at N=3,
K = 2/3 = (1 + α_vac)/2 = n_g²(0)/2 = 2·α_vac — the Koide ratio equals half the
GRUT DC refractive index n_g²(0)=1+α_vac=4/3. Numerically clean, but it is a
re-expression of the A²=N−1 posit; the dynamics (finding 2) does not produce it.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Dict

import numpy as np
import sympy as sp


# ─────────────────────────────────────────────────────────────────────
# Symbolic circulant Koide invariant
# ─────────────────────────────────────────────────────────────────────
def K_circulant_symbolic(N: int) -> sp.Expr:
    """K_N(A) computed symbolically from the circulant sum (theta-general).

    Returns the closed form in symbol A; verifies it is theta-independent.
    """
    A, theta = sp.symbols("A theta", real=True)
    k = sp.symbols("k", integer=True)
    s = [1 + A * sp.cos(theta + 2 * sp.pi * kk / N) for kk in range(N)]
    Ssum = sp.simplify(sum(s))
    S2 = sp.simplify(sum(si**2 for si in s))
    K = sp.simplify(S2 / Ssum**2)
    return sp.simplify(K)


def K_closed_form(A, N: int):
    """The proven closed form K_N(A) = (1 + A²/2)/N."""
    return (1 + A**2 / 2) / N


# ─────────────────────────────────────────────────────────────────────
# The A² = N − 1 unification
# ─────────────────────────────────────────────────────────────────────
def K_from_unification(N: int) -> Fraction:
    """K under A² = N−1:  K = (N+1)/(2N).  → 2/3 at N=3."""
    return Fraction(N + 1, 2 * N)


def theta_from_unification(N: int) -> Fraction:
    """θ = K·α_vac under A²=N−1, α_vac=1/N:  θ = (N+1)/(2N²). → 2/9 at N=3."""
    return Fraction(N + 1, 2 * N * N)


def amplitude_for_koide(K_target=Fraction(2, 3), N: int = 3) -> float:
    """Invert K_N(A) = (1+A²/2)/N for the amplitude A. K=2/3,N=3 → √2."""
    return float(sp.sqrt(2 * (Fraction(N) * K_target - 1)))


# ─────────────────────────────────────────────────────────────────────
# Empirical anchor: do the charged leptons sit at A = √2?
# ─────────────────────────────────────────────────────────────────────
def observed_amplitude() -> Dict[str, float]:
    """Implied amplitude A from measured charged-lepton masses (PDG)."""
    me, mmu, mtau = 0.51099895e-3, 105.6583755e-3, 1776.86e-3  # GeV
    s = np.array([np.sqrt(me), np.sqrt(mmu), np.sqrt(mtau)])
    K_obs = float((s**2).sum() / s.sum() ** 2)
    A_obs = float(np.sqrt(2 * (3 * K_obs - 1)))
    return {"K_obs": K_obs, "A_obs": A_obs, "sqrt2": float(np.sqrt(2)),
            "A_obs_minus_sqrt2": A_obs - float(np.sqrt(2))}


# ─────────────────────────────────────────────────────────────────────
# Fixed-point derivation NO-GO (June 2026)
# ─────────────────────────────────────────────────────────────────────
def K_from_power_ratio(two_rho, N: int = 3):
    """Koide K for structured/democratic power ratio 2ρ = 2|ζ₁|²/|ζ₀|²:
    K = (1 + 2ρ)/N."""
    return (1 + two_rho) / N


def fixed_point_amplitude_nogo() -> Dict[str, object]:
    """The fixed-point derivation NO-GO, as numbers.

    Shows the GRUT impedance balance gives K=4/9 (wrong), equipartition gives
    K=2/3 (right but = "impedance 1", not α_vac), and A=√2 is ~4× α_vac.
    """
    N = 3
    alpha = 1.0 / N
    return {
        "K_impedance_balance":  float(K_from_power_ratio(alpha, N)),   # 2ρ=α_vac → 4/9
        "K_equipartition":      float(K_from_power_ratio(1.0, N)),     # 2ρ=1     → 2/3
        "K_observed":           2.0 / 3.0,
        "A_koide":              float(np.sqrt(2)),
        "alpha_vac":            alpha,
        "A_over_alpha":         float(np.sqrt(2)) / alpha,             # ~4.24
        "K_eq_half_n_g_sq":     (1 + alpha) / 2,                       # = n_g²/2 = 2/3 (coincidence)
        "verdict": ("NO-GO: GRUT impedance gives K=4/9, not 2/3; Koide needs "
                    "equipartition (impedance 1, not α_vac=1/3); amplitude is "
                    "Yukawa-input. K=2/3 and θ=2/9 remain CANDIDATES, not theorems."),
    }


# ─────────────────────────────────────────────────────────────────────
# Verification harness (GRUT NIS pattern)
# ─────────────────────────────────────────────────────────────────────
def verify() -> Dict[str, bool]:
    """Self-test the unification result.

      (1) Circulant K_N(A) = (1+A²/2)/N  (symbolic, theta-independent), N=3,4,5.
      (2) Z₃ alone does NOT fix K: K varies with A  (corrects V7 conjecture).
      (3) K=2/3 ⟺ A=√2.
      (4) A²=N−1 ⟹ K=(N+1)/(2N); N=3 → 2/3.
      (5) A²=N−1 ⟹ θ=K·α_vac=(N+1)/(2N²); N=3 → 2/9.
      (6) Measured charged leptons sit at A=√2 (Koide K≈2/3).
    """
    A = sp.Symbol("A", real=True)

    # (1) symbolic closed form for N=3,4,5
    leg1 = all(
        sp.simplify(K_circulant_symbolic(N) - K_closed_form(A, N)) == 0
        for N in (3, 4, 5)
    )

    # (2) K depends on A (NOT forced by Z₃ alone): three amplitudes, three K's
    Ks = [float(K_closed_form(a, 3)) for a in (1.0, np.sqrt(2), 2.0)]
    leg2 = len(set(round(x, 6) for x in Ks)) == 3 and not np.isclose(Ks[0], 2 / 3)

    # (3) K=2/3 ⟺ A=√2
    leg3 = np.isclose(amplitude_for_koide(Fraction(2, 3), 3), np.sqrt(2))

    # (4) A²=N−1 ⟹ K=(N+1)/(2N); N=3 → 2/3
    leg4 = (K_from_unification(3) == Fraction(2, 3)) and all(
        np.isclose(float(K_closed_form(np.sqrt(N - 1), N)), float(K_from_unification(N)))
        for N in (3, 4, 5)
    )

    # (5) θ=(N+1)/(2N²); N=3 → 2/9
    leg5 = (theta_from_unification(3) == Fraction(2, 9)) and all(
        theta_from_unification(N) == K_from_unification(N) * Fraction(1, N)
        for N in (3, 4, 5)
    )

    # (6) measured leptons at A≈√2
    obs = observed_amplitude()
    leg6 = abs(obs["A_obs_minus_sqrt2"]) < 1e-3 and np.isclose(obs["K_obs"], 2 / 3, atol=1e-4)

    # (7) NO-GO: GRUT impedance balance gives K=4/9 (≠ 2/3); equipartition gives 2/3
    ng = fixed_point_amplitude_nogo()
    leg7 = (np.isclose(ng["K_impedance_balance"], 4 / 9)
            and not np.isclose(ng["K_impedance_balance"], 2 / 3)
            and np.isclose(ng["K_equipartition"], 2 / 3))

    # (8) NO-GO: Koide amplitude is ~4× the impedance (too large to be a GRUT-impedance effect)
    leg8 = ng["A_over_alpha"] > 4.0 and np.isclose(ng["K_eq_half_n_g_sq"], 2 / 3)

    return {
        "circulant_closed_form_K_N":          bool(leg1),
        "Z3_alone_does_not_fix_K":            bool(leg2),
        "K_two_thirds_iff_A_sqrt2":           bool(leg3),
        "Asq_eq_Nminus1_gives_K":             bool(leg4),
        "Asq_eq_Nminus1_gives_theta":         bool(leg5),
        "measured_leptons_sit_at_A_sqrt2":    bool(leg6),
        "nogo_impedance_gives_4_9_not_2_3":   bool(leg7),
        "nogo_koide_amplitude_4x_impedance":  bool(leg8),
    }


if __name__ == "__main__":
    import json
    print("Symbolic K_3(A) =", K_circulant_symbolic(3))
    print("K under A²=N−1:  N=3 →", K_from_unification(3), " θ →", theta_from_unification(3))
    print("A for Koide (K=2/3, N=3):", amplitude_for_koide())
    print("Observed:", observed_amplitude())
    print("verify():", json.dumps(verify(), indent=2))
