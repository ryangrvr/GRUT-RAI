"""Yukawa coupling utilities — input data, hierarchy summaries."""
import numpy as np

V_HIGGS = 246.0  # GeV

SM_MASSES_GEV = {
    "up": 0.0022, "down": 0.0047, "charm": 1.28, "strange": 0.095,
    "top": 173.0, "bottom": 4.18,
    "electron": 0.000511, "muon": 0.1057, "tau": 1.777,
}

def yukawa_table() -> list[dict]:
    """Return SM fermion Yukawa couplings (FREE, not derived)."""
    return [{"name": n, "M_GeV": m, "y_f": m*np.sqrt(2)/V_HIGGS,
             "log10_y": np.log10(m*np.sqrt(2)/V_HIGGS)}
            for n, m in SM_MASSES_GEV.items()]

def hierarchy_ratio() -> float:
    """y_top / y_electron — the Yukawa hierarchy."""
    return SM_MASSES_GEV["top"] / SM_MASSES_GEV["electron"]
