#!/usr/bin/env python3
"""
Gate 3 Hminus-Derivative-Regularized Phase A: Laurent Extraction (Python Implementation)

Purpose: Compute I(h_-, epsilon) for multiple h_- values and extract Laurent expansion
Uses scipy for hypergeometric functions and numerical integration.

Specification version: gate3-hminus-dr-spec-v1.0
Date: May 16, 2026
"""

import json
import numpy as np
from scipy.integrate import quad
from scipy.special import hyp2f1
from pathlib import Path
from datetime import datetime
from numpy.polynomial import polynomial as P

print("\n" + "="*60)
print("Gate 3 Phase A: Laurent Extraction (Python)")
print("Specification: gate3-hminus-dr-spec-v1.0")
print("Start time:", datetime.now().isoformat())
print("="*60 + "\n")

# ===== Setup =====

# Get script directory and create output directory
script_dir = Path(__file__).parent.absolute()
output_dir = script_dir / "gate3_outputs"
output_dir.mkdir(exist_ok=True)
output_file = output_dir / "gate3_hminus_dr_laurent_extraction.json"

print(f"Output directory: {output_dir}")
print(f"Output file: {output_file}\n")

# ===== Configuration =====

h_minus_values = [0.1, 0.05, 0.02, 0.01, 0.005, 0.002, 0.001]
epsilon_values = [0.01, 0.005, 0.002, 0.001]

print(f"h_minus values: {h_minus_values}")
print(f"epsilon values: {epsilon_values}")
print(f"Total samples to compute: {len(h_minus_values) * len(epsilon_values)}\n")

# ===== Define Integral =====

def define_integral(alpha, eps):
    """
    Define the integrand for I(alpha, epsilon)
    
    I(alpha, epsilon) = 2 * 4^{(D-3)/2} * Integral_0^1 
                        2F1(h_+, alpha; D/2; u)^3 * u^{(D-3)/2} * (1-u)^{(D-3)/2} du
    
    where h_+ = D - 1, D = 4 - 2*epsilon
    """
    D = 4 - 2*eps
    hplus = D - 1
    
    prefactor = 2 * (4 ** ((D - 3) / 2))
    
    def integrand(u):
        try:
            hyp_val = hyp2f1(hplus, alpha, D/2, u)
            result = prefactor * (hyp_val ** 3) * (u ** ((D - 3) / 2)) * ((1 - u) ** ((D - 3) / 2))
            return result
        except Exception as e:
            print(f"    Error in integrand at u={u}: {e}")
            return 0
    
    return integrand

# ===== Sample Collection =====

print("Beginning sample collection...\n")

samples = []
successful_count = 0
total_samples = len(h_minus_values) * len(epsilon_values)

for h_idx, h_val in enumerate(h_minus_values):
    for e_idx, eps_val in enumerate(epsilon_values):
        sample_num = h_idx * len(epsilon_values) + e_idx + 1
        
        print(f"Sample {sample_num} of {total_samples}: h_- = {h_val}, eps = {eps_val}")
        
        # Define integrand for this (h_val, eps_val) pair
        integrand = define_integral(h_val, eps_val)
        
        # Numerically integrate
        try:
            result, error = quad(integrand, 0, 1, limit=100, epsabs=1e-20, epsrel=1e-15)
            
            if np.isfinite(result) and not np.isnan(result):
                samples.append((h_val, eps_val, result))
                successful_count += 1
                print(f"  Result: {result:.10e} (error estimate: {error:.2e})")
            else:
                print(f"  FAILED: Non-finite result {result}")
        except Exception as e:
            print(f"  FAILED: {type(e).__name__}: {e}")

print(f"\nSample collection complete")
print(f"Total samples: {len(samples)}")
print(f"Successful samples: {successful_count}\n")

# ===== Laurent Fitting in h_- =====

print("Performing Laurent expansion fitting in h_-...\n")

successful_samples = samples  # All in samples list are successful

if len(successful_samples) < 5:
    print(f"ERROR: Insufficient samples ({len(successful_samples)} < 5)")
    print("Cannot proceed with fitting.")
    exit(1)

# Fit Laurent expansion for each epsilon
laurent_coefficients = {}
pole_order = 0

for eps_val in epsilon_values:
    # Extract data for this epsilon
    data_this_eps = [s for s in successful_samples if s[1] == eps_val]
    
    print(f"Epsilon {eps_val}: {len(data_this_eps)} samples")
    
    if len(data_this_eps) >= 3:
        # Prepare data as (h_-, I) pairs
        h_data = np.array([s[0] for s in data_this_eps])
        I_data = np.array([s[2] for s in data_this_eps])
        
        # Fit polynomial up to degree 3 in h
        # Using numpy polynomial (coefficients in ascending order)
        coeffs = np.polyfit(h_data, I_data, 3)  # Returns [c3, c2, c1, c0]
        coeffs_asc = coeffs[::-1]  # Reverse to get ascending order [c0, c1, c2, c3]
        
        # Extract coefficients
        coeff_0 = float(coeffs_asc[0])
        coeff_1 = float(coeffs_asc[1]) if len(coeffs_asc) > 1 else 0
        coeff_2 = float(coeffs_asc[2]) if len(coeffs_asc) > 2 else 0
        coeff_3 = float(coeffs_asc[3]) if len(coeffs_asc) > 3 else 0
        
        # Calculate R² (coefficient of determination)
        y_pred = np.polyval(coeffs, h_data)
        ss_res = np.sum((I_data - y_pred) ** 2)
        ss_tot = np.sum((I_data - np.mean(I_data)) ** 2)
        r2 = 1 - (ss_res / ss_tot) if ss_tot > 0 else 0
        
        laurent_coefficients[str(eps_val)] = {
            "A_0": coeff_0,
            "A_1": coeff_1,
            "A_2": coeff_2,
            "A_3": coeff_3,
            "fit_r2": r2
        }
        
        # Track pole order
        if abs(coeff_1) > 0.1 * abs(coeff_0):
            pole_order = max(pole_order, 1)
        
        print(f"  A_0 = {coeff_0:.10e}")
        print(f"  A_1 = {coeff_1:.10e}")
        print(f"  R² = {r2:.10f}\n")
    else:
        print(f"  WARNING: Insufficient data for this epsilon\n")

print(f"Fitted {len(laurent_coefficients)} epsilon values")
print(f"Empirically determined pole order: {pole_order}\n")

# ===== Build Output JSON =====

print("Building output JSON...\n")

# Build I_samples dictionary
i_samples_dict = {}
for sample in successful_samples:
    key = f"{sample[0]:.5f}_{sample[1]:.5f}"
    i_samples_dict[key] = float(sample[2])

output_json = {
    "spec_version": "1.0",
    "date": datetime.now().isoformat(),
    "h_minus_values": h_minus_values,
    "epsilon_values": epsilon_values,
    "total_samples": len(samples),
    "successful_samples": len(successful_samples),
    "I_samples": i_samples_dict,
    "laurent_fit": {
        "pole_order": pole_order,
        "coefficients": laurent_coefficients,
        "fit_quality": {
            "method": "numpy.polyfit degree 3",
            "avg_r2": float(np.mean([laurent_coefficients[str(eps)]["fit_r2"] for eps in epsilon_values if str(eps) in laurent_coefficients]))
        }
    }
}

# ===== Write Output =====

print("Writing output to file...")

with open(output_file, 'w') as f:
    json.dump(output_json, f, indent=2)

if output_file.exists():
    print(f"SUCCESS: Output written to {output_file}")
    print(f"File size: {output_file.stat().st_size} bytes\n")
else:
    print(f"ERROR: Output file not created\n")
    exit(1)

print("="*60)
print("Phase A COMPLETE")
print("Specification: gate3-hminus-dr-spec-v1.0")
print(f"Output: {output_file}")
print("End time:", datetime.now().isoformat())
print("="*60 + "\n")
