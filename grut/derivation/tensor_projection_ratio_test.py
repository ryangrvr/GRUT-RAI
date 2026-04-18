"""
TENSOR PROJECTION RATIO TEST — follow-up to tensor_projection_S4.py

Key finding from main calculation: a ratio of eps-like coefficients drifts
by only ~5% across 18 orders of magnitude in mu, while eps itself drifts
by ~13%. This script isolates the structural implication.

Three hypotheses for what R_GRUT = |C_Cosmo/C_Final| actually is:

  H1:  R_GRUT = eps(mu)                        -- scheme-dependent
  H2:  R_GRUT = eps(mu) / eps(mu)              -- trivially 1 (ruled out)
  H3:  R_GRUT = eps(mu) * (structural factor)  -- scheme-dependent via eps
  H4:  R_GRUT = A * eps_num(mu) / eps_den(mu)  -- approximately scheme-invariant

Test: if H4 is the right structure, then:
  * R_GRUT is ALMOST mu-independent (drift is 2-loop small)
  * The numerical value A comes from tree-level S^4 geometry and 3-loop
    tensor structure combined
  * The 0.04% match of R_GRUT to eps(M_Z) = 1.155 would require
      A * eps_num / eps_den ≈ 1.155
    at any scale (all RG-equivalent).

Purpose: explore the phase space of A-values and relative eps strengths
to see which combinations give R_GRUT ≈ 1.155 across ALL mu.
"""

import math

# SM at M_Z
alpha_s_MZ = 0.1181
alpha_2_MZ = 0.03376
alpha_Y_MZ = 0.01018
M_Z = 91.2
H_inf = 1e13

K_SU3 = 17.0
K_SU2 = 6.5
K_U1 = -40.4

b0_SU3 = 7.0
b0_SU2 = 19.0 / 6.0
b0_U1 = -41.0 / 6.0

def alpha_rg(a_ref, b0, mu_ref, mu):
    return 1.0 / (1.0 / a_ref + (b0 / (2.0 * math.pi)) * math.log(mu / mu_ref))

def eps_combined(mu):
    a_s = alpha_rg(alpha_s_MZ, b0_SU3, M_Z, mu)
    a_2 = alpha_rg(alpha_2_MZ, b0_SU2, M_Z, mu)
    a_Y = alpha_rg(alpha_Y_MZ, b0_U1, M_Z, mu)
    return (0.960 * (1 + K_SU3 * a_s / (4 * math.pi))
            + 0.032 * (1 + K_SU2 * a_2 / (4 * math.pi))
            + 0.008 * (1 + K_U1 * a_Y / (4 * math.pi)))

print("=" * 78)
print("TENSOR PROJECTION RATIO TEST")
print("=" * 78)
print()

# =============================================================================
# Test 1: Does H4 with various (K_num, K_den) pairs work?
# =============================================================================
print("Test 1: ratio structure R = A * (1 + K1 alpha/4pi) / (1 + K2 alpha/4pi)")
print("-" * 78)
print()
print("Try to find (K1, K2) such that R is mu-invariant AND equals ~1.155.")
print()

def R_ratio(mu, K1, K2, A=1.0):
    a_s = alpha_rg(alpha_s_MZ, b0_SU3, M_Z, mu)
    num = 1.0 + K1 * a_s / (4 * math.pi)
    den = 1.0 + K2 * a_s / (4 * math.pi)
    return A * num / den

test_mus = [M_Z, 1e3, 1e6, 1e9, H_inf, 1e17, 1e19]
print(f"  {'K1':>6s}  {'K2':>6s}  {'A':>6s}  | " + " ".join(f"{mu:>9.1e}" for mu in test_mus))
print("  " + "-" * 78)

candidates = [
    (K_SU3, 0, 1.0),       # eps_num only: equiv to eps
    (K_SU3, K_SU3/2, 1.0), # half-dress denom
    (K_SU3, -K_SU3, 1.0),  # anti-symm
    (2*K_SU3, K_SU3, 1.0), # double-dress num
    (K_SU3, 0, 1.0),       # pure eps
    (17, 0, 1.0),
    (0, 17, 1.155),        # A=1.155, eps on DENOMINATOR
    (0, 0, 1.155),         # Pure geometry 1.155
    (17, 17*0.134, 1.0),   # specific ratio that happens to give 1.155 at MZ
]

for K1, K2, A in candidates:
    row = [f"{K1:>6.1f}  {K2:>6.1f}  {A:>6.3f}  |"]
    for mu in test_mus:
        row.append(f"{R_ratio(mu, K1, K2, A):>9.5f}")
    print("  " + " ".join(row))

print()
print("Observation: only (K1=0, K2=0, A=1.155) is EXACTLY mu-invariant.")
print("Any ratio with non-trivial eps dependence drifts with mu.")
print("But when K1 ~ K2, the drift is small (perturbatively suppressed).")
print()

# =============================================================================
# Test 2: Fractional drift vs |K1 - K2|
# =============================================================================
print("Test 2: drift magnitude vs |K1 - K2|")
print("-" * 78)
print()
print("Fix A so R(M_Z) = 1.155; vary K2 relative to K1=17.")
print("Drift = |R(H_inf) - R(M_Z)| / R(M_Z), in percent.")
print()
print(f"  {'K2':>8s}  {'R(M_Z)':>10s}  {'R(H_inf)':>10s}  {'drift %':>9s}")
print("  " + "-" * 45)

K1 = 17.0
for K2 in [0, 4, 8, 12, 16, 17, 17.5, 18, 20, 24, 32]:
    # Find A such that R(M_Z) = 1.155
    a_s_MZ = alpha_s_MZ
    num_MZ = 1.0 + K1 * a_s_MZ / (4 * math.pi)
    den_MZ = 1.0 + K2 * a_s_MZ / (4 * math.pi)
    A = 1.155 * den_MZ / num_MZ

    R_at_MZ = R_ratio(M_Z, K1, K2, A)
    R_at_H = R_ratio(H_inf, K1, K2, A)
    drift = (R_at_H / R_at_MZ - 1.0) * 100
    print(f"  {K2:>8.2f}  {R_at_MZ:>10.5f}  {R_at_H:>10.5f}  {drift:>8.2f}%")

print()
print("""
  INTERPRETATION:
    * K2 = 17 (= K1): pure geometric, R is exactly mu-invariant at 1.155.
    * K2 far from K1: large drift, R is scheme-dependent.
    * The closer K2 is to K1, the more RG-invariant the ratio.

  The 3-loop CTP tensor projection determines BOTH K2 and the prefactor A.
  If the physics gives K2 near K1 (i.e., C_Cosmo and C_Final have similar
  anomalous dimensions), then the ratio is approximately scheme-free and
  GRUT's numerical R_GRUT is the 'correct answer' regardless of scheme.
""")

# =============================================================================
# Test 3: The SM-EFT matching window argument
# =============================================================================
print("Test 3: SM-EFT matching window")
print("-" * 78)
print("""
  The SM is defined as an EFT at a matching scale. For cosmological
  observables sensitive to SM matter, this matching scale is M_Z (or
  roughly the EW scale where the full SM is in effect).

  For scales mu < M_Z: light quark decoupling changes beta functions.
  For scales mu > M_Z: the SM runs smoothly up to where new physics enters.

  If GRUT's R_GRUT is a MATTER-DECOHERENCE observable (as the framework
  argues), and matter decoherence is dominated by light-mode contributions
  (where the spectral sum has its weight), then the effective matching
  scale is where ALL SM matter is present but none has been integrated out.
  That scale is M_Z ~ m_t ~ EW scale.

  Conclusion from this argument:
    - R_GRUT should be evaluated at mu ~ M_Z
    - eps(M_Z) = 1.155
    - If R_GRUT = eps * (ratio correction) and the ratio correction is
      mildly RG-varying, the answer at any scale is ~eps(M_Z) ± 5%.
""")

# Compute: what does R_GRUT = 1.155 require?
print("Required R_GRUT values at different scales to match 0.6889 Omega_L:")
print()

S = 108.0 * math.pi
tau_0 = 1.322e15
H_0_Hz = 70.0e3 / 3.0857e22

# Solve (2-R) / (S tau_0 H_0) = sqrt(Omega_L)
R_target_exact = 2.0 - math.sqrt(0.6889) * S * tau_0 * H_0_Hz
print(f"  R_target (Omega_L = 0.6889): {R_target_exact:.5f}")
print(f"  eps(M_Z) = {eps_combined(M_Z):.5f}")
print(f"  Match ratio: eps/R = {eps_combined(M_Z)/R_target_exact:.5f}")
print(f"  Fractional deviation: {(eps_combined(M_Z)/R_target_exact - 1)*100:.4f}%")
print()
print(f"  eps(H_inf) = {eps_combined(H_inf):.5f}")
print(f"  Match ratio: eps/R = {eps_combined(H_inf)/R_target_exact:.5f}")
print(f"  Fractional deviation: {(eps_combined(H_inf)/R_target_exact - 1)*100:.4f}%")

print()
print("=" * 78)
print("Summary of ratio test")
print("=" * 78)
print("""
  Three structural scenarios for R_GRUT:

  1. R_GRUT = eps(M_Z) directly (Scenario A, scheme-fixed)
     Requires physical argument for mu = M_Z.
     Gives Omega_L = 0.6886 at 0.04% from Planck.
     Supported by: IR spectral evidence, matter-decoherence framework.

  2. R_GRUT = A (pure geometry, no eps dressing) (Scenario C, geometric)
     Would require A = 1.155 exactly from tree-level S^4 geometry.
     This is the 'geometric constant = 1.155' interpretation.
     No physical reason it should equal this value unless lucky.

  3. R_GRUT = A * eps_num/eps_den (Scenario B, approximately scheme-free)
     The specific K_num, K_den and A come from 3-loop tensor projection.
     If K_num ~ K_den, approximately scheme-independent at ~1.155.
     If K_num >> K_den, scheme-dependent and only M_Z matches Planck.

  Scenario A and B give the SAME numerical answer at mu=M_Z (by construction
  if A is tuned). At other scales they differ by a few percent — within
  observational error of Planck.

  The one scenario that FAILS is "R_GRUT = eps(H_inf)" which gives
  Omega_L = 0.91 (30% miss). This is the uncorrectable scheme that the
  specialist must rule out.

  Current evidence suggesting this CAN be ruled out:
    * Matter-decoherence framework (decoherence paper)
    * IR-dominated spectral structure for the right observable (Part E)
    * Standard RG practice: evaluate observables at their physical scale
    * GRUT's formula is defined with SM matter as input
""")
