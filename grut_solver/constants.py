"""
GRUT Solver — Physical Constants

SINGLE SOURCE OF TRUTH for all physical constants in the framework.
CODATA 2018 exact values where available.
"""

import numpy as np

# =============================================================================
# FUNDAMENTAL CONSTANTS (CODATA 2018)
# =============================================================================

G: float = 6.67430e-11            # Gravitational constant [m^3 kg^-1 s^-2]
HBAR: float = 1.054571817e-34     # Reduced Planck constant [J s]
C: float = 2.99792458e8           # Speed of light [m/s]
K_B: float = 1.380649e-23         # Boltzmann constant [J/K] (exact, SI 2019)
SIGMA_SB: float = 5.670374419e-8  # Stefan-Boltzmann constant [W m^-2 K^-4]
AMU: float = 1.66053906660e-27    # Atomic mass unit [kg]
E_CHARGE: float = 1.602176634e-19 # Elementary charge [C] (exact, SI 2019)
EPSILON_0: float = 8.8541878128e-12  # Vacuum permittivity [F/m]
M_ELECTRON: float = 9.1093837015e-31  # Electron mass [kg]

# =============================================================================
# DERIVED SCALES
# =============================================================================

M_PLANCK: float = np.sqrt(HBAR * C / G)        # Planck mass [kg] ~ 2.18e-8
L_PLANCK: float = np.sqrt(HBAR * G / C**3)      # Planck length [m] ~ 1.62e-35
T_PLANCK: float = L_PLANCK / C                   # Planck time [s] ~ 5.39e-44
E_PLANCK: float = M_PLANCK * C**2                # Planck energy [J]
ALPHA_EM: float = E_CHARGE**2 / (4 * np.pi * EPSILON_0 * HBAR * C)  # ~ 1/137

# =============================================================================
# GRUT-SPECIFIC CONSTANTS
# =============================================================================

TAU_I: float = HBAR / 2  # Imaginary relaxation time [J s / 2]
# tau_I = hbar/2 is IDENTIFIED (not derived). See Stage 9.

# Riemann zeta(3) = Apery's constant
ZETA_3: float = 1.2020569031595942

# 3-loop gravitational anomaly coefficient (scheme-protected, nonlocal operator)
# C_Final = 3*(99 + 2*pi^2 + 576*ln(2)*zeta(3)) / (16384*pi^6)
# From Program M (Grover 2025). Verified to 15 significant figures.
C_FINAL: float = 3.0 * (99.0 + 2.0 * np.pi**2 + 576.0 * np.log(2.0) * ZETA_3) / (16384.0 * np.pi**6)

# Anomaly ratio R = |C_Cosmo / C_Final| (from published papers)
R_ANOMALY: float = 1.15428

# =============================================================================
# COMMON MATERIAL PROPERTIES
# =============================================================================

# Gas molecule masses [kg]
M_N2: float = 28.0 * AMU          # Nitrogen
M_HE: float = 4.0 * AMU           # Helium
M_H2: float = 2.0 * AMU           # Hydrogen
M_RESIDUAL: float = 29.0 * AMU    # Typical residual gas mix (air-like)

# Material densities [kg/m^3]
RHO_SILICA: float = 2200.0
RHO_DIAMOND: float = 3510.0
RHO_GOLD: float = 19300.0
RHO_SILICON: float = 2330.0

# =============================================================================
# GRAVITATIONAL WAVE / DETECTOR CONSTANTS
# =============================================================================

# Schwarzschild fundamental QNM (n=0, l=2) — Leaver 1985
# In units of c^3/(G M)
QNM_OMEGA_R: float = 0.3737    # Real part (oscillation)
QNM_OMEGA_I: float = 0.0890    # Imaginary part (damping, positive convention)

# Detector frequency bands [Hz]
LIGO_F_LOW: float = 10.0
LIGO_F_HIGH: float = 5000.0
LISA_F_LOW: float = 1e-4
LISA_F_HIGH: float = 0.1

# Solar mass [kg]
M_SUN: float = 1.989e30

# =============================================================================
# SELF-TEST
# =============================================================================

def verify_constants() -> dict:
    """Verify all constants against known values. Returns dict of checks."""
    checks = {}

    # C_Final to 6 significant figures
    checks["C_FINAL_value"] = abs(C_FINAL - 1.14021e-4) / 1.14021e-4 < 1e-4
    checks["C_FINAL_positive"] = C_FINAL > 0

    # Planck mass
    checks["M_PLANCK"] = abs(M_PLANCK - 2.176e-8) / 2.176e-8 < 1e-3

    # Fine structure constant
    checks["ALPHA_EM"] = abs(1/ALPHA_EM - 137.036) / 137.036 < 1e-4

    # tau_I = hbar/2
    checks["TAU_I"] = TAU_I == HBAR / 2

    # Anomaly ratio
    checks["R_ANOMALY"] = abs(R_ANOMALY - 1.15428) < 1e-4

    return checks


if __name__ == "__main__":
    checks = verify_constants()
    all_pass = all(checks.values())
    for name, passed in checks.items():
        print(f"  {'PASS' if passed else 'FAIL'}: {name}")
    print(f"\n  All checks: {'PASS' if all_pass else 'FAIL'}")
    print(f"\n  C_FINAL = {C_FINAL:.15e}")
    print(f"  M_PLANCK = {M_PLANCK:.6e} kg")
    print(f"  L_PLANCK = {L_PLANCK:.6e} m")
    print(f"  ALPHA_EM = {ALPHA_EM:.8f} (1/alpha = {1/ALPHA_EM:.4f})")
    print(f"  TAU_I = {TAU_I:.6e} J s")
