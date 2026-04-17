"""The Bridge Parameter — connecting decoherence to cosmology.

STATUS (per main doc §26.1):
    f(R) = 2-R structure: COMPUTED.
    R value: CONDITIONAL — hand-constructed R_ANOMALY = 1.15428, SM-derivable
        candidate R_EPSILON_CANDIDATE = 1.1537 (Osborn 2003 eq 36). Both
        give Omega_Lambda consistent with Planck within observational bounds.
"""
import numpy as np
from grut.foundation.constants import G, HBAR
from grut.foundation.noise_kernel import lambda_grav, extended_body_suppression
from grut.foundation.anomaly import R_ANOMALY, R_EPSILON_CANDIDATE, S_CTP

TAU_0_CANONICAL = 41.9e6 * 3.156e7

def bridge_prediction(H_0_kms=70.0, tau_0_s=None, R_choice="hand"):
    """Given tau_0, predict Omega_Lambda.

    Args:
        H_0_kms: Hubble constant in km/s/Mpc.
        tau_0_s: decoherence timescale in seconds (default: canonical 41.9 Myr).
        R_choice: "hand" (R_ANOMALY = 1.15428, v7 default) or "epsilon"
            (R_EPSILON_CANDIDATE = 1.1537, v8 SM-derivable candidate).
    """
    tau = tau_0_s or TAU_0_CANONICAL
    H_0 = H_0_kms * 1e3 / 3.0857e22
    R = R_EPSILON_CANDIDATE if R_choice == "epsilon" else R_ANOMALY
    H_inf = (2 - R) / (S_CTP * tau)
    OL = (H_inf / H_0)**2
    return {"tau_0_s": tau, "tau_0_Myr": tau/(1e6*3.156e7),
            "H_inf_Hz": H_inf, "Omega_Lambda": OL, "Planck": 0.6889,
            "deviation_pct": (OL/0.6889 - 1)*100,
            "R": R, "R_choice": R_choice}

def experimental_chain(m_kg, l_m, R_m, Lambda_measured_Hz, H_0_kms=70.0):
    """Full experimental chain: measured Lambda → tau_0 → Omega_Lambda."""
    S = extended_body_suppression(l_m, R_m)
    tau_0 = HBAR * l_m / (G * m_kg**2 * S) if S > 0 else 0
    Lambda_predicted = lambda_grav(m_kg, l_m, R_m)
    prediction = bridge_prediction(H_0_kms, tau_0)
    return {**prediction, "Lambda_predicted_Hz": Lambda_predicted,
            "Lambda_measured_Hz": Lambda_measured_Hz,
            "Lambda_agreement": abs(Lambda_predicted - Lambda_measured_Hz)/Lambda_predicted < 0.1
                if Lambda_predicted > 0 else False}

def tau_0_from_observation():
    """The canonical tau_0 derived from cosmological observation."""
    return {"tau_0_s": TAU_0_CANONICAL, "tau_0_Myr": 41.9,
            "formula": "tau_0 = (2-R) / (S × H_0 × sqrt(Omega_Lambda))",
            "inputs": {"2-R": 2-R_ANOMALY, "S": S_CTP, "H_0": "70 km/s/Mpc", "OL": 0.6889},
            "note": "Two computed (2-R, S) + two measured (H_0, OL). Experiment determines tau_0 independently."}
