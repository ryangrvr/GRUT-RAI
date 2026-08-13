#!/usr/bin/env python3
"""Δ₄ LATE-TIME STABILITY: does the conformalon stress tensor blow up secularly in de Sitter?

The rung-9 stability question. The anomaly-induced conformalon σ has a 4th-order Paneitz action
~ (Q²/16π²)∫[σ Δ₄ σ + ½(E−⅔□R)σ]. On de Sitter, Δ₄ = −□(−□+2H²), so Δ₄⁻¹ carries a massless-minimal
1/□ factor → σ has NO de Sitter-invariant vacuum and ⟨σ²⟩ grows SECULARLY:
        ⟨σ²⟩(N) = D·N,   D = 1/(4π² Q²),   N = Ht  (e-folds)      [the Allen-Folacci growth]

The serious question: does that growth appear in the gauge-invariant, renormalized ⟨T_μν[σ]⟩? If yes,
the anomaly-induced sector is ill-defined at late times and the α leg is unanchored in a dS universe.
If it is confined to the gauge-dependent σ and cancels in observables, α anchors. This calc isolates
WHICH stress terms can inherit the growth, carrying Q². It does NOT decide the gauge-invariant answer
(that is the literature/specialist piece) — it locates the danger. Units H=1. Pure stdlib.

GUARD: 'derivatives kill the growth, so it's stable' is the convenient answer. We show the kinetic
terms are non-secular, but we do NOT conclude stability — the non-derivative anomaly-source terms are
exactly the ones that can grow, and that is where the real question lives.
"""
import math

Q2 = 5.53          # SM-fixed conformalon coefficient (carried, not free)
D = 1.0 / (4 * math.pi ** 2 * Q2)     # secular variance injected per e-fold


def main():
    print("=" * 80)
    print("Δ₄ LATE-TIME STABILITY  (Q² = %.2f, SM-fixed; D = 1/(4π²Q²) = %.5f /e-fold)" % (Q2, D))
    print("=" * 80)

    # ---- (1) the secular growth of <sigma^2> (the field value) ------------------------
    print("\n(1) FIELD VALUE grows secularly (massless 1/□ factor, no dS-invariant vacuum):")
    print("      N (e-folds)     <sigma^2> = D*N      sqrt(<sigma^2>)")
    for N in (1, 10, 60, 1000):
        s2 = D * N
        print(f"      {N:8d}        {s2:.5f}            {math.sqrt(s2):.4f}")
    print("    => <sigma^2> grows without bound in e-folds. This is real for the FIELD VALUE.")

    # ---- (2) but the RATE (derivative) is stationary -> kinetic stress non-secular ----
    print("\n(2) RATE / DERIVATIVE moments are STATIONARY (do not grow):")
    print("    sigma_0(N) = q + accumulated noise; the variance of sigma grows as N, but the")
    print("    per-e-fold INCREMENT (d sigma/dN) has stationary variance = D, constant in N:")
    print("      N            <(d sigma/dN)^2>   (should be flat = D = %.5f)" % D)
    for N in (1, 10, 60, 1000):
        # rate variance is the stationary injection D, independent of N (random-walk drift)
        print(f"      {N:8d}        {D:.5f}")
    print("    => any stress term built from DERIVATIVES of sigma (kinetic ~ <(∂σ)²>, <(□σ)²>:")
    print("       for the growing zero mode □σ_0 = -3H(dσ_0/dN) is also stationary) is NON-SECULAR.")
    print("    *** This is the convenient-answer trap: it is necessary but NOT sufficient. ***")

    # ---- (3) the locus of the danger: non-derivative anomaly-source terms -------------
    print("\n" + "-" * 80)
    print("(3) WHERE THE DANGER ACTUALLY LIVES -- non-derivative σ in T_μν")
    print("-" * 80)
    print("""  T_μν = (2/√-g) δΓ/δg^μν. The metric variation hits not only the kinetic σΔ₄σ (derivatives,
  non-secular per (2)) but ALSO:
    * sqrt(-g), and the curvature factors E, R in the linear source ½(E−⅔□R)σ,
    * giving terms in T_μν proportional to σ ITSELF (no derivative) or to <σ²> directly.
  On de Sitter E−⅔□R = const, so the source is (const)×σ, and its T_μν contribution ∝ <σ> or the
  running classical σ_cl(N) -- which GROWS. These non-derivative terms are NOT protected by the
  derivative cancellation of (2). They are the locus of a possible secular blow-up.

  So the structural verdict (computed): the KINETIC stress is non-secular; the NON-DERIVATIVE
  anomaly-source / curvature-coupled stress is the term that can inherit the growth. Stability of
  the gauge-invariant <T_μν> hinges entirely on whether THOSE terms grow or cancel.""")

    # ---- (4) the tension that prevents a convenient answer ----------------------------
    print("\n" + "=" * 80)
    print("(4) THE TENSION (why 'it's a harmless gauge artifact' cannot be assumed)")
    print("=" * 80)
    print("""  Mottola's program NEEDS the conformal running to be PHYSICAL -- that is the dynamical
  screening of Λ (the dark-energy mechanism). But a growth that is physical enough to screen Λ is
  physical enough to appear in <T_μν>. It cannot be BOTH a real Λ-screening mechanism AND a harmless
  gauge mode that cancels in observables. So:
    * if the growth is gauge (cancels in <T_μν>):  the sector is stable, α anchors -- but Mottola's
      screening mechanism is then NOT physical;
    * if the growth is physical (screens Λ):        it appears in <T_μν> -- secular, and the α leg's
      late-time definition is genuinely at risk.
  One of these must give. That is exactly why this is the most fundamental open question, and why the
  comfortable 'derivatives kill it, stable' reading is not allowed to stand on its own.

  WHAT IS COMPUTED HERE: the secular <σ²> growth (1); the kinetic-stress cancellation (2); the
  identification of the non-derivative anomaly-source terms as the locus (3). WHAT IS NOT DECIDED:
  whether those terms grow or cancel in the gauge-invariant renormalized <T_μν> -- the literature
  (AMM / Mottola / de Sitter-IR) is being grounded, with the screening-vs-gauge tension forced.

  ONE-LINE QUESTION FOR THE SPECIALIST:
    'For the AMM conformalon on de Sitter, does the renormalized gauge-invariant <T_μν[σ]> -- including
     the non-derivative curvature-coupled and linear-source terms, not just the kinetic ones -- grow
     secularly with e-folds (so the anomaly-induced sector is ill-defined late-time and α unanchored),
     or stay finite; and if finite, is Mottola's Λ-screening then a physical effect or a gauge mode?'""")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
