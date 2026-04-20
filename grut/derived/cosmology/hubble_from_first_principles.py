"""
Prototype: H_0 from GRUT first principles (V8 Track X extension).

GRUT computes H_inf = 58.16 km/s/Mpc (asymptotic vacuum rate from the
3-loop CTP formula) and τ_0 = 41.9 Myr (noise kernel at gold benchmark).
The era map gives N_total = 329 eras to present → age t_0 = 13.78 Gyr.

Given H_inf and t_0, flat ΛCDM Friedmann integration uniquely determines
(Ω_m, Ω_Λ, H_0). This is a one-parameter prediction: age is input, H_0
is output.

The age itself in V7 is t_0 = N × τ_0 where N = 329 comes from
13.8 Gyr / 41.9 Myr. In a truly first-principles framework, N would be
predicted structurally (via the threshold era N_th = 215 plus post-
threshold relaxation). For now we treat age as observational input and
see what H_0 drops out.

Cross-check: result should be near observed H_0 ~ 67-73 km/s/Mpc if
GRUT's H_inf is consistent with flat ΛCDM cosmology.
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
        "PROTOTYPE — H_0 from GRUT first principles using H_inf (COMPUTED, V7 §26.2) "
        "+ age = N_eras × τ_0 as input. If N_eras = 329 is itself derived "
        "(structural from era-map threshold + relaxation, not fit to observed age), "
        "this becomes a zero-parameter prediction."
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


if __name__ == "__main__":
    result = grut_H_0_prediction()
    print("=" * 65)
    print("GRUT first-principles H_0 prediction (prototype, V8 track)")
    print("=" * 65)
    print(f"\nInputs (from GRUT):")
    print(f"  R = {result['R']:.5f}                  (3-loop CTP on S⁴)")
    print(f"  τ_0 = {result['tau_0_Myr']:.2f} Myr            (noise kernel, gold benchmark)")
    print(f"  N_eras = {result['n_eras']}                (era map)")
    print(f"\nDerived:")
    print(f"  H_inf  = {result['H_inf_km_s_Mpc']:.2f} km/s/Mpc")
    print(f"  age    = {result['age_Gyr']:.2f} Gyr")
    print(f"\nOutputs (flat ΛCDM Friedmann):")
    print(f"  Ω_m    = {result['Omega_m']:.4f}")
    print(f"  Ω_Λ    = {result['Omega_Lambda']:.4f}")
    print(f"  H_0    = {result['H_0_km_s_Mpc']:.2f} km/s/Mpc")
    print()

    print("=" * 65)
    print("Comparison to observations")
    print("=" * 65)
    comp = compare_to_observations()
    print(f"\nGRUT prediction:  H_0 = {comp['grut_prediction']['H_0_km_s_Mpc']:.2f} km/s/Mpc,"
          f"  Ω_m = {comp['grut_prediction']['Omega_m']:.4f}")
    print(f"Planck CMB:       H_0 = 67.4 km/s/Mpc,   Ω_m = 0.3111")
    print(f"SH0ES ladder:     H_0 = 73.0 km/s/Mpc,   Ω_m = 0.3534")
    print(f"Riess 2024:       H_0 = 73.5 km/s/Mpc")
    print()
    print(f"GRUT vs Planck H_0: {comp['grut_vs_planck_H0']}")
    print(f"GRUT vs SH0ES H_0:  {comp['grut_vs_shoes_H0']}")
    print(f"GRUT vs Planck Ω_m: {comp['grut_vs_planck_Om']}")
