#!/usr/bin/env python3
"""WALL A, STAGE A4: the dual-gauge check, under the FROZEN A3 protocol.

BUILDER NOTE (disclosed): built by the CHECKER (Claude) under the standing
build-and-disclose arrangement, on the owner's directive, while Ox was stalled.
The second-author countersign slot is OPEN: Ox (or an independent verifier pass)
reviews this instrument; it is not self-certified.

STANDING STATE: commit 8347ac8. A3 FROZEN (checker-amended F1-F7); this instrument
treats WALL_A_A3_DECLARATIONS.md / WALL_A_A3_REGISTRY.json as immutable law.
W-0 FENCE: computed-and-reported, NOT banked. No register edits.

WHAT A4 ESTABLISHES (Declaration 5, as frozen): the synchronous-gauge computation
reproduces the gauge-invariant content of the gauge-UNFIXED computation (A1's full
untruncated h). At the vertex level that decomposes into FOUR facts, each computed:
  (2) the synchronous vertex from the sliced expansion equals the unfixed vertex's
      ij-block (expected BY LINEARITY of L1 in h -- stated honestly: this gate is
      confirmation, not discovery);
  (3) the gauge transformation TO synchronous exists; its residual family is
      zeta^0 = C(x)/a with zeta_i = C_i(x) - (d_i C) Ia(eta), Ia' = 1/a. THE FROZEN F3
      PRODUCT CHARACTERISATION WAS REFUTED BY THE VERIFIER FLEET (the first version of
      this instrument hard-coded the zeta_i conjunct -- a print-statement fact in the
      checker's own code); corrected by substitution with negative control, and the
      frozen clause superseded by WALL_A_A3_DECLARATIONS_V2_AMENDMENT.md;
  (4) the invariance identity: L1(delta_zeta h) == a^2 E (zeta.dphi) - d_m V^m
      -- verified from first principles (E from L0's Euler-Lagrange; V from the
      boundary bookkeeping of the simultaneous transport), identically in
      (phi, zeta, a(eta)), friction term included. This is what makes the
      unfixed-vs-synchronous difference pure orbit: the two computations differ by
      an orbit variation with the derived zeta, hence by EoM terms + a total
      derivative and nothing else.
  (5) TT blindness: the spatial-TT projection of the orbit direction vanishes
      identically (the countersigned delta h^TT = 0), so the TT coupling -- the
      gauge-invariant content -- is untouched by the transformation.
STEP 0 runs the FROZEN BARRED-INPUTS GUARD LIVE (its first exercise): load, echo,
scan (transitive imports, file reads with content hashes, own-source symbol scan),
FAIL non-zero on any match. Output reported verbatim.

Exit 0 iff every gate passes AND the guard is clean.
"""
import sympy as sp
import json, os, sys, hashlib

HERE = os.path.dirname(os.path.abspath(__file__))
READ_FILES = []          # every file this instrument reads, for the guard's hash scan

def tracked_read(path, mode='r'):
    READ_FILES.append(path)
    with open(path, mode) as f:
        return f.read()

# ================= STEP 0: THE FROZEN GUARD, LIVE =================
print("=== STEP 0: BARRED-INPUTS GUARD (first live exercise; frozen registry is law) ===")
REGISTRY_PATH = os.path.join(HERE, "WALL_A_A3_REGISTRY.json")
registry = json.loads(tracked_read(REGISTRY_PATH))
print("   REGISTRY ECHO (frozen A3, verbatim):")
print("   " + json.dumps(registry["g0_spectral_wiring"]["barred_inputs"], indent=1).replace("\n", "\n   "))
print(f"   registry status: {registry['status']}")
barred_names = set()
barred_files = {}
for entry in registry["g0_spectral_wiring"]["barred_inputs"]:
    for o in entry.get("objects", []):
        barred_names.add(o)
    for f in entry.get("files", []):
        barred_files[f] = entry.get("sha256", {}).get(f)
# (a) transitive import scan (sys.modules at scan time, per the frozen F5 hardening)
mod_hits = [mname for mname in list(sys.modules)
            if any(b.lower() in mname.lower() for b in barred_names)
            or any(mname.split('.')[-1] + ext in barred_files for ext in ('.py',))]
# (b) file-read scan: names AND content hashes
read_hits = []
for p in READ_FILES:
    base = os.path.basename(p)
    if base in barred_files and base != "WALL_A_A3_REGISTRY.json":
        read_hits.append(base + " (by name)")
    h = hashlib.sha256(open(p, 'rb').read()).hexdigest()
    for bf, bh in barred_files.items():
        if bh and h == bh:
            read_hits.append(f"{p} (content-hash match to barred {bf})")
# (c) own-source symbol scan (barred object names as identifiers)
own_src = tracked_read(os.path.abspath(__file__))
sym_hits = [b for b in barred_names if b in own_src.replace('barred_names', '')
            and f'"{b}"' not in own_src]  # quoted occurrences are the registry echo itself
guard_hits = mod_hits + read_hits + sym_hits
print(f"   scan: {len(sys.modules)} loaded modules, {len(READ_FILES)} files read, "
      f"{len(barred_names)} barred symbols, {len(barred_files)} barred files")
if guard_hits:
    print(f"   GUARD TRIPPED: {guard_hits} -- THE RUN IS VOID (non-zero exit).")
    sys.exit(2)
print("   GUARD CLEAN: no barred module, file, hash, or symbol reached this run.")

# ================= STEP 1: OBJECT REGISTRY =================
print("\n=== STEP 1: OBJECT REGISTRY (synchronous-gauge objects, typed before algebra) ===")
for k, v in {
    "gauge":      "synchronous: h_00 = h_0i = 0 (delta g_00 = delta g_0i = 0); ONLY h_ij survive",
    "residual":   "DERIVED here, and the frozen F3 clause CORRECTED (v2 amendment): zeta^0 = C(x)/a(eta), "
                  "zeta_i = C_i(x) - (d_i C) Ia(eta) with Ia'=1/a -- the C-coupled piece is MANDATORY "
                  "and time-dependent; asymptotic coincidence at eta -> -infty kills the C-sector, fixes C_i",
    "orbit":      "delta h_mn = 2(a'/a) zeta^0 eta_mn + d_m zeta_n + d_n zeta_m (countersigned "
                  "Lie_xi g form, a'-term included); zeta_m = eta_mn zeta^n, mostly-minus",
    "first_comp": "gauge-UNFIXED: A1's full untruncated h_mn (per frozen F3 correction -- NOT de Donder)",
    "L1":         "per-kappa interaction: L1(h) = a^2 [ (1/4) h_tr (dphi)^2 - (1/2) h^{mn} d_m phi d_n phi ]"
                  " - (1/4) a^4 m^2 h_tr phi^2  (countersigned A1 structure)",
    "signature":  "eta = diag(1,-1,-1,-1); indices raised/lowered with eta; a(eta) factors explicit",
}.items():
    print(f"   {k:10s}: {v}")

eta_c, xs, ys, zs = sp.symbols('eta x y z')
COORDS = (eta_c, xs, ys, zs)
a = sp.Function('a', positive=True)(eta_c)
m, kappa = sp.symbols('m kappa', positive=True)
ETA = sp.diag(1, -1, -1, -1)
phi = sp.Function('phi')(*COORDS)
zeta_up = [sp.Function(f'zeta{i}')(*COORDS) for i in range(4)]     # zeta^m CONTRAVARIANT
zeta_lo = [ETA[i, i]*zeta_up[i] for i in range(4)]
d = lambda F, mu: sp.diff(F, COORDS[mu])

def orbit(hsym=None):
    """delta h_mn = 2(a'/a) zeta^0 eta_mn + d_m zeta_n + d_n zeta_m."""
    return {(mu, nu): 2*(sp.diff(a, eta_c)/a)*zeta_up[0]*ETA[mu, nu]
                      + d(zeta_lo[nu], mu) + d(zeta_lo[mu], nu)
            for mu in range(4) for nu in range(4)}

# ================= STEP 2: THE SYNCHRONOUS VERTEX (sliced expansion) =================
print("\n=== STEP 2: SYNCHRONOUS VERTEX from the sliced expansion ===")
# Re-run the A1 programmatic expansion with the synchronous slice imposed at symbol level.
hsyms = {}
for mu in range(4):
    for nu in range(4):
        key = (min(mu, nu), max(mu, nu))
        hsyms.setdefault(key, sp.Symbol(f'h{key[0]}{key[1]}'))
def build_L1(sliced):
    hlo = {}
    for mu in range(4):
        for nu in range(4):
            v = hsyms[(min(mu, nu), max(mu, nu))]
            if sliced and (mu == 0 or nu == 0):
                v = sp.Integer(0)                      # synchronous slice: h_00 = h_0i = 0
            hlo[(mu, nu)] = v
    Hm = sp.Matrix(4, 4, lambda i, j: hlo[(i, j)])
    trH = sum(ETA[i, i]*Hm[i, i] for i in range(4))
    inv1 = ETA.inv() - kappa*ETA.inv()*Hm*ETA.inv()    # product-verified O(kappa) inverse (A1 SA E2)
    dm = list(sp.symbols('d0 d1 d2 d3'))
    PHI2 = sp.Symbol('PHI2')
    sng = a**4*(1 + kappa*trH/2)
    kin = sng*sp.Rational(1, 2)*sum((a**-2*inv1[i, j])*dm[i]*dm[j] for i in range(4) for j in range(4))
    mass = sng*sp.Rational(-1, 2)*m**2*PHI2
    return sp.expand(sp.expand(kin + mass).coeff(kappa, 1)), dm, PHI2
L1_full, dm, PHI2 = build_L1(sliced=False)
L1_syn, _, _ = build_L1(sliced=True)
# gate 2: the synchronous L1 equals the full L1 with the 0-row symbols set to zero
sub0 = {hsyms[(0, 0)]: 0, hsyms[(0, 1)]: 0, hsyms[(0, 2)]: 0, hsyms[(0, 3)]: 0}
g2 = sp.expand(L1_syn - L1_full.subs(sub0)) == 0
# and the ij-coefficients agree between the two derivations (per-component):
g2b = all(sp.expand(L1_syn.coeff(hsyms[(i, j)]) - L1_full.coeff(hsyms[(i, j)])) == 0
          for i in range(1, 4) for j in range(i, 4))
print(f"   synchronous L1 == full L1 restricted to the slice                 : {g2}")
print(f"   ij-block coefficients identical between the two derivations       : {g2b}")
print("   (EXPECTED BY LINEARITY of L1 in h -- this gate is confirmation, not discovery;")
print("    the dual-gauge content lives in steps 3-5.)")

# ================= STEP 3: THE TRANSFORMATION TO SYNCHRONOUS, DERIVED =================
print("\n=== STEP 3: gauge transformation to synchronous -- existence + the residual ===")
# Work per spatial Fourier mode: h_00, h_0i as functions of eta times e^{i k.x}; spatial
# derivative -> i k_i. The synchronous conditions are ODEs in eta:
#   delta h_00 = 2(a'/a) zeta^0 + 2 d_0 zeta_0        (eta_00 = +1, zeta_0 = zeta^0)
#   want: h_00 + delta h_00 = 0  =>  (a zeta^0)' = -(a/2) h_00
#   delta h_0i = d_0 zeta_i + d_i zeta_0              (zeta_i = -zeta^i)
#   want: h_0i + delta h_0i = 0
h00f = sp.Function('h00')(eta_c)
ki = sp.symbols('k1 k2 k3')
etp = sp.Symbol('eta_p')                                # integration variable
C0 = sp.Function('C0')(xs, ys, zs)                      # the residual, spatially arbitrary
ap = sp.Function('a', positive=True)(etp)
h00p = sp.Function('h00')(etp)
zeta0_sol = (sp.Integer(-1)/(2*a))*sp.Integral(ap*h00p, (etp, -sp.oo, eta_c)) + C0/a
# verify by differentiation that the synchronous condition holds identically:
lhs00 = h00f + 2*(sp.diff(a, eta_c)/a)*zeta0_sol + 2*sp.diff(zeta0_sol, eta_c)
g3a = sp.simplify(sp.expand(lhs00.doit() if hasattr(lhs00, 'doit') else lhs00)) == 0 or \
      sp.simplify(lhs00.rewrite(sp.Integral).doit() - 0) == 0
# sympy handles Integral differentiation: diff of Integral wrt upper limit gives integrand
lhs00_expl = sp.expand(h00f + 2*(sp.diff(a, eta_c)/a)*zeta0_sol + 2*sp.diff(zeta0_sol, eta_c))
g3a = sp.simplify(lhs00_expl) == 0
print(f"   zeta^0 = -(1/2a) INT a h_00 d eta' + C(x)/a  satisfies h_00 + delta h_00 = 0: {g3a}")
print("   zeta^0 homogeneous piece IS C(x)/a (a property of the ODE) -- but the FULL")
print("   residual family is NOT the frozen F3 product structure: fleet-refutation fix")
print("   below. The asymptotic prescription still kills the C-sector entirely.")
# zeta_i -- FLEET-REFUTATION FIX (2026-08-25): the first version HARD-CODED
# zeta_i_hom_is_time_indep = True (a print-statement fact, the defect class this program
# hunts -- caught in the CHECKER'S OWN build by the verifier fleet). The computation the
# assertion skipped is exactly the one that refutes the claimed product family: preserving
# h_0i = 0 with zeta^0 = C(x)/a FORCES d_0 zeta_i = -d_i(C/a) = -(d_i C)/a, so
#   zeta_lo_i = C_i(x) - (d_i C) * Ia(eta),   Ia'(eta) = 1/a(eta)
# -- a MANDATORY time-dependent piece coupled to C. The frozen F3 clause characterised the
# family as {C(x)/a} x {time-independent C_i(x)}: WRONG (superseding v2 issued). The
# parameter count (C, C_i) is unchanged and the asymptotic prescription still kills the
# full family. Computed now, by substitution, with negative control:
Cx = sp.Function('Cres')(xs, ys, zs)
Ci = [sp.Function(f'Cres{i}')(xs, ys, zs) for i in range(1, 4)]
Ia = sp.Function('Ia')(eta_c)                       # antiderivative of 1/a: Ia' = 1/a
zres_lo = [Cx/a] + [Ci[i-1] - sp.diff(Cx, COORDS[i])*Ia for i in range(1, 4)]
def dh_of(zlo):
    zup = [ETA[i, i]*zlo[i] for i in range(4)]
    return {(mu, nu): (2*(sp.diff(a, eta_c)/a)*zup[0]*ETA[mu, nu]
                       + d(zlo[nu], mu) + d(zlo[mu], nu))
            for mu in range(4) for nu in range(4)}
fix_Ia = lambda e: sp.expand(e.subs(sp.Derivative(Ia, eta_c), 1/a))
dres = dh_of(zres_lo)
g3b = all(sp.simplify(fix_Ia(dres[(0, nu)])) == 0 for nu in range(4))
print(f"   TRUE residual family (zeta^0=C/a, zeta_i = C_i - (d_i C) Ia, Ia'=1/a)")
print(f"   preserves BOTH synchronous conditions delta h_00 = delta h_0i = 0             : {g3b}")
# negative control: the REFUTED product family (time-independent zeta_i, d_i C != 0)
zbad_lo = [Cx/a] + [Ci[i-1] for i in range(1, 4)]
dbad = dh_of(zbad_lo)
g3c = any(sp.simplify(fix_Ia(dbad[(0, i)])) != 0 for i in range(1, 4))
print(f"   REFUTED product family (time-independent zeta_i) EXITS the gauge:")
print(f"   delta h_0i = (d_i C)/a != 0 exhibited (negative control)                      : {g3c}")
print("   The frozen F3 clause's product characterisation is WRONG -- corrected here and")
print("   superseded by WALL_A_A3_DECLARATIONS_V2_AMENDMENT.md. Post-prescription content")
print("   unchanged: asymptotic coincidence at eta -> -infty kills C (and its coupled")
print("   time-dependent piece), leaving time-independent spatial reparametrisations.")
g3 = g3a and g3b and g3c

# ================= STEP 4: THE INVARIANCE IDENTITY, FIRST PRINCIPLES =================
print("\n=== STEP 4: L1(delta_zeta h) == a^2 E (zeta.dphi) - d_m V^m  (identically) ===")
# Every ingredient derived from its own principle, then the four-term combination checked:
#   E  from L0's Euler-Lagrange:  L0 = (a^2/2)(dphi)^2 - (a^4/2) m^2 phi^2
#   V  from the transport bookkeeping: V^m = a^2 (d^m phi)(zeta.dphi) - zeta^m L0
#   delta phi = zeta^alpha d_alpha phi  (the transport the h-only variation omits)
dphi = [d(phi, mu) for mu in range(4)]
dphi_up = [ETA[mu, mu]*dphi[mu] for mu in range(4)]
dphi2 = sum(dphi_up[mu]*dphi[mu] for mu in range(4))
L0 = a**2/2*dphi2 - a**4/2*m**2*phi**2
# Euler-Lagrange: E_op = -( d_m (dL0/d(d_m phi)) - dL0/dphi ) organised to the standard form
EL = sum(d(sp.diff(L0, dphi[mu]), mu) for mu in range(4)) - sp.diff(L0, phi)
E_std = a**2*(sp.diff(phi, eta_c, 2) + 2*(sp.diff(a, eta_c)/a)*sp.diff(phi, eta_c)
              - sum(sp.diff(phi, COORDS[i], 2) for i in range(1, 4)) + a**2*m**2*phi)
gE = sp.simplify(sp.expand(EL - E_std)) == 0
print(f"   Euler-Lagrange of L0 == a^2 [phi'' + 2(a'/a)phi' - lap phi + a^2 m^2 phi]     : {gE}")
# L1 evaluated on the orbit direction (position space, exact):
dh = orbit()
h_tr_dh = sum(ETA[mu, mu]*dh[(mu, mu)] for mu in range(4))
dh_up = {(mu, nu): ETA[mu, mu]*ETA[nu, nu]*dh[(mu, nu)] for mu in range(4) for nu in range(4)}
L1_dh = (a**2*(sp.Rational(1, 4)*h_tr_dh*dphi2
               - sp.Rational(1, 2)*sum(dh_up[(mu, nu)]*dphi[mu]*dphi[nu]
                                       for mu in range(4) for nu in range(4)))
         - sp.Rational(1, 4)*a**4*m**2*h_tr_dh*phi**2)
zeta_dphi = sum(zeta_up[al]*dphi[al] for al in range(4))
Vm = [a**2*dphi_up[mu]*zeta_dphi - zeta_up[mu]*L0 for mu in range(4)]
divV = sum(d(Vm[mu], mu) for mu in range(4))
resid = sp.simplify(sp.expand(L1_dh - (EL*zeta_dphi - divV)))
g4 = resid == 0
print(f"   L1(delta h) - [E (zeta.dphi) - d_m V^m] == 0, arbitrary phi/zeta/a(eta)       : {g4}")
if not g4:
    print(f"   RESIDUAL (diagnose before report): {resid}")
print("   => the unfixed and synchronous computations differ by L1(delta h) with the")
print("      derived zeta: pure bath-EoM (friction included) + total derivative. The")
print("      gauge-invariant content CANNOT differ between them. Constant-H trap covered:")
# constant-H trap plant: drop the (a'/a) term from the orbit -> identity must FAIL
dh_trap = {(mu, nu): d(zeta_lo[nu], mu) + d(zeta_lo[mu], nu) for mu in range(4) for nu in range(4)}
htr_t = sum(ETA[mu, mu]*dh_trap[(mu, mu)] for mu in range(4))
dhu_t = {(mu, nu): ETA[mu, mu]*ETA[nu, nu]*dh_trap[(mu, nu)] for mu in range(4) for nu in range(4)}
L1_t = (a**2*(sp.Rational(1, 4)*htr_t*dphi2
              - sp.Rational(1, 2)*sum(dhu_t[(mu, nu)]*dphi[mu]*dphi[nu]
                                      for mu in range(4) for nu in range(4)))
        - sp.Rational(1, 4)*a**4*m**2*htr_t*phi**2)
resid_t = sp.simplify(sp.expand(L1_t - (EL*zeta_dphi - divV)))
g4t = resid_t != 0
print(f"      orbit WITHOUT the 2(a'/a)zeta^0 term FAILS the identity (plant detects)    : {g4t}")

# ================= STEP 5: TT BLINDNESS OF THE ORBIT =================
print("\n=== STEP 5: spatial-TT projection of the orbit direction vanishes ===")
# Per spatial Fourier mode k, on the spatial block: delta h_ij = 2(a'/a) zeta^0 eta_ij
# + d_i zeta_j + d_j zeta_i -> ( -2(a'/a) zeta^0 delta_ij + i(k_i zeta_j + k_j zeta_i) ).
# The spatial TT projector P_ij,kl = (T_ik T_jl + T_il T_jk)/2 - T_ij T_kl / 2,
# T_ij = delta_ij - k_i k_j / k^2, annihilates BOTH pieces:
k1, k2, k3 = sp.symbols('k1 k2 k3', real=True)
kv = [k1, k2, k3]
k2n = k1**2 + k2**2 + k3**2
z0s, zv = sp.Symbol('z0'), list(sp.symbols('zv1 zv2 zv3'))
apr = sp.Symbol('aprime_over_a')
dh_sp = {(i, j): -2*apr*z0s*(1 if i == j else 0) + sp.I*(kv[i]*zv[j] + kv[j]*zv[i])
         for i in range(3) for j in range(3)}
T = {(i, j): (1 if i == j else 0) - kv[i]*kv[j]/k2n for i in range(3) for j in range(3)}
PTT = {}
for i in range(3):
    for j in range(3):
        for kk in range(3):
            for ll in range(3):
                PTT[(i, j, kk, ll)] = (T[(i, kk)]*T[(j, ll)] + T[(i, ll)]*T[(j, kk)])/2 \
                                      - T[(i, j)]*T[(kk, ll)]/2
proj = {(i, j): sp.simplify(sum(PTT[(i, j, kk, ll)]*dh_sp[(kk, ll)]
                                for kk in range(3) for ll in range(3)))
        for i in range(3) for j in range(3)}
g5 = all(v == 0 for v in proj.values())
print(f"   P^TT_spatial [delta h_ij(orbit)] == 0 for arbitrary (zeta, a'/a, k)           : {g5}")
print("   (the countersigned delta h^TT = 0, instantiated: the trace piece dies on the")
print("    traceless part, the k zeta piece on the transverse part -- the TT coupling is")
print("    IDENTICAL in the two gauges, which is the gauge-invariant-content statement.)")
# plant: a NON-orbit perturbation must NOT be annihilated (the projector is not trivially zero):
probe = {(i, j): sp.Integer(1) if (i, j) in ((0, 1), (1, 0)) else sp.Integer(0)
         for i in range(3) for j in range(3)}
probe_out = sp.simplify(sum(PTT[(0, 1, kk, ll)]*probe[(kk, ll)] for kk in range(3) for ll in range(3)))
g5p = probe_out != 0
print(f"   projector non-vacuity plant: a generic h_12 probe SURVIVES projection         : {g5p}")

# ================= STEP 6: FLAT-LIMIT PLANT + WRONG-a PLANT =================
print("\n=== STEP 6: PLANTS on the synchronous vertex ===")
pu = list(sp.symbols('P0:4'))
qu = list(sp.symbols('Q0:4'))
dotf = lambda P, Q: sum(ETA[i, i]*P[i]*Q[i] for i in range(4))
# momentum-space ij-block from L1_syn via the A1-countersigned extraction (lower-index coeff):
plo = [ETA[i, i]*pu[i] for i in range(4)]
qlo = [ETA[i, i]*qu[i] for i in range(4)]
def vertex_from(L1x):
    G = {}
    for i in range(1, 4):
        for j in range(i, 4):
            coeff = sp.expand(L1x.coeff(hsyms[(i, j)]))
            if i != j:
                coeff = coeff/2
            out = sp.Integer(0)
            poly = sp.Poly(coeff, *dm, PHI2)
            for mono, cf in zip(poly.monoms(), poly.coeffs()):
                da = mono[:4]
                if sum(da) == 2:
                    idxs = [t for t in range(4) for _ in range(da[t])]
                    a_, b_ = idxs
                    out += cf*(-(2*plo[a_]*qlo[a_]) if a_ == b_
                               else -(plo[a_]*qlo[b_] + qlo[a_]*plo[b_]))
                elif mono[4] == 1:
                    out += 2*cf
            G[(i, j)] = sp.expand(kappa*out)
    return G
Gsyn = vertex_from(L1_syn)
cand = {(i, j): sp.expand((kappa*a**2/2)*(pu[i]*qu[j] + qu[i]*pu[j]
                                          - ETA[i, j]*(dotf(pu, qu) + a**2*m**2)))
        for i in range(1, 4) for j in range(i, 4)}
g6a = all(sp.expand(Gsyn[k] - cand[k]) == 0 for k in Gsyn)
print(f"   synchronous ij-vertex == countersigned A1 compact form (ij-block)             : {g6a}")
# flat-limit independent comparator: T^{ij} of the flat scalar, typed from the definition
Tij = {(i, j): sp.expand(-(pu[i]*qu[j] + qu[i]*pu[j]) + ETA[i, j]*(dotf(pu, qu) + m**2))
       for i in range(1, 4) for j in range(i, 4)}
g6b = all(sp.expand(Gsyn[k].subs(a, 1) - (-kappa/2)*Tij[k]) == 0 for k in Gsyn)
print(f"   flat limit a->1 reproduces the typed flat synchronous vertex                  : {g6b}")
# wrong-a plant: a^4 misplaced onto the kinetic channel must FAIL:
Gbad = {k: sp.expand((kappa*a**4/2)*(pu[k[0]]*qu[k[1]] + qu[k[0]]*pu[k[1]]
                                     - ETA[k[0], k[1]]*(dotf(pu, qu) + m**2))) for k in Gsyn}
g6c = any(sp.expand(Gbad[k] - cand[k]) != 0 for k in Gsyn)
print(f"   wrong-a plant (a^4 on kinetic, mass undressed) FAILS the comparison           : {g6c}")

# ================= STEP 7: VERDICT =================
gates = {"g0_guard_clean": True, "g2_slice_equality": bool(g2 and g2b),
         "g3_transformation_and_residual": bool(g3), "gE_euler_lagrange": bool(gE),
         "g4_invariance_identity": bool(g4), "g4t_constant_H_trap_detected": bool(g4t),
         "g5_TT_blindness": bool(g5), "g5p_projector_nonvacuous": bool(g5p),
         "g6a_vertex_match": bool(g6a), "g6b_flat_plant": bool(g6b),
         "g6c_wrong_a_plant_detected": bool(g6c)}
all_ok = all(gates.values())
verdict = ("A4 PASS: the synchronous-gauge computation reproduces the gauge-invariant "
           "content of the gauge-unfixed computation. The transformation to synchronous "
           "exists; its residual family is zeta^0 = C(x)/a with zeta_i = C_i(x) - (d_i C) Ia "
           "(the frozen F3 product characterisation was REFUTED by the fleet, superseded by "
           "the v2 amendment; the asymptotic prescription still kills the C-sector); the difference of the two "
           "computations is the orbit variation, which reduces identically to bath-EoM "
           "(friction included) + total derivative; the spatial-TT content is orbit-blind; "
           "plants (constant-H trap, wrong-a, projector vacuity) all detected. The frozen "
           "barred-inputs guard ran live and clean. Sigma_R^TT assembly is UNBLOCKED under "
           "the frozen protocol. The response-level dual-gauge check (Pi_nonlocal equality) "
           "re-runs at assembly per Declaration 5."
           if all_ok else "A4 INCOMPLETE OR ANOMALOUS -- see gates; report as found.")
print(f"\nVERDICT: {verdict}")
json.dump({"instrument": "wall_a_a4_dual_gauge.py",
           "builder": "checker (Claude), build-and-disclose; Ox countersign slot OPEN",
           "standing_state": "8347ac8; A3 frozen; W-0 computed-and-reported, not banked",
           "guard": {"clean": True, "modules_scanned": len(sys.modules),
                     "files_read": READ_FILES, "barred_symbols": len(barred_names),
                     "barred_files": len(barred_files)},
           "gates": gates, "verdict": verdict},
          open(os.path.join(HERE, "WALL_A_A4_RESULT.json"), "w"), indent=2)
print("result written: WALL_A_A4_RESULT.json")
sys.exit(0 if all_ok else 1)
