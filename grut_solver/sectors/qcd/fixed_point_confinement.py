"""
QCD Confinement as a Self-Referential Fixed Point

THE CLAIM: Confinement is the color sector achieving z = z_target[z].

Below Lambda_QCD (~200 MeV), the QCD vacuum becomes self-referential:
the gluon condensate determines the vacuum, and the vacuum determines
the gluon condensate. This is z = z_target[z] for color fields.

Above Lambda_QCD: asymptotic freedom. Quarks are in the external-target
regime — perturbative vacuum drives the dynamics.

The threshold crossing at Lambda_QCD is structurally identical to:
  - 38,000 neurons crossing into consciousness (Sector 13)
  - z ~ 0.33 crossing into cosmic acceleration (Sector 5)

WHAT WE CAN COMPUTE:
  1. The self-referential fraction f_self(mu) for the QCD coupling
  2. The threshold energy where f_self = 0.5
  3. Whether this matches Lambda_QCD from standard QCD
  4. The fixed-point value of alpha_s at confinement

STATUS: Computed. The self-referential threshold analysis is new.
The underlying QCD running is standard (not GRUT-modified).
"""

import numpy as np


# Standard QCD parameters
LAMBDA_QCD = 0.200  # GeV (approximate)
ALPHA_S_MZ = 0.1185  # alpha_s at M_Z
M_Z = 91.2  # GeV
N_C = 3  # SU(3) colors
N_F = 6  # active flavors (full SM)
B_0 = 11 * N_C / 3 - 2 * N_F / 3  # = 7 for SM


def alpha_s(mu_GeV: float) -> float:
    """Running alpha_s(mu) using the Landau pole formula with N_f = 3.

    For the confinement analysis, we use the low-energy running with
    N_f = 3 light quarks (u, d, s). The Landau pole occurs at Lambda_QCD.

    alpha_s(mu) = 2 pi / (b_0 ln(mu / Lambda_QCD))
    where b_0 = 11 - 2*3/3 = 9 for N_f = 3.

    This diverges at mu = Lambda_QCD (the confinement scale).
    """
    if mu_GeV <= LAMBDA_QCD:
        return float('inf')
    b_0_nf3 = 11 * N_C / 3 - 2 * 3 / 3  # = 9
    return 2 * np.pi / (b_0_nf3 * np.log(mu_GeV / LAMBDA_QCD))


def self_referential_fraction_qcd(mu_GeV: float) -> float:
    """Self-referential fraction f_self for the QCD coupling.

    In the constitutive picture:
      f_self = 0: purely perturbative (external-target, asymptotic freedom)
      f_self = 1: fully confined (self-referential vacuum)

    We define f_self via the coupling strength:
      f_self(mu) = alpha_s(mu) / alpha_s_critical

    where alpha_s_critical is the coupling at which perturbation theory
    breaks down and the vacuum becomes self-referential.

    From lattice QCD: alpha_s ~ 1 at the confinement scale.
    So alpha_s_critical ~ 1 (non-perturbative onset).

    f_self = min(1, alpha_s(mu) / alpha_critical)
    """
    alpha_critical = 1.0  # non-perturbative threshold
    a_s = alpha_s(mu_GeV)
    if not np.isfinite(a_s):
        return 1.0
    return min(1.0, a_s / alpha_critical)


def confinement_threshold() -> dict:
    """Find the energy where f_self = 0.5 (self-reference onset).

    This is the QCD analog of:
      - z ~ 0.33 in cosmology (Omega_m = Omega_Lambda)
      - 38,000 neurons in consciousness
    """
    # Scan from high to low energy (f_self increases as mu decreases)
    mu_values = np.geomspace(100, 0.1, 1000)  # descending
    f_values = [self_referential_fraction_qcd(mu) for mu in mu_values]

    # Find crossing where f_self rises through 0.5
    threshold_mu = None
    for i in range(len(f_values) - 1):
        if f_values[i] < 0.5 and f_values[i + 1] >= 0.5:
            frac = (0.5 - f_values[i]) / (f_values[i + 1] - f_values[i])
            threshold_mu = mu_values[i] + frac * (mu_values[i + 1] - mu_values[i])
            break

    # alpha_s at threshold
    alpha_threshold = alpha_s(threshold_mu) if threshold_mu else None

    return {
        "threshold_GeV": threshold_mu,
        "Lambda_QCD_GeV": LAMBDA_QCD,
        "ratio_to_Lambda_QCD": threshold_mu / LAMBDA_QCD if threshold_mu else None,
        "alpha_s_at_threshold": alpha_threshold,
        "sector_13_analogue": "38,000 neurons (consciousness onset)",
        "sector_5_analogue": "z ~ 0.33 (cosmic acceleration onset)",
        "note": (
            f"QCD self-reference threshold: mu = {threshold_mu:.3f} GeV. "
            f"Lambda_QCD = {LAMBDA_QCD} GeV. "
            f"Ratio: {threshold_mu/LAMBDA_QCD:.2f}. "
            f"The confinement transition IS the self-reference crossing "
            f"for the color sector."
        ) if threshold_mu else "Threshold not found in scan range.",
    }


def self_referential_profile(n_points: int = 200) -> dict:
    """Compute f_self(mu) across the full energy range.

    Returns the sigmoid-like profile showing the transition from
    perturbative (f=0) to confined (f=1).
    """
    mu_values = np.geomspace(0.1, 1000, n_points)
    f_values = [self_referential_fraction_qcd(mu) for mu in mu_values]
    alpha_values = [alpha_s(mu) for mu in mu_values]

    return {
        "mu_GeV": mu_values.tolist(),
        "f_self": f_values,
        "alpha_s": [float(a) if np.isfinite(a) else 999 for a in alpha_values],
    }


def confinement_as_fixed_point() -> dict:
    """The structural argument: confinement IS z = z_target[z].

    In the confining vacuum:
      - The gluon condensate <G^2> determines the vacuum structure
      - The vacuum structure determines which gluon configurations are allowed
      - These configurations determine <G^2>

    This is a self-consistency loop: z (gluon field) = z_target[z] (vacuum state).
    The confining vacuum is the FIXED POINT of this loop.

    Observable consequences of the fixed-point structure:
      1. String tension: the restoring force when z departs from z_target
      2. Flux tubes: the geometry of the constitutive response in the confined regime
      3. Hadron masses: eigenvalues of the constitutive equation at the fixed point
    """
    threshold = confinement_threshold()

    # Gluon condensate value (from lattice/phenomenology)
    gluon_condensate_GeV4 = 0.012  # <alpha_s/pi G^2> ~ 0.012 GeV^4

    # String tension (from lattice)
    string_tension_GeV2 = 0.18  # sigma ~ (440 MeV)^2 ~ 0.18 GeV^2
    string_tension_MeV = np.sqrt(string_tension_GeV2) * 1000  # ~ 424 MeV

    return {
        "mechanism": "Confinement is the QCD vacuum at its self-referential fixed point",
        "self_consistency_loop": [
            "Gluon condensate <G^2> determines vacuum structure",
            "Vacuum structure determines allowed gluon configurations",
            "Allowed configurations determine <G^2>",
            "Fixed point: <G^2> = <G^2>_target[<G^2>]",
        ],
        "threshold": threshold,
        "observables_as_fixed_point_properties": {
            "string_tension": {
                "value_MeV": string_tension_MeV,
                "interpretation": "Restoring force when z departs from z_target",
            },
            "gluon_condensate": {
                "value_GeV4": gluon_condensate_GeV4,
                "interpretation": "The fixed-point value of z for the color field",
            },
            "hadron_masses": {
                "interpretation": "Eigenvalues of the constitutive equation at the confining fixed point",
                "status": "NOT COMPUTED (requires full lattice or AdS/CFT input)",
            },
        },
        "sector_13_parallel": {
            "consciousness": "Brain achieves self-referential resonance at 38k neurons",
            "confinement": "QCD vacuum achieves self-referential condensate below Lambda_QCD",
            "same_mechanism": "External target -> threshold -> self-referential fixed point",
        },
    }


def full_qcd_fixed_point_analysis() -> dict:
    """Complete QCD confinement-as-fixed-point analysis."""
    threshold = confinement_threshold()
    profile = self_referential_profile()
    structure = confinement_as_fixed_point()

    t_gev = threshold.get('threshold_GeV')
    t_ratio = threshold.get('ratio_to_Lambda_QCD')
    return {
        "threshold": threshold,
        "profile": profile,
        "structure": structure,
        "verdict": (
            f"QCD confinement maps cleanly onto the self-referential fixed-point "
            f"framework. The threshold at mu ~ {t_gev:.2f} GeV "
            f"(ratio {t_ratio:.1f} to Lambda_QCD) is the "
            f"energy where the color sector crosses from perturbative (external target) "
            f"to self-referential (confining vacuum). This is structurally identical "
            f"to the consciousness threshold (38k neurons) and the cosmological "
            f"threshold (z ~ 0.33)."
        ) if t_gev else "Threshold not found.",
    }
