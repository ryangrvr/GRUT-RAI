"""GRUT-RAI v4.1 — TARGET 3: the Deborah number and scale (corrected after an adversarial pre-screen).

The first draft of this target over-claimed in three ways the round-3 failure mode predicts
(errors that STRENGTHEN the result). An adversarial pre-screen caught them; all three are
verified first-hand and fixed here. The honest, weaker, correct version:

WHAT IS TRUE — and it is NOT "forward motion that bypasses the kernel fork":
  De(L) = τ_relax / t_probe(L). With the posited probe law t_probe = L/c_s, De(L) = c_s τ_relax / L,
  and there is a single DIVIDING SCALE L* = c_s τ_relax where De = 1 — elastic (holds structure)
  below it, viscous (flows) above it — **only when the kernel has a single relaxation time τ_relax**,
  i.e. the single-pole / Maxwell (collisional) branch of the fork. On the power-law / free-streaming
  (Weinberg) branch the kernel is self-similar K(t)~t^{-α} with NO characteristic time: there is no
  τ_relax to plug in, NO L*, and the medium is SCALE-FREE — the same viscoelastic character at every
  scale (verified: tan δ = const). So:

    • the bare statement "De = c_s τ/L runs with scale" is kernel-independent but VACUOUS (it is the
      definition De=τ/t plus the probe law — a ratio changes when its denominator does);
    • the CONTENTFUL statement "different aspects of reality at different scales" (a solid→fluid
      crossover at L*) holds ONLY on the single-τ / Maxwell branch. On the power-law branch the
      prediction is the OPPOSITE — scale invariance, the SAME aspect at every scale.

  Therefore the Deborah target does NOT route around the collisionality fork; it presupposes the
  collisional side. Its real value is the reverse of what was first claimed: the two branches predict
  QUALITATIVELY DIFFERENT scale-structure (a dividing scale vs scale invariance), so the observed
  scale-dependence of cosmic structure is an OBSERVABLE HANDLE ON THE FORK — not a way to avoid it.
  (This is the honest correction to "it works for either rheology, just differently": it does, but
  one branch has a crossover and the other has none, and that difference re-invokes the fork.)

THE CHARACTER DISCRIMINANT IS DEGENERATE (do not over-sell it). Reading the rheology from the
storage/loss split (Maxwell → one loss peak; critical gel → tan δ const, scale-free; well-separated
multi-mode → one peak per mode) is a clean-limit heuristic only. Verified first-hand: a closely
spaced 3-mode kernel reads as ~Maxwell, and a continuous BSW spectrum (Σ Maxwell modes weighted
τ^{-α}) reproduces power-law/scale-free — so the kernel→character map is MANY-TO-ONE and not
invertible. It discriminates the kernel only when relaxation times are well separated AND the
observation window spans them.

NOTE ON TWO "De"s. The physical Deborah number De(L)=c_s τ/L lives in L-space and needs τ. The
character functions below sweep a dimensionless frequency x = ωτ_ref in ω-space and need no τ→L map.
They are different objects; the ω-sweep is named `x` to stop it lending false well-posedness to the
L-space mechanism.

GUARD held (the one thing the pre-screen confirmed was clean): c_s is a free parameter, L* is carried
as L*(c_s), and the c_s=c value (~12.9 Mpc) appears only in a print, never in a check — not fit to
any observed scale.

TIER: this is HOSTED / PLACE, not DERIVED — De(L)=c_s τ/L is algebraic substitution of two anchors
(the kernel's τ and the posited probe law), scoped to the un-resolved single-τ branch. It is a
placed structural consequence, not a forward derivation.
"""
from __future__ import annotations

import numpy as np


# ── the single-τ Deborah mechanism (well-posed ONLY on the Maxwell/collisional branch) ────
def deborah_number(tau_relax: float, t_probe: float) -> float:
    """De = τ_relax / t_probe. Well-defined only for a kernel with a single relaxation time
    (Maxwell/collisional branch). >1 ⇒ elastic; <1 ⇒ viscous."""
    return tau_relax / t_probe


def has_dividing_scale(kernel: str) -> bool:
    """Does a sharp dividing scale L* exist? YES for a single/finite relaxation time
    (Maxwell/multi-mode); NO for a power-law/scale-free kernel (no characteristic time)."""
    return kernel in ("maxwell", "multi_mode")


def crossover_scale(tau_relax: float, c_s: float, kernel: str = "maxwell"):
    """L* = c_s · τ_relax, where De(L*) = 1. Returns None for a power-law/scale-free kernel —
    there is no τ_relax and no dividing scale (refusing to manufacture a fictitious L*, the
    pre-screen's C-C catch). c_s is a FREE PARAMETER; L* is a function of it."""
    if not has_dividing_scale(kernel):
        return None
    return c_s * tau_relax


# ── the rheology character (ω-sweep x = ωτ_ref; a DEGENERATE clean-limit heuristic) ───────
def _maxwell(x):
    return x ** 2 / (1 + x ** 2), x / (1 + x ** 2)


def _power_law(x, alpha=0.5):
    return (x ** alpha) * np.cos(alpha * np.pi / 2), (x ** alpha) * np.sin(alpha * np.pi / 2)


def _multi_mode(x, taus=(0.01, 1.0, 100.0)):
    Gp = sum((x * t) ** 2 / (1 + (x * t) ** 2) for t in taus)
    Gpp = sum((x * t) / (1 + (x * t) ** 2) for t in taus)
    return Gp, Gpp


def _loss_peaks(Gpp) -> int:
    """Strict interior local maxima of G''(x) via derivative sign change, with flats removed
    (fixes the non-strict-tie over-count that read 3 modes as 4)."""
    d = np.sign(np.diff(np.log(Gpp + 1e-30)))
    d = d[d != 0]                                    # drop flat segments (plateau/tie dedup)
    return int(np.sum((d[:-1] > 0) & (d[1:] < 0)))


def _tand_spread(Gp, Gpp, x) -> float:
    t = np.log(Gpp / Gp); m = (x > 1e-2) & (x < 1e2)
    return float(np.std(t[m]))


def rheology_character(kernel: str = "maxwell") -> dict:
    """Clean-limit character of a rheology. DEGENERATE: closely-spaced multi-mode mimics Maxwell,
    a continuous spectrum mimics power-law — so this resolves the kernel only for well-separated
    times spanning the window. The sweep variable x is ωτ_ref (frequency), NOT the L-space De."""
    x = np.logspace(-4, 4, 20000)
    Gp, Gpp = {"maxwell": _maxwell, "power_law": _power_law, "multi_mode": _multi_mode}[kernel](x)
    npk, spread = _loss_peaks(Gpp), _tand_spread(Gp, Gpp, x)
    if npk == 0 and spread < 0.2:
        character = "scale-free (critical gel; NO dividing scale — same aspect at every scale)"
    elif npk == 1:
        character = "one elastic→viscous crossover (a single dividing scale L*, Maxwell branch)"
    else:
        character = f"{npk} crossovers (a hierarchy; well-separated modes only)"
    return {"kernel": kernel, "loss_peaks": npk, "tan_delta_logspread": round(spread, 3),
            "character": character}


def discriminant_is_degenerate() -> bool:
    """Demonstrate the many-to-one degeneracy first-hand: a closely-spaced 3-mode kernel reads as
    ≈Maxwell (its peaks merge to 1), and a continuous τ^{-α} spectrum reads scale-free over its
    interior band (≈power-law). So the character does NOT invert to a unique kernel."""
    x = np.logspace(-4, 4, 20000)
    _, g_close = _multi_mode(x, taus=(0.8, 1.0, 1.25))
    close_reads_maxwellish = _loss_peaks(g_close) <= 1               # 3 modes → 1 peak (merged)
    taus = np.logspace(-2, 2, 60); w = taus ** -0.5                  # a BSW continuum gel
    Gp = sum(wi * (x * t) ** 2 / (1 + (x * t) ** 2) for t, wi in zip(taus, w))
    Gpp = sum(wi * (x * t) / (1 + (x * t) ** 2) for t, wi in zip(taus, w))
    band = (x > 0.1) & (x < 10.0)                                    # the spectrum's scale-free interior
    continuum_band_spread = float(np.std(np.log((Gpp / Gp)[band])))
    return bool(close_reads_maxwellish and continuum_band_spread < 0.2)


def status() -> dict:
    return {
        "target": "3 — Deborah number & scale (HOSTED/PLACE; corrected after adversarial pre-screen)",
        "true_content": "a dividing scale L*=c_s·τ_relax (elastic below, viscous above) exists ONLY "
                        "on the single-τ / Maxwell (collisional) branch; the power-law / free-streaming "
                        "branch is SCALE-FREE (no L*, same aspect at every scale)",
        "not": "NOT kernel-independent forward motion: the contentful crossover needs a single τ, so "
               "it presupposes the collisional side — it does NOT bypass the fork",
        "real_value": "the two branches predict DIFFERENT scale-structure (dividing scale vs scale "
                      "invariance) ⇒ the observed scale-dependence is an OBSERVABLE HANDLE ON the fork",
        "discriminant": "DEGENERATE (many-to-one): resolves the kernel only for well-separated times "
                        "spanning the window; closely-spaced multi-mode mimics Maxwell, a continuum mimics power-law",
        "guard_held": "c_s free, L*(c_s) a function; the c_s=c value (~12.9 Mpc) is not fit to any observed scale",
        "errors_fixed": "peak counter (3-mode read 4 → now 3); fictitious L* on the power-law branch "
                        "(crossover_scale now returns None); DERIVED→HOSTED (definitional substitution, not a derivation)",
    }


if __name__ == "__main__":
    print("TARGET 3 — Deborah number & scale (corrected, HOSTED/PLACE).\n")
    print("Dividing scale L*=c_s·τ_relax exists only on the single-τ (Maxwell) branch:")
    for k in ("maxwell", "multi_mode", "power_law"):
        L = crossover_scale(1.0, 3e10, k)
        print(f"  {k:11s}: dividing scale? {has_dividing_scale(k)!s:5s}  L*(c_s=c)="
              f"{'None (scale-free)' if L is None else f'{L:.2e} cm'}")
    print("\nRheology character (DEGENERATE clean-limit heuristic; sweep x=ωτ_ref, not L-space De):")
    for k in ("maxwell", "power_law", "multi_mode"):
        r = rheology_character(k)
        print(f"  {k:11s}: peaks={r['loss_peaks']}, tanδ-spread={r['tan_delta_logspread']:.2f}  →  {r['character']}")
    print(f"\n  discriminant is degenerate (many-to-one)? {discriminant_is_degenerate()}")
    print("\n  ⇒ NOT a fork-bypass: the crossover needs a single τ (collisional branch). The two")
    print("    branches predict different scale-structure — an observable HANDLE on the fork, not an escape.")
