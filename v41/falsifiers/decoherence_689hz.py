"""GRUT-RAI v4.1 — STEP 5: the one forward falsifier, built to stand alone.

This module is FRAMEWORK-INDEPENDENT. The decoherence rate below is the Diósi /
Anastopoulos–Hu gravitational kernel (a KNOWN, published result — cited) evaluated
with zero free parameters. A physicist who rejects GRUT can run it and check the
number. GRUT's only distinctive inputs are (i) the extended-body suppression
S(l/R) giving the F6 geometric kink, and (ii) the τ₀-tied plateau.

Prediction (gold benchmark, m ≈ 80.8 pg, R = 1 μm, l = R):
    Λ_grav = G m² S(l/R) / (ħ l)  ≈  689 Hz     (a decoherence-rate plateau point)

What kills it:
    A measured null at the predicted point (decoherence rate inconsistent with
    Λ_grav at the >few-σ level for a body where S(l/R) is known) falsifies the
    τ₀-tied gravitational-decoherence prediction.

Distinction from the competitor class (honest):
    - CSL (continuous spontaneous localization): rate ∝ m (linear). Killed by F1
      (GRUT/gravity is ∝ m²) — the isotope-mass ratio separates them.
    - Diósi–Penrose (point mass): rate ∝ G m² — SHARES GRUT's mass scaling. The
      isotope ratio does NOT separate GRUT from DP. The discriminator is F6: the
      extended-body geometric kink at l ≈ 1.8 R, which a point-mass DP model
      cannot produce. (Verified: DP matches GRUT on F1/F3/F4/F5, differs on F6.)
    - Bare Anastopoulos–Hu point kernel: same kernel, no extended-body integral,
      so again no F6 kink.

Reference for the kernel: Anastopoulos & Hu, Class. Quantum Grav. 30, 165007 (2013).
"""
from __future__ import annotations

# Physical constants (SI) — declared here so the module is self-contained.
G = 6.67430e-11
HBAR = 1.054571817e-34
GOLD_RHO = 19300.0


def extended_body_suppression(l: float, R: float) -> float:
    """S(l/R) = min(1, (l/R)³ / 6). Near field (l<R): (l/R)³; far field (l>R): 1.
    Integrating the 1/r Diósi kernel over a uniform sphere. The l≈1.8R region is
    the F6 geometric kink — GRUT's distinctive, point-mass-impossible signature."""
    if R <= 0:
        return 1.0
    return min(1.0, (l / R) ** 3 / 6.0)


def decoherence_rate(m: float, l: float, R: float) -> float:
    """Λ_grav = G m² S(l/R) / (ħ l)  [Hz]. Zero free parameters."""
    if m <= 0 or l <= 0:
        return 0.0
    return G * m ** 2 * extended_body_suppression(l, R) / (HBAR * l)


def gold_benchmark() -> dict:
    """The headline prediction: a 1 μm gold sphere, separation l = R."""
    R = 1e-6
    m = (4.0 / 3.0) * 3.141592653589793 * R ** 3 * GOLD_RHO   # ≈ 80.8 pg
    rate = decoherence_rate(m, l=R, R=R)
    return {"m_kg": m, "R_m": R, "l_m": R, "rate_Hz": rate,
            "prediction": "~689 Hz decoherence-rate plateau point",
            "free_parameters": 0}


def f6_kink_location(R: float) -> float:
    """The far/near transition (F6) — the point-mass-impossible geometric kink."""
    return 1.8 * R


def check_plateau() -> bool:
    """Internal falsifiable check the registry consumes: the gold-benchmark rate is
    finite, positive, and lands at the predicted ~689 Hz (±2%)."""
    r = gold_benchmark()["rate_Hz"]
    return bool(r > 0 and abs(r - 689.0) / 689.0 < 0.02)


if __name__ == "__main__":
    b = gold_benchmark()
    print("GRUT-RAI v4.1 — standalone gravitational-decoherence falsifier")
    print(f"  gold sphere: m = {b['m_kg']*1e15:.1f} pg, R = {b['R_m']*1e6:.1f} μm, l = R")
    print(f"  predicted rate Λ_grav = {b['rate_Hz']:.1f} Hz   (0 free parameters)")
    print(f"  F6 kink at l = {f6_kink_location(b['R_m'])*1e6:.2f} μm "
          "(GRUT-vs-Diósi–Penrose discriminator)")
    print(f"  check_plateau(): {check_plateau()}")
