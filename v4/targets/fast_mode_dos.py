"""GRUT-RAI v4.1 — TARGET 1D: the IR exponent s from the COMMITTED fast-mode content.

History (kept honest): round 1 of external review corrected Target 1C ("s is free") and this
module FIRST claimed s=2 (super-Ohmic) ⇒ single-pole DERIVED. Round 2 of the SAME review found
that claim still wrong on the load-bearing step, and the graduation premature. Both corrections
are absorbed here.

THE ROUND-2 CORRECTION (verified first-hand): s=2 conflated the density of states with the
SPECTRAL DENSITY. J(ω) is not the DOS — it is the standard Caldeira–Leggett influence-functional
weight J(ω) = (π/2) Σ_k (c_k²/(m_k ω_k)) δ(ω−ω_k), and the field-mode normalization 1/ω_k knocks
ONE power off the DOS. For a local LINEAR coupling to a massless field in 3+1D:
     J(ω) ∝ ∫ d³k (1/ω_k) δ(ω−c|k|) ∝ ∫ k² dk (1/k) δ(ω−ck) ∝ ω   ⇒  s = 1 (OHMIC, MARGINAL),
not the s=2 claimed. The DOS gives ω²; the 1/ω_k makes it ω. The old "relativity fixes the DOS to
ω² so s=2" is RETRACTED — it was the v4 sin in miniature, the DOS argument wearing the spectral
density's clothes.

THE REAL PHYSICS (the exponent is NOT settled by power-counting — it depends on COLLISIONALITY,
the one thing two documents established the action does not fix). Three regimes, three ω→0
structures for the bilinear TT/stress-tensor vertex GRUT actually has:
  - COLLISIONAL (vacuum at T_c, hydrodynamic): the Kubo formula gives Im G_R^{TT}(ω) ~ ηω at
    low ω ⇒ s = 1 (Ohmic). This branch is LIVE — a vacuum at T_c has thermal structure; it is
    NOT a zero-temperature free field, so "needs self-interaction beyond the action" was wrong.
  - COLLISIONLESS VACUUM (T=0, free): stress-tensor phase space ⇒ super-Ohmic, s ≈ 2 (the
    reviewer's value for (∂φ)²; the earlier s=5 needs the specific quadrupole/spin-2 derivative
    structure of GRUT's vertex, UNCOMPUTED here — not asserted).
  - COLLISIONLESS THERMAL: the non-relaxing thermal momentum puts a δ(ω) spike at zero frequency
    ON TOP of the continuum. That spike is not an exponent — it is a different object that must
    be interpreted before any s can be read off.

WHAT IS ROBUST (and is the honest claim, NOT a theorem): every clean branch lands s ≥ 1, and the
only route to s < 1 needs an IR-ENHANCED DOS (ρ rising slower than ω² as ω→0 — non-relativistic
ω~k², or a glassy/1-over-f soft mode), which masslessness in 3+1D FORBIDS. So single-pole-ness is
WELL-MOTIVATED (s ≥ 1 across branches; the sub-Ohmic route is forbidden) — but it is a strong
CROSS-BRANCH ARGUMENT, not a single-exponent derivation. Note: collisionality remains free data;
it stopped deciding the single-pole VERDICT (all branches ≥1) but still decides whether the
vacuum is robustly fast (s=2) or marginally fast (s=1 — where the curved-space IR sub-leading
terms, the ones Target 1C closed, become the deciding pieces). That residual is exactly why this
is not a theorem yet.

TIER (corrected): single_pole is PENDING_REVIEW, not DERIVED. A DERIVED claim in this gate
consumes no unsettled input and passes a check that SETTLES it. This one rests on an exponent
three regimes disagree about, with the deciding computation — the finite-T interacting
⟨T_TT T_TT⟩(ω, k→0) for GRUT's vertex, and the free-gas δ(ω) interpretation — UNDONE. "DERIVED …
pending review" was a contradiction in the tier system; the honest label is PENDING_REVIEW with
that computation as the settle/graduate condition.

THE EXTERNALIZED QUESTION (publishable as-is; the clean leave-the-loop computation):
  A slow variable bilinearly coupled to the transverse-traceless sector of a thermal massless
  field (graviton bath at T_c) — what is the IR exponent of the influence-functional J(ω) as
  ω→0? Does the finite-T interacting ⟨T_TT T_TT⟩(ω, k→0) give Ohmic (s=1, hydrodynamic viscosity
  peak) or super-Ohmic (s≥2, free phase space), and how is the free-gas δ(ω) handled?
"""
from __future__ import annotations

import numpy as np


def massless_dos_exponent(d_space: int = 3) -> float:
    """DOS edge of a massless field in d_space spatial dimensions: ρ(ω) ∝ ω^(d_space−1).
    In 3+1D this is ω². NOTE: this is the DOS, NOT J(ω) — see linear_coupling_s()."""
    w = np.linspace(1e-3, 1.0, 4000)
    rho = w ** (d_space - 1)
    return float(np.polyfit(np.log(w[:1300]), np.log(rho[:1300]), 1)[0])


def linear_coupling_s(d_space: int = 3) -> float:
    """The CORRECTED linear-coupling exponent: J(ω) ∝ ∫d³k (1/ω_k) δ(ω−|k|) ∝ ω^(d_space−2).
    In 3+1D: s = 1 (Ohmic, marginal) — the 1/ω_k mode normalization knocks one power off the DOS.
    Computed by quadrature with the 1/ω_k factor present (the factor whose omission gave the
    wrong s=2)."""
    k = np.linspace(1e-4, 5.0, 400000)
    def J(w, dw=2e-3):
        band = np.abs(k - w) < dw
        return np.trapezoid(np.where(band, (k ** (d_space - 1)) * (1.0 / k), 0.0), k)
    ws = np.array([0.2, 0.4, 0.8, 1.6, 3.2])
    Js = np.array([J(w) for w in ws])
    return float(np.polyfit(np.log(ws), np.log(Js), 1)[0])


def cross_branch_map() -> list:
    """The honest state: the IR exponent depends on collisionality, not power-counting. Every
    clean branch is s ≥ 1; the s<1 route is forbidden by masslessness. This is the ARGUMENT that
    motivates single-pole-ness — not a single-exponent theorem."""
    return [
        {"regime": "collisional (T_c hydrodynamic)", "s": "1 (Ohmic)", "geq1": True,
         "basis": "Kubo: Im G_R^{TT}(ω) ~ ηω"},
        {"regime": "collisionless vacuum (T=0)", "s": "≈2 (super-Ohmic)", "geq1": True,
         "basis": "stress-tensor phase space (reviewer; exact value needs GRUT's vertex)"},
        {"regime": "collisionless thermal", "s": "δ(ω) + continuum", "geq1": None,
         "basis": "free-gas zero-frequency spike — needs interpretation, not an exponent"},
    ]


def sub_ohmic_is_forbidden() -> dict:
    """The one robust leg: s < 1 needs an IR-ENHANCED DOS (ρ rising slower than ω²) — a
    non-relativistic ω~k² band (ρ~ω^{1/2}) or a glassy/1-over-f soft mode. Masslessness in
    3+1D fixes ρ~ω² and forbids both. So no clean branch goes sub-Ohmic."""
    return {"needs": "ρ(ω→0) rising slower than ω² (non-relativistic / lower-D / glassy)",
            "masslessness_gives": "ρ ~ ω² exactly (3+1D relativistic)",
            "forbidden": True}


def settle_condition() -> str:
    """The computation (the PENDING_REVIEW target) that would settle the exponent and graduate or
    de-graduate single-pole-ness."""
    return ("finite-T interacting ⟨T_TT T_TT⟩(ω, k→0) for GRUT's TT/quadrupole vertex: Ohmic "
            "(s=1, hydro viscosity peak) vs super-Ohmic (s≥2, free phase space), and the "
            "free-gas δ(ω) interpretation. Externalized for adjudication (publishable as-is).")


def status() -> dict:
    return {
        "target": "1D — s from the committed fast modes (post round-2 review)",
        "outcome": "single-pole-ness is WELL-MOTIVATED (s≥1 across all clean branches; sub-Ohmic "
                   "forbidden by masslessness) but NOT a theorem — the exponent is collisionality-"
                   "dependent and the deciding finite-T computation is undone",
        "round2_correction": "the earlier s=2 conflated DOS with J(ω); with the 1/ω_k mode "
                             "normalization the massless linear case is s=1 (Ohmic, marginal), not 2",
        "branches": "collisional s=1 (Kubo); collisionless-vacuum s≈2; collisionless-thermal δ(ω)",
        "robust_leg": "no clean branch is sub-Ohmic; s<1 needs an IR-enhanced DOS masslessness forbids",
        "tier": "single_pole re-tiered DERIVED → PENDING_REVIEW (the exponent is open; 'DERIVED "
                "pending review' was a contradiction)",
        "settle_condition": settle_condition(),
    }


if __name__ == "__main__":
    print("TARGET 1D — s from the committed fast modes (post round-2 review).\n")
    print(f"  DOS exponent (3+1D)               : ρ ~ ω^{massless_dos_exponent():.2f}  (this is the DOS, not J)")
    print(f"  CORRECTED linear-coupling s       : s = {linear_coupling_s():.2f}  (Ohmic, marginal — with 1/ω_k)")
    print("  [the earlier s=2 dropped the 1/ω_k mode-normalization factor — RETRACTED]\n")
    print("  cross-branch map (exponent depends on collisionality, not power-counting):")
    for r in cross_branch_map():
        flag = "≥1" if r["geq1"] else "?"
        print(f"     {r['regime']:34s} s = {r['s']:18s} [{flag}]  {r['basis']}")
    sf = sub_ohmic_is_forbidden()
    print(f"\n  robust leg: sub-Ohmic needs {sf['needs']};")
    print(f"              masslessness gives {sf['masslessness_gives']} ⇒ s<1 FORBIDDEN.")
    print(f"\n  ⇒ single-pole-ness: PENDING_REVIEW (well-motivated, not a theorem).")
    print(f"  settle condition: {settle_condition()}")
