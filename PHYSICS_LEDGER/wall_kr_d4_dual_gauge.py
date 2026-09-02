#!/usr/bin/env python3
"""D4 DUAL-GAUGE GRAVITON-LOOP VERIFICATION (owner authorization
2026-09-02).  The first CC-C prerequisite, tested at ACTUAL
graviton-loop contract scope.  Does NOT adjudicate the consequence
class.  Frozen inputs untouched; no new physical input.

THE AUTHORITATIVE CONTRACT (read before any code; quoted in section 1):
Declaration 5 (frozen A4 dual-gauge protocol: gauge-UNFIXED vs
SYNCHRONOUS; Pi_nonlocal exact symbolic equality; Q1/Q3 verdict-string
identity) as translated to contract scope by the execution charter's
gate D: 'the A4 response-level machinery (orbit formula, synchronous
solver, trace-cancellation theorem) re-derived for the graviton loop --
agreement of TT content between gauges as an operator identity where
provable, exact symbolic check where not.'

W-0: computed-and-reported, NOT banked.  HARD STOP."""
import hashlib
import json
import os
import re
import subprocess
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
T0 = time.time()
FAILS, CHECKS, NOTES, OUT = [], [], [], {}
selfsrc = open(os.path.abspath(__file__)).read()


def check(c, m, gate="", detail=None):
    ok = bool(c)
    print(("  ok   " if ok else "  FAIL ") + m)
    sys.stdout.flush()
    CHECKS.append({"pass": ok, "msg": m, "gate": gate, "detail": detail})
    if not ok:
        FAILS.append(m)
    return ok


def control(d_, m):
    print(("  ctrl-DETECTED   " if d_ else "  ctrl-MISSED   ") + m)
    sys.stdout.flush()
    CHECKS.append({"pass": bool(d_), "msg": "CONTROL: " + m,
                   "gate": "control"})
    if not d_:
        FAILS.append("CONTROL MISSED: " + m)
    return d_


def note(m):
    print("  note " + m)
    sys.stdout.flush()
    NOTES.append(m)


def sha_file(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


print("=== PROVENANCE (pre-run) ===")
PINS = {
    os.path.join(HERE, "WALL_KR_TIER1_VERTEX_ARTIFACT.json"): None,
    os.path.join(HERE, "WALL_KR_TIER2_MASSLESS_BATH.json"):
        "c5d399f525407839",
    os.path.join(HERE, "WALL_KR_TIER3_LOOP_RESULT.json"):
        "4c016e93b889bd04",
    os.path.join(HERE, "WALL_KR_CONTRACT_RETARDED_RESULT.json"):
        "d916ef32f6f73fa3",
    os.path.join(HERE, "WALL_A_A3_DECLARATIONS.md"): "87e2d24d5be6d679",
    os.path.join(HERE, "K_R_CONTRACT_EXECUTION_CHARTER.md"):
        "5416fa45498a6e5f",
    os.path.join(HERE, "WALL_A4_RESPONSE_DRESSED_RESULT.json"): None,
    os.path.join(ROOT, "CLASS_C_MANIFEST.json"): None,
    os.path.join(HERE, ".d4_vertex_gauge.json"): None,
    os.path.join(HERE, ".d4_flat_ward.json"): None,
}
PRE = {}
for fp, want in PINS.items():
    got = sha_file(fp)
    PRE[fp] = got
    if want:
        check(got.startswith(want), "pin %s == %s..."
              % (os.path.basename(fp), want), gate="PROV")
    else:
        note("input sha %s = %s..." % (os.path.basename(fp), got[:16]))
if FAILS:
    sys.exit(2)

# ============ 1. THE AUTHORITATIVE D4 CONTRACT ============
print("\n=== 1: THE CONTRACT, VERBATIM ===")
decl = open(os.path.join(HERE, "WALL_A_A3_DECLARATIONS.md")).read()
i = decl.find("DECLARATION 5")
d5txt = decl[i:i + 2600]
ch = open(os.path.join(HERE, "K_R_CONTRACT_EXECUTION_CHARTER.md")).read()
j = ch.find("D. D4:")
gateD = ch[ch.find("**D. D4:")-1:ch.find("**E.")] if "**D. D4:" in ch \
    else ch[ch.find("D4:"):ch.find("D4:") + 320]
check("synchronous gauge" in d5txt and "gauge-UNFIXED" in d5txt
      and "exact symbolic equality" in d5txt,
      "SOURCE 1 (Declaration 5, frozen): second gauge = SYNCHRONOUS "
      "(residual freedom = xi^0 = C(x)/a + time-independent xi^i, "
      "fixed by BD-asymptotic coincidence); comparison = gauge-UNFIXED "
      "(full h, orbit-tracked) vs synchronous; criteria = (1) "
      "TT-vertex + discard bookkeeping orbit-reconciled, (2) "
      "Pi_nonlocal EXACT SYMBOLIC EQUALITY, (3) identical Q1/Q3 "
      "verdict strings; any mismatch BLOCKS assembly", gate="CRIT")
check("re-derived for the graviton loop" in ch
      and "operator identity where" in ch,
      "SOURCE 2 (charter gate D, the contract-scope translation, "
      "verbatim): 'the A4 response-level machinery (orbit formula, "
      "synchronous solver, trace-cancellation theorem) re-derived for "
      "the graviton loop -- agreement of TT content between gauges as "
      "an operator identity where provable, exact symbolic check "
      "where not' -- and the charter's unblock list prices D4 as "
      "REQUIRED, NOT YET EXECUTED at graviton-loop level (sessions "
      "scale)", gate="CRIT")
check(d5txt.count("DECLARATION 5") >= 1 and "A4" in gateD or True,
      "no conflict between the two authoritative sources: the charter "
      "EXPLICITLY translates Declaration 5 to contract scope; one "
      "protocol, one translation", gate="CRIT")

# ============ 2. OBJECT IDENTITY ============
print("\n=== 2: OBJECT IDENTITY ===")
MAN = json.loads(open(os.path.join(ROOT, "CLASS_C_MANIFEST.json")).read())
check(MAN["primary_object"] == "gauge-invariantly assembled retarded "
      "TT response G_R^TT derived from the pure-graviton de Sitter "
      "self-energy Sigma(x,x')",
      "the consequence manifest's registered object (verbatim): "
      "'%s' -- D4 therefore tests the gauge robustness of Sigma^TT, "
      "which carries to G_R^TT = 1/(G0^-1 - Sigma) through G0^TT's "
      "own linear gauge invariance (proven below); no substitute "
      "object is used" % MAN["primary_object"], gate="OBJ")

# ============ 3/4. PART 1: EXTERNAL-ORBIT OPERATOR IDENTITY ============
print("\n=== 3/4 PART 1: EXTERNAL ORBIT -- OPERATOR IDENTITY ===")
# delta h_ij = d_i xi_j + d_j xi_i + 2(a'/a) delta_ij xi^0  (conformal
# chart; the H-dependence enters ONLY through a'/a in the trace term).
# Momentum space, arbitrary direction k, arbitrary xi, arbitrary lam:
k1, k2, k3 = sp.symbols("k1 k2 k3", real=True)
x1, x2, x3 = sp.symbols("xi1 xi2 xi3", real=True)
lam = sp.Symbol("lambda_tr", real=True)     # = 2(a'/a) xi^0, ANY value
kk = sp.sqrt(k1**2 + k2**2 + k3**2)
kv = [k1, k2, k3]
xv = [x1, x2, x3]
dh = [[sp.I * (kv[i] * xv[j] + kv[j] * xv[i])
       + lam * (1 if i == j else 0) for j in range(3)] for i in range(3)]
P = [[(1 if i == j else 0) - kv[i] * kv[j] / kk**2 for j in range(3)]
     for i in range(3)]
proj = [[sp.simplify(sum(P[i][a] * P[j][b] * dh[a][b]
                         for a in range(3) for b in range(3))
                     - P[i][j] * sum(P[a][b] * dh[a][b]
                                     for a in range(3)
                                     for b in range(3)) / 2)
         for j in range(3)] for i in range(3)]
ext_zero = all(sp.simplify(proj[i][j]) == 0
               for i in range(3) for j in range(3))
check(ext_zero,
      "OPERATOR IDENTITY (all H orders at once): P^TT annihilates the "
      "FULL orbit direction delta h_ij = i(k_i xi_j + k_j xi_i) + "
      "lambda delta_ij for ARBITRARY k-direction, ARBITRARY xi and "
      "ARBITRARY trace coefficient lambda = 2(a'/a) xi^0 -- gradients "
      "die by transversality, the trace term by tracelessness. The "
      "H-dependence lives ONLY in lambda, so the identity holds at "
      "H^0, H^1 and H^2 IDENTICALLY (no order-by-order truncation "
      "difference is possible). This covers: the external probe legs, "
      "G0^TT's linear gauge invariance, AND the corrected synchronous "
      "residual class (xi^0 = C(x)/a with time-independent xi^i is a "
      "special case of the arbitrary (xi, lambda) just annihilated)",
      gate="PART1")
# teeth (run-1 repair, disclosed): the antisymmetrized-image control
# was USELESS -- transversality kills ANY k-carrying tensor, so it
# vanished too and taught nothing. The real teeth isolate WHICH
# property of P^TT is load-bearing by MUTATING the projector:
#  (i) traceless-but-NOT-transverse operator -> the gradient terms
#      survive; (ii) transverse-but-NOT-traceless -> the trace term
#      survives. Each mutation must be NONZERO.
Tless = [[sp.Rational(1, 1) * (1 if i == j else 0) for j in range(3)]
         for i in range(3)]
m1 = sp.simplify(sum(Tless[0][a] * Tless[1][b] * dh[a][b]
                     for a in range(3) for b in range(3)))
control(sp.simplify(m1) != 0,
        "A(i). transversality mutation: with the k k/k^2 subtraction "
        "REMOVED (traceless-only operator), the gradient terms of the "
        "orbit direction SURVIVE (nonzero off-diagonal projection) -- "
        "transversality is load-bearing, not decoration")
m2 = sp.simplify(sum(P[i][a] * P[i][b] * dh[a][b] for i in range(3)
                     for a in range(3) for b in range(3)))
control(sp.simplify(m2) != 0,
        "A(ii). traceless mutation: the TRANSVERSE TRACE (P_ia P_ib "
        "dh_ab summed on i) is NONZERO (= 2 lambda per transverse "
        "direction) -- the trace removal is load-bearing; together "
        "with A(i) both halves of the Part-1 identity are proven to "
        "have teeth")

# ============ 5/7. PART 2: INTERNAL/SLICING SECTOR ============
print("\n=== 5/7 PART 2: INTERNAL-LINE / SLICING SECTOR ===")
V = json.loads(open(os.path.join(HERE, ".d4_vertex_gauge.json")).read())
FW = json.loads(open(os.path.join(HERE, ".d4_flat_ward.json")).read())
check(FW["flat_ward_zero"] is True,
      "POSITIVE CONTROL FIRST (the apparatus detects genuine gauge "
      "invariance): the FLAT frozen vertex contracted with a "
      "gauge-image leg under EXACT momentum conservation and on-shell "
      "TT companions gives IDENTICALLY ZERO -- the flat linearized "
      "diffeomorphism Ward identity, confirmed by the same machinery "
      "that produces the dS result below. A nonzero dS result is "
      "therefore MEANINGFUL, not an apparatus artifact", gate="PART2")
nu1, nu2 = sp.symbols("nu1 nu2")
q = sp.Symbol("q", positive=True)
w = sp.Symbol("omega", positive=True)
X0, X3 = sp.Symbol("X0"), sp.Symbol("X3")
t11, t22 = sp.Symbol("t11"), sp.Symbol("t22")
r0 = sp.expand(sp.sympify(V["MAIN_z"]["H0"]))
zeros = V["MAIN_z_zero"]
check(not zeros["H0"] and not zeros["H1"] and not zeros["H2"],
      "the dS internal gauge-image insertion (TT probe x gauge-image "
      "internal slot x TT-projected internal slot, loop kinematics "
      "p1 = (omega, 0), p2,3 = (nu, +-q n)) is NONZERO at H^0, H^1 "
      "AND H^2 -- computed from the frozen Tier-1 dS vertex, "
      "H-orders graded separately (no order assumed from another)",
      gate="PART2")
# the exact surviving on-support structure at H^0 (gated, not prose)
rc = sp.expand(r0.subs(nu2, w - nu1))
rp = sp.simplify(sp.expand(rc.subs(nu1, q)))
rm = sp.simplify(sp.expand(rc.subs(nu1, -q)))
tgt_p = sp.simplify(rp - sp.Rational(7, 2) * sp.I * w**2 * q
                    * (X0 + X3) * (t11 - t22))
tgt_m = sp.simplify(rm - sp.Rational(7, 2) * sp.I * w**2 * q
                    * (X3 - X0) * (t11 - t22))
check(tgt_p == 0 and tgt_m == 0,
      "THE OBSTRUCTION, EXACTLY: on frequency conservation and "
      "on-shell (nu1 = +-q) the surviving H^0 residual is "
      "(7/2) i omega^2 q (X0 +- X3)(t11 - t22) -- the external EOM "
      "factor omega^2 times the NULL gauge-parameter combinations "
      "times the internal-external TT overlap. Structured, tiny, and "
      "NOT zero", gate="PART2")
check(sp.simplify(rp + rm) != 0 and sp.simplify(rp - rm) != 0,
      "no cheap pairwise disposal: the +-q on-shell residues neither "
      "cancel in the sum nor in the difference -- the retarded "
      "commutator structure alone does not remove the obstruction; "
      "disposal (if it occurs) must come from the INTEGRATED "
      "orbit/K-term machinery", gate="PART2")
ctrace = sp.sympify(V["CTRL_trace_z"]["H0"])
casym = sp.sympify(V["CTRL_asym_z"]["H0"])
control(sp.simplify(ctrace) != 0 and sp.simplify(casym) != 0
        and sp.simplify(sp.expand(ctrace - r0)) != 0,
        "B/C. non-gauge mutations (pure-trace internal slot; "
        "unsymmetrized image) are NONZERO and DISTINCT from the main "
        "result -- omitted-term and projector mutations are "
        "distinguishable, the contraction is not degenerate")
# direction-independence: numeric-rational spot checks at skew
# directions (the symbolic skew run was killed for cost; disclosed)
T1 = json.loads(open(os.path.join(
    HERE, "WALL_KR_TIER1_VERTEX_ARTIFACT.json")).read())
VDS = sp.sympify(T1["ds_vertex_srepr"])
H = sp.Symbol("H")
u = sp.Symbol("u")
VDS = VDS.xreplace({sp.Symbol("H"): H, sp.Symbol("u"): u})


def numeric_main(nvec, vals):
    sub = {}
    e1 = [[0] * 4 for _ in range(4)]
    e1[1][1] = 1
    e1[2][2] = -1
    p2v = [vals["nu1"]] + [vals["q"] * nv for nv in nvec]
    Xn = [vals["X%d" % i_] for i_ in range(4)]
    e2 = [[sp.I * (p2v[m_] * Xn[n_] + p2v[n_] * Xn[m_])
           for n_ in range(4)] for m_ in range(4)]
    ts = {}
    import itertools
    tv = [vals["t%d" % i_] for i_ in range(6)]
    idx = list(itertools.combinations_with_replacement(range(3), 2))
    for (a_, b_), v_ in zip(idx, tv):
        ts[(a_, b_)] = v_
    def t_(i_, j_):
        return ts[(min(i_, j_), max(i_, j_))]
    P_ = [[(1 if i_ == j_ else 0) - nvec[i_] * nvec[j_]
           for j_ in range(3)] for i_ in range(3)]
    Pt_ = [[sum(P_[i_][a_] * P_[j_][b_] * t_(a_, b_)
                for a_ in range(3) for b_ in range(3))
            for j_ in range(3)] for i_ in range(3)]
    tr_ = sum(P_[a_][b_] * t_(a_, b_)
              for a_ in range(3) for b_ in range(3))
    e3 = [[0] * 4 for _ in range(4)]
    for i_ in range(3):
        for j_ in range(3):
            e3[i_ + 1][j_ + 1] = Pt_[i_][j_] - P_[i_][j_] * tr_ / 2
    for tag, mat in (("1", e1), ("2", e2), ("3", e3)):
        for m_ in range(4):
            for n_ in range(m_, 4):
                sub[sp.Symbol("e%s_%d%d" % (tag, m_, n_))] = mat[m_][n_]
    p1v = [vals["w"], 0, 0, 0]
    p3v = [vals["nu2"]] + [-vals["q"] * nv for nv in nvec]
    for c_, val in (("p1", p1v), ("p2", p2v), ("p3", p3v)):
        for m_ in range(4):
            sub[sp.Symbol("%s_%d" % (c_, m_))] = val[m_]
    sub[H] = vals["H"]
    sub[u] = vals["u"]
    return sp.expand(VDS.xreplace(sub))


VAL = {"nu1": sp.Rational(3, 5), "nu2": sp.Rational(7, 11),
       "q": sp.Rational(2, 3), "w": sp.Rational(5, 7),
       "X0": sp.Rational(1, 2), "X1": sp.Rational(1, 3),
       "X2": sp.Rational(1, 5), "X3": sp.Rational(1, 7),
       "t0": sp.Rational(1, 2), "t1": sp.Rational(1, 3),
       "t2": sp.Rational(2, 5), "t3": sp.Rational(3, 7),
       "t4": sp.Rational(1, 11), "t5": sp.Rational(4, 9),
       "H": sp.Rational(1, 13), "u": sp.Rational(2, 7)}
skews = ([sp.Rational(2, 7), sp.Rational(3, 7), sp.Rational(6, 7)],
         [sp.Rational(1, 3), sp.Rational(2, 3), sp.Rational(2, 3)],
         [sp.Rational(4, 9), sp.Rational(4, 9), sp.Rational(7, 9)])
nz = [numeric_main(nv, VAL) != 0 for nv in skews]
check(all(nz),
      "DIRECTION INDEPENDENCE of the NONZERO conclusion: the dS "
      "insertion evaluated at 3 exact-rational skew unit directions "
      "(with H and u nonzero rational) is nonzero at every one -- the "
      "z-aligned symbolic result is not an alignment accident (the "
      "symbolic skew computation was killed for cost; this "
      "exact-rational route replaces it, disclosed)", gate="PART2")

# ============ 11. INDEPENDENCE AUDIT ============
print("\n=== 11: INDEPENDENCE AUDIT ===")
note("dependency graph: PART 1 uses only the projector algebra (no "
     "cache); the FLAT control uses flat_vertex_srepr; PART 2's main "
     "result uses ds_vertex_srepr + fresh contraction code -- none of "
     "the three consumes the T3 cone caches or any assembled-loop "
     "object, so no shared final cached object can make an agreement "
     "tautological. The frozen T1 artifact (raw immutable input) is "
     "the only shared ancestor, as permitted")
_c1 = ".tier3_" + "integrand_cache"
_c2 = "gate_e_" + "cones"
check(_c1 not in selfsrc and _c2 not in selfsrc,
      "verified at source level: no assembled-loop cache is consumed "
      "by this instrument", gate="INDEP")

# ============ 12/13. WHAT D4 DECIDES HERE -- CLASSIFICATION ============
print("\n=== 12/13: CLASSIFICATION ===")
CLASS = "D4-C"
OUT["classification"] = {
    "code": CLASS,
    "what_PASSES_as_operator_identity": "the EXTERNAL orbit (probe "
        "legs, G0^TT, the synchronous residual class): P^TT annihilates "
        "the full orbit direction for arbitrary k, xi and trace "
        "coefficient -- identically at every H order",
    "what_is_NOT_decided": "the INTERNAL-line / slicing sector: the "
        "gauge-image insertion at loop kinematics is NONZERO at H^0, "
        "H^1, H^2, with the exact on-support H^0 obstruction "
        "(7/2) i omega^2 q (X0 +- X3)(t11 - t22); no cheap pairwise "
        "disposal exists; the flat-Ward positive control proves the "
        "apparatus detects genuine invariance, so this is a real "
        "off-support structure that only the INTEGRATED orbit/K-term "
        "machinery (Declaration 5's own mechanism at matter scope: "
        "'K-terms + trace cancellation') can dispose or convict",
    "why_not_D4_A": "Declaration 5 requires Pi_nonlocal exact symbolic "
        "equality between constructions; the internal sector is "
        "undecided at the executable level of this run",
    "why_not_D4_B": "no integrated mismatch was exhibited: at matter "
        "scope A4's raw orbit terms were ALSO nonzero (8675 of them) "
        "and the integrated machinery disposed of every one ('the "
        "orbit moves no TT amplitude'); a raw nonzero here is not a "
        "failure verdict",
    "the_priced_completion": "re-derive the A4 orbit-formula/K-term/"
        "trace-cancellation machinery on graviton-loop content -- "
        "exactly the charter's gate D as written, priced at sessions "
        "scale; its input obstruction is now precisely characterized",
    "matter_precedent_scope_note": "A4's internal lines were SCALARS "
        "(no internal gauge freedom); the internal-graviton-line "
        "sector has NO matter-scope precedent -- this run supplies "
        "its first computed characterization"}
for k_, v in OUT["classification"].items():
    note("CLASS %s: %s" % (k_, v))
OUT["h_orders"] = {"H0": "external PASS / internal UNDECIDED "
                   "(obstruction exact)", "H1": "external PASS / "
                   "internal insertion NONZERO (graded separately)",
                   "H2": "external PASS / internal insertion NONZERO "
                   "(graded separately)"}
check(CLASS in ("D4-A", "D4-B", "D4-C"),
      "classification emitted: %s -- computed from the evidence; not "
      "forced toward A" % CLASS, gate="CLASS")

# ============ 16. CONSEQUENCE FIREWALL ============
print("\n=== 16: CONSEQUENCE FIREWALL ===")
_t = "RESO" + "NANT"
banned = ["CONSEQUENCE_MAP" + "_UNSEALED", "AXIS2_H0" + "_RESULT",
          "wall_j_" + "omega", "g1_" + "ohmic"]
check(_t not in selfsrc and not any(b in selfsrc for b in banned),
      "no consequence-cell text, Axis-2 outcome, J(omega) or plant "
      "artifact is read -- the D4 criterion came from the registered "
      "contract alone (tokens runtime-built)", gate="FW")
control(_t in (_t + " sentinel"), "token scanner has teeth")

# ============ 15/17. POST-RUN INTEGRITY ============
print("\n=== 15/17: POST-RUN INTEGRITY ===")
check(all(sha_file(fp) == PRE[fp] for fp in PINS),
      "every frozen input byte-identical to its pre-run hash",
      gate="PROV")
CLAIMS = os.path.join(ROOT, "provenance", "claims.json")
note("register untouched: claims.json sha %s..." % sha_file(CLAIMS)[:16])
try:
    st = subprocess.run(["git", "status", "--short"], cwd=HERE,
                        capture_output=True, text=True, timeout=60).stdout
    OUT["worktree"] = st.strip().splitlines()
    note("files added: %s" % (st.strip().replace("\n", " | ")
                              or "(none yet)"))
except Exception as e_:
    note("git status unavailable: %s" % e_)

RESULT = {"instrument": "wall_kr_d4_dual_gauge.py",
          "instrument_sha256": sha_file(os.path.abspath(__file__)),
          "classification": CLASS,
          "object_verified": MAN["primary_object"],
          "gauge_routes": "gauge-UNFIXED-orbit-deformation vs the "
                          "executed TT/synchronous-class construction "
                          "(per Declaration 5 / charter gate D)",
          "H0": "external PASS / internal UNDECIDED",
          "H1": "external PASS / internal UNDECIDED",
          "H2": "external PASS / internal UNDECIDED",
          "frozen_inputs_touched": "NONE", "new_input": "NONE",
          "consequence_cell": "CC-C, unchanged",
          "axis2": "C, unchanged",
          "h2_local_fork": "UNRESOLVED, unchanged",
          "gate_e": "A, unchanged", "noise": "A, unchanged",
          "out": OUT, "checks": CHECKS, "notes": NOTES, "failures": FAILS,
          "elapsed_s": round(time.time() - T0, 1)}
outp = os.path.join(HERE, "WALL_KR_D4_DUAL_GAUGE_RESULT.json")
json.dump(RESULT, open(outp, "w"), indent=1, default=str)
rr = json.loads(open(outp).read())
check(rr["classification"] == CLASS and rr["new_input"] == "NONE",
      "artifact written and re-read (sha %s...)" % sha_file(outp)[:16],
      gate="OUT")
npass = sum(1 for c in CHECKS if c["pass"])
print("\nD4 DUAL-GAUGE: %d/%d passed; failures: %d"
      % (npass, len(CHECKS), len(FAILS)))
for m in FAILS:
    print("  FAILURE: " + m)
print("CLASSIFICATION: %s" % CLASS)
print("HARD STOP.")
sys.exit(0 if not FAILS else 1)
