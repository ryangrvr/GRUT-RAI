"""
Stochastic Gravity from CTP — Direction 1

The Einstein-Langevin equation with GRUT noise kernel:

  ⟨G_μν⟩ + τ_grav D_t ⟨G_μν⟩ = 8πG ⟨T_μν⟩ + ξ_μν

where ξ_μν is stochastic noise with correlator from the CTP influence functional.
The noise kernel N_μναβ(x,y) is the Hadamard function of the stress tensor.

GRUT modification: the constitutive τ changes the retarded propagator,
which modifies the noise kernel at high frequencies.

KEY RESULT: The stochastic decoherence rate from metric fluctuations is
subdominant to Sector 3's Diósi rate. The USL remains the dominant channel.

STATUS: Scaffolded. Connects to Sector 3. Direction 1 is automatically
consistent from CTP axiom (zero new structure needed).
"""

import numpy as np
from grut_solver.constants import G, HBAR, C, K_B, T_PLANCK, TAU_I, L_PLANCK


def noise_kernel_flat_scalar(f_hz: np.ndarray, T_K: float = 2.725,
                             tau_grav: float = 0.0) -> dict:
    """Noise kernel N(ω) for a thermal scalar field in flat space.

    Standard (Hu-Verdaguer):
      N(ω) ~ ω⁴ × coth(ℏω / 2k_BT)

    GRUT-modified:
      N_grut(ω) = N(ω) / |1 + iωτ_grav|²

    The constitutive τ suppresses the noise at high frequencies
    (ω >> 1/τ_grav), acting as a UV regulator.
    """
    omega = 2 * np.pi * f_hz
    hbar_omega_over_2kT = HBAR * omega / (2 * K_B * T_K)

    # Standard noise kernel (dimensionless shape)
    # Handle overflow in coth for large arguments
    coth = np.where(hbar_omega_over_2kT < 500,
                    1.0 / np.tanh(np.maximum(hbar_omega_over_2kT, 1e-30)),
                    1.0)
    N_standard = omega**4 * coth

    # GRUT modification
    if tau_grav > 0:
        omega_tau = omega * tau_grav
        suppression = 1.0 / (1 + omega_tau**2)
        N_grut = N_standard * suppression
    else:
        N_grut = N_standard.copy()
        suppression = np.ones_like(omega)

    return {
        "f_hz": f_hz.tolist(),
        "N_standard": N_standard.tolist(),
        "N_grut": N_grut.tolist(),
        "suppression_factor": suppression.tolist() if hasattr(suppression, 'tolist') else [float(suppression)],
        "tau_grav_s": tau_grav,
        "T_K": T_K,
        "uv_regulated": tau_grav > 0,
    }


def metric_fluctuation_spectrum(f_hz: np.ndarray, T_K: float = 2.725,
                                tau_grav: float = 0.0) -> dict:
    """Metric fluctuation power spectrum from stochastic gravity.

    ⟨δg²⟩(ω) ~ (G/c⁴)² × N(ω) / ω⁴

    The G/c⁴ factor comes from the Einstein equation: δg ~ G δT / c⁴.
    """
    nk = noise_kernel_flat_scalar(f_hz, T_K, tau_grav)
    omega = 2 * np.pi * f_hz

    prefactor = (G / C**4)**2

    N_std = np.array(nk["N_standard"])
    N_grut = np.array(nk["N_grut"])

    # δg² ~ prefactor × N/ω⁴ = prefactor × coth(ℏω/2kT)
    delta_g2_standard = prefactor * N_std / np.maximum(omega**4, 1e-200)
    delta_g2_grut = prefactor * N_grut / np.maximum(omega**4, 1e-200)

    return {
        "f_hz": f_hz.tolist(),
        "delta_g2_standard": delta_g2_standard.tolist(),
        "delta_g2_grut": delta_g2_grut.tolist(),
        "prefactor_G_c4_squared": prefactor,
        "max_strain_standard": float(np.sqrt(np.max(delta_g2_standard))),
        "max_strain_grut": float(np.sqrt(np.max(delta_g2_grut))),
    }


def stochastic_decoherence_rate(m: float, l: float, T_K: float = 300.0,
                                tau_grav: float = 0.0) -> dict:
    """Decoherence rate from stochastic metric fluctuations.

    The stochastic gravity contribution to decoherence comes from
    integrating the metric fluctuation spectrum over the object's
    response function.

    Compare to Sector 3's USL: Λ_Diósi = Gm²/(ℏl)

    The stochastic contribution is typically much smaller because
    it involves an additional factor of (G/c⁴)² from the metric response.
    """
    from grut_solver.usl.gravitational import lambda_grav

    # Diósi rate (Sector 3)
    Lg = lambda_grav(m, l)

    # Stochastic gravity rate (order of magnitude)
    # Λ_stoch ~ (G²/c⁸) × (kT)⁴ / ℏ⁵ × m² l² / c⁴
    # This is the integral of ⟨δg²⟩ × (object response)
    # The dominant contribution comes from thermal frequencies ω ~ kT/ℏ
    omega_T = K_B * T_K / HBAR
    N_thermal = omega_T**4  # approximate noise kernel at thermal frequency

    # Metric fluctuation at thermal frequency
    delta_g2 = (G / C**4)**2 * N_thermal / omega_T**4  # = (G/c⁴)²

    # Decoherence rate: Λ ~ delta_g² × (m c² l / ℏ)² × ω_T
    # (phase accumulation rate from metric fluctuations)
    Lambda_stoch = delta_g2 * (m * C**2 * l / HBAR)**2 * omega_T

    ratio = Lambda_stoch / Lg if Lg > 0 else 0

    return {
        "m_kg": m,
        "l_m": l,
        "T_K": T_K,
        "lambda_diosi_hz": Lg,
        "lambda_stochastic_hz": Lambda_stoch,
        "ratio_stoch_to_diosi": ratio,
        "log10_ratio": np.log10(ratio) if ratio > 0 else float('-inf'),
        "dominant_channel": "Diósi (Sector 3)" if ratio < 1 else "Stochastic",
        "note": (
            f"Stochastic gravity decoherence: {Lambda_stoch:.2e} Hz. "
            f"Diósi (Sector 3): {Lg:.2e} Hz. "
            f"Ratio: {ratio:.2e}. "
            f"Diósi dominates by {-np.log10(ratio):.0f} orders. "
            f"Stochastic metric fluctuations are subdominant."
        ),
    }


def hu_verdaguer_comparison() -> dict:
    """Compare GRUT's stochastic gravity to the Hu-Verdaguer program."""
    return {
        "common_elements": [
            "CTP (Schwinger-Keldysh) formalism as foundation",
            "Einstein-Langevin equation as semiclassical limit",
            "Noise kernel from stress-energy fluctuations",
            "Stochastic metric as c-number (not operator)",
            "FDT-consistent noise-dissipation relation",
        ],
        "grut_specific": [
            "Constitutive τ modifies the retarded propagator",
            "Noise kernel UV-regulated by 1/(1 + ω²τ²) factor",
            "Direct connection to USL decoherence rate (same CTP origin)",
            "Projected dissipative term (Israel-Stewart type) for metric",
            "τ_I = ℏ/2 as universal relaxation parameter",
        ],
        "differences": [
            "Hu-Verdaguer: τ is environment-specific (bath spectral density)",
            "GRUT: τ is universal (same for all sectors)",
            "Hu-Verdaguer: no constitutive equation for metric itself",
            "GRUT: metric satisfies constitutive equation (Direction 2)",
            "Hu-Verdaguer: noise kernel computed case-by-case",
            "GRUT: noise kernel follows from universal CTP action",
        ],
    }


def directions_comparison() -> dict:
    """Head-to-head comparison of Direction 1 vs Direction 2."""
    return {
        "direction_1": {
            "name": "Stochastic Gravity (Einstein-Langevin)",
            "difficulty": "Low (uses existing CTP infrastructure)",
            "new_ingredients": "None (CTP axiom already contains everything)",
            "consistency": "Automatic (CTP preserves conservation)",
            "predictions": [
                "Stochastic metric fluctuation spectrum",
                "Spacetime decoherence corrections",
                "Primordial metric noise (CMB imprint)",
            ],
            "link_to_usl": "Direct (same noise kernel)",
            "cosmological_impact": "Gentle (sub-percent corrections to H(z))",
            "risk": "Very low",
        },
        "direction_2": {
            "name": "Constitutive Gravity (Dissipative Einstein)",
            "difficulty": "Medium (required transverse projector fix)",
            "new_ingredients": "Transverse projector P_μν^αβ, preferred direction u^μ",
            "consistency": "Achieved (projector verified symbolically)",
            "predictions": [
                "Frequency-dependent GW propagation",
                "Modified BH ringdown (QNM shift)",
                "Singularity regularization (H bounded)",
                "Gravitational wave memory modification",
            ],
            "link_to_usl": "Indirect (via τ_grav)",
            "cosmological_impact": (
                "Negligible at canonical τ₀ = 41.9 Myr (τ_grav H₀ = 0.003). "
                "Viable with phenomenological τ but does not close the DE gate."
            ),
            "risk": "Low (projector fixed)",
        },
        "complementarity": (
            "The two directions are complementary, not competing. "
            "Direction 1 provides the noise (quantum fluctuations of matter). "
            "Direction 2 provides the dissipation (metric memory). "
            "Together they form a complete noise-dissipation pair, "
            "consistent with the FDT from Axiom A0."
        ),
        "cosmological_gate_status": (
            "Both directions are mathematically consistent and produce "
            "late-time modifications. With canonical τ₀ = 41.9 Myr, "
            "the corrections are sub-percent — the cosmological gate "
            "remains open for dark energy. The memory kernel works "
            "beautifully at decoherence/galactic scales but is "
            "suppressed on cosmic expansion scales."
        ),
    }
