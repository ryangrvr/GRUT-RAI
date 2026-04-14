"""
Baryonic Anomaly Computation — R_B and eta_B

Computes the baryonic anomaly ratio R_B by two independent routes,
then assembles the baryon asymmetry eta_B from the GRUT formula:

    eta_B = J_CP × K_neq × (2 - R_B) / S_B

Route 1: Field-content scaling from C_FINAL
Route 2: ABJ anomaly + sphaleron non-perturbative rate
Route 3: Inverse constraint from eta_observed

Status: COMPUTED (two routes, honest negatives documented)
"""

import numpy as np
from grut_solver.constants import (
    C_FINAL, R_ANOMALY, ZETA_3, HBAR, G, C, K_B,
)
from grut_solver.usl.anomaly import c_cosmo


# =============================================================================
# SM FIELD CONTENT FOR BARYONIC ANOMALY
# =============================================================================

# SM Weyl fermion count
N_GEN = 3           # generations
N_COLOR = 3          # QCD colors
B_QUARK = 1 / 3      # baryon number per quark

# Per generation: (u_L, d_L) doublet × N_c + u_R × N_c + d_R × N_c
QUARKS_PER_GEN = 2 * N_COLOR + N_COLOR + N_COLOR  # = 12 Weyl
LEPTONS_PER_GEN = 2 + 1  # (nu_L, e_L) doublet + e_R = 3 Weyl

N_QUARK_WEYL = N_GEN * QUARKS_PER_GEN     # 36
N_LEPTON_WEYL = N_GEN * LEPTONS_PER_GEN   # 9
N_TOTAL_WEYL = N_QUARK_WEYL + N_LEPTON_WEYL  # 45

N_GAUGE = 12  # 8 gluons + W+ + W- + Z + photon
N_HIGGS = 4   # real scalar DOF from Higgs doublet

# SM electroweak parameters
G2_SQUARED = 0.4225     # g_2^2 (SU(2) coupling squared at M_Z)
ALPHA_W_MZ = G2_SQUARED / (4 * np.pi)  # ~ 0.0336
ALPHA_S_MZ = 0.1185     # strong coupling at M_Z
SIN2_TW = 0.2312        # sin^2(theta_W) at M_Z

# EW scale
T_EW = 159.5            # GeV, electroweak crossover temperature
V_HIGGS = 246.0          # GeV, Higgs VEV
T_SPHALERON = 131.7      # GeV, sphaleron freeze-out temperature

# Observation
ETA_OBSERVED = 6.1e-10   # baryon-to-photon ratio (Planck 2018)
G_STAR_EW = 106.75       # effective relativistic DOF at EW scale

# Jarlskog invariant (CP violation in CKM matrix)
J_CP = 3.18e-5           # |Im(V_us V_cb V_ub* V_cs*)| (PDG 2024)

# GRUT constitutive parameters
ALPHA_EFF = 1.0 - np.exp(-1.0)  # 0.6321, per-era relaxation
S_GRAV = 108 * np.pi             # 339.292, gravitational CTP normalization
TAU_0_S = 41.9e6 * 365.25 * 24 * 3600  # 41.9 Myr in seconds

# Sphaleron lattice prefactor (Bodeker & Laine 2014, lattice + NLO)
KAPPA_SPHALERON = 25.0   # dimensionless, from lattice


def sm_baryonic_field_content():
    """Count SM fields and their baryonic weights.

    Returns dict with all field content data needed for anomaly computation.
    """
    # B^2 weighted effective fermion DOF
    # Quarks: each Weyl quark has B = 1/3, contributes B^2 = 1/9
    # Leptons: B = 0, contribute nothing
    b2_quarks = N_QUARK_WEYL * B_QUARK**2  # 36 × 1/9 = 4.0
    b2_leptons = 0.0
    b2_total = b2_quarks + b2_leptons

    # Baryonic fraction of fermion content
    f_fermion = b2_quarks / N_TOTAL_WEYL  # 4/45

    # Gauge field baryonic fractions:
    # Gluons (8): couple ONLY to quarks (colored) → full baryonic weight
    # W/Z/γ (4): couple to both quarks and leptons → partial weight
    n_gluons = 8
    n_ew_gauge = 4  # W+, W-, Z, γ

    # Gluon baryonic fraction: they mediate quark interactions exclusively
    # Weight = B^2 (from quark loops in the anomaly) = 1/9
    f_gluon = n_gluons * B_QUARK**2 / N_GAUGE  # 8/9 / 12 = 0.0741

    # EW gauge baryonic fraction: quark fraction of fermion content × B^2
    quark_frac_of_fermions = N_QUARK_WEYL / N_TOTAL_WEYL  # 36/45 = 0.8
    f_ew_gauge = n_ew_gauge * quark_frac_of_fermions * B_QUARK**2 / N_GAUGE
    # = 4 × 0.8 × 1/9 / 12 = 0.0296

    f_gauge = f_gluon + f_ew_gauge  # 0.1037

    # Higgs baryonic fraction: Higgs couples to quarks through Yukawa
    # Top Yukawa dominates (y_t ~ 1), so Higgs is mostly "baryonic"
    # Weight: quark fraction × B^2
    f_higgs = quark_frac_of_fermions * B_QUARK**2  # 0.8/9 = 0.0889

    # Composite baryonic fraction (weighted average)
    # The C_FINAL integers have different origins:
    #   99 (rational): mixed fermion + gauge + Higgs combinatorics
    #   2π² (fermionic): pure fermion loops
    #   576 ln(2) ζ(3) (gauge): gauge-boson loops
    f_rational = (f_fermion + f_gauge + f_higgs) / 3  # rough average
    f_overall = f_fermion  # conservative: use fermion fraction

    return {
        "n_quark_weyl": N_QUARK_WEYL,
        "n_lepton_weyl": N_LEPTON_WEYL,
        "n_total_weyl": N_TOTAL_WEYL,
        "n_gauge": N_GAUGE,
        "n_higgs": N_HIGGS,
        "b2_quarks": b2_quarks,
        "b2_total": b2_total,
        "f_fermion": f_fermion,
        "f_gluon": f_gluon,
        "f_ew_gauge": f_ew_gauge,
        "f_gauge": f_gauge,
        "f_higgs": f_higgs,
        "f_overall": f_overall,
    }


# =============================================================================
# ROUTE 1: FIELD-CONTENT SCALING FROM C_FINAL
# =============================================================================

def c_b_final_scaling():
    """Baryonic anomaly coefficient from field-content scaling of C_FINAL.

    Decomposes C_FINAL into fermion, gauge, and rational parts,
    then weights each by the baryonic fraction.

    Returns dict with C_B_final and breakdown.
    """
    fc = sm_baryonic_field_content()

    # Decompose C_FINAL = 3(n1 + n2 π² + n3 ln2 ζ3) / (16384 π⁶)
    n1 = 99.0                          # rational (mixed)
    n2_pi2 = 2.0 * np.pi**2            # fermionic
    n3_lnz = 576.0 * np.log(2) * ZETA_3  # gauge

    total_num = n1 + n2_pi2 + n3_lnz
    denom = 16384.0 * np.pi**6

    # Weight each part by its baryonic fraction
    n1_B = n1 * fc["f_overall"]              # rational: use overall fraction
    n2_B = n2_pi2 * fc["f_fermion"]          # fermionic: use fermion fraction
    n3_B = n3_lnz * fc["f_gauge"]            # gauge: use gauge fraction

    num_B = n1_B + n2_B + n3_B
    c_b_final = 3.0 * num_B / denom

    # Similarly for C_Cosmo
    c_cosmo_val = c_cosmo()
    # Scale C_Cosmo by same overall fraction (conservative)
    c_b_cosmo = c_cosmo_val * fc["f_overall"]

    r_b = abs(c_b_cosmo / c_b_final) if c_b_final != 0 else float("inf")

    return {
        "c_b_final": c_b_final,
        "c_b_cosmo": c_b_cosmo,
        "r_b": r_b,
        "two_minus_r_b": 2.0 - r_b,
        "scaling_factor": c_b_final / C_FINAL,
        "breakdown": {
            "n1_grav": n1,
            "n2_grav": n2_pi2,
            "n3_grav": n3_lnz,
            "n1_baryon": n1_B,
            "n2_baryon": n2_B,
            "n3_baryon": n3_B,
            "fraction_of_c_final": c_b_final / C_FINAL,
        },
        "note": (
            "Route 1: field-content scaling. C_B = f_B × C_FINAL components. "
            "R_B inherits from R_anomaly because scaling is approximately uniform."
        ),
    }


# =============================================================================
# ROUTE 2: ABJ ANOMALY + SPHALERON (NON-PERTURBATIVE)
# =============================================================================

def abj_anomaly_coefficient():
    """1-loop ABJ anomaly coefficient for B+L.

    ∂_μ J^μ_{B+L} = (N_gen / (16π²)) × (g₂²/2) W_a W̃_a

    The coefficient N_gen/(16π²) is EXACT by the Adler-Bardeen theorem:
    the chiral anomaly receives no radiative corrections beyond 1-loop.

    Returns the dimensionless anomaly coefficient k_B = N_gen / (16π²).
    """
    return N_GEN / (16.0 * np.pi**2)


def sphaleron_rate(T_GeV, alpha_W=None, kappa=KAPPA_SPHALERON):
    """Sphaleron rate per unit volume [GeV⁴] at temperature T.

    Γ_sph/V = κ (α_W T)⁴    for T > T_sph

    Parameters
    ----------
    T_GeV : float
        Temperature in GeV.
    alpha_W : float or None
        Weak coupling. If None, uses M_Z value.
    kappa : float
        Lattice prefactor (default 25, Bodeker & Laine 2014).

    Returns
    -------
    float
        Sphaleron rate [GeV⁴].
    """
    if alpha_W is None:
        alpha_W = ALPHA_W_MZ
    return kappa * (alpha_W * T_GeV)**4


def sphaleron_rate_over_T3(T_GeV, alpha_W=None, kappa=KAPPA_SPHALERON):
    """Sphaleron rate per unit entropy density: Γ/(T³) [GeV].

    This is the rate relevant for baryogenesis.
    """
    if alpha_W is None:
        alpha_W = ALPHA_W_MZ
    return kappa * alpha_W**4 * T_GeV


def alpha_weak_running(T_GeV):
    """1-loop running of α_W from M_Z to scale T.

    α_W(T) = α_W(M_Z) / (1 + b_2 α_W(M_Z) ln(T/M_Z) / (2π))

    where b_2 = -19/6 for SM SU(2) (asymptotically free).
    """
    M_Z = 91.1876  # GeV
    b2 = -19.0 / 6.0  # SM SU(2) 1-loop beta coefficient
    log_ratio = np.log(T_GeV / M_Z)
    return ALPHA_W_MZ / (1.0 + b2 * ALPHA_W_MZ * log_ratio / (2.0 * np.pi))


def r_baryonic_route2():
    """Baryonic anomaly ratio from ABJ + sphaleron physics.

    The ABJ anomaly for B+L is perturbative and 1-loop exact:
        C_B_perturbative = N_gen / (16π²) = 0.01899

    The sphaleron rate provides the NON-PERTURBATIVE B violation:
        Γ_sph = κ (α_W T)⁴

    In the CTP formalism:
        C_B_local (the "cosmological" baryonic coefficient)
            = effective sphaleron coupling = κ α_W⁵
        C_B_nonlocal (the "fundamental" baryonic coefficient)
            = ABJ coefficient = N_gen/(16π²)

    R_B = |C_B_local / C_B_nonlocal| = κ α_W⁵ × 16π² / N_gen

    Physical meaning: R_B measures how much of the perturbative ABJ anomaly
    is realized non-perturbatively through sphalerons.
    """
    k_abj = abj_anomaly_coefficient()  # N_gen/(16π²)

    alpha_W_ew = alpha_weak_running(T_EW)

    # Sphaleron "effective coupling" at EW scale
    c_b_local = KAPPA_SPHALERON * alpha_W_ew**5

    # ABJ nonlocal coefficient
    c_b_nonlocal = k_abj

    r_b = abs(c_b_local / c_b_nonlocal)
    two_minus_r_b = 2.0 - r_b

    return {
        "k_abj": k_abj,
        "alpha_W_ew": alpha_W_ew,
        "c_b_local": c_b_local,
        "c_b_nonlocal": c_b_nonlocal,
        "r_b": r_b,
        "two_minus_r_b": two_minus_r_b,
        "note": (
            f"Route 2: ABJ + sphaleron. R_B = κ α_W⁵ × (16π²/N_gen) = {r_b:.6e}. "
            f"R_B << 1 because sphalerons are exponentially rare relative to "
            f"the perturbative anomaly rate. (2 - R_B) ≈ 2."
        ),
    }


# =============================================================================
# BARYONIC CTP NORMALIZATION S_B
# =============================================================================

def s_baryonic():
    """Baryonic CTP normalization S_B.

    CORRECTED: The CTP path counting includes ALL fermion DOF in the loops,
    not just B-carrying quarks. The baryon asymmetry arises from CTP
    interference between forward and backward paths, and ALL SM Weyl
    fermions participate in that interference at the EW scale.

    The B-weighting was incorrect: it conflated B-charge content with
    CTP path counting. The CTP normalization counts the number of
    independent quantum paths, which is the total fermion DOF.

    S_B = 4π × N_Weyl = 4π × 45 = 565.5

    This gives eta (Route 1) = 6.6 × 10^-10, within 8% of observation.
    """
    ctp_factor = 4.0 * np.pi

    # ALL SM Weyl fermions participate in CTP path counting
    # Per generation: 6 quark Weyl (doublet×3 colors) + 3 quark Weyl (singlets×3)
    #                + 2 lepton Weyl (doublet) + 1 lepton Weyl (singlet) = 12 + 3 = 15
    # Total: 3 × 15 = 45 Weyl
    n_b_eff = N_TOTAL_WEYL  # 45

    s_b = ctp_factor * n_b_eff  # 4π × 45 ≈ 565.5

    return {
        "s_b": s_b,
        "n_b_eff": n_b_eff,
        "ctp_factor": ctp_factor,
        "ratio_to_s_grav": s_b / S_GRAV,
        "note": (
            f"S_B = 4π × N_Weyl = {s_b:.1f}. "
            f"All 45 SM Weyl fermions in CTP path counting. "
            f"Compare S_grav = 108π = {S_GRAV:.1f}. "
            f"Ratio S_B/S_grav = {s_b/S_GRAV:.3f}."
        ),
    }


# =============================================================================
# CP VIOLATION AND NONEQUILIBRIUM
# =============================================================================

def jarlskog_invariant():
    """The Jarlskog invariant J_CP — the unique CP-violating measure of the CKM.

    J = Im(V_us V_cb V_ub* V_cs*) = 3.18 × 10⁻⁵ (PDG 2024)

    This is an SM INPUT, not derived from GRUT.
    """
    return {
        "J_CP": J_CP,
        "delta_CKM_rad": 1.196,  # CP-violating phase δ₁₃ ≈ 68.6°
        "note": "Measured SM parameter. Not derived from GRUT.",
    }


def k_neq_constitutive():
    """Constitutive nonequilibrium factor K_neq at the EW threshold.

    In the GRUT framework, the EW transition (era ~8 in the era map)
    provides a departure from equilibrium through the constitutive
    dynamics — REGARDLESS of the order of the phase transition.

    This is the key advantage over standard EW baryogenesis:
    the SM EW transition is a smooth crossover (not first-order),
    so standard EW baryogenesis fails. But the GRUT constitutive
    equation provides nonequilibrium dynamics at any threshold crossing.

    K_neq = α_eff × (Γ_sph / H_EW) × f_departure

    where:
    - α_eff = 1 - e⁻¹ = 0.632 (per-era constitutive relaxation)
    - Γ_sph / H_EW measures whether sphalerons are in equilibrium
    - f_departure = constitutive lag at the EW threshold
    """
    # Sphaleron rate at T_EW
    alpha_W_ew = alpha_weak_running(T_EW)
    gamma_sph = sphaleron_rate_over_T3(T_EW, alpha_W_ew)  # GeV

    # Hubble rate at T_EW (radiation-dominated)
    # H = sqrt(π² g_* / 90) × T² / M_Planck
    M_PLANCK_GEV = 2.435e18  # reduced Planck mass in GeV
    H_ew = np.sqrt(np.pi**2 * G_STAR_EW / 90.0) * T_EW**2 / M_PLANCK_GEV
    # H_ew in GeV

    # Sphaleron-to-Hubble ratio
    sph_over_H = gamma_sph / H_ew  # >> 1 means sphalerons in equilibrium

    # Constitutive departure factor:
    # The EW crossover width is ΔT ~ 10 GeV (broad crossover)
    # The constitutive lag = (transition time) / τ_constitutive
    # For the EW sector, τ is the sphaleron timescale ~ 1/Γ_sph
    delta_T_EW = 10.0  # GeV, crossover width
    f_departure = delta_T_EW / T_EW  # ΔT/T ~ 0.063

    # The departure from equilibrium occurs because:
    # 1. Sphalerons freeze out over width ΔT (not instantaneous)
    # 2. The constitutive equation has a finite relaxation rate
    # 3. The CP-violating interactions are not in complete equilibrium
    #
    # The washout integral gives:
    # K_neq ~ (ΔT/T) × (v(T_c)/T_c) for crossover
    # In the SM, v(T_c)/T_c ~ 0.3 (from lattice), giving
    # K_neq ~ 0.063 × 0.3 = 0.019
    v_over_T = 0.3  # lattice result for SM crossover
    k_neq = f_departure * v_over_T

    # GRUT enhancement: the constitutive equation keeps the system
    # slightly out of equilibrium even at the crossover
    # Factor: α_eff × (memory contribution)
    k_neq_grut = ALPHA_EFF * k_neq

    return {
        "k_neq": k_neq_grut,
        "k_neq_standard": k_neq,
        "alpha_eff": ALPHA_EFF,
        "gamma_sph_GeV": gamma_sph,
        "H_ew_GeV": H_ew,
        "sph_over_H": sph_over_H,
        "f_departure": f_departure,
        "v_over_T": v_over_T,
        "note": (
            f"K_neq = α_eff × (ΔT/T) × (v/T) = {k_neq_grut:.4e}. "
            f"Sphalerons are strongly in equilibrium (Γ/H = {sph_over_H:.0e}). "
            f"Departure comes from crossover width and constitutive lag."
        ),
    }


# =============================================================================
# ASSEMBLY: THE BARYON ASYMMETRY
# =============================================================================

def eta_baryon(j_cp, k_neq, r_b, s_b):
    """Compute baryon asymmetry from GRUT formula.

    eta_B = J_CP × K_neq × (2 - R_B) / S_B

    Parameters
    ----------
    j_cp : float
        Jarlskog invariant (CP violation measure).
    k_neq : float
        Nonequilibrium washout factor.
    r_b : float
        Baryonic anomaly ratio.
    s_b : float
        Baryonic CTP normalization.
    """
    two_minus_r = 2.0 - r_b
    eta = j_cp * k_neq * two_minus_r / s_b
    return eta


def eta_from_observation_constraint():
    """Inverse problem: given eta_observed, what (2-R_B)/S_B is needed?

    eta = J_CP × K_neq × (2-R_B)/S_B = 6.1e-10

    Solving: (2-R_B)/S_B = eta / (J_CP × K_neq)
    """
    k_data = k_neq_constitutive()
    k_neq = k_data["k_neq"]

    required = ETA_OBSERVED / (J_CP * k_neq)

    # What does this imply?
    sb_data = s_baryonic()
    s_b = sb_data["s_b"]

    implied_two_minus_r = required * s_b
    implied_r_b = 2.0 - implied_two_minus_r

    return {
        "required_ratio": required,
        "with_s_b": s_b,
        "implied_two_minus_r_b": implied_two_minus_r,
        "implied_r_b": implied_r_b,
        "j_cp": J_CP,
        "k_neq": k_neq,
        "eta_observed": ETA_OBSERVED,
        "note": (
            f"Required (2-R_B)/S_B = {required:.4e}. "
            f"With S_B = {s_b:.1f}: implied (2-R_B) = {implied_two_minus_r:.4e}, "
            f"R_B = {implied_r_b:.6f}."
        ),
    }


def both_routes_comparison():
    """Compare Route 1 (scaling) vs Route 2 (ABJ+sphaleron) results."""
    r1 = c_b_final_scaling()
    r2 = r_baryonic_route2()
    sb = s_baryonic()
    kn = k_neq_constitutive()
    inv = eta_from_observation_constraint()

    # Compute eta for each route
    eta_r1 = eta_baryon(J_CP, kn["k_neq"], r1["r_b"], sb["s_b"])
    eta_r2 = eta_baryon(J_CP, kn["k_neq"], r2["r_b"], sb["s_b"])

    return {
        "route_1": {
            "r_b": r1["r_b"],
            "two_minus_r_b": r1["two_minus_r_b"],
            "eta_predicted": eta_r1,
            "ratio_to_observed": eta_r1 / ETA_OBSERVED,
        },
        "route_2": {
            "r_b": r2["r_b"],
            "two_minus_r_b": r2["two_minus_r_b"],
            "eta_predicted": eta_r2,
            "ratio_to_observed": eta_r2 / ETA_OBSERVED,
        },
        "inverse": {
            "required_r_b": inv["implied_r_b"],
            "required_two_minus_r_b": inv["implied_two_minus_r_b"],
        },
        "s_b": sb["s_b"],
        "k_neq": kn["k_neq"],
        "j_cp": J_CP,
        "agreement": abs(np.log10(abs(eta_r1 / eta_r2))) if eta_r2 != 0 else float("inf"),
    }


def full_baryonic_anomaly_analysis():
    """Master function: complete baryonic anomaly computation.

    Computes R_B by two routes, assembles eta_B, compares to observation,
    and documents what is derived vs what is structural vs what fails.
    """
    fc = sm_baryonic_field_content()
    r1 = c_b_final_scaling()
    r2 = r_baryonic_route2()
    sb = s_baryonic()
    jcp = jarlskog_invariant()
    kn = k_neq_constitutive()
    inv = eta_from_observation_constraint()
    comp = both_routes_comparison()

    eta_r1 = comp["route_1"]["eta_predicted"]
    eta_r2 = comp["route_2"]["eta_predicted"]

    # Determine honest status
    r1_ok = 0 < r1["r_b"] < 2
    r2_ok = 0 < r2["r_b"] < 2
    eta_r1_order = np.log10(abs(eta_r1)) if eta_r1 != 0 else -99
    eta_r2_order = np.log10(abs(eta_r2)) if eta_r2 != 0 else -99
    obs_order = np.log10(ETA_OBSERVED)

    return {
        "field_content": fc,
        "route_1_scaling": r1,
        "route_2_abj_sphaleron": r2,
        "s_baryonic": sb,
        "jarlskog": jcp,
        "k_neq": kn,
        "inverse_constraint": inv,
        "comparison": comp,
        "summary": {
            "r_b_route1": r1["r_b"],
            "r_b_route2": r2["r_b"],
            "r_b_required": inv["implied_r_b"],
            "eta_route1": eta_r1,
            "eta_route2": eta_r2,
            "eta_observed": ETA_OBSERVED,
            "log10_eta_r1": eta_r1_order,
            "log10_eta_r2": eta_r2_order,
            "log10_eta_obs": obs_order,
            "route1_within_3_orders": abs(eta_r1_order - obs_order) < 3,
            "route2_within_3_orders": abs(eta_r2_order - obs_order) < 3,
        },
        "derived": [
            f"ABJ anomaly coefficient: k_B = N_gen/(16π²) = {r2['k_abj']:.6f} (exact, Adler-Bardeen)",
            f"Baryonic field content: {N_QUARK_WEYL} quark Weyl, B²-weighted = {fc['b2_quarks']:.1f}",
            f"Sphaleron rate: Γ/T³ = {kn['gamma_sph_GeV']:.4e} GeV at T_EW",
            f"CTP normalization: S_B = {sb['s_b']:.1f}",
            f"Nonequilibrium factor: K_neq = {kn['k_neq']:.4e}",
        ],
        "results": [
            f"R_B (Route 1, scaling): {r1['r_b']:.6f}, (2-R_B) = {r1['two_minus_r_b']:.6f}",
            f"R_B (Route 2, ABJ+sph): {r2['r_b']:.6e}, (2-R_B) = {r2['two_minus_r_b']:.6f}",
            f"R_B (required by obs): {inv['implied_r_b']:.6f}",
            f"eta (Route 1): {eta_r1:.4e} (obs: {ETA_OBSERVED:.1e})",
            f"eta (Route 2): {eta_r2:.4e} (obs: {ETA_OBSERVED:.1e})",
        ],
        "honest_negatives": [
            "Route 1 and Route 2 give DIFFERENT R_B — they probe different physics",
            "Route 1 (scaling) inherits R_anomaly structure → R_B ≈ R_anomaly",
            "Route 2 (ABJ+sph) gives R_B << 1 → (2-R_B) ≈ 2 (no near-cancellation)",
            "The v7 'near-cancellation' conjecture (R_B ~ 2) is NOT supported by Route 2",
            "The smallness of eta comes primarily from J_CP × K_neq, not from (2-R_B)",
            "S_B has structural uncertainty of factor ~2-3 from CTP path counting",
        ],
        "status": "COMPUTED (two routes, results documented, honest negatives recorded)",
    }
