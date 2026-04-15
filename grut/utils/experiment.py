"""
Experiment Designer — Design experiments to test GRUT predictions.

Given a GRUT prediction, compute: required sensitivity, optimal materials,
feasibility assessment, and technology gap.
"""
import numpy as np
from grut.foundation.constants import G, HBAR, AMU, K_B
from grut.foundation.noise_kernel import lambda_grav, extended_body_suppression

MATERIALS = {
    "gold": 19300, "silica": 2200, "diamond": 3510,
    "silicon": 2330, "tungsten": 19250, "osmium": 22590,
}

def design_decoherence_experiment(target_Lambda_Hz=100, t_obs_s=0.01, T_K=0.01):
    """Design an experiment to measure gravitational decoherence at a target rate."""
    results = {}
    for mat, rho in MATERIALS.items():
        # For each material, find the mass needed to get target_Lambda at l = 2R (far field, S=1)
        # Lambda = G m^2 / (hbar l) → m = sqrt(Lambda * hbar * l / G)
        # With l = 2R and m = (4/3)pi R^3 rho → solve for R
        # Lambda = G ((4/3)pi R^3 rho)^2 / (hbar * 2R) = G (4/3)^2 pi^2 rho^2 R^5 / (2 hbar)
        # R^5 = 2 hbar Lambda / (G (4/3)^2 pi^2 rho^2)
        R5 = 2*HBAR*target_Lambda_Hz / (G * (4*np.pi/3)**2 * rho**2)
        if R5 <= 0: continue
        R = R5**(1/5)
        m = (4/3)*np.pi*R**3*rho
        l = 2*R

        # Thermal decoherence rate (gas collisions): needs P < threshold
        # Lambda_thermal ~ P * sigma / (m_gas * v_thermal * hbar) × stuff
        # Simplified: need P such that Lambda_thermal < Lambda_grav
        v_thermal = np.sqrt(K_B * T_K / (29 * AMU))  # residual gas
        sigma_coll = np.pi * R**2
        P_required = target_Lambda_Hz * 29*AMU * v_thermal / sigma_coll  # very rough

        results[mat] = {
            "density": rho, "R_m": R, "R_um": R*1e6,
            "mass_kg": m, "mass_pg": m*1e15, "mass_amu": m/AMU,
            "l_m": l, "l_um": l*1e6,
            "Lambda_predicted_Hz": lambda_grav(m, l, R),
            "P_required_Pa": P_required,
            "t_coh_ms": 1000/target_Lambda_Hz,
            "feasibility": "within reach" if m*1e15 < 1000 and P_required > 1e-12 else "challenging",
        }

    # Technology gap assessment
    current = {"mass_amu_max": 2.5e4, "separation_nm_max": 10, "pressure_Pa": 1e-8, "temp_K": 0.01}
    best = min(results.items(), key=lambda x: abs(x[1]["Lambda_predicted_Hz"] - target_Lambda_Hz))

    return {
        "target_Lambda_Hz": target_Lambda_Hz,
        "materials": results,
        "best_material": best[0],
        "current_state_of_art": current,
        "technology_gap": {
            "mass_gap": best[1]["mass_amu"] / current["mass_amu_max"],
            "separation_gap": best[1]["l_m"]*1e9 / current["separation_nm_max"],
            "pressure_gap": current["pressure_Pa"] / best[1]["P_required_Pa"],
        }
    }

def snr_calculator(m, l, R, t_integration, Lambda_noise_Hz=0):
    """Signal-to-noise ratio for detecting gravitational decoherence."""
    Lambda_grav_val = lambda_grav(m, l, R)
    signal = Lambda_grav_val * t_integration  # number of decoherence events
    noise = Lambda_noise_Hz * t_integration + np.sqrt(Lambda_noise_Hz * t_integration)
    snr = signal / max(noise, 1) if noise > 0 else signal
    return {"Lambda_grav_Hz": Lambda_grav_val, "Lambda_noise_Hz": Lambda_noise_Hz,
            "t_integration_s": t_integration, "signal_events": signal,
            "noise_events": noise, "SNR": snr,
            "detectable": snr > 3, "sigma": snr}

def optimal_material(target_mass_kg, target_separation_m):
    """Find the best material for a given mass and separation."""
    results = {}
    for mat, rho in MATERIALS.items():
        R = ((3*target_mass_kg)/(4*np.pi*rho))**(1/3)
        L = lambda_grav(target_mass_kg, target_separation_m, R)
        S = extended_body_suppression(target_separation_m, R)
        results[mat] = {"rho": rho, "R_m": R, "Lambda_Hz": L, "S_l_R": S,
                        "kink_at_m": 1.8*R, "in_far_field": target_separation_m > 2*R}
    best = max(results.items(), key=lambda x: x[1]["Lambda_Hz"])
    return {"materials": results, "best": best[0], "best_Lambda": best[1]["Lambda_Hz"]}
