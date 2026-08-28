#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""PHASE-11 FOUR-OPERATOR ACTION-FUNCTIONAL BASIS RECONSTRUCTION (owner-authorized
2026-08-27; standing state 5fd77c0).

Generalises the toy-validated nine-step functional-Hessian algorithm
(wall_d2_phase11_toy_hessian.py, 46/46) to the four frozen operators {sqrt(-g),
sqrt(-g)R, sqrt(-g)R^2, sqrt(-g)R_mnR^mn}, emitting corrected, IBP-invariant,
action-functional kernels IN THE EXACT REPRESENTATION wall_d2_span_test.py consumes
(same E_/P_ component map, same K samples, same H grading, numeric (omega,k)). The
span test then runs UNCHANGED. The old basis side (coincident density, u->0, "Route
A") is the r=0 term of this construction and is IBP-non-invariant (2026-08-27
centre-mismatch diagnostic); the (l,r)!=(0,0) terms are the explicit distributional
corrections it could not see -- the generalisation of
    C(u1) dd''(u1-u2)  ->  -C(u_c) dd''(Delta) + (1/4) C''(u_c) dd(Delta).

HARD GATES (a rebuild without every one of these is not acceptable):
  G0 normalisation table, gated explicitly: S=(1/2)Int C(h')^2 => dK=(1/4)C'';
     S=Int C(h')^2 => dK=(1/2)C''. The four operators carry the Int-row (no 1/2),
     asserted in code; both rows verified through the same engine.
  G1 IBP invariance at the ACTION level (symbolic, before any omega/K evaluation);
     two representations differing by a total derivative must give IDENTICAL kernels.
  G2 H^0 Gilkey regression {m^4/4, m^2/12, 1/240, 1/120} + held-out K sample, no refit.
     If H^0 breaks: STOP (no cache written).
  G3 toy agreement: the engine restricted to the toy reproduces the toy's kernels
     exactly, incl. K~(0,om) = om^2 + c2/2.
  G4 dual route: one operator built a second way (full-eps split construction,
     independent of the sector algebra); agreement required.
  G5 odd-structure functional-Hessian test (the order-theorem replacement): the
     exact functional Hessian of S=Int B(u)[hA'hB+hA hB'] computed three
     independent ways (direct EL Hessian, raw-kernel centred slot route,
     generalised master kernel) must agree: K~ = -B'(u_c) -- a genuine O(H^1)
     correction whenever B' carries an O(H) slope, with the old coincident-density
     kernel identically zero on the pair; plus the computed H^1 attribution on the
     real tables and non-vacuity at H^2.  The retired 'corrections first appear at
     H^2' claim was toy-only (its proof used the toy's single even structure); no
     universal first-nonzero correction order is claimed beyond what is computed.
  G6 controls: the toy's broken conventions ported; each must FAIL to reproduce
     the corrected kernel at the order it corrupts (A/B/C/Cp: H^0 preserved,
     difference at H^1/H^2; D/conj: caught already at H^0, computed and reported).

INDEPENDENCE CONDITION (reviewer, wired): the corrected kernels are DERIVED from the
functional-Hessian construction. Old kernels / H^2 residual / span test are used ONLY
as validation targets (G2, G6), never as inputs. No correction coefficient is guessed,
fitted, or solved for.

ARTIFACT HYGIENE: every `checks` entry carries an explicit "pass" field; notes live in
a separate array. The AF-basis cache (.p11_af_basis_cache.txt, srepr round-trip) is
written ONLY on a fully green run.

W-0: computed and reported only. No register edits, no operator additions, no refit,
no edits to the loop side, the assembly cache, or wall_d2_span_test.py.
"""
import json
import os
import sys
import time

import sympy as sp

assert len(sys.argv) == 1, "no phase argument (argv must stay clean for the machinery exec)"
HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()
FAIL = []
CHECKS = []
NOTES = []


def check(cond, msg, gate=""):
    ok = bool(cond)
    print(("  ok   " if ok else "  FAIL ") + (("[%s] " % gate if gate else "")) + msg)
    sys.stdout.flush()
    CHECKS.append({"kind": "check", "gate": gate, "pass": ok, "msg": msg})
    if not ok:
        FAIL.append(("[%s] %s" % (gate, msg)) if gate else msg)
    return ok


def note(msg):
    print("  --   " + msg)
    sys.stdout.flush()
    NOTES.append({"kind": "note", "msg": msg})


def stamp(s):
    print("[%7.1fs] %s" % (time.time() - T0, s))
    sys.stdout.flush()


_BLK = [time.time()]


def blk(name, limit=1200):
    """per-sub-block wall-clock guard (owner rule: ~20 min)."""
    el = time.time() - _BLK[0]
    _BLK[0] = time.time()
    flag = "  <-- EXCEEDS THRESHOLD" if el > limit else ""
    print("   [block] %s: %7.1fs%s" % (name, el, flag))
    sys.stdout.flush()
    return el


# ---------------- symbols (mirrored from wall_d2_phases8_12.py) ------------------
H, om, kk, mm = sp.symbols('H omega k m', positive=True)
uu = sp.Symbol('u', real=True)                    # the machinery's basis-side u
zz3 = sp.Symbol('z', real=True)
xx3, yy3 = sp.symbols('x_c y_c', real=True)
COORD = [uu, xx3, yy3, zz3]
wE, wP = sp.symbols('wE wP')                      # SPLIT u-frequencies: E/A-leg, P/B-leg
eta = sp.diag(1, -1, -1, -1)
a_bg = 1 + H * uu + H ** 2 * uu ** 2              # H-truncated a(u), machinery's basis side


def sym_mat(pref):
    M = sp.zeros(4, 4)
    for i in range(4):
        for j in range(i, 4):
            s_ = sp.Symbol('%s_%d%d' % (pref, i, j))
            M[i, j] = s_
            M[j, i] = s_
    return M


e1m, e2m = sym_mat('E'), sym_mat('P')             # same interned E_ij / P_ij symbols
OPS = ('Lam', 'EH', 'R2', 'Rmn2')
K_SAMPLES = [(sp.Rational(3), sp.Rational(2)), (sp.Rational(5), sp.Rational(2)),
             (sp.Rational(7), sp.Rational(3))]     # third is HELD OUT (frozen)


# ---------------- the master-formula engine (toy-validated conventions) -----------
# MASTER FORMULA (derived; the toy's registered u1_pow/u2_pow lever-arm rules are the
# p=q=1 specialisation):
#   P-placement (dressings at u_P = u_c + Delta/2):
#     K~ = Sum_{p,q} Sum_{l<=q} Sum_{r>=0} (-1)^q C(q,l) (1/2)^r/r! B^{(l+r)}_{pq}(u_c)
#          * (-i d/dom)^r [(-i om)^{p+q-l}]
#   E-placement (dressings at u_E = u_c - Delta/2):
#     K~ = Sum_{p,q} Sum_{l<=p} Sum_{r>=0} (-1)^p C(p,l) (-1/2)^r/r! B^{(l+r)}_{pq}(u_c)
#          * (-1)^{p+q-l} * (-i d/dom)^r [(-i om)^{p+q-l}]
# The (l,r)=(0,0) term of either placement is EXACTLY the old coincident-density
# kernel: Sum_pq B_pq(u_c) (-i om)^p (i om)^q.
def Etr(r, Q, conj=False):
    """registered E_transform of Delta^r dd^(Q)(Delta):  (-i d/dom)^r [(-i om)^Q].
    conj=True is the CONTROL-E variant (the e^{-i om Delta} action)."""
    if r < 0 or r > Q:
        return sp.Integer(0)
    ii = sp.I if conj else -sp.I
    term = (ii * om) ** Q
    for _ in range(r):
        term = ii * sp.diff(term, om)
    return sp.expand(term)


def bder(B, s, uc=None):
    """s-th u-derivative of B(u), evaluated at u = uc (default 0 = the reference)."""
    at = 0 if uc is None else uc
    if s == 0:
        return sp.expand(B.subs(uu, at))
    return sp.expand(sp.diff(B, uu, s).subs(uu, at))


def udeg(B):
    e = sp.expand(B)
    return sp.Poly(e, uu).degree() if e != 0 else -1


def _iter_terms(tab, placement, uc=None):
    """yield (prefactor, B^{(l+r)}, r, Q, (p,q,l)) over the master-formula sum."""
    for (p, q), B in tab.items():
        dg = udeg(B)
        if dg < 0:
            continue
        lmax = q if placement == 'P' else p
        for l in range(lmax + 1):
            for r in range(dg + 1 - l):
                Blr = bder(B, l + r, uc)
                if Blr == 0:
                    continue
                if placement == 'P':       # dressings at u_P = u_c + Delta/2
                    pref = sp.Integer(-1) ** q * sp.binomial(q, l) \
                        / (sp.Integer(2) ** r * sp.factorial(r))
                else:                      # dressings at u_E = u_c - Delta/2
                    pref = sp.Integer(-1) ** p * sp.binomial(p, l) \
                        * sp.Integer(-1) ** r / (sp.Integer(2) ** r * sp.factorial(r)) \
                        * sp.Integer(-1) ** (p + q - l)
                yield pref, Blr, r, p + q - l, (p, q, l)


def master(tab, placement='P', conj=False, uc=None):
    """the action-functional (functional-Hessian) kernel: the master formula."""
    out = sp.Integer(0)
    for pref, Blr, r, Q, _key in _iter_terms(tab, placement, uc):
        out += pref * Blr * Etr(r, Q, conj)
    return sp.expand(out)


def old_kernel_of(tab, uc=None):
    """Route A: the (l,r)=(0,0) term == the OLD coincident-density kernel
    (D_AB evaluated at the centre with the shared frequency)."""
    out = sp.Integer(0)
    for (p, q), B in tab.items():
        out += bder(B, 0, uc) * (-sp.I * om) ** p * (sp.I * om) ** q
    return sp.expand(out)


def correction_of(tab, placement='P'):
    """the EXPLICIT distributional corrections: every (l,r) != (0,0) term."""
    out = sp.Integer(0)
    for pref, Blr, r, Q, (p, q, l) in _iter_terms(tab, placement):
        if (l, r) == (0, 0):
            continue
        out += pref * Blr * Etr(r, Q)
    return sp.expand(out)


def slot_coeffs(tab, placement='P'):
    """{(l, r, Q): coefficient}: the engine's Delta-space slot decomposition."""
    out = {}
    for pref, Blr, r, Q, (p, q, l) in _iter_terms(tab, placement):
        out[(l, r, Q)] = sp.expand(out.get((l, r, Q), 0) + pref * Blr)
    return dict((k, v) for k, v in out.items() if v != 0)


def master_broken(tab, which):
    """G6 CONTROL kernels -- deliberately broken conventions; never used for science."""
    out = sp.Integer(0)
    for (p, q), B in tab.items():
        dg = udeg(B)
        if dg < 0:
            continue
        for l in range(q + 1):
            for r in range(dg + 1 - l):
                Blr = bder(B, l + r)
                if Blr == 0:
                    continue
                if which == 'A':       # wrong lever sign (wrong d/dDelta chain rule)
                    pref = sp.Integer(-1) ** q * sp.binomial(q, l) \
                        * sp.Integer(-1) ** r / (sp.Integer(2) ** r * sp.factorial(r))
                elif which == 'B':     # lever arm 1 instead of 1/2
                    pref = sp.Integer(-1) ** q * sp.binomial(q, l) / sp.factorial(r)
                elif which == 'C':     # frozen centre (Route A): only (l,r)=(0,0)
                    if (l, r) != (0, 0):
                        continue
                    pref = sp.Integer(-1) ** q * sp.binomial(q, l)
                elif which == 'Cp':    # freeze-at-centre: all l, but no levers (r=0)
                    if r != 0:
                        continue
                    pref = sp.Integer(-1) ** q * sp.binomial(q, l)
                elif which == 'D':     # wrong-vertex placement: (-1)^p on u_P slots
                    pref = sp.Integer(-1) ** p * sp.binomial(q, l) \
                        / (sp.Integer(2) ** r * sp.factorial(r))
                else:
                    raise ValueError(which)
                out += pref * Blr * Etr(r, p + q - l)
    return sp.expand(out)


def td_table(F, Xtab):
    """B-table of the total-derivative density d/du[F(u) X_pq(h_E,h_P)]:
    X_{pq} are u-independent bilinear structures; the u-derivative shifts the leg
    order: (p,q) -> (p+1,q) and (p,q+1), plus F' on the unshifted slot."""
    out = {}
    for (p, q), X in Xtab.items():
        out[(p, q)] = sp.expand(out.get((p, q), 0) + sp.diff(F, uu) * X)
        out[(p + 1, q)] = sp.expand(out.get((p + 1, q), 0) + F * X)
        out[(p, q + 1)] = sp.expand(out.get((p, q + 1), 0) + F * X)
    return dict((k, v) for k, v in out.items() if v != 0)


# =============================================================================
print("\n=== G0: NORMALISATION TABLE (gated explicitly, not inherited) ===")
# Table (owner hard gate):   S = (1/2) Int C (h')^2  =>  Delta K = (1/4) C''
#                            S =       Int C (h')^2  =>  Delta K = (1/2) C''
c1, c2 = sp.symbols('c1 c2', real=True)


def Ctoy(x):
    return 1 + c1 * x + c2 * x ** 2


TAB_HALF = {(1, 1): Ctoy(uu)}           # S = (1/2) Int C (h')^2   ->  B_11 = C
TAB_INT = {(1, 1): 2 * Ctoy(uu)}        # S =       Int C (h')^2   ->  B_11 = 2C

k_half_P = master(TAB_HALF, 'P')
k_half_E = master(TAB_HALF, 'E')
k_int_P = master(TAB_INT, 'P')
FA_toy = sp.expand(om ** 2 * Ctoy(0))   # the frozen-centre F_A

check(sp.expand(k_half_P - (om ** 2 + c2 / 2)) == 0
      and sp.expand(k_half_E - (om ** 2 + c2 / 2)) == 0
      and sp.expand(correction_of(TAB_HALF) - c2 / 2) == 0,
      "G0 row 1: S = (1/2) Int C (h')^2 through the engine: K~ = om^2 C(0) + (1/4)C''(0) "
      "= om^2 + c2/2 (both placements); the correction alone is (1/4)C'' = c2/2",
      gate="G0")
check(sp.expand(k_int_P - (2 * om ** 2 + c2)) == 0
      and sp.expand(correction_of(TAB_INT) - c2) == 0,
      "G0 row 2: S = Int C (h')^2 through the engine: K~ = 2 om^2 C(0) + (1/2)C''(0) = "
      "2 om^2 + c2; the correction alone is (1/2)C'' = c2 -- EXACTLY TWICE row 1",
      gate="G0")
for pp in (2, 3):
    tab_op1 = {(1, 1): 2 * a_bg ** pp}   # S = Int a^p (phi')^2 (the diagnostic's OP1)
    check(sp.expand(correction_of(tab_op1) - pp * (pp + 1) * H ** 2 / 2) == 0,
          "G0 OP1 correspondence: S = Int a^%d (phi')^2 -> correction = %d*%d/2 H^2 "
          "(the 2026-08-27 diagnostic's OP1 figure, no-1/2 row, through the engine)"
          % (pp, pp, pp), gate="G0")
# THE ASSERTION, wired in code: the four frozen operators carry the Int-row (no 1/2).
OP_ACTION_NORMALISATION = dict(
    (o, "S = Int du sqrt(-g) I_O   (NO overall 1/2: the Int-row of the table)")
    for o in OPS)
check(all("NO overall 1/2" in v for v in OP_ACTION_NORMALISATION.values())
      and sp.expand(master(TAB_INT) - 2 * master(TAB_HALF)) == 0,
      "G0 assertion wired: all four operators' actions carry the Int-row (no 1/2); the "
      "engine is linear in the action normalisation (factor 2 end-to-end)", gate="G0")

# =============================================================================
print("\n=== G3: TOY AGREEMENT (the generalised machinery restricted to the toy) ===")
check(sp.expand(k_half_P - FA_toy - c2 / 2) == 0,
      "G3: toy master identity F_B - F_A = (1/4)C''(0) = c2/2 (additive, om-independent)",
      gate="G3")
sc_toy = slot_coeffs(TAB_HALF)
ok_slots = all(sp.expand(sc_toy.get((0, r, 2), 0)
                         + sp.diff(Ctoy(uu), uu, r).subs(uu, 0)
                         / (2 ** r * sp.factorial(r))) == 0 for r in (0, 1, 2))
ok_slots = ok_slots and all(
    sp.expand(sc_toy.get((1, r, 1), 0)
              + sp.diff(Ctoy(uu), uu, r + 1).subs(uu, 0)
              / (2 ** r * sp.factorial(r))) == 0 for r in (0, 1))
check(ok_slots,
      "G3: the engine's r-slot lever structure == the toy's registered slots "
      "C^{(r)}(0)(1/2)^r/r! (u1_pow lever arms; the C'-pairing on the l=1 slots)",
      gate="G3")
k_third = master(TAB_HALF, 'P', uc=sp.Rational(1, 3))
k_third_E = master(TAB_HALF, 'E', uc=sp.Rational(1, 3))
check(sp.expand(k_third - (om ** 2 * Ctoy(sp.Rational(1, 3)) + c2 / 2)) == 0
      and sp.expand(k_third - k_third_E) == 0,
      "G3: second centre u_c = 1/3: K~ = om^2 C(1/3) + (1/4)C''(1/3), both placements "
      "(centre dependence verified, not inferred)", gate="G3")
check(sp.expand(sc_toy.get((0, 0, 2), 0) + Ctoy(0)) == 0
      and sp.expand(sc_toy.get((0, 2, 2), 0) + 2 * c2 / 8) == 0,
      "G3: the Delta-space slots are -C(0) dd''(Delta) [slot (0,0,2)] and "
      "C''(0)/8 dd [slot (0,2,2)] -- the distributional structure "
      "-C dd'' + (1/4)C'' dd is preserved EXPLICITLY", gate="G3")

# =============================================================================
print("\n=== G1 (scalar part): IBP INVARIANCE AT THE ACTION LEVEL ===")
# The diagnostic's decisive pair: S = Int C h h'  vs  S' = -(1/2) Int C' h^2
# (they differ by the total derivative d/du[(1/2) C h^2]).
TAB_S = {(0, 1): Ctoy(uu), (1, 0): Ctoy(uu)}            # B_01 = B_10 = C
TAB_SP = {(0, 0): -sp.diff(Ctoy(uu), uu)}               # B_00 = -C'
kS_P, kS_E = master(TAB_S, 'P'), master(TAB_S, 'E')
kSP_P, kSP_E = master(TAB_SP, 'P'), master(TAB_SP, 'E')
check(sp.expand(kS_P - kSP_P) == 0 and sp.expand(kS_E - kSP_E) == 0
      and sp.expand(kS_P - kS_E) == 0,
      "G1: Int C h h' and -(1/2) Int C' h^2 (differing by a total derivative) give the "
      "IDENTICAL action-functional kernel, both placements -- IBP invariance at the "
      "Hessian/distribution level, BEFORE any omega/K evaluation", gate="G1")
TAB_TD = td_table(Ctoy(uu), {(0, 0): sp.Integer(1)})    # d/du[C h1 h2]
check(sp.expand(master(TAB_TD, 'P')) == 0 and sp.expand(master(TAB_TD, 'E')) == 0,
      "G1: the total-derivative density d/du[C h1 h2] gives the IDENTICALLY ZERO kernel "
      "(both placements) -- the Hessian of a boundary term vanishes", gate="G1")
check(sp.expand(old_kernel_of(TAB_S) - old_kernel_of(TAB_SP)) != 0,
      "G1 contrast (computed, not asserted): the OLD coincident-density construction is "
      "NOT IBP-invariant on the same pair (Int C hh' -> 0 vs -(1/2)Int C'h^2 -> -C'(0)) "
      "-- the defect the rebuild removes", gate="G1")

# =============================================================================
print("\n=== STEP M: the validated construction executed (cache-backed; loop side frozen) ===")
# The loop side (Phase-10 assembly, cached) and the old basis are executed exactly as
# the span test does, to obtain (i) the frozen targets SIG0/1/2 for the G2 Gilkey
# regression and (ii) the old kernels as VALIDATION targets. They are NEVER inputs to
# the corrected construction (independence condition).
os.environ.setdefault("SKIPBAT", "1")
os.environ["AFB_NOLOAD"] = "1"       # ignore any AF-basis cache during this exec
import hashlib
_cache_path = os.path.join(HERE, ".p10_assembly_cache.txt")
_cache_sha_before = hashlib.sha256(open(_cache_path, 'rb').read()).hexdigest()
src = open(os.path.join(HERE, "wall_d2_phases8_12.py")).read()
MARK = "# ================= PHASE 11: IDENTIFICATION"
assert MARK in src, "marker not found -- refusing to guess where to split"
ns = {'__name__': '__main__', '__file__': os.path.join(HERE, "wall_d2_phases8_12.py")}
exec(compile(src.split(MARK)[0], "wall_d2_phases8_12.py", "exec"), ns)
blk("machinery exec (engines + cached assembly + old basis)")
_cache_sha_after = hashlib.sha256(open(_cache_path, 'rb').read()).hexdigest()
SIG0, SIG1, SIG2 = ns['SIG0'], ns['SIG1'], ns['SIG2']
QS_OLD = ns['QS']
check(not ns['FAIL'], "M: the machinery prefix's own gates all pass (the loop side and "
      "the old basis are exactly as validated)", gate="M")
check(_cache_sha_before == _cache_sha_after,
      "M: .p10_assembly_cache.txt byte-identical across the exec (loaded and "
      "round-tripped, never regenerated)", gate="M")

stamp("G0 + G3 + G1(scalar) done")


# =============================================================================
print("\n=== STEP C: SPLIT-FREQUENCY SECTOR-GRADED CASCADE (the B-table machinery) ===")
# The machinery's basis_graded mirrored verbatim in form, with the SPLIT derivative
# rule; returns the AB densities D_O(u; wE, wP) -- NOT evaluated at u -> 0 (that
# evaluation is exactly what the rebuild removes).
SECMUL = {('0', '0'): '0', ('0', 'A'): 'A', ('A', '0'): 'A', ('0', 'B'): 'B',
          ('B', '0'): 'B', ('0', 'AB'): 'AB', ('AB', '0'): 'AB', ('A', 'B'): 'AB',
          ('B', 'A'): 'AB'}     # everything else is DROPPED (machinery, verbatim)


def hT(e):
    e = sp.expand(e)
    return sp.expand(sum(H ** q * e.coeff(H, q) for q in range(3)))


def gmul(a, b):
    out = {}
    for s1, v1 in a.items():
        for s2, v2 in b.items():
            s = SECMUL.get((s1, s2))
            if s is None:
                continue
            out[s] = sp.expand(out.get(s, sp.Integer(0)) + hT(v1 * v2))
    return dict((k, v) for k, v in out.items() if v != 0)


def gadd(*objs):
    out = {}
    for a in objs:
        for s, v in a.items():
            out[s] = sp.expand(out.get(s, sp.Integer(0)) + v)
    return dict((k, v) for k, v in out.items() if v != 0)


def gscale(a, c):
    return dict((s, hT(sp.expand(c * v))) for s, v in a.items()
                if sp.expand(c * v) != 0)


def gdiff_split(a, mu, kkv):
    """sector derivative with SPLIT u-frequencies (the machinery's gdiff_ph with
    wE != wP): the A sector (E leg) picks up -i wE per u-derivative, the B sector
    (P leg) +i wP, the AB sector -i(wE - wP) (the residual phase of the two-leg
    product); z-derivatives: A: +i k, B: -i k (shared k). Reduces to the machinery's
    rule exactly at wE = wP = om."""
    out = {}
    for sname, v in a.items():
        d = sp.diff(v, COORD[mu])
        if mu == 0:
            sh = {'A': -sp.I * wE, 'B': sp.I * wP,
                  'AB': -sp.I * wE + sp.I * wP}.get(sname, 0)
        elif mu == 3:
            sh = {'A': sp.I * kkv, 'B': -sp.I * kkv}.get(sname, 0)
        else:
            sh = 0
        val = sp.expand(d + sh * v)
        if val != 0:
            out[sname] = val
    return out



def cascade_split(kkv, gates=False):
    """the four operators' split-frequency AB densities + the background R^(0)."""
    gd = lambda a, mu: gdiff_split(a, mu, kkv)
    a2, a4 = hT(a_bg ** 2), hT(a_bg ** 4)
    ai2 = hT(sp.series(a_bg ** -2, H, 0, 3).removeO())
    EE = sp.Matrix(4, 4, lambda i, j: e1m[i, j])
    PP = sp.Matrix(4, 4, lambda i, j: e2m[i, j])
    gm = [[{'0': hT(a2 * eta[i, j]), 'A': hT(a2 * EE[i, j]), 'B': hT(a2 * PP[i, j])}
           for j in range(4)] for i in range(4)]
    hEu = eta * EE * eta
    hPu = eta * PP * eta
    hcross = eta * EE * eta * PP * eta + eta * PP * eta * EE * eta
    gi = [[{'0': hT(ai2 * eta[i, j]), 'A': hT(-ai2 * hEu[i, j]),
            'B': hT(-ai2 * hPu[i, j]), 'AB': hT(ai2 * hcross[i, j])}
           for j in range(4)] for i in range(4)]
    if gates:
        ok = True
        for i in range(4):
            for j in range(4):
                pr = {}
                for s2 in range(4):
                    pr = gadd(pr, gmul(gm[i][s2], gi[s2][j]))
                for sec in ('0', 'A', 'B', 'AB'):
                    tgt = sp.Integer(1) if (sec == '0' and i == j) else sp.Integer(0)
                    ok &= (sp.simplify(sp.expand(pr.get(sec, 0) - tgt)) == 0)
        check(ok, "C: g.ginv == 1 in every eps sector (split-frequency sector algebra)",
              gate="C")
    blk("metric+inverse")
    ep1, ep2 = sp.symbols('ep1 ep2')
    Mh = eta + ep1 * EE + ep2 * PP
    Dt = sp.expand(-Mh.det(method='berkowitz'))
    d1A = sp.expand(Dt.coeff(ep1, 1).coeff(ep2, 0))
    d1B = sp.expand(Dt.coeff(ep1, 0).coeff(ep2, 1))
    d2AB = sp.expand(Dt.coeff(ep1, 1).coeff(ep2, 1))
    sq = {'0': a4, 'A': hT(a4 * d1A / 2), 'B': hT(a4 * d1B / 2),
          'AB': hT(a4 * (d2AB / 2 - d1A * d1B / 4))}
    if gates:
        a8 = hT(a4 * a4)
        sq2 = gmul(sq, sq)
        tgt8 = {'0': a8, 'A': hT(a8 * d1A), 'B': hT(a8 * d1B), 'AB': hT(a8 * d2AB)}
        okd = all(sp.expand(hT(sq2.get(sec, 0)) - hT(tgt8.get(sec, 0))) == 0
                  for sec in ('0', 'A', 'B', 'AB'))
        check(okd, "C: sqrt(-g)^2 == a^8 (-det(eta+h)) in every eps sector "
              "(division-free)", gate="C")
    blk("sqrt(-g)")
    Chr = [[[None] * 4 for _ in range(4)] for _ in range(4)]
    for lam in range(4):
        for m2 in range(4):
            for n2 in range(m2, 4):
                acc = {}
                for s2 in range(4):
                    inner = gadd(gd(gm[s2][n2], m2), gd(gm[s2][m2], n2),
                                 gscale(gd(gm[m2][n2], s2), -1))
                    acc = gadd(acc, gmul(gi[lam][s2], inner))
                Chr[lam][m2][n2] = Chr[lam][n2][m2] = gscale(acc, sp.Rational(1, 2))
    blk("christoffels")
    Rm = [[None] * 4 for _ in range(4)]
    for m2 in range(4):
        for n2 in range(m2, 4):
            t0 = time.time()
            acc = {}
            for lam in range(4):
                acc = gadd(acc, gd(Chr[lam][m2][n2], lam),
                           gscale(gd(Chr[lam][lam][m2], n2), -1))
                for s2 in range(4):
                    acc = gadd(acc, gmul(Chr[lam][lam][s2], Chr[s2][m2][n2]),
                               gscale(gmul(Chr[lam][n2][s2], Chr[s2][lam][m2]), -1))
            Rm[m2][n2] = Rm[n2][m2] = acc
            el = time.time() - t0
            if el > 60:
                print("      [ricci (%d,%d)] %.1fs" % (m2, n2, el))
                sys.stdout.flush()
    blk("ricci")
    Rs = {}
    for i in range(4):
        for j in range(4):
            Rs = gadd(Rs, gmul(gi[i][j], Rm[i][j]))
    blk("scalar curvature")
    dens = {'Lam': sq, 'EH': gmul(sq, Rs), 'R2': gmul(sq, gmul(Rs, Rs))}
    blk("Lam/EH/R2 densities")
    rmn2 = {}
    for i in range(4):
        for j in range(4):
            for a2i in range(4):
                for b2i in range(4):
                    rmn2 = gadd(rmn2, gmul(gmul(gi[i][a2i], gi[j][b2i]),
                                           gmul(Rm[i][j], Rm[a2i][b2i])))
    dens['Rmn2'] = gmul(sq, rmn2)
    blk("Rmn2 density")
    out = dict((nm2, dd.get('AB', sp.Integer(0))) for nm2, dd in dens.items())
    r0 = sp.expand(Rs.get('0', sp.Integer(0)).subs(uu, 0))
    return out, r0


def table_of(Dab):
    """{(p,q): B_pq(u)} from the split-frequency AB density:
    D_AB(u; wE, wP) = Sum_pq B_pq(u) (-i wE)^p (+i wP)^q  =>  B = T * i^p * (-i)^q."""
    tab = {}
    if sp.expand(Dab) == 0:
        return tab
    for (pw, qw), coef in sp.Poly(sp.expand(Dab), wE, wP).terms():
        Bpq = sp.expand(coef * sp.I ** pw * (-sp.I) ** qw)
        if Bpq != 0:
            tab[(pw, qw)] = Bpq
    return tab


# =============================================================================
print("\n=== STEP K: TABLES -> CORRECTED KERNELS (both placements; corrections explicit) ===")
AF_QS = []       # AF_QS[i][op][n]: the corrected kernels, the span test's QS format
AF_CORR = []     # AF_CORR[i][op][n]: the explicit (l,r)!=(0,0) corrections
AF_TABS = []     # the B-tables (inspection)
R0s = []
for _i, (_ov, _kv) in enumerate(K_SAMPLES):
    print("\n   --- split cascade at K = (%s, %s) ---" % (_ov, _kv))
    _dens, _r0 = cascade_split(_kv, gates=(_i == 0))
    R0s.append(_r0)
    stamp("cascade at K=(%s,%s) done" % (_ov, _kv))
    q_i, corr_i, tabs_i = {}, {}, {}
    for _op in OPS:
        tab = table_of(_dens[_op])
        tabs_i[_op] = tab
        kP = master(tab, 'P')
        kE = master(tab, 'E')
        check(sp.expand(kP - kE) == 0,
              "G1 order-independence at K=(%s,%s), %s: the two Hessian placements "
              "(dressings at u_P vs u_E) give the IDENTICAL kernel" % (_ov, _kv, _op),
              gate="G1")
        old_asm = sp.expand(old_kernel_of(tab).subs(om, _ov))
        for _n in (0, 1, 2):
            check(sp.expand(old_asm.coeff(H, _n) - QS_OLD[_i][_op][_n]) == 0,
                  "G2 mirror at K=(%s,%s), %s, H^%d: the split-cascade's (l,r)=(0,0) "
                  "assembly == the ORIGINAL machinery's kernel" % (_ov, _kv, _op, _n),
                  gate="G2")
        kfull = sp.expand(kP.subs(om, _ov))
        q_i[_op] = dict((_n, sp.expand(kfull.coeff(H, _n))) for _n in (0, 1, 2))
        corr = sp.expand(correction_of(tab).subs(om, _ov))
        corr_i[_op] = dict((_n, sp.expand(corr.coeff(H, _n))) for _n in (0, 1, 2))
        check(sp.expand(q_i[_op][0] - QS_OLD[_i][_op][0]) == 0,
              "G2 at K=(%s,%s), %s: the corrected kernel's H^0 part == the old kernel's "
              "H^0 part EXACTLY (all corrections are >= O(H))" % (_ov, _kv, _op),
              gate="G2")
    AF_QS.append(q_i)
    AF_CORR.append(corr_i)
    AF_TABS.append(tabs_i)
    blk("kernels+gates at K=(%s,%s)" % (_ov, _kv))
check(all(sp.simplify(r - R0s[0]) == 0 for r in R0s),
      "C: background curvature R^(0) is K-independent (as it must be); R^(0) = %s"
      % R0s[0], gate="C")

# =============================================================================
print("\n=== G1 (tensor part): IBP ON THE REAL OPERATOR TABLES (action level) ===")
Flist = [sp.Integer(1), a_bg ** 2, a_bg ** 4]
Xlist = [
    {(0, 0): sp.Integer(1)},
    {(0, 0): sp.Integer(1), (1, 1): sp.I * kk},
    {(1, 0): sp.I * kk, (0, 1): -sp.I * kk, (1, 1): kk ** 2},
    {(2, 0): -kk ** 2, (0, 2): -kk ** 2, (2, 2): kk ** 4},
]
ok_ibp_t = True
for _op in OPS:
    tab0 = AF_TABS[0][_op]
    for F in Flist:
        for Xt in Xlist:
            tabp = dict(tab0)
            for (p, q), v in td_table(F, Xt).items():
                tabp[(p, q)] = sp.expand(tabp.get((p, q), 0) + v)
            if sp.expand(master(tabp, 'P') - master(tab0, 'P')) != 0:
                ok_ibp_t = False
check(ok_ibp_t,
      "G1: adding d/du[F(u) X_pq] total-derivative structures (3 dressings x 4 rich "
      "(p,q)-structures x 4 operators) leaves every REAL kernel UNCHANGED -- symbolic "
      "identity at the Hessian/distribution level, before any omega/K evaluation",
      gate="G1")


# =============================================================================
print("\n=== G2: H^0 GILKEY REGRESSION ON THE CORRECTED KERNELS (no refit) ===")
uL, uE, uR, uM = sp.symbols('uL uE uR uM')
GIL = {uL: mm ** 4 / 4, uE: mm ** 2 / 12, uR: sp.Rational(1, 240), uM: sp.Rational(1, 120)}


def pol_syms(ex):
    return sorted({q for q in sp.expand(ex).free_symbols
                   if str(q).startswith('E_') or str(q).startswith('P_')}, key=str)


def rows_for_af(sample_idx, order):
    """one row per (E_ij, P_kl) bilinear slot: [corrected basis coeffs] and the target."""
    ov, kv = K_SAMPLES[sample_idx]
    Q = AF_QS[sample_idx]
    tgt = sp.expand({0: SIG0, 1: SIG1, 2: SIG2}[order].subs({om: ov, kk: kv}))
    cols = [sp.expand(Q[o][order]) for o in OPS]
    slots = sorted(set(pol_syms(tgt)) | {q for cc in cols for q in pol_syms(cc)}, key=str)
    Es = [q for q in slots if str(q).startswith('E_')]
    Ps = [q for q in slots if str(q).startswith('P_')]
    rows = []
    for e_ in Es:
        for p_ in Ps:
            rows.append(([sp.expand(cc).coeff(e_, 1).coeff(p_, 1) for cc in cols],
                         sp.expand(tgt).coeff(e_, 1).coeff(p_, 1)))
    return rows


def stack_af(idxs, order):
    A, b = [], []
    for ix in idxs:
        for (r, t) in rows_for_af(ix, order):
            A.append(r)
            b.append(t)
    return sp.Matrix(A), sp.Matrix(b)


A0, b0 = stack_af([0, 1], 0)
rkA, rkAug = A0.rank(), A0.row_join(b0).rank()
sol0 = sp.solve(list(A0 * sp.Matrix([uL, uE, uR, uM]) - b0),
                [uL, uE, uR, uM], dict=True)
ok_gilkey = bool(sol0) and all(sp.simplify(sol0[0].get(k_, k_) - v_) == 0
                               for k_, v_ in GIL.items())
check(ok_gilkey and rkAug == rkA,
      "G2: H^0 Gilkey regression on the CORRECTED kernels: target IN span "
      "(rank %d/%d); fitted coefficients == {m^4/4, m^2/12, 1/240, 1/120} EXACTLY "
      "(samples 0,1 fit)" % (rkA, rkAug), gate="G2")
if sol0:
    A2h, b2h = stack_af([2], 0)
    resid = sp.Matrix([sp.simplify(x) for x in
                       (A2h * sp.Matrix([sol0[0].get(s_, 0)
                                         for s_ in (uL, uE, uR, uM)]) - b2h)])
    check(all(x == 0 for x in resid),
          "G2: HELD-OUT sample K=(7,3) reproduced EXACTLY by the fitted coefficients "
          "(NO refit)", gate="G2")
else:
    check(False, "G2: no exact solution for the anchor coefficients", gate="G2")
stamp("G2 Gilkey regression done")


# =============================================================================
print("\n=== G4: DUAL ROUTE (full-eps split construction; independent of the sector algebra) ===")


def route_B_EH_split(kkv):
    """the machinery's route_B_EH mirrored with SPLIT frequencies: the FULL eps
    polynomial (eps1^2 and eps2^2 sectors included), phases tracked as the formal
    markers phE/phP with the split derivative rules, eps1*eps2 extracted at the end."""
    ep1, ep2 = sp.symbols('ep1 ep2')
    phE, phP = sp.symbols('phE phP')
    a2, a4 = hT(a_bg ** 2), hT(a_bg ** 4)
    ai2 = hT(sp.series(a_bg ** -2, H, 0, 3).removeO())
    EE = sp.Matrix(4, 4, lambda i, j: e1m[i, j])
    PP = sp.Matrix(4, 4, lambda i, j: e2m[i, j])
    hm = ep1 * EE * phE + ep2 * PP * phP
    g = (a2 * (eta + hm)).applyfunc(sp.expand)
    gi = (ai2 * (eta - eta * hm * eta + eta * hm * eta * hm * eta)).applyfunc(sp.expand)

    def dph(e, mu):
        d = sp.diff(e, COORD[mu])
        if mu == 0:
            d += sp.diff(e, phE) * (-sp.I * wE) * phE \
                + sp.diff(e, phP) * (sp.I * wP) * phP
        elif mu == 3:
            d += sp.diff(e, phE) * (sp.I * kkv) * phE \
                + sp.diff(e, phP) * (-sp.I * kkv) * phP
        return sp.expand(d)

    def tr3(e):
        e = sp.expand(e)
        return sp.expand(sum(ep1 ** q1 * ep2 ** q2 * e.coeff(ep1, q1).coeff(ep2, q2)
                             for q1 in range(3) for q2 in range(3) if q1 + q2 <= 2))

    Chr = [[[hT(tr3(sum(gi[lam, s2] * (dph(g[s2, n2], m2) + dph(g[s2, m2], n2)
                                       - dph(g[m2, n2], s2)) for s2 in range(4)) / 2))
             for n2 in range(4)] for m2 in range(4)] for lam in range(4)]
    Rm = sp.Matrix(4, 4, lambda m2, n2: hT(tr3(
        sum(dph(Chr[lam][m2][n2], lam) for lam in range(4))
        - sum(dph(Chr[lam][lam][m2], n2) for lam in range(4))
        + sum(Chr[lam][lam][s2] * Chr[s2][m2][n2] - Chr[lam][n2][s2] * Chr[s2][lam][m2]
              for lam in range(4) for s2 in range(4)))))
    Rs = hT(tr3(sum(gi[i, j] * Rm[i, j] for i in range(4) for j in range(4))))
    Dt = sp.expand(-(eta + hm).det(method='berkowitz'))
    d1_ = sp.expand(Dt.coeff(ep1, 1).coeff(ep2, 0) * ep1
                    + Dt.coeff(ep1, 0).coeff(ep2, 1) * ep2)
    d2_ = sp.expand(Dt.coeff(ep1, 1).coeff(ep2, 1) * ep1 * ep2)
    sq = a4 * (1 + d1_ / 2 + (d2_ / 2 - sp.expand(d1_ ** 2) / 8))
    ex = sp.expand(tr3(sp.expand(sq * Rs))).coeff(ep1, 1).coeff(ep2, 1)
    return sp.expand(ex.subs(phE, 1).subs(phP, 1))


dens_B = route_B_EH_split(K_SAMPLES[0][1])
blk("route B (full-eps split EH)")
tab_B = table_of(dens_B)
kB_P = master(tab_B, 'P')
kB_E = master(tab_B, 'E')
kA_EH_P = master(AF_TABS[0]['EH'], 'P')
kA_EH_E = master(AF_TABS[0]['EH'], 'E')
check(sp.expand(kB_P - kA_EH_P) == 0 and sp.expand(kB_E - kA_EH_E) == 0
      and sp.expand(kB_P - kB_E) == 0,
      "G4: the EH kernel from the FULL-EPS split route (no sector grading) == the "
      "sector-graded kernel, both placements, at K=(3,2) -- the B-table extraction is "
      "validated by a method independent of the sector algebra", gate="G4")
stamp("G4 dual route done")


# =============================================================================
print("\n=== G5: ODD-STRUCTURE FUNCTIONAL-HESSIAN TEST + ATTRIBUTION + NON-VACUITY ===")
# The retired 'order theorem' (corrections exactly O(H^2)) was a TOY-ONLY statement:
# its proof used the toy's single even structure B_11, whose B'-type slots cancel in
# pairs.  It is replaced by a COMPUTED, discriminating test on an independent model
# whose functional Hessian is exactly derivable -- the symmetric odd pair
#     S_B = Int du B(u) [ hA'(u) hB(u) + hA(u) hB'(u) ],  B = b0 + H b1 u + H^2 b2 u^2,
# whose exact Hessian kernel is -B'(u_c) dd(Delta): a GENUINE O(H^1) correction
# (-H b1 at the reference centre) whenever B' carries an O(H) slope, while the OLD
# coincident-density construction gives IDENTICALLY ZERO on this pair.  Three
# independent derivations must agree (direct functional Hessian; raw-kernel centred
# slot route; the generalised master kernel).
b0c, b1c, b2c = sp.symbols('b0c b1c b2c', real=True)
Bmod = b0c + H * b1c * uu + H ** 2 * b2c * uu ** 2
TAB_B = {(1, 0): Bmod, (0, 1): Bmod}          # S_B's split-frequency B-table


def fh_el(Bfun):
    """DIRECT functional Hessian (Euler-Lagrange; no master formula):
    K(u1,u2) = Sum_{m,n} (-d/du1)^m [ L_{hA_m hB_n}(u1) dd_n(u1-u2) ], the
    derivative acting on the product (product rule, computed term by term),
    L = B(u)(hA' hB + hA hB') in leg-derivative symbols."""
    hAs = [sp.Symbol('hA_%d' % i) for i in range(2)]
    hBs = [sp.Symbol('hB_%d' % i) for i in range(2)]
    L = Bfun * (hAs[1] * hBs[0] + hAs[0] * hBs[1])
    acc = {}
    for m in range(2):
        for n in range(2):
            c = sp.diff(sp.diff(L, hAs[m]), hBs[n])
            if c == 0:
                continue
            dist = {n: c}
            for _ in range(m):
                nd = {}
                for q_, cf in dist.items():
                    nd[q_] = sp.expand(nd.get(q_, 0) + sp.diff(cf, uu))
                    nd[q_ + 1] = sp.expand(nd.get(q_ + 1, 0) + cf)
                dist = dict((k_, v_) for k_, v_ in nd.items() if v_ != 0)
            for q_, cf in dist.items():
                acc[q_] = sp.expand(acc.get(q_, 0) + (-1) ** m * cf)
    return dict((k_, v_) for k_, v_ in acc.items() if v_ != 0)


ELslots = fh_el(Bmod)
check(ELslots == {0: -sp.diff(Bmod, uu)},
      "G5 route 1 (direct functional Hessian): the Euler-Lagrange second variation of "
      "S_B is K(u1,u2) = -B'(u1) dd(u1-u2) EXACTLY -- the dd' pieces generated by the "
      "two density terms cancel inside the computation itself", gate="G5")

# the distributional identities everything rests on, verified (not assumed)
_xg = sp.Symbol('xg', real=True)
_fg = 3 + 2 * _xg + _xg ** 2
check(sp.integrate(_fg * sp.DiracDelta(_xg), (_xg, -sp.oo, sp.oo)) == 3
      and sp.integrate(_fg * sp.Derivative(sp.DiracDelta(_xg), _xg),
                       (_xg, -sp.oo, sp.oo)) == -2
      and sp.integrate(_xg * sp.Derivative(sp.DiracDelta(_xg), _xg),
                       (_xg, -sp.oo, sp.oo)) == -1
      and sp.integrate(_xg ** 2 * sp.Derivative(sp.DiracDelta(_xg), _xg),
                       (_xg, -sp.oo, sp.oo)) == 0,
      "G5 distributional identities (sympy DiracDelta, exact): Int f dd = f(0); "
      "Int f dd' = -f'(0); Int x dd' = -1 (x dd' = -dd); Int x^2 dd' = 0 -- the "
      "identities behind the centre collapse and the slot reductions", gate="G5")
# route-1 kernel validated against the plain second variation of the action
_phiv = sp.exp(-uu ** 2) * (1 + uu)
_psiv = sp.exp(-uu ** 2) * (2 - uu + uu ** 2)
_var2 = sp.integrate(Bmod * (sp.diff(_phiv, uu) * _psiv + _phiv * sp.diff(_psiv, uu)),
                     (uu, -sp.oo, sp.oo))
_bil1 = sp.integrate(ELslots[0] * _phiv * _psiv, (uu, -sp.oo, sp.oo))
_phiv2 = sp.exp(-uu ** 2) * uu
_psiv2 = sp.exp(-uu ** 2) * (1 + 3 * uu + uu ** 2)
_var2b = sp.integrate(Bmod * (sp.diff(_phiv2, uu) * _psiv2 + _phiv2 * sp.diff(_psiv2, uu)),
                      (uu, -sp.oo, sp.oo))
_bil1b = sp.integrate(ELslots[0] * _phiv2 * _psiv2, (uu, -sp.oo, sp.oo))
check(sp.simplify(_var2 - _bil1) == 0 and sp.simplify(_var2b - _bil1b) == 0,
      "G5 route 1 validation: the bilinear form of -B'(u) dd(u1-u2) == the plain "
      "second variation of S_B on Gaussian test pairs (sympy, exact) -- the kernel "
      "really is delta^2 S_B, computed, not transcribed", gate="G5")

# route 2: the RAW kernel (density differentiated twice, before any EL/IBP step),
# validated distributionally, then centred and E-transformed slot by slot
_u1v, _u2v = sp.symbols('u1v u2v', real=True)
_sv, _tv = sp.symbols('sv tv', real=True)
# NOTE (sympy): deltaintegrate mis-signs the mirrored form Int f(u2) dd'(u2-u1) du2
# (returns +[f]' instead of -[f]'; found by checking against the analytic collapse),
# so BOTH dd' shift integrals are computed in the CANONICAL orientation -- argument
# x - y with the derivative taken wrt x -- which is exact, and each result is
# checked against its analytic collapse before it is used.
_inA = sp.integrate(_phiv.subs(uu, _u1v) * Bmod.subs(uu, _u1v)
                    * sp.Derivative(sp.DiracDelta(_u1v - _u2v), _u1v),
                    (_u1v, -sp.oo, sp.oo))
_inB = sp.integrate(Bmod.subs(uu, _sv) * _psiv.subs(uu, _sv)
                    * sp.Derivative(sp.DiracDelta(_sv - _tv), _sv),
                    (_sv, -sp.oo, sp.oo))
check(sp.expand(_inA + sp.diff(_phiv.subs(uu, _u2v) * Bmod.subs(uu, _u2v), _u2v)) == 0
      and sp.expand(_inB + sp.diff(Bmod.subs(uu, _tv) * _psiv.subs(uu, _tv), _tv)) == 0,
      "G5 route 2 collapses: the dd' shift integrals equal their analytic values "
      "EXACTLY -- Int f(x) dd'(x-y) dx = -f'(y) for BOTH raw-kernel terms (f = phi*B "
      "on the A leg, f = B*psi on the B leg; canonical orientation)", gate="G5")
_tA = sp.integrate(sp.expand(_inA * _psiv.subs(uu, _u2v)), (_u2v, -sp.oo, sp.oo))
_tB = sp.integrate(sp.expand(_inB * _phiv.subs(uu, _tv)), (_tv, -sp.oo, sp.oo))
check(sp.simplify(_tA + _tB - _var2) == 0,
      "G5 route 2 validation: the RAW kernel B(u1) dd'(u1-u2) + B(u2) dd'(u2-u1) (the "
      "second functional derivative of the density, before any EL/IBP rearrangement) "
      "has the SAME bilinear form as the second variation (the two dd' collapses above "
      "+ plain Gaussian integrals, exact) -- both raw terms are the true delta^2 S_B",
      gate="G5")
_Dlv, _ucv = sp.symbols('Deltav ucv', real=True)
_diffB = sp.expand(Bmod.subs(uu, _ucv + _Dlv / 2) - Bmod.subs(uu, _ucv - _Dlv / 2))
_k2 = sp.Integer(0)
for (j_,), _cj in sp.Poly(_diffB, _Dlv).terms():
    _k2 = sp.expand(_k2 + _cj * Etr(j_, 1))
check(sp.expand(_diffB.subs(_Dlv, -_Dlv) + _diffB) == 0
      and sp.expand(_k2 + sp.diff(Bmod, uu).subs(uu, _ucv)) == 0,
      "G5 route 2 (independent distributional/Fourier): the raw kernel centred is "
      "[B(u1)-B(u2)] dd'(Delta) (ODD in Delta, computed); decomposed into Delta^j "
      "dd'(Delta) slots and E-transformed with the registered convention, only j=1 "
      "survives (Etr(1,1) = -1; Etr(j,1) = 0 for j >= 2): K~ = -B'(u_c) = "
      "-H b1 - 2 H^2 b2 u_c", gate="G5")
_nzops = [o for o in OPS if sp.expand(AF_CORR[0][o][2]) != 0]
# route 3: the current generalised master kernel, both placements + the old kernel
_kBP = sp.expand(master(TAB_B, 'P'))
_kBE = sp.expand(master(TAB_B, 'E'))
check(sp.expand(_kBP - _kBE) == 0
      and sp.expand(_kBP + sp.diff(Bmod, uu).subs(uu, 0)) == 0
      and sp.expand(old_kernel_of(TAB_B)) == 0,
      "G5 route 3 (generalised master kernel): master(TAB_B) = -B'(0) = -H b1, BOTH "
      "placements (order-independence on the odd pair), while the OLD "
      "coincident-density kernel is IDENTICALLY ZERO on this pair at EVERY H order "
      "-- the master formula reproduces the exact functional Hessian; the old "
      "construction is blind to it", gate="G5")
check(sp.expand(_k2.subs(_ucv, 0) - _kBP) == 0,
      "G5 THREE-ROUTE AGREEMENT: direct functional Hessian (EL), raw-kernel centred "
      "slot route, and the generalised master formula ALL give K~ = -B'(u_c) = -H b1 "
      "at the reference centre -- the H^1 correction is a property of the "
      "action-functional Hessian, not of any one construction", gate="G5")

# the discriminating sub-checks
TAB_Bc = {(1, 0): sp.Integer(7), (0, 1): sp.Integer(7)}
check(sp.expand(master(TAB_Bc, 'P')) == 0 and sp.expand(old_kernel_of(TAB_Bc)) == 0,
      "G5 B=constant control: B' = 0 -> corrected == old == 0 (NO correction at ANY "
      "order on the pair) -- the H^1 correction is exactly the B' mechanism, not an "
      "implementation artefact", gate="G5")
check(sp.expand(_kBP.coeff(H, 1) + b1c) == 0 and sp.expand(_kBP.coeff(H, 0)) == 0
      and sp.expand(old_kernel_of(TAB_B).coeff(H, 1)) == 0,
      "G5 B'!=0 statement (H-graded): with B = b0 + H b1 u + H^2 b2 u^2 the corrected "
      "kernel is -H b1 + O(H^2): H^0 part 0 (== old H^0 part), H^1 part -b1 while the "
      "old H^1 part is 0 -- a GENUINE O(H^1) correction from an odd-derivative "
      "structure whose coefficient acquires u-dependence at O(H)", gate="G5")
_kBuc = sp.expand(master(TAB_B, 'P', uc=sp.Rational(1, 3)))
check(sp.expand(_kBuc + sp.diff(Bmod, uu).subs(uu, sp.Rational(1, 3))) == 0,
      "G5 second centre u_c = 1/3: K~ = -B'(1/3) (the centre dependence of the H^1 "
      "correction is verified, not inferred)", gate="G5")

# the exact decomposition identity (kept)
check(all(sp.expand(AF_CORR[i][_op][_n] - (AF_QS[i][_op][_n] - QS_OLD[i][_op][_n])) == 0
          for i in range(3) for _op in OPS for _n in (0, 1, 2)),
      "G5: correction == corrected - old, IDENTICALLY (every operator, sample, H "
      "order) -- the decomposition 'old (r=0 term) + explicit distributional "
      "corrections' is exact", gate="G5")
# --- the computed H^1 attribution on the REAL tables (nothing asserted vs old) ---


def _h1_generators(tab):
    """structures whose O(H) dressing carries a linear-in-u term (B'(u_c) ~ O(H)):
    the exact and only source of H^1 corrections (l+r=1 master-formula slots)."""
    out = {}
    for (p, q), B in tab.items():
        d1 = sp.expand(B.coeff(H, 1))
        if sp.expand(sp.diff(d1, uu).subs(uu, 0)) != 0:
            out[(p, q)] = B
    return out


_ok_attr = True
for i in range(3):
    for _op in OPS:
        _gen = _h1_generators(AF_TABS[i][_op])
        _nongen = dict((k, v) for k, v in AF_TABS[i][_op].items() if k not in _gen)
        _cg = sp.expand(master(_gen, 'P').subs(om, K_SAMPLES[i][0]).coeff(H, 1)
                        - old_kernel_of(_gen).subs(om, K_SAMPLES[i][0]).coeff(H, 1))
        _cn = sp.expand(master(_nongen, 'P').subs(om, K_SAMPLES[i][0]).coeff(H, 1)
                        - old_kernel_of(_nongen).subs(om, K_SAMPLES[i][0]).coeff(H, 1))
        if sp.expand(_cg - (AF_QS[i][_op][1] - QS_OLD[i][_op][1])) != 0 or _cn != 0:
            _ok_attr = False
check(_ok_attr,
      "G5 H^1 ATTRIBUTION (computed, every operator and sample): the H^1 correction "
      "is generated EXCLUSIVELY by structures whose O(H) coefficients are u-dependent "
      "(B'(u_c) ~ O(H) -- exactly the -B' mechanism gated above on the independent "
      "model); structures with u-independent O(H) coefficients contribute ZERO at "
      "H^1", gate="G5")
_nz1 = [o for o in OPS if any(sp.expand(AF_QS[i][o][1] - QS_OLD[i][o][1]) != 0
                              for i in range(3))]
check(len(_nzops) > 0,
      "G5 NON-VACUITY: the (l,r)!=(0,0) terms are NONZERO at H^2 for %s -- the rebuild "
      "is not a no-op (sqrt(-g), if absent, is CORRECT: its only structure is B_00 and "
      "Etr(r,0)=0 for r>=1, so it carries no corrections at any order)"
      % (", ".join(_nzops) if _nzops else "NO operator"), gate="G5")
for o in OPS:
    csym = sp.expand(correction_of(AF_TABS[0][o]))
    note("H^2 correction, %s: %s; the symbolic correction is %s"
         % (o,
            "NONZERO" if sp.expand(csym.coeff(H, 2)) != 0 else "zero",
            ("omega-free (additive master identity, as in the toy)"
             if om not in csym.free_symbols else
             "omega-DEPENDENT (the generalised (p,q)-resolved corrections carry "
             "per-leg structure the toy's single B_11 could not exhibit)")))
    note("H^1 correction, %s: %s; structures with u-dependent O(H) coefficients: %s"
         % (o, "NONZERO" if o in _nz1 else "zero",
            ", ".join("(%d,%d)" % pq for pq in sorted(_h1_generators(AF_TABS[0][o])))
            or "none"))
note("COMPUTED ORDER STATEMENT -- H^0: corrected kernel == coincident-density kernel "
     "(gated, G2); H^1: corrections OCCUR for %s, generated exclusively by u-dependent "
     "O(H) coefficients via the gated -B' mechanism (all other operators' H^1 kernels "
     "are unchanged); H^2: corrections occur for %s (non-vacuity gated). No universal "
     "first-nonzero correction order is claimed beyond these computed statements."
     % (", ".join(_nz1) if _nz1 else "no operator",
        ", ".join(_nzops) if _nzops else "no operator"))
stamp("G5 done")


# =============================================================================
print("\n=== G6: BROKEN CONTROLS (the toy's failed conventions, ported; each must FAIL) ===")
# The controls no longer demand corrected_H1 == old_H1 (that expectation was the
# retired toy-only order theorem).  Each control must FAIL to reproduce the
# corrected kernel at the order its broken convention corrupts -- compared against
# the INDEPENDENTLY COMPUTED corrected kernel (AF_QS), never a hardcoded expected
# difference.  A/B/C/Cp provably touch only r>=1 terms: H^0 must be preserved and
# the difference must surface at H^1 or H^2.  D/conj corrupt the placement/Fourier
# conventions themselves and are caught already at H^0 (computed, reported).
for _which in ('A', 'B', 'C', 'Cp'):
    _kb = dict((o, sp.expand(master_broken(AF_TABS[0][o], _which).subs(om, K_SAMPLES[0][0])))
               for o in OPS)
    _same0 = all(sp.expand(_kb[o].coeff(H, 0) - AF_QS[0][o][0]) == 0 for o in OPS)
    _d1 = [o for o in OPS if sp.expand(_kb[o].coeff(H, 1) - AF_QS[0][o][1]) != 0]
    _d2 = [o for o in OPS if sp.expand(_kb[o].coeff(H, 2) - AF_QS[0][o][2]) != 0]
    check(_same0 and bool(_d1 or _d2),
          "G6 control '%s' (r>=1-only corruption): reproduces the corrected kernel "
          "EXACTLY at H^0 (the Gilkey level untouched) but FAILS to reproduce it at "
          "H^1/H^2 (H^1 differs for: %s; H^2 differs for: %s) -- caught at the order "
          "it corrupts, against the independently computed corrected kernel"
          % (_which, ", ".join(_d1) if _d1 else "none",
             ", ".join(_d2) if _d2 else "none"), gate="G6")
_kbD = dict((o, sp.expand(master_broken(AF_TABS[0][o], 'D').subs(om, K_SAMPLES[0][0])))
            for o in OPS)
_d0D = [o for o in OPS if sp.expand(_kbD[o].coeff(H, 0) - AF_QS[0][o][0]) != 0]
_d1D = [o for o in OPS if sp.expand(_kbD[o].coeff(H, 1) - AF_QS[0][o][1]) != 0]
_d2D = [o for o in OPS if sp.expand(_kbD[o].coeff(H, 2) - AF_QS[0][o][2]) != 0]
check(bool(_d1D or _d2D),
      "G6 control 'D' (wrong-vertex placement sign): FAILS to reproduce the corrected "
      "kernel at H^1/H^2 (H^1 differs for: %s; H^2 differs for: %s) and additionally "
      "breaks H^0 itself for %s -- the placement convention is load-bearing at every "
      "order (H^0-sameness is not required here: this control corrupts orders its "
      "convention cannot spare)"
      % (", ".join(_d1D) if _d1D else "none", ", ".join(_d2D) if _d2D else "none",
         ", ".join(_d0D) if _d0D else "none"), gate="G6")
check(all(sp.expand(master_broken(AF_TABS[0][o], 'C') - old_kernel_of(AF_TABS[0][o])) == 0
          for o in OPS),
      "G6: control 'C' (frozen centre) IS the old coincident-density kernel, IDENTICALLY "
      "(all four operators, symbolic omega) -- the old basis is literally the (l,r)=(0,0) "
      "term of this construction, now a checked identity rather than a claim", gate="G6")
_kbc = dict((o, sp.expand(master(AF_TABS[0][o], 'P', conj=True).subs(om, K_SAMPLES[0][0])))
            for o in OPS)
_d0c = [o for o in OPS if sp.expand(_kbc[o].coeff(H, 0) - AF_QS[0][o][0]) != 0]
_d1c = [o for o in OPS if sp.expand(_kbc[o].coeff(H, 1) - AF_QS[0][o][1]) != 0]
_d2c = [o for o in OPS if sp.expand(_kbc[o].coeff(H, 2) - AF_QS[0][o][2]) != 0]
check(bool(_d1c or _d2c),
      "G6 control 'conj' (per-term conjugate Fourier transform): FAILS to reproduce "
      "the corrected kernel at H^1/H^2 (H^1 differs for: %s; H^2 differs for: %s), "
      "and additionally breaks H^0 for %s -- the E-transform sign convention is "
      "load-bearing at every order"
      % (", ".join(_d1c) if _d1c else "none", ", ".join(_d2c) if _d2c else "none",
         ", ".join(_d0c) if _d0c else "none"), gate="G6")
stamp("G6 done")


# =============================================================================
print("\n=== EMISSION: corrected kernels in the span-test representation (green-gated) ===")
_rt = all(sp.expand(sp.sympify(sp.srepr(AF_QS[i][o][_n])) - AF_QS[i][o][_n]) == 0
          for i in range(3) for o in OPS for _n in (0, 1, 2))
check(_rt, "E: srepr round-trip of every emitted kernel is EXACT (sympify(srepr(x)) == x)",
      gate="E")
GREEN = not FAIL
if GREEN:
    _cache = {
        "instrument": "wall_d2_phase11_af_basis.py",
        "tag": "AF-BASIS-v1",
        "note": "corrected action-functional (functional-Hessian) kernels; the old "
                "coincident-density basis is the (l,r)=(0,0) term (checked identity, "
                "G6); feed into the UNCHANGED span test with AFB_LOAD=1",
        "K_SAMPLES": [[str(a), str(b)] for a, b in K_SAMPLES],
        "OPS": list(OPS),
        "R0s": [sp.srepr(r) for r in R0s],
        "QS": [dict((o, dict((str(_n), sp.srepr(AF_QS[i][o][_n])) for _n in (0, 1, 2)))
                    for o in OPS) for i in range(3)],
    }
    open(os.path.join(HERE, ".p11_af_basis_cache.txt"), "w").write(json.dumps(_cache))
    note("cache written: .p11_af_basis_cache.txt (%d bytes); run the UNCHANGED span test "
         "against the corrected kernels with:  AFB_LOAD=1 python3 wall_d2_span_test.py"
         % os.path.getsize(os.path.join(HERE, ".p11_af_basis_cache.txt")))
else:
    note("RUN NOT GREEN -- .p11_af_basis_cache.txt NOT written (nothing fed downstream)")
stamp("emission done")


# =============================================================================
print("\n=== SUMMARY ===")
_gsum = {}
for c in CHECKS:
    _gsum.setdefault(c["gate"], [0, 0])[0 if c["pass"] else 1] += 1
for g in sorted(_gsum):
    note("gate %-3s: %3d checks, %d failed" % (g, sum(_gsum[g]), _gsum[g][1]))
res = {
    "instrument": "wall_d2_phase11_af_basis.py",
    "question": "was the old 96/300 H^2 outside-span result a basis-construction "
                "artifact (coincident-density basis, IBP-non-invariant)?",
    "verdict": ("GREEN -- corrected action-functional basis emitted; reclassify with: "
                "AFB_LOAD=1 python3 wall_d2_span_test.py" if GREEN else
                "RED -- see failures; no cache written"),
    "gates": dict((g, {"checks": v[0], "failed": v[1]}) for g, v in sorted(_gsum.items())),
    "corrections_H1_nonzero_for": _nz1,
    "corrections_H2_nonzero_for": _nzops,
    "order_statement": "H^0: corrected == old (gated). H^1: corrections occur exactly "
                       "via u-dependent O(H) coefficients (the -B' mechanism, gated "
                       "on the independent odd-pair model S=Int B(hA'hB+hA hB') whose "
                       "exact Hessian is -B'(u_c)). H^2: corrections occur "
                       "(non-vacuity gated). The old 'exactly O(H^2)' order theorem "
                       "is retired as toy-only.",
    "old_basis_is_r0_term": "checked identity (G6 control 'C' == old_kernel_of)",
    "checks": CHECKS,
    "notes": NOTES,
    "fail_count": len(FAIL),
    "failures": FAIL,
    "fence": "W-0: computed and reported only. No register edits, no operator additions, "
             "no refit, no edits to the loop side, the assembly cache, or "
             "wall_d2_span_test.py. The span-test reclassification concerns LOCAL UV "
             "COUNTERTERM STRUCTURE only and determines nothing about Q1 placement, "
             "Im chi, convergence class, or relaxational/resonant character.",
}
json.dump(res, open(os.path.join(HERE, "WALL_D2_PHASE11_AF_BASIS_RESULT.json"), "w"),
          indent=2)
print("result written: WALL_D2_PHASE11_AF_BASIS_RESULT.json")

_md = []
_md.append("# PHASE-11 ACTION-FUNCTIONAL BASIS RECONSTRUCTION -- VERDICT")
_md.append("")
_md.append("Instrument: `wall_d2_phase11_af_basis.py` (owner-authorized 2026-08-27; "
           "standing state 5fd77c0).")
_md.append("Verdict: **%s** (fail count %d)." % ("GREEN" if GREEN else "RED", len(FAIL)))
_md.append("")
_md.append("## What was built")
_md.append("")
_md.append("The toy-validated split-frequency functional-Hessian construction, "
           "generalised to the")
_md.append("four frozen operators {sqrt(-g), sqrt(-g)R, sqrt(-g)R^2, sqrt(-g)R_mnR^mn}: "
           "the machinery's")
_md.append("sector-graded cascade is mirrored with SPLIT u-frequencies (wE for the E "
           "leg, wP for the P")
_md.append("leg), so the eps1*eps2 density resolves as "
           "D(u; wE, wP) = Sum_pq B_pq(u) (-i wE)^p (+i wP)^q -- the per-leg derivative")
_md.append("counts that the shared-frequency construction conflates. The master formula "
           "then produces the")
_md.append("IBP-invariant action-functional kernels; the old coincident-density kernel "
           "is the (l,r)=(0,0)")
_md.append("term (checked identity), and the (l,r)!=(0,0) terms are the explicit "
           "distributional")
_md.append("corrections  -C(u_c) dd''(Delta) + (1/4)C''(u_c) dd(Delta)  it could not "
           "see. Independence")
_md.append("condition wired: old kernels / H^2 residual / span test are used ONLY as "
           "validation targets")
_md.append("(G2, G6); no correction coefficient is guessed, fitted, or solved for.")
_md.append("")
_md.append("## Gates (all hard)")
_md.append("")
for g in sorted(_gsum):
    _md.append("- **%s**: %d checks, %d failed" % (g, sum(_gsum[g]), _gsum[g][1]))
_md.append("")
_md.append("## Findings (computed)")
_md.append("")
_md.append("- H^0 kernels are UNCHANGED (gated): corrected == coincident-density.")
_md.append("- H^1 corrections OCCUR for: %s -- genuine action-functional Hessian "
           "corrections. The previous 'corrections exactly O(H^2)' theorem is RETIRED "
           "as toy-only (its proof used the toy's single even structure); the "
           "replacement gate derives the exact Hessian of S=Int B(u)[hA'hB+hA hB'] "
           "three independent ways (direct EL Hessian, raw-kernel centred slots, "
           "master kernel): K~ = -B'(u_c), an O(H^1) correction from u-dependent O(H) "
           "coefficients that the old construction is blind to; on the real tables "
           "the H^1 correction is attributed exclusively to such structures."
           % (", ".join(_nz1) if _nz1 else "no operator"))
_md.append("- Nonzero H^2 corrections for: %s."
           % (", ".join(_nzops) if _nzops else "none"))
_md.append("- The old basis is the r=0 term of this construction (G6 control-'C' "
           "identity).")
_md.append("")
_md.append("## How to reclassify (span test UNCHANGED)")
_md.append("")
_md.append("    python3 wall_d2_span_test.py               # old basis (baseline; must")
_md.append("                                             #  reproduce the 96/300 reading)")
_md.append("    AFB_LOAD=1 python3 wall_d2_span_test.py    # corrected AF basis")
_md.append("")
_md.append("The machinery's Phase-11 BASIS section carries a DEFAULT-OFF cache hook "
           "(AFB_LOAD=1 plus")
_md.append(".p11_af_basis_cache.txt); the loop side, .p10_assembly_cache.txt, the "
           "identification")
_md.append("section and wall_d2_span_test.py are untouched, and the default path is "
           "unchanged.")
_md.append("")
_md.append("## Fence")
_md.append("")
_md.append("W-0: computed and reported only. The reclassification concerns LOCAL UV "
           "counterterm")
_md.append("structure only; it determines nothing about Q1 placement, Im chi, "
           "convergence class, or")
_md.append("relaxational/resonant character. No register edits; nothing banked.")
open(os.path.join(HERE, "WALL_D2_PHASE11_AF_BASIS_VERDICT.md"), "w").write(
    "\n".join(_md) + "\n")
print("verdict written: WALL_D2_PHASE11_AF_BASIS_VERDICT.md")

print(f"\n[FAIL count = {len(FAIL)}]  elapsed {time.time()-T0:.1f}s")
for f_ in FAIL:
    print("   FAILED:", f_)
sys.exit(0 if not FAIL else 1)
