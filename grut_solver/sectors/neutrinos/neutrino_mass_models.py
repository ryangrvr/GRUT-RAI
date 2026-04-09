"""Neutrino mass model entry points — Dirac and seesaw scaffolds."""
import numpy as np

V_HIGGS = 246.0  # GeV

def dirac_mass(y_nu: float, v: float = V_HIGGS) -> float:
    """Dirac neutrino mass: m = y_nu v / sqrt(2). Requires y_nu ~ 10^-12."""
    return y_nu * v / np.sqrt(2)

def seesaw_type1(y_nu: float, M_R: float, v: float = V_HIGGS) -> float:
    """Type-I seesaw: m_nu ~ (y_nu v)^2 / (2 M_R). M_R >> v."""
    return (y_nu * v)**2 / (2 * M_R)

def mass_scale_scan() -> list[dict]:
    """Show required y_nu or M_R for observed neutrino masses."""
    m_atm = 0.05  # eV (atmospheric scale)
    results = []
    # Dirac: y_nu = m sqrt(2) / v
    y_dirac = m_atm * 1e-9 * np.sqrt(2) / V_HIGGS  # convert eV to GeV
    results.append({"model": "Dirac", "y_nu": y_dirac,
                    "note": f"y ~ {y_dirac:.2e} (unnaturally small)"})
    # Seesaw: M_R = (y v)^2 / (2 m)
    for y in [0.01, 0.1, 1.0]:
        M_R = (y * V_HIGGS)**2 / (2 * m_atm * 1e-9)
        results.append({"model": f"Seesaw (y={y})", "M_R_GeV": M_R,
                        "note": f"M_R ~ {M_R:.2e} GeV"})
    return results

MODEL_STATUS = {
    "Dirac": "exploratory entry point (y_nu unnaturally small)",
    "Majorana/seesaw": "exploratory entry point (M_R undetermined)",
    "GRUT-native mechanism": "OPEN — no constitutive neutrino mass mechanism derived",
}
