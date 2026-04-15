"""Cosmological Constant — f(R)=2-R from 3-loop CTP on de Sitter."""
import numpy as np
from grut.foundation.anomaly import C_FINAL, R_ANOMALY, S_CTP
from grut.foundation.constants import HBAR, G, C as C_LIGHT, K_B, T_PLANCK

TAU_0 = 41.9e6 * 3.156e7
H_INF = (2 - R_ANOMALY) / (S_CTP * TAU_0)

def vacuum_prediction(H_0_kms=70.0):
    H_0 = H_0_kms * 1e3 / 3.0857e22
    OL = (H_INF / H_0)**2
    return {"H_inf_Hz": H_INF, "H_0_Hz": H_0, "Omega_Lambda": OL,
            "Planck_OL": 0.6889, "deviation_pct": (OL/0.6889-1)*100,
            "f_R": 2-R_ANOMALY, "status": "COMPUTED (3-loop CTP on S4)"}

def era_map(n_eras=329):
    """Discrete constitutive era map."""
    alpha = 1-np.exp(-1); gamma = 0.000982; k = 2*np.pi/(1.5428-1); N_th = 215
    x, mem = 0.0, 0.0; history = []
    for n in range(n_eras):
        arg = min(500, max(-500, k*(n-N_th)))
        tgt = 1/(1+np.exp(-arg))
        mem = (1-np.exp(-1))*(x-tgt) + np.exp(-1)*mem
        x = max(0, min(1, x + alpha*(tgt-x) + gamma*mem))
        history.append({"era": n, "x": x, "target": tgt})
    return {"n_eras": n_eras, "final_x": x, "data": history}

def constitutive_cosmology(t_start=1.0, t_end=None, n_steps=5000):
    """Full expansion history with KMS-derived tau."""
    if t_end is None: t_end = 13.8e9*3.156e7
    GEV_TO_K = 1.16e13; M_PL = 2.435e18; g_star = 106.75
    s = np.linspace(np.log(t_start), np.log(t_end), n_steps); t = np.exp(s)
    H = np.zeros(n_steps); H[0] = 0.5/t_start
    t_eq = 50000*3.156e7; t_L = 9.8e9*3.156e7
    for i in range(1, n_steps):
        # Target
        if t[i-1] < t_eq: H_tgt = 1/(2*t[i-1])
        elif t[i-1] < t_L: H_tgt = 2/(3*t[i-1])
        else:
            f = 1-np.exp(-(t[i-1]-t_L)/TAU_0)
            H_tgt = 2/(3*t[i-1])*(1-f) + H_INF*f
        H_tgt = max(H_tgt, H_INF)
        # KMS tau
        H_GeV = H[i-1]/1.519e24
        T_GeV = np.sqrt(abs(H_GeV)*M_PL/np.sqrt(np.pi**2*g_star/90)) if H_GeV > 0 else 0
        T_K = max(T_GeV*GEV_TO_K, 2.725)
        tau = max(T_PLANCK, min(HBAR/(2*np.pi*K_B*T_K), TAU_0))
        dt = t[i]-t[i-1]; decay = np.exp(-dt/tau) if tau > 0 else 0
        H[i] = max(H_tgt + (H[i-1]-H_tgt)*decay, H_INF*0.01)
    return {"t": t.tolist(), "H": H.tolist(), "H_inf": H_INF}
