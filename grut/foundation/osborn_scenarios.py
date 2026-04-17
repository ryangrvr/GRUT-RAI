"""
osborn_scenarios.py — Scenario exploration for the brother

This script shows what the pipeline produces for different w_g values
and sign choices. The brother provides the ACTUAL w_g values from
Jack-Osborn section 4. This is scenario planning, not a result.

No target is assumed. We map the landscape so the brother can see
where his extraction lands.

Author: D. Ryan Grover, April 2026
Status: SCENARIO PLANNING — not a physics result
"""

import numpy as np

# ============================================================
# VERIFIED CONSTANTS
# ============================================================

# 1-loop anomaly coefficients (verified against Birrell-Davies)
a_SM = 283 / 120       # = 2.35833...
b_SM = -3487 / 1440    # = -2.42153...
R_1loop = abs(b_SM / a_SM)  # = 1.02680

# Cosmological formula constants
S_CTP = 108 * np.pi           # = 339.292
tau_0 = 41.9e6 * 3.156e7      # 41.9 Myr in seconds

# SM couplings at M_Z
g3, g2, g1 = 1.2203, 0.6517, 0.3574
alpha_s = g3**2 / (4*np.pi)
loop = 1 / (16 * np.pi**2)

# Osborn eq (36) A-coefficients (Dirac convention, verified)
A_SU3 = 17          # (1/3)(29×3 - 12×3)
A_SU2 = 83/12       # (1/3)(29×2 - 12×3 - 5/2 × 1/2)
A_U1 = -245/12      # (1/3)(0 - 12×5 - 5/2 × 1/2)

# ε values at M_Z (verified)
eps_SU3 = 1 + A_SU3 * g3**2 * loop   # 1.1603
eps_SU2 = 1 + A_SU2 * g2**2 * loop   # 1.0186
eps_U1  = 1 + A_U1  * g1**2 * loop   # 0.9835

# Beta function coefficients (1-loop)
b0_SU3 = 7       # for 6 flavors
b0_SU2 = 19/6
b0_U1  = -41/6   # U(1) not AF

# ln(M_Planck/M_Z)
ln_ratio = np.log(1.221e19 / 91.19)  # ≈ 39.4

# ============================================================
# COSMOLOGICAL FORMULA
# ============================================================

def omega_lambda(R, H0_km=70.0):
    """Compute Omega_Lambda from anomaly ratio R."""
    H0 = H0_km * 1e3 / 3.086e22
    H_inf = (2 - R) / (S_CTP * tau_0)
    return (H_inf / H0)**2

def R_needed(H0_km=70.0):
    """What R gives Omega_Lambda = 0.6889 for given H0."""
    H0 = H0_km * 1e3 / 3.086e22
    H_inf_needed = H0 * np.sqrt(0.6889)
    return 2 - H_inf_needed * S_CTP * tau_0

# ============================================================
# SCENARIO A: Direct ε substitution (if Q1=A, ε IS the object)
# ============================================================

def scenario_A():
    """What if ε_SU3 is literally R in the cosmological formula?"""
    print("=" * 70)
    print("SCENARIO A: ε_SU3 directly as R (requires Q1=A)")
    print("=" * 70)
    print("\n  This scenario assumes the CTP formalism selects the")
    print("  local-coupling anomaly coefficient ε, not b/a.")
    print("  Currently Q1=B (constant couplings), so this is hypothetical.\n")

    for H0 in [67.4, 70.0, 73.0]:
        R_need = R_needed(H0)
        OL = omega_lambda(eps_SU3, H0)
        gap = (eps_SU3 - R_need) / R_need * 100
        print(f"  H0 = {H0:5.1f}: ε_SU3 = {eps_SU3:.4f}, R_needed = {R_need:.4f}, "
              f"gap = {gap:+.2f}%, Ω_Λ = {OL:.4f}")

    print("\n  Including SU(2) and U(1) as perturbative corrections:")
    # Weighted combination: each group contributes proportionally
    # to its A × g^4 (Zamolodchikov × beta weight)
    w3 = abs(A_SU3) * g3**4
    w2 = abs(A_SU2) * g2**4
    w1 = abs(A_U1)  * g1**4
    wtot = w3 + w2 + w1

    eps_combined = (w3 * eps_SU3 + w2 * eps_SU2 + w1 * eps_U1) / wtot
    print(f"  Weights: QCD {w3/wtot*100:.1f}%, SU(2) {w2/wtot*100:.1f}%, U(1) {w1/wtot*100:.1f}%")
    print(f"  ε_combined = {eps_combined:.4f}")
    print(f"  Ω_Λ(ε_combined, H0=70) = {omega_lambda(eps_combined, 70):.4f}")

    return eps_SU3

# ============================================================
# SCENARIO B: Integrated Osborn with explicit w_g
# ============================================================

def scenario_B_single(c_w, label=""):
    """
    Run integrated Osborn with a specific c_w value.

    The w_i contribution shifts β_b but NOT β_a:
        Δβ_b += Σ_groups  c_w × n_V × |b0| × g × 4 × loop²
    integrated over ln(M_Planck/M_Z) ≈ 39.4 e-folds.

    NOTE: This is the SIMPLIFIED version using M_Z couplings over the full
    range. The real integration (in osborn_integrated.py) runs the couplings
    with the SM RGEs, which changes the result because g_s grows from ~0.5
    at M_Planck to ~1.22 at M_Z. The simplified version here is for
    scenario exploration only.
    """
    w_QCD = c_w * 8 * b0_SU3 * g3 * 4 * loop**2
    w_SU2 = c_w * 3 * b0_SU2 * g2 * 4 * loop**2
    w_U1  = c_w * 1 * abs(b0_U1) * g1 * 4 * loop**2
    delta_b = -(w_QCD + w_SU2 + w_U1) * ln_ratio
    b_new = b_SM + delta_b
    R_new = abs(b_new / a_SM)
    OL = omega_lambda(R_new)
    return {
        'c_w': c_w, 'label': label, 'delta_b': delta_b,
        'frac_shift_b': delta_b / abs(b_SM) * 100,
        'R': R_new, 'R_shift': (R_new - R_1loop) / R_1loop * 100,
        'Omega_Lambda': OL,
    }

def scenario_B():
    """Scan c_w values in both directions."""
    print("\n" + "=" * 70)
    print("SCENARIO B: Integrated Osborn with w_g (requires brother's extraction)")
    print("=" * 70)
    print("\n  c_w > 0: w_g positive → −L_β w negative → β_b less negative → |b| decreases → R DOWN")
    print("  c_w < 0: w_g negative → −L_β w positive → β_b more negative → |b| increases → R UP")
    print("  (Sign direction depends on conventions in Jack-Osborn — this is the")
    print("   sign chain the brother needs to verify)\n")

    print(f"  {'c_w':>8s}  {'Label':<25s}  {'Δb/b':>8s}  {'R':>8s}  {'ΔR%':>8s}  {'Ω_Λ':>8s}")
    print(f"  {'-'*8}  {'-'*25}  {'-'*8}  {'-'*8}  {'-'*8}  {'-'*8}")

    scenarios = [
        (-5.0, "strong negative"), (-3.0, "moderate negative"),
        (-2.0, "mild negative"), (-1.0, "unit negative"),
        (-0.5, "small negative"), (-0.1, "tiny negative"),
        (0.0, "no w_i (baseline)"),
        (0.1, "tiny positive"), (0.5, "small positive"),
        (1.0, "unit positive"), (2.0, "mild positive"),
        (3.0, "moderate positive"), (5.0, "strong positive"),
    ]

    for c_w, label in scenarios:
        r = scenario_B_single(c_w, label)
        marker = " ◄ near Planck" if abs(r['Omega_Lambda'] - 0.689) < 0.05 else ""
        print(f"  {c_w:+8.1f}  {label:<25s}  {r['frac_shift_b']:+7.2f}%  "
              f"{r['R']:8.4f}  {r['R_shift']:+7.2f}%  {r['Omega_Lambda']:8.4f}{marker}")

# ============================================================
# SCENARIO C: Inversion (explicitly labeled as fit)
# ============================================================

def scenario_C():
    """Find c_w that gives Omega_Lambda = 0.689. This is a FIT, not a derivation."""
    print("\n" + "=" * 70)
    print("SCENARIO C: INVERSION — what c_w matches Planck? (FIT, not derivation)")
    print("=" * 70)

    c_lo, c_hi = -20.0, 20.0
    for _ in range(60):
        c_mid = (c_lo + c_hi) / 2
        r = scenario_B_single(c_mid)
        if r['Omega_Lambda'] > 0.689:
            c_hi = c_mid
        else:
            c_lo = c_mid

    r_match = scenario_B_single(c_mid, "Planck match (FIT)")

    print(f"\n  c_w that gives Ω_Λ = 0.689 (simplified integration):  {c_mid:.4f}")
    print(f"  R at that c_w:               {r_match['R']:.6f}")
    print(f"  Ω_Λ:                         {r_match['Omega_Lambda']:.4f}")
    print(f"  Δb/b:                        {r_match['frac_shift_b']:+.2f}%")
    print(f"\n  NOTE: This simplified version uses M_Z couplings over full range.")
    print(f"  The full RG-running version in osborn_integrated.py gave c_w ≈ -1.")
    print(f"  The discrepancy is because g_s runs from ~0.5 (Planck) to ~1.22 (M_Z),")
    print(f"  and the per-step w contribution scales as g. So the full integration")
    print(f"  effectively averages over a smaller g, requiring a larger c_w to")
    print(f"  produce the same Δβ_b, OR the opposite depending on integration direction.")
    print(f"\n  Is |c_w| = {abs(c_mid):.1f} a natural O(1) coefficient?  "
          f"{'YES' if abs(c_mid) < 5 else 'NO — requires fine-tuning'}")
    return c_mid

# ============================================================
# SCENARIO D: Scale dependence (brother's Q4)
# ============================================================

def scenario_D():
    """Show how ε_SU3 varies with evaluation scale."""
    print("\n" + "=" * 70)
    print("SCENARIO D: Scale dependence of ε_SU3 (brother's Q4)")
    print("=" * 70)

    scales = [
        ("Λ_QCD (300 MeV)",    0.300,    3.0),
        ("τ mass (1.78 GeV)",   1.78,     0.34),
        ("b mass (4.18 GeV)",   4.18,     0.225),
        ("M_Z (91.2 GeV)",     91.2,     0.1181),
        ("m_top (173 GeV)",    173,      0.1074),
        ("1 TeV",              1000,     0.0885),
        ("10 TeV",             10000,    0.0745),
        ("M_GUT (2×10¹⁶ GeV)", 2e16,    0.0260),
        ("M_Planck (10¹⁹ GeV)", 1e19,   0.0188),
    ]

    print(f"\n  {'Scale':<25s}  {'μ (GeV)':>12s}  {'α_s':>8s}  {'ĝ²':>10s}  {'ε_SU3':>8s}  {'Ω_Λ(ε)':>8s}")
    print(f"  {'-'*25}  {'-'*12}  {'-'*8}  {'-'*10}  {'-'*8}  {'-'*8}")

    for name, mu, alpha in scales:
        g = np.sqrt(4 * np.pi * alpha)
        ghat2 = g**2 * loop
        eps = 1 + A_SU3 * ghat2
        OL = omega_lambda(eps)
        note = ""
        if abs(OL - 0.689) < 0.1:
            note = " ◄"
        if alpha > 0.5:
            note = " (non-pert!)"
        print(f"  {name:<25s}  {mu:>12.1f}  {alpha:8.4f}  {ghat2:10.6f}  {eps:8.4f}  {OL:8.4f}{note}")

    print("\n  The match window for Ω_Λ ~ 0.689 is roughly 50-200 GeV — EW scale.")
    print("  Above: α_s shrinks, ε → 1, Ω_Λ → too large.")
    print("  Below: α_s grows, eventually non-perturbative.")

# ============================================================
# SCENARIO E: Hypothetical w_g triplets
# ============================================================

def scenario_E():
    """Show how specific w_g values from Jack-Osborn feed into the pipeline."""
    print("\n" + "=" * 70)
    print("SCENARIO E: Example w_g extractions (HYPOTHETICAL)")
    print("=" * 70)

    examples = [
        ("All positive O(1)",      (+1.0, +0.5, +0.3)),
        ("All negative O(1)",      (-1.0, -0.5, -0.3)),
        ("QCD positive, EW neg.",  (+2.0, -0.5, -0.3)),
        ("QCD negative, EW pos.",  (-2.0, +0.5, +0.3)),
        ("QCD dominant positive",  (+3.0, +0.1, -0.1)),
        ("QCD dominant negative",  (-3.0, -0.1, +0.1)),
        ("Small everywhere",       (+0.1, +0.1, +0.1)),
    ]

    print(f"\n  {'Description':<25s}  {'w_3':>6s}  {'w_2':>6s}  {'w_1':>6s}  "
          f"{'R':>8s}  {'ΔR%':>8s}  {'Ω_Λ':>8s}")
    print(f"  {'-'*25}  {'-'*6}  {'-'*6}  {'-'*6}  {'-'*8}  {'-'*8}  {'-'*8}")

    for desc, (w3, w2, w1) in examples:
        db3 = -w3 * 8 * b0_SU3 * g3 * 4 * loop**2 * ln_ratio
        db2 = -w2 * 3 * b0_SU2 * g2 * 4 * loop**2 * ln_ratio
        db1 = -w1 * 1 * abs(b0_U1) * g1 * 4 * loop**2 * ln_ratio
        delta_b = db3 + db2 + db1
        b_new = b_SM + delta_b
        R_new = abs(b_new / a_SM)
        OL = omega_lambda(R_new)
        marker = " ◄" if abs(OL - 0.689) < 0.05 else ""
        print(f"  {desc:<25s}  {w3:+6.1f}  {w2:+6.1f}  {w1:+6.1f}  "
              f"{R_new:8.4f}  {(R_new-R_1loop)/R_1loop*100:+7.2f}%  {OL:8.4f}{marker}")

# ============================================================
# SUMMARY
# ============================================================

def summary():
    print("\n" + "=" * 70)
    print("SUMMARY FOR THE BROTHER")
    print("=" * 70)
    print(f"""
  VERIFIED INPUTS:
    a_SM = 283/120 = {a_SM:.6f}     (Weyl² coefficient, 1-loop)
    b_SM = -3487/1440 = {b_SM:.6f}  (Euler coefficient, 1-loop)
    R_1loop = |b/a| = {R_1loop:.6f}
    ε_SU3(M_Z) = {eps_SU3:.6f}       (Osborn 2003 eq 36, Dirac)

  WHAT YOU PROVIDE:
    w_g for SU(3), SU(2), U(1) from Jack-Osborn section 4
    Sign of −L_β w_g at M_Z (this determines direction of ΔR)

  WHAT THE PIPELINE DOES:
    1. Takes your w_g values
    2. Integrates the Osborn equation from M_Planck to M_Z
       (SM couplings running via 1-loop RGEs, 39.4 e-folds)
    3. Accumulates Δβ_b from the w_i term (β_a unchanged)
    4. Computes R_final = |b_final / a_SM|
    5. Computes Ω_Λ = (H_inf/H_0)² where H_inf = (2-R)/(S×τ_0)
    6. Reports whatever comes out

  THE SIGN CHAIN (you verify):
    Link 1: PZ Δb̄ > 0 — does NOT apply to SM (needs IR CFT)
    Link 2: Your w_g extraction determines sign
    Link 3: Your Lie derivative convention determines sign of −L_β w
    Link 4: LOCKED — β_a has no w_i term, so ΔR = sign(−L_β w)

  WHAT WE'RE NOT DOING:
    - Not fitting to Ω_Λ = 0.689
    - Not choosing c_w to hit a target
    - Not assuming ε = R (that's Q1, answered B for now)

  YOUR EXTRACTION → OUR PIPELINE → THE NUMBER
  Whatever Ω_Λ comes out is the result.
""")


def main():
    print("=" * 70)
    print("OSBORN SCENARIOS: What different w_g values produce")
    print("For the brother — scenario planning, NOT results")
    print("=" * 70)

    print(f"\n  Baseline: R_1loop = {R_1loop:.5f}")
    print(f"  Target (Planck, H0=70): R = {R_needed(70):.5f}")
    print(f"  ε_SU3 at M_Z: {eps_SU3:.5f}")
    print(f"  Ω_Λ at R_1loop: {omega_lambda(R_1loop):.4f}")
    print(f"  Ω_Λ at ε_SU3:  {omega_lambda(eps_SU3):.4f}")

    scenario_A()
    scenario_B()
    scenario_C()
    scenario_D()
    scenario_E()
    summary()


if __name__ == '__main__':
    main()
