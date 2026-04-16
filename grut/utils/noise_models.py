"""
Realistic Experimental Noise Models

Models the actual noise environment of a quantum optomechanics experiment:
- Gas scattering (kinetic theory, multiple gas species)
- Blackbody radiation (emission + absorption + scattering)
- Laser noise (shot noise, radiation pressure, back-action)
- Vibrational isolation (seismic, acoustic, mechanical resonances)
- Electromagnetic shielding (DC fields, RF pickup, Johnson noise)
- Detector noise (dark counts, readout noise)

Each model takes physical parameters and returns a decoherence rate.
Combined with Lambda_grav, this gives realistic signal-to-noise.
"""

import numpy as np
from grut.foundation.constants import G, HBAR, K_B, C, AMU, ALPHA_EM

SIGMA_SB = 5.670374419e-8  # Stefan-Boltzmann constant [W/m^2/K^4]


# ═══════════════════════════════════════════════════════
# GAS SCATTERING (detailed)
# ═══════════════════════════════════════════════════════

GAS_SPECIES = {
    "N2": {"mass_amu": 28, "sigma_nm2": 0.43},
    "He": {"mass_amu": 4, "sigma_nm2": 0.21},
    "H2": {"mass_amu": 2, "sigma_nm2": 0.27},
    "Ar": {"mass_amu": 40, "sigma_nm2": 0.36},
    "residual_air": {"mass_amu": 29, "sigma_nm2": 0.40},
}

def gas_decoherence(m_kg, l_m, R_m, P_Pa, T_K=300, gas="residual_air"):
    """Gas scattering decoherence from kinetic theory.
    
    Lambda_gas = n × sigma × v_th × F(q l / hbar)
    
    where F is the form factor accounting for partial decoherence
    at small momentum transfer.
    """
    spec = GAS_SPECIES.get(gas, GAS_SPECIES["residual_air"])
    m_gas = spec["mass_amu"] * AMU
    
    n = P_Pa / (K_B * T_K)  # number density
    sigma = np.pi * R_m**2   # geometric cross-section
    v_th = np.sqrt(8 * K_B * T_K / (np.pi * m_gas))  # thermal velocity
    
    # Momentum transfer: q ~ m_gas × v_th
    q = m_gas * v_th
    ql_hbar = q * l_m / HBAR
    
    # Form factor: F = 1 - sinc(ql/hbar)
    if ql_hbar > 100:
        F = 1.0
    elif ql_hbar < 0.01:
        F = ql_hbar**2 / 6  # small argument expansion
    else:
        F = 1.0 - np.sin(ql_hbar) / ql_hbar
    
    return n * sigma * v_th * F


# ═══════════════════════════════════════════════════════
# BLACKBODY RADIATION (detailed)
# ═══════════════════════════════════════════════════════

def blackbody_emission(R_m, T_K):
    """Decoherence from thermal photon emission.
    
    Rate ~ (emissivity × area × sigma_SB × T^4) / (hbar × omega_thermal)
    """
    area = 4 * np.pi * R_m**2
    power = area * SIGMA_SB * T_K**4  # total radiated power (assuming emissivity ~ 1)
    omega_th = K_B * T_K / HBAR  # thermal frequency
    photon_rate = power / (HBAR * omega_th) if omega_th > 0 else 0
    return photon_rate


def blackbody_scattering(R_m, l_m, T_K):
    """Decoherence from scattering ambient thermal photons.
    
    For particles much smaller than thermal wavelength (R << lambda_th):
    Lambda_scatter ~ (8pi/3) × (R/lambda_th)^6 × sigma_SB T^4 / (hbar c) × l^2
    
    Rayleigh regime: strong R^6 dependence.
    """
    lambda_th = HBAR * C / (K_B * T_K) if T_K > 0 else 1e10  # thermal wavelength
    if R_m < lambda_th:
        # Rayleigh regime
        x = R_m / lambda_th
        rate = (8 * np.pi / 3) * x**6 * SIGMA_SB * T_K**4 / (HBAR * C) * l_m**2
    else:
        # Geometric regime
        sigma_scatter = np.pi * R_m**2
        n_photon = 2 * 1.202 * (K_B * T_K)**3 / (np.pi**2 * HBAR**3 * C**3)  # photon density
        rate = n_photon * sigma_scatter * C * l_m**2 / lambda_th**2
    return rate


def blackbody_total(R_m, l_m, T_K):
    """Total blackbody decoherence (emission + scattering)."""
    return blackbody_emission(R_m, T_K) + blackbody_scattering(R_m, l_m, T_K)


# ═══════════════════════════════════════════════════════
# LASER NOISE
# ═══════════════════════════════════════════════════════

def laser_shot_noise(power_W, wavelength_m=1064e-9):
    """Shot noise from trapping/readout laser.
    
    Photon arrival rate: n_dot = P / (hbar omega)
    Momentum kick per photon: p = hbar k = h/lambda
    Decoherence rate: ~ n_dot × (p l / hbar)^2 for l << lambda
    """
    omega = 2 * np.pi * C / wavelength_m
    n_dot = power_W / (HBAR * omega)  # photon rate
    return n_dot  # simplified: each photon is a potential decoherence event


def laser_radiation_pressure(power_W, m_kg, wavelength_m=1064e-9):
    """Radiation pressure noise heating rate.
    
    Momentum diffusion: D_p = (2P/c) × (hbar k)^2 × delta_f
    Decoherence: Lambda ~ D_p l^2 / hbar^2
    """
    k = 2 * np.pi / wavelength_m
    F_rad = 2 * power_W / C  # radiation pressure force
    D_p = F_rad * HBAR * k  # momentum diffusion
    return D_p / m_kg  # heating rate [Hz-like]


# ═══════════════════════════════════════════════════════
# VIBRATION ISOLATION
# ═══════════════════════════════════════════════════════

def vibrational_decoherence(isolation_level="good"):
    """Vibrational noise floor for different isolation levels.
    
    Returns effective decoherence rate from mechanical vibrations.
    """
    levels = {
        "poor":      {"delta_x": 1e-9,  "tau": 0.01, "Lambda": 1e-7},
        "standard":  {"delta_x": 1e-10, "tau": 0.1,  "Lambda": 1e-10},
        "good":      {"delta_x": 1e-11, "tau": 0.1,  "Lambda": 1e-12},
        "excellent":  {"delta_x": 1e-12, "tau": 1.0,  "Lambda": 1e-15},
        "state_of_art": {"delta_x": 1e-13, "tau": 10.0, "Lambda": 1e-18},
    }
    return levels.get(isolation_level, levels["good"])


# ═══════════════════════════════════════════════════════
# ELECTROMAGNETIC SHIELDING
# ═══════════════════════════════════════════════════════

def em_noise_floor(shielding="good"):
    """Electromagnetic noise floor for different shielding levels.
    
    Includes: stray DC fields, RF pickup, Johnson noise from nearby conductors.
    """
    levels = {
        "none":       {"Lambda_Hz": 1e3,  "description": "No shielding"},
        "basic":      {"Lambda_Hz": 1e0,   "description": "Faraday cage"},
        "good":       {"Lambda_Hz": 1e-3,  "description": "Faraday cage + mu-metal"},
        "excellent":  {"Lambda_Hz": 1e-6,  "description": "Multi-layer + active compensation"},
        "state_of_art": {"Lambda_Hz": 1e-9, "description": "Superconducting shield + active"},
    }
    return levels.get(shielding, levels["good"])


# ═══════════════════════════════════════════════════════
# COMBINED NOISE BUDGET
# ═══════════════════════════════════════════════════════

def full_noise_budget(m_kg, l_m, R_m, P_Pa, T_K, 
                       laser_power_W=1e-3, 
                       isolation="good", shielding="good",
                       gas="residual_air"):
    """Complete noise budget for a decoherence experiment."""
    
    L_grav = G * m_kg**2 * min(1, (l_m/R_m)**3/6) / (HBAR * l_m)
    L_gas = gas_decoherence(m_kg, l_m, R_m, P_Pa, T_K, gas)
    L_bb = blackbody_total(R_m, l_m, T_K)
    L_laser = laser_shot_noise(laser_power_W)
    L_rad_press = laser_radiation_pressure(laser_power_W, m_kg)
    vib = vibrational_decoherence(isolation)
    L_vib = vib["Lambda"]
    em = em_noise_floor(shielding)
    L_em = em["Lambda_Hz"]
    
    L_total_env = L_gas + L_bb + L_laser + L_rad_press + L_vib + L_em
    L_total = L_grav + L_total_env
    
    channels = {
        "gravitational": {"rate_Hz": L_grav, "fraction_pct": L_grav/L_total*100 if L_total > 0 else 0},
        "gas_scattering": {"rate_Hz": L_gas, "fraction_pct": L_gas/L_total*100 if L_total > 0 else 0},
        "blackbody": {"rate_Hz": L_bb, "fraction_pct": L_bb/L_total*100 if L_total > 0 else 0},
        "laser_shot": {"rate_Hz": L_laser, "fraction_pct": L_laser/L_total*100 if L_total > 0 else 0},
        "radiation_pressure": {"rate_Hz": L_rad_press, "fraction_pct": L_rad_press/L_total*100 if L_total > 0 else 0},
        "vibrational": {"rate_Hz": L_vib, "fraction_pct": L_vib/L_total*100 if L_total > 0 else 0},
        "electromagnetic": {"rate_Hz": L_em, "fraction_pct": L_em/L_total*100 if L_total > 0 else 0},
    }
    
    dominant = max(channels.items(), key=lambda x: x[1]["rate_Hz"])
    dominant_env = max(((k,v) for k,v in channels.items() if k != "gravitational"), key=lambda x: x[1]["rate_Hz"])
    
    snr = L_grav / L_total_env if L_total_env > 0 else float('inf')
    
    return {
        "signal": {"Lambda_grav_Hz": L_grav},
        "noise": {"Lambda_total_env_Hz": L_total_env},
        "total": {"Lambda_total_Hz": L_total},
        "channels": channels,
        "dominant_channel": dominant[0],
        "dominant_env_channel": dominant_env[0],
        "snr": snr,
        "grut_detectable": snr > 0.01,
        "grut_dominant": snr > 1,
        "params": {
            "m_kg": m_kg, "l_m": l_m, "R_m": R_m,
            "P_Pa": P_Pa, "T_K": T_K,
            "laser_W": laser_power_W,
            "isolation": isolation, "shielding": shielding,
        },
    }


def optimize_experiment(m_kg, l_m, rho=19300, target_snr=1.0):
    """Find the experimental parameters needed to achieve a target SNR."""
    R = (3 * m_kg / (4 * np.pi * rho))**(1/3)
    L_grav = G * m_kg**2 * min(1, (l_m/R)**3/6) / (HBAR * l_m)
    
    # Required total env noise for target SNR
    L_env_required = L_grav / target_snr
    
    # Scan parameter combinations
    best = None
    for T in [300, 77, 20, 4, 1, 0.1]:
        for P_log in range(-8, -17, -1):
            P = 10**P_log
            for shielding in ["none", "basic", "good", "excellent", "state_of_art"]:
                for isolation in ["poor", "standard", "good", "excellent", "state_of_art"]:
                    budget = full_noise_budget(m_kg, l_m, R, P, T, 1e-4, isolation, shielding)
                    if budget["snr"] >= target_snr:
                        difficulty = (300/max(T,0.01)) + abs(P_log) + \
                                     {"none":0,"basic":1,"good":2,"excellent":3,"state_of_art":4}[shielding] + \
                                     {"poor":0,"standard":1,"good":2,"excellent":3,"state_of_art":4}[isolation]
                        if best is None or difficulty < best["difficulty"]:
                            best = {
                                "T_K": T, "P_Pa": P,
                                "shielding": shielding, "isolation": isolation,
                                "snr": budget["snr"],
                                "difficulty": difficulty,
                                "dominant_noise": budget["dominant_env_channel"],
                            }
    
    return {
        "target_snr": target_snr,
        "Lambda_grav_Hz": L_grav,
        "L_env_required_Hz": L_env_required,
        "optimal": best,
        "achievable": best is not None,
    }
