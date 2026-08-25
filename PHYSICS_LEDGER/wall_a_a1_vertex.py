#!/usr/bin/env python3
"""WALL A, STAGE A1: the full graviton-bath vertex Gamma^{mu nu}_{a}(x; y, z), CTP, untruncated.

STANDING STATE: commit e754d14. Kinematic half of Wall A CLOSED and countersigned:
21 -(gauge)-> 11 -(Lorentz-covariant response, +1 BOOKED)-> 3 -(equilibrium reciprocity/KMS)-> 2.
W-0 FENCE: everything computed here is COMPUTED-AND-REPORTED, NOT BANKED. No register edits.

MANDATED SEQUENCE: S_interaction -> Gamma^{mu nu} -> Gamma^TT -> Sigma_R^TT.
TT projection is a RECORDED DOWNSTREAM STEP; the discarded structures are data for the
assembly stage. No renormalisation choices, no spectral assumptions, no subtraction
schemes -- those belong to A3/G3. A1 stops at the vertex.

METHOD: the O(kappa) interaction term is obtained by PROGRAMMATIC EXPANSION of
sqrt(-g) g^{mu nu} on the de Sitter background -- no vertex formula is typed from
memory. Compact candidate forms are TESTED AGAINST the expansion; the Ward/EoM
identity and the flat-limit plant arbitrate.
"""
import sympy as sp
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
I = sp.I

# ================= STEP 0: OBJECT REGISTRY (before any algebra) =================
print("=== STEP 0: OBJECT REGISTRY ===")
REG = {
    "chart":        "de Sitter, FLAT SLICING: ds^2 = a(eta)^2 (d eta^2 - |dx|^2); a(eta) kept SYMBOLIC "
                    "(never set to -1/H*eta in A1 -- that is loop-stage data)",
    "signature":    "mostly-minus for the flat review layer: eta_{mu nu} = diag(1,-1,-1,-1), "
                    "matching the countersigned flat files (second_author_review.py et al.)",
    "metric_split": "g_{mu nu} = a^2(eta) (eta_{mu nu} + kappa h_{mu nu}); h = eta^{mu nu} h_{mu nu}; "
                    "kappa^2 = 32 pi G, kappa symbolic",
    "index_variance": "h_{mu nu} COVARIANT (as it enters g_{mu nu}); h^{mu nu} := eta^{ma} eta^{nb} h_{ab} "
                    "(BACKGROUND-raised); bath momenta p,q carried CONTRAVARIANT p^mu; all lowerings explicit",
    "bath":         "single real scalar phi, MINIMALLY coupled (xi = 0 declared; the xi R phi^2 improvement "
                    "is a recorded extension, not used): L = sqrt(-g) [1/2 g^{mu nu} d_mu phi d_nu phi - 1/2 m^2 phi^2]",
    "bath_state":   "Bunch-Davies DECLARED, NOT DERIVED -- the state choice is an INPUT to wall questions "
                    "(ii)/(iii), not an A1 output; recorded here so it cannot be chosen silently later",
    "slot":         "slot 1 = r-slot (response) as countersigned; the VERTEX has one graviton pair (mu,nu) "
                    "and two bath legs (p,q); graviton momentum K := p + q (all bath momenta incoming)",
    "omega_power":  "the vertex is a classical kernel (no omega-power of its own); the G1 chi/J distinction "
                    "enters only when the loop is turned into a response -- NOT here",
    "ctp":          "branch index a in {+,-}; S_CTP = S[phi_+] - S[phi_-]; vertex on branch a carries "
                    "eta_a in {+1,-1}; recorded at the CTP step, kept out of the derivation",
    "fourier":      "phi(x) = int e^{-i p.x} phi(p); each d_mu on a field -> -i p_mu on that leg; "
                    "S_int = (1/2) int Gamma^{mu nu}(p,q) h_{mu nu}(K) phi(p) phi(q), the 1/2 from "
                    "identical-field combinatorics; Gamma defined by functional derivative "
                    "delta^3 S / delta h delta phi delta phi (convention-free)",
}
for kk, vv in REG.items():
    print(f"   {kk:15s}: {vv}")

# ================= STEP 1: G0 DECLARATION =================
print("\n=== STEP 1: G0 DECLARATION (mode-counting / DOS discipline) ===")
print("   DERIVED   : the vertex itself -- a LOCAL covariant coupling h_{mu nu} T^{mu nu}[phi].")
print("               It uses NO density of states, NO spectral model, NO mode functions.")
print("   INHERITED-FROM-DOS-MODEL: the loop-level spectral content (Ohmic J(omega), the")
print("               registered (eps,tau2) family). Per the G0 gate, J(omega) is BARRED as")
print("               input to A1: A1 neither uses nor needs it. The bath spectral content")
print("               re-enters only at loop assembly, under A3/G3, where its provenance is")
print("               declared on that artifact's face.")
print("   BD state  : DECLARED (see registry) -- flagged as a wall-question input, not derived.")

# ============ STEP 2: THE DERIVATION -- programmatic expansion to O(kappa) ============
print("\n=== STEP 2: PROGRAMMATIC DERIVATION OF L^(1) ===")
eta, x, y, z = sp.symbols('eta x y z')
kappa, m = sp.symbols('kappa m', positive=True)
a = sp.Function('a')(eta)
ETA = sp.diag(1, -1, -1, -1)
hup = {}   # h^{mu nu} = eta-raised, as independent O(kappa) symbols
hlo = {}
for mu in range(4):
    for nu in range(4):
        hlo[(mu, nu)] = sp.Symbol(f'h{mu}{nu}')
# SYMMETRY IMPOSED (self-catch, 2026-08-24): the graviton is a SYMMETRIC tensor (10
# components). With h01, h10 as independent symbols the derivation "loses" the identical-
# field factor 2 in the c1 channel and the structural match fails. h must be symmetrised
# BEFORE the expansion, exactly as the physical field is.
for mu in range(4):
    for nu in range(4):
        if mu > nu:
            hlo[(mu, nu)] = hlo[(nu, mu)]
for mu in range(4):
    for nu in range(4):
        hup[(mu, nu)] = sum(ETA[mu, al]*ETA[nu, be]*hlo[(al, be)] for al in range(4) for be in range(4))
h_tr = sum(ETA[mu, mu]*hlo[(mu, mu)] for mu in range(4))          # h = eta^{mu nu} h_{mu nu}
# derivative monomials as commuting placeholders: dmu[mu] stands for d_mu phi
dmu = list(sp.symbols('d0 d1 d2 d3'))
phi2 = sp.Symbol('PHI2')                                          # stands for phi^2
kin0 = sum(dmu[al]*dmu[be]*ETA[al, be] for al in range(4) for be in range(4))   # (d phi)^2

# sqrt(-g) and g^{mu nu} to O(kappa), from g_{mu nu} = a^2 (eta + kappa h):
# SELF-CATCH (2026-08-24, third defect of this file): the first draft built M with a
# conditional that added kappa*h ONLY on the diagonal -- the off-diagonal metric
# perturbations never entered M, Minv came out diagonal, and every cross term vanished.
# The det-check PASSED anyway (det's O(kappa) term is the trace, which a diagonal M
# reproduces) -- a calibration plant that could not see this defect class. The Ward/EoM
# and flat-limit plants are what force the full M.
M = sp.Matrix(4, 4, lambda mu, nu: ETA[mu, nu] + kappa*hlo[(mu, nu)])
detM = sp.expand(M.det())
# sqrt expansion WITHOUT sp.series (it stalls on a 17-symbol polynomial):
# -detM is polynomial in kappa; sqrt(1 + kappa*c) = 1 + kappa*c/2 + O(kappa^2)
# CONFORMAL DRESSING (self-catch: first draft omitted it -- g_{mu nu} = a^2(eta+kappa h)
# means sqrt(-g) = a^4 sqrt(-det(eta+kappa h)) and g^{mu nu} = a^{-2}(eta+kappa h)^{-1};
# without these the vertex loses ALL a(eta)-dependence, which the flat plant cannot see
# but the de Sitter content requires):
neg_det = sp.expand(-detM)
det_const = neg_det.coeff(kappa, 0)
det_lin = sp.simplify(neg_det.coeff(kappa, 1))
chk_det = sp.simplify(det_const - 1)
# SECOND-AUTHOR CORRECTION (see second_author_a1_vertex.py E1): the original gate verified
# ONLY the O(kappa^0) term while its print claimed the O(kappa) check -- ironically on the
# same det-check this file's own headline lesson calls blind. The O(kappa) coefficient is
# now actually compared against h_tr and gated:
chk_det_lin = sp.simplify(det_lin - h_tr)
sqrt_neg_g = a**4*(1 + kappa*sp.expand(det_lin)/2)
gup = {}
Minv = M.inv()   # RATIONAL in kappa (adjugate/det) -- .coeff does NOT series-expand rationals.
# SELF-CATCH: first draft used Minv.coeff(kappa,0/1), which returned zeros and silently
# killed the kinetic term (g^00 = 0). Correct extraction: Taylor at kappa=0 via
# differentiation: g^{mu nu} = Minv|_0 + kappa * (dMinv/dkappa)|_0.
for mu in range(4):
    for nu in range(4):
        g0 = sp.simplify(Minv[mu, nu].subs(kappa, 0))
        g1 = sp.simplify(sp.diff(Minv[mu, nu], kappa).subs(kappa, 0))
        gup[(mu, nu)] = sp.expand(a**(-2)*(g0 + kappa*g1))
print(f"   sqrt(-g) expansion check, O(kappa^0) term == 1                : {'PASS' if chk_det == 0 else 'FAIL: '+str(chk_det)}")
print(f"   sqrt(-g) expansion check, O(kappa) term == h_tr (SA-added)    : {'PASS' if chk_det_lin == 0 else 'FAIL: '+str(chk_det_lin)}")
print(f"   sqrt(-g) = {sqrt_neg_g}")
print(f"   g^00 = {gup[(0, 0)]}")

# L = sqrt(-g) [ 1/2 g^{mu nu} d_mu phi d_nu phi - 1/2 m^2 phi^2 ]; collect O(kappa)
kin_term = sqrt_neg_g * sp.Rational(1, 2) * sum(
    gup[(mu, nu)]*dmu[mu]*dmu[nu] for mu in range(4) for nu in range(4))
mass_term = sqrt_neg_g * sp.Rational(-1, 2)*m**2*phi2
L1 = sp.expand(((kin_term + mass_term).subs(a, a)) - (
    sp.Rational(1, 2)*a**2*kin0 - sp.Rational(1, 2)*a**4*m**2*phi2))   # subtract O(1) background piece
L1 = sp.collect(sp.expand(L1), kappa).coeff(kappa)
L1 = sp.simplify(sp.expand(L1))
print(f"   L^(1)/kappa = {L1}")
# extract the three structural coefficients by monomial matching:
#   L1 = c1*h_{mu nu} d^mu phi d^nu phi + c2*h*kin0 + c3*h*m^2*phi2   (h raised, kin0=(d phi)^2)
# c1 from the h01*d0*d1 cross term (hup[(0,1)] = -h01, so L1 has -c1*h01*d0*d1*2? -- code decides):
E = sp.expand(L1)
c1 = sp.simplify(-sp.Rational(1, 2)*E.coeff(hlo[(0, 1)]).coeff(dmu[0], 1).coeff(dmu[1], 1))
# c2 from h00*d1^2 (only the h_tr*kin0 term contributes there):
c2 = sp.simplify(-E.coeff(hlo[(0, 0)]).coeff(dmu[1], 2))
# c3 from h00*m^2*phi2 (only the h_tr*phi2 term contributes):
c3 = sp.simplify(E.coeff(hlo[(0, 0)]).coeff(m**2, 1).coeff(phi2, 1))
print(f"   derived structural coefficients:")
print(f"      c1 (h_{{mu nu}} d^mu phi d^nu phi) = {c1}")
print(f"      c2 (h * (d phi)^2)               = {c2}")
print(f"      c3 (h * m^2 phi^2)               = {c3}")
# full structural match: L1 == c1*hup.d.d + c2*h_tr*kin0 + c3*h_tr*m^2*phi2
cand = c1*sum(hup[(mu, nu)]*dmu[mu]*dmu[nu] for mu in range(4) for nu in range(4)) \
     + c2*h_tr*kin0 + c3*h_tr*m**2*phi2
match = sp.simplify(sp.expand(L1 - cand)) == 0
print(f"   full monomial match L1 == c1*hup.d.d + c2*h*kin0 + c3*h*phi2   : {'PASS' if match else 'FAIL'}")
if not match:
    raise SystemExit("STOP: structural match failed; derivation unusable.")

# ---- momentum-space vertex via the functional-derivative rule (declared in registry) ----
#   d_a d_b (each d on its own leg, e^{-ipx}):  (−i p_a)(−i q_b) -> functional-derivative
#   symmetrisation gives −(p_a q_b + q_a p_b);  phi^2 gives +2;  eta^{ls} d_l d_s gives −2 p.q
pu = list(sp.symbols('P0:4'))          # bath leg 1, CONTRAVARIANT
qu = list(sp.symbols('Q0:4'))          # bath leg 2, CONTRAVARIANT
plo = [ETA[i, i]*pu[i] for i in range(4)]
qlo = [ETA[i, i]*qu[i] for i in range(4)]
def dot(P, Q):
    return sum(ETA[i, i]*P[i]*Q[i] for i in range(4))
pdq = dot(pu, qu)
Gam = {}
for mu in range(4):
    for nu in range(4):
        # mass rule: the phi^2 term c3*k*h_tr*m^2*phi^2 carries the m^2 explicitly
        # (SELF-CATCH: first draft wrote 2*c3*ETA without m^2 -- the vertex then had
        # -a^2 where -a^2 m^2 belongs; the flat plant's kappa*(m^2-1)/2 mismatch and the
        # Ward/TT failures all traced here)
        Gam[(mu, nu)] = sp.simplify(kappa*(
            -c1*(pu[mu]*qu[nu] + qu[mu]*pu[nu])
            - 2*c2*ETA[mu, nu]*pdq
            + 2*c3*m**2*ETA[mu, nu]))
print("\n   FULL VERTEX (momentum space, both bath legs incoming), Gamma^{mu nu}(p,q):")
print(f"   Gamma^00 = {Gam[(0, 0)]}")
print(f"   Gamma^01 = {Gam[(0, 1)]}")
# compact candidate form, TESTED against the derivation (never assumed):
cand_c = {}
for mu in range(4):
    for nu in range(4):
        cand_c[(mu, nu)] = sp.simplify((kappa*a**2/sp.Integer(2))*
                                       (pu[mu]*qu[nu] + qu[mu]*pu[nu] - ETA[mu, nu]*(pdq + a**2*m**2)))
compact_ok = all(sp.simplify(Gam[(mu, nu)] - cand_c[(mu, nu)]) == 0
                 for mu in range(4) for nu in range(4))
print(f"   COMPACT FORM TESTED: Gamma = (kappa*a^2/2)[p^m q^n + q^m p^n - eta^{{mn}}(p.q + a^2 m^2)]")
print(f"      matches the programmatic derivation: {'PASS' if compact_ok else 'FAIL -- record raw form'}")



# ============ STEP 3: PLANTS (before the de Sitter vertex is trusted) ============
print("\n=== STEP 3: PLANTS ===")
# (a) flat limit a -> 1 vs an INDEPENDENTLY TYPED standard vertex. Typed from the T^{mu nu}
#     definition with FT signs applied carefully: (d_mu phi)(d_nu phi) -> (−i p_mu)(−i q_nu)
#     = −p_mu q_nu, symmetrised over the two identical fields (kernel carries the 1/2):
KT = {}   # T^{mu nu} bilinear kernel: T^{mu nu} = (1/2) int KT^{mu nu} phi phi
for mu in range(4):
    for nu in range(4):
        KT[(mu, nu)] = (-(pu[mu]*qu[nu] + qu[mu]*pu[nu])
                        + ETA[mu, nu]*(pdq + m**2))
# S_int = -(kappa/2) int h_{mu nu} T^{mu nu}; with S = (1/2) int Gamma h phi phi the vertex is
# Gamma_std = -(kappa/2) * KT  (KT's symmetrisation already carries the identical-field 2's):
Gamma_std = {kk: sp.simplify(-sp.Rational(1, 2)*kappa*KT[kk]) for kk in KT}
flat = {}
for mu in range(4):
    for nu in range(4):
        flat[(mu, nu)] = sp.simplify(Gam[(mu, nu)].subs(a, 1) - Gamma_std[(mu, nu)])
flat_ok = all(v == 0 for v in flat.values())
print(f"   (a) flat limit a->1 vs independently typed standard vertex   : {'PASS' if flat_ok else 'FAIL'}")
if not flat_ok:
    for kk in flat:
        if flat[kk] != 0:
            print(f"        mismatch at ({kk}): {flat[kk]}")

# (b) deliberately mis-indexed variant (all-lower p.q, the standing defect family):
pdq_wrong = sum(pu[i]*qu[i] for i in range(4))     # NO metric -- the k^mu vs k_mu error
Gam_wrong = {}
for mu in range(4):
    for nu in range(4):
        Gam_wrong[(mu, nu)] = sp.simplify((kappa*sp.Rational(1, 2))*
                                          (pu[mu]*qu[nu] + qu[mu]*pu[nu] - ETA[mu, nu]*(pdq_wrong + m**2)))
wrong_flat = all(sp.simplify(Gam_wrong[(mu, nu)].subs(a, 1) - Gamma_std[(mu, nu)]) == 0
                 for mu in range(4) for nu in range(4))
print(f"   (b) mis-indexed variant (no-metric contraction) FAILS check  : {'PASS (detected)' if not wrong_flat else 'FAIL -- instrument blind'}")

# (c) Ward / EoM reconciliation: K_mu Gamma^{mu nu} with K = p + q (graviton momentum):
Ku = [pu[i] + qu[i] for i in range(4)]
ward = {}
for nu in range(4):
    ward[nu] = sp.simplify(sum(ETA[mu, mu]*Ku[mu]*Gam[(mu, nu)] for mu in range(4)))
ward_expected = {}
for nu in range(4):
    ward_expected[nu] = sp.simplify((kappa*a**2/sp.Integer(2))*
                                    ((dot(pu, pu) - a**2*m**2)*qu[nu] + (dot(qu, qu) - a**2*m**2)*pu[nu]))
ward_ok = all(sp.simplify(ward[nu] - ward_expected[nu]) == 0 for nu in range(4))
print(f"   (c) Ward/EoM: K_mu Gamma^{{mu nu}} == (kappa a^2/2)[(p^2-a^2m^2) q^nu + (q^2-a^2m^2) p^nu]")
print(f"       exact at general (p,q,a)                                : {'PASS' if ward_ok else 'FAIL'}")
# on-shell (flat layer): p^2 = q^2 = m^2 -> vanishes (gauge directions are EoM directions);
# numeric check with back-to-back loop kinematics p = q' , q = -p' (self-energy configuration):
P0, P1, P2, P3 = pu
Q0, Q1, Q2, Q3 = qu
sol = {P0: sp.Rational(7, 3), P1: sp.Rational(2, 5), P2: sp.Rational(1, 7), P3: sp.Rational(4, 5),
       Q0: sp.Rational(7, 3), Q1: sp.Rational(-2, 5), Q2: sp.Rational(-1, 7), Q3: sp.Rational(-4, 5)}
msq = sp.Rational(7, 3)**2 - (sp.Rational(2, 5)**2 + sp.Rational(1, 7)**2 + sp.Rational(4, 5)**2)
onshell_num = [sp.simplify(ward[nu].subs(a, 1).subs(sol).subs(m, sp.sqrt(msq))) for nu in range(4)]
onshell_ok = all(v == 0 for v in onshell_num)
print(f"       on-shell numeric check (p=q, p^2=m^2, a=1): all components zero: "
      f"{'PASS' if onshell_ok else 'FAIL: '+str(onshell_num)}")
# the mis-indexed variant must FAIL the Ward check too:
ward_wrong = [sp.simplify(sum(ETA[mu, mu]*Ku[mu]*Gam_wrong[(mu, nu)] for mu in range(4))
              - ward_expected[nu].subs(a, 1)) for nu in range(4)]
wrong_ward = any(v != 0 for v in ward_wrong)
print(f"       mis-indexed variant violates the Ward identity          : "
      f"{'PASS (detected)' if wrong_ward else 'FAIL -- instrument blind'}")
plants_ok = flat_ok and (not wrong_flat) and ward_ok and onshell_ok and wrong_ward


# ============ STEP 4: CTP BRANCH RECORD ============
print("\n=== STEP 4: CTP BRANCH STRUCTURE (recorded, kept out of the derivation) ===")
print("   S_CTP = S[phi_+] - S[phi_-]  =>  vertex on branch a:  Gamma_a^{mu nu} = eta_a * Gamma^{mu nu},")
print("   eta_+ = +1, eta_- = -1. The self-energy's CTP index structure (ab) and the retarded")
print("   projection (theta/eta_a algebra) belong to the loop-assembly stage, not A1.")
eta_branch = {'+': 1, '-': -1}
print(f"   recorded: Gamma_+ = +Gamma, Gamma_- = -Gamma  (branch factors {eta_branch})")

# ============ STEP 5: TT PROJECTION AS A RECORDED STEP (discards are DATA) ============
print("\n=== STEP 5: TT PROJECTION (downstream operation on the completed full vertex) ===")
Ku = [pu[i] + qu[i] for i in range(4)]
Ksq = sp.simplify(dot(Ku, Ku))
Klo = [ETA[i, i]*Ku[i] for i in range(4)]
thK = sp.Matrix(4, 4, lambda m, n: ETA[m, n] - Klo[m]*Klo[n]/Ksq)      # theta_{mu nu} (lower)
# VARIANCE REGISTRY (self-catch: first draft applied the all-lower theta to the UPPER-index
# Gamma^{rs} -- a mixed-variance contraction, the standing defect family; transversality
# then fails spuriously). The projector acting on an UPPER-index symmetric tensor needs
# theta_mu^rho (mixed) for the derivative part and theta^{mu nu} (upper) for the trace part:
d_ud = [[(1 if m == r else 0) - Ku[m]*Klo[r]/Ksq for r in range(4)] for m in range(4)]  # theta^mu_rho (UPPER mixed -- the form that contracts with K_mu)
th_uu = sp.Matrix(4, 4, lambda m, n: ETA[m, n] - Ku[m]*Ku[n]/Ksq)                       # theta^{mu nu}
P2_1 = {}
for m in range(4):
    for n in range(4):
        for r in range(4):
            for s in range(4):
                P2_1[(m, n, r, s)] = sp.cancel((d_ud[m][r]*d_ud[n][s] + d_ud[m][s]*d_ud[n][r])/2
                                               - th_uu[m, n]*thK[r, s]/3)
GamTT = {}
for m in range(4):
    for n in range(4):
        GamTT[(m, n)] = sp.cancel(sum(P2_1[(m, n, r, s)]*Gam[(r, s)] for r in range(4) for s in range(4)))
tt_trace = sp.simplify(sum(ETA[m, m]*GamTT[(m, m)] for m in range(4)))
tt_trans = [sp.simplify(sum(Klo[m]*GamTT[(m, n)] for m in range(4))) for n in range(4)]
tt_ok = (tt_trace == 0) and all(v == 0 for v in tt_trans)
print(f"   Gamma^TT traceless: {tt_trace == 0}   transverse: {all(v == 0 for v in tt_trans)}   -> {'PASS' if tt_ok else 'FAIL'}")
trace_scal = sp.simplify(sum(ETA[m, m]*Gam[(m, m)] for m in range(4)))
long_vec = [sp.simplify(sum(Klo[m]*Gam[(m, n)] for m in range(4))) for n in range(4)]
print("   DISCARDED STRUCTURES (data for the assembly stage):")
print(f"      trace scalar   eta_mn Gamma^mn = {sp.factor(sp.simplify(trace_scal/kappa))} * kappa")
print(f"      longitudinal   K_mu Gamma^mu nu = the Ward/EoM combination (step 3c), EoM-organised,")
print(f"         vanishing on-shell in the flat limit: the gauge-orbit reconciliation holds")
print(f"         (longitudinal vertex content lives in the orbit directions, as the Bardeen")
print(f"         machinery predicts).")
# SECOND-AUTHOR ANNOTATION: this gate recomputes the SAME contraction as gate 3c -- it is a
# consistency re-check, NOT an independent gauge-orbit reconciliation. The genuine flat-orbit
# content is nonetheless fully carried by 3c (Gamma.(K xi + xi K) == 2 xi.(K.Gamma) is an
# algebraic identity -- second_author_a1_vertex.py E3), and the FRW a'-layer reconciliation
# (Lie_xi g orbit with the 2(a'/a)xi^0 eta_mn term: delta L1 == bath-EoM-with-friction x
# (xi.dphi) + total derivative, identically) was performed by the independent verifier fleet.
recon = all(sp.simplify(long_vec[nu] - ward_expected[nu]) == 0 for nu in range(4))
print(f"      reconcile check (longitudinal == Ward combination; duplicates 3c): {'PASS' if recon else 'FAIL'}")


# ============ STEP 6: HONEST BOUNDARY -- A1 STOPS HERE ============
print("\n=== STEP 6: HONEST BOUNDARY ===")
print("   A1 ESTABLISHES: the full CTP vertex Gamma^{mu nu}_a(x;y,z) = eta_a (kappa a^2(x)/2)")
print("     x [p^mu q^nu + q^mu p^nu - eta^{mu nu}(p.q + a^2 m^2)] in momentum space, derived,")
print("     with the a^2 m^2 background-mass structure as the de Sitter-specific feature the")
print("     loop's a(eta) integrals will act on; plus the recorded TT projection and discards.")
print("   ASSUMED from A2/A5: the countersigned projectors and channel basis (used only in the")
print("     recorded projection); the EH channel identity (untouched here).")
print("   ASSUMED/DECLARED: minimal coupling xi=0; BD bath state (wall-question input).")
print("   A3 MUST DECLARE before loop assembly: the renormalisation scheme; the bath state's")
print("     status as computed vs assumed; the spectral wiring (G0: INHERITED-FROM-DOS-MODEL).")
print("   STOP REACHED CLEANLY: the vertex closes WITHOUT any renormalisation or spectral")
print("     choice -- no fork to report. A3/G3 own every such choice.")
all_ok = bool(chk_det == 0 and chk_det_lin == 0 and match and compact_ok and plants_ok and tt_ok and recon)
verdict = ("A1 COMPLETE: the full graviton-bath vertex is derived programmatically (no typed "
           "formula), passes the flat-limit plant, detects the mis-indexed plant, satisfies the "
           "Ward/EoM identity exactly, and its longitudinal content reconciles with the "
           "countersigned gauge orbit. TT projection recorded with discards as data. A1 STOPS "
           "at the vertex; A3/G3 own renormalisation, spectral wiring, and state status."
           if all_ok else "A1 INCOMPLETE OR ANOMALOUS -- see gates above; report as found.")
print("\nVERDICT:", verdict)
json.dump({
    "instrument": "wall_a_a1_vertex.py",
    "standing_state": "e754d14; kinematic half closed; W-0: computed-and-reported, not banked",
    "vertex": {"form": "Gamma^{mu nu} = (kappa a^2(eta)/2)[p^mu q^nu + q^mu p^nu - eta^{mu nu}(p.q + a^2 m^2)]",
               "derived_programmatically": True, "compact_form_matches": bool(compact_ok),
               "ctp": "Gamma_a = eta_a Gamma, eta_+ = +1, eta_- = -1"},
    "gates": {"sqrt_expansion_check": bool(chk_det == 0), "sqrt_expansion_okappa_check": bool(chk_det_lin == 0), "structural_match": bool(match),
              "flat_limit_plant": bool(flat_ok), "misindexed_detected": bool(not wrong_flat),
              "ward_eom_identity": bool(ward_ok), "onshell_vanishing": bool(onshell_ok),
              "misindexed_ward_detected": bool(wrong_ward),
              "tt_projection_wellformed": bool(tt_ok), "discard_reconciliation": bool(recon)},
    "discards_recorded": {"trace": "eta_mn Gamma^{mn} = -kappa a^2 (p.q + 2 a^2 m^2)",
                          "longitudinal": "K_mu Gamma^{mu nu} = (kappa a^2/2)[(p^2-a^2m^2) q^nu + (q^2-a^2m^2) p^nu]"},
    "declared_not_derived": ["xi = 0 minimal coupling", "Bunch-Davies bath state"],
    "a3_forks": ["renormalisation scheme", "bath state computed-vs-assumed",
                 "spectral wiring (G0 INHERITED-FROM-DOS-MODEL)"],
    "verdict": verdict,
}, open(os.path.join(HERE, "WALL_A_A1_RESULT.json"), "w"), indent=2)
print("result written: WALL_A_A1_RESULT.json")
import sys as _sys
_sys.exit(0 if all_ok else 1)

