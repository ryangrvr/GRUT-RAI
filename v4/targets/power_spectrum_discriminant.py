"""GRUT-RAI v4.1 — TARGET 4: toward an outward branch test (NOT yet a falsifier — OPEN).

The intent was the first claim DATA can kill: turn the kernel fork into a power-spectrum test. A
second adversarial pre-screen (the highest-stakes, match-temptation moment the reviewer flagged)
showed the first draft over-claimed in all four ways the team's failure mode predicts. All four are
verified first-hand and recorded here; the honest status is OPEN, not a DERIVED falsifier.

THE POSITED CONTRAST (what would discriminate, IF the ansätze below held). Map the Deborah number
to k-space, De(k) ∝ k (small scales probe fast ⇒ elastic; large scales ⇒ viscous). Take the
viscoelastic "support" of structure to be the storage fraction S(k)=G'/(G'+G''). Then a single-τ
Maxwell medium gives S(k) with a BREAK (a characteristic scale); a strict critical gel gives S(k)
CONSTANT (scale-free). So *at the two endpoints* the contrast is real.

WHY IT IS NOT A FALSIFIER YET — four findings from the pre-screen, all reproduced in __main__:

  (P-C, fatal) THE DISCRIMINANT IS DEGENERATE. "Collisional" does not mean single-τ; a collisional
    medium generically has a relaxation SPECTRUM. As the spectrum widens the break vanishes — a
    collisional medium broader than ~5 decades reads SCALE-FREE, identical to free-streaming (a
    power-law relaxation spectrum reproduces the critical-gel response exactly). Maxwell and the
    gel are the two ENDPOINTS of one continuous parameter (spectrum width); the binary cannot tell
    broad-collisional from free-streaming. The single-τ choice silently picked the maximally-
    breaking endpoint. → a real test needs GRUT to DERIVE that the collisional branch is narrow.

  (P-B, fatal) FALSIFIABILITY IS ONE-SIDED, AND ENTANGLED. Because k_star is free, a collisional
    break can always hide outside any finite window — so BOTH "break" and "no break" are consistent
    with collisional: it is the unfalsifiable null. Only free-streaming (forbids any break) is
    killable. And P(k) ALREADY has breaks from known ΛCDM physics (the turnover k_eq, BAO), so
    "is there a break" is answered before GRUT is consulted; attributing a break to rheology needs
    the viscoelastic feature separated from k_eq/BAO — a structure-formation computation NOT done.

  (P-D, major) DEFINITION-AS-TARGET. The contrast is algebraic, not discovered: the critical-gel
    S=cos(απ/2)/(cos+sin) is constant for EVERY α (the De^α cancels) — scale-invariance is a
    tautology of the form, not a prediction; the Maxwell sigmoid breaks automatically. And De(k)∝k
    does zero work — any monotone De(k)=(k/k_star)^n gives the identical verdict, so the test cannot
    derive the linear law. The mappings De∝k and S = structure-support are POSITED ansätze, not
    obtained from the CTP action.

  (P-A, major) THE MATCH WAS DEFERRED, NOT AVOIDED. k_star=2π/(c_s·τ₀) with τ₀ anchored is a
    one-parameter (c_s) family — a fit-in-waiting — and the earlier draft had already computed and
    "suggestively" quoted the c_s=c, near-BAO value. That number is now excised everywhere; this
    module exposes no absolute scale and ingests no observed scale (test-enforced). But "no fit
    here" only DEFERS a one-parameter fit; it does not abolish it.

THE OPEN TARGET (what would make this a real, two-sided, ΛCDM-separable falsifier):
  (a) derive/bound the collisional relaxation-spectrum WIDTH from GRUT (only a narrow ≈single-τ
      kernel breaks; otherwise it is degenerate with free-streaming);
  (b) derive De(k)∝k and S = structure-support from the action (currently posited);
  (c) compute the full structure-formation P(k) modification per branch and show separability from
      k_eq and BAO;
  (d) bound c_s independently (not = c) so "no break in the observed window" can disfavour
      collisional — restoring two-sided falsifiability without a fit.
Until (a)–(d), this is a posited qualitative contrast, not a test. Tier: OPEN.
"""
from __future__ import annotations

import numpy as np

_K = np.logspace(-3, 3, 6000)   # k in units of k_star — dimensionless; no absolute scale anywhere


def _support_single_tau(branch: str) -> np.ndarray:
    """Endpoint storage fractions S(k)=G'/(G'+G''), De(k)=k/k_star (k in units of k_star)."""
    De = _K
    if branch == "collisional":          # single-τ Maxwell — the maximally-breaking ENDPOINT
        Gp, Gpp = De ** 2 / (1 + De ** 2), De / (1 + De ** 2)
    elif branch == "free_streaming":     # strict critical gel — scale-free by construction
        a = 0.5
        Gp, Gpp = (De ** a) * np.cos(a * np.pi / 2), (De ** a) * np.sin(a * np.pi / 2)
    else:
        raise ValueError(branch)
    return Gp / (Gp + Gpp)


def _logslope_variation(S: np.ndarray) -> float:
    sl = np.gradient(np.log(S), np.log(_K)); band = (_K > 1e-2) & (_K < 1e2)
    return float(np.std(sl[band]))


def collisional_spectrum_variation(spectrum_decades: float) -> float:
    """The P-C degeneracy, computable: support log-slope variation for a COLLISIONAL medium whose
    relaxation times span `spectrum_decades` (power-law weighted). Single-τ (0 decades) breaks;
    a broad spectrum (≳5 decades) reads SCALE-FREE — degenerate with free-streaming."""
    if spectrum_decades <= 0:
        taus, w = np.array([1.0]), np.array([1.0])
    else:
        taus = np.logspace(-spectrum_decades / 2, spectrum_decades / 2, 80); w = taus ** -0.5
    De = _K
    Gp = sum(wi * (De * t) ** 2 / (1 + (De * t) ** 2) for t, wi in zip(taus, w))
    Gpp = sum(wi * (De * t) / (1 + (De * t) ** 2) for t, wi in zip(taus, w))
    return _logslope_variation(Gp / (Gp + Gpp))


def discriminant_breaks_with_spectrum_width() -> bool:
    """True iff a broad collisional spectrum becomes SCALE-FREE (mislabeled free-streaming) — i.e.
    the binary discriminant is degenerate (P-C). This is the honest self-test: it confirms the
    contrast is NOT robust, the opposite of a passing-check that would launder it."""
    return collisional_spectrum_variation(0) > 0.05 and collisional_spectrum_variation(7) < 0.05


def open_target() -> list:
    return [
        "(a) derive/bound the collisional relaxation-spectrum width from GRUT (narrow ⇒ break; broad ⇒ degenerate)",
        "(b) derive De(k)∝k and S = structure-support from the action (currently posited ansätze)",
        "(c) full structure-formation P(k) per branch; show separability from k_eq and BAO",
        "(d) bound c_s independently (not =c) to restore two-sided falsifiability without a fit",
    ]


def status() -> dict:
    return {
        "target": "4 — toward an outward branch test (OPEN, not a falsifier)",
        "posited_contrast": "single-τ Maxwell ⇒ a characteristic-scale break; strict critical gel ⇒ "
                            "scale-free — TRUE only at the two endpoints",
        "why_not_a_test": "(P-C) degenerate — broad-spectrum collisional reads scale-free; (P-B) "
                          "one-sided (collisional unfalsifiable, k_star hides) and entangled with k_eq/BAO; "
                          "(P-D) definition-as-target, De∝k & S=support are posited; (P-A) match deferred, "
                          "the c_s=c (~near-BAO) value excised",
        "tier": "OPEN — a posited qualitative contrast, not yet a falsifier",
        "open_target": open_target(),
    }


if __name__ == "__main__":
    print("TARGET 4 — toward an outward branch test (OPEN, NOT a falsifier).\n")
    print("Posited endpoint contrast (real only at the extremes):")
    print(f"  collisional single-τ : support log-slope var = {_logslope_variation(_support_single_tau('collisional')):.3f} (break)")
    print(f"  free-streaming gel    : support log-slope var = {_logslope_variation(_support_single_tau('free_streaming')):.3f} (scale-free)")
    print("\nP-C degeneracy (a COLLISIONAL spectrum loses the break as it widens):")
    for d in (0, 1, 3, 5, 7):
        v = collisional_spectrum_variation(d)
        print(f"  spectrum width {d:2d} dec: var={v:.3f} → {'break' if v > 0.05 else 'SCALE-FREE (≡ free-streaming — degenerate)'}")
    print(f"\n  discriminant is degenerate with spectrum width? {discriminant_breaks_with_spectrum_width()}")
    print("\n  ⇒ NOT a falsifier yet. To become one, OPEN target:")
    for t in open_target():
        print(f"     {t}")
