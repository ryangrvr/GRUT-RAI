#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PHASE-11 TOY FUNCTIONAL-HESSIAN CALIBRATION -- standalone W-0 instrument.

WHY (owner stop directive, 2026-08-27): general Phase-11 reasoning is HALTED until an
exact toy pins, once and for all: (i) coefficient placement, (ii) the (u_c, Delta)
transform, (iii) the Delta^r delta^(q) reduction, (iv) FT signs.  No sqrt(-g)/R/R^2/Rmn^2
generalization before this toy is green.

THE TOY (self-contained, analytically known; the Phase-11 residual is NOT the target):
    S[h] = 1/2 * Int du C(u) (h'(u))^2 ,    C(u) = 1 + c1*u + c2*u^2 .
Exact functional Hessian, both differentiation orders:
    u2-order: K(u1,u2) = -d/du2 [ C(u2) d/du2 delta(u2-u1) ]
    u1-order: K(u1,u2) = -d/du1 [ C(u1) d/du1 delta(u1-u2) ]

REGISTERED CONVENTIONS UNDER TEST (mirrored verbatim in form from
PHYSICS_LEDGER/wall_d2_phases8_12.py: FT convention line 298, apply_Delta_power line 310,
u1_pow/u2_pow lines 318-324, E_transform line 338; reimplemented standalone -- NO import
of, and NO edit to, any existing machinery):
  (i)   FT convention  Sigma_tilde(om) = Int dDelta e^{+i om Delta} Sigma(Delta)
  (ii)  apply_Delta_power(expr, n) = (-i d/dom)^n
  (iii) E_transform: sum_p a_p Delta^p delta^(q)(Delta) -> sum_p a_p (-i d/dom)^p[(-i om)^q]
  (iv)  vertex placement u1 = +Delta/2, u2 = -Delta/2 with lever arms (+-1/2)^r (the
        r-slot convention); at general centre u = u_c +- Delta/2.

NINE-STEP PROTOCOL (all must pass):
 (1) exact K(u1,u2) from the functional definition, both orders;
 (2) verify via test functions: <hA,K,hB> == Int du C hA' hB' (exact, generic Gaussians,
     two pairs incl. shifted centres; plus sympy's own DiracDelta integration as a third
     route);
 (3) transform to (u_c, Delta) with the FULL distributional structure
     (d/du2 = 1/2 d/duc - d/dDelta, d/du1 = 1/2 d/duc + d/dDelta);
 (4) apply the registered r-slot convention ((+-1/2)^r lever arms);
 (5) expand C(u_c +- Delta/2) and reduce EVERY Delta^r delta^(q);
 (6) FT with the frozen convention (E_transform);
 (7) set u_c = 0 LAST (plus a second-centre repeat at u_c = 1/3, and the registered
     u1_pow/u2_pow rules exercised directly at u_c = 0);
 (8) independently cross-check by acting on plane waves (bilinear pairing
     h_A = e^{+i o1 u}, h_B = e^{-i o2 u}, mirroring the machinery's A/B sectors);
 (9) both constructions must agree EXACTLY.

CONTROLS (each MUST be detected as wrong):
  A   wrong sign of d/dDelta in the (u_c,Delta) chain rule;
  B   wrong lever arm (u = u_c +- Delta instead of u_c +- Delta/2);
  C   frozen-centre shortcut (Route A: only the undifferentiated-dressing slot; discards
      every derivative-of-C term) -- the suspected Phase-11 basis-side defect class;
  C'  freeze-at-centre variant (keeps a frozen C' dd' term);
  D   coefficient placement at the wrong vertex (u2-order signs with u1-slot placement);
  E   conjugate FT sign (negative control, per-term; summed-level flip is degenerate for
      this toy because the exact kernel is distributionally even in Delta -- disclosed).
FLAT CONTROL: C == 1 must reduce EXACTLY to the old r=0 structure (-dd'' -> om^2).

PRE-REGISTERED EXPECTATIONS (hand-derived via three independent routes: kernel FT,
Weyl/Moyal symbol x2, plane-wave matrix elements; the script must reproduce all):
  K_tilde(u_c,om)  = om^2 C(u_c) + (1/4) C''(u_c)                  [both placements]
  reduced kernel   = -C(u_c) dd''(Dl) + (1/4) C''(u_c) dd(Dl)
  frozen-centre F_A = om^2 C(u_c);   F_B - F_A = (1/4) C''(u_c)    (toy master identity)
  at u_c = 0       : K_tilde = om^2 + c2/2
  plane waves      : <e^{i o1 u},K,e^{-i o2 u}> = 2 pi {(S^2/4 + c2/2) dd(Q)
                     - i (c1 S^2/4) dd'(Q) - (c2 S^2/4) dd''(Q)}, S = o1+o2, Q = o1-o2.

W-0: computed and reported only.  No register edits, no edits to any existing file, no
basis change, no refit, no interpretation of the 96/300 H^2 residual.
"""
import json
import os
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()
FAIL = []
LOG = []


def check(cond, msg):
    ok = bool(cond)
    print(("  ok   " if ok else "  FAIL ") + msg)
    sys.stdout.flush()
    LOG.append({"kind": "check", "pass": ok, "msg": msg})
    if not ok:
        FAIL.append(msg)
    return ok


def note(msg):
    print("  --   " + msg)
    sys.stdout.flush()
    LOG.append({"kind": "note", "msg": msg})


def stamp(s):
    print("[%7.1fs] %s" % (time.time() - T0, s))
    sys.stdout.flush()


# ---------------- symbols and the toy action ----------------
c1, c2 = sp.symbols('c1 c2', real=True)
u1, u2, uu, uc, Dl, om = sp.symbols('u1 u2 uu uc Dl om', real=True)
qv, sv = sp.symbols('qv sv', real=True)            # Q = o1 - o2, S = o1 + o2
al, be, ga, de = sp.symbols('al be ga de', real=True)   # generic test-function parameters
eps_ = sp.Symbol('eps', positive=True)


def C(x):
    return 1 + c1 * x + c2 * x ** 2                # the dressing


def dC(x):
    return c1 + 2 * c2 * x


def d2C(x):
    return 2 * c2


# ------------- registered engines, mirrored verbatim in form -------------
def apply_Delta_power(expr, n):
    """apply the Delta^n factor to an omega-space expression: (-i d/domega)^n."""
    out = expr
    for _ in range(n):
        out = -sp.I * sp.diff(out, om)
    return sp.expand(out)


def E_transform(pcoeffs, q):
    """transform of sum_p pcoeffs[p] * Delta^p * delta^(q)(Delta):
    = sum_p pcoeffs[p] * (-i d/dom)^p [(-i om)^q]."""
    base = (-sp.I * om) ** q
    out = sp.Integer(0)
    for p_, cf in pcoeffs.items():
        term = base
        for _ in range(p_):
            term = -sp.I * sp.diff(term, om)
        out += cf * term
    return sp.expand(out)


# vertex placements u1 = +Delta/2, u2 = -Delta/2 (the r-slot lever arms), mirrored:
def u1_pow(expr, n):
    return sp.expand(apply_Delta_power(expr, n) / sp.Integer(2) ** n)


def u2_pow(expr, n):
    return sp.expand(apply_Delta_power(expr, n) * sp.Integer(-1) ** n / sp.Integer(2) ** n)


# ------------- distribution machinery: sum coeff(uc,Dl) * dd^(q)(Dl) -------------
def dnrm(d):
    out = {}
    for (cf, q) in d:
        cf = sp.expand(cf)
        if cf != 0:
            out[q] = sp.expand(out.get(q, 0) + cf)
    return [(cf, q) for q, cf in sorted(out.items()) if sp.expand(cf) != 0]


def dmul(d, p):
    return dnrm([(sp.expand(cf * p), q) for (cf, q) in d])


def dop(d, a, b):
    """apply a*d/duc + b*d/dDl to sum coeff(uc,Dl) dd^(q)(Dl), full product rule."""
    t = []
    for (cf, q) in d:
        t.append((a * sp.diff(cf, uc) + b * sp.diff(cf, Dl), q))
        if b != 0:
            t.append((b * cf, q + 1))
    return dnrm(t)


def slots_of(d):
    """r-slot table {(r, q): a_r(uc)} from coeff = sum_r a_r(uc) Dl^r."""
    tab = {}
    for (cf, q) in d:
        for (pows, coef) in sp.Poly(sp.expand(cf), Dl).terms():
            r = pows[0] if pows else 0
            if coef != 0:
                tab[(r, q)] = sp.expand(tab.get((r, q), 0) + coef)
    return dict((k, v) for k, v in tab.items() if v != 0)


def d_reduce(d, x):
    """Delta^r dd^(q)(x) -> 0 if r > q, else (-1)^r q!/(q-r)! dd^(q-r)."""
    out = []
    for (cf, q) in d:
        for (pows, coef) in sp.Poly(sp.expand(cf), x).terms():
            r = pows[0] if pows else 0
            if coef == 0 or r > q:
                continue
            out.append((coef * sp.Integer(-1) ** r * sp.factorial(q)
                        / sp.factorial(q - r), q - r))
    return dnrm(out)


def d_ft(d):
    """FT with the registered convention: sum over r-slots of E_transform({r: a_r}, q)."""
    out = sp.Integer(0)
    for ((r, q), a) in slots_of(d).items():
        out += E_transform({r: a}, q)
    return sp.expand(out)


def dist_eq(d1, d2):
    m = {}
    for (cf, q) in d1:
        m[q] = sp.expand(m.get(q, 0) + cf)
    for (cf, q) in d2:
        m[q] = sp.expand(m.get(q, 0) - cf)
    return all(v == 0 for v in m.values())


def dist_diff(d1, d2):
    m = {}
    for (cf, q) in d1:
        m[q] = sp.expand(m.get(q, 0) + cf)
    for (cf, q) in d2:
        m[q] = sp.expand(m.get(q, 0) - cf)
    return [(cf, q) for q, cf in sorted(m.items()) if cf != 0]


def dd_action_at(p, q, w):
    """<Dl^p dd^(q), e^{i w Dl}> = (-1)^q d^q/dDl [Dl^p e^{i w Dl}]|_0 (definition)."""
    return sp.expand((-1) ** q * sp.diff(Dl ** p * sp.exp(sp.I * w * Dl), Dl, q).subs(Dl, 0))


def dstr(d):
    return "; ".join("%s*dd^(%d)" % (cf, q) for (cf, q) in d)


# pre-registered expectations (hand-derived, three independent routes):
KEX_uc = sp.expand(om ** 2 * C(uc) + sp.Rational(1, 4) * d2C(uc))
KR_exact = [(-C(uc), 2), (sp.Rational(1, 4) * d2C(uc), 0)]

# =============================================================================
print("\n=== STEP 1: exact kernel K(u1,u2) from the functional definition ===")
# dS/dh(v) = -d/dv [C(v) h'(v)]  (by parts; boundary terms vanish on test functions).
# Second variation, both orders (functional derivatives commute; both must be exact):
K2_sympy = sp.expand(-sp.diff(C(u2) * sp.diff(sp.DiracDelta(u2 - u1), u2), u2))
K1_sympy = sp.expand(-sp.diff(C(u1) * sp.diff(sp.DiracDelta(u1 - u2), u1), u1))
K2_terms = [(-dC(u2), 1), (-C(u2), 2)]        # sum coeff(u2) dd^(q)(u2-u1)
K1_terms = [(-dC(u1), 1), (-C(u1), 2)]        # sum coeff(u1) dd^(q)(u1-u2)
_expr2 = -dC(u2) * sp.DiracDelta(u2 - u1, 1) - C(u2) * sp.DiracDelta(u2 - u1, 2)
_expr1 = -dC(u1) * sp.DiracDelta(u1 - u2, 1) - C(u1) * sp.DiracDelta(u1 - u2, 2)
check(sp.expand(K2_sympy - _expr2) == 0 and sp.expand(K1_sympy - _expr1) == 0,
      "STEP1 sympy-differentiated kernels == explicit term lists (both orders): "
      "K = -C' dd' - C dd'' with the dressing on the DIFFERENTIATED vertex")
stamp("step 1 done")

print("\n=== STEP 2: test-function verification (definition level) ===")
hA1 = (1 + al * uu) * sp.exp(-uu ** 2 / 2)
hB1 = (1 + be * uu + ga * uu ** 2) * sp.exp(-uu ** 2 / 2)
hA2 = (1 + de * uu) * sp.exp(-(uu - sp.Rational(1, 3)) ** 2 / 2)
hB2 = (1 - be * uu + ga * uu ** 2 / 3) * sp.exp(-(uu + sp.Rational(2, 5)) ** 2 / 2)


def gint(expr, uvar):
    """Exact Int_{-oo}^{oo} expr duvar for expr = sum_i poly_i(u) * exp(quadratic_i(u)),
    via closed-form Gaussian moments:
        Int u^k exp(-al u^2 + b u + c0) du = e^{c0} d^k/db^k [sqrt(pi/al) exp(b^2/(4 al))].
    (sympy's own integrate is pathological on shifted Gaussians with symbolic parameters
    -- 285+ s per integral -- so this helper is used throughout STEP 2 and STEP 8; it is
    VALIDATED against sympy's own integrate on the centered case below, and the kernel
    identity is additionally cross-checked by a sympy-native DiracDelta double integral.)"""
    tot = sp.Integer(0)
    B_ = sp.Dummy('B')
    for term in sp.Add.make_args(sp.expand(expr)):
        args = sp.Mul.make_args(term)
        expf = [a for a in args if a.func == sp.exp]
        rest = sp.Mul(*[a for a in args if a.func != sp.exp])
        if not expf:
            raise ValueError("gint: term without a Gaussian factor")
        arg = sp.expand(sum(e.args[0] for e in expf))     # exp(a)*exp(b) -> exp(a+b)
        al = -arg.coeff(uvar, 2)                          # arg = c0 + b*u - al*u^2
        b = arg.coeff(uvar, 1)
        c0 = arg.coeff(uvar, 0)
        base = sp.sqrt(sp.pi / al) * sp.exp(B_ ** 2 / (4 * al))
        for (pows, coef) in sp.Poly(sp.expand(rest), uvar).terms():
            k = pows[0] if pows else 0
            tot += coef * sp.exp(c0) * sp.diff(base, B_, k).subs(B_, b)
    return sp.expand(tot)


def zero_of(expr):
    d = sp.expand(expr)
    return d == 0 or sp.simplify(d) == 0


# validate the moment helper against sympy's own integrate on the centered case:
_v_int = sp.expand(C(uu) * sp.diff(hA1, uu) * sp.diff(hB1, uu))
check(zero_of(gint(_v_int, uu) - sp.integrate(_v_int, (uu, -sp.oo, sp.oo))),
      "STEP2 Gaussian-moment helper validated against sympy's own integrate (exact)")


def me_u2order(hA, hB):
    """(K hB)(u1) = sum (-1)^q d^q/du2 [coeff(u2) hB(u2)]|_{u2=u1}; then Int hA du1."""
    KhB = sp.Integer(0)
    for (cf, q) in K2_terms:
        KhB += (-1) ** q * sp.diff(cf * hB.subs(uu, u2), u2, q).subs(u2, u1)
    return gint(sp.expand(hA.subs(uu, u1) * KhB), u1)


def me_u1order(hA, hB):
    """(K hB)(u1) = sum coeff(u1) hB^(q)(u1); then Int hA du1."""
    KhB = sp.Integer(0)
    for (cf, q) in K1_terms:
        KhB += cf * sp.diff(hB.subs(uu, u2), u2, q).subs(u2, u1)
    return gint(sp.expand(hA.subs(uu, u1) * KhB), u1)


def qform(hA, hB):
    return gint(sp.expand(C(uu) * sp.diff(hA, uu) * sp.diff(hB, uu)), uu)



for (nm, hA, hB) in (("pair 1", hA1, hB1), ("pair 2 (shifted centres)", hA2, hB2)):
    qf = sp.expand(qform(hA, hB))
    check(zero_of(me_u2order(hA, hB) - qf),
          "STEP2 %s, u2-order: <hA,K,hB> == Int du C(u) hA' hB' (exact)" % nm)
    check(zero_of(me_u1order(hA, hB) - qf),
          "STEP2 %s, u1-order: <hA,K,hB> == Int du C(u) hA' hB' (exact)" % nm)
check(zero_of(me_u2order(hA1, hB1) - me_u2order(hB1, hA1)),
      "STEP2 kernel symmetry: <hA,K,hB> == <hB,K,hA>")
# third route: sympy's own DiracDelta integration over BOTH variables, no hand bookkeeping:
_native = sp.integrate(sp.integrate(hA1.subs(uu, u1) * K2_sympy * hB1.subs(uu, u2),
                                    (u2, -sp.oo, sp.oo)), (u1, -sp.oo, sp.oo))
check(zero_of(sp.expand(_native) - sp.expand(qform(hA1, hB1))),
      "STEP2 sympy-native DiracDelta double integral agrees (third route)")
stamp("step 2 done")


print("\n=== STEP 3: (u_c,Delta) transform, FULL distributional structure ===")
# transform under test:  u1 = uc + Dl/2, u2 = uc - Dl/2, u1 - u2 = Dl:
#     d/du2 = 1/2 d/duc - d/dDl        d/du1 = 1/2 d/duc + d/dDl
d0 = [(sp.Integer(1), 0)]                       # dd(Dl)
t = dmul(dop(d0, sp.Rational(1, 2), -1), C(uc - Dl / 2))
KD_u2 = dop(t, -sp.Rational(1, 2), 1)           # -d/du2 [ C(u2) d/du2 dd(u2-u1) ]
t = dmul(dop(d0, sp.Rational(1, 2), 1), C(uc + Dl / 2))
KD_u1 = dop(t, -sp.Rational(1, 2), -1)          # -d/du1 [ C(u1) d/du1 dd(u1-u2) ]
print("   u2-order: " + dstr(KD_u2))
print("   u1-order: " + dstr(KD_u1))
# independent route: substitute directly into the ALREADY-DIFFERENTIATED step-1 terms,
# using dd^(q)(-Dl) = (-1)^q dd^(q)(Dl):
KD_u2_subst = dnrm([((-1) ** q * cf.subs(u2, uc - Dl / 2), q) for (cf, q) in K2_terms])
KD_u1_subst = dnrm([(cf.subs(u1, uc + Dl / 2), q) for (cf, q) in K1_terms])
check(dist_eq(KD_u2, KD_u2_subst) and dist_eq(KD_u1, KD_u1_subst),
      "STEP3 operator-composition route == direct-substitution route (both orders)")
check(dist_eq(KD_u2, [(dC(uc - Dl / 2), 1), (-C(uc - Dl / 2), 2)])
      and dist_eq(KD_u1, [(-dC(uc + Dl / 2), 1), (-C(uc + Dl / 2), 2)]),
      "STEP3 transformed kernels == hand-expected exact forms: u2-order "
      "C'(uc-Dl/2) dd' - C(uc-Dl/2) dd'';  u1-order -C'(uc+Dl/2) dd' - C(uc+Dl/2) dd''")
stamp("step 3 done")

print("\n=== STEP 4: registered r-slot convention ((+-1/2)^r lever arms) ===")
S_main = slots_of(KD_u1)      # MAIN construction (protocol step 5: expand C(uc + Dl/2))
S_rev = slots_of(KD_u2)       # reversed differentiation order (expand C(uc - Dl/2))
print("   u1-placement slots (r,q)->a_r(uc): %s"
      % {str(k): str(v) for k, v in sorted(S_main.items())})
print("   u2-placement slots (r,q)->a_r(uc): %s"
      % {str(k): str(v) for k, v in sorted(S_rev.items())})
ok1 = all(sp.expand(S_main.get((r, 2), 0)
                    + sp.diff(C(uc), uc, r) / (2 ** r * sp.factorial(r))) == 0
          for r in (0, 1, 2))
ok1 = ok1 and all(sp.expand(S_main.get((r, 1), 0)
                            + sp.diff(dC(uc), uc, r) / (2 ** r * sp.factorial(r))) == 0
                  for r in (0, 1))
check(ok1, "STEP4 u1-placement r-slots == C^{(r)}(uc) (1/2)^r / r! (u1_pow lever arms at "
           "general centre); Taylor terminates at r = 2")
ok2 = all(sp.expand(S_rev.get((r, 2), 0)
                    + sp.Integer(-1) ** r * sp.diff(C(uc), uc, r)
                    / (2 ** r * sp.factorial(r))) == 0 for r in (0, 1, 2))
ok2 = ok2 and all(sp.expand(S_rev.get((r, 1), 0)
                            - sp.Integer(-1) ** r * sp.diff(dC(uc), uc, r)
                            / (2 ** r * sp.factorial(r))) == 0 for r in (0, 1))
check(ok2, "STEP4 u2-placement r-slots == C^{(r)}(uc) (-1/2)^r / r! with OPPOSITE C'-sign "
           "pairing (u2_pow lever arms) -- the coefficient-placement pin")
ok3 = all(sp.expand(S_main.get((r, 2), 0)
                    - sp.Integer(-1) ** r * S_rev.get((r, 2), 0)) == 0 for r in (0, 1, 2))
ok3 = ok3 and all(sp.expand(S_main.get((r, 1), 0)
                            + sp.Integer(-1) ** r * S_rev.get((r, 1), 0)) == 0 for r in (0, 1))
check(ok3, "STEP4 the two placements differ ONLY by the (-1)^r lever flip and the C' sign: "
           "placement and derivative-order pairing are locked together")
stamp("step 4 done")

print("\n=== STEP 5: expand C(uc +- Dl/2); reduce EVERY Dl^r dd^(q) ===")
phi_t = (1 + 3 * Dl + 5 * Dl ** 2 + 7 * Dl ** 3) * sp.exp(-Dl ** 2 / 2)
okred = True
for r in (0, 1, 2):
    for q in (0, 1, 2):
        lhs = sp.expand((-1) ** q * sp.diff(Dl ** r * phi_t, Dl, q).subs(Dl, 0))
        if r > q:
            rhs = sp.Integer(0)
        else:
            rhs = sp.expand(sp.Integer(-1) ** r * sp.factorial(q) / sp.factorial(q - r)
                            * (-1) ** (q - r) * sp.diff(phi_t, Dl, q - r).subs(Dl, 0))
        okred = okred and (sp.expand(lhs - rhs) == 0)
check(okred, "STEP5 reduction identity Dl^r dd^(q) = (-1)^r q!/(q-r)! dd^(q-r) (0 if r>q), "
             "verified by delta-action on a generic test function, all (r,q) in {0,1,2}^2")
KR_u1 = d_reduce(KD_u1, Dl)
KR_u2 = d_reduce(KD_u2, Dl)
print("   reduced (both orders): " + dstr(KR_u1))
check(dist_eq(KR_u1, KR_exact) and dist_eq(KR_u2, KR_exact),
      "STEP5 both differentiation orders reduce to the SAME manifestly centre-symmetric "
      "kernel -C(uc) dd'' + (1/4)C''(uc) dd (pre-registered)")
diff_forms = dist_diff(KD_u2, KD_u1)
check(dist_eq(diff_forms, [(2 * dC(uc), 1), (sp.expand(dC(uc) * Dl), 2)])
      and dist_eq(d_reduce(diff_forms, Dl), []),
      "STEP5 the UNREDUCED orders differ by exactly 2C'(uc) dd' + C'(uc) Dl dd'', which "
      "reduces to ZERO -- order-independence is a distributional identity, not an assumption")
okrf = True
for ((r, q), a) in S_main.items():
    if r > q:
        red = []
    else:
        red = [(a * sp.Integer(-1) ** r * sp.factorial(q) / sp.factorial(q - r), q - r)]
    okrf = okrf and (sp.expand(E_transform({r: a}, q) - d_ft(red)) == 0)
check(okrf, "STEP5/6 per-slot consistency: E_transform(slot) == FT of the REDUCED slot, "
            "every slot (reduce-then-FT == direct E_transform)")
stamp("step 5 done")

print("\n=== STEP 6: FT with the frozen convention (E_transform) ===")
Kt_u1 = d_ft(KD_u1)
Kt_u2 = d_ft(KD_u2)
print("   K_tilde(uc,om) = " + str(Kt_u1))
check(sp.expand(Kt_u1 - KEX_uc) == 0 and sp.expand(Kt_u2 - KEX_uc) == 0,
      "STEP6 K_tilde(uc,om) == om^2 C(uc) + (1/4) C''(uc)  (BOTH placements; pre-registered)")
okp = True
okm = True
for r in (0, 1, 2):
    for q in (0, 1, 2):
        okp = okp and (sp.expand(E_transform({r: sp.Integer(1)}, q)
                                 - dd_action_at(r, q, om)) == 0)
        if (r + q) % 2 == 1 and r <= q:
            okm = okm and (sp.expand(E_transform({r: sp.Integer(1)}, q)
                                     - dd_action_at(r, q, -om)) != 0)
check(okp, "STEP6 FT-sign pin: E_transform(p,q) == delta-action on e^{+i om Dl} for every "
           "(p,q) in {0,1,2}^2 (the registered convention IS the e^{+i om Dl} kernel FT)")
check(okm, "CONTROL E (negative): the conjugate action e^{-i om Dl} DIFFERS on every odd "
           "(p,q) term -- the registered FT sign is pinned per-term, non-degenerately")
note("global-flip degeneracy of THIS toy: the exact kernel is distributionally EVEN in Dl "
     "(reduced form has Dl-free coefficients), so a consistent global conjugation "
     "(E_transform -> conjugate AND om -> -om) is unobservable at the summed level; the pin "
     "above is per-term, which is exactly the granularity at which engines 4-5 apply it")
note("E_transform table: dd->1, dd'->-i om, dd''->-om^2, Dl dd'-> -1, Dl dd''-> 2 i om, "
     "Dl^2 dd''-> 2")
stamp("step 6 done")

print("\n=== STEP 7: set u_c = 0 LAST (+ second-centre repeat + registered u_pow rules) ===")
Kt0 = sp.expand(Kt_u1.subs(uc, 0))
check(sp.expand(Kt0 - (om ** 2 + c2 / 2)) == 0,
      "STEP7 K_tilde(0,om) == om^2 + c2/2  (pre-registered; u_c = 0 applied LAST)")
KD_u1_at0 = dnrm([(cf.subs(uc, 0), q) for (cf, q) in KD_u1])
check(sp.expand(d_ft(KD_u1_at0) - Kt0) == 0,
      "STEP7 exact early-vs-late equivalence: substituting u_c = 0 in the FULL transformed "
      "kernel commutes with reduction+FT (the discipline 'LAST' protects the slot "
      "bookkeeping; the exact pipeline itself is order-independent)")
# exercise the registered u1_pow/u2_pow rules DIRECTLY at u_c = 0 (u = +-Dl/2 vertices):
cC = [sp.Integer(1), c1, c2]                    # C(u)  = sum cC[n] u^n
cdC = [c1, 2 * c2]                              # C'(u) = sum cdC[n] u^n
Ebase = lambda q: E_transform({0: sp.Integer(1)}, q)
Kt0_reg2 = sum(cdC[n] * u2_pow(Ebase(1), n) for n in (0, 1)) \
    - sum(cC[n] * u2_pow(Ebase(2), n) for n in (0, 1, 2))
Kt0_reg1 = -sum(cdC[n] * u1_pow(Ebase(1), n) for n in (0, 1)) \
    - sum(cC[n] * u1_pow(Ebase(2), n) for n in (0, 1, 2))
check(sp.expand(Kt0_reg2 - Kt0) == 0 and sp.expand(Kt0_reg1 - Kt0) == 0,
      "STEP7 registered u2_pow / u1_pow rules (u^n -> (+-1/2)^n (-i d/dom)^n on the omega "
      "base) reproduce K_tilde(0,om) exactly -- the r-slot convention IS the registered "
      "vertex-placement rule")
ucs = sp.Rational(1, 3)
inner_direct = sp.Integer(0)
for ((r, q), a) in S_main.items():
    inner_direct += a.subs(uc, ucs) * dd_action_at(r, q, om)
check(sp.expand(inner_direct - Kt_u1.subs(uc, ucs)) == 0,
      "STEP7 second centre u_c = 1/3: direct delta-action Dl-integral == pipeline K_tilde "
      "(centre dependence VERIFIED, not inferred from one coordinate choice)")
stamp("step 7 done")

print("\n=== STEP 8: independent cross-check by acting on plane waves ===")
# bilinear pairing mirroring the machinery's A/B sectors:  h_A = e^{+i o1 u}, h_B = e^{-i o2 u}
# Construction 2 (NO Dl-machinery): (K h_B)(u) = -d/du[C h_B'] = (o2^2 C + i o2 C') e^{-i o2 u}
#   M2 = Int du e^{i(o1-o2)u} [o2^2 C(u) + i o2 C'(u)]
# Construction 1: M1 = Int duc e^{i(o1-o2)uc} K_tilde(uc, (o1+o2)/2)   [pipeline]
# Coordinates S = o1+o2 = sv, Q = o1-o2 = qv (so o2 = (sv-qv)/2); moments:
#   Int du e^{i qv u} u^m = 2 pi (-i)^m dd^(m)(qv)      (grounded by the regulator below)


def moments_to_dist(poly_in_u, uvar):
    """Int du e^{i qv u} poly(u)  ->  dist in qv (coefficients carry the 2 pi (-i)^m)."""
    out = []
    for (pows, coef) in sp.Poly(sp.expand(poly_in_u), uvar).terms():
        m = pows[0] if pows else 0
        out.append((sp.expand(coef * 2 * sp.pi * (-sp.I) ** m), m))
    return dnrm(out)


phq = sp.exp(-qv ** 2 / 2) * (1 + 2 * qv)      # generic test function of qv
reg0 = gint(sp.exp(sp.I * qv * uu - eps_ * uu ** 2), uu)    # sqrt(pi/eps) e^{-qv^2/(4 eps)}
_lhs0 = sp.limit(sp.simplify(gint(sp.expand(reg0 * phq), qv)), eps_, 0, '+')
okmom = sp.simplify(_lhs0 - 2 * sp.pi * phq.subs(qv, 0)) == 0
for m in (1, 2):
    okmom = okmom and zero_of(
        gint(sp.exp(sp.I * qv * uu - eps_ * uu ** 2) * uu ** m, uu)
        - sp.diff(reg0, qv, m) / sp.I ** m)
check(okmom, "STEP8 moment identity Int du e^{i Q u} u^m = 2 pi (-i)^m dd^(m)(Q) grounded: "
             "m=0 regulator limit == 2 pi dd acting on a generic test function; m>=1 follow "
             "exactly as (1/i)^m d^m/dQ^m of the m=0 regulator transform")


integrand2 = sp.expand((sv - qv) ** 2 / 4 * C(uu) + sp.I * (sv - qv) / 2 * dC(uu))
M2_red = d_reduce(moments_to_dist(integrand2, uu), qv)
M1_dist = moments_to_dist(sp.expand(Kt_u1.subs(om, sv / 2)), uc)
innerp = sp.Integer(0)
for ((r, q), a) in S_main.items():
    innerp += a * dd_action_at(r, q, sv / 2)
M1p_dist = moments_to_dist(sp.expand(innerp), uc)
EX_M = [(sp.expand(2 * sp.pi * (sv ** 2 / 4 + c2 / 2)), 0),
        (sp.expand(2 * sp.pi * (-sp.I) * c1 * sv ** 2 / 4), 1),
        (sp.expand(2 * sp.pi * (-c2 * sv ** 2 / 4)), 2)]
print("   M2 (direct action)   : " + dstr(M2_red))
print("   M1 (pipeline FT)     : " + dstr(M1_dist))
check(dist_eq(M1_dist, M1p_dist),
      "STEP8 pipeline-E_transform route == direct delta-action Dl-integral route (same M1)")
check(dist_eq(M1_dist, M2_red),
      "STEP9 BOTH CONSTRUCTIONS AGREE EXACTLY: M1 (transform -> r-slots -> reduction -> "
      "E_transform) == M2 (direct operator action on plane waves), as distributions in "
      "Q = o1-o2, coefficient by coefficient")
check(dist_eq(M2_red, EX_M) and dist_eq(M1_dist, EX_M),
      "STEP8/9 matrix element == pre-registered 2 pi {(S^2/4 + c2/2) dd(Q) "
      "- i (c1 S^2/4) dd'(Q) - (c2 S^2/4) dd''(Q)}")
stamp("steps 8-9 done")

print("\n=== STEP 9 (continued): toy master identity ===")
FA = sp.expand(om ** 2 * C(uc))
check(sp.expand(Kt_u1 - FA - sp.Rational(1, 4) * d2C(uc)) == 0
      and sp.expand(Kt_u1 - FA) == c2 / 2,
      "STEP9 toy master identity: F_B - F_A = (1/4) C''(uc) = c2/2 (additive, om-independent)")
check(sp.expand(Kt_u1 - FA).subs(c2, 0) == 0,
      "STEP9 order theorem: the frozen-centre discrepancy is structurally ABSENT when "
      "C'' = 0 (linear dressings are centre-blind); it first bites at C'' ~ H^2, exactly "
      "the regime where the Phase-11 span test flips")
note("normalization correspondence (computed, flagged for the owner): with "
     "S = (1/2) Int C (h')^2 the exact frozen-centre discrepancy is (1/4)C''.  The "
     "2026-08-27 centre-mismatch diagnostic reported p(p+1)/2 H^2 for OP1 = c (phi')^2, "
     "i.e. (1/2)c''(0) -- exactly TWICE this toy's coefficient; the two agree iff that "
     "instrument's OP1 kernel was normalised without the 1/2 (S = Int c (phi')^2 => "
     "discrepancy (1/2)c'').  This toy's spec pins the 1/2 explicitly; the general rebuild "
     "must carry this normalization table.")

print("\n=== CONTROLS A-D (each MUST be detected as WRONG) ===")


def pw_agrees(KD):
    """does the candidate kernel's pipeline matrix element equal the direct M2?"""
    return dist_eq(moments_to_dist(sp.expand(d_ft(KD).subs(om, sv / 2)), uc), M2_red)


# -- Control A: wrong sign of d/dDl in the (uc,Dl) chain rule ----------------------
t = dmul(dop(d0, sp.Rational(1, 2), 1), C(uc - Dl / 2))     # WRONG inner d/du2
KDA = dop(t, -sp.Rational(1, 2), -1)                        # WRONG outer -d/du2
t = dmul(dop(d0, sp.Rational(1, 2), -1), C(uc + Dl / 2))    # WRONG inner d/du1
KDA1 = dop(t, -sp.Rational(1, 2), 1)                        # WRONG outer -d/du1
detA = [check(not dist_eq(d_reduce(KDA, Dl), d_reduce(KDA1, Dl)),
              "CONTROL A (wrong d/dDl sign) detected: the two differentiation orders "
              "DISAGREE after reduction"),
        check(sp.expand(d_ft(KDA) - KEX_uc) != 0,
              "CONTROL A detected: K_tilde != om^2 C + (1/4)C'' (spurious i om C' term, "
              "wrong C'' sign)"),
        check(not pw_agrees(KDA),
              "CONTROL A detected: plane-wave matrix element != direct operator action")]

# -- Control B: wrong lever arm (u = uc +- Dl instead of uc +- Dl/2) ---------------
# geometry u1 = uc + Dl, u2 = uc - Dl  =>  u2 - u1 = -2 Dl, dd(-2Dl) = (1/2) dd(Dl)
t = dmul(dop([(sp.Rational(1, 2), 0)], sp.Rational(1, 2), -1), C(uc - Dl))
KDB = dop(t, -sp.Rational(1, 2), 1)
detB = [check(sp.expand(d_ft(KDB) - KEX_uc) != 0,
              "CONTROL B (lever arm 1 instead of 1/2) detected: K_tilde != exact "
              "(half-weight om^2 C term + spurious (i/4) om C' term)"),
        check(not pw_agrees(KDB), "CONTROL B detected: plane-wave mismatch")]

# -- Control C: frozen-centre shortcut (Route A) -----------------------------------
KDC1 = [(-C(uc), 2)]                    # only the undifferentiated-dressing slot survives
detC = [check(sp.expand(d_ft(KDC1) - KEX_uc) != 0,
              "CONTROL C (frozen-centre / Route A) detected: om^2 C(uc) != om^2 C + (1/4)C'' "
              "-- the discarded derivative-of-C terms are exactly the (1/4)C'' "
              "master-identity residue"),
        check(not pw_agrees(KDC1), "CONTROL C detected: plane-wave mismatch")]
KDC2 = [(-dC(uc), 1), (-C(uc), 2)]      # freeze-at-centre variant (keeps frozen C' dd')
detCp = [check(sp.expand(d_ft(KDC2) - KEX_uc) != 0 and not pw_agrees(KDC2),
               "CONTROL C' (freeze-at-centre variant) detected: spurious -i om C'(uc) term")]

# -- Control D: coefficient placement at the wrong vertex ---------------------------
KDD = [(dC(uc + Dl / 2), 1), (-C(uc + Dl / 2), 2)]   # u2-order signs, u1-slot placement
detD = [check(not dist_eq(d_reduce(KDD, Dl), KR_exact),
              "CONTROL D (wrong-vertex placement) detected: reduced kernel wrong "
              "(2C' dd' - C dd'' - (3/4)C'' dd)"),
        check(sp.expand(d_ft(KDD) - KEX_uc) != 0 and not pw_agrees(KDD),
              "CONTROL D detected: K_tilde != exact and plane-wave mismatch")]
KDD_swapped = dnrm([(sp.Integer(-1) ** q * cf.subs(Dl, -Dl), q) for (cf, q) in KDD])
detD.append(check(not dist_eq(KDD, KDD_swapped),
                  "CONTROL D detected: kernel NOT symmetric under u1 <-> u2 (Dl -> -Dl)"))
sym_exact = dnrm([(sp.Integer(-1) ** q * cf.subs(Dl, -Dl), q) for (cf, q) in KR_exact])
detD.append(check(dist_eq(KR_exact, sym_exact),
                  "CONTROL D contrast: the EXACT reduced kernel IS symmetric under "
                  "Dl -> -Dl (coefficient placement is pinned by symmetry itself)"))
stamp("controls A-D done")

print("\n=== FLAT CONTROL: C == 1 reduces exactly to the old r=0 structure ===")
flat = {c1: 0, c2: 0}
KD_u1f = dnrm([(cf.subs(flat), q) for (cf, q) in KD_u1])
KD_u2f = dnrm([(cf.subs(flat), q) for (cf, q) in KD_u2])
detF = [check(dist_eq(d_reduce(KD_u1f, Dl), [(-sp.Integer(1), 2)])
              and dist_eq(d_reduce(KD_u2f, Dl), [(-sp.Integer(1), 2)]),
              "FLAT: reduced kernel == -dd''(Dl) exactly (the old r=0 structure), both orders"),
        check(sp.expand(d_ft(KD_u1f) - om ** 2) == 0 and sp.expand(d_ft(KD_u2f) - om ** 2) == 0,
              "FLAT: K_tilde == om^2 exactly (old r=0 structure), both orders")]
M1f = moments_to_dist(sp.expand(d_ft(KD_u1f).subs(om, sv / 2)), uc)
M2f = d_reduce(moments_to_dist(sp.expand((sv - qv) ** 2 / 4), uu), qv)
detF.append(check(dist_eq(M1f, M2f) and dist_eq(M2f, [(sp.expand(2 * sp.pi * sv ** 2 / 4), 0)]),
                  "FLAT: plane-wave check passes; M == 2 pi (S^2/4) dd(Q)"))
detF.append(check(sp.expand(d_ft(KD_u1f) - d_ft([(-sp.Integer(1), 2)])) == 0,
                  "FLAT: the frozen-centre shortcut is EXACT at C == 1 (documents why a "
                  "flat/linear dressing is structurally blind to the centre defect -- "
                  "computed structure, not interpretation)"))
stamp("flat control done")

print("\n=== VERDICT ===")
green = not FAIL
verdict = "GREEN" if green else "RED"
detE = [e["pass"] for e in LOG if e["kind"] == "check" and e["msg"].startswith("CONTROL E")]
detE_ok = bool(detE) and all(detE)
ctrl = {
    "A_wrong_Delta_sign": "detected" if all(detA) else "NOT DETECTED",
    "B_wrong_lever_arm": "detected" if all(detB) else "NOT DETECTED",
    "C_frozen_centre_shortcut": "detected" if all(detC) else "NOT DETECTED",
    "Cp_freeze_at_centre": "detected" if all(detCp) else "NOT DETECTED",
    "D_wrong_vertex_placement": "detected" if all(detD) else "NOT DETECTED",
    "E_conjugate_FT_sign": ("detected per-term (odd (p,q)); summed-level global flip "
                            "degenerate for this toy (exact kernel even in Dl)"
                            if detE_ok else "NOT DETECTED"),
    "flat_C_eq_1": ("PASS (reduces exactly to -dd'' -> om^2; frozen shortcut exact at "
                    "C''=0)" if all(detF) else "FAILED"),
}
print("PHASE-11 TOY HESSIAN CALIBRATION: %s   [FAIL count = %d]" % (verdict, len(FAIL)))
for f_ in FAIL:
    print("   FAILED:", f_)

res = {
    "instrument": "wall_d2_phase11_toy_hessian.py",
    "verdict": verdict,
    "question": "do the registered Phase-11 conventions (coefficient placement, (u_c,Delta) "
                "transform, Delta^r delta^(q) reduction, FT signs) reproduce the EXACT "
                "functional Hessian of S = (1/2) Int du C(u) (h'(u))^2, "
                "C = 1 + c1 u + c2 u^2, with both constructions agreeing exactly?",
    "action": "S[h] = 1/2*Int du C(u)*h'(u)^2,  C(u) = 1 + c1*u + c2*u^2",
    "pinned": {
        "exact_kernel_u_c_Delta": ("u2-order: C'(uc-Dl/2) dd' - C(uc-Dl/2) dd'' ; "
                                   "u1-order: -C'(uc+Dl/2) dd' - C(uc+Dl/2) dd'' ; "
                                   "equal after Dl^r dd^(q) reduction"),
        "transform": ("d/du2 = 1/2 d/duc - d/dDl ; d/du1 = 1/2 d/duc + d/dDl ; "
                      "u1 = uc + Dl/2, u2 = uc - Dl/2"),
        "r_slot_convention": ("C(uc +- Dl/2) = sum_r C^{(r)}(uc) (+-1/2)^r / r! * Dl^r "
                              "(u1_pow/u2_pow lever arms); Taylor terminates at r = 2"),
        "Delta_power_delta_reduction": ("Dl^r dd^(q) = (-1)^r q!/(q-r)! dd^(q-r) if r<=q "
                                        "else 0; verified against delta-action and "
                                        "per-slot consistent with E_transform"),
        "FT_sign": ("E_transform(p,q) == delta-action on e^{+i om Dl}, per term; conjugate "
                    "fails on odd (p,q); summed-level global flip degenerate for this toy "
                    "(kernel even in Dl) -- disclosed"),
        "kernel_tilde": "om^2 C(uc) + (1/4) C''(uc) = " + str(Kt_u1),
        "kernel_tilde_at_reference": str(Kt0),
        "reduced_kernel": "-C(uc) dd''(Dl) + (1/4) C''(uc) dd(Dl)",
        "toy_master_identity": ("F_B - F_A = (1/4) C''(uc) = c2/2 (additive, om-independent; "
                                "structurally absent when C'' = 0)"),
        "plane_wave_matrix_element": ("2 pi {(S^2/4 + c2/2) dd(Q) - i (c1 S^2/4) dd'(Q) "
                                      "- (c2 S^2/4) dd''(Q)}, S = o1+o2, Q = o1-o2"),
        "normalization_note": ("prior centre-mismatch diagnostic OP1 (c (phi')^2) reported "
                               "(1/2)c''(0) = p(p+1)/2 H^2, i.e. TWICE this toy's (1/4)C''; "
                               "consistent iff that instrument's OP1 kernel carried no 1/2 "
                               "(S = Int c (phi')^2); flagged for the owner"),
    },
    "controls": ctrl,
    "checks": LOG,
    "fail_count": len(FAIL),
    "failures": FAIL,
    "fence": ("toy calibration only; the 96/300 H^2 residual remains COMPUTED AND "
              "UNINTERPRETED; no basis change, no refit, no register edits, nothing banked"),
}
with open(os.path.join(HERE, "WALL_D2_PHASE11_TOY_HESSIAN_RESULT.json"), "w") as fh:
    json.dump(res, fh, indent=2)

md = """# WALL-D2 PHASE-11 TOY FUNCTIONAL-HESSIAN CALIBRATION -- VERDICT (W-0, computed-and-reported)

Instrument: `PHYSICS_LEDGER/wall_d2_phase11_toy_hessian.py` (standalone; no import of, and
no edit to, any existing file).  Date: {date}.  Exit code: {exitcode}.  FAIL count: {nfail}.

## VERDICT: {verdict}

The nine-step protocol ran on the owner-specified toy
`S[h] = 1/2 Int du C(u) (h'(u))^2,  C(u) = 1 + c1 u + c2 u^2`,
with the registered Phase-11 conventions mirrored verbatim in form from
`wall_d2_phases8_12.py` (FT `Sigma_tilde(om) = Int dDelta e^(+i om Delta) Sigma(Delta)`,
`apply_Delta_power = (-i d/dom)^n`, `E_transform`, `u1_pow`/`u2_pow` lever arms).
{summary}

## Pinned conventions (each backed by the checks in the JSON artifact)

1. **Coefficient placement.** The exact Hessian carries the dressing on the DIFFERENTIATED
   vertex with a locked sign pairing: u2-order `C'(uc-Dl/2) dd' - C(uc-Dl/2) dd''`,
   u1-order `-C'(uc+Dl/2) dd' - C(uc+Dl/2) dd''`. Placement and derivative-order pairing
   are NOT independent: the wrong-vertex hybrid (control D) breaks kernel symmetry and
   every check.
2. **(u_c, Delta) transform.** `u1 = uc + Dl/2, u2 = uc - Dl/2`;
   `d/du2 = 1/2 d/duc - d/dDl`, `d/du1 = 1/2 d/duc + d/dDl` (control A pins the signs).
3. **r-slot convention.** `C(uc +- Dl/2) = sum_r C^(r)(uc) (+-1/2)^r / r! Dl^r` -- the
   registered `u1_pow`/`u2_pow` lever arms at general centre (also exercised directly at
   uc = 0); Taylor terminates at r = 2 (control B pins the 1/2).
4. **Dl^r dd^(q) reduction.** `Dl^r dd^(q) = (-1)^r q!/(q-r)! dd^(q-r)` (r <= q), `0`
   (r > q); verified against delta-action on generic test functions and per-slot
   consistent with the registered E_transform.
5. **FT signs.** `E_transform(p,q) == <Dl^p dd^(q), e^(+i om Dl)>` per term; the conjugate
   action differs on every odd (p,q) (control E). A summed-level global flip is degenerate
   for THIS toy (the exact kernel is distributionally even in Dl) -- disclosed; the pin is
   at the per-term granularity at which engines 4-5 actually apply the rule.

## Computed exact results

- `K_tilde(uc,om) = om^2 C(uc) + (1/4) C''(uc) = {ktu}`
- At the reference `uc = 0`: `K_tilde = {kt0}`
- Reduced kernel: `-C(uc) dd''(Dl) + (1/4) C''(uc) dd(Dl)` (manifestly centre-symmetric;
  both differentiation orders agree exactly after reduction).
- Plane-wave matrix element (both constructions, exact):
  `2 pi {{(S^2/4 + c2/2) dd(Q) - i (c1 S^2/4) dd'(Q) - (c2 S^2/4) dd''(Q)}}`.
- **Toy master identity:** `F_B - F_A = (1/4) C''(uc) = c2/2` -- additive, om-independent,
  and structurally ABSENT when `C'' = 0` (the order theorem: flat/linear dressings are
  centre-blind; the defect first bites at `C'' ~ H^2`).

## Controls

| control | required | outcome |
|---|---|---|
| A wrong d/dDl sign in the chain rule | FAIL | {cA} |
| B lever arm 1 instead of 1/2 | FAIL | {cB} |
| C frozen-centre shortcut (Route A) | FAIL | {cC} |
| C' freeze-at-centre variant | FAIL | {cCp} |
| D wrong-vertex coefficient placement | FAIL | {cD} |
| E conjugate FT sign | FAIL | {cE} |
| flat C = 1 | PASS | {cF} |

## Scoped notes (no interpretation)

- Normalization correspondence, flagged for the owner: the 2026-08-27 centre-mismatch
  diagnostic reported an OP1 (`c (phi')^2`) discrepancy of `p(p+1)/2 H^2 = (1/2)c''(0)`;
  this toy's exact coefficient with the explicit `1/2` in the action is `(1/4)C''`. The two
  agree iff that instrument's OP1 kernel was normalised without the `1/2`. The rebuild must
  carry this normalization table explicitly.
- The 96/300 H^2 residual remains COMPUTED AND UNINTERPRETED. No basis change, no refit,
  no operator addition, no register edits, nothing banked.

## Next (only if GREEN, per the stop directive)

Generalise the SAME nine-step algorithm to the four frozen operators as an action-functional
(IBP-invariant, F_B-type) instrument; then re-run `wall_d2_span_test.py` UNCHANGED. The
owner-adjudication gate from the 2026-08-27 ruling stands.
""".format(date=time.strftime("%Y-%m-%d"),
           exitcode=("0" if green else "1"),
           nfail=len(FAIL),
           verdict=verdict,
           summary=("ALL checks passed." if green else
                    "FAILURES PRESENT -- see WALL_D2_PHASE11_TOY_HESSIAN_RESULT.json."),
           ktu=str(Kt_u1),
           kt0=str(Kt0),
           cA=ctrl["A_wrong_Delta_sign"], cB=ctrl["B_wrong_lever_arm"],
           cC=ctrl["C_frozen_centre_shortcut"], cCp=ctrl["Cp_freeze_at_centre"],
           cD=ctrl["D_wrong_vertex_placement"], cE=ctrl["E_conjugate_FT_sign"],
           cF=ctrl["flat_C_eq_1"])
with open(os.path.join(HERE, "WALL_D2_PHASE11_TOY_HESSIAN_VERDICT.md"), "w") as fh:
    fh.write(md)

print("\nwrote WALL_D2_PHASE11_TOY_HESSIAN_RESULT.json and "
      "WALL_D2_PHASE11_TOY_HESSIAN_VERDICT.md")
sys.exit(0 if green else 1)








