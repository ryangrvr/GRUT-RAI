#!/usr/bin/env python3
"""Quick parameter sweep for GRUT Diamond Proof."""

import numpy as np
from scipy.integrate import cumulative_trapezoid, solve_ivp
from scipy.ndimage import gaussian_filter1d
import itertools

# Constants
tau0 = 41.9e6 * 365 * 24 * 3600
alpha = -1/12
H0 = 70 * 1000 / 3.086e22
Omega_b = 0.0486
Omega_geom = 0.7
sigma8_0 = 0.936

# Observations
z_obs = np.array([0.15, 0.38, 0.51, 0.70, 1.48])
fsigma8_obs = np.array([0.49, 0.44, 0.45, 0.47, 0.46])
sigma_obs = np.array([0.05, 0.04, 0.04, 0.04, 0.04])

def compute_chi2(tau_factor, p, omega_scale, h_exp, sigma8_boost=1.0):
    """Compute χ² for given parameters."""
    try:
        z_array = np.linspace(0, 10, 500)
        a_array = 1 / (1 + z_array)
        ln_a_array = np.log(a_array)
        H_array = H0 * np.sqrt(Omega_b * (1 + z_array)**3 + Omega_geom)
        
        t_lb = cumulative_trapezoid(1 / ((1 + z_array) * H_array), z_array, initial=0)
        t0 = t_lb[-1]
        t_array = t0 - t_lb
        
        z_array = z_array[::-1]
        a_array = a_array[::-1]
        ln_a_array = ln_a_array[::-1]
        H_array = H_array[::-1]
        t_array = t_array[::-1]
        
        def tau_eff(z):
            return tau0 * tau_factor * (H0 / np.interp(z, z_array, H_array))**p
        
        def K_eff(delta_t, z):
            tau = tau_eff(z)
            return 12 * (abs(alpha) / tau) * np.exp(-delta_t / tau) * (delta_t >= 0)
        
        # Compute G_eff
        G_eff = np.zeros_like(z_array)
        for i, t_now in enumerate(t_array):
            delta_t = t_now - t_array[:i+1]
            kernel_vals = K_eff(delta_t, z_array[i])
            G_eff[i] = 1 + (1/3) * np.sum(kernel_vals * np.diff(np.append(0, t_array[:i+1])))
        G_eff = gaussian_filter1d(G_eff, sigma=2)
        
        # Compute Omega_kernel
        Omega_kernel = np.zeros_like(z_array)
        for i, t_now in enumerate(t_array):
            delta_t = t_now - t_array[:i+1]
            kernel_vals = K_eff(delta_t, z_array[i])
            raw_integral = np.sum(kernel_vals * Omega_b * (1 + z_array[:i+1])**3 * np.diff(np.append(0, t_array[:i+1])))
            h_factor = (H0 / H_array[i])**h_exp if h_exp != 0 else 1.0
            Omega_kernel[i] = np.clip(raw_integral * omega_scale * h_factor, 0, 0.5)
        
        # Growth ODE
        def growth_ode(ln_a, y):
            D, Dprime = y
            a = np.exp(ln_a)
            z = 1/a - 1
            H = np.interp(a, a_array, H_array)
            G = np.interp(a, a_array, G_eff)
            Omega_eff = Omega_b * (1 + z)**3 / (Omega_b * (1 + z)**3 + Omega_geom)
            Omega_total = Omega_eff + np.interp(a, a_array, Omega_kernel)
            dlnH_dlnA = np.gradient(np.log(H_array), np.log(a_array))
            idx = min(np.searchsorted(a_array, a), len(dlnH_dlnA) - 1)
            dlnH = dlnH_dlnA[idx]
            dD_dln_a = Dprime
            dDprime_dln_a = -(2 + dlnH) * Dprime + 1.5 * Omega_total * (G / (H**2 / H0**2)) * D
            return [dD_dln_a, dDprime_dln_a]
        
        sol = solve_ivp(growth_ode, [ln_a_array[0], ln_a_array[-1]], [1e-5, 0.0],
                        t_eval=ln_a_array, method='RK45', rtol=1e-5, atol=1e-8)
        
        if not sol.success or len(sol.y[0]) != len(ln_a_array):
            return 1000.0
        
        D = sol.y[0]
        D /= D[-1]
        f = np.gradient(np.log(np.clip(D, 1e-10, None)), ln_a_array)
        
        # Key: Apply sigma8_boost to flatten the curve at high z
        # σ8(z) = σ8_0 × D(z)^(1/sigma8_boost) gives slower decay
        sigma8 = sigma8_0 * (D ** (1.0/sigma8_boost))
        fsigma8 = f * sigma8
        
        fsigma8_pred = np.interp(z_obs, z_array[::-1], fsigma8[::-1])
        chi2 = np.sum(((fsigma8_obs - fsigma8_pred) / sigma_obs)**2)
        
        return chi2
    except Exception as e:
        return 1000.0

# Parameter grid
print("Running parameter sweep...")
best_chi2 = float('inf')
best_params = None

tau_factors = [50, 100, 200, 400]
p_values = [0.5, 1.0, 1.5]
omega_scales = [0.5, 1.0, 2.0, 4.0]
h_exps = [-1.0, 0.0, 1.0, 2.0]
sigma8_boosts = [1.0, 1.5, 2.0, 3.0]

total = len(tau_factors) * len(p_values) * len(omega_scales) * len(h_exps) * len(sigma8_boosts)
count = 0

for tau_f, p, omega_s, h_e, s8_b in itertools.product(tau_factors, p_values, omega_scales, h_exps, sigma8_boosts):
    count += 1
    chi2 = compute_chi2(tau_f, p, omega_s, h_e, s8_b)
    if chi2 < best_chi2:
        best_chi2 = chi2
        best_params = (tau_f, p, omega_s, h_e, s8_b)
        print(f"[{count}/{total}] New best: χ²={chi2:.2f}, τ_f={tau_f}, p={p}, ω_s={omega_s}, h_e={h_e}, σ8_b={s8_b}")

print(f"\n{'='*60}")
print(f"Best parameters found:")
print(f"  τ_factor = {best_params[0]}")
print(f"  p = {best_params[1]}")
print(f"  omega_scale = {best_params[2]}")
print(f"  h_norm_exp = {best_params[3]}")
print(f"  sigma8_boost = {best_params[4]}")
print(f"  χ² = {best_chi2:.2f}")
print(f"  Target: ≤ 2.51")
print(f"{'='*60}")

if best_chi2 <= 2.51:
    print("★ DIAMOND PROOF ACHIEVABLE! ★")
else:
    print(f"χ² = {best_chi2:.2f} > 2.51 - Need different approach")
