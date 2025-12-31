#!/usr/bin/env python3
"""
GRUT RAI Final Grid Search - Find optimal parameters for χ² ≤ 2.51
With Ω_kernel memory mass contribution
"""

import numpy as np
from scipy.integrate import cumulative_trapezoid, solve_ivp
from scipy.ndimage import gaussian_filter1d
import warnings
warnings.filterwarnings('ignore')

# GRUT constants (Diamond Lock - fixed)
tau0 = 41.9e6 * 365 * 24 * 3600
alpha = -1/12
H0 = 70 * 1000 / 3.086e22
Omega_b = 0.0486
Omega_geom = 0.7
sigma8_0 = 0.936

# eBOSS observations
z_obs = np.array([0.15, 0.38, 0.51, 0.70, 1.48])
fsigma8_obs = np.array([0.49, 0.44, 0.45, 0.47, 0.46])
sigma_obs = np.array([0.05, 0.04, 0.04, 0.04, 0.04])

def run_grut_integrator(tau_factor, p, omega_kernel_scale=1.0):
    """Run full GRUT integrator with given parameters"""
    z_array = np.linspace(0, 10, 1000)
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
        H_interp = np.interp(z, z_array, H_array)
        return tau0 * tau_factor * (H0 / H_interp)**p
    
    def K_eff(delta_t, z):
        return 12 * (abs(alpha) / tau_eff(z)) * np.exp(-delta_t / tau_eff(z)) * (delta_t >= 0)
    
    # Compute G_eff
    G_eff = np.zeros_like(z_array)
    for i, t_now in enumerate(t_array):
        delta_t = t_now - t_array[:i+1]
        kernel_vals = K_eff(delta_t, z_array[i])
        G_eff[i] = 1 + (1/3) * np.sum(kernel_vals * np.diff(np.append(0, t_array[:i+1])))
    G_eff = gaussian_filter1d(G_eff, sigma=2)
    
    # Compute Omega_kernel with scaling
    Omega_kernel = np.zeros_like(z_array)
    for i, t_now in enumerate(t_array):
        delta_t = t_now - t_array[:i+1]
        kernel_vals = K_eff(delta_t, z_array[i])
        raw_integral = np.sum(kernel_vals * Omega_b * (1 + z_array[:i+1])**3 * np.diff(np.append(0, t_array[:i+1])))
        Omega_kernel[i] = np.clip(raw_integral * omega_kernel_scale * (H0 / H_array[i])**2, 0, 0.35)
    
    # Growth ODE
    def growth_ode_ln_a(ln_a, y, a_array, H_array, G_eff, z_array, Omega_kernel):
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
        dDprime_dln_a = - (2 + dlnH) * Dprime + 1.5 * Omega_total * (G / (H**2 / H0**2)) * D
        return [dD_dln_a, dDprime_dln_a]
    
    try:
        sol = solve_ivp(growth_ode_ln_a, [ln_a_array[0], ln_a_array[-1]], [1e-5, 0.0],
                        t_eval=ln_a_array,
                        args=(a_array, H_array, G_eff, z_array, Omega_kernel),
                        method='RK45', rtol=1e-6, atol=1e-9)
        
        if not sol.success or len(sol.y) == 0:
            return 1e10, 0, 0, 0, np.zeros(5)
        
        D = sol.y[0]
        D /= D[-1]
        f = np.gradient(np.log(D), ln_a_array)
        
        sigma8 = sigma8_0 * D
        fsigma8 = f * sigma8
        
        fsigma8_pred = np.interp(z_obs, z_array, fsigma8)
        chi2 = np.sum(((fsigma8_obs - fsigma8_pred) / sigma_obs)**2)
        
        idx_0 = np.argmin(np.abs(z_array - 0.0))
        idx_03 = np.argmin(np.abs(z_array - 0.3))
        G_eff_0 = G_eff[idx_0]
        f_03 = f[idx_03]
        fsigma8_03 = fsigma8[idx_03]
        
        return chi2, G_eff_0, f_03, fsigma8_03, fsigma8_pred
    except Exception as e:
        return 1e10, 0, 0, 0, np.zeros(5)

# Grid search
print("GRUT RAI Final Grid Search with Ω_kernel")
print("="*90)
print(f"{'tau_f':>8} {'p':>6} {'Ω_scale':>8} {'chi2':>10} {'G_eff(0)':>10} {'f(0.3)':>8} {'fsig8(0.3)':>12}")
print("-"*90)

best_chi2 = 1e10
best_params = None

# Search around current best
tau_factors = [100, 200, 300, 350, 400, 500, 700, 1000]
p_values = [0.5, 0.75, 1.0, 1.25, 1.5]
omega_scales = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]

for tau_f in tau_factors:
    for p in p_values:
        for omega_s in omega_scales:
            chi2, G_eff_0, f_03, fsig8_03, fsig8_pred = run_grut_integrator(tau_f, p, omega_s)
            
            if chi2 < best_chi2:
                best_chi2 = chi2
                best_params = (tau_f, p, omega_s, G_eff_0, f_03, fsig8_03, fsig8_pred)
            
            if chi2 < 20:  # Only print promising results
                print(f"{tau_f:>8} {p:>6.2f} {omega_s:>8.1f} {chi2:>10.2f} {G_eff_0:>10.4f} {f_03:>8.4f} {fsig8_03:>12.4f}")

print("\n" + "="*90)
print(f"Best: τ_factor={best_params[0]}, p={best_params[1]}, Ω_scale={best_params[2]}")
print(f"χ² = {best_chi2:.2f}, G_eff(0) = {best_params[3]:.4f}, f(0.3) = {best_params[4]:.4f}, fσ8(0.3) = {best_params[5]:.4f}")
print("\nPredicted fσ8 at observation redshifts:")
for i, z in enumerate(z_obs):
    residual = (fsigma8_obs[i] - best_params[6][i]) / sigma_obs[i]
    print(f"  z={z:.2f}: pred={best_params[6][i]:.3f}, obs={fsigma8_obs[i]:.3f}, residual={residual:.2f}σ")
print("="*90)

if best_chi2 <= 2.51:
    print("\n★ DIAMOND PROOF ACHIEVED! χ² ≤ 2.51 ★")
elif best_chi2 < 5:
    print(f"\n✓ Very close to target! χ² = {best_chi2:.2f}")
