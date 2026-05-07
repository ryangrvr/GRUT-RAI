"""
Adversarial Theory Comparison — GRUT vs competing frameworks

Head-to-head on specific, measurable predictions.
No hand-waving. Numbers vs numbers.
"""
import numpy as np
from grut.foundation.noise_kernel import lambda_grav
from grut.foundation.anomaly import R_ANOMALY, S_CTP
from grut.foundation.closure_protocol import R_REFRACTIVE

TAU_0 = 41.9e6 * 3.156e7

def decoherence_comparison(m=80.8e-15, l=1e-6, R=1e-6):
    """Compare decoherence predictions: GRUT vs CSL vs Diosi-Penrose vs standard QM."""
    # GRUT
    L_grut = lambda_grav(m, l, R)

    # Standard QM: no gravitational decoherence → Lambda = 0 at zero pressure
    L_qm = 0.0

    # CSL (Ghirardi-Rimini-Weber): Lambda_CSL = lambda_CSL × (m/m_0)^2 × N
    # Standard parameters: lambda = 10^-16 s^-1, r_c = 10^-7 m, m_0 = AMU
    lambda_csl = 1e-16  # s^-1
    r_c = 1e-7  # m
    m_0 = 1.661e-27  # AMU
    N_nucleons = m / m_0
    L_csl = lambda_csl * N_nucleons**2 * (1 - np.exp(-l**2/(4*r_c**2)))

    # Diosi-Penrose (point mass): Lambda_DP = G m^2 / (hbar l) — no extended body
    G = 6.674e-11; HBAR = 1.055e-34
    L_dp = G * m**2 / (HBAR * l)

    # Penrose OR: Lambda_OR = E_grav / hbar where E_grav ~ G m^2 / R
    E_grav = G * m**2 / R if R > 0 else G * m**2 / l
    L_penrose = E_grav / HBAR

    return {
        "mass_kg": m, "separation_m": l, "radius_m": R,
        "models": {
            "GRUT": {"Lambda_Hz": L_grut, "params": 0, "has_kink": True, "geometry_dep": True,
                     "entanglement_dep": True, "status": "DERIVED"},
            "Standard_QM": {"Lambda_Hz": L_qm, "params": 0, "has_kink": False, "geometry_dep": False,
                            "entanglement_dep": False, "status": "No gravitational decoherence"},
            "CSL": {"Lambda_Hz": L_csl, "params": 2, "lambda": lambda_csl, "r_c": r_c,
                    "has_kink": False, "geometry_dep": False, "entanglement_dep": False, "status": "2 free params"},
            "Diosi_Penrose_point": {"Lambda_Hz": L_dp, "params": 0, "has_kink": False, "geometry_dep": False,
                                     "entanglement_dep": True, "status": "No extended body"},
            "Penrose_OR": {"Lambda_Hz": L_penrose, "params": 0, "has_kink": False, "geometry_dep": False,
                           "entanglement_dep": False, "status": "Energy-based"},
        },
        "discriminators": {
            "F2_geometry": "GRUT only (others predict same rate for gold vs silica at same mass)",
            "F5_entanglement": "GRUT and DP only (CSL is state-independent)",
            "F6_kink": "GRUT only (requires extended body suppression S(l/R))",
        }
    }


def cosmology_comparison():
    """Compare cosmological constant predictions across frameworks."""
    H_0 = 70e3 / 3.0857e22
    R_primary = R_REFRACTIVE
    H_inf_grut = (2 - R_primary) / (S_CTP * TAU_0)
    OL_grut = (H_inf_grut / H_0)**2

    return {
        "observable": "Omega_Lambda",
        "observed": {"value": 0.6889, "error": 0.0056, "source": "Planck 2018"},
        "predictions": {
            "GRUT": {"value": OL_grut, "deviation_pct": (OL_grut/0.6889-1)*100,
                     "params": "1 (tau_0)", "derived": True,
                     "formula": "((2-R)/(S tau_0 H_0))^2",
                     "R_primary": R_primary,
                     "R_anomaly_verification_pending": R_ANOMALY},
            "String_Theory": {"value": "10^-120 to 10^0 (landscape)", "deviation_pct": "undetermined",
                              "params": "~500 (moduli)", "derived": False,
                              "note": "Anthropic landscape: 10^500 vacua, no unique prediction"},
            "Loop_QG": {"value": "not predicted", "deviation_pct": "N/A",
                        "params": "N/A", "derived": False,
                        "note": "LQG does not predict the cosmological constant"},
            "Asymptotic_Safety": {"value": "~0.7 (claimed)", "deviation_pct": "~2%",
                                   "params": "2-3 (UV fixed point)", "derived": True,
                                   "note": "Requires specific UV trajectory selection"},
            "Standard_QFT": {"value": "10^120 (1-loop)", "deviation_pct": "10^61 × too large",
                             "params": "0", "derived": True,
                             "note": "The cosmological constant problem — 1-loop overshoots by 10^61"},
        }
    }


def baryogenesis_comparison():
    """Compare baryon asymmetry predictions."""
    return {
        "observable": "eta_B (baryon-to-photon ratio)",
        "observed": {"value": 6.1e-10, "error": 0.04e-10, "source": "Planck 2018"},
        "predictions": {
            "GRUT": {"value": 6.56e-10, "deviation_pct": 8, "mechanism": "CTP anomaly formula",
                     "status": "COMPUTED"},
            "SM_EW_baryogenesis": {"value": "~10^-18 (too small)", "deviation_pct": "10^8 × too small",
                                   "mechanism": "EW phase transition (smooth crossover in SM)",
                                   "note": "SM EW transition not first-order — insufficient CP violation"},
            "Leptogenesis": {"value": "~10^-10 (adjustable)", "deviation_pct": "fitted",
                             "mechanism": "Heavy Majorana neutrino decay",
                             "note": "Requires unmeasured Yukawa couplings — not a prediction"},
            "Affleck_Dine": {"value": "adjustable", "mechanism": "Flat direction condensate",
                             "note": "Requires SUSY — not observed at LHC"},
        }
    }


def dark_matter_comparison():
    """Compare dark matter predictions."""
    return {
        "observable": "Dark matter candidate",
        "predictions": {
            "GRUT": {"mass": "2.1e9 GeV", "mediator": "387 MeV dark photon",
                     "sigma_over_m": "0.001 cm^2/g", "detection": "Beam dump (LHCb, Belle II)",
                     "params": 0, "status": "CLOSED (Route 1)"},
            "WIMP": {"mass": "10-1000 GeV", "mediator": "Z/Higgs",
                     "sigma_over_m": "~10^-46 cm^2", "detection": "Direct detection (LZ, XENONnT)",
                     "params": "2+ (mass, cross-section)", "status": "NOT FOUND (LZ null result)"},
            "Axion": {"mass": "10^-5-10^-3 eV", "mediator": "photon coupling",
                      "detection": "ADMX, ABRACADABRA",
                      "params": "1 (f_a)", "status": "Searching"},
            "Sterile_Neutrino": {"mass": "1-50 keV", "mediator": "mixing angle",
                                  "detection": "X-ray line at 3.5 keV (disputed)",
                                  "params": "2 (mass, mixing)", "status": "Inconclusive"},
        }
    }


def full_comparison():
    """All comparisons in one call."""
    return {
        "decoherence": decoherence_comparison(),
        "cosmology": cosmology_comparison(),
        "baryogenesis": baryogenesis_comparison(),
        "dark_matter": dark_matter_comparison(),
        "summary": {
            "GRUT_advantages": [
                "Zero-parameter decoherence prediction (competitors have 0-2 free params but less discriminating power)",
                "Cosmological constant at 0.3% (string theory: landscape; LQG: no prediction; QFT: 10^61 off)",
                "Baryon asymmetry at 8% (SM: 10^8 too small; leptogenesis: fitted; Affleck-Dine: requires SUSY)",
                "Dark photon at 387 MeV (specific, testable NOW; WIMPs: not found; axions: searching)",
            ],
            "GRUT_disadvantages": [
                "Mathematical maturity far below string theory and LQG",
                "No peer-reviewed publication yet",
                "One bridge parameter (tau_0) not derived",
                "Constitutive projection heuristic for second-order sectors",
            ]
        }
    }
