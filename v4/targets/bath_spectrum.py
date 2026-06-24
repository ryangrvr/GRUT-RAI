"""GRUT-RAI v4.1 — TARGET 1B: specify or bound the TT-shear bath spectral density J(ω).

Target 1 reduced single-pole-ness to one object: J(ω), the spectral density of the
orthogonal (fast) Mori–Zwanzig force F(t) on the slow TT-shear variable z. This module
asks the next question the brief demands: does GRUT's CTP action FIX J(ω)'s low-frequency
behavior — enough to decide fast (single-pole theorem) vs slow (dark-capable second pole)?

────────────────────────────────────────────────────────────────────────────────────────
OUTCOME: (C)-DOMINANT — the action does NOT determine the IR tail. But the question is now
sharply collapsed, and the dangerous sub-case is partly closed. Details below; this label
is the corrected one AFTER an adversarial panel broke a stronger claim I first reached.

A RETRACTION (load-bearing — the panel earned it): my first pass claimed a "strong FAST
lean by scale separation": the threshold 4/τ₀ ≈ 3×10⁻¹⁵ s⁻¹ sits ~33 orders below any
microphysical bath frequency (1/τ_micro ≈ 7×10¹⁸ s⁻¹), so "any bath at its natural scale
is fast." THAT IS FALSE and is withdrawn. Scale separation is SHAPE-DEPENDENT: with the
SAME micro-scale UV cutoff, an Ohmic-or-stiffer bath (J∼ω^s, s≥1) is fast, but a
sub-Ohmic / IR-divergent bath (s<1) has τ_K = ∞ and is SLOW (verified, `ir_exponent_decides`).
The 33-order margin only buys "fast" IF J(ω)/ω carries no IR weight — which is exactly the
open question. So scale separation does not deliver a verdict; it RELOCATES the question.

WHAT THIS MODULE DOES ESTABLISH (the genuine deliverable):

  1. QUESTION COLLAPSE. The verdict does not need the whole function J(ω). It needs ONE
     bit: is J(ω)/ω IR-divergent at ω→0?
        Ohmic-or-stiffer (s≥1, no IR weight) → τ_K finite, UV-set → FAST → single-pole.
        sub-Ohmic / IR-divergent (s<1)       → τ_K → ∞                → SLOW.
     Everything else about J(ω) (its UV shape, its overall scale) is irrelevant to
     single-pole-ness. `ir_exponent_decides` shows the flip at fixed UV cutoff.

  2. THE SLOW REGIME IS STRUCTURED, AND ITS DISCRETE-RELIC SUB-CASE IS DOUBLY FORBIDDEN
     (conditional on the single-relaxational-channel model χ_mem). Two independent gates:
       (a) critical damping: for χ_mem = (1−iωτ_K)/(1−iωτ₀−ω²τ₀τ_K), τ_K=τ₀/4 is the
           overdamped→underdamped point (Q=√(τ_K/τ₀); τ₀/4 ⇔ Q=½, textbook critical).
           CAVEAT: this is a property of the assumed single-exponential memory, NOT a
           discovered universal feature; a genuine slow bath can be a sub-Ohmic CONTINUUM
           (branch cut, power-law memory) that χ_mem cannot represent. And the ring
           frequency is 1/√(τ₀τ_K), which equals ~1/τ₀ only near τ_K∼τ₀ — the earlier
           "the vacuum rings at 1/τ₀" is also withdrawn.
       (b) FDT positivity: Im χ_mem(ω>0) ≥ 0 (passive, N≥0) only for τ_K ≤ τ₀; it goes
           NEGATIVE for τ_K > τ₀. A relic-grade narrow resonance (Q>5 ⇔ τ_K ≳ 25 τ₀) lies
           deep in the FDT-non-passive zone. So a DISCRETE dark relic pole is closed twice
           over — by FDT positivity (τ_K>τ₀) and, in the undamped limit, by the existing
           Ostrogradsky relic no-go. (Parametrization-dependent; flagged in `fdt_gate`.)
     CONSEQUENCE: the genuinely open "slow" danger is NOT a tidy discrete dark pole — it is
     a non-resonant sub-Ohmic CONTINUUM in F(t). That is the precise object a curved-space
     MZ computation must rule in or out.

  3. THE CURVED-SPACE CAVEAT IS REAL BUT NARROW (not "the decisive regime"). The verdict
     lives in the IR; the flat-space reduction is IR-blind there. But every named
     curved-space mechanism (Hubble friction, super-horizon freezing, de Sitter IR growth,
     Gibbons–Hawking) deposits weight at ∼H₀, and 1/τ₀ ≈ 346 H₀ (`threshold_vs_hubble`),
     so the threshold 4/τ₀ sits ∼1.4×10³ ABOVE where curved effects live; Hubble friction
     in fact pushes toward fast (more adiabatic). The one residual channel is a parametric
     SWEEP (an effective frequency crossing 1/τ₀ during evolution, as H did near z∼48) or a
     from-scratch curved-space Mori–Zwanzig kernel. Neither is excluded by scale-counting.

ANTI-CIRCULARITY (the v4 sin, FORBIDDEN here): no spectral shape and no cutoff is assumed
to obtain a verdict. The IR exponent s is exactly what is NOT supplied — `grut_ir_tail()`
RAISES and names it. The no-go is not used to derive single-pole-ness (that would be
circular: the no-go consumes single-pole). The FDT gate (2b) is derived directly from
χ_mem's analytic structure, independently of the no-go.

TIER DECISION: single_pole stays OPEN — NOT promoted to DERIVED (the deciding integral,
the curved-space MZ force autocorrelation K(t)=⟨F(0)F(t)⟩, is uncomputed; the analysis is
flat-space), and NOT demoted to ANCHOR (we have not PROVEN the action cannot fix the IR
tail — we have shown the flat-space/single-channel route does not, and named a curved-space
computation that still could). It is OPEN-uncomputed: a theorem modulo one named integral.
The brief's "(C) ⇒ re-tier OPEN→ANCHOR" is therefore DECLINED, with reason recorded — full
ANCHOR status would require also showing the curved-space MZ route cannot determine s.
"""
from __future__ import annotations

import numpy as np

from v4.targets.memory_function import memory_kernel_from_J, tau_K_functional

OFF_AXIS_THRESHOLD_FACTOR = 0.25   # τ_K = τ₀/4 (= critical damping of χ_mem)


# ── 1. The verdict is a functional of the IR EXPONENT, not of scale separation ──────────
def power_law_bath(s: float, Omega_c: float):
    """J(ω) = ω^s · exp(−ω/Ω_c): IR exponent s, UV cutoff Ω_c. s≥1 Ohmic-or-stiffer,
    s<1 sub-Ohmic, s≤0 IR-divergent. ILLUSTRATIVE — used to EXHIBIT shape-dependence, not
    asserted to be GRUT's bath (that is the open question)."""
    return lambda w: (w ** s) * np.exp(-w / Omega_c)


def tail_residual(J, t0: float, wmax: float, tmax_over_t0: float = 50.0,
                  nw: int = 120000) -> float:
    """|γ(t)|/γ(0) evaluated at t = tmax_over_t0·τ₀. The ROBUST discriminant: an exponential
    (Ohmic-or-stiffer) tail has decayed to ≈0; a power-law (sub-Ohmic) tail still carries
    weight. Unlike the 1/e time, this does not mis-fire on power-law memory (panel C1/C2).
    Only the two endpoints t∈{0, tmax} are needed, so this is cheap."""
    g = memory_kernel_from_J(J, np.array([0.0, tmax_over_t0 * t0]), wmax=wmax, n=nw)
    return float(np.abs(g[1]) / abs(g[0]))


FAST_RESIDUAL_TOL = 1e-2   # an exponential single-pole tail is utterly negligible by 50τ₀


def ir_exponent_decides(tau0: float = 1.0, Omega_c: float = 100.0):
    """Show the verdict flips with the IR exponent s at a FIXED micro-scale UV cutoff Ω_c —
    the refutation of 'scale separation ⇒ fast' (same Ω_c, opposite verdicts). Classified by
    the TAIL RESIDUAL at 50τ₀ against a STRICT tolerance: a single-pole (exponential, single
    scale) tail with τ_K<τ₀/4 would be e^{−200}≈0 there, so any residual ≳10⁻² means the
    memory is NOT single-pole. The 1/e time is reported alongside ONLY to expose its failure
    on sub-Ohmic baths — it reads 'fast' (small τ_K) while a fat power-law tail remains. The
    s=0.5 residual is grid-sensitive in VALUE but ≫10⁻² regardless, so its SLOW call is robust."""
    out = []
    for s in (3.0, 1.0, 0.5, 0.0, -0.5):
        J = power_law_bath(s, Omega_c)
        resid = tail_residual(J, tau0, wmax=8.0 * Omega_c)
        # illustrative-only: a SHORT window suffices to catch the (fast) 1/e crossing and
        # expose the metric's failure (small τ_K) against the fat residual above.
        tauK_1e = tau_K_functional(J, t0=tau0, wmax=8.0 * Omega_c,
                                   tmax_over_t0=2.0, nw=40000, nt=2000)
        fast = resid < FAST_RESIDUAL_TOL
        out.append({"s": s, "Omega_c": Omega_c,
                    "class": "Ohmic-or-stiffer" if s >= 1 else "sub-Ohmic/IR-divergent",
                    "tail_residual_at_50tau0": resid, "tauK_1e_metric": tauK_1e,
                    "verdict": "FAST (single-pole)" if fast else "SLOW (power-law long memory)"})
    return out


# ── 2a. τ₀/4 is critical damping of the single-channel model (CONDITIONAL) ───────────────
def chi_mem(w: np.ndarray, tau0: float, tauK: float) -> np.ndarray:
    """The single-relaxational-channel response. NOTE: assuming THIS form is assuming the
    slow tail is one exponential; a continuum bath is not captured (panel C2)."""
    return (1 - 1j * w * tauK) / (1 - 1j * w * tau0 - (w ** 2) * tau0 * tauK)


def critical_damping_point(tau0: float = 1.0):
    """For χ_mem: poles are pure-imaginary (overdamped) for τ_K≤τ₀/4 and acquire a real
    part (underdamped) above. Q = √(τ_K/τ₀); τ₀/4 ⇔ Q=½ (textbook critical damping)."""
    out = []
    for r in (0.10, 0.24, 0.25, 0.26, 1.0):
        tauK = r * tau0
        poles = np.roots([-(tau0 * tauK), -1j * tau0, 1.0])
        out.append({"tauK_over_tau0": r, "max_abs_re_pole": float(np.max(np.abs(poles.real))),
                    "Q": float(np.sqrt(r)),
                    "regime": "overdamped" if np.max(np.abs(poles.real)) < 1e-9 else "underdamped (rings)"})
    return out


# ── 2b. FDT positivity is a SECOND, independent gate on the slow case ────────────────────
def fdt_gate(tau0: float = 1.0):
    """min Im χ_mem(ω>0) vs τ_K/τ₀. Passive (N≥0) requires Im χ ≥ 0. For χ_mem this holds
    only for τ_K ≤ τ₀; relic-grade Q>5 (τ_K ≳ 25 τ₀) is deep in the non-passive zone, so a
    DISCRETE dark relic is FDT-forbidden — independently of the Ostrogradsky no-go.
    Parametrization-dependent: a pure inertial kernel stays passive for all underdamping."""
    w = np.linspace(1e-4, 60.0, 200000)
    out = []
    for r in (0.5, 1.0, 1.1, 4.0, 25.0):
        tauK = r * tau0
        mn = float(np.min(np.imag(chi_mem(w, tau0, tauK))))
        out.append({"tauK_over_tau0": r, "Q": float(np.sqrt(r)), "min_Im_chi": mn,
                    "passive": bool(mn >= -1e-9)})
    return out


# ── 3. The curved-space caveat, quantified: the threshold is far above the Hubble scale ──
def threshold_vs_hubble(tau0_Myr: float = 41.9, H0_inv_Gyr: float = 14.5) -> dict:
    """1/τ₀ vs the Hubble frequency H₀. The verdict threshold 4/τ₀ sits ∼10³ ABOVE H₀, so
    curved-space effects (which live at ∼H₀) do not naturally deposit weight at 1/τ₀."""
    yr = 3.155815e7
    tau0_s = tau0_Myr * 1e6 * yr
    H0 = 1.0 / (H0_inv_Gyr * 1e9 * yr)
    return {"inv_tau0_per_s": 1.0 / tau0_s, "H0_per_s": H0,
            "inv_tau0_over_H0": (1.0 / tau0_s) / H0,
            "threshold_4_over_tau0_over_H0": (4.0 / tau0_s) / H0,
            "note": "curved-space weight sits at ∼H₀, ∼10³× below the 4/τ₀ threshold"}


# ── the GRUT-specific input that is STILL MISSING (the honest raise) ─────────────────────
def grut_ir_tail(*_a, **_k):
    """RAISE. The verdict needs ONE bit — the IR exponent s of J(ω) (is J(ω)/ω IR-divergent?).
    GRUT's CTP action supplies the FDT relation, the 1/r spatial kernel, and the TT projector
    — none of which fixes s. The deciding object is the curved-space Mori–Zwanzig force
    autocorrelation K(t)=⟨F(0)F(t)⟩, which is uncomputed. Refusing to assume s (v4 assumed
    Ohmic, s=1, with cutoff 1/τ_micro — which IS the fast conclusion) is the point."""
    raise NotImplementedError(
        "single-pole-ness is UNDECIDED until the IR exponent s of J(ω) is fixed: s≥1 "
        "(Ohmic-or-stiffer) ⇒ FAST ⇒ single-pole; s<1 (sub-Ohmic/IR-divergent) ⇒ SLOW. "
        "GRUT supplies FDT + 1/r kernel + TT projector but NOT s. The deciding object is the "
        "curved-space MZ force autocorrelation K(t)=⟨F(0)F(t)⟩ (uncomputed). Do not assume s "
        "(v4 assumed s=1, cutoff 1/τ_micro — the fast conclusion as an input)."
    )


def status() -> dict:
    return {
        "target": "1B — specify or bound J(ω)'s IR tail from the CTP action",
        "outcome": "(C)-dominant: action does NOT determine the IR tail; FAST is conditional "
                   "on an Ohmic-or-stiffer property that is itself the open question",
        "retracted": "the pre-panel 'strong FAST lean by scale separation' (shape-dependent; "
                     "fails for sub-Ohmic) and 'the vacuum rings at 1/τ₀' (rings at 1/√(τ₀τ_K))",
        "question_collapse": "from 'specify the function J(ω)' to ONE bit: is J(ω)/ω IR-divergent "
                             "(sub-Ohmic, s<1 ⇒ SLOW) or not (Ohmic-or-stiffer, s≥1 ⇒ FAST)?",
        "slow_is_structured": "discrete dark RELIC is doubly forbidden (FDT positivity τ_K>τ₀ + "
                              "Ostrogradsky undamped); the open danger is a non-resonant sub-Ohmic "
                              "CONTINUUM, conditional on the single-channel χ_mem model",
        "curved_caveat": "real but NARROW: 1/τ₀ ≈ 346 H₀; threshold ∼10³× above where curved "
                         "effects live; residual channel = parametric sweep or curved MZ kernel",
        "tier": "single_pole stays OPEN-uncomputed (theorem modulo the curved-space MZ integral); "
                "NOT DERIVED (flat-space, integral uncomputed), NOT ANCHOR (curved route unexhausted)",
        "sharpened_target": "compute K(t)=⟨F(0)F(t)⟩ for the TT-shear bath in curved space (KMS at "
                            "T_c); extract the IR exponent s of J(ω); s≥1 ⇒ single-pole theorem, "
                            "s<1 ⇒ dark continuum",
        "anti_circularity": "no spectral shape/cutoff assumed; s is the named missing object "
                            "(grut_ir_tail RAISES); no-go not used to derive single-pole",
    }


if __name__ == "__main__":
    print("TARGET 1B — does the CTP action fix J(ω)'s IR tail?  OUTCOME: (C)-dominant.\n")
    print("1. The verdict is set by the IR EXPONENT s, not by scale separation")
    print("   (SAME micro-scale UV cutoff Ω_c=100/τ₀; only s changes; classified by tail residual):")
    for r in ir_exponent_decides():
        print(f"   s={r['s']:+4.1f} [{r['class']:>22}]  resid@50τ₀={r['tail_residual_at_50tau0']:.3f}  "
              f"(1/e metric says τ_K={r['tauK_1e_metric']:.3g})  →  {r['verdict']}")
    print("\n2a. τ₀/4 = critical damping of the single-channel model (CONDITIONAL on χ_mem):")
    for r in critical_damping_point():
        print(f"    τ_K/τ₀={r['tauK_over_tau0']:.2f}  Q={r['Q']:.2f}  max|Re pole|={r['max_abs_re_pole']:.3f}  {r['regime']}")
    print("\n2b. FDT positivity — a SECOND gate (Im χ_mem(ω>0) ≥ 0 only for τ_K ≤ τ₀):")
    for r in fdt_gate():
        print(f"    τ_K/τ₀={r['tauK_over_tau0']:>5.1f}  Q={r['Q']:.2f}  min Im χ={r['min_Im_chi']:+9.3g}  "
              f"{'PASSIVE' if r['passive'] else 'NON-PASSIVE (relic forbidden)'}")
    h = threshold_vs_hubble()
    print(f"\n3. Curved caveat is narrow: 1/τ₀ = {h['inv_tau0_over_H0']:.0f}·H₀; "
          f"threshold 4/τ₀ = {h['threshold_4_over_tau0_over_H0']:.0f}·H₀ (curved weight lives at ∼H₀).")
    print("\nThe still-missing object (the action does not supply it):")
    try:
        grut_ir_tail()
    except NotImplementedError as e:
        print("   RAISE:", e)
