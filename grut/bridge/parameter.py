"""The Bridge Parameter — connecting decoherence to cosmology.

STATUS (current):
    f(R) = 2-R structure: COMPUTED.
    R value: PRIMARY = R_REFRACTIVE = sqrt(4/3) via closure protocol.
    3-loop R_ANOMALY = 1.15428 is verification-pending (expert audit needed).
    Independent confirmation candidate: R_EPSILON_CANDIDATE = 1.1537
    (Osborn 2003 eq 36) matches within 0.05%.

    v3 INHERITANCE: R_REFRACTIVE = sqrt(4/3) is the CANONICAL value
    (conformal-mode-scalar / alpha = 1/3 trace-anomaly result). R_ANOMALY
    (3-loop, verification-pending) and R_EPSILON_CANDIDATE are ARCHIVED
    v2 cross-check candidates, not operative inputs for v3.
"""
import numpy as np
from grut.foundation.constants import G, HBAR
from grut.foundation.noise_kernel import lambda_grav, extended_body_suppression
from grut.foundation.anomaly import R_ANOMALY, R_EPSILON_CANDIDATE, S_CTP
from grut.foundation.closure_protocol import R_REFRACTIVE

TAU_0_CANONICAL = 41.9e6 * 3.156e7
R_PRIMARY = R_REFRACTIVE

def bridge_prediction(H_0_kms=70.0, tau_0_s=None, R_choice="closure"):
    """Given tau_0, predict Omega_Lambda.

    Args:
        H_0_kms: Hubble constant in km/s/Mpc.
        tau_0_s: decoherence timescale in seconds (default: canonical 41.9 Myr).
        R_choice: "closure" (R_REFRACTIVE = sqrt(4/3), primary),
            "anomaly" (R_ANOMALY = 1.15428, 3-loop verification-pending),
            or "epsilon" (R_EPSILON_CANDIDATE = 1.1537).
    """
    tau = tau_0_s or TAU_0_CANONICAL
    H_0 = H_0_kms * 1e3 / 3.0857e22
    if R_choice == "epsilon":
        R = R_EPSILON_CANDIDATE
    elif R_choice == "anomaly":
        R = R_ANOMALY
    else:
        R = R_PRIMARY
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
            "inputs": {"2-R": 2-R_PRIMARY, "S": S_CTP, "H_0": "70 km/s/Mpc", "OL": 0.6889},
            "note": "Two computed (2-R, S) + two measured (H_0, OL). Experiment determines tau_0 independently."}
