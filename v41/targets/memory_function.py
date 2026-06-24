"""GRUT-RAI v4.1 — TARGET 1: K̃(ω) from the bath. The integral that decides single-pole-ness.

K(t) = ⟨F(0)F(t)⟩/⟨|z|²⟩ is the memory function of the responsive vacuum (F = the
orthogonal/fast Mori–Zwanzig force on the slow TT-shear variable z). Its decay time
τ_K is the whole question:
    FAST tail (τ_K < τ₀/4): single-pole-ness becomes a THEOREM of {Q + bath spectrum}.
    SLOW tail (τ_K ≳ τ₀/4): a dark-capable second pole reappears INSIDE F(t).
Either outcome is decisive. There is no run that wastes effort.

THE ANTI-CIRCULARITY RULE (the v4 sin, FORBIDDEN here): v4 hard-coded τ_K = τ_micro and
called the fast tail "by construction." That made the premise equal the conclusion.
Here τ_K is COMPUTED from the bath spectral density J(ω); it is NEVER set to τ_micro by
assertion. If J(ω) is not supplied, the module RAISES and names the missing object.

WHAT THIS MODULE ESTABLISHES (outcome (b) — the gap is one level deeper, now pinned):
  The reduction K(t) ← J(ω) is the standard open-systems / Caldeira–Leggett route
  (Anastopoulos–Hu lineage; KNOWN-REUSED). It is COMPUTED here:
       γ(t) = (2/π) ∫₀^∞ [J(ω)/ω] cos(ωt) dω,     τ_K = (1/e decay time of γ).
  Verified analytic anchor: Ohmic–Drude J(ω)=ηω/(1+(ω/Ω_c)²) ⇒ γ(t)=ηΩ_c e^{−Ω_c t},
  so τ_K = 1/Ω_c. The verdict therefore reduces to ONE property of J(ω): does it carry
  spectral weight below ~4/τ₀?  fast iff bandwidth Ω_c ≳ 4/τ₀; slow otherwise.
  GRUT's CTP action fixes the FDT relation (noise↔dissipation) and the 1/r spatial
  kernel — but it does NOT derive the SPECTRAL bandwidth of F(t). That J(ω) is the
  missing object. v4's τ_K=τ_micro is the special case "Ohmic–Drude, cutoff 1/τ_micro"
  — an ASSUMED broadband bath, i.e. the single-pole conclusion wearing an input's clothes.

CAVEAT: the reduction here is FLAT-SPACE and IR-blind (standard open-systems kernel).
The qualitative decider (J's low-ω weight) is robust; the precise J(ω) and any
curved-space/IR correction are unspecified. Provisional on the curved-space version.
"""
from __future__ import annotations

from typing import Callable
import numpy as np

OFF_AXIS_THRESHOLD_FACTOR = 0.25   # poles go off-axis (dark-capable) iff τ_K > τ₀/4


# ── given τ_K, the pole structure is COMPUTABLE (the "back half" of the reduction) ──
def poles_second_level(tau0: float, tauK: float):
    """χ ∝ (1−iωτ_K)/(1 − iωτ₀ − ω²·τ₀τ_K); returns the denominator roots (poles)."""
    return np.roots([-(tau0 * tauK), -1j * tau0, 1.0])


def verdict(tauK: float, tau0: float) -> str:
    return "FAST (single-pole)" if tauK < OFF_AXIS_THRESHOLD_FACTOR * tau0 else "SLOW (dark pole in F(t))"


# ── given J(ω), τ_K is COMPUTED (the "front half" — the new content) ────────────────
def memory_kernel_from_J(J: Callable[[np.ndarray], np.ndarray], t: np.ndarray,
                         wmax: float, n: int = 40000) -> np.ndarray:
    """γ(t) = (2/π) ∫₀^∞ [J(ω)/ω] cos(ωt) dω. The Caldeira–Leggett / Anastopoulos–Hu
    friction (memory) kernel from a bath spectral density J(ω). KNOWN-REUSED machinery."""
    w = np.linspace(1e-6, wmax, n)
    Jw = J(w) / w
    return (2.0 / np.pi) * np.array([np.trapezoid(Jw * np.cos(ti * w), w) for ti in t])


def tau_K_from_J(J: Callable[[np.ndarray], np.ndarray], omega_scale: float,
                 t_span: float = 12.0) -> float:
    """COMPUTE τ_K = the 1/e decay time of γ(t), from a given spectral density J(ω).
    omega_scale sets the integration/grid scale (the bath's characteristic frequency)."""
    t = np.linspace(0.0, t_span / omega_scale, 600)
    g = memory_kernel_from_J(J, t, wmax=400.0 * omega_scale)
    g = g / g[0]
    below = np.where(g <= np.exp(-1))[0]
    if below.size == 0:
        return float(t[-1])          # did not decay within the window → very slow
    return float(t[below[0]])


def ohmic_drude_J(eta: float = 1.0, Omega_c: float = 1.0) -> Callable[[np.ndarray], np.ndarray]:
    """An ILLUSTRATIVE bath: Ohmic with a Drude cutoff Ω_c. (Used to exhibit the
    reduction; NOT claimed to be GRUT's bath — that is the open question.)"""
    return lambda w: eta * w / (1.0 + (w / Omega_c) ** 2)


def reduction_demo(tau0: float = 1.0):
    """Exhibit the COMPUTED reduction: τ_K (hence fast/slow) is a functional of J(ω).
    Same machinery, three baths — the verdict flips with the bath bandwidth."""
    out = []
    for Oc in (100.0 / tau0, 4.0 / tau0, 0.1 / tau0):
        tauK = tau_K_from_J(ohmic_drude_J(Omega_c=Oc), omega_scale=Oc)
        out.append({"Omega_c": Oc, "tau_K": tauK, "verdict": verdict(tauK, tau0)})
    return out


# ── the GRUT-specific input that is MISSING (the honest raise, outcome (b)) ─────────
def grut_bath_spectral_density(*_a, **_k):
    """RAISE. GRUT's CTP action fixes the FDT relation and the 1/r spatial kernel, but
    does NOT derive J(ω) — the spectral density of the TT-shear orthogonal force, and in
    particular whether it carries weight below ~4/τ₀. That is the missing object. Refusing
    to assume it (v4 assumed Ohmic–Drude, cutoff 1/τ_micro) is the point."""
    raise NotImplementedError(
        "single-pole-ness is UNDECIDABLE until GRUT specifies J(ω) for the TT-shear bath. "
        "Given J(ω), this module computes τ_K and the fast/slow verdict (see reduction_demo). "
        "The missing input: prove J(ω) has no spectral weight below ~4/τ₀ (the white-noise / "
        "broadband property F(t) is POSITED but not derived). v4 assumed Ohmic–Drude with "
        "cutoff 1/τ_micro — which IS the single-pole conclusion; do not repeat it."
    )


def compute_tauK_from_bath(*a, **k):
    """Alias for the honest entry point: deriving τ_K from GRUT's actual content raises,
    because J(ω) is unspecified."""
    return grut_bath_spectral_density(*a, **k)


def status() -> dict:
    return {
        "target": "K̃(ω) from the bath",
        "state": "OPEN",
        "outcome": "(b) — reduction COMPUTED; the gap is one level deeper, now pinned",
        "computed": "τ_K = 1/e decay of γ(t)=(2/π)∫(J/ω)cosωt dω; verdict reduces to J's "
                    "spectral weight below ~4/τ₀ (Ohmic–Drude anchor: τ_K=1/Ω_c, verified)",
        "missing_input": "J(ω) for the TT-shear bath — its low-frequency structure. GRUT "
                         "supplies the FDT relation + 1/r kernel, NOT the spectral bandwidth.",
        "sharpened_target": "specify J(ω); prove no spectral weight below ~4/τ₀ "
                            "(⇒ fast ⇒ single-pole theorem) or exhibit it (⇒ slow ⇒ dark pole in F(t))",
        "caveat": "flat-space, IR-blind reduction; provisional on the curved-space version",
        "v4_sin_exposed": "τ_K=τ_micro ≡ assuming Ohmic–Drude with cutoff 1/τ_micro (broadband) "
                          "— an assumed J(ω), i.e. the conclusion as an input",
    }


if __name__ == "__main__":
    print("TARGET 1 — K̃(ω): the reduction is COMPUTED; J(ω) is the missing input.\n")
    print("Reduction demo (τ₀=1; the SAME machinery, three baths — verdict flips with J):")
    for r in reduction_demo():
        print(f"   Ω_c={r['Omega_c']:>7.3g}  τ_K={r['tau_K']:.4g}  →  {r['verdict']}")
    print("\nDeriving τ_K from GRUT's actual content:")
    try:
        grut_bath_spectral_density()
    except NotImplementedError as e:
        print("   RAISE:", e)
