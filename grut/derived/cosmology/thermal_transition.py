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
to the cosmological-chronology pin (T at t≈16 hours post-BB).

Above T_c, the vacuum is too "hot" to remember — gravitational response
is local (standard GR). Below T_c, the memory kernel activates and the
metric develops bandwidth-limited response with n_g ≈ 1.1547 at DC.

Cosmological chronology:
    t ≈ 1 s post-Big Bang:          T ~ 10⁹–10¹⁰ K, above T_c, no DM effects
    t ≈ 16 h post-Big Bang:         T ~ T_c ≈ 5.5 × 10⁷ K, transition
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
    not sharp; memory_activation_fraction() gives the derived finite-T
    Mori–Zwanzig profile f(T) = tanh(T_c/2T).
    """
    return T_Kelvin < T_C_KELVIN


def memory_activation_fraction(T_Kelvin):
    """Finite-T memory-activation fraction f(T) ∈ (0, 1], from the
    finite-temperature Mori–Zwanzig kernel — replaces the former ad-hoc sigmoid.
    HONEST TIER (adversarially checked): the functional SHAPE follows from Q's
    FDT/KMS structure GIVEN one physical identification — it is NOT a fully
    parameter-free theorem; it trades the sigmoid's free width for a well-motivated
    identification.

    Memory (the coherent single-pole response) survives to the extent that the
    microscopic bath at ω_micro = 1/τ_micro is QUANTUM-coherent rather than
    thermally re-randomized. The FDT/KMS factor splits the bath fluctuation into
    a zero-point (coherent) and a thermal part:
        coth(ℏω/2k_BT) = 1 + 2n(ω,T),   n = Bose occupation.
    The activation = the coherent (zero-point) FRACTION at the micro scale:
        f(T) = 1/coth(ℏω_micro/2k_BT) = tanh(T_c/2T),   k_B T_c ≡ ℏ/τ_micro.
    STRONGEST SUPPORT: this is exactly GRUT's own T=0/finite-T noise ratio,
    f(T) = N(ω_micro, 0) / N(ω_micro, T) with N = noise_kernel.fdt_noise — not an
    imported formula. CAVEATS: (i) "activation = zero-point fraction" is a
    well-motivated identification, not forced by FDT alone (the complement 1−tanh,
    or a τ-ratio T_c/2πT, are a-priori alternatives); (ii) evaluated at the single
    micro scale ω_micro (faithful to GRUT's single-pole/single-τ_micro structure;
    a full bath spectral density would shift f(T_c) and the tail prefactor, not the
    qualitative 1/T tail).

    Limits: T ≪ T_c ⇒ f → 1 (full memory); T ≫ T_c ⇒ f → T_c/2T — a POWER-LAW
    1/T tail from classical equipartition, NOT the sigmoid's exponential cutoff;
    f(T_c) = tanh(½) = 0.4621 (a derived value, not the ad-hoc 0.5). The 1/T
    tail leaves a small residual activation at T > T_c, but the physical memory
    EFFECT f·α/(1+(ωτ_0)²) is bandwidth-protected: early-universe dynamics have
    ωτ_0 ≫ 1, so the residual is suppressed by ~1/(ωτ_0)² and is negligible
    (e.g. at BBN). See effective_n_g_with_thermal.
    """
    if T_Kelvin <= 0:
        return 1.0
    return float(np.tanh(T_C_KELVIN / (2.0 * T_Kelvin)))


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
        ("T_c_transition",           T_C_KELVIN,           "t ≈ 16 hours"),
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
    """Self-test thermal transition (derived finite-T Mori–Zwanzig activation)."""
    import math
    # The physical memory EFFECT at BBN is bandwidth-protected: a BBN-dynamical
    # frequency (ω ~ 1/t_BBN, here 1 Hz) has ωτ_0 ≫ 1, so n_g → 1 regardless of
    # the f(T) power-law tail.
    n_g_bbn = effective_n_g_with_thermal(1.0, T_BBN_K)
    checks = {
        "T_c_is_54p7_MK":            abs(T_C_MK - 54.7) / 54.7 < 0.05,
        "BBN_above_T_c":             T_BBN_K > T_C_KELVIN,
        "recombination_below_T_c":   T_RECOMBINATION_K < T_C_KELVIN,
        "CMB_today_below_T_c":       T_CMB_TODAY_K < T_C_KELVIN,
        # DERIVED value at T_c is tanh(½), NOT the ad-hoc sigmoid's 0.5
        "activation_at_Tc_is_tanh_half": abs(memory_activation_fraction(T_C_KELVIN) - math.tanh(0.5)) < 1e-9,
        "activation_full_at_CMB":    memory_activation_fraction(T_CMB_TODAY_K) > 0.99,
        # high-T behaviour is a POWER-LAW 1/T tail (tanh asymptote T_c/2T), not <0.01
        "activation_power_law_tail": abs(memory_activation_fraction(T_BBN_K) - T_C_KELVIN / (2 * T_BBN_K)) < 1e-3,
        # but the memory EFFECT at BBN is bandwidth-protected → n_g ≈ 1
        "bbn_effect_bandwidth_protected": abs(n_g_bbn - 1.0) < 1e-9,
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
