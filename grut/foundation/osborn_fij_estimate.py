"""
Best-effort numerical estimate of the antisymmetric Osborn 2-form F_ij
contracted with the SM beta function at M_Z.

Basis paper: Jack & Osborn, Nucl. Phys. B343 (1990) 647.
Complementary: Osborn, DAMTP/91-1 (Weyl consistency conditions).

The physical RG-improved object (Osborn 1991 eq 6.1) is:

    8 d_i beta_tilde_b = [chi^g_ij + (d_i w_j - d_j w_i)] beta^j,
    beta_tilde_b = beta_b + (1/8) w_i beta^i.

For a SINGLE coupling the antisymmetric part F_ij = d_i w_j - d_j w_i
vanishes identically. R = |b/a| does not shift through the w-mechanism.

For the full SM coupling space (g3, g2, gY, y_t, lambda) the antisymmetric
part can be non-zero through cross-coupling dependence of w_i.

This script evaluates the explicit gauge formulas from Jack-Osborn 1990
eq (5.12)-(5.13), computes F_ij for (g3, g2, gY) at 1-loop and 2-loop,
and gives a structural (not first-principles) estimate for the Yukawa-gauge
entry. No fitting, no free parameters. All assumptions flagged.

Honesty note: sections 6 (scalar quartic) and 7 (Yukawa) of Jack-Osborn
1990 provide the w_I and w_y formulas. The leading-order forms quoted in
the user's reading of those sections are:

    w_yt  ~ d/dy_t [(1/16pi^2)^2 * (1/6) * tr(Gamma^2)]
    w_lam ~ (1/16pi^2)^3 * (1/216) * g_lam

At leading order these Yukawa/scalar expressions are INDEPENDENT of gauge
couplings, so their cross-partial with a gauge coupling is zero at that
order. Non-zero F(gauge, Yukawa) first appears when 1-loop gauge
corrections to the Yukawa sector (or vice versa) are included --
formally a 2-loop object with genuine mixed g-y structure.
"""

import math

# ---------------------------------------------------------------------------
# SM coupling values at M_Z (MS-bar), standard references
# ---------------------------------------------------------------------------
g3 = math.sqrt(4 * math.pi * 0.1181)       # alpha_s(M_Z) = 0.1181
gY = math.sqrt(4 * math.pi * 0.01018)      # alpha_Y(M_Z) = 0.01018 (hypercharge)
g2 = math.sqrt(4 * math.pi * 0.03376)      # alpha_2(M_Z) = 0.03376
yt = 0.937                                  # top Yukawa at M_Z
lam = 0.126                                 # Higgs quartic at M_Z

# Loop factor h_i = g_i^2 / (16 pi^2)
four_pi2_16 = 16.0 * math.pi**2
h3 = g3**2 / four_pi2_16
h2 = g2**2 / four_pi2_16
hY = gY**2 / four_pi2_16

# ---------------------------------------------------------------------------
# Group-theory constants for each SM gauge factor
#   n_V : dim of adjoint (gauge bosons)
#   C   : adjoint Casimir, f_acd f_bcd = C delta_ab
#   R   : fermion index, tr(t_a t_b) = -R delta_ab, Dirac convention
#         with T_F = 1/2 per fundamental; for SM at M_Z use n_f=5 (top decoupled
#         on the nose; close enough for a structural estimate).
# ---------------------------------------------------------------------------
groups = {
    'SU(3)': dict(n_V=8, C=3, R=5/2, g=g3, h=h3),     # QCD with 5 active flavors
    'SU(2)': dict(n_V=3, C=2, R=3,   g=g2, h=h2),     # SU(2)_L with 12 Weyl doublets
    'U(1)':  dict(n_V=1, C=0, R=10,  g=gY, h=hY),     # abelian; R=sum(Y^2)*conv
}

# ---------------------------------------------------------------------------
# w_i(g_i) from Jack-Osborn 1990 eq (5.13), per gauge factor:
#
#     g_i * W_i = (n_V / 16pi^2) * [2 + (1/3)(51*C - 20*R) * h_i]
#
# Solving for W_i:
#     W_i(g_i) = (n_V / (16pi^2 * g_i)) * [2 + (1/3)(51*C - 20*R) * g_i^2/(16pi^2)]
#
# This is a function of g_i ALONE -- no dependence on other gauge couplings,
# on y_t, or on lambda. Therefore partial derivatives d_j W_i for j != i
# are zero at both 1-loop AND 2-loop from this formula.
# ---------------------------------------------------------------------------

def W_gauge(gi, n_V, C, R):
    """w_i for a simple-group gauge coupling at 2-loop (Jack-Osborn eq 5.13)."""
    h = gi**2 / four_pi2_16
    return (n_V / (four_pi2_16 * gi)) * (2.0 + (1.0/3.0) * (51*C - 20*R) * h)

print("="*72)
print("Step 1: Evaluate W_i for each SM gauge coupling at M_Z")
print("="*72)
W_g = {}
for name, g in groups.items():
    Wi = W_gauge(g['g'], g['n_V'], g['C'], g['R'])
    W_g[name] = Wi
    leading = g['n_V'] / (four_pi2_16 * g['g']) * 2.0
    correction = Wi - leading
    print(f"  {name}: g={g['g']:.4f}  W_i = {Wi:.6f}")
    print(f"     1-loop piece = {leading:.6f},  2-loop correction = {correction:+.6f}")

# ---------------------------------------------------------------------------
# Step 2: Verify F_{ij} = d_i W_j - d_j W_i = 0 for (g3, g2, gY) at 1-loop & 2-loop
#
# Since W_i depends only on g_i (from eq 5.13), d_j W_i = 0 for i != j.
# So F_ij = 0 in the 3x3 gauge block.
# ---------------------------------------------------------------------------
print()
print("="*72)
print("Step 2: Antisymmetric F_ij in the pure gauge sector")
print("="*72)
print("  F_{g_i, g_j} = d_{g_j} W_{g_i} - d_{g_i} W_{g_j}")
print("  W_i depends only on g_i -> d_{g_j} W_i = 0 for i != j.")
print("  Therefore F = 0 for all gauge-gauge pairs at 1-loop AND 2-loop.")
print()
print("  Contribution of pure gauge F_ij to beta_tilde_b:  EXACTLY ZERO.")

# ---------------------------------------------------------------------------
# Step 3: Yukawa sector leading W_yt formula
#
# From Jack-Osborn 1990 sec 7 (as relayed from the source text):
#
#     W_yt ~ d/d y_t [ (1/16pi^2)^2 * (1/6) * tr(Gamma^2) ]
#
# For a single Yukawa y_t, tr(Gamma^2) = y_t^2 (up to color/flavor multiplicity).
# Let N_t be the net multiplicity (3 colors * 1 top flavor = 3 for SM top
# coupling to Higgs; in Weyl-chirality bookkeeping SM top is one Dirac fermion
# with 3 colors). Use N_t = 3 as a representative number.
#
# At LEADING order this expression is INDEPENDENT of gauge couplings,
# so d_{g_i} W_yt = 0 at leading order in the Yukawa sector.
# ---------------------------------------------------------------------------
N_t = 3

def W_yukawa_leading(y, N):
    """Leading W_yt from Jack-Osborn eq (7.6) schematic form.
    tr(Gamma^2) = N * y^2 for a single Yukawa coupling with multiplicity N."""
    return (1.0 / four_pi2_16)**2 * (1.0/6.0) * 2 * N * y   # d/dy of (1/6)*N*y^2

W_yt = W_yukawa_leading(yt, N_t)
print()
print("="*72)
print("Step 3: Yukawa W_yt at leading order (Jack-Osborn eq 7.6)")
print("="*72)
print(f"  W_yt (leading)                = {W_yt:.3e}")
print("  At leading order W_yt is independent of (g3, g2, gY):")
print("     d_{g_i} W_yt |_leading     = 0")
print("  Therefore F_{yt, g_i} |_leading = 0 as well.")

# ---------------------------------------------------------------------------
# Step 4: Scalar quartic W_lam (Jack-Osborn eq 6.34 schematic)
#
#     W_lam ~ (1/16pi^2)^3 * (1/216) * g_lam
#
# Also independent of gauge couplings at leading order.
# ---------------------------------------------------------------------------
W_lam = (1.0 / four_pi2_16)**3 * (1.0/216.0) * lam
print()
print("="*72)
print("Step 4: Scalar quartic W_lambda at leading order (Jack-Osborn eq 6.34)")
print("="*72)
print(f"  W_lam (leading)               = {W_lam:.3e}")
print("  Independent of (g3, g2, gY, y_t) at leading order -> F = 0.")

# ---------------------------------------------------------------------------
# Step 5: Subleading mixing (rough structural estimate)
#
# Non-zero F(gauge, Yukawa) first appears when the Yukawa formula includes
# 1-loop gauge corrections to the fermion kinetic term (anomalous dimension
# gamma_psi ~ (g^2/16pi^2) * C_F), or when the gauge formula gets a Yukawa
# correction through fermion mass insertions (at 2-loop).
#
# Structural magnitude: a subleading W_yt correction ~ (1/y_t) * C_F * h_g
# would give d_{g_i} W_yt ~ C_F * g_i / (8pi^2 y_t).
# Contracting with beta^{g_i} at M_Z gives
#     F_{yt, g_i} * beta^{g_i}  ~  O(1) * g_i * beta_{g_i} / (8pi^2 y_t)
#
# We report this magnitude with explicit O(1) coefficient placeholder.
# ---------------------------------------------------------------------------
# SM 1-loop beta functions at M_Z
beta_g3 = -7.0 * g3 * h3       # QCD asymptotic freedom
beta_g2 = -19.0/6.0 * g2 * h2  # SU(2)_L
beta_gY = 41.0/10.0 * gY * hY  # U(1)_Y (GUT-normalized factor 41/10 = 4.1)
beta_yt = yt/four_pi2_16 * (4.5*yt**2 - 8*g3**2 - 2.25*g2**2 - (17.0/12.0)*gY**2)
beta_lam = (1.0/four_pi2_16) * (24*lam**2 - 6*yt**4)  # approx, gauge terms dropped

print()
print("="*72)
print("Step 5: SM beta functions at M_Z (1-loop)")
print("="*72)
print(f"  beta_g3        = {beta_g3:+.4e}")
print(f"  beta_g2        = {beta_g2:+.4e}")
print(f"  beta_gY        = {beta_gY:+.4e}")
print(f"  beta_yt        = {beta_yt:+.4e}")
print(f"  beta_lambda    = {beta_lam:+.4e}  (rough, gauge terms dropped)")

# Subleading F(yt, gi) structural magnitude with O(1) coefficient A.
#
# LOOP COUNTING (corrected per brother's review):
#   - W_yt first appears at 2-loop in Jack-Osborn eq (7.6), carrying (1/16pi^2)^2
#   - Gauge corrections to W_yt add another power of g^2/(16pi^2) -> 3-loop
#   - So d_{g_i} W_yt ~ A * g_i / y_t  *  (1/16pi^2)^2  (not 1/(8pi^2))
#
# An earlier draft used 1/(8pi^2), which under-counted the loop suppression
# by a factor of ~32 pi^2 ~ O(10^2) - O(10^3). The correct suppression is
# three-loop, so the realistic parametric shift is far smaller.
print()
print("="*72)
print("Step 6: Subleading F(yt, g_i) contribution -- parametric estimate")
print("  (corrected loop counting: F lives at 3-loop overall)")
print("="*72)
print("  F_{yt, g_i} ~ A * g_i * (1/16pi^2)^2 / y_t  with A = O(1)")
print()
A = 1.0
suppression = 1.0 / four_pi2_16**2   # correct 3-loop suppression
for name, coupling, beta in [('g3', g3, beta_g3), ('g2', g2, beta_g2), ('gY', gY, beta_gY)]:
    F_times_beta = -A * coupling * beta * suppression / yt
    print(f"  F_{{yt, {name}}} * beta^{name}  ~ {F_times_beta:+.3e}  (A=1)")

total_F_beta_parametric = sum(
    -A * c * b * suppression / yt
    for (c, b) in [(g3, beta_g3), (g2, beta_g2), (gY, beta_gY)]
)
print()
print(f"  Sum (Yukawa-gauge): F_{{yt, gauge}} * beta^gauge ~ {total_F_beta_parametric:+.3e}")

# Convert to delta beta_tilde_b via eq (6.1): 8 * d_yt beta_tilde_b = F * beta
# The piece entering beta_tilde_b via flow: integrate (d_yt beta_tilde_b) * d yt
# over the running. At M_Z instantaneously, the shift to beta_b from this piece
# on a d ln(mu) step is (d_yt beta_tilde_b) * beta_yt * d ln(mu).
#
# The order-of-magnitude of the FULL Planck -> M_Z integrated shift is bounded
# by (F * beta) * beta_yt / 8 * Delta(ln mu), with Delta(ln mu) ~ 35.
d_yt_beta_tilde_b = total_F_beta_parametric / 8.0
delta_ln_mu = 35.0    # ~ ln(M_Planck / M_Z)
integrated_shift = d_yt_beta_tilde_b * beta_yt * delta_ln_mu

print()
print("="*72)
print("Step 7: Translate to an integrated shift of beta_tilde_b")
print("="*72)
print(f"  d_{{yt}} beta_tilde_b  ~ (F*beta) / 8  =  {d_yt_beta_tilde_b:+.3e}")
print(f"  Over ln(M_Planck/M_Z) ~ 35 e-folds, parametric integrated shift")
print(f"  in beta_tilde_b (upper-bound order of magnitude):   {integrated_shift:+.3e}")

# Compare to what's needed: R must go from 1.027 to 1.155, i.e. |b|
# must INCREASE by ~12.5%. beta_b at 1-loop = -3487/1440 ~ -2.42,
# so |delta b| needed ~ 0.30 at 1-loop magnitude scale.
b1loop = 3487.0/1440.0
R1loop = b1loop / (283.0/120.0)
R_target = 1.155
delta_b_needed = b1loop * (R_target/R1loop - 1.0)
print()
print("="*72)
print("Step 8: Compare to the shift GRUT needs")
print("="*72)
print(f"  |b|_1loop   = {b1loop:.4f}")
print(f"  R_1loop     = {R1loop:.4f}")
print(f"  R_target    = {R_target:.4f}")
print(f"  |delta_b| needed to reach R_target = {delta_b_needed:+.4f}")
print()
print(f"  Parametric best-effort shift from F-mechanism:  ~ {integrated_shift:+.3e}")
print(f"  Needed shift in b for GRUT target:              ~ {delta_b_needed:+.3e}")
ratio = abs(integrated_shift / delta_b_needed)
print(f"  Ratio (obtained / needed):                      ~ {ratio:.3e}")

print()
print("="*72)
print("Bottom line")
print("="*72)
print("  1. Pure gauge F_{ij} = 0 at 1-loop and 2-loop from eq (5.13).")
print("  2. Leading Yukawa (eq 7.6) and scalar (eq 6.34) W are independent")
print("     of gauge couplings -> F = 0 at that order as well.")
print("  3. The first non-zero F(gauge, Yukawa) lives at 3-loop overall")
print("     (W_yt at 2-loop from eq 7.6, one more loop from gauge mixing),")
print("     parametrized by A * g * beta_g * (1/16pi^2)^2 / y_t for A ~ O(1).")
print("  4. Integrated over the SM RG flow from M_Planck to M_Z (~35 e-folds),")
print(f"     this gives |delta beta_tilde_b|  ~ {abs(integrated_shift):.1e}")
print(f"     compared to |delta b| needed     ~ {abs(delta_b_needed):.1e}.")
print(f"     Shortfall factor                  ~ {1.0/ratio:.0f}x.")
print()
print("  The Osborn F_ij mechanism is DEFINITIVELY INSUFFICIENT to lift R")
print("  from 1.027 to 1.155 through the SM perturbative expansion. Leading")
print("  order gives zero exactly; the first non-zero cross-derivative lives")
print("  at 3-loop and is parametrically O(10^5 - 10^6)x short of what is")
print("  needed. No realistic section-7 prefactor closes this gap.")
print()
print("  Interpretation: the perturbative Osborn route cannot produce")
print("  GRUT's cosmological R shift. This is a definitive NEGATIVE result")
print("  from within perturbative QFT on the SM coupling space.")
