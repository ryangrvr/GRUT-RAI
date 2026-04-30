"""
H_0 from GRUT first principles — one-parameter prediction.

STATUS (April 2026, audit-corrected):
    This module produces a one-parameter H_0 prediction:
        Inputs (computed by GRUT):
            R_anomaly  — 3-loop CTP scalar (Path G + Osborn ε)
            S_CTP      — path counting (= 108π)
            τ_0        — 41.9 Myr (cosmic-baseline + Bullet anchor)
        Input (observational anchor):
            N_total    — 329 eras (= observed t_0 / τ_0,
                         where t_0 ≈ 13.78 Gyr)
        Derived: H_inf = 58.16 km/s/Mpc from (2−R)/(S·τ_0)
        Derived: Ω_m, Ω_Λ from flat-ΛCDM Friedmann integration with
                 input (H_inf, t_0)
        Output:  H_0 = 69.03 km/s/Mpc

    The single observational parameter is N_total = 329 (equivalently:
    cosmic age). A zero-parameter H_0 chain via this route would
    require deriving N_total from framework foundations alone —
    registered as an open negative:
        registry: n_total_zero_parameter_derivation_open_question
                  (Chapter 12)
        ledger:   grut/toe/ledger.py (closure conditions,
                  4 attempts already closed negative)
        log:      theory/derivation/N_TOTAL_DERIVATION_ATTEMPT.md

    Closure likely depends on the Genesis Hypothesis (V7/V8
    Appendix A) being formalized to the point where the start time
    of cosmic evolution emerges from the null fixed point's
    destabilization timescale. Genesis Hypothesis is currently
    [SPECULATIVE]; closure does NOT require adopting it — it
    requires its machinery becoming computable.

    Note on prior framing: an earlier docstring named "Input 1
    (observational): Ω_dm (Planck value)" as the one parameter.
    That framing was inaccurate — the actual `grut_H_0_prediction`
    function does not consume Ω_dm. The one parameter is N_total,
    not Ω_dm. The Track VII vorton Ω_dm-derivation work (closed
    negative; theory/derivation/TRACK_VII_STEP_03_VORTEX.md) is
    related but doesn't change which input enters this module.

    The framework's simpler cosmic-baseline H_0 = 1/(S × τ_0) ≈
    68.8 km/s/Mpc (closure_protocol.py:H_0_IMPLIED_KM_S_MPC,
    registry claim h_0_prediction) is zero-parameter and does not
    use N_total. The two H_0 routes agree at 0.3%, supporting the
    cosmic-baseline approximation.

Framework details:
    GRUT computes H_inf = 58.16 km/s/Mpc (asymptotic vacuum rate
    from the 3-loop CTP formula) and τ_0 = 41.9 Myr (cosmic-baseline
    + Bullet Cluster anchors). The era map gives N_total = 329
    eras to present → age t_0 = 13.78 Gyr.

    Given H_inf and t_0, flat-ΛCDM Friedmann integration uniquely
    determines (Ω_m, Ω_Λ, H_0). Age is treated as input in this
    module; the open negative documents what would close that gap.

Cross-check: H_0 = 69.03 km/s/Mpc sits between Planck (67.4) and
SH0ES (73.0), consistent with flat ΛCDM at the ~2% level.
"""

import numpy as np
from scipy.optimize import brentq
from grut.foundation.anomaly import R_ANOMALY, R_EPSILON_CANDIDATE, S_CTP


# Constants
MPC_M = 3.0857e22          # 1 Mpc in meters
HZ_TO_KMSMPC = 3.0857e19   # conversion factor for H (Hz → km/s/Mpc)
YEAR_S = 3.156e7
TAU_0_DEFAULT = 41.9e6 * YEAR_S    # seconds


def age_flat_LCDM(H_0_kms, Omega_m):
    """Age of the universe in flat ΛCDM cosmology.

    Flat ΛCDM: Ω_m + Ω_Λ = 1 (no radiation, no curvature).

        t_0 = (2 / (3 H_0)) × (1 / √Ω_Λ) × sinh⁻¹(√(Ω_Λ / Ω_m))

    Returns age in seconds.
    """
    Omega_L = 1.0 - Omega_m
    if Omega_L <= 0:
        return float("inf")
    H_0_hz = H_0_kms / HZ_TO_KMSMPC
    return (2.0 / (3.0 * H_0_hz)) * (1.0 / np.sqrt(Omega_L)) * \
           np.arcsinh(np.sqrt(Omega_L / Omega_m))


def hubble_from_age_and_H_inf(H_inf_hz, t_0_s):
    """Given GRUT's H_inf and the age t_0, solve for (Ω_m, Ω_Λ, H_0).

    Uses flat ΛCDM relation: Ω_Λ = (H_inf / H_0)², so
    H_0 = H_inf / √Ω_Λ = H_inf / √(1 - Ω_m).

    Substituting into the age formula:

        t_0 = (2 / (3 H_inf)) × sinh⁻¹(√((1-Ω_m) / Ω_m))

    Solve for Ω_m.
    """
    target_arcsinh = 1.5 * H_inf_hz * t_0_s  # sinh⁻¹(√x) = 3 H_inf t_0 / 2
    sqrt_x = np.sinh(target_arcsinh)
    x = sqrt_x ** 2  # x = (1 - Ω_m) / Ω_m
    Omega_m = 1.0 / (1.0 + x)
    Omega_L = 1.0 - Omega_m

    H_0_hz = H_inf_hz / np.sqrt(Omega_L)
    H_0_kms = H_0_hz * HZ_TO_KMSMPC

    return {
        "Omega_m": Omega_m,
        "Omega_Lambda": Omega_L,
        "H_0_km_s_Mpc": H_0_kms,
        "H_0_Hz": H_0_hz,
        "age_Gyr": t_0_s / YEAR_S / 1e9,
        "H_inf_km_s_Mpc": H_inf_hz * HZ_TO_KMSMPC,
    }


def grut_H_0_prediction(n_eras=329, tau_0_s=TAU_0_DEFAULT,
                         R_choice="hand", include_radiation=False):
    """Compute H_0 from GRUT first principles.

    Inputs (all from GRUT):
      - R_anomaly (3-loop CTP on S⁴, V7 §26.2)
      - S_CTP (CTP path counting)
      - τ_0 (decoherence sector, gold benchmark)
      - N_eras (era map, threshold + post-threshold relaxation)

    Output: (Ω_m, Ω_Λ, H_0) from flat ΛCDM Friedmann integration.

    include_radiation: if True, account for small Ω_r ~ 5e-5 (tiny correction).
    """
    # GRUT's computed asymptotic rate
    R = R_ANOMALY if R_choice == "hand" else R_EPSILON_CANDIDATE
    H_inf_hz = (2.0 - R) / (S_CTP * tau_0_s)
    H_inf_kms = H_inf_hz * HZ_TO_KMSMPC

    # GRUT's era-map age
    t_0_s = n_eras * tau_0_s
    t_0_Gyr = t_0_s / YEAR_S / 1e9

    # Friedmann: solve for (Ω_m, Ω_Λ, H_0) given (H_inf, t_0)
    result = hubble_from_age_and_H_inf(H_inf_hz, t_0_s)

    # Optionally: include radiation (tiny effect today)
    if include_radiation:
        # Ω_r today ≈ 5e-5 (photons + neutrinos)
        Omega_r = 5e-5
        # Renormalize: Ω_m + Ω_Λ + Ω_r = 1
        Omega_m = result["Omega_m"] - Omega_r  # shift from matter (tiny)
        result["Omega_m"] = Omega_m
        result["Omega_r"] = Omega_r
        result["Omega_Lambda"] = 1.0 - Omega_m - Omega_r

    result["R"] = R
    result["R_choice"] = R_choice
    result["n_eras"] = n_eras
    result["tau_0_Myr"] = tau_0_s / YEAR_S / 1e6
    result["age_Gyr"] = t_0_Gyr
    result["status"] = (
        "ONE-PARAMETER — H_0 from H_inf (COMPUTED, V7 §26.2) plus "
        "age = N_eras × τ_0 with N_eras = 329 as observed-cosmic-age "
        "anchor. Open negative: deriving N_eras zero-parameter from "
        "framework foundations (registry: n_total_zero_parameter_"
        "derivation_open_question; log: N_TOTAL_DERIVATION_ATTEMPT.md, "
        "4 attempts closed negative). Closure likely requires the "
        "Genesis Hypothesis (Appendix A) becoming formal."
    )
    return result


def compare_to_observations():
    """Compare GRUT's prediction to Planck and SH0ES."""
    grut = grut_H_0_prediction()

    # Observational references
    planck = {"H_0_km_s_Mpc": 67.4, "Omega_Lambda": 0.6889, "Omega_m": 0.3111}
    shoes = {"H_0_km_s_Mpc": 73.0, "Omega_Lambda": 0.6466, "Omega_m": 0.3534}
    shoes_2024 = {"H_0_km_s_Mpc": 73.5, "source": "Riess/Casertano 2024"}

    return {
        "grut_prediction": grut,
        "planck_CMB": planck,
        "shoes_distance_ladder": shoes,
        "shoes_2024": shoes_2024,
        "grut_vs_planck_H0": f"{(grut['H_0_km_s_Mpc']/67.4 - 1)*100:+.2f}%",
        "grut_vs_shoes_H0": f"{(grut['H_0_km_s_Mpc']/73.0 - 1)*100:+.2f}%",
        "grut_vs_planck_Om": f"{(grut['Omega_m']/0.3111 - 1)*100:+.2f}%",
    }


def grut_H_inf_comparison():
    """GRUT's H_inf as a standalone falsifiable prediction.

    The structural identity H_inf² = H_0² × Ω_Λ means GRUT predicts a
    specific value of H_0 × √Ω_Λ independent of Ω_m/Ω_Λ individually.

    This is the strongest falsifiable cosmological prediction GRUT makes:
    any (H_0, Ω_Λ) pair consistent with flat ΛCDM should satisfy
    H_0 × √Ω_Λ = 58.16 km/s/Mpc.
    """
    from grut.foundation.anomaly import R_ANOMALY, S_CTP
    tau_0_s = TAU_0_DEFAULT
    H_inf_hz = (2 - R_ANOMALY) / (S_CTP * tau_0_s)
    H_inf_kms = H_inf_hz * HZ_TO_KMSMPC

    sources = [
        ("Planck CMB", 67.4, 0.6889),
        ("SH0ES 2023", 73.0, 0.6466),
        ("Riess 2024", 73.5, 0.6466),  # Ω_Λ approximate
    ]

    result = {
        "grut_H_inf_km_s_Mpc": H_inf_kms,
        "structural_identity": "H_inf² = H_0² × Ω_Λ (flat ΛCDM)",
        "comparisons": [],
    }

    for name, H_0, OL in sources:
        inferred_H_inf = H_0 * np.sqrt(OL)
        dev_pct = (H_inf_kms / inferred_H_inf - 1) * 100
        result["comparisons"].append({
            "source": name,
            "H_0": H_0,
            "Omega_Lambda": OL,
            "inferred_H_inf_km_s_Mpc": inferred_H_inf,
            "GRUT_minus_inferred_pct": dev_pct,
        })

    return result


def structural_t_eq():
    """Matter-Λ equality time from flat-ΛCDM structural identity.

    In flat ΛCDM, H_inf × t_eq = (2/3) × sinh⁻¹(1) = 0.5876 is an
    invariant — independent of Ω_m/Ω_Λ individually. Given GRUT's H_inf,
    this fixes t_eq structurally.

    Returns t_eq in Gyr and the corresponding N_threshold (era count).
    """
    from grut.foundation.anomaly import R_ANOMALY, S_CTP
    tau_0_s = TAU_0_DEFAULT
    H_inf_hz = (2 - R_ANOMALY) / (S_CTP * tau_0_s)

    K_eq = (2.0/3.0) * np.arcsinh(1.0)  # = 0.58758
    t_eq_s = K_eq / H_inf_hz
    t_eq_Gyr = t_eq_s / YEAR_S / 1e9
    N_threshold = t_eq_s / tau_0_s

    return {
        "structural_constant": K_eq,
        "constant_name": "H_inf × t_eq = (2/3) × sinh⁻¹(1) in flat ΛCDM",
        "t_eq_Gyr": t_eq_Gyr,
        "N_threshold_structural": N_threshold,
        "V7_claimed_N_threshold": 215,
        "discrepancy_pct": (N_threshold / 215 - 1) * 100,
        "status": (
            "COMPUTED — structural identity. "
            "V7's N_threshold = 215 differs by ~10%, suggesting it is fit "
            "(not fully structural) or the constitutive cosmology departs "
            "from flat ΛCDM at the ~10% level at late times."
        ),
    }


def run_all():
    """Run all predictions and print the full report."""
    print("=" * 65)
    print("GRUT cosmological predictions (V7 §26 + prototype extensions)")
    print("=" * 65)
    print()

    # H_inf standalone
    hinf = grut_H_inf_comparison()
    print("1. H_inf prediction (COMPUTED, V7 §26.2)")
    print(f"   GRUT: H_inf = {hinf['grut_H_inf_km_s_Mpc']:.2f} km/s/Mpc")
    print(f"   Identity: {hinf['structural_identity']}")
    print(f"   Observed H_0 × √Ω_Λ from different sources:")
    for c in hinf["comparisons"]:
        print(f"     {c['source']:15s} -> {c['inferred_H_inf_km_s_Mpc']:.2f} km/s/Mpc  "
              f"(GRUT {c['GRUT_minus_inferred_pct']:+.2f}%)")
    print()

    # Structural t_eq
    teq = structural_t_eq()
    print("2. Matter-Λ equality (structural identity)")
    print(f"   H_inf × t_eq = {teq['structural_constant']:.5f} (flat ΛCDM)")
    print(f"   t_eq = {teq['t_eq_Gyr']:.2f} Gyr")
    print(f"   N_threshold = {teq['N_threshold_structural']:.1f}")
    print(f"   V7 claims N_threshold = 215 (deviation {teq['discrepancy_pct']:+.1f}%)")
    print()

    # Full H_0 prediction
    result = grut_H_0_prediction()
    print("3. H_0 prediction (one-parameter — uses observed age)")
    print(f"   Inputs: R = {result['R']:.5f}, τ_0 = {result['tau_0_Myr']:.2f} Myr, N_eras = {result['n_eras']}")
    print(f"   Age (V7): {result['age_Gyr']:.2f} Gyr")
    print(f"   Outputs: Ω_m = {result['Omega_m']:.4f}, Ω_Λ = {result['Omega_Lambda']:.4f}")
    print(f"   ===> H_0 = {result['H_0_km_s_Mpc']:.2f} km/s/Mpc")
    print()

    # Comparison
    comp = compare_to_observations()
    print("4. Observational comparison")
    print(f"   Planck CMB:    67.4 km/s/Mpc  (GRUT {comp['grut_vs_planck_H0']})")
    print(f"   GRUT:          {comp['grut_prediction']['H_0_km_s_Mpc']:.2f} km/s/Mpc")
    print(f"   SH0ES 2023:    73.0 km/s/Mpc  (GRUT {comp['grut_vs_shoes_H0']})")
    print(f"   Riess 2024:    73.5 km/s/Mpc")


if __name__ == "__main__":
    run_all()
