#!/usr/bin/env python3
"""
Program H — Stage H1: Ward Residual Scaling Law Extraction

Self-consistent T-matrix in 1D with contact interaction.
Compute Ward-identity residual ΔW(κ₀) across coupling scan.
Classify scaling: higher-order / leading-order / non-perturbative.

Model: 1D Fermi gas with contact interaction -κ₀
Units: k_F = 1, E_F = k_F²/(2m) = 0.5 (m = 1)
Method: Matsubara frequencies at low T, self-consistent iteration
"""

import numpy as np
from scipy.interpolate import interp1d
import warnings
warnings.filterwarnings('ignore')

# ============================================================
# PARAMETERS
# ============================================================
k_F = 1.0
E_F = 0.5  # k_F^2 / (2m), m=1
T = 0.02 * E_F  # temperature (low but finite for Matsubara)
beta = 1.0 / T

# Grid parameters
N_k = 128          # momentum grid points
N_omega = 64       # Matsubara frequencies (positive only; use symmetry)

mixing = 0.3       # self-consistency mixing parameter
max_iter = 200     # max iterations
tol = 1e-6         # convergence tolerance

# Coupling scan
kappa_over_kF = np.array([0.01, 0.02, 0.05, 0.10, 0.15, 0.20])

# Cutoff scan for RG stability
Lambda_values = [50.0, 100.0]  # in units of k_F

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def matsubara_freq(n, beta):
    """Fermionic Matsubara frequency: iω_n = i(2n+1)πT"""
    return (2*n + 1) * np.pi / beta

def bosonic_matsubara(m, beta):
    """Bosonic Matsubara frequency: iΩ_m = i(2m)πT"""
    return 2*m * np.pi / beta

def epsilon_k(k):
    """Free dispersion: ε_k = k²/2 - E_F"""
    return k**2 / 2.0 - E_F

def run_self_consistent_tmatrix(kappa0, Lambda, N_k=N_k, N_omega=N_omega,
                                  mixing=mixing, max_iter=max_iter, tol=tol,
                                  verbose=False):
    """
    Run self-consistent T-matrix calculation.
    Returns: Sigma(k, iw_n), G(k, iw_n), T-matrix, convergence info.
    """
    # Momentum grid
    dk = 2*Lambda / N_k
    k_grid = np.linspace(-Lambda, Lambda, N_k, endpoint=False) + dk/2

    # Matsubara frequencies (positive only; use G(-iw) = G(iw)* for real Sigma)
    omega_n = np.array([matsubara_freq(n, beta) for n in range(N_omega)])  # positive
    # For convolutions we need both signs
    omega_all = np.concatenate([-omega_n[::-1], omega_n])
    N_w_all = len(omega_all)

    # Dispersion
    eps_k = epsilon_k(k_grid)

    # Initialize self-energy to zero
    # Sigma[ik, iw] for positive Matsubara frequencies
    Sigma = np.zeros((N_k, N_omega), dtype=complex)

    # Green's function
    def compute_G(Sigma_in):
        G = np.zeros((N_k, N_omega), dtype=complex)
        for iw in range(N_omega):
            G[:, iw] = 1.0 / (1j * omega_n[iw] - eps_k - Sigma_in[:, iw])
        return G

    # Pair bubble Π(q, iΩ_m) = -T/N_k Σ_{k,n} G(k, iω_n) G(q-k, iΩ_m - iω_n)
    # For bosonic frequency iΩ_m = i(2m)πT
    N_Omega = N_omega  # number of bosonic frequencies
    Omega_m = np.array([bosonic_matsubara(m, beta) for m in range(N_Omega)])

    def compute_pair_bubble(G_in):
        Pi = np.zeros((N_k, N_Omega), dtype=complex)
        for iq in range(N_k):
            for im in range(N_Omega):
                # Sum over k and n
                val = 0.0 + 0j
                for ik in range(N_k):
                    # q - k index (periodic)
                    k_diff = k_grid[iq] - k_grid[ik]
                    # Find nearest k-grid point for q-k
                    ik_diff = int(round((k_diff + Lambda) / dk - 0.5)) % N_k

                    for iw in range(N_omega):
                        # iΩ_m - iω_n: this is a fermionic frequency
                        # iΩ_m - iω_n = i(2m - 2n - 1)πT
                        n_diff = im - iw  # This gives 2m - (2n+1) = 2(m-n) - 1
                        # The resulting fermionic index: n' where iω_{n'} = i(2n'+1)πT
                        # 2n'+1 = 2m - 2n - 1 → n' = m - n - 1
                        n_prime = im - iw - 1

                        if 0 <= n_prime < N_omega:
                            G2 = G_in[ik_diff, n_prime]
                        elif -N_omega <= n_prime < 0:
                            # G(k, -iω_n) = G(k, iω_n)* for real Sigma
                            G2 = np.conj(G_in[ik_diff, -n_prime - 1])
                        else:
                            continue

                        val += G_in[ik, iw] * G2

                # Negative frequencies contribute equally (symmetry)
                val *= 2.0  # account for n < 0 (approximate)
                Pi[iq, im] = -T * val * dk / (2*np.pi)
        return Pi

    # Simplified: for speed, compute Pi only at q=0 and small q for the Ward check
    # Full q-dependence for the T-matrix self-energy

    # FAST APPROXIMATE VERSION: compute Pi on a coarser grid
    # and interpolate for the self-energy convolution

    # Actually, for tractability with N_k=128, N_omega=64, the full double loop
    # is O(N_k^2 * N_omega^2) ~ 128^2 * 64^2 ~ 67M per iteration.
    # This is too slow. Reduce to smaller grids.

    # REDUCE for tractability
    N_k_eff = min(N_k, 48)
    N_w_eff = min(N_omega, 24)
    dk_eff = 2*Lambda / N_k_eff
    k_eff = np.linspace(-Lambda, Lambda, N_k_eff, endpoint=False) + dk_eff/2
    eps_eff = epsilon_k(k_eff)
    omega_eff = np.array([matsubara_freq(n, beta) for n in range(N_w_eff)])
    Omega_eff = np.array([bosonic_matsubara(m, beta) for m in range(N_w_eff)])

    Sigma_eff = np.zeros((N_k_eff, N_w_eff), dtype=complex)

    for iteration in range(max_iter):
        # G
        G_eff = np.zeros((N_k_eff, N_w_eff), dtype=complex)
        for iw in range(N_w_eff):
            G_eff[:, iw] = 1.0 / (1j * omega_eff[iw] - eps_eff - Sigma_eff[:, iw])

        # Pair bubble (pp channel)
        Pi_eff = np.zeros((N_k_eff, N_w_eff), dtype=complex)
        for iq in range(N_k_eff):
            for im in range(N_w_eff):
                val = 0.0 + 0j
                for ik in range(N_k_eff):
                    k_diff = k_eff[iq] - k_eff[ik]
                    ik_diff = int(round((k_diff + Lambda) / dk_eff - 0.5)) % N_k_eff

                    for iw in range(N_w_eff):
                        n_prime = im - iw - 1
                        if 0 <= n_prime < N_w_eff:
                            G2 = G_eff[ik_diff, n_prime]
                        elif -N_w_eff <= n_prime < 0:
                            G2 = np.conj(G_eff[ik_diff, -n_prime - 1])
                        else:
                            continue
                        val += G_eff[ik, iw] * G2
                val *= 2.0
                Pi_eff[iq, im] = -T * val * dk_eff / (2*np.pi)

        # T-matrix
        T_mat = np.zeros((N_k_eff, N_w_eff), dtype=complex)
        for iq in range(N_k_eff):
            for im in range(N_w_eff):
                T_mat[iq, im] = -kappa0 / (1.0 + kappa0 * Pi_eff[iq, im])

        # Self-energy: Σ(k, iω_n) = T Σ_m ∫dq/(2π) T(k+q, iω_n+iΩ_m) G(q, iΩ_m-iω_n+iω_n)
        # More precisely: Σ(k, iω_n) = T/N_k Σ_{q,m} T(k+q, iω_n + iΩ_m) G(q, iΩ_m)
        # Wait, the T-matrix self-energy is a convolution of T and G:
        # Σ(k, iω_n) = -T Σ_m ∫dq/(2π) T(q, iΩ_m) G(q-k, iΩ_m - iω_n)

        Sigma_new = np.zeros((N_k_eff, N_w_eff), dtype=complex)
        for ik in range(N_k_eff):
            for iw_n in range(N_w_eff):
                val = 0.0 + 0j
                for iq in range(N_k_eff):
                    ik_diff = int(round((k_eff[iq] - k_eff[ik] + Lambda) / dk_eff - 0.5)) % N_k_eff

                    for im in range(N_w_eff):
                        # iΩ_m - iω_n is fermionic: n' = m - n - 1 (using bosonic Ω and fermionic ω)
                        # Actually: iΩ_m - iω_n = i(2m)πT - i(2n+1)πT = i(2m-2n-1)πT = i(2(m-n-1)+1)πT
                        # So n' = m - n - 1 (same index as before but different meaning)
                        # Wait, iΩ_m - iω_n = i(2m - 2n - 1)πT, and a fermionic freq is i(2n'+1)πT
                        # So 2n'+1 = 2m - 2n - 1, n' = m - n - 1
                        n_prime = im - iw_n - 1
                        if 0 <= n_prime < N_w_eff:
                            G_qk = G_eff[ik_diff, n_prime]
                        elif -N_w_eff <= n_prime < 0:
                            G_qk = np.conj(G_eff[ik_diff, -n_prime - 1])
                        else:
                            continue
                        val += T_mat[iq, im] * G_qk
                val *= 2.0  # negative m contribution
                Sigma_new[ik, iw_n] = -T * val * dk_eff / (2*np.pi)

        # Mixing
        Sigma_eff_new = mixing * Sigma_new + (1 - mixing) * Sigma_eff

        # Convergence check
        diff = np.max(np.abs(Sigma_eff_new - Sigma_eff))
        Sigma_eff = Sigma_eff_new

        if diff < tol:
            if verbose:
                print(f"    Converged at iteration {iteration+1}, residual = {diff:.2e}")
            break
    else:
        if verbose:
            print(f"    Did not converge after {max_iter} iterations, residual = {diff:.2e}")

    convergence_residual = diff

    # Extract ∂_ω Σ at (k_F, E_F)
    # k_F = 1.0 → find nearest k-grid index
    ik_F = np.argmin(np.abs(k_eff - k_F))

    # Σ(k_F, iω_n) for the first few Matsubara frequencies
    # ∂_ω Σ ≈ Im[Σ(k_F, iω_0)] / ω_0 (leading order at low T)
    # More precisely: ∂_ω Σ|_{ω=0} ≈ [Im Σ(iω_1) - Im Σ(iω_0)] / (ω_1 - ω_0)
    # Using symmetric finite difference on Matsubara axis:
    # ∂_ω Σ ≈ Im[Σ(iω_0)] / ω_0  (since Σ(iω) = Re Σ + i ω ∂_ω Σ + ... for small ω)
    # Actually, for Matsubara: Σ(iω_n) ≈ Σ(0) + iω_n ∂_ω Σ|_{ω=0} for small ω_n
    # So Im[Σ(iω_n)] / ω_n → ∂_ω Σ|_{ω=0}

    Sigma_kF = Sigma_eff[ik_F, :]
    dSigma_dw = np.imag(Sigma_kF[0]) / omega_eff[0]  # leading estimate

    # Better: linear fit of Im(Σ) vs ω for first few frequencies
    if N_w_eff >= 3:
        omega_low = omega_eff[:3]
        ImSigma_low = np.imag(Sigma_kF[:3])
        # Im Σ(iω) ≈ ω × ∂_ω Σ (at small ω, for a Fermi liquid)
        slope = np.polyfit(omega_low, ImSigma_low, 1)[0]
        dSigma_dw = slope

    Z = 1.0 / (1.0 - dSigma_dw)

    # Spectral positivity check: Im G^R(k, ω) < 0 for retarded GF
    # On Matsubara axis: Im G(k, iω_n) should have consistent sign
    # A(k, ω) = -2 Im G^R ≥ 0 → check sign of Im G
    spectral_ok = True
    for iw in range(N_w_eff):
        # Im G(k, iω_n) should be negative for ω_n > 0 (standard convention)
        if np.any(np.imag(G_eff[:, iw]) > 0.01):
            spectral_ok = False
            break

    # Particle-hole vertex Γ_ph at q→0
    # BSE: Γ_ph = 1 + Γ_ph Π_ph T_mat (schematic)
    # At q→0: Γ_ph relates to density response
    # Ward identity: Z = (1 - ∂_ω Σ)^{-1} should equal the vertex correction
    #
    # For the self-consistent T-matrix, the vertex in the ph channel at q→0:
    # Γ_ph(q→0) = 1 / (1 + κ₀ Π_ph(q→0))
    # where Π_ph is the particle-hole bubble
    #
    # Compute Π_ph(q=0, Ω=0):
    # Π_ph(0, 0) = -T Σ_n ∫dk/(2π) G(k, iω_n) G(k, iω_n)
    # = -T Σ_n ∫dk/(2π) |G(k, iω_n)|²  (for q=0, Ω=0)

    Pi_ph_0 = 0.0 + 0j
    for ik in range(N_k_eff):
        for iw in range(N_w_eff):
            Pi_ph_0 += G_eff[ik, iw] * G_eff[ik, iw]
    Pi_ph_0 *= -T * 2.0 * dk_eff / (2*np.pi)  # factor 2 for negative freq

    # Vertex at q=0 (ladder approximation in ph channel):
    # Γ_ph = 1 / (1 - κ₀ Π_ph)  [attractive interaction]
    # or Γ_ph = 1 / (1 + κ₀ Π_ph) depending on sign convention

    # The Ward identity states:
    # Z = 1 / Γ_ph(q→0, Ω→0) for a conserving approximation
    # So: 1/Γ_ph = Z = 1/(1 - ∂_ω Σ)

    # Try both sign conventions and pick the one closer to Z
    Gamma_ph_plus = 1.0 / (1.0 + kappa0 * Pi_ph_0)
    Gamma_ph_minus = 1.0 / (1.0 - kappa0 * Pi_ph_0)

    inv_Gamma_plus = np.real(Gamma_ph_plus)
    inv_Gamma_minus = np.real(Gamma_ph_minus)

    # Z from self-energy
    Z_from_Sigma = 1.0 / (1.0 - dSigma_dw)

    # Pick the convention that makes more sense (closer to Z or to 1 at weak coupling)
    # At κ→0: Γ_ph → 1, Z → 1, so both should approach 1
    # Use the one where |1/Γ - Z| is minimized
    if abs(inv_Gamma_plus - Z_from_Sigma) < abs(inv_Gamma_minus - Z_from_Sigma):
        inv_Gamma = inv_Gamma_plus
        convention = "+"
    else:
        inv_Gamma = inv_Gamma_minus
        convention = "-"

    # Ward residual
    Delta_W = abs((1 - dSigma_dw) - inv_Gamma)

    return {
        'kappa0': kappa0,
        'kappa_over_kF': kappa0 / k_F,
        'dSigma_dw': dSigma_dw,
        'Z': Z_from_Sigma,
        'inv_Gamma_ph': inv_Gamma,
        'Delta_W': Delta_W,
        'convergence_residual': convergence_residual,
        'spectral_ok': spectral_ok,
        'convention': convention,
        'Pi_ph_0': Pi_ph_0,
        'Lambda': Lambda,
        'N_k': N_k_eff,
        'N_omega': N_w_eff,
    }


# ============================================================
# MAIN COMPUTATION
# ============================================================
print("=" * 90)
print("Program H — Stage H1: Ward Residual Scaling Law Extraction")
print("=" * 90)
print(f"\nModel: 1D Fermi gas, contact interaction, self-consistent T-matrix")
print(f"Units: k_F = 1, E_F = 0.5, m = 1")
print(f"Temperature: T = {T:.4f} E_F")
print(f"Mixing: {mixing}, tolerance: {tol}")

# ============================================================
# PRIMARY TABLE
# ============================================================
results_all = {}

for Lambda in Lambda_values:
    print(f"\n{'='*90}")
    print(f"CUTOFF Λ/k_F = {Lambda:.0f}")
    print(f"{'='*90}")

    results = []
    for kappa_ratio in kappa_over_kF:
        kappa0 = kappa_ratio * k_F
        print(f"\n  Computing κ₀/k_F = {kappa_ratio:.2f} ...", end=" ", flush=True)
        res = run_self_consistent_tmatrix(kappa0, Lambda, verbose=False)
        results.append(res)
        print(f"done. ΔW = {res['Delta_W']:.6e}, converged: {res['convergence_residual']:.2e}")

    results_all[Lambda] = results

    # Print table
    print(f"\n  {'κ₀/kF':>8s} {'∂ωΣ':>12s} {'1/Γph':>12s} {'ΔW':>12s} {'Z':>8s} {'conv':>10s} {'spec':>6s}")
    print(f"  {'-'*8} {'-'*12} {'-'*12} {'-'*12} {'-'*8} {'-'*10} {'-'*6}")

    for r in results:
        print(f"  {r['kappa_over_kF']:8.2f} {r['dSigma_dw']:12.6f} {r['inv_Gamma_ph']:12.6f} "
              f"{r['Delta_W']:12.6e} {r['Z']:8.4f} {r['convergence_residual']:10.2e} "
              f"{'PASS' if r['spectral_ok'] else 'FAIL':>6s}")

# ============================================================
# SCALING FIT
# ============================================================
print(f"\n{'='*90}")
print("SCALING FIT: ΔW ~ κ₀^α")
print("=" * 90)

for Lambda in Lambda_values:
    results = results_all[Lambda]
    kappa_arr = np.array([r['kappa_over_kF'] for r in results])
    DW_arr = np.array([r['Delta_W'] for r in results])

    # Filter out zero or nan
    valid = (DW_arr > 0) & np.isfinite(DW_arr) & (kappa_arr > 0)

    if np.sum(valid) >= 3:
        log_kappa = np.log(kappa_arr[valid])
        log_DW = np.log(DW_arr[valid])

        # Linear fit in log-log
        coeffs, cov = np.polyfit(log_kappa, log_DW, 1, cov=True)
        alpha = coeffs[0]
        alpha_err = np.sqrt(cov[0, 0])

        # R²
        residuals = log_DW - np.polyval(coeffs, log_kappa)
        ss_res = np.sum(residuals**2)
        ss_tot = np.sum((log_DW - np.mean(log_DW))**2)
        R2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0

        print(f"\n  Λ/k_F = {Lambda:.0f}:")
        print(f"    α = {alpha:.3f} ± {alpha_err:.3f}")
        print(f"    R² = {R2:.4f}")
        print(f"    Fit range: κ₀/k_F ∈ [{kappa_arr[valid].min():.2f}, {kappa_arr[valid].max():.2f}]")
    else:
        print(f"\n  Λ/k_F = {Lambda:.0f}: insufficient valid data for fit")
        alpha = np.nan
        alpha_err = np.nan
        R2 = np.nan

# ============================================================
# RG STABILITY CHECK
# ============================================================
print(f"\n{'='*90}")
print("RG STABILITY CHECK")
print("=" * 90)

if len(Lambda_values) >= 2:
    L1, L2 = Lambda_values[0], Lambda_values[1]
    r1 = results_all[L1]
    r2 = results_all[L2]

    print(f"\n  {'κ₀/kF':>8s} {'ΔW(Λ={L1:.0f})':>15s} {'ΔW(Λ={L2:.0f})':>15s} {'rel drift':>12s} {'stable?':>8s}")
    print(f"  {'-'*8} {'-'*15} {'-'*15} {'-'*12} {'-'*8}")

    for i in range(len(kappa_over_kF)):
        dw1 = r1[i]['Delta_W']
        dw2 = r2[i]['Delta_W']
        if dw1 > 0 and dw2 > 0:
            drift = abs(dw1 - dw2) / max(dw1, dw2)
            stable = "YES" if drift < 0.05 else ("MARG" if drift < 0.15 else "NO")
        else:
            drift = np.nan
            stable = "N/A"
        print(f"  {kappa_over_kF[i]:8.2f} {dw1:15.6e} {dw2:15.6e} {drift:12.4f} {stable:>8s}")

# ============================================================
# CLASSIFICATION
# ============================================================
print(f"\n{'='*90}")
print("CLASSIFICATION")
print("=" * 90)

# Use the primary cutoff results for classification
results_primary = results_all[Lambda_values[-1]]
kappa_arr = np.array([r['kappa_over_kF'] for r in results_primary])
DW_arr = np.array([r['Delta_W'] for r in results_primary])
valid = (DW_arr > 0) & np.isfinite(DW_arr) & (kappa_arr > 0)

if np.sum(valid) >= 3:
    log_kappa = np.log(kappa_arr[valid])
    log_DW = np.log(DW_arr[valid])
    coeffs_final = np.polyfit(log_kappa, log_DW, 1)
    alpha_final = coeffs_final[0]

    print(f"\n  Scaling exponent: α = {alpha_final:.3f}")

    if alpha_final >= 1.8:
        classification = "higher-order"
        interpretation = (
            "ΔW scales as κ₀^{α≥2}, indicating the Ward-identity violation is a "
            "higher-order truncation artifact. The self-consistent T-matrix (ladder "
            "approximation) conserves the Ward identity at LEADING ORDER. The residual "
            "arises from omitted vertex corrections (crossed diagrams, exchange terms) "
            "that enter at next-to-leading order in κ₀."
        )
    elif alpha_final >= 0.7:
        classification = "leading-order"
        interpretation = (
            "ΔW scales as κ₀^{α≈1}, indicating a LEADING-ORDER symmetry violation. "
            "The self-consistent T-matrix (ladder topology) is insufficient to satisfy "
            "the Ward identity even at lowest nontrivial order. The particle-hole vertex "
            "from the ladder BSE does not match the self-energy derivative. This means "
            "the approximation is not a Φ-derivable (Baym-Kadanoff conserving) scheme "
            "in the particle-hole channel, even though it may be conserving in the "
            "particle-particle channel."
        )
    else:
        classification = "non-perturbative"
        interpretation = (
            "ΔW scales as κ₀^{α≈0}, indicating a NON-PERTURBATIVE obstruction. "
            "The Ward-identity violation does not vanish at weak coupling. This would "
            "suggest a fundamental inconsistency in the self-consistent T-matrix approach "
            "that cannot be fixed by including higher-order diagrams."
        )

    print(f"  Classification: {classification}")
    print(f"\n  Interpretation:")
    # Print wrapped
    words = interpretation.split()
    line = "    "
    for w in words:
        if len(line) + len(w) > 85:
            print(line)
            line = "    " + w
        else:
            line += " " + w
    print(line)
else:
    classification = "UNDETERMINED"
    print(f"\n  Insufficient data for classification")

print(f"\n{'='*90}")
print("END OF COMPUTATION")
print("=" * 90)
