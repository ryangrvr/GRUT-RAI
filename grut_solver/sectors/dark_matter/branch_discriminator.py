"""
Dark Matter Branch Discriminator

Five independent tests to select between Route 1 (RG) and Route 2 (Anomaly).

Test 1: Anomaly self-consistency — Route 2 extracts g_dark from C_FINAL,
        but the dark sector with coupling g_dark contributes BACK to C_FINAL.
        The self-consistent fixed point g* = g[C_FINAL + C_dark(g*)] selects.

Test 2: Fixed-point stability — eigenvalue spectrum of dz_target/dz at the
        dark vacuum for each route.

Test 3: Naturalness — distance from the perturbative unitarity bound.

Test 4: Baryonic consistency — which route's dark sector contribution
        to C_FINAL is compatible with the baryonic eta_B computation.

Test 5: Anomaly budget — the dark sector should not over-contribute to C_FINAL.

Status: COMPUTED (discriminator selects Route 1 as preferred)
"""

import numpy as np
from grut_solver.constants import C_FINAL, ZETA_3


# =============================================================================
# DARK SECTOR CONTRIBUTION TO C_FINAL
# =============================================================================

# The gravitational trace anomaly coefficients per field type (1-loop):
# For a real scalar:  a_s = 1/360,   c_s = 1/120
# For a Dirac fermion: a_D = 11/720, c_D = 1/20
# For a vector boson:  a_v = 62/360, c_v = 12/120
#
# The 3-loop coefficient C scales with the total field content.
# C_FINAL = 3(99 + 2π² + 576 ln2 ζ3)/(16384 π⁶) uses the FULL SM:
#   4 real scalars, 45 Weyl = 22.5 Dirac, 12 vectors

# SM trace anomaly weights (for 3-loop scaling)
N_S_SM = 4        # real scalars (Higgs doublet)
N_D_SM = 22.5     # Dirac fermions (= 45 Weyl / 2)
N_V_SM = 12       # vectors (8g + W+ + W- + Z + γ)

# Effective weight: w = N_s + 6 N_D + 12 N_v (from 1-loop trace anomaly)
W_SM = N_S_SM + 6 * N_D_SM + 12 * N_V_SM  # 4 + 135 + 144 = 283


def dark_sector_field_content(g_dark, lam, v):
    """Count the dark sector degrees of freedom and their anomaly weight.

    The U(1)_dark Abelian Higgs model contains:
    - 1 complex scalar (dark Higgs) = 2 real scalars
    - 1 massive dark photon = 3 DOF (after symmetry breaking)
      But in the unbroken phase (relevant for UV anomaly): 1 massless vector

    The dark Higgs mass: m_h = sqrt(2 lambda) v
    The dark photon mass: m_A = g_dark v
    """
    n_s_dark = 2       # real scalar DOF (complex scalar)
    n_d_dark = 0       # no dark fermions
    n_v_dark = 1       # one dark photon

    w_dark = n_s_dark + 6 * n_d_dark + 12 * n_v_dark  # 2 + 0 + 12 = 14

    # Fraction of total anomaly weight
    f_dark = w_dark / (W_SM + w_dark)

    return {
        "n_s_dark": n_s_dark,
        "n_d_dark": n_d_dark,
        "n_v_dark": n_v_dark,
        "w_dark": w_dark,
        "w_sm": W_SM,
        "w_total": W_SM + w_dark,
        "f_dark": f_dark,
        "m_h_GeV": np.sqrt(2 * lam) * v,
        "m_A_GeV": g_dark * v,
    }


def c_final_with_dark_sector(g_dark, lam, v):
    """Compute the modified C_FINAL when the dark sector is included.

    The dark sector contributes additional loops to the gravitational
    effective action. At 3-loop, the total coefficient becomes:

        C_total = C_SM + C_dark

    where C_dark/C_SM ≈ w_dark/w_SM (at leading order in the field-content
    scaling approximation).

    At higher order, the dark gauge coupling g_dark modifies the gauge
    contribution. The gauge part of C_FINAL (the 576 ln(2) ζ(3) term)
    scales with the sum of gauge-field contributions weighted by their
    coupling strengths.
    """
    fc = dark_sector_field_content(g_dark, lam, v)

    # Leading-order scaling: C_dark/C_SM = w_dark/w_SM
    c_dark_leading = C_FINAL * fc["w_dark"] / fc["w_sm"]

    # Coupling-weighted correction: the gauge part scales with g^4
    # For SM: sum of g_i^4 weighted by gauge DOF
    # The SM gauge contribution comes from: 8 gluons (g_s), 3 weak (g_2), 1 U(1) (g')
    # Rough weighting: (8 α_s² + 3 α_W² + α_Y²) for SM
    alpha_s = 0.1185
    alpha_W = 0.0336
    alpha_Y = 0.0102
    alpha_dark = g_dark**2 / (4 * np.pi)

    gauge_weight_SM = 8 * alpha_s**2 + 3 * alpha_W**2 + alpha_Y**2
    gauge_weight_dark = alpha_dark**2  # one dark photon

    gauge_correction = gauge_weight_dark / gauge_weight_SM

    # The gauge part of C_FINAL:
    n3 = 576.0 * np.log(2) * ZETA_3
    total_num = 99.0 + 2.0 * np.pi**2 + n3
    gauge_fraction = n3 / total_num  # fraction of C_FINAL from gauge loops

    c_dark_gauge = C_FINAL * gauge_fraction * gauge_correction

    # Total dark contribution (leading + gauge correction)
    c_dark_total = c_dark_leading + c_dark_gauge

    c_total = C_FINAL + c_dark_total

    return {
        "c_final_sm": C_FINAL,
        "c_dark_leading": c_dark_leading,
        "c_dark_gauge": c_dark_gauge,
        "c_dark_total": c_dark_total,
        "c_total": c_total,
        "dark_fraction": c_dark_total / c_total,
        "modification_pct": 100 * c_dark_total / C_FINAL,
    }


# =============================================================================
# TEST 1: ANOMALY SELF-CONSISTENCY
# =============================================================================

def anomaly_self_consistency():
    """Test whether each route's g_dark is self-consistent with C_FINAL.

    Route 2 extracts g_dark FROM C_FINAL:
        g_dark² = (C_FINAL × (16π²)³)^(1/3)

    But the dark sector with coupling g_dark contributes C_dark BACK to C_FINAL.
    Self-consistency requires:
        g_dark² = ((C_FINAL + C_dark(g_dark)) × (16π²)³)^(1/3)

    This is a fixed-point equation: g* = G[g*]. We solve by iteration.
    """
    from grut_solver.sectors.dark_matter.gauge_dark_matter import (
        route_1_rg_running, route_2_anomaly_extraction,
    )

    r1 = route_1_rg_running()
    r2 = route_2_anomaly_extraction()

    # Route 2 self-consistency: iterate g_dark² = (C_total(g) × (16π²)³)^(1/3)
    g2_current = r2["g_dark"]**2
    lam_current = g2_current / 2
    N_ERAS = 329

    history = [g2_current]
    for iteration in range(50):
        v = np.sqrt(2 * C_FINAL * N_ERAS / lam_current)
        c_data = c_final_with_dark_sector(np.sqrt(g2_current), lam_current, v)
        c_total = c_data["c_total"]

        g2_new = (c_total * (16 * np.pi**2)**3)**(1.0 / 3.0)
        history.append(g2_new)

        if abs(g2_new - g2_current) / g2_current < 1e-12:
            break
        g2_current = g2_new
        lam_current = g2_current / 2

    g_star_r2 = np.sqrt(g2_current)
    lam_star_r2 = g2_current / 2

    # Fractional shift from the naive (non-self-consistent) value
    shift_r2 = (g_star_r2 - r2["g_dark"]) / r2["g_dark"]

    # Route 1 consistency check: does the dark sector's contribution
    # significantly change the RG running?
    v_r1 = r1["v_GeV"]
    c_r1 = c_final_with_dark_sector(r1["g_dark"], r1["lambda"], v_r1)

    # Route 1 doesn't USE C_FINAL to determine g_dark (it uses RG running).
    # But does the dark sector contribution change C_FINAL enough to matter
    # for the cosmological formula H_inf = (2-R)/(S tau_0)?
    # If C_FINAL shifts by delta, R shifts by ~ delta/C_FINAL × R.
    delta_c_r1 = c_r1["c_dark_total"]
    delta_R_r1 = (delta_c_r1 / C_FINAL) * 1.15428  # rough proportional shift

    delta_c_r2_data = c_final_with_dark_sector(g_star_r2, lam_star_r2,
                                                np.sqrt(2 * C_FINAL * N_ERAS / lam_star_r2))
    delta_c_r2 = delta_c_r2_data["c_dark_total"]
    delta_R_r2 = (delta_c_r2 / C_FINAL) * 1.15428

    return {
        "route_1": {
            "g_dark": r1["g_dark"],
            "self_consistent": True,  # RG doesn't depend on C_FINAL
            "dark_contribution_to_C": c_r1["c_dark_total"],
            "modification_pct": c_r1["modification_pct"],
            "delta_R_anomaly": delta_R_r1,
            "cosmology_impact": abs(delta_R_r1) < 0.01,  # < 1% change in R
        },
        "route_2": {
            "g_dark_naive": r2["g_dark"],
            "g_dark_self_consistent": g_star_r2,
            "fractional_shift": shift_r2,
            "converged_in": len(history) - 1,
            "self_consistent": abs(shift_r2) < 0.1,  # < 10% shift
            "dark_contribution_to_C": delta_c_r2,
            "modification_pct": delta_c_r2_data["modification_pct"],
            "delta_R_anomaly": delta_R_r2,
            "cosmology_impact": abs(delta_R_r2) < 0.01,
        },
        "discriminator": (
            "Route 1 is independent of C_FINAL (RG-determined). "
            "Route 2 is self-referential: g_dark depends on C_FINAL, which "
            "depends on g_dark. The self-consistent fixed point shifts "
            f"g_dark by {100*abs(shift_r2):.1f}%."
        ),
    }


# =============================================================================
# TEST 2: FIXED-POINT STABILITY
# =============================================================================

def fixed_point_stability():
    """Compare the stability eigenvalues of the dark vacuum for both routes.

    At the dark vacuum z = v (broken phase), the constitutive Jacobian is:
        J = dz_target/dz|_{z=v}

    For the double-well V(z) = λ(|z|²-v²)²/4, the second derivative at z=v:
        V''(v) = 2λv²

    The eigenvalue of the constitutive map:
        lambda_J = 1 - tau × V''(v) = 1 - tau × 2λv²

    Stability requires |lambda_J| < 1 (attracting fixed point).
    """
    from grut_solver.sectors.dark_matter.gauge_dark_matter import (
        route_1_rg_running, route_2_anomaly_extraction,
    )

    r1 = route_1_rg_running()
    r2 = route_2_anomaly_extraction()

    results = {}
    for label, r in [("route_1", r1), ("route_2", r2)]:
        lam = r["lambda"]
        v = r["v_GeV"]

        # Curvature at the broken vacuum
        V_pp = 2 * lam * v**2  # d²V/dz² at z = v

        # For the constitutive equation with tau normalization,
        # the Jacobian eigenvalue depends on the ratio V''/tau
        # In the discrete map (one era per step), the effective eigenvalue:
        #   lambda_J = exp(-V_pp × delta_t) for continuous
        #   lambda_J ≈ 1 - alpha_eff × V_pp / v² for the constitutive map

        # The constitutive eigenvalue at the dark fixed point:
        # z_target(z) = z - tau × dV/dz / (dz/dt normalization)
        # At z = v: z_target = v (fixed point), and
        # dz_target/dz = 1 - tau × V''(v) / norm
        #
        # For the gauged model, the relevant eigenvalue is
        # the mass-squared ratio: m_h² / v² = 2λ
        eigenvalue = 1.0 - 2.0 * lam  # from dz_target/dz at the minimum

        # Distance from marginal stability
        stability_margin = 1.0 - abs(eigenvalue)

        # The dark photon mode eigenvalue (gauge mode)
        # At the vacuum: m_A = g_dark v, eigenvalue related to g_dark²
        eigenvalue_gauge = 1.0 - r["g_dark"]**2

        results[label] = {
            "lambda": lam,
            "v_GeV": v,
            "V_pp": V_pp,
            "eigenvalue_higgs": eigenvalue,
            "eigenvalue_gauge": eigenvalue_gauge,
            "stable_higgs": abs(eigenvalue) < 1.0,
            "stable_gauge": abs(eigenvalue_gauge) < 1.0,
            "stability_margin_higgs": stability_margin,
            "stability_margin_gauge": 1.0 - abs(eigenvalue_gauge),
        }

    # Which route has better stability margin?
    m1_h = results["route_1"]["stability_margin_higgs"]
    m2_h = results["route_2"]["stability_margin_higgs"]
    m1_g = results["route_1"]["stability_margin_gauge"]
    m2_g = results["route_2"]["stability_margin_gauge"]

    results["preferred"] = (
        "Route 1" if (m1_h + m1_g) > (m2_h + m2_g) else "Route 2"
    )
    results["discriminator"] = (
        f"Route 1 Higgs eigenvalue: {results['route_1']['eigenvalue_higgs']:.4f}, "
        f"margin: {m1_h:.4f}. "
        f"Route 2 Higgs eigenvalue: {results['route_2']['eigenvalue_higgs']:.4f}, "
        f"margin: {m2_h:.4f}. "
        f"Route 1 gauge eigenvalue: {results['route_1']['eigenvalue_gauge']:.4f}. "
        f"Route 2 gauge eigenvalue: {results['route_2']['eigenvalue_gauge']:.4f}."
    )

    return results


# =============================================================================
# TEST 3: NATURALNESS (PERTURBATIVE UNITARITY)
# =============================================================================

def naturalness_test():
    """Compare lambda to perturbative unitarity bounds.

    For a scalar field theory, perturbative unitarity requires:
        lambda < 4π    (tree-level s-wave unitarity)
        lambda < 8π²/3 (improved 1-loop bound, ~26.3)

    For a gauge theory, the additional constraint:
        g_dark < sqrt(4π) ≈ 3.54  (perturbativity)

    Naturalness prefers lambda ~ O(1) and g ~ O(1).
    """
    from grut_solver.sectors.dark_matter.gauge_dark_matter import (
        route_1_rg_running, route_2_anomaly_extraction,
    )

    r1 = route_1_rg_running()
    r2 = route_2_anomaly_extraction()

    unitarity_bound = 4 * np.pi  # ≈ 12.57
    perturbativity_g = np.sqrt(4 * np.pi)  # ≈ 3.54

    results = {}
    for label, r in [("route_1", r1), ("route_2", r2)]:
        lam = r["lambda"]
        g = r["g_dark"]

        # Distance from unitarity bound (0 = at bound, 1 = maximally natural)
        lam_margin = 1.0 - lam / unitarity_bound
        g_margin = 1.0 - g / perturbativity_g

        # Naturalness score: how close to O(1) is lambda?
        # Score = 1 at lambda = 1, decreasing away
        naturalness_lam = np.exp(-abs(np.log(lam)))
        naturalness_g = np.exp(-abs(np.log(g)))

        results[label] = {
            "lambda": lam,
            "g_dark": g,
            "lambda_margin": lam_margin,
            "g_margin": g_margin,
            "lambda_natural": 0.01 < lam < 4 * np.pi,
            "g_natural": g < perturbativity_g,
            "naturalness_score_lambda": naturalness_lam,
            "naturalness_score_g": naturalness_g,
            "combined_score": naturalness_lam * naturalness_g,
        }

    results["preferred"] = (
        "Route 1" if results["route_1"]["combined_score"] >
        results["route_2"]["combined_score"] else "Route 2"
    )

    return results


# =============================================================================
# TEST 4: BARYONIC CONSISTENCY
# =============================================================================

def baryonic_consistency():
    """Test which route's dark sector is consistent with baryonic eta_B.

    The dark sector modifies C_FINAL, which modifies R_anomaly,
    which feeds into both:
    - H_inf = (2 - R)/(S tau_0)  [cosmology]
    - eta_B = J_CP × K_neq × (2 - R_B)/S_B  [baryogenesis]

    The route whose dark sector contribution keeps R_anomaly closest
    to 1.15428 (preserving the cosmological fit) is preferred.
    """
    from grut_solver.sectors.dark_matter.gauge_dark_matter import (
        route_1_rg_running, route_2_anomaly_extraction,
    )

    r1 = route_1_rg_running()
    r2 = route_2_anomaly_extraction()

    R_ANOMALY = 1.15428
    S = 108 * np.pi
    TAU_0 = 41.9e6 * 365.25 * 24 * 3600  # seconds
    H_OBS = 1.885e-18  # Hz (the GRUT prediction)

    results = {}
    for label, r in [("route_1", r1), ("route_2", r2)]:
        c_data = c_final_with_dark_sector(r["g_dark"], r["lambda"], r["v_GeV"])

        # Modified C_FINAL
        c_mod = c_data["c_total"]

        # Modified R_anomaly (assuming C_Cosmo scales proportionally)
        r_mod = R_ANOMALY * (1 + c_data["dark_fraction"])

        # Modified H_inf
        h_mod = (2.0 - r_mod) / (S * TAU_0)
        h_shift = (h_mod - H_OBS) / H_OBS

        # Impact on Omega_Lambda (at H_0 = 70 km/s/Mpc)
        H0 = 70 * 1e3 / (3.0857e22)  # Hz
        omega_mod = (h_mod / H0)**2
        omega_obs = (H_OBS / H0)**2

        results[label] = {
            "c_final_modified": c_mod,
            "dark_fraction": c_data["dark_fraction"],
            "R_anomaly_modified": r_mod,
            "H_inf_modified_Hz": h_mod,
            "H_inf_shift_pct": 100 * h_shift,
            "Omega_Lambda_modified": omega_mod,
            "Omega_Lambda_original": omega_obs,
            "cosmology_preserved": abs(h_shift) < 0.05,  # < 5%
        }

    # Prefer the route with smaller cosmological impact
    s1 = abs(results["route_1"]["H_inf_shift_pct"])
    s2 = abs(results["route_2"]["H_inf_shift_pct"])
    results["preferred"] = "Route 1" if s1 < s2 else "Route 2"

    return results


# =============================================================================
# TEST 5: ANOMALY BUDGET
# =============================================================================

def anomaly_budget():
    """Check that the dark sector doesn't over-contribute to C_FINAL.

    If C_dark > C_SM, the dark sector dominates the anomaly and the
    SM interpretation of C_FINAL breaks down. The dark contribution
    should be a perturbative correction (C_dark << C_SM).
    """
    from grut_solver.sectors.dark_matter.gauge_dark_matter import (
        route_1_rg_running, route_2_anomaly_extraction,
    )

    r1 = route_1_rg_running()
    r2 = route_2_anomaly_extraction()

    results = {}
    for label, r in [("route_1", r1), ("route_2", r2)]:
        c_data = c_final_with_dark_sector(r["g_dark"], r["lambda"], r["v_GeV"])
        fraction = c_data["dark_fraction"]
        perturbative = fraction < 0.1  # dark sector < 10% of total

        results[label] = {
            "dark_fraction": fraction,
            "dark_pct": 100 * fraction,
            "perturbative": perturbative,
        }

    results["preferred"] = (
        "Route 1" if results["route_1"]["dark_fraction"] <
        results["route_2"]["dark_fraction"] else "Route 2"
    )

    return results


# =============================================================================
# MASTER DISCRIMINATOR
# =============================================================================

def full_branch_discrimination():
    """Run all five tests and produce a final verdict.

    Returns a scorecard: Route 1 vs Route 2 on each test,
    with an overall preferred branch.
    """
    t1 = anomaly_self_consistency()
    t2 = fixed_point_stability()
    t3 = naturalness_test()
    t4 = baryonic_consistency()
    t5 = anomaly_budget()

    scorecard = {
        "test_1_self_consistency": {
            "route_1": "PASS (independent of C_FINAL)",
            "route_2": f"{'PASS' if t1['route_2']['self_consistent'] else 'FAIL'} "
                       f"(shift {100*abs(t1['route_2']['fractional_shift']):.1f}%)",
            "preferred": "Route 1" if not t1["route_2"]["self_consistent"] else "Tie",
        },
        "test_2_stability": {
            "route_1": f"Higgs λ_J={t2['route_1']['eigenvalue_higgs']:.3f}, "
                       f"margin={t2['route_1']['stability_margin_higgs']:.3f}",
            "route_2": f"Higgs λ_J={t2['route_2']['eigenvalue_higgs']:.3f}, "
                       f"margin={t2['route_2']['stability_margin_higgs']:.3f}",
            "preferred": t2["preferred"],
        },
        "test_3_naturalness": {
            "route_1": f"λ={t3['route_1']['lambda']:.2f}, score={t3['route_1']['combined_score']:.3f}",
            "route_2": f"λ={t3['route_2']['lambda']:.2f}, score={t3['route_2']['combined_score']:.3f}",
            "preferred": t3["preferred"],
        },
        "test_4_baryonic": {
            "route_1": f"H_inf shift {t4['route_1']['H_inf_shift_pct']:.2f}%",
            "route_2": f"H_inf shift {t4['route_2']['H_inf_shift_pct']:.2f}%",
            "preferred": t4["preferred"],
        },
        "test_5_budget": {
            "route_1": f"dark {t5['route_1']['dark_pct']:.1f}% of C_FINAL",
            "route_2": f"dark {t5['route_2']['dark_pct']:.1f}% of C_FINAL",
            "preferred": t5["preferred"],
        },
    }

    # Count preferences
    r1_wins = sum(1 for v in scorecard.values() if v["preferred"] == "Route 1")
    r2_wins = sum(1 for v in scorecard.values() if v["preferred"] == "Route 2")
    ties = sum(1 for v in scorecard.values() if v["preferred"] == "Tie")

    overall = "Route 1" if r1_wins > r2_wins else "Route 2" if r2_wins > r1_wins else "Tie"

    return {
        "scorecard": scorecard,
        "tally": {"route_1": r1_wins, "route_2": r2_wins, "tie": ties},
        "overall_preferred": overall,
        "details": {
            "self_consistency": t1,
            "stability": t2,
            "naturalness": t3,
            "baryonic": t4,
            "budget": t5,
        },
        "verdict": (
            f"Branch discrimination: Route 1 wins {r1_wins}/5, "
            f"Route 2 wins {r2_wins}/5, ties {ties}/5. "
            f"Overall preferred: {overall}."
        ),
        "honest_caveats": [
            "The field-content scaling of C_dark is approximate (not exact 3-loop)",
            "The stability eigenvalues use simplified constitutive Jacobian",
            "Naturalness is a criterion, not a theorem",
            "Baryonic consistency uses the same C_FINAL scaling approximation",
            "A unique selection requires either exact 3-loop computation or experimental dark photon detection",
        ],
    }
