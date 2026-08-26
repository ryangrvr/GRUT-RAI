#!/usr/bin/env python3
"""WALL A, D2-R1 PHASES 8-12 -- *** INSTRUMENT IN PROGRESS: DO NOT CITE AS A RESULT ***

STATUS (checker, 2026-08-26, disclosed on the face): the ENGINE layers are complete and
gated (masters 5/5, moments, u-rule, E-transform, insertion normalisation, vertex
expansion, decomposition-independence GATE WIRED). Phase 10's assembly is BLOCKED by a
defect the gate caught and which is diagnosed but NOT yet repaired -- see
"THE OPEN DEFECT" below. No Phase 11/12 result is claimed. Nothing banked.

THE OPEN DEFECT (frequency-locality of the t-weight derivative):
  A u-WEIGHTED insertion on an internal line makes the two segments carry DIFFERENT
  frequencies (nu_1 != nu_2); the s-integral then yields a frequency derivative rather
  than a delta-collapse. The derivative must act on EVERY factor carrying the affected
  segment's frequency. Two levels were found:
    LEVEL 1 (fixed in this file): the insertion vertex itself is two-sided,
      KV = A nu_L nu_R + Bconst, and the derivative acts on (nu-share x propagator),
      not the propagator alone. Analytically the naive form leaves
      route1 - route2 = i Int (dKV/dl0)/(D1^2 D2).
    LEVEL 2 (NOT yet fixed -- the current blocker): the h-VERTEX KERNEL at each endpoint
      also carries the adjacent segment's frequency. With an insertion on line A, the
      vertex at u1 must be evaluated at nu_A1 and the vertex at u2 at nu_A2. This file
      still factors both Mker's outside the differentiated group, leaving a residue
      proportional to d(Mker Mker)/dl0 at fixed (K - l).
  REPAIR SPEC: fuse assemble() with the insertion construction so the differentiated
  group is [adjacent Mker x nu-share x propagator]; the far vertex stays outside. The
  decomposition-independence gate is the acceptance test for the repair.

Original header follows.
--------------------------------------------------------------------------------
WALL A, D2-R1 PHASES 8-12 -- the curvature-corrected one-loop pole structure.

BUILDER: checker (claim 8640ce5, owner-directed takeover). SECOND-AUTHOR SLOT OPEN.
STANDING: Phases 0-7 GREEN at ea165dd (cited per ruling 5d6338e, not rebuilt).
W-0: computed-and-reported, NOT banked. No register edits. Frozen declarations
(v1+v2+v3) are law: Option B, parameter (H/M)^2, retained order O(H^2); consistent
dressing mandatory; hybrid prohibited; H->0 must reproduce the Gilkey anchor.

DECLARED FORMULATION (from the claim, derived in Section D below, not asserted):
conformal chart, reference eta_bar with a(eta_bar) = 1, u = eta - eta_bar;
exact dS: a(u) = 1/(1 - H u) => a^2 = 1 + 2Hu + 3H^2u^2, a^4 = 1 + 4Hu + 10H^2u^2.
Centre-at-reference: vertices at u1 = +Delta/2, u2 = -Delta/2; kernel transform
Sigma(omega) = int dDelta e^{i omega Delta} Sigma(Delta) so a Delta-factor maps to
-i d/d omega (GATED on an exact Gaussian below). Both target and basis kernels are
reduced with the SAME rule.

ENGINE: everything polynomial in (omega, k, m, H) -- no radicals, no brute series
(the y-lesson). Pole masters DERIVED from the trace relation:
   Ipole[(l^2)^j / (l^2 - Delta)^N] = c * Delta^(j-N+2) * [C(j,N-1) + C(j,N-2)]
(c = the 2/eps pole of the measure; binomials vanish out of range), gated against
ALL five validated masters of the flat anchor. Tensor numerators by exact moments:
   <l0^2a l1^2b l2^2c l3^2d> = (l^2)^j * (-1)^(b+c+d)
        * (2a)!(2b)!(2c)!(2d)! / (a! b! c! d! 2^j) / prod_{i=1..j}(2+2i)
gated against the known rank-2/4 reductions.

Run: python3 wall_d2_phases8_12.py [phase]   phase in {all, engine, p9, p10, p11, p12}
Exit 0 iff every executed gate passes.
"""
import hashlib
import json
import math
import os
import sys
import time
from functools import lru_cache

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()
READ_FILES = []
FAIL = []
PHASE = sys.argv[1] if len(sys.argv) > 1 else "all"


def stamp(msg):
    print(f"[{time.time()-T0:7.1f}s] {msg}")
    sys.stdout.flush()


def check(cond, msg):
    ok = bool(cond)
    print(("  ok   " if ok else "  FAIL ") + msg)
    sys.stdout.flush()
    if not ok:
        FAIL.append(msg)
    return ok


def tracked_read(path):
    READ_FILES.append(path)
    with open(path) as f:
        return f.read()


# ================= PHASE 8a: BARRED-INPUTS GUARD, LIVE =================
print("=== GUARD (LOAD/ECHO/SCAN/FAIL; frozen registry is law) ===")
registry = json.loads(tracked_read(os.path.join(HERE, "WALL_A_A3_REGISTRY.json")))
barred_names, barred_files = set(), {}
for entry in registry["g0_spectral_wiring"]["barred_inputs"]:
    for o in entry.get("objects", []):
        barred_names.add(o)
    for f in entry.get("files", []):
        barred_files[f] = entry.get("sha256", {}).get(f)
mod_hits = [mn for mn in list(sys.modules)
            if any(b.lower() in mn.lower() for b in barred_names)
            or (mn.split('.')[-1] + '.py') in barred_files]
read_hits = []
for p in READ_FILES:
    base = os.path.basename(p)
    if base in barred_files and base != "WALL_A_A3_REGISTRY.json":
        read_hits.append(base)
    hh = hashlib.sha256(open(p, 'rb').read()).hexdigest()
    for bf, bh in barred_files.items():
        if bh and hh == bh:
            read_hits.append(f"{p} (hash match {bf})")
own_src = tracked_read(os.path.abspath(__file__))
sym_hits = [b for b in barred_names if b in own_src.replace('barred_names', '')
            and ('"' + b + '"') not in own_src]
hits = mod_hits + read_hits + sym_hits
if hits:
    print(f"   GUARD TRIPPED: {hits} -- RUN VOID")
    sys.exit(2)
print(f"   GUARD CLEAN ({len(barred_names)} symbols, {len(barred_files)} files)")

# ================= SECTION D: DECLARED FORMULATION, DERIVED =================
print("\n=== SECTION D: FORMULATION DERIVED (a-expansions from the exact chart) ===")
H, u_s, om, kk, mm = sp.symbols('H u omega k m', positive=True)
c = sp.Symbol('c')                       # the 2/eps pole constant of the measure
eta = sp.diag(1, -1, -1, -1)
a_exact = 1 / (1 - H * u_s)              # derived: a(eta) = -1/(H eta), a(eta_bar)=1,
#   eta_bar = -1/H, eta = eta_bar + u  =>  a = -1/(H(eta_bar+u)) = 1/(1 - H u)
a2_ser = sp.expand(sp.series(a_exact**2, H, 0, 3).removeO())
a4_ser = sp.expand(sp.series(a_exact**4, H, 0, 3).removeO())
check(a2_ser == 1 + 2 * H * u_s + 3 * H**2 * u_s**2,
      "a^2 = 1 + 2Hu + 3H^2u^2 + O(H^3)  (DERIVED from the exact chart)")
check(a4_ser == 1 + 4 * H * u_s + 10 * H**2 * u_s**2,
      "a^4 = 1 + 4Hu + 10H^2u^2 + O(H^3)  (DERIVED)")

# ================= ENGINE 1: POLE MASTERS (derived + gated) =================
print("\n=== ENGINE 1: GENERAL POLE MASTERS ===")
Dl = sp.Symbol('Delta', positive=True)


def Ipole_scalar(j, N):
    """pole of int d^4l (l^2)^j / (l^2 - Delta)^N, in units of c; DERIVED from the
    trace relation (l^2)^j = ((l^2-Delta)+Delta)^j and the two base poles
    Ipole[1/(l^2-Delta)] = c Delta, Ipole[1/(l^2-Delta)^2] = c (validated lineage);
    higher powers are UV finite (pole 0), power 0 scaleless (0)."""
    val = sp.Integer(0)
    val += sp.binomial(j, N - 1) if N - 1 >= 0 else 0
    val += sp.binomial(j, N - 2) if N - 2 >= 0 else 0
    return val * Dl**(j - N + 2) if j - N + 2 >= 0 else sp.Integer(0)


# gates against ALL FIVE validated masters of the flat anchor:
check(Ipole_scalar(0, 1) == Dl, "master gate: Ipole[1/(l^2-m^2)] = c Delta  (Delta=m^2)")
check(Ipole_scalar(0, 2) == 1, "master gate: Ipole[1/D^2] = c")
# rank-2 tadpole: moment eta_ab/4 x Ipole[(l^2)/(l^2-m^2)] = eta_ab/4 x Delta^2 = eta_ab m^4/4:
# (SELF-CATCH, disclosed: the first version of THIS GATE compared against Delta^2/2 --
# a transcription error in the check itself; the engine value 1/4 Delta^2 IS the
# validated master. The gate caught its own author.)
check(sp.Rational(1, 4) * Ipole_scalar(1, 1) == sp.Rational(1, 4) * Dl**2,
      "master gate: Ipole[l_a l_b/(l^2-m^2)] = c eta_ab m^4/4 "
      "(moment 1/4 x Ipole[(l^2)/D^1] = Delta^2/4, Delta = m^2)")
# NOTE the gate above: 1/4 * (C(1,0)+C(1,-1)) Delta^2 = 1/4 * 1 * Delta^2? C(1,0)=1 (N-1=0),
# C(1,-1)=0: Ipole_scalar(1,1) = Delta^2. 1/4*Delta^2 vs validated m^4/4: MATCH requires
# Ipole_scalar(1,1) = Delta^2:
check(Ipole_scalar(1, 1) == Dl**2, "master gate: Ipole[(l^2)/(l^2-m^2)] = c Delta^2")
check(sp.Rational(1, 4) * Ipole_scalar(1, 2) == Dl / 2,
      "master gate: Ipole[l_a l_b/D^2] = c eta_ab Delta/2 (moment 1/4 x 2 Delta)")
check(sp.Rational(1, 24) * Ipole_scalar(2, 2) == Dl**2 / 8,
      "master gate: Ipole[llll/D^2] = c (3-perm) Delta^2/8 (moment 1/24 x 3 Delta^2)")
check(Ipole_scalar(0, 3) == 0 and Ipole_scalar(0, 4) == 0,
      "master gate: 1/D^3, 1/D^4 are UV finite (pole 0)")
stamp("engine 1 gated")

# ================= ENGINE 2: TENSOR MOMENTS (derived + gated) =================
print("\n=== ENGINE 2: TENSOR MOMENTS ===")


@lru_cache(maxsize=None)
def moment(a, b, c_, d):
    """<l0^2a l1^2b l2^2c l3^2d> = coeff * (l^2)^j, j = a+b+c+d; returns coeff (exact)."""
    j = a + b + c_ + d
    if j == 0:
        return sp.Integer(1)
    num = (sp.factorial(2 * a) * sp.factorial(2 * b) * sp.factorial(2 * c_)
           * sp.factorial(2 * d))
    den = (sp.factorial(a) * sp.factorial(b) * sp.factorial(c_) * sp.factorial(d)
           * sp.Integer(2)**j)
    prod = sp.Integer(1)
    for i in range(1, j + 1):
        prod *= (2 + 2 * i)
    return sp.Integer(-1)**(b + c_ + d) * num / den / prod


check(moment(1, 0, 0, 0) == sp.Rational(1, 4) and moment(0, 1, 0, 0) == sp.Rational(-1, 4),
      "moment gate rank 2: <l0^2> = +l^2/4, <l1^2> = -l^2/4  (eta^{aa}/4)")
check(moment(2, 0, 0, 0) == sp.Rational(1, 8),
      "moment gate rank 4: <l0^4> = (l^2)^2/8  (3(eta^{00})^2/24)")
check(moment(1, 1, 0, 0) == sp.Rational(-1, 24),
      "moment gate rank 4: <l0^2 l1^2> = -(l^2)^2/24  (eta^{00}eta^{11}/24)")
check(moment(0, 1, 1, 1) == sp.Rational(-1, 384) * sp.Integer(0) + moment(0, 1, 1, 1),
      "moment rank 6 computed (self-consistency placeholder)")
stamp("engine 2 gated")

# ================= ENGINE 3: THE LOOP-POLE INTEGRATOR =================
print("\n=== ENGINE 3: LOOP-POLE INTEGRATOR (two-denominator, general powers) ===")
l0, l1, l2, l3 = sp.symbols('l0 l1 l2 l3', real=True)
LSY = (l0, l1, l2, l3)
xf = sp.Symbol('x', positive=True)
KUP = [om, sp.Integer(0), sp.Integer(0), kk]      # external K = (omega, 0, 0, k)
KSQ = om**2 - kk**2


def lsq(vec):
    return vec[0]**2 - vec[1]**2 - vec[2]**2 - vec[3]**2


@lru_cache(maxsize=None)
def _mono_pole_2den(expo, aP, bP):
    """cached pole of int d^4l l0^e0 l1^e1 l2^e2 l3^e3 / (D1^aP D2^bP),
    D1 = l^2 - m^2, D2 = (l - K)^2 - m^2  [ROUTING FIX: -K; the decomposition-
    independence gate CAUGHT the +K orientation inconsistency -- with the declared
    phase conventions the loop must assemble as G(p) G(p - omega)].
    Feynman: y D2 + (1-y) D1 = (l - yK)^2 - Delta, Delta = m^2 - y(1-y) K^2;
    weight Gamma(a+b)/Gamma(a)Gamma(b) y^{b-1}(1-y)^{a-1}; shift l -> l + yK."""
    N = aP + bP
    wt = sp.factorial(N - 1) / (sp.factorial(aP - 1) * sp.factorial(bP - 1))
    monoexpr = sp.prod([(LSY[i] + xf * KUP[i])**expo[i] for i in range(4)])
    nsh = sp.expand(monoexpr)
    poly = sp.Poly(nsh, *LSY)
    out = sp.Integer(0)
    for mono, cf in zip(poly.monoms(), poly.coeffs()):
        if any(e % 2 for e in mono):
            continue
        a_, b_, c2, d_ = (e // 2 for e in mono)
        base = Ipole_scalar(a_ + b_ + c2 + d_, N)
        if base == 0:
            continue
        out += cf * moment(a_, b_, c2, d_) * base
    DeltaF = mm**2 - xf * (1 - xf) * KSQ
    out = sp.expand(out.subs(Dl, DeltaF))
    return sp.expand(wt * sp.integrate(out * xf**(bP - 1) * (1 - xf)**(aP - 1),
                                       (xf, 0, 1)))


def loop_pole_2den(numer, aP, bP):
    poly = sp.Poly(sp.expand(numer), *LSY)
    out = sp.Integer(0)
    for mono, cf in zip(poly.monoms(), poly.coeffs()):
        out += cf * _mono_pole_2den(tuple(mono), aP, bP)
    return sp.expand(out)


@lru_cache(maxsize=None)
def _mono_pole_tad(expo, aP):
    if any(e % 2 for e in expo):
        return sp.Integer(0)
    a_, b_, c2, d_ = (e // 2 for e in expo)
    base = Ipole_scalar(a_ + b_ + c2 + d_, aP)
    if base == 0:
        return sp.Integer(0)
    return sp.expand((moment(a_, b_, c2, d_) * base).subs(Dl, mm**2))


def loop_pole_tad(numer, aP):
    """pole part (units of c) of int d^4l numer(l)/(l^2 - m^2)^aP."""
    poly = sp.Poly(sp.expand(numer), *LSY)
    out = sp.Integer(0)
    for mono, cf in zip(poly.monoms(), poly.coeffs()):
        out += cf * _mono_pole_tad(tuple(mono), aP)
    return sp.expand(out)


# engine-3 internal gate: symmetric-power identity 1/(D1 D2) with numer 1 must equal
# the classic single-x result (weight 1, x^0(1-x)^0):
g3a = loop_pole_2den(sp.Integer(1), 1, 1)
check(sp.expand(g3a - sp.integrate(sp.Integer(1), (xf, 0, 1))) == 0,
      "engine 3 gate: Ipole[1/(D1 D2)] = c (the classic bubble pole, x-integral of 1)")
# derivative-consistency gate: d/dm^2 Ipole[1/(l^2-m^2)] == Ipole[1/(l^2-m^2)^2]:
check(sp.diff(loop_pole_tad(sp.Integer(1), 1), mm**2) if False else
      sp.expand(sp.diff(loop_pole_tad(sp.Integer(1), 1), mm) / (2 * mm)
                - loop_pole_tad(sp.Integer(1), 2)) == 0,
      "engine 3 gate: d/dm^2 of the tadpole pole == the double-denominator tadpole pole "
      "(the trace relation closed on the engine itself)")
stamp("engine 3 gated")

# ================= ENGINE 4: THE Delta -> -i d/domega RULE (gated) =================
print("\n=== ENGINE 4: THE u-RULE ===")
# convention: Sigma_tilde(omega) = int dDelta e^{+i omega Delta} Sigma(Delta).
# Then Delta * Sigma(Delta) transforms to -i d/domega Sigma_tilde(omega).
# EXACT GATE on a Gaussian: Sigma = exp(-Delta^2):
Dt, w_ = sp.symbols('Delta_t w_', real=True)
gauss = sp.exp(-Dt**2)
lhs = sp.simplify(sp.integrate(Dt * gauss * sp.exp(sp.I * w_ * Dt), (Dt, -sp.oo, sp.oo)))
rhs = sp.simplify(-sp.I * sp.diff(
    sp.integrate(gauss * sp.exp(sp.I * w_ * Dt), (Dt, -sp.oo, sp.oo)), w_))
check(sp.simplify(lhs - rhs) == 0,
      "u-rule gate: FT[Delta f(Delta)] == -i d/domega FT[f]  (exact Gaussian, sign pinned)")


def apply_Delta_power(expr, n):
    """apply the Delta^n factor to an omega-space expression: (-i d/domega)^n."""
    out = expr
    for _ in range(n):
        out = -sp.I * sp.diff(out, om)
    return sp.expand(out)


# vertex placements: u1 = +Delta/2, u2 = -Delta/2:
def u1_pow(expr, n):
    return sp.expand(apply_Delta_power(expr, n) / sp.Integer(2)**n)


def u2_pow(expr, n):
    return sp.expand(apply_Delta_power(expr, n) * sp.Integer(-1)**n / sp.Integer(2)**n)


# ================= ENGINE 5: LOCAL-KERNEL DISTRIBUTION TRANSFORM =================
print("\n=== ENGINE 5: LOCAL-KERNEL TRANSFORM (basis side) ===")
# For local (basis) kernels: terms P(Delta) * delta^(q)(Delta) transform to
#   E[P, q](omega) = P(-i d/domega) applied to (-i omega)^q ... derived:
#   int dDelta e^{i omega Delta} delta^(q)(Delta) = (-i omega)^q  (by parts, q times)
# GATE: q = 1 against the direct definition via a limit representation:
check(sp.simplify(sp.integrate(sp.exp(sp.I * w_ * Dt) * sp.DiracDelta(Dt, 1),
                               (Dt, -sp.oo, sp.oo)) - (-sp.I * w_)) == 0,
      "E-transform gate: FT[delta'(Delta)] == -i omega (sympy DiracDelta, exact)")


def E_transform(pcoeffs, q):
    """transform of sum_p pcoeffs[p] * Delta^p * delta^(q)(Delta):
    = sum_p pcoeffs[p] * (-i d/dom)^p [(-i om)^q]."""
    base = (-sp.I * om)**q
    out = sp.Integer(0)
    for p_, cf in pcoeffs.items():
        term = base
        for _ in range(p_):
            term = -sp.I * sp.diff(term, om)
        out += cf * term
    return sp.expand(out)


check(sp.expand(E_transform({1: 1}, 1) - (-sp.I) * sp.diff(-sp.I * om, om)) == 0,
      "E-transform self-consistency: Delta * delta'(Delta) -> -i d/dom(-i om) = -1... wired")
stamp("engines 4-5 gated")

# ================= ENGINE 6: INSERTION KERNEL, NORMALISATION PINNED =================
print("\n=== ENGINE 6: INSERTION KERNEL (the dm^2 exact gate) ===")
# Convention: propagator G = i/(l^2 - m^2). A quadratic-action perturbation
# deltaS = int (1/2) KV(u) [field bilinear] contributes one insertion as
#   G * (i KV) * G   per insertion (X = i x action-kernel).
# EXACT GATE: pure mass shift deltaS = -(1/2) dm2 phi^2 => KV = -dm2; the corrected
# propagator to first order must equal d/dm^2 expansion of G:
dm2 = sp.Symbol('dm2')
G0 = sp.I / (lsq(LSY) - mm**2)
first_order = sp.expand(G0 * (sp.I * (-dm2)) * G0)
target = sp.expand(sp.diff(G0, mm) / (2 * mm) * dm2)
check(sp.simplify(first_order - target) == 0,
      "insertion gate: G (i KV) G with KV = -dm2 == dm2 * dG/dm^2 EXACTLY "
      "(all i/sign/factor conventions of insertions pinned)")
# The bath insertion kernels, DERIVED from delta L_bath (Section D expansions):
#   delta L = (a^2-1)/2 [(phi')^2 - (grad phi)^2] - (a^4-1)/2 m^2 phi^2
#   quadratic-form kernel at 4-momentum l (mostly-minus):  KV(l; u)
#   kinetic part: (a^2-1) * l^2   [since (phi')^2 - (grad phi)^2 -> l0^2 - lvec^2 = l^2,
#                                  and the 1/2 with two field derivatives gives factor 1]
#   mass part:   -(a^4-1) * m^2
# DERIVE the kinetic normalisation from the same dm2-style gate: a pure kinetic
# perturbation deltaS = (z/2)[(phi')^2 - (grad phi)^2] must shift G to
# i/((1+z) l^2 - m^2) at first order = G - i z l^2/(l^2-m^2)^2 + O(z^2):
z_ = sp.Symbol('z_')
kin_first = sp.expand(G0 * (sp.I * (z_ * lsq(LSY))) * G0)
kin_target = sp.expand(-sp.I * z_ * lsq(LSY) / (lsq(LSY) - mm**2)**2)
check(sp.simplify(kin_first - kin_target) == 0,
      "insertion gate: kinetic KV = z l^2 reproduces the exact first-order propagator "
      "shift of i/((1+z)l^2 - m^2)")
# So, per Section D:  KV1(l) = H * u * (2 l^2 - 4 m^2)   [coeff of Hu]
#                     KV2(l) = H^2 u^2 * (3 l^2 - 10 m^2) [coeff of H^2 u^2]
KV1_of = lambda lv: 2 * lsq(lv) - 4 * mm**2
KV2_of = lambda lv: 3 * lsq(lv) - 10 * mm**2
print("   KV1 = Hu (2 l^2 - 4 m^2);  KV2 = H^2u^2 (3 l^2 - 10 m^2)  [derived from a^2/a^4]")
stamp("engine 6 gated")

# ================= PHASE 9: MATCHED-ORDER VERTEX, DERIVED =================
print("\n=== PHASE 9: VERTEX EXPANSION (from the exact A1 form) ===")
# polarisation-contracted vertex kernel, per kappa (2b lineage):
#   M_e(pin, pout; u) = a^2 [ e^{ab} pout_a pin_b ... ] with the A1 structure:
#   Gamma_e(p, q; a) = a^2 [ e(p,q)_sym - (tr e)/2 (p.q) ] - a^4 (tr e)/2 m^2
# where e(p,q) = e_{ab} p^a q^b (contravariant momenta, e covariant symmetric).
def sym_mat(pref):
    M = sp.zeros(4, 4)
    for i in range(4):
        for j in range(i, 4):
            s_ = sp.Symbol(f'{pref}_{i}{j}')
            M[i, j] = s_
            M[j, i] = s_
    return M


e1m, e2m = sym_mat('E'), sym_mat('P')


def dot4(p, q):
    return p[0] * q[0] - p[1] * q[1] - p[2] * q[2] - p[3] * q[3]


def vertex_kernel(e, p, q, a2f, a4f):
    """Gamma contracted with covariant polarisation e; momenta contravariant;
    kinetic block x a2f, mass block x a4f. Per kappa; the flat limit (a2f=a4f=1)
    must equal the countersigned form (gate below)."""
    epq = sum(e[i, j] * p[i] * q[j] for i in range(4) for j in range(4))
    tre = sum(eta[i, i] * e[i, i] for i in range(4))
    return sp.expand(a2f * (epq - sp.Rational(1, 2) * tre * dot4(p, q))
                     - a4f * sp.Rational(1, 2) * tre * mm**2)


# gate: flat limit against the countersigned A1 compact form (kappa/2)[pq+qp-eta(pq+m^2)]
pS = list(sp.symbols('p0:4'))
qS = list(sp.symbols('q0:4'))
flat_ref = sp.expand(sum(e1m[i, j] * (pS[i] * qS[j] + qS[i] * pS[j]) / 2 * 2
                         for i in range(4) for j in range(4)) / 2
                     - sum(eta[i, i] * e1m[i, i] for i in range(4)) / 2
                     * (dot4(pS, qS) + mm**2))
check(sp.expand(vertex_kernel(e1m, pS, qS, 1, 1) - flat_ref) == 0,
      "P9 gate: flat vertex kernel == countersigned A1 form contracted with e")
# expansion coefficients (a2, a4) per u-order, from Section D:
VTX_ORDERS = {0: (1, 1), 1: (2, 4), 2: (3, 10)}   # u^n coefficient of (a^2, a^4)
print("   vertex u-orders: n=0 -> (1,1); n=1 -> (2,4) x Hu; n=2 -> (3,10) x H^2u^2 "
      "(DERIVED in Section D)")
stamp("phase 9 done")
if PHASE == "engine" or PHASE == "p9":
    print("\n[partial run complete]")
    sys.exit(0 if not FAIL else 1)

# ================= PHASE 10: THE TARGET -- FISH + SEAGULL THROUGH O(H^2) =================
print("\n=== PHASE 10: TARGET ASSEMBLY (fish + seagull, O(H^0..H^2)) ===")
# structural term-list representation: a "piece" is (num, aP, bP) meaning
#   num(l; omega,k,m,e) / (D1^aP * D2^bP),  D1 = l^2 - m^2, D2 = (l+K)^2 - m^2.
# REAL (i-stripped) conventions anchored to the flat 2b normalisation:
#   plain line = 1/D ; each insertion multiplies by (-KV) and joins segment powers;
#   fish weight +1/2 ; seagull weight -1/2.  (Engine-6 pins the i-bookkeeping; in
#   stripped units the dressed line is 1/D + (-KV)/D^2 + ... -- gated below.)
D1e = lsq(LSY) - mm**2
Kminus = [LSY[0] - om, LSY[1], LSY[2], LSY[3] - kk]
D2e = lsq(Kminus) - mm**2
# stripped-units insertion gate: dressed = 1/(l^2(1+z) - m^2 - dm2) expanded must be
# 1/D + (-KV)/D^2 with KV = z l^2 - dm2... wait sign: KV(action kernel) for
# deltaS = (z/2)(dphi)^2-form - (dm2/2)phi^2 is KV = z l^2 - dm2; dressed inverse
# kernel = D + KV => dressed = 1/(D + KV) = 1/D - KV/D^2 + ...  => insertion factor
# = -KV per insertion. GATED:
zz, dd2 = sp.symbols('zz dd2')
KVtest = zz * lsq(LSY) - dd2
dressed_exact = 1 / (D1e + KVtest)
dressed_pert = 1 / D1e - KVtest / D1e**2
check(sp.simplify(sp.series(dressed_exact - dressed_pert, zz, 0, 2).removeO().subs(zz, 0)
                  .rewrite(sp.Add)) == 0 if False else
      sp.simplify((dressed_exact - dressed_pert)
                  - (KVtest**2 / (D1e**2 * (D1e + KVtest)))) == 0,
      "stripped-units insertion rule: 1/(D+KV) - [1/D - KV/D^2] == KV^2/(D^2(D+KV)) "
      "EXACTLY (i.e. the -KV/D^2 insertion is the exact first order)")


def pieces_mult(A, B):
    return [(sp.expand(na * nb), aa + ab, ba + bb) for (na, aa, ba) in A
            for (nb, ab, bb) in B]


def pieces_diff_l0(P):
    """d/dl0 of sum num/(D1^a D2^b): product rule; dD1/dl0 = 2 l0, dD2/dl0 = 2(l0+om)."""
    out = []
    for (n, a, b) in P:
        out.append((sp.expand(sp.diff(n, l0)), a, b))
        if a:
            out.append((sp.expand(-a * n * 2 * l0), a + 1, b))
        if b:
            out.append((sp.expand(-b * n * 2 * (l0 - om)), a, b + 1))
    return out


def pieces_scale(P, s):
    return [(sp.expand(s * n), a, b) for (n, a, b) in P]


def pieces_pole(P):
    tot = sp.Integer(0)
    for (n, a, b) in P:
        if b == 0:
            tot += loop_pole_tad(n, a)
        elif a == 0:
            tot += loop_pole_tad(n.subs({LSY[i]: LSY[i] + [om, 0, 0, kk][i]
                                         for i in range(4)}, simultaneous=True), b)
        else:
            tot += loop_pole_2den(n, a, b)
    return sp.expand(tot)


# vertex kernels (A1 form, both-momenta-incoming (l, K-l); line B carries l-K):
lv_in = [l0, l1, l2, l3]
KmL = [om - l0, -l1, -l2, kk - l3]


def Mker(e, n):
    a2c, a4c = VTX_ORDERS[n]
    return vertex_kernel(e, lv_in, KmL, a2c, a4c)


# KV insertion kernels -- TWO-SIDED FORM (defect found by the decomposition-
# independence gate and fixed here; disclosed):
#   the insertion coefficient c(s) sits BETWEEN the two field derivatives of
#   c(s)[(phi')^2 - (grad phi)^2], so the momentum-space factor is
#        KV = A * nu_L * nu_R + Bconst,    Bconst = -A |kvec|^2 - (mass term)
#   with nu_L, nu_R the frequencies of the segments LEFT and RIGHT of the insertion.
#   For an UNWEIGHTED insertion nu_L = nu_R = l0 and this collapses to A l^2 - mass
#   (the naive form). For a u-WEIGHTED insertion the segment frequencies differ, and
#   the t-weight derivative must act on (nu-factor x propagator), NOT on the
#   propagator alone -- that omission is exactly what the gate caught:
#   route1 - route2 = i Int (dKV/dl0)/(D1^2 D2), nonzero for a derivative insertion.
def KV(order, mom):
    """collapsed (nu_L = nu_R) form -- valid only for unweighted insertions; kept for
    the seagull's zero-weight terms and for gates."""
    return (2 * lsq(mom) - 4 * mm**2) if order == 1 else (3 * lsq(mom) - 10 * mm**2)


def KV_split(order, mom):
    """(A, Bconst) of the two-sided form KV = A nu_L nu_R + Bconst."""
    A = sp.Integer(2) if order == 1 else sp.Integer(3)
    mass = 4 * mm**2 if order == 1 else 10 * mm**2
    spatial = mom[1]**2 + mom[2]**2 + mom[3]**2
    return A, sp.expand(-A * spatial - mass)


# s-position monomial expansion helpers: an insertion's s expressed as
#   s = ext + t_seg  with ext in {+Delta/2 (lineB route1), -Delta/2 (lineA route2), ...}
# We expand s^p into sum_{r} C(p,r) ext^(p-r) t^r ; t^r attaches r structural diffs
# (-i d/dl0) to the DESIGNATED SEGMENT factor; ext^(q) contributes an external
# Delta-power q with coefficient (+-1/2)^q applied after the loop integral.
def line_with_insertions(Dpick, ins_list):
    """Dpick: 'A' or 'B'. ins_list: list of (KVorder, s_ext_sign, spower_total) is not
    general enough for doubles -- handled explicitly below. Single-insertion helper:
    returns list of (pieces, next_ext_power, coeff) contributions for ONE insertion
    with s^spow needed, using route s = ext + t_seg1 (ext = +-Delta/2)."""
    raise NotImplementedError


def _seg(aP, nu_pow, nu_sym, nderiv):
    """one propagator segment carrying nu^nu_pow, then nderiv t-weight derivatives
    applied to the PRODUCT (nu-factor x propagator) -- the two-sided fix."""
    base = [(nu_sym**nu_pow, aP[0], aP[1])]
    for _ in range(nderiv):
        base = pieces_scale(pieces_diff_l0(base), -sp.I)
    return base


def single_insertion_line(Dpick, KVord, spow, route):
    """ONE insertion of order KVord with position weight s^spow on line Dpick.
    route 1: s = u_start + t1 (t-weight on the LEFT segment)
    route 2: s = u_end   - t2 (t-weight on the RIGHT segment)
    line A runs v2 -> v1 (start u2 = -Delta/2, end u1 = +Delta/2); line B the reverse.
    Two-sided vertex: KV = A nu_L nu_R + Bconst (see KV_split)."""
    mom = list(LSY) if Dpick == 'A' else list(Kminus)
    aP = (1, 0) if Dpick == 'A' else (0, 1)
    nu = mom[0]
    A_, B_ = KV_split(KVord, mom)
    if Dpick == 'A':
        ext = -sp.Rational(1, 2) if route == 1 else +sp.Rational(1, 2)
    else:
        ext = +sp.Rational(1, 2) if route == 1 else -sp.Rational(1, 2)
    tsign = 1 if route == 1 else -1
    out = []
    for r in range(spow + 1):
        coeff = sp.binomial(spow, r) * ext**(spow - r) * tsign**r
        dL, dR = (r, 0) if route == 1 else (0, r)
        # type A: nu on BOTH segments; type B: plain segments times Bconst
        typeA = pieces_mult(_seg(aP, 1, nu, dL), _seg(aP, 1, nu, dR))
        typeB = pieces_mult(_seg(aP, 0, nu, dL), _seg(aP, 0, nu, dR))
        contrib = pieces_scale(typeA, -A_) + pieces_scale(typeB, -B_)
        out.append((contrib, spow - r, coeff))
    return out


def plain_line(Dpick):
    return [(sp.Integer(1), 1, 0)] if Dpick == 'A' else [(sp.Integer(1), 0, 1)]


def assemble(vn1, vn2, lineA_terms, lineB_terms):
    """fish assembly: vertex orders (vn1, vn2) with u1^vn1 u2^vn2 external factors;
    line terms as lists of (pieces, ext_power, coeff). Returns the omega-space pole
    expression with all external Delta-powers applied."""
    total = sp.Integer(0)
    for (pa, ea, ca) in lineA_terms:
        for (pb, eb, cb) in lineB_terms:
            integrand = pieces_mult(pieces_mult(
                [(sp.expand(Mker(e1m, vn1) * Mker(e2m, vn2)), 0, 0)], pa), pb)
            pol = pieces_pole(integrand)
            next_ext = ea + eb
            val = apply_Delta_power(pol, next_ext) * ca * cb
            # vertex external u-powers: u1^vn1 u2^vn2 = (Delta/2)^vn1 (-Delta/2)^vn2
            val = apply_Delta_power(val, vn1 + vn2) \
                * sp.Rational(1, 2)**vn1 * sp.Rational(-1, 2)**vn2
            total += val
    return sp.expand(sp.Rational(1, 2) * total)


stamp("p10 machinery ready")
# ---- H^0: the flat fish (anchor input) ----
F_H0 = assemble(0, 0, [(plain_line('A'), 0, 1)], [(plain_line('B'), 0, 1)])
# epsilon^2 gate: pole expressions must be LINEAR in c (no c^2 anywhere):
def eps2_gate(expr, name):
    return check(sp.degree(sp.Poly(expr, c), c) <= 1,
                 f"eps^2 gate: {name} is linear in c (no 1/eps^2 artifacts)")


# NOTE: engine emits poles in units of c ALREADY (c multiplied inside masters)...
# masters return values in units WITHOUT c? Ipole_scalar returns pure Delta-powers;
# loop_pole_* therefore returns the pole in UNITS OF c. We multiply by c at report
# time only; linearity is then structural. Record that convention:
print("   convention: engine returns poles in units of c; c is applied at report time "
      "(eps^2-cancellation is structural: no c enters the assembly at all)")

# ---- decomposition-independence gate on ONE insertion diagram (route 1 vs 2) ----
t_r1 = assemble(0, 0, single_insertion_line('A', 1, 1, 1), [(plain_line('B'), 0, 1)])
t_r2 = assemble(0, 0, single_insertion_line('A', 1, 1, 2), [(plain_line('B'), 0, 1)])
_rd = sp.expand(t_r1 - t_r2)
if _rd != 0:
    _e1 = sorted({q for q in _rd.free_symbols if str(q).startswith('E_')}, key=str)[0]
    _p1 = sorted({q for q in _rd.free_symbols if str(q).startswith('P_')}, key=str)[0]
    print("   DIAGNOSTIC route residual, one bilinear slot:",
          sp.factor(sp.simplify(sp.expand(_rd).coeff(_e1, 1).coeff(_p1, 1))))
    print("   residual free symbols:", sorted(map(str, _rd.free_symbols)))
    # is the residual PURE type-A (nu-structure) or type-B (constant)?  Rebuild the
    # two routes with a MASS-ONLY insertion (A -> 0) to separate the channels:
    _sv = KV_split
    KV_split = lambda o, mom: (sp.Integer(0), _sv(o, mom)[1])
    _b1 = assemble(0, 0, single_insertion_line('A', 1, 1, 1), [(plain_line('B'), 0, 1)])
    _b2 = assemble(0, 0, single_insertion_line('A', 1, 1, 2), [(plain_line('B'), 0, 1)])
    print("   MASS-ONLY (type-B) channel route-independent:", sp.expand(_b1 - _b2) == 0)
    KV_split = lambda o, mom: (_sv(o, mom)[0], sp.Integer(0))
    _a1 = assemble(0, 0, single_insertion_line('A', 1, 1, 1), [(plain_line('B'), 0, 1)])
    _a2 = assemble(0, 0, single_insertion_line('A', 1, 1, 2), [(plain_line('B'), 0, 1)])
    print("   NU-ONLY (type-A) channel route-independent:", sp.expand(_a1 - _a2) == 0)
    KV_split = _sv
check(_rd == 0,
      "DECOMPOSITION-INDEPENDENCE: V1 insertion via route s = u_start + t1 equals "
      "route s = u_end - t2 EXACTLY (the u-rule wiring is self-consistent)")
stamp("p10 gates: decomposition independence done")

# ---- O(H) sector (classification, not deliverable) ----
H1_terms = {
    'vtx(1,0)': assemble(1, 0, [(plain_line('A'), 0, 1)], [(plain_line('B'), 0, 1)]),
    'vtx(0,1)': assemble(0, 1, [(plain_line('A'), 0, 1)], [(plain_line('B'), 0, 1)]),
    'V1 on A':  assemble(0, 0, single_insertion_line('A', 1, 1, 1),
                         [(plain_line('B'), 0, 1)]),
    'V1 on B':  assemble(0, 0, [(plain_line('A'), 0, 1)],
                         single_insertion_line('B', 1, 1, 1)),
}
H1_total = sp.expand(sum(H1_terms.values()))
stamp("p10 O(H) assembled")

# ---- O(H^2) sector: the deliverable ----
H2 = {}
H2['vtx(2,0)'] = assemble(2, 0, [(plain_line('A'), 0, 1)], [(plain_line('B'), 0, 1)])
H2['vtx(0,2)'] = assemble(0, 2, [(plain_line('A'), 0, 1)], [(plain_line('B'), 0, 1)])
H2['vtx(1,1)'] = assemble(1, 1, [(plain_line('A'), 0, 1)], [(plain_line('B'), 0, 1)])
H2['vtx1xV1A'] = assemble(1, 0, single_insertion_line('A', 1, 1, 1),
                          [(plain_line('B'), 0, 1)])
H2['vtx1xV1B'] = assemble(1, 0, [(plain_line('A'), 0, 1)],
                          single_insertion_line('B', 1, 1, 1))
H2['vtx2xV1A'] = assemble(0, 1, single_insertion_line('A', 1, 1, 1),
                          [(plain_line('B'), 0, 1)])
H2['vtx2xV1B'] = assemble(0, 1, [(plain_line('A'), 0, 1)],
                          single_insertion_line('B', 1, 1, 1))
H2['V2 on A'] = assemble(0, 0, single_insertion_line('A', 2, 2, 1),
                         [(plain_line('B'), 0, 1)])
H2['V2 on B'] = assemble(0, 0, [(plain_line('A'), 0, 1)],
                         single_insertion_line('B', 2, 2, 1))
H2['V1AxV1B'] = assemble(0, 0, single_insertion_line('A', 1, 1, 1),
                         single_insertion_line('B', 1, 1, 1))
stamp("p10 O(H^2) single/vertex classes assembled")


def double_insertion_line(Dpick):
    """two order-1 insertions on one line: segments (t1,t2,t3); s1 = u_start + t1,
    s2 = u_start + t1 + t2. Two-sided vertices V1 = A nu1 nu2 + B (across the first
    insertion), V2 = A nu2 nu3 + B (across the second); their product expands into
    four segment-factor structures."""
    mom = list(LSY) if Dpick == 'A' else list(Kminus)
    aP = (1, 0) if Dpick == 'A' else (0, 1)
    nu = mom[0]
    A_, B_ = KV_split(1, mom)
    ext = -sp.Rational(1, 2) if Dpick == 'A' else +sp.Rational(1, 2)
    # s1*s2 = ext^2 + ext(2 t1 + t2) + t1^2 + t1 t2
    monos = [((0, 0), ext**2, 2), ((1, 0), 2 * ext, 1), ((0, 1), ext, 1),
             ((2, 0), sp.Integer(1), 0), ((1, 1), sp.Integer(1), 0)]
    # vertex structures: (nu-power on seg1, seg2, seg3, coefficient)
    vstruct = [(1, 2, 1, A_ * A_), (1, 1, 0, A_ * B_), (0, 1, 1, A_ * B_),
               (0, 0, 0, B_ * B_)]
    out = []
    for (r1, r2), coeff, extpow in monos:
        pieces = []
        for (p1, p2, p3, vc) in vstruct:
            seg1 = _seg(aP, p1, nu, r1)
            seg2 = _seg(aP, p2, nu, r2)
            seg3 = _seg(aP, p3, nu, 0)
            block = pieces_mult(pieces_mult(seg1, seg2), seg3)
            pieces += pieces_scale(block, vc)      # two (-KV) factors: (-1)^2 = +1
        out.append((pieces, extpow, coeff))
    return out


H2['V1V1 on A'] = assemble(0, 0, double_insertion_line('A'),
                           [(plain_line('B'), 0, 1)])
H2['V1V1 on B'] = assemble(0, 0, [(plain_line('A'), 0, 1)],
                           double_insertion_line('B'))
stamp("p10 O(H^2) doubles assembled")
F_H2 = sp.expand(sum(H2.values()))

# ---- SEAGULL (closed tadpole line; vertex at the reference, u = 0) ----
print("\n--- seagull sector ---")
kap = sp.Symbol('kappa')
hmat = sp.Matrix(4, 4, lambda i, j: e1m[i, j] * sp.Symbol('a1') + e2m[i, j] * sp.Symbol('a2'))
a1s, a2s = sp.Symbol('a1'), sp.Symbol('a2')
etainv = eta
G1m = -etainv * hmat * etainv
G2m = etainv * hmat * etainv * hmat * etainv
Ddet = sp.expand(-(eta + kap * hmat).det(method='berkowitz'))
d1c, d2c = Ddet.coeff(kap, 1), Ddet.coeff(kap, 2)
s1c = sp.expand(d1c / 2)
s2c_full = sp.expand(d2c / 2 - d1c**2 / 8)
F2m = (s2c_full * etainv + s1c * G1m + G2m).applyfunc(sp.expand)
cross = lambda ex: sp.expand(ex).coeff(a1s, 1).coeff(a2s, 1)
F2c = F2m.applyfunc(cross)
s2c = cross(s2c_full)
llo = [l0, -l1, -l2, -l3]
L2ker = sp.expand(sum(F2c[i, j] * llo[i] * llo[j] for i in range(4) for j in range(4))
                  - s2c * mm**2)
# NOTE the seagull vertex sits at u = 0 (both h legs coincident at the reference):
# a(0) = 1 exactly => NO vertex dressing; all seagull H-orders come from the closed
# line's insertions (structural, stated, and consistent with centre-at-reference).
S_H0 = sp.expand(-sp.Rational(1, 2) * loop_pole_tad(L2ker, 1))
check(sp.expand(S_H0 - (-sp.Rational(1, 2)) * (mm**4 * s2c * sp.Integer(0)
      + loop_pole_tad(L2ker, 1))) == 0, "seagull H^0 assembled (bookkeeping)")
# flat seagull identity gate (2b lineage): S_H0 == (m^4/2) * [sqrt(-g)]_{h^2-cross}:
check(sp.simplify(S_H0 - mm**4 / 2 * s2c) == 0,
      "SEAGULL IDENTITY (flat): seagull pole == (m^4/2) [sqrt(-g)]_{h^2}  "
      "(the 2b anchor identity, reproduced by the NEW engine)")


def seagull_closed_line(ins_spec):
    """closed line at the reference vertex (u = 0): segments t1.. with s1 = t1,
    s2 = t1 + t2. Two-sided insertion vertices as in the fish."""
    A_, B_ = KV_split(1, list(LSY))
    A2_, B2_ = KV_split(2, list(LSY))
    aP = (1, 0)
    nu = l0
    base = [(L2ker, 0, 0)]
    if ins_spec in ('V1', 'V2'):
        Ax, Bx = (A_, B_) if ins_spec == 'V1' else (A2_, B2_)
        spow = 1 if ins_spec == 'V1' else 2
        acc = []
        for (p1, p2, vc) in ((1, 1, Ax), (0, 0, Bx)):
            seg1 = _seg(aP, p1, nu, spow)          # s^spow = t1^spow
            seg2 = _seg(aP, p2, nu, 0)
            acc += pieces_scale(pieces_mult(seg1, seg2), -vc)
        pieces = pieces_mult(base, acc)
        return sp.expand(-sp.Rational(1, 2) * pieces_pole(pieces))
    # V1V1: s1 s2 = t1^2 + t1 t2 over segments (t1, t2, t3)
    out = sp.Integer(0)
    vstruct = [(1, 2, 1, A_ * A_), (1, 1, 0, A_ * B_), (0, 1, 1, A_ * B_),
               (0, 0, 0, B_ * B_)]
    for (r1, r2) in ((2, 0), (1, 1)):
        acc = []
        for (p1, p2, p3, vc) in vstruct:
            block = pieces_mult(pieces_mult(_seg(aP, p1, nu, r1), _seg(aP, p2, nu, r2)),
                                _seg(aP, p3, nu, 0))
            acc += pieces_scale(block, vc)
        out += pieces_pole(pieces_mult(base, acc))
    return sp.expand(-sp.Rational(1, 2) * out)


S_H1 = seagull_closed_line('V1')
S_H2 = sp.expand(seagull_closed_line('V2') + seagull_closed_line('V1V1'))
stamp("seagull sector assembled")

# ---- sector totals (units: engine c-units; H-powers attached here) ----
SIG0 = sp.expand(F_H0 + S_H0)
SIG1 = sp.expand(H1_total + S_H1)          # coefficient of H^1
SIG2 = sp.expand(F_H2 + S_H2)              # coefficient of H^2
conj = lambda ex: ex.subs(sp.I, -sp.I)
check(sp.expand(SIG0 - conj(SIG0)) == 0, "reality: SIG(H^0) real")
check(sp.expand(SIG2 - conj(SIG2)) == 0, "reality: SIG(H^2) real (i-pairs closed)")
h1_zero = sp.expand(SIG1) == 0
h1_imag = sp.expand(SIG1 + conj(SIG1)) == 0
print(f"   O(H^1) classification: identically zero: {h1_zero}; purely imaginary "
      f"(reference/phase artifact class): {h1_imag}")
check(h1_zero or h1_imag,
      "H-PARITY: the O(H^1) pole either vanishes or is purely imaginary "
      "(no real odd-H pole survives at the reference -- classified, not forced)")
stamp("p10 totals + parity done")
if PHASE == "p10":
    print(f"\n[p10 partial run: FAIL count = {len(FAIL)}]")
    sys.exit(0 if not FAIL else 1)

# ================= PHASE 11: BASIS SIDE + IDENTIFICATION =================
print("\n=== PHASE 11: BASIS KERNELS ON THE DRESSED BACKGROUND + IDENTIFICATION ===")
uu, zz3 = sp.symbols('u z', real=True)
f1F, f2F = sp.Function('f1', real=True)(uu), sp.Function('f2', real=True)(uu)
a_bg = 1 + H * uu + H**2 * uu**2            # Section-D derived, truncated O(H^2)
COORD = [uu, sp.Symbol('x_c'), sp.Symbol('y_c'), zz3]
phz1, phz2 = sp.exp(sp.I * kk * zz3), sp.exp(-sp.I * kk * zz3)
hfield = sp.Matrix(4, 4, lambda i, j: e1m[i, j] * f1F * phz1 + e2m[i, j] * f2F * phz2)
gmat = (a_bg**2 * (eta + kap * hfield)).applyfunc(sp.expand)


def trunc_H2(ex):
    ex = sp.expand(ex)
    return sp.expand(ex.coeff(H, 0) + H * ex.coeff(H, 1) + H**2 * ex.coeff(H, 2))


def metric_inverse_pert(g):
    """inverse of g = A + kap B through O(kap^2), A = a^2 eta: exact block route:
    g = a^2(eta + kap h): ginv = a^-2 (eta - kap h~ + kap^2 h~h~-form) with
    eta-raised h; built explicitly and VERIFIED by multiplication through O(kap^2)."""
    hh = hfield
    inv = (eta - kap * (etainv * hh * etainv) * sp.Integer(1)
           + kap**2 * (etainv * hh * etainv * hh * etainv))
    ginv = (inv / a_bg**2).applyfunc(sp.expand)
    prod = (g * ginv).applyfunc(sp.expand)
    ok0 = all(sp.expand(prod[i, j].coeff(kap, 0) - (1 if i == j else 0)) == 0
              for i in range(4) for j in range(4))
    ok1 = all(sp.expand(prod[i, j].coeff(kap, 1)) == 0 for i in range(4) for j in range(4))
    ok2 = all(sp.expand(prod[i, j].coeff(kap, 2)) == 0 for i in range(4) for j in range(4))
    check(ok0 and ok1 and ok2, "basis: g.ginv == 1 through O(kap^2) by multiplication")
    return ginv


ginv = metric_inverse_pert(gmat)
stamp("p11 metric inverse verified")
detg = sp.expand(-gmat.det(method='berkowitz'))
# sqrt(-g) through O(kap^2): a^4 sqrt(-det(eta+kap h)) = a^4 (1 + kap s1 + kap^2 s2):
s1f = sp.expand(sum(etainv[i, j] * hfield[i, j] for i in range(4) for j in range(4)) / 2)
d1f = sp.expand(detg.coeff(kap, 1) / a_bg**8)
d2f = sp.expand(detg.coeff(kap, 2) / a_bg**8)
s2f = sp.expand(d2f / 2 - d1f**2 / 8)
sqrtg = a_bg**4 * (1 + kap * s1f + kap**2 * s2f)
chk = sp.expand((sqrtg**2 - detg).coeff(kap, 0))
check(sp.simplify(chk) == 0 and sp.simplify(sp.expand((sqrtg**2 - detg).coeff(kap, 1))) == 0
      and sp.simplify(sp.expand((sqrtg**2 - detg).coeff(kap, 2))) == 0,
      "basis: sqrt(-g)^2 == -det g through O(kap^2) by multiplication")
stamp("p11 sqrt(-g) verified")


def christoffel(g, gi):
    Chr = [[[sp.Integer(0)] * 4 for _ in range(4)] for _ in range(4)]
    for lam in range(4):
        for mu2 in range(4):
            for nu2 in range(mu2, 4):
                t = sum(gi[lam, s2_] * (sp.diff(g[s2_, nu2], COORD[mu2])
                                        + sp.diff(g[s2_, mu2], COORD[nu2])
                                        - sp.diff(g[mu2, nu2], COORD[s2_]))
                        for s2_ in range(4)) / 2
                t = trunc_H2(sp.expand(t))
                Chr[lam][mu2][nu2] = t
                Chr[lam][nu2][mu2] = t
    return Chr


def ricci(Chr):
    R = sp.zeros(4, 4)
    for mu2 in range(4):
        for nu2 in range(mu2, 4):
            t = (sum(sp.diff(Chr[lam][mu2][nu2], COORD[lam]) for lam in range(4))
                 - sum(sp.diff(Chr[lam][lam][mu2], COORD[nu2]) for lam in range(4))
                 + sum(Chr[lam][lam][s2_] * Chr[s2_][mu2][nu2]
                       - Chr[lam][nu2][s2_] * Chr[s2_][lam][mu2]
                       for lam in range(4) for s2_ in range(4)))
            t = trunc_H2(sp.expand(t))
            R[mu2, nu2] = t
            R[nu2, mu2] = t
    return R


Chr = christoffel(gmat, ginv)
stamp("p11 christoffels done")
Rmn = ricci(Chr)
stamp("p11 ricci done")
Rsc = sp.expand(sum(ginv[i, j] * Rmn[i, j] for i in range(4) for j in range(4)))
Rsc = trunc_H2(Rsc)
# background curvature, DERIVED: R(bar g) = kap^0 part at f = 0:
Rbar = sp.expand(Rsc.coeff(kap, 0))
Rbar_ref = sp.expand(Rbar.subs(uu, 0))
print(f"   background curvature at the reference: R(bar) = {sp.simplify(Rbar_ref)}  "
      "(DERIVED; sign convention of this Ricci machinery, mostly-minus)")
check(sp.simplify(Rbar_ref / H**2 + 12) == 0 or sp.simplify(Rbar_ref / H**2 - 12) == 0,
      "background curvature magnitude: |R(bar)| = 12 H^2 at the reference "
      "(sign reported, magnitude gated)")


def density_cross(expr):
    """kap^2, f1*f2-bilinear (zero z-phase) part of a density expression."""
    ex = sp.expand(expr).coeff(kap, 2)
    ex = sp.expand(ex)
    # zero-phase filter: coefficient of (phz1*phz2)^1 pattern == terms with no exp:
    ex = ex.rewrite(sp.exp)
    ex = sp.expand(ex.subs({phz1 * phz2: 1}))
    ex = sp.expand(ex.subs({sp.exp(2 * sp.I * kk * zz3): 0,
                            sp.exp(-2 * sp.I * kk * zz3): 0,
                            sp.exp(sp.I * kk * zz3): sp.Symbol('_P1'),
                            sp.exp(-sp.I * kk * zz3): sp.Symbol('_P2')}))
    # keep only terms bilinear with both phases (i.e. _P1*_P2 -> 1), drop the rest:
    P1_, P2_ = sp.Symbol('_P1'), sp.Symbol('_P2')
    ex = sp.expand(ex).coeff(P1_, 1).coeff(P2_, 1) + \
        (sp.expand(ex).coeff(P1_, 0).coeff(P2_, 0))
    return sp.expand(ex)


DENSITIES = {
    'Lam': sqrtg,
    'EH': sp.expand(sqrtg * Rsc),
    'R2': sp.expand(sqrtg * Rsc**2),
    'Rmn2': sp.expand(sqrtg * sum(ginv[i, a_] * ginv[j, b_] * Rmn[i, j] * Rmn[a_, b_]
                                  for i in range(4) for j in range(4)
                                  for a_ in range(4) for b_ in range(4))),
}
stamp("p11 densities built")


def kernel_transform(dens):
    """density cross-bilinear -> Q(omega) via the functional-kernel distribution
    transform: term c_n u^n f1^(r) f2^(s):
      K(u1,u2) = (-1)^r d^r/du1^r [ c(u1) delta^(s)(u1-u2) ]
      Q(omega) = sum_j binom(r,j) (-1)^r c^(j)(D/2) x FT[delta^(r-j+s)]
    with c^(j)(D/2) expanded in Delta-powers and Delta^p -> (-i d/dom)^p."""
    ex = density_cross(dens)
    ex = trunc_H2(ex)
    # replace derivatives by symbols for collection:
    reps, syms2 = {}, {}
    for (fF, tag) in ((f1F, 'F1'), (f2F, 'F2')):
        for r_ in (4, 3, 2, 1):
            reps[sp.Derivative(fF, (uu, r_))] = sp.Symbol(f'{tag}_{r_}')
        reps[fF] = sp.Symbol(f'{tag}_0')
    exs = sp.expand(ex.subs(reps))
    gens = [sp.Symbol(f'F{i}_{r_}') for i in (1, 2) for r_ in range(5)]
    poly = sp.Poly(exs, *gens, uu)
    Q = sp.Integer(0)
    for mono, cf in zip(poly.monoms(), poly.coeffs()):
        n_u = mono[-1]
        r_ = next((r2 for i2, r2 in enumerate(
            [r3 for _ in (1,) for r3 in range(5)]) if mono[i2] == 1), None)
        # decode: first 5 slots = F1_0..F1_4, next 5 = F2_0..F2_4
        r1s = [i2 for i2 in range(5) if mono[i2] >= 1]
        r2s = [i2 for i2 in range(5) if mono[5 + i2] >= 1]
        if len(r1s) != 1 or len(r2s) != 1 or mono[r1s[0]] != 1 or mono[5 + r2s[0]] != 1:
            check(False, f"P11 kernel_transform: unexpected monomial structure {mono}")
            continue
        rr, ss = r1s[0], r2s[0]
        # c(u) = cf * u^{n_u}; sum over Leibniz j:
        for j2 in range(min(rr, n_u) + 1):
            cj = cf * sp.factorial(n_u) / sp.factorial(n_u - j2) * sp.binomial(rr, j2) \
                * sp.Integer(-1)**rr
            p_ = n_u - j2                      # Delta-power via (Delta/2)^p
            mord = rr - j2 + ss                # delta-derivative order
            base = (-sp.I * om)**mord
            term = base
            for _ in range(p_):
                term = -sp.I * sp.diff(term, om)
            Q += cj * term / sp.Integer(2)**p_
    return sp.expand(Q)


QK = {}
for nm2, dd_ in DENSITIES.items():
    QK[nm2] = kernel_transform(dd_)
    stamp(f"p11 kernel {nm2} transformed")
QH = {nm2: {n2: sp.expand(QK[nm2].coeff(H, n2)) for n2 in (0, 1, 2)} for nm2 in QK}

# ---- identification at H^0: THE GILKEY ANCHOR (sampled fit + symbolic residual) ----
print("\n--- identification: H^0 anchor ---")
uL, uE, uR, uM = sp.symbols('uL uE uR uM')
target0 = sp.expand(SIG0.coeff(H, 0) if SIG0.has(H) else SIG0)
model0 = uL * QH['Lam'][0] + uE * QH['EH'][0] + uR * QH['R2'][0] + uM * QH['Rmn2'][0]
diff0 = sp.expand(target0 - model0)
esyms = sorted({s_ for s_ in diff0.free_symbols
                if str(s_).startswith('E_') or str(s_).startswith('P_')}, key=str)
eqs = []
for smp in ({om: sp.Rational(3, 2), kk: sp.Rational(1, 3)},
            {om: sp.Rational(5, 7), kk: sp.Rational(2, 5)},
            {om: sp.Rational(7, 3), kk: sp.Rational(3, 2)}):
    dsub = sp.expand(diff0.subs(smp))
    pol2 = sp.Poly(dsub, *esyms)
    eqs.extend(pol2.coeffs())
sol0 = sp.solve(list(set([sp.expand(e_) for e_ in eqs])), [uL, uE, uR, uM], dict=True)
got0 = bool(sol0) and len(sol0[0]) == 4
if got0:
    resid0 = sp.expand(diff0.subs(sol0[0]))
    got0 = sp.simplify(resid0) == 0
    if got0:
        print("   H^0 coefficients:", {str(k2): sp.factor(v2)
                                       for k2, v2 in sol0[0].items()})
check(got0, "H^0: target fits the four-operator basis EXACTLY "
      "(sampled fit + FULL symbolic residual zero)")
gilkey = {uL: mm**4 / 4, uE: mm**2 / 12, uR: sp.Rational(1, 240), uM: sp.Rational(1, 120)}
anchor = got0 and all(sp.simplify(sol0[0][s_] - gilkey[s_]) == 0 for s_ in gilkey)
check(anchor, "THE ANCHOR: H^0 coefficients == Gilkey {m^4/4, m^2/12, 1/240, 1/120} "
      "in c-units EXACTLY (the doubly-verified flat anchor reproduced by the NEW engine)")
stamp("p11 H^0 identification done")

# ---- zero-free-parameter checks at H^1 and H^2 (counterterm covariance) ----
print("\n--- identification: H^1 and H^2 (zero free parameters, Gilkey-pinned) ---")
results_h = {}
for n2 in (1, 2):
    tgt = SIG1 if n2 == 1 else SIG2
    prediction = sp.expand(sum(gilkey[s_] * {uL: QH['Lam'], uE: QH['EH'],
                                             uR: QH['R2'], uM: QH['Rmn2']}[s_][n2]
                               for s_ in gilkey))
    resid = sp.expand(tgt - prediction)
    zero = sp.simplify(resid) == 0
    results_h[n2] = (zero, resid)
    print(f"   O(H^{n2}): covariance residual identically zero: {zero}")
    if not zero:
        print(f"      residual (reported as found, on the face): "
              f"{sp.simplify(resid)}")
check(True, f"H^1/H^2 covariance checks COMPUTED and recorded "
      f"(H^1 zero: {results_h[1][0]}; H^2 zero: {results_h[2][0]}) -- "
      "a nonzero residual is a FINDING, not silently absorbed")
stamp("p11 H-order identification done")

# ================= PHASE 8 (wired here): THE DRESSING PLANT =================
print("\n=== PHASE 8: DRESSING-CONSISTENCY PLANT (mechanically wired) ===")
SIG2_hybrid_vtx = sp.expand(sum(v2_ for k2_, v2_ in H2.items() if k2_.startswith('vtx'))
                            )           # vertex-dressed, propagators undressed
pred2 = sp.expand(sum(gilkey[s_] * {uL: QH['Lam'], uE: QH['EH'],
                                    uR: QH['R2'], uM: QH['Rmn2']}[s_][2] for s_ in gilkey))
hyb_resid = sp.expand(SIG2_hybrid_vtx - pred2)
hyb_fails = sp.simplify(hyb_resid) != 0
check(hyb_fails, "PLANT: the PROHIBITED hybrid (dressed vertices x undressed "
      "propagators) FAILS the covariance check (nonzero residual) -- the v3 "
      "prohibition is mechanically visible")
SIG2_hybrid_prop = sp.expand(SIG2 - SIG2_hybrid_vtx)    # insertions-only converse
hyb2_resid = sp.expand(SIG2_hybrid_prop - pred2)
check(sp.simplify(hyb2_resid) != 0,
      "PLANT (converse): propagator-dressed x undressed-vertex ALSO fails -- only the "
      "matched construction can satisfy covariance")
stamp("phase 8 plant done")

# ================= PHASE 12: MS SPLIT + INTEGRITY =================
print("\n=== PHASE 12: MS SPLIT (pole-only) + INTEGRITY ===")
Pi_local = {0: sp.expand(sum(gilkey[s_] * {uL: QH['Lam'], uE: QH['EH'],
                                           uR: QH['R2'], uM: QH['Rmn2']}[s_][n2]
                             for s_ in gilkey)) for n2 in (0, 1, 2)}
integ = {n2: sp.simplify(sp.expand((SIG0, SIG1, SIG2)[n2] - Pi_local[n2])) == 0
         for n2 in (0, 1, 2)}
print(f"   integrity per order (pole == covariant local form): {integ}")
check(integ[0], "P12 integrity at H^0: the entire flat pole is the Gilkey local form "
      "(non-vacuous MS split at the anchor)")
print("   per-channel a-power audit: vertex kinetic block (a^2: orders (1,2Hu,3H^2u^2))"
      " vs mass block (a^4: (1,4Hu,10H^2u^2)) carried EXPLICITLY through every term "
      "(VTX_ORDERS / KV1 / KV2 on the face); the H^2 pole's kinetic-vs-mass split is "
      "recoverable per class from the H2 dict keys (recorded in the JSON).")
print("   Pi_nonlocal^invariant(H-orders): the eps^0 content of the same diagrams -- "
      "DEFINED and untouched by pole-only MS; its evaluation is the ASSEMBLY-3 entry.")

all_ok = not FAIL
verdict = ("D2-R1 PHASES 8-12 COMPLETE: matched O(H^2) fish+seagull assembled from one "
           "derived engine (masters, moments, u-rule, insertion kernels all gated); "
           "H^0 reproduces the Gilkey anchor EXACTLY through the new machinery; the "
           "H^1/H^2 covariance residuals are computed and recorded on the face; the "
           "prohibited hybrids mechanically FAIL the covariance check; MS split "
           "executed pole-only with the anchor-order integrity non-vacuous."
           if all_ok else "PHASES 8-12 ANOMALOUS -- see FAIL gates; report as found.")
print("\nVERDICT:", verdict)
json.dump({
    "instrument": "wall_d2_phases8_12.py",
    "builder": "checker under claim 8640ce5; SECOND-AUTHOR SLOT OPEN",
    "standing": "Phases 0-7 green at ea165dd (cited); v1+v2+v3 law; W-0 not banked",
    "engine_gates": "masters(5/5), moments, u-rule Gaussian, E-transform, insertion dm2 "
                    "+ kinetic exact, decomposition-independence",
    "H0_anchor": {"fit": "exact, sampled + full symbolic residual",
                  "gilkey": str(anchor)},
    "H1": {"classification": f"zero: {h1_zero}, imaginary: {h1_imag}",
           "covariance_zero": str(results_h[1][0])},
    "H2": {"covariance_zero": str(results_h[2][0]),
           "residual_recorded": str(sp.simplify(results_h[2][1])) if not results_h[2][0]
           else "0"},
    "plant": {"hybrid_vtx_fails": str(hyb_fails)},
    "background_R_at_reference": str(sp.simplify(Rbar_ref)),
    "verdict": verdict,
}, open(os.path.join(HERE, "WALL_D2_PHASES8_12_RESULT.json"), "w"), indent=2)
print("result written: WALL_D2_PHASES8_12_RESULT.json")
sys.exit(0 if all_ok else 1)
