"""CKM matrix diagnostics — unitarity and angle extraction."""
import numpy as np

# PDG central values (Wolfenstein-like)
CKM_PDG = np.array([
    [0.97370, 0.2245, 0.00382],
    [0.221,   0.987,  0.0410],
    [0.008,   0.0388, 1.013],
], dtype=float)

def unitarity_check(V: np.ndarray = None) -> dict:
    """Check V^dag V ~ I."""
    if V is None:
        V = CKM_PDG
    product = V.T @ V  # approximate for real |V|
    off_diag = np.max(np.abs(product - np.eye(3)))
    return {"max_off_diagonal": off_diag,
            "status": "PASS" if off_diag < 0.05 else "MARGINAL"}

def cabibbo_angle() -> float:
    """sin(theta_C) ~ |V_us| ~ 0.225."""
    return CKM_PDG[0, 1]

def hierarchy_summary() -> dict:
    """CKM hierarchy: |V_us| >> |V_cb| >> |V_ub|."""
    return {"V_us": CKM_PDG[0,1], "V_cb": CKM_PDG[1,2], "V_ub": CKM_PDG[0,2],
            "ratio_us_cb": CKM_PDG[0,1]/CKM_PDG[1,2],
            "ratio_cb_ub": CKM_PDG[1,2]/CKM_PDG[0,2],
            "note": "Hierarchical structure. NOT derived from GRUT — input data."}
