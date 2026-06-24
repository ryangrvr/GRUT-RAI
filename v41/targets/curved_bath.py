"""GRUT-RAI v4.1 — TARGET 1C: the curved-space IR exponent s of the TT-shear bath.

Target 1B reduced single-pole-ness to ONE number: the IR exponent s of the bath spectral
density J(ω) ~ ω^s (ω→0). s≥1 ⇒ single-pole THEOREM; s<1 ⇒ sub-Ohmic power-law continuum
(SLOW). Flat-space did not fix s. The verdict lives in the IR, where curvature matters; this
module attempts s in a curved (de Sitter / FRW) background — the last route before the
single-pole property must be conceded as an anchor rather than a theorem.

────────────────────────────────────────────────────────────────────────────────────────
OUTCOME: (C) — CURVED SPACE ALSO DOES NOT FIX s. Both routes (flat 1B, curved 1C) fail.
This is the proof 1B was missing; single_pole is re-tiered OPEN → ANCHOR (posited, not
derived). The missing datum is named: the vacuum bath's TRANSPORT / COLLISIONALITY.

WHY (all four legs verified first-hand; numbers reproduce in __main__):

  THE STRUCTURAL INPUTS GRUT SUPPLIES EACH FAIL TO FIX s.
    J(ω) for a bath bilinearly coupled to the slow TT-shear is the coupling-weighted bath
    density of states (Caldeira–Leggett: J(ω)=π Σ (c_k²/2m_kω_k) δ(ω−ω_k)). So s is the IR
    edge of that DOS. The three things the action fixes do NOT pin that edge:
      (i)  Q / FDT / causality + positivity  → only J(ω) ≥ 0, analytic in the lower half-ω
           plane. Admits any s.
      (ii) the 1/r spatial kernel (masslessness) → the bath is GAPLESS (DOS reaches ω=0),
           but the EDGE POWER is unconstrained.
      (iii) KMS at T_c → fixes the fluctuation↔dissipation ratio (noise from J), not J's shape.
    Each is a real constraint; none touches the ω→0 power. (s_three_ways)

  THE DYNAMICAL VALUE OF s HINGES ON COLLISIONALITY — WHICH THE ACTION DOES NOT SPECIFY.
    • COLLISIONAL bath (finite shear viscosity): Kubo ⇒ J(ω→0)=ηω ⇒ s=1 (Ohmic) ⇒ FAST,
      independent of the DOS edge. Requires bath self-interaction (mode coupling) BEYOND the
      minimal linear-response/Gaussian action.
    • COLLISIONLESS bath (free / Gaussian — what linear response + FDT actually give):
      J(ω)=(π/2)·DOS(ω) ⇒ s = the DOS IR-edge exponent, which is FREE DATA. Generic edges
      give s<1 ⇒ SLOW (power-law phase-mixing memory). (free_bath_J vs interacting_bath_J)
    The CTP action fixes neither the collisionality nor the DOS edge ⇒ s ∈ {1, free} ⇒ (C).
    (Note: the MINIMAL/Gaussian reading is collisionless, which leans s<1/SLOW — the OPPOSITE
    of 1B's flat-space 'fast' intuition. Taking the action minimally points AWAY from
    single-pole, which is itself evidence single-pole is an assumption, not a consequence.)

  THE HUBBLE-FRICTION CHECK (1B's load-bearing 'H pushes s↑/fast') IS BROKEN.
    Modeled honestly, Hubble friction broadens each bath spectral line by width ~H. Convolving
    even a super-Ohmic (fast, p=2) DOS edge with a Lorentzian of width H fills ω=0 with weight
    ~H^p (nonzero) ⇒ drives s TOWARD 0 (more sub-Ohmic / SLOW), not toward fast. And it acts
    only at ω≲H ≈ (1/346)/τ₀ — ~10³× BELOW the decisive threshold 4/τ₀ — so it cannot settle
    the verdict either way. 1B's claim does not survive. (hubble_broadening)

  THE de SITTER IR-ENHANCEMENT CHANNEL IS CLOSED (but does not fix s).
    The dS secular IR growth lives in ⟨φ²⟩ (∫dk/k, divergent). The TT-shear couples to
    T ~ (∂φ)², and the derivatives give ⟨(∂φ)²⟩ ~ ∫k dk (IR-FINITE). So the cosmological
    scalar IR enhancement is derivative-PROTECTED and does NOT force s<1. This closes one
    specific slow channel — but the collisionless DOS-edge freedom is a DIFFERENT channel,
    still open. (ds_ir_protection)

ANTI-LAUNDERING (the brief's guards, the regime where answers get manufactured):
  - s computed THREE WAYS disagrees (structural: unconstrained; collisional Kubo: 1;
    collisionless DOS: free) ⇒ "s not robustly determined" ⇒ (C), per the brief.
  - NO IR REGULATOR SETS s honestly here: the would-be transport integral for a collisionless
    bath is IR-floor-sensitive (the v4 sin in curved clothing). We do not introduce a floor to
    manufacture s=1; the floor-sensitivity IS the (C) signal.
  - The 'natural' interacting-bath lean to s=1/fast is NAMED but NOT promoted: finite shear
    viscosity is the unproven assumption (a naturalness argument, exactly what the gate refuses
    to launder as a derivation).
  - Leading order in H/Λ, quasi-equilibrium (KMS). A leading-order lean is not a theorem.

GATE CONSEQUENCE (per the brief's (C) path): single_pole OPEN → ANCHOR, justified by the
two-route failure (flat 1B + curved 1C). Every claim consuming single_pole is re-audited:
the relic no-go is re-stated as conditional on the single-pole ANCHOR (it always was).
"""
from __future__ import annotations

import numpy as np

CB_THRESHOLD = 1.0   # s ≥ 1 ⇒ single-pole (fast); s < 1 ⇒ sub-Ohmic continuum (slow)


def ir_slope(J, w: float) -> float:
    """Clean log-log slope dlnJ/dlnω at ω, with a wide stencil that never straddles a
    resonance (the artifact that makes naive sub-Ohmic estimates unreliable)."""
    f = 1.2
    return float((np.log(J(w * f)) - np.log(J(w / f))) / (2.0 * np.log(f)))


# ── the two physically-permitted baths the action does NOT choose between ─────────────────
def free_bath_J(p: float, Omega_c: float = 100.0):
    """COLLISIONLESS (free / Gaussian) bath: J(ω) = coupling-weighted DOS = ω^p·e^{−ω/Ω_c}.
    s = p, the DOS IR-edge exponent — FREE DATA the action does not fix. This is what linear
    response + FDT (all the minimal action supplies) actually give."""
    return lambda w: (w ** p) * np.exp(-w / Omega_c)


def interacting_bath_J(eta: float = 1.0, Omega_c: float = 100.0):
    """COLLISIONAL bath with finite shear viscosity: Drude J(ω)=η ω/(1+(ω/Ω_c)²). Kubo ⇒
    s=1 (Ohmic) INDEPENDENT of any DOS edge — but requires bath self-interaction beyond the
    Gaussian action."""
    return lambda w: eta * w / (1.0 + (w / Omega_c) ** 2)


def s_three_ways(p_free: float = 0.5) -> dict:
    """The three determinations of s the action allows — they DISAGREE ⇒ s not robust ⇒ (C).
    p_free is an EXAMPLE collisionless DOS edge (itself free); s=p_free is read off, not fixed."""
    s_struct = "unconstrained (Q/FDT/positivity, 1/r-gaplessness, KMS all admit any s)"
    s_collisional = ir_slope(interacting_bath_J(), 1e-3)         # → 1
    s_collisionless = ir_slope(free_bath_J(p_free), 1e-3)        # → p_free (free)
    return {"structural_constraints": s_struct,
            "collisional_Kubo": s_collisional,
            "collisionless_DOS_edge": s_collisionless,
            "agree": False,
            "verdict": "s NOT robustly determined — collisional⇒1 (fast), collisionless⇒free (slow)"}


# ── the Hubble-friction check (1B's load-bearing claim) — modeled as line broadening ─────
def hubble_broadening(p: float, H: float, Omega_c: float = 100.0, n: int = 120000):
    """Hubble friction ≈ broadening each bath line by width ~H. Convolve a DOS edge ω^p with a
    Lorentzian of width H; return the broadened DOS at ω=0 and the IR slope just above it.
    A nonzero value at ω=0 means weight was added there ⇒ s driven toward 0 (slow), not fast."""
    def rho_H(w):
        wp = np.linspace(1e-7, Omega_c, n)
        return float(np.trapezoid((wp ** p) * (H / np.pi) / ((w - wp) ** 2 + H ** 2), wp))
    return {"H": H, "rho_H_at_0": rho_H(0.0), "s_below_H": ir_slope(rho_H, 0.1 * H)}


# ── the de Sitter IR-enhancement channel: derivative-protected ───────────────────────────
def ds_ir_protection(kmin: float = 1e-4, kmax: float = 10.0, n: int = 400000) -> dict:
    """dS super-horizon |φ_k|²~H²/k³. ⟨φ²⟩ ~ ∫dk/k (IR-divergent) but ⟨(∂φ)²⟩ ~ ∫k dk
    (IR-finite). The TT-shear couples to T~(∂φ)², so the scalar IR enhancement is suppressed
    — it does NOT push the bath sub-Ohmic. Returns both, with their kmin-sensitivity."""
    k = np.linspace(kmin, kmax, n)
    phi2 = float(np.trapezoid(k ** -1.0, k))          # ∫ k^-1 dk  → grows as kmin→0
    dphi2 = float(np.trapezoid(k ** 1.0, k))          # ∫ k^+1 dk  → finite as kmin→0
    return {"phi2_IR_divergent": phi2, "dphi2_IR_finite": dphi2,
            "stress_tensor_IR_protected": True}


def grut_curved_ir_exponent(*_a, **_k):
    """RAISE. The curved-space (de Sitter/FRW, KMS at T_c) route does not fix s either. s = the
    bath transport exponent: 1 if collisional (finite shear viscosity, Kubo) ⇒ fast; the free
    DOS-edge if collisionless ⇒ generically slow. GRUT's Q + FDT + 1/r kernel + KMS fix NEITHER
    the collisionality NOR the DOS edge. With BOTH the flat-space (1B) and curved-space (1C)
    routes failing, single-pole-ness is not derivable; it must be ANCHORED."""
    raise NotImplementedError(
        "curved space does not fix the IR exponent s. s=1 (fast) iff the vacuum bath is "
        "COLLISIONAL (finite shear viscosity, Kubo); s=DOS-edge (free, generically <1 ⇒ slow) "
        "if COLLISIONLESS. Q + FDT + 1/r kernel + KMS(T_c) fix neither collisionality nor the "
        "DOS edge. Both routes (1B flat, 1C curved) fail ⇒ single-pole is an ANCHOR, not a "
        "theorem. Missing datum: the vacuum bath's transport/collisionality."
    )


def status() -> dict:
    return {
        "target": "1C — the curved-space IR exponent s of the TT-shear bath",
        "outcome": "(C): curved space ALSO does not fix s; both routes (1B flat, 1C curved) fail",
        "gate_action": "single_pole re-tiered OPEN → ANCHOR (posited, not derived) — the "
                       "two-route failure is the justification 1B was missing",
        "missing_datum": "the vacuum bath's TRANSPORT/COLLISIONALITY (and, if collisionless, its "
                         "DOS IR-edge) — fixes neither s=1 (collisional/fast) nor s<1 (collisionless/slow)",
        "structural_inputs_insufficient": "Q/FDT/positivity, 1/r-gaplessness, KMS(T_c) each admit any s",
        "hubble_friction": "1B's 'H→fast' BROKEN: broadening adds IR weight (slow-ward) and acts "
                           "~10³× below the 4/τ₀ threshold — cannot settle the verdict",
        "ds_ir_enhancement": "CLOSED as a slow channel: T~(∂φ)² is derivative-IR-protected; but "
                             "the collisionless DOS-edge freedom remains a separate open slow channel",
        "natural_lean_named_not_promoted": "an interacting (finite-η) bath gives s=1/fast, but "
                                           "finiteness of transport is the unproven assumption (naturalness, not derivation)",
        "caveat": "leading order in H/Λ, quasi-equilibrium (KMS); a leading-order lean is not a theorem",
    }


if __name__ == "__main__":
    print("TARGET 1C — does curved space fix the IR exponent s?  OUTCOME: (C), no.\n")
    print("s THREE WAYS (they disagree ⇒ not robust ⇒ (C)):")
    r = s_three_ways()
    print(f"   structural constraints : {r['structural_constraints']}")
    print(f"   collisional (Kubo)     : s = {r['collisional_Kubo']:+.3f}  (= 1, fast)")
    print(f"   collisionless (DOS)    : s = {r['collisionless_DOS_edge']:+.3f}  (= the free DOS edge, slow)")
    print("\nHubble-friction check (1B claimed H → fast):")
    for H in (1e-3, 1e-2, 1e-1):
        b = hubble_broadening(2.0, H)
        print(f"   H={H:.0e}: ρ_H(0)={b['rho_H_at_0']:.3e} (weight added at ω=0) → s_below_H={b['s_below_H']:+.2f} (slow-ward)")
    d = ds_ir_protection()
    print(f"\nde Sitter IR protection: ⟨φ²⟩={d['phi2_IR_divergent']:.2f} (IR-divergent) vs "
          f"⟨(∂φ)²⟩={d['dphi2_IR_finite']:.2f} (IR-finite) → stress tensor IR-protected.")
    print("\nThe missing datum (the action does not supply it):")
    try:
        grut_curved_ir_exponent()
    except NotImplementedError as e:
        print("   RAISE:", e)
