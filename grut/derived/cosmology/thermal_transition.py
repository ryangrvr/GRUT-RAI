"""
Thermal Transition — T_c = 54.7 MK, the "Boiling Point of Gravity".

From v9.0 Thermodynamics of Metric Memory, with the τ-cleanup of
Correction #22 (2026-04-30) applied:

    T_c = ℏ / (τ_micro × k_B) ≈ 54.7 × 10⁶ K

where τ_micro ≈ 1.4×10⁻¹⁹ s is the microscopic plasma relaxation
time of the responsive vacuum's microstates — distinct from the
macroscopic gravitational τ_0 = 41.9 Myr by ~34 orders of magnitude.
The pre-Correction-#22 form T_c = 1/(τ_0 × k_B) was dimensionally
invalid; the value 54.7 MK is preserved exactly under the SI-correct
formula because τ_micro is defined as ℏ/(k_B × T_c) with T_c anchored
to the cosmological-chronology pin (T at t≈1 hour post-BB).

Above T_c, the vacuum is too "hot" to remember — gravitational response
is local (standard GR). Below T_c, the memory kernel activates and the
metric develops bandwidth-limited response with n_g ≈ 1.1547 at DC.

Cosmological chronology:
    t ≈ 1 s post-Big Bang:          T ~ 10⁹–10¹⁰ K, above T_c, no DM effects
    t ≈ 1 h post-Big Bang:          T ~ T_c ≈ 5.5 × 10⁷ K, transition
    t ≈ 380 kyr (recombination):    T ~ 3000 K << T_c, deep refractive regime
    t = today (13.8 Gyr):           T = 2.725 K (CMB), n_g ≈ 1.1547 fully active

This answers: "why no DM at BBN?" — because T > T_c then, and the
vacuum had no memory yet to create a DM-like refractive enhancement.

The v11 Appendix L interpretation: spacetime begins to remember mass
distributions only after it cools through T_c. Before that, there's
no memory, so no refractive index, so no DM-like effects.
"""

import numpy as np

from grut.foundation.closure_protocol import (
    T_C_KELVIN, T_C_MK, TAU_0_SEC, ALPHA_VAC, n_g_refractive,
)
from grut.foundation.constants import K_B, HBAR


# Cosmological epochs (approximate)
T_BBN_K = 1e9               # ~1 MeV, nucleosynthesis
T_MATTER_RAD_EQ_K = 8800     # z ≈ 3400 matter-rad equality
T_RECOMBINATION_K = 3000     # z ≈ 1100 recombination
T_CMB_TODAY_K = 2.725        # today


def in_memory_regime(T_Kelvin):
    """True if T < T_c, i.e., the vacuum is in the viscoelastic regime.

    This is a step-function approximation. The transition at T = T_c is
    not sharp; see phase_transition_smoothness() for a more realistic
    sigmoid.
    """
    return T_Kelvin < T_C_KELVIN


def memory_activation_fraction(T_Kelvin, width=0.3):
    """Smooth activation f(T) ∈ [0, 1] across T_c.

    At T ≫ T_c: f → 0 (no memory, local GR).
    At T ≪ T_c: f → 1 (full memory, refractive regime).
    At T = T_c: f = 0.5.

    Uses sigmoid in ln(T_c/T) with characteristic width.
    """
    if T_Kelvin <= 0:
        return 1.0
    x = np.log(T_C_KELVIN / T_Kelvin) / width
    return 1.0 / (1.0 + np.exp(-x))


def effective_n_g_with_thermal(omega_Hz, T_Kelvin,
                                alpha=ALPHA_VAC, tau_0_sec=TAU_0_SEC):
    """Refractive index with thermal activation factor.

        n_g²(ω, T) = 1 + f(T) × α/(1+(ωτ_0)²)

    where f(T) is the memory activation fraction. At T > T_c the
    enhancement vanishes; at T < T_c it reaches the full α value.
    """
    f = memory_activation_fraction(T_Kelvin)
    return np.sqrt(1.0 + f * alpha / (1.0 + (omega_Hz * tau_0_sec)**2))


def cosmological_chronology():
    """Report the refractive enhancement at canonical cosmological epochs."""
    epochs = [
        ("plasma_era_BBN",           T_BBN_K,              "t ≈ 1 s"),
        ("T_c_transition",           T_C_KELVIN,           "t ≈ 1 hour"),
        ("matter_rad_equality",      T_MATTER_RAD_EQ_K,    "t ≈ 50 kyr"),
        ("recombination",            T_RECOMBINATION_K,    "t ≈ 380 kyr"),
        ("CMB_today",                T_CMB_TODAY_K,        "t ≈ 13.8 Gyr"),
    ]
    out = {}
    for name, T, age in epochs:
        f = memory_activation_fraction(T)
        # Enhancement at DC (cosmic scale), assuming long-wavelength modes
        enhancement_DC = f * ALPHA_VAC
        out[name] = {
            "T_K":                   T,
            "T_over_T_c":            T / T_C_KELVIN,
            "age":                   age,
            "memory_activation_f":   f,
            "enhancement_DC":        enhancement_DC,
            "in_memory_regime":      T < T_C_KELVIN,
        }
    return out


def verify():
    """Self-test thermal transition."""
    checks = {
        "T_c_is_54p7_MK":           abs(T_C_MK - 54.7) / 54.7 < 0.05,
        "BBN_above_T_c":            T_BBN_K > T_C_KELVIN,
        "recombination_below_T_c":  T_RECOMBINATION_K < T_C_KELVIN,
        "CMB_today_below_T_c":      T_CMB_TODAY_K < T_C_KELVIN,
        "activation_sigmoid_at_Tc": abs(memory_activation_fraction(T_C_KELVIN) - 0.5) < 0.01,
        "activation_full_at_CMB":   memory_activation_fraction(T_CMB_TODAY_K) > 0.99,
        "activation_zero_at_BBN":   memory_activation_fraction(T_BBN_K) < 0.01,
    }
    return checks


if __name__ == "__main__":
    import json
    from grut.foundation.closure_protocol import TAU_MICRO_SEC
    print(f"T_c = {T_C_MK:.2f} × 10⁶ K = ℏ/(τ_micro × k_B), SI-correct (Correction #22)")
    print(f"τ_0     = {TAU_0_SEC / (3.156e7 * 1e6):.2f} Myr        (gravitational sector)")
    print(f"τ_micro = {TAU_MICRO_SEC:.3e} s    (thermal sector — sets T_c)")
    print()
    print("Cosmological chronology:")
    print(json.dumps(cosmological_chronology(), indent=2, default=str))
    print()
    print("Verify:")
    for k, v in verify().items():
        print(f"  {'✓' if v else '✗'} {k}")
