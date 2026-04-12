"""
Neutrino Masses as Near-Zero Self-Referential Fixed Points

THE CLAIM: Neutrino masses are tiny because their constitutive fixed
point z = z_target[z] is nearly at zero. The fixed point doesn't quite
reach zero — the residual distance IS the neutrino mass.

This explains two puzzles simultaneously:
  1. WHY neutrino masses are tiny (the fixed point nearly cancels)
  2. WHY PMNS mixing is large (nearly degenerate eigenvalues mix maximally)

Comparison to quarks:
  - Quarks: well-separated eigenvalues -> small CKM mixing
  - Neutrinos: nearly degenerate (all near zero) -> large PMNS mixing

STATUS: Structural argument. The numerical values require the
neutrino target functional, which has not been computed.
"""

import numpy as np


# Observed neutrino parameters
DELTA_M21_SQ = 7.53e-5    # eV^2 (solar)
DELTA_M32_SQ = 2.453e-3   # eV^2 (atmospheric, normal ordering)
SUM_MASSES_UPPER = 0.12   # eV (Planck 2018 upper bound)

# PMNS angles (normal ordering, PDG 2022)
THETA_12 = 33.4  # degrees (solar angle)
THETA_23 = 49.0  # degrees (atmospheric, near maximal)
THETA_13 = 8.6   # degrees (reactor)

# For comparison: CKM angles
THETA_C = 13.0   # degrees (Cabibbo)


def near_zero_fixed_point_argument() -> dict:
    """Why neutrino masses are near zero.

    In the constitutive framework, each particle's mass is the eigenvalue
    of the self-referential operator at the fixed point. For charged leptons:
    the eigenvalues are well-separated (0.511 MeV, 106 MeV, 1777 MeV).

    For neutrinos: the eigenvalues are ALL close to zero (< 0.1 eV).
    This means the neutrino target functional nearly satisfies
    z_target[z] = 0 — the massless fixed point.

    The SMALL residual (< 0.1 eV / 1777 MeV ~ 10^-5 of tau mass)
    is the "distance" from perfect cancellation at the fixed point.

    WHY would the neutrino fixed point nearly cancel?
    - Neutrinos are the only fermions that can be Majorana
    - A Majorana mass mixes particle and antiparticle
    - The CTP forward/backward symmetry nearly cancels Majorana masses
    - The residual ~ (2-R_neutrino) / normalization, analogous to (2-R)/S tau_0

    This is the SEESAW in constitutive language: the heavy Majorana
    mass drives the light eigenvalue toward zero through the CTP balance.
    """
    # Ratio of largest neutrino mass to tau mass
    m_nu_max = np.sqrt(DELTA_M32_SQ)  # ~ 0.05 eV
    m_tau = 1.777e9  # eV
    suppression = m_nu_max / m_tau

    return {
        "neutrino_masses_eV": {
            "m1_upper": 0.05,
            "m2": np.sqrt(DELTA_M21_SQ),
            "m3": np.sqrt(DELTA_M32_SQ),
        },
        "suppression_vs_tau": suppression,
        "log10_suppression": np.log10(suppression),
        "fixed_point_interpretation": (
            f"Neutrino masses are suppressed by 10^{np.log10(suppression):.0f} "
            f"relative to tau. In the fixed-point picture: the neutrino "
            f"self-referential condition nearly cancels. The residual mass "
            f"is the distance from perfect cancellation."
        ),
        "seesaw_analogy": (
            "The seesaw mechanism (m_light ~ v^2 / M_heavy) has a natural "
            "constitutive interpretation: the heavy Majorana mass M_heavy is "
            "the scale at which the neutrino fixed point transitions from "
            "external-target (massive) to self-referential (nearly massless). "
            "The light mass is the residual after the CTP paths nearly cancel."
        ),
    }


def large_mixing_from_degeneracy() -> dict:
    """Why PMNS mixing is large (while CKM mixing is small).

    Eigenvalue degeneracy → large mixing. This is a standard linear algebra
    result: when two eigenvalues are nearly equal, the eigenvectors become
    sensitive to small perturbations, producing large mixing angles.

    For neutrinos: all three masses are O(0.01-0.05 eV). The ratios are:
      m2/m1 ~ O(1), m3/m2 ~ O(10)

    For quarks: m_t/m_c ~ 136, m_c/m_u ~ 577. HUGE ratios → small mixing.

    The prediction: mixing angles correlate inversely with mass ratios.
    Small ratios (degenerate) → large mixing (PMNS).
    Large ratios (hierarchical) → small mixing (CKM).
    """
    # Mass ratios for quarks (up-type)
    m_u, m_c, m_t = 0.0022, 1.27, 173.0
    quark_ratios = [m_c / m_u, m_t / m_c]
    quark_mixing = THETA_C  # Cabibbo angle ~ 13 deg

    # Mass ratios for neutrinos (using sqrt of mass-squared differences)
    m2 = np.sqrt(DELTA_M21_SQ)  # ~ 8.7 meV
    m3 = np.sqrt(DELTA_M32_SQ)  # ~ 49.5 meV
    m1 = max(0.001, m2 * 0.5)  # rough estimate for normal ordering
    nu_ratios = [m2 / m1, m3 / m2]
    nu_mixing = THETA_23  # atmospheric ~ 49 deg (near maximal)

    return {
        "quarks": {
            "mass_ratios": quark_ratios,
            "mixing_angle_deg": quark_mixing,
            "hierarchical": True,
        },
        "neutrinos": {
            "mass_ratios": nu_ratios,
            "mixing_angle_deg": nu_mixing,
            "near_degenerate": True,
        },
        "structural_prediction": (
            f"Quarks: mass ratios {quark_ratios[0]:.0f}, {quark_ratios[1]:.0f} → "
            f"Cabibbo angle {quark_mixing:.0f} deg (small). "
            f"Neutrinos: mass ratios {nu_ratios[0]:.1f}, {nu_ratios[1]:.1f} → "
            f"atmospheric angle {nu_mixing:.0f} deg (near maximal). "
            f"Degeneracy → large mixing. Hierarchy → small mixing. "
            f"This is exactly what the eigenvalue fixed-point structure predicts."
        ),
    }


def full_neutrino_fixed_point() -> dict:
    """Complete neutrino fixed-point analysis."""
    near_zero = near_zero_fixed_point_argument()
    mixing = large_mixing_from_degeneracy()

    return {
        "near_zero": near_zero,
        "mixing": mixing,
        "verdict": (
            "Neutrino masses and mixing map cleanly onto the fixed-point "
            "framework. Tiny masses = near-zero fixed point (CTP paths "
            "nearly cancel). Large PMNS mixing = eigenvalue degeneracy "
            "(all masses near zero). The seesaw mechanism is reinterpreted "
            "as the transition from external-target (massive) to "
            "self-referential (nearly massless) regime. Numerical values "
            "require the neutrino anomaly ratio R_neutrino."
        ),
    }
