#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""F1 GOVERNANCE REPLAY -- UV locality classification under the V4-corrected predicate.

Owner-directed governance action (2026-08-28), authorized with ONE binding condition:
the locality classifier here must be INDEPENDENTLY IMPLEMENTED -- no verbatim reuse of
the Phase-12 S2 classification code path (sp.Poly construction), so that the same
defect cannot be inherited.

What this instrument does (and all it does):
  R0  input integrity: the a22b587 manifest + the Phase-12 record/instrument hashes
      (94cfffc), and PROOF THAT NO FROZEN FILE WAS EDITED by the V4 amendment
      (v1/registry/v2/v3 sha256 unchanged; V4 document/record mutually consistent);
  R1  re-materialisation of the ALREADY-RECORDED pole object Sigma_0/1/2 from the
      frozen caches via the validated machinery load (NO loop regeneration) + identity
      proof against the Phase-12 record by expression fingerprints and term census;
  R2  re-classification of every pole term under the V4-corrected F1 predicate using
      TWO independent routes (expression-tree analysis; sympy Expr.is_polynomial --
      neither calls sp.Poly) + negative/positive controls + the literal-wording
      census (exponent-parity route) as the amendment's live demonstration;
  R3  proof the MS subtraction and counterterm mapping are UNCHANGED: Pi_local^MS
      fingerprint equality with the recorded value, split residual 0, PIN/operator
      exact identities re-derived (m symbolic, held-out sample included);
  R4  emission of the governance-replay result, the UV FREEZE record, and the
      ASSEMBLY-3 ENTRY OBJECT (finite eps^0 kernel: TO_BE_DERIVED).

It does NOT: regenerate the loop, compute any finite eps^0 response, run Q1-Q5,
compare J(omega), run PV, classify spectral behaviour, alter the basis, refit
coefficients, add operators, or touch any frozen artifact. HARD STOP after R4. W-0.

Run: python3 wall_d2_f1_replay_uv_locality.py    (no arguments)
Exit 0 iff every gate passes.
"""
import hashlib
import json
import os
import subprocess
import sys
import time

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()
FAIL = []
CHECKS = []
NOTES = []
assert len(sys.argv) == 1, "no arguments (argv must stay clean for the machinery exec)"


def check(cond, msg, gate=""):
    ok = bool(cond)
    print(("  ok   " if ok else "  FAIL ") + (("[%s] " % gate if gate else "") + msg))
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


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def expr_fp(ex):
    """sha256 fingerprint of a sympy expression -- copied VERBATIM from the Phase-12
    instrument: it is the IDENTITY TOKEN by which the recorded pole object is matched,
    not a classification decision (reusing it here is the provenance mechanism)."""
    return hashlib.sha256(sp.srepr(sp.expand(ex)).encode()).hexdigest()[:16]


RESULT_PATH = os.path.join(HERE, "WALL_D2_F1_REPLAY_UV_LOCALITY_RESULT.json")

# =====================================================================================
# R0 -- INPUT INTEGRITY + NO-FROZEN-FILE-EDITED (the V4 amendment edits nothing)
# =====================================================================================
print("=== R0: INPUT INTEGRITY + NO-FROZEN-FILE-EDITED ===")
EXPECTED = {
    ".p10_assembly_cache.txt": "3208492fcf01caad5b9d35c40a4379b056cd5ca8bc175d4ca2569a273561a0af",
    ".p11_af_basis_cache.txt": "692039d8c2a9d462eb314557ddc78e00d68c73054aed7db2987671ad58f63fbb",
    "wall_d2_span_test.py": "69fa98e4c92144dc0d1ab86c148e9ddf698952cb4b2d7b25ea6d14c109176dd8",
    "wall_d2_phases8_12.py": "f48b2cc898017493a11f08c8b6bfcb1c2367a0f577b583f00d77d0bd8341c558",
    "wall_d2_phase11_af_basis.py": "5dccac11a597582f19d632749b09b57c3e8d882a2de434c7da6e83f9d236be4b",
    "WALL_A_A3_REGISTRY.json": "faa977d40f1ba31836e35b18223c1f573559b49649a84fad237a3809aae59b55",
    "wall_d2_phase12_ms_split.py": "a9850cd5d8ce5d61e1eb9574c9aaeed2a412db4a833f851e447b36b5955c83a2",
    "WALL_D2_PHASE12_MS_SPLIT_RESULT.json": "185e1bf5330ad9b6a9eacca5c236b234d4d924a3e980ab88e0cad2a58814ce1f",
}
FROZEN = {
    "WALL_A_A3_DECLARATIONS.md": "87e2d24d5be6d67970f4089a09aa61a28d4de8cf6471f987af3db1c2ac015f6e",
    "WALL_A_A3_REGISTRY.json": "faa977d40f1ba31836e35b18223c1f573559b49649a84fad237a3809aae59b55",
    "WALL_A_A3_DECLARATIONS_V2_AMENDMENT.md": "6f2a762f4a4a01cd4794d029eecb2f1aadace9cd52637f12d3529e0564ce3d53",
    "WALL_A_A3_DECLARATIONS_V3_AMENDMENT.md": "b0b9983bf0ab04c0c5017e094a4e53a7e34fc8ddb1b6483724a14bb36eb36ee3",
}
V4_DOC = "WALL_A_A3_DECLARATIONS_V4_AMENDMENT.md"
V4_REC = "WALL_A_A3_V4_AMENDMENT_RECORD.json"
P10 = os.path.join(HERE, ".p10_assembly_cache.txt")

drift = []
for fname, want in EXPECTED.items():
    p = os.path.join(HERE, fname)
    if not os.path.exists(p):
        drift.append("%s: MISSING" % fname)
        continue
    got = sha(p)
    print("   %s  %s" % (got, fname))
    if got != want:
        drift.append("%s: sha256 %s != recorded %s" % (fname, got, want))
if os.path.exists(P10):
    if os.path.getsize(P10) != 28795:
        drift.append(".p10_assembly_cache.txt: size %d != 28795" % os.path.getsize(P10))
    if open(P10).read(11) != "L2repair-v1":
        drift.append(".p10_assembly_cache.txt: tag != L2repair-v1")
for fname, want in FROZEN.items():
    p = os.path.join(HERE, fname)
    if not os.path.exists(p) or sha(p) != want:
        drift.append("FROZEN FILE EDITED (or missing): %s must stand at sha256 %s" % (fname, want))
V4DOC_SHA = sha(os.path.join(HERE, V4_DOC)) if os.path.exists(os.path.join(HERE, V4_DOC)) else None
v4rec = {}
if V4DOC_SHA is None:
    drift.append("V4 amendment document MISSING: %s" % V4_DOC)
else:
    try:
        v4rec = json.loads(open(os.path.join(HERE, V4_REC)).read())
    except Exception as e:
        drift.append("V4 amendment record unreadable: %s" % e)
    if v4rec.get("amendment_document_sha256") != V4DOC_SHA:
        drift.append("V4 record/document inconsistency: record cites %r, on-disk sha256 %s"
                     % (v4rec.get("amendment_document_sha256"), V4DOC_SHA))
HEAD = "unavailable"
try:
    st = subprocess.run(["git", "status", "--porcelain", "--"]
                        + [os.path.join(HERE, f) for f in EXPECTED],
                        capture_output=True, text=True, cwd=HERE).stdout.strip()
    if st:
        drift.append("git working tree not clean for the frozen artifacts: %s" % st[:120])
    HEAD = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                          text=True, cwd=HERE).stdout.strip()
except Exception as e:                                    # pragma: no cover
    note("git check unavailable: %s" % e)
if drift:
    print("   INPUT DRIFT DETECTED -- STOPPING BEFORE ANY REPLAY:")
    for d in drift:
        print("     " + d)
    json.dump({"instrument": "wall_d2_f1_replay_uv_locality.py", "stage": "R0 integrity",
               "verdict": "STOPPED -- input drift", "drift": drift,
               "fence": "no replay performed; inputs preserved for adjudication"},
              open(RESULT_PATH, "w"), indent=2)
    sys.exit(2)
check(True, "all replay inputs match their recorded sha256 (a22b587 manifest + 94cfffc "
      "Phase-12 record/instrument) -- NO DRIFT", gate="R0")
check(all(sha(os.path.join(HERE, f)) == w for f, w in FROZEN.items()),
      "NO FROZEN FILE EDITED by the V4 amendment: v1 declarations, registry, v2, v3 all "
      "stand at their frozen sha256s; the correction lives in %s (sha256 %s...)"
      % (V4_DOC, (V4DOC_SHA or "")[:16]), gate="R0")
note("git HEAD at run start: %s" % HEAD)
note("V4 amendment cited by this replay: %s sha256 %s" % (V4_DOC, V4DOC_SHA))

reg = json.loads(open(os.path.join(HERE, "WALL_A_A3_REGISTRY.json")).read())
ren = reg["renormalisation"]
check(ren["counterterm_basis_frozen"] == ["Lambda (cosmological constant)", "G (EH term)",
                                          "R^2", "R_mn^2", "R_mnrs^2", "box R"],
      "A3 law: the counterterm basis is the frozen SIX-operator set", gate="R0")
check("d = 4 - eps" in ren["primary_scheme"],
      "A3 law: primary scheme is de Sitter-invariant dim-reg at d = 4 - eps", gate="R0")
check("MINIMAL SUBTRACTION" in ren["renormalisation_condition"]
      and "mu symbolic" in ren["renormalisation_condition"],
      "A3 law (F2): MINIMAL SUBTRACTION, pole terms only, mu symbolic (unchanged by V4)", gate="R0")
check("Pi_ren = Pi_local^scheme + Pi_nonlocal^invariant" in ren["split"],
      "A3 law: split convention Pi_ren = Pi_local^scheme + Pi_nonlocal^invariant", gate="R0")
check("polynomial in (omega^2, k^2)" in ren["split_audit"],
      "registry UNEDITED: the superseded F1 mirror wording is STILL on disk -- the "
      "correction lives in the V4 amendment document, not in a registry edit (W-0)", gate="R0")
check(str(v4rec.get("corrected_predicate", "")).startswith("Pi_local^scheme: local terms are finite polynomials"),
      "V4 record carries the corrected predicate: finite polynomial in (omega, k), "
      "coefficients finite in (m^2, H^2, mu)", gate="R0")
afb = json.loads(open(os.path.join(HERE, ".p11_af_basis_cache.txt")).read())
okstruct = (len(afb["QS"]) == 3
            and all(set(s.keys()) >= {"Lam", "EH", "R2", "Rmn2"} for s in afb["QS"])
            and all(set(s[o].keys()) >= {"0", "1", "2"} for s in afb["QS"]
                    for o in ("Lam", "EH", "R2", "Rmn2"))
            and len(afb["R0s"]) == 3)
check(okstruct, "corrected AF-basis cache structure intact (3 K-samples x 4 operators x "
      "H-orders {0,1,2} + R0s)", gate="R0")
stamp("R0 done")

# =====================================================================================
# R1 -- POLE-OBJECT RE-MATERIALISATION (cache-backed; NO loop regeneration) + IDENTITY
# =====================================================================================
print("\n=== R1: POLE-OBJECT RE-MATERIALISATION (fingerprint identity with 94cfffc) ===")
os.environ.setdefault("SKIPBAT", "1")     # identical to the Phase-12 construction load (disclosed there)
os.environ["AFB_LOAD"] = "1"              # corrected AF basis; hook disclosed + closed at a22b587
src = open(os.path.join(HERE, "wall_d2_phases8_12.py")).read()
MARK = "# ================= PHASE 11: IDENTIFICATION"
assert MARK in src, "machinery marker not found -- refusing to guess where to split"
_ns = {"__name__": "__main__", "__file__": os.path.join(HERE, "wall_d2_phases8_12.py")}
try:
    exec(compile(src.split(MARK)[0], "wall_d2_phases8_12.py", "exec"), _ns)
except SystemExit as e:                                    # pragma: no cover
    json.dump({"instrument": "wall_d2_f1_replay_uv_locality.py", "stage": "R1 construction load",
               "verdict": "STOPPED -- machinery exited (%s)" % e.code}, open(RESULT_PATH, "w"), indent=2)
    sys.exit(2)
SIG0, SIG1, SIG2 = _ns["SIG0"], _ns["SIG1"], _ns["SIG2"]
QS, K_SAMPLES = _ns["QS"], _ns["K_SAMPLES"]
om, kk, mm, H, c = _ns["om"], _ns["kk"], _ns["mm"], _ns["H"], _ns["c"]
OPS = ("Lam", "EH", "R2", "Rmn2")            # the cached four of the frozen six
PIN = {"Lam": mm**4 / 4, "EH": mm**2 / 12, "R2": sp.Rational(1, 240),
       "Rmn2": sp.Rational(1, 120)}          # the frozen Gilkey / 't Hooft-Veltman anchor
check(sha(P10) == EXPECTED[".p10_assembly_cache.txt"],
      "Phase-10 cache byte-stable across the machinery load (the loop target is "
      "immutable in fact; NO loop regeneration)", gate="R1")
P12 = json.loads(open(os.path.join(HERE, "WALL_D2_PHASE12_MS_SPLIT_RESULT.json")).read())
RECFPS = P12["pole_extraction"]["expression_fingerprints"]
SIG = {0: SIG0, 1: SIG1, 2: SIG2}
for n in (0, 1, 2):
    got = expr_fp(SIG[n])
    check(got == RECFPS[str(n)],
          "Sigma_%d re-materialised from the frozen caches is FINGERPRINT-IDENTICAL to "
          "the recorded pole object (%s == %s): the SAME object the Phase-12 verdict "
          "was issued on" % (n, got, RECFPS[str(n)]), gate="R1")
eps = sp.Symbol("eps", positive=True)
mu = sp.Symbol("mu", positive=True)
c_sym = sp.Symbol("c")
check(all(c_sym not in sp.expand(SIG[n]).free_symbols for n in (0, 1, 2)),
      "cached assemblies c-free (engine poles in units of c = 2/eps, applied at report "
      "time)", gate="R1")
TERMS = {n: sp.Add.make_args(sp.expand(SIG[n])) for n in (0, 1, 2)}
check(all(sp.expand(SIG[n] - sum(TERMS[n])) == 0 for n in (0, 1, 2)),
      "Add-args enumeration reconstructs each H order exactly (nothing dropped, nothing "
      "aggregated)", gate="R1")
Pi_bare = (2 / eps) * (SIG0 + H * SIG1 + H**2 * SIG2)
ze = sp.Symbol("zInv")
Pz = sp.Poly(sp.expand(Pi_bare.subs(eps, 1 / ze)), ze)
check(Pz.degree() == 1 and Pz.monoms() == [(1,)],
      "Pi_bare exactly LINEAR in 1/eps (degree 1, no 1/eps^2 artifacts) -- the pole "
      "object identity re-verified", gate="R1")
for n in (0, 1, 2):
    check(len(TERMS[n]) == int(P12["pole_extraction"]["census"]["H^%d" % n]["terms"]),
          "term census identical to the Phase-12 record at H^%d: %d terms"
          % (n, len(TERMS[n])), gate="R1")
note("the replay reuses the recorded pole object MECHANICALLY: same caches, same "
     "validated machinery load, fingerprint equality. What changes is ONLY the "
     "classifier (R2) -- independently implemented per the owner's authorization "
     "condition, so the superseded wording's defect cannot be inherited by copy.")
stamp("R1 done")

# =====================================================================================
# R2 -- LOCALITY UNDER THE V4-CORRECTED PREDICATE (INDEPENDENTLY IMPLEMENTED)
# =====================================================================================
print("\n=== R2: LOCALITY UNDER THE V4-CORRECTED PREDICATE (independent classifier) ===")
MOM = (om, kk)


def _route_tree(expr):
    """INDEPENDENT ROUTE 1 -- direct expression-tree analysis of the EXPANDED term
    (the V4 predicate; no sp.Poly anywhere). LOCAL iff:
      T1  omega/k never appear inside an applied-function argument (log, atan, exp,
          sqrt, ... -- any function of the momenta);
      T2  omega/k never appear with a negative exponent (no denominators);
      T3  every Pow exponent of omega/k is a non-negative Integer.
    Mechanically distinct from the Phase-12 S2 route (sp.Poly(t, om, kk) construction
    success), which this file never calls for classification -- the owner's
    authorization condition: no inherited defect."""
    ex = sp.expand(expr)
    for node in sp.preorder_traversal(ex):
        if isinstance(node, sp.Function):
            if any(s in node.free_symbols for s in MOM):
                return False                        # T1: function of a momentum
        elif isinstance(node, sp.Pow):
            if any(s in node.base.free_symbols for s in MOM):
                e = node.exp
                if not (e.is_Integer and e >= 0):
                    return False                    # T2/T3: denominator or non-integer
    return True


def _route_ispoly(expr):
    """INDEPENDENT ROUTE 2 -- sympy's Expr.is_polynomial(omega, k) predicate: an
    assumptions-query API, not Poly construction. A third mechanical route, distinct
    from both the tree walk and the Phase-12 sp.Poly route."""
    return bool(sp.expand(expr).is_polynomial(om, kk))


def local_v4(expr):
    """V4-corrected F1 predicate: returns the verdicts of the two independent routes."""
    return _route_tree(expr), _route_ispoly(expr)


def _term_parity(term):
    """(omega-exponent, k-exponent) of one Add-term, by direct factor inspection."""
    a = b = 0
    for f_ in sp.Mul.make_args(term):
        if f_ == om:
            a += 1
        elif f_ == kk:
            b += 1
        elif isinstance(f_, sp.Pow) and f_.base == om and f_.exp.is_Integer:
            a += int(f_.exp)
        elif isinstance(f_, sp.Pow) and f_.base == kk and f_.exp.is_Integer:
            b += int(f_.exp)
    return a, b


def literal_old(term):
    """the SUPERSEDED literal wording ('polynomial in (omega^2, k^2)'), implemented by
    monomial-exponent parity -- distinct from the a1282af diagnostic's substitution
    route and from Phase-12's literal_even (Poly.monoms). Used ONLY for the census
    demonstrating which local terms the old wording would have excluded."""
    return all(a % 2 == 0 and b % 2 == 0
               for (a, b) in (_term_parity(t) for t in sp.Add.make_args(sp.expand(term))))


# --- mechanical independence proof: no Poly reference in the classifier/census code
def _code_names(code):
    """every name referenced by this code object and all its nested code objects
    (bytecode-level; immune to docstring/comment mentions)."""
    names = set(code.co_names)
    for const in code.co_consts:
        if hasattr(const, "co_names"):
            names |= _code_names(const)
    return names


_cls_names = set()
for _fn in (_route_tree, _route_ispoly, _term_parity, literal_old):
    _cls_names |= _code_names(_fn.__code__)
check("Poly" not in _cls_names,
      "classifier INDEPENDENCE (mechanical, bytecode-level): the replay's classification/"
      "census code objects reference NO Poly symbol anywhere -- no inherited Phase-12 S2 "
      "code path (the owner's authorization condition, verified on compiled code, not "
      "asserted)", gate="R2")

# --- controls: the nonlocal witnesses and the local false-negative classes
E00, P00 = sp.Symbol("E_00"), sp.Symbol("P_00")
E11, P11 = sp.Symbol("E_11"), sp.Symbol("P_11")
E03 = sp.Symbol("E_03")
NEGATIVE = {
    "omega^2 log(omega^2+m^2)": om**2 * sp.log(om**2 + mm**2) * E00 * P00,
    "omega^4 / k^2": om**4 / kk**2 * E00 * P00,
    "log(-omega^2+k^2+m^2) [branch cut]": sp.log(-om**2 + kk**2 + mm**2) * E11 * P11,
    "omega*atan(k/m) [threshold-type]": om * sp.atan(kk / mm) * E00 * P00,
    "omega^2 log(k^2) [hostile case named in v1]": om**2 * sp.log(kk**2) * E00 * P00,
}
POSITIVE = {
    "omega k m^2 [local mixed-odd -- the false-negative class]": om * kk * mm**2 * E03 * P00,
    "omega m^2 [local single-odd]": om * mm**2 * E00 * P00,
    "omega^2 + k^2 [local even]": (om**2 + kk**2) * E00 * P00,
    "log(m^2/mu^2)*omega^2 [F1 coefficient log -- local]": sp.log(mm**2 / mu**2) * om**2 * E00 * P00,
}
for name, x in NEGATIVE.items():
    a, b = local_v4(x)
    check((not a) and (not b),
          "nonlocal witness REJECTED by BOTH independent routes (not subtractable): %s"
          % name, gate="R2")
for name, x in POSITIVE.items():
    a, b = local_v4(x)
    check(a and b,
          "local structure ACCEPTED by BOTH independent routes (the class the literal "
          "wording falsely excluded): %s" % name, gate="R2")

# --- the replay classification of the recorded pole object, term by term
LOC, NONLOC, DISAGREE = {}, {}, []
for n in (0, 1, 2):
    loc, nonloc = [], []
    for t in TERMS[n]:
        a, b = local_v4(t)
        if a != b:
            DISAGREE.append((n, str(t)[:80]))
        (loc if (a and b) else nonloc).append(t)
    LOC[n], NONLOC[n] = loc, nonloc
    print("   H^%d: %d/%d terms LOCAL under V4 (both independent routes); %d nonlocal"
          % (n, len(LOC[n]), len(TERMS[n]), len(NONLOC[n])))
TOTAL = sum(len(LOC[n]) for n in (0, 1, 2))
check(len(DISAGREE) == 0,
      "dual independent routes AGREE on all %d pole terms (no classification ambiguity "
      "between the tree walk and is_polynomial)" % TOTAL, gate="R2")
check(all(len(NONLOC[n]) == 0 for n in (0, 1, 2)),
      "V4 REPLAY VERDICT: every pole term at every H order is LOCAL (finite polynomial "
      "in (omega, k), coefficients finite in (m^2, H^2, mu)) -- nonlocal pole count 0, "
      "re-established under the corrected predicate with the independent classifier",
      gate="R2")
check(TOTAL == 208 and [len(LOC[n]) for n in (0, 1, 2)] == [112, 40, 56],
      "classification census identical to the Phase-12 record: 112/40/56 = 208 terms, "
      "all local (same verdict, independently derived)", gate="R2")

# --- literal-wording census: the defect, demonstrated live on the real object
MIXODD = {n: [t for t in LOC[n] if not literal_old(t)] for n in (0, 1, 2)}
for n in (0, 1, 2):
    rec = int(P12["locality_split"]["mixed_odd_literal_census"][str(n)])
    check(len(MIXODD[n]) == rec,
          "literal-wording census reproduced at H^%d: %d local terms carry mixed-odd "
          "monomials the SUPERSEDED wording would have excluded (all LOCAL under V4) "
          "-- the one-sided false-negative defect, live" % (n, len(MIXODD[n])), gate="R2")
note("the corrected predicate is NOT permissive (non-absorption, live): all five "
     "nonlocal witnesses above -- including v1's own named hostile cases omega^2 log(k^2) "
     "and omega^4/k^2 -- are rejected by both independent routes; only derivative "
     "structures (finite-derivative delta kernels) gain or hold local status")
stamp("R2 done")

# =====================================================================================
# R3 -- SUBTRACTION UNCHANGED (fingerprint + exact operator identities)
# =====================================================================================
print("\n=== R3: SUBTRACTION UNCHANGED (fingerprint equality + exact identities) ===")
LSUM = {n: sp.expand(sum(LOC[n])) for n in (0, 1, 2)}
check(all(sp.expand(LSUM[n] - SIG[n]) == 0 for n in (0, 1, 2)),
      "under V4 every pole term is subtractable: local sum == Sigma at every H order "
      "(the subtraction object is the pole object itself -- unchanged)", gate="R3")
Pi_local_MS = (2 / eps) * (LSUM[0] + H * LSUM[1] + H**2 * LSUM[2])
rec_ms = P12["ms_split"]["Pi_local_MS"]
rec_fp = rec_ms.split("fingerprint ")[-1].strip()
FPS = expr_fp(Pi_local_MS)
check(FPS == rec_fp,
      "Pi_local^MS FINGERPRINT-IDENTICAL to the frozen Phase-12 value (%s == %s): NO "
      "subtraction term has changed" % (FPS, rec_fp), gate="R3")
check(sp.expand(Pi_bare - Pi_local_MS) == 0,
      "split integrity re-derived: Pi_bare - Pi_local^MS = 0 with ZERO nonlocal pole "
      "residue (residual 0, exact)", gate="R3")
PzL = sp.Poly(sp.expand(Pi_local_MS.subs(eps, 1 / ze)), ze)
check(PzL.degree() == 1 and PzL.monoms() == [(1,)],
      "Pi_local^MS exactly degree 1 in 1/eps, no finite part (zero finite-part "
      "discretion unchanged)", gate="R3")
check(mu not in Pi_local_MS.free_symbols,
      "Pi_local^MS mu-free at pole order (pure MS, unchanged)", gate="R3")
for n, sign in ((0, 1), (1, -1), (2, 1)):
    for idx in range(3):
        ov, kv = K_SAMPLES[idx]
        tgt = sp.expand(SIG[n].subs({om: ov, kk: kv}))
        pred = sp.expand(sum(PIN[o] * QS[idx][o][n] for o in OPS))
        tag = "HELD-OUT" if idx == 2 else "fitting"
        sgn = "+" if sign > 0 else "-"
        check(sp.expand(tgt - sign * pred) == 0,
              "H^%d K=(%s,%s) [%s]: Sigma_%d == %s PIN*basis EXACTLY (m symbolic, "
              "frozen {m^4/4, m^2/12, 1/240, 1/120}, NO refit) -- the counterterm "
              "mapping is unchanged" % (n, ov, kv, tag, n, sgn), gate="R3")
CTA = P12["operator_mapping"]["counterterm_action"]
check(isinstance(CTA, str) and "m^4/4" in CTA and "R^2/240" in CTA and "R_mn^2/120" in CTA,
      "counterterm action carried VERBATIM from the Phase-12 record into the freeze "
      "(mechanical read-back, no retyping): %s" % CTA, gate="R3")
stamp("R3 done")

# =====================================================================================
# R4 -- EMISSIONS: replay result + UV FREEZE + ASSEMBLY-3 ENTRY OBJECT
# =====================================================================================
print("\n=== R4: EMISSIONS (replay result / UV freeze / ASSEMBLY-3 entry object) ===")


def pol(ex, pre):
    return sorted({q for q in sp.expand(ex).free_symbols if str(q).startswith(pre)}, key=str)


_allsyms = sp.expand(SIG2.subs({om: K_SAMPLES[0][0], kk: K_SAMPLES[0][1]}))
Es = pol(_allsyms, "E_") or pol(sum(QS[0][o][2] for o in OPS), "E_")
Ps = pol(_allsyms, "P_") or pol(sum(QS[0][o][2] for o in OPS), "P_")
for o in OPS:
    Es = sorted(set(Es) | set(pol(QS[0][o][2], "E_")), key=str)
    Ps = sorted(set(Ps) | set(pol(QS[0][o][2], "P_")), key=str)
SLOTS = [(e_, p_) for e_ in Es for p_ in Ps]
Eused, Pused = set(), set()
for n in (0, 1, 2):
    for idx in range(3):
        s = sp.expand(SIG[n].subs({om: K_SAMPLES[idx][0], kk: K_SAMPLES[idx][1]}))
        Eused |= set(pol(s, "E_"))
        Pused |= set(pol(s, "P_"))
check(Eused <= set(Es) and Pused <= set(Ps) and len(SLOTS) == len(Es) * len(Ps),
      "tensor slot map complete: %d E-symbols x %d P-symbols = %d slots covers every "
      "E/P symbol of the pole object at every K sample (span-test representation, "
      "re-materialised from the frozen cache)" % (len(Es), len(Ps), len(SLOTS)), gate="R4")

REPLAY = {
    "instrument": "wall_d2_f1_replay_uv_locality.py",
    "kind": "F1 GOVERNANCE REPLAY (owner-directed; V4 amendment enforcement)",
    "date": "2026-08-28",
    "git_head_at_run_start": HEAD,
    "amendment_cited": {"document": V4_DOC, "sha256": V4DOC_SHA, "record": V4_REC,
                        "record_cited_sha256": v4rec.get("amendment_document_sha256")},
    "classifier": {
        "requirement": "owner authorization condition: independently implemented -- no "
                       "verbatim S0/S1 copy that could reproduce the same defect",
        "route_1": "expression-tree analysis of the expanded term (T1 function args, "
                   "T2 denominators/negative exponents, T3 non-negative integer exponents)",
        "route_2": "sympy Expr.is_polynomial(omega, k) (assumptions query, NOT Poly construction)",
        "phase12_route_NOT_used": "sp.Poly(term, omega, k) construction success (the Phase-12 S2 path)",
        "literal_census_route": "monomial exponent parity (distinct from the a1282af "
                                "substitution route and Phase-12 literal_even)",
        "independence_guarantee": "no Poly call anywhere in the classifier/census routes "
                                  "(gated by source inspection, check gate R2)",
        "route_agreement": "perfect on all %d pole terms + all controls" % TOTAL,
    },
    "pole_object_identity": {
        "fingerprints": {str(n): expr_fp(SIG[n]) for n in (0, 1, 2)},
        "recorded_fingerprints": RECFPS,
        "identical": True,
        "term_census": {"H^0": len(TERMS[0]), "H^1": len(TERMS[1]), "H^2": len(TERMS[2])},
        "loop_regeneration": "NONE (cache-backed machinery load; Phase-10 cache byte-stable)",
    },
    "replay_verdict": {
        "local_terms": {str(n): len(LOC[n]) for n in (0, 1, 2)},
        "nonlocal_pole_terms": {str(n): len(NONLOC[n]) for n in (0, 1, 2)},
        "mixed_odd_literal_census": {str(n): len(MIXODD[n]) for n in (0, 1, 2)},
        "statement": "208/208 pole terms LOCAL under the V4-corrected predicate; zero "
                     "nonlocal UV-pole residue; the superseded wording would have "
                     "falsely excluded 28/40/8 of them (census reproduced)",
        "nonlocal_witnesses_rejected": sorted(NEGATIVE.keys()),
        "local_structures_accepted": sorted(POSITIVE.keys()),
    },
    "unchanged": {
        "Pi_local_MS_fingerprint": FPS,
        "recorded_fingerprint": rec_fp,
        "split_residual": 0,
        "operator_mapping": "Sigma_n == +/-PIN*basis EXACT at all K samples incl. "
                            "held-out, m symbolic, no refit (9 identities re-derived)",
        "counterterm_action": CTA,
    },
    "emissions": ["WALL_D2_F1_REPLAY_UV_LOCALITY_RESULT.json",
                  "WALL_D2_UV_FREEZE_RESULT.json",
                  "WALL_D2_ASSEMBLY3_ENTRY_OBJECT.json"],
    "inputs_verified": EXPECTED,
    "frozen_unedited": FROZEN,
    "verdict": None,
    "checks": CHECKS,
    "notes": NOTES,
    "fail_count": len(FAIL),
    "failures": FAIL,
    "fence": "GOVERNANCE ONLY: no loop regeneration, no finite eps^0 response computed, "
             "no Q1-Q5, no J(omega) comparison, no PV, no spectral classification. The "
             "finite nonlocal sector is NOT YET COMPUTED / TO_BE_DERIVED (ASSEMBLY-3, a "
             "separate task; owner review required before it begins). W-0; register "
             "untouched; nothing banked.",
}
REPLAY["verdict"] = ("GREEN -- V4 replay confirms the Phase-12 UV verdict under the "
                     "corrected predicate with an independent classifier; subtraction "
                     "unchanged" if not FAIL else "RED -- replay failures present")
json.dump(REPLAY, open(RESULT_PATH, "w"), indent=2, default=str)
check(json.loads(open(RESULT_PATH).read())["kind"].startswith("F1 GOVERNANCE REPLAY"),
      "replay result written and parses back: WALL_D2_F1_REPLAY_UV_LOCALITY_RESULT.json",
      gate="R4")

FREEZE = {
    "record": "WALL D2 -- UV FREEZE (local MS pole sector), governance-sealed",
    "date": "2026-08-28",
    "kind": "freeze of a COMPLETED result (owner-directed); NOT a new computation",
    "Pi_local_MS": {
        "expression": "(2/eps)(Sigma_0 + H Sigma_1 + H^2 Sigma_2)",
        "fingerprint": FPS,
        "identity": "fingerprint-identical to the Phase-12 record at 94cfffc and "
                    "re-derived in this replay from the cache-backed pole object under "
                    "the V4-corrected predicate (independent classifier)",
        "degree_in_1_over_eps": 1,
        "finite_part": "none (zero finite-part discretion)",
        "mu_content": "none at pole order (pure MS)",
    },
    "counterterm_action": CTA,
    "operator_attribution": {
        "H0": "Sigma_0 == +PIN*basis EXACT (all samples incl. held-out, m symbolic) -- the "
              "doubly verified Gilkey / 't Hooft-Veltman flat anchor {m^4/4, m^2/12, 1/240, 1/120}",
        "H1": "Sigma_1 == -PIN*basis EXACT (same scope) -- sign-flipped pinned prediction; "
              "T4 fence: recorded, NOT interpreted",
        "H2": "Sigma_2 == +PIN*basis EXACT (same scope)",
    },
    "nonlocal": {
        "pole_sector": "0 -- no nonlocal UV-pole residue; established at 94cfffc "
                       "(implemented derivative-structure predicate) and RE-ESTABLISHED "
                       "here under the V4-corrected predicate by the independent-classifier "
                       "replay (208/208 local)",
        "finite_eps0_sector": "NOT YET COMPUTED -- TO_BE_DERIVED by ASSEMBLY-3. "
                              "Pi_nonlocal^invariant is NOT to be described as evaluated "
                              "until that task completes and is owner-reviewed.",
    },
    "split_audit": "Pi_bare - Pi_local^MS - Pi_nonlocal(pole=0) = 0, residual 0, exact "
                   "(re-derived in this replay)",
    "provenance": {
        "phase12_result_commit": "94cfffc",
        "phase12_result_sha256": EXPECTED["WALL_D2_PHASE12_MS_SPLIT_RESULT.json"],
        "phase12_instrument_sha256": EXPECTED["wall_d2_phase12_ms_split.py"],
        "v4_amendment": {"document": V4_DOC, "sha256": V4DOC_SHA, "record": V4_REC},
        "replay_instrument": "wall_d2_f1_replay_uv_locality.py",
        "replay_result": "WALL_D2_F1_REPLAY_UV_LOCALITY_RESULT.json",
        "inputs": EXPECTED,
        "frozen_unedited": FROZEN,
        "git_head_at_run_start": HEAD,
    },
    "fence": "UV/local sector closed and sealed. NOTHING about the finite eps^0 nonlocal "
             "response, Q1-Q5, J(omega), PV robustness, or spectral behaviour is "
             "determined or implied by this freeze. W-0; register untouched; nothing banked.",
}
FREEZE_PATH = os.path.join(HERE, "WALL_D2_UV_FREEZE_RESULT.json")
if not FAIL:
    json.dump(FREEZE, open(FREEZE_PATH, "w"), indent=2, default=str)
    check(json.loads(open(FREEZE_PATH).read())["Pi_local_MS"]["fingerprint"] == FPS,
          "UV FREEZE written and parses back: WALL_D2_UV_FREEZE_RESULT.json "
          "(Pi_local^MS frozen at fingerprint %s; finite eps^0 sector NOT YET COMPUTED)"
          % FPS, gate="R4")
else:
    note("replay NOT green: UV freeze NOT emitted (no partial freezes)")

# --- the pre-registered questions, echoed VERBATIM from the frozen v1 DECLARATION 4
QTBL = [
    {"id": "Q1",
     "quantity": "Tensor decomposition of the loop integrand's nonlocal part onto the countersigned channel basis {P\u00b2, P\u2070\u02e2, X_sw, residue}",
     "inside": "Every nonlocal coefficient function multiplies ONLY structures in {P\u00b2, P\u2070\u02e2, X_sw}; residue = 0 or a recorded FINDING",
     "outside": "Any nonlocal coefficient multiplying a structure OUTSIDE the 3D family (P1, P0w, Xws, or a genuinely new structure) -- including coefficient functions that vanish only on-shell"},
    {"id": "Q2",
     "quantity": "a(\u03b7)-weighted time integrals acting on the a\u00b2 and a\u2074 vertex channels",
     "inside": "Bookkeeping only: convergence status of each channel declared per-channel; no placement verdict",
     "outside": "An ill-defined channel (non-convergent after the declared regularisation) -- reported as FINDING, not regularised ad hoc"},
    {"id": "Q3",
     "quantity": "Convergence-boundary diagnostic: Re \u03c7(0) = (2/\u03c0) \u222b Im \u03c7(\u03c9\u2032)/\u03c9\u2032 d\u03c9\u2032; spectral class s",
     "inside": "s \u2265 2: convergent (the registered benchmark's class)",
     "outside": "s \u2264 1: divergent -- reported as found; BLIND to which outcome favours the register"},
    {"id": "Q4",
     "quantity": "Reciprocity / detailed-balance diagnostic on the COMPUTED kernel (the closure test's mechanism, run on \u03a3_R^TT)",
     "inside": "Holds \u21d2 the equilibrium regime is established \u21d2 the 2D closure reduction is licensed for the computed response",
     "outside": "Fails \u21d2 the response family stays honestly 3D for this state; question (ii) answered NEGATIVE"},
    {"id": "Q5",
     "quantity": "Flat-limit reduction of \u03a0_nonlocal: the H \u2192 0 limit, per channel",
     "inside": "The limit exists per-channel and its decomposition onto the FLAT 3D family {P\u00b2, P\u2070\u02e2, X_sw} matches Q1's placement",
     "outside": "The limit fails to exist / does not commute with the decomposition (IR obstruction) -- a FINDING; the booked +1 is then UNDISCHARGEABLE via this route"},
]
Q_ADDENDA = {
    "Q1b_subrecord": "Q1b (sub-record, mandatory if Q1's X_sw coefficient \u2260 0): record the coefficient's (\u03c9-parity, H-parity) decomposition and its H \u2192 0 behaviour -- the closure test's interpretive frame (an X_sw piece odd in H and vanishing at H \u2192 0 is flat-limit-compatible; one surviving H \u2192 0 is a flat placement failure).",
    "Q3_gap_closed": "Q3 gap closed: 1 < s < 2 is INTERMEDIATE -- neither criterion covers it; reported as its own finding, never rounded to either side.",
    "Q4_predicate_pinned": "Q4 predicate pinned: the reciprocity diagnostic is the PROPER Onsager-Casimir test of the countersigned closure instrument (\u03b5-signature-corrected slot exchange; H treated as T-ODD) -- NOT the naive slot-symmetry test, which the closure review exhibited killing a legitimate Hall term. The implementation must cite wall_a_closure_premises.py / second_author_closure_premises.py.",
    "discharge_map": "THE +1 DISCHARGE MAP (pre-registered so no post-hoc interpretation is possible): the booked response_lorentz_covariance +1 is dischargeable ONLY by Q1 INSIDE and Q5 INSIDE, per the owner's discharge condition. Q3 and Q4 do NOT vote on the +1 -- they answer questions (iii) and (ii) respectively. Any discharge claim citing other evidence is invalid. (Discharge itself remains an owner ruling at the bank gate; this map only fixes what evidence could support one.)",
    "blind_rule_uv_neutrality": "Local counterterm contributions are listed per-term against the frozen basis and are EXCLUDED from all placement verdicts (they cannot vote on (i) or (iii)). No outcome may be inferred from the UV pole result.",
    "blind_rule_jomega": "The comparison with the registered J(\u03c9) happens ONLY in the separate post-assembly comparison stage (not inside ASSEMBLY-3).",
}

ENTRY = {
    "object": "Pi_nonlocal^invariant -- the finite (eps^0) retarded nonlocal kernel of the frozen Phase-10 assembly",
    "status": "TO_BE_DERIVED -- not computed, not evaluated, no property assumed; nothing in this object may be read as a prediction about it",
    "authority": {
        "owner_task": "F1 GOVERNANCE AMENDMENT + UV REPLAY + ASSEMBLY-3 PREPARATION (2026-08-28)",
        "declarations": {"v1": FROZEN["WALL_A_A3_DECLARATIONS.md"],
                         "v2": FROZEN["WALL_A_A3_DECLARATIONS_V2_AMENDMENT.md"],
                         "v3": FROZEN["WALL_A_A3_DECLARATIONS_V3_AMENDMENT.md"],
                         "v4": V4DOC_SHA},
        "hard_stop": "no finite-response computation, no Q1-Q5, no J(omega) comparison, no PV run, no spectral classification, no basis alteration, no refits, no operators added",
    },
    "tensor_slot_map": {
        "convention": "E_ab (ket slot) x P_cd (bra slot) coefficient symbols of the bilinear kernel",
        "E_symbols": [str(e_) for e_ in Es],
        "P_symbols": [str(p_) for p_ in Ps],
        "slots": len(SLOTS),
        "source": "re-materialised from the frozen caches (AF-BASIS-v1) by the governance replay; identical to the span-test representation",
    },
    "h_grading": {
        "pole_sector": "Pi_bare = (2/eps)(Sigma_0 + H Sigma_1 + H^2 Sigma_2) [fingerprint-recorded, frozen]",
        "finite_sector": "graded by the same H orders; to be derived at eps^0",
    },
    "conventions": {
        "omega_k": "d_t -> -i*omega, d_z -> -i*k (the machinery E-transform; the validated local-kernel transform (-i omega)^q for any q)",
        "poles": "engine poles in units of c = 2/eps (the measure pole), c applied at report time; cached assemblies c-free",
        "reference_centre": "centre-at-reference (machinery wall_d2_phases8_12.py: conformal chart, reference eta_bar with a(eta_bar)=1, u = eta - eta_bar; vertices at u1=+Delta/2, u2=-Delta/2; reference-centre evaluation u -> 0 taken ONLY AFTER all derivatives so the centre convention matches the loop side's -- the adjudicated consistent-centre class)",
        "split": "Pi_ren = Pi_local^scheme + Pi_nonlocal^invariant (A3 registry, unchanged)",
    },
    "locality_predicate": {
        "id": "F1 (V4-corrected)",
        "statement": "finite polynomial in (omega, k), coefficients finite in (m^2, H^2, mu); equivalently position-space finite sums of derivatives of delta functions",
        "amendment": "WALL_A_A3_DECLARATIONS_V4_AMENDMENT.md sha256 %s" % V4DOC_SHA,
        "superseded_wording": "polynomial in (omega^2, k^2)",
    },
    "subtraction": {
        "status": "COMPLETED AND FROZEN (see WALL_D2_UV_FREEZE_RESULT.json)",
        "Pi_local_MS": "(2/eps)(Sigma_0 + H Sigma_1 + H^2 Sigma_2)",
        "fingerprint": FPS,
        "counterterm_action": CTA,
        "replay": "fingerprint-identical under the governance replay; zero nonlocal pole residue (208/208 local, independent classifier)",
    },
    "input_identities": {
        "p10_cache": {"file": ".p10_assembly_cache.txt", "sha256": EXPECTED[".p10_assembly_cache.txt"], "tag": "L2repair-v1", "bytes": 28795},
        "p11_cache": {"file": ".p11_af_basis_cache.txt", "sha256": EXPECTED[".p11_af_basis_cache.txt"], "tag": "AF-BASIS-v1"},
        "machinery": {"file": "wall_d2_phases8_12.py", "sha256": EXPECTED["wall_d2_phases8_12.py"]},
        "span_test": {"file": "wall_d2_span_test.py", "sha256": EXPECTED["wall_d2_span_test.py"]},
        "phase11_instrument": {"file": "wall_d2_phase11_af_basis.py", "sha256": EXPECTED["wall_d2_phase11_af_basis.py"]},
        "registry": {"file": "WALL_A_A3_REGISTRY.json", "sha256": EXPECTED["WALL_A_A3_REGISTRY.json"]},
        "phase12": {"result": "WALL_D2_PHASE12_MS_SPLIT_RESULT.json", "sha256": EXPECTED["WALL_D2_PHASE12_MS_SPLIT_RESULT.json"], "commit": "94cfffc"},
    },
    "basis_labeling": {
        "frozen_six": ["Lambda (cosmological constant)", "G (EH term)", "R^2", "R_mn^2", "R_mnrs^2", "box R"],
        "computed_kernels": ["Lam", "EH", "R2", "Rmn2"],
        "riem2_boxr": "IDENTITY-DERIVED (K_Riem2 = 4 K_Rmn2 - K_R2 by the 4D Gauss-Bonnet total-derivative identity; K_boxR = 0 as an exact total derivative); NOT engine-verified; NON-LOAD-BEARING: the UV pole closes inside the computed four-operator sub-basis. This labeling MUST remain explicit through ASSEMBLY-3 (owner watch item, 2026-08-28).",
    },
    "pre_registered_questions": {
        "source": "WALL_A_A3_DECLARATIONS.md DECLARATION 4 (sha256 %s), echoed verbatim, unchanged" % FROZEN["WALL_A_A3_DECLARATIONS.md"],
        "table": QTBL,
        "addenda": Q_ADDENDA,
    },
    "pv_ordering": {
        "status": "NOT RUN -- and NOT to be run before the finite nonlocal object exists in the primary scheme",
        "rule": "PV enters only at the frozen robustness stage, and only if the frozen ASSEMBLY-3 ordering explicitly places it before the first response verdict (owner adjudication required otherwise)",
        "protocol": "nonlocal low-frequency analytic structure must AGREE across schemes; disagreement is a recorded FINDING, never averaged; local pole content excluded from the comparison; no scheme averaging",
    },
    "next_task": "ASSEMBLY-3: derive the finite eps^0 nonlocal response of the frozen Phase-10 assembly and adjudicate Q1/Q2/Q3/Q4/Q5 exactly as pre-registered (owner review required before finite-response assembly begins)",
    "provenance": {"entry_object_emitted_by": "wall_d2_f1_replay_uv_locality.py", "git_head_at_run_start": HEAD, "date": "2026-08-28"},
}
ENTRY_PATH = os.path.join(HERE, "WALL_D2_ASSEMBLY3_ENTRY_OBJECT.json")
if not FAIL:
    json.dump(ENTRY, open(ENTRY_PATH, "w"), indent=2, default=str)
    _eb = json.loads(open(ENTRY_PATH).read())
    check(_eb["status"].startswith("TO_BE_DERIVED") and len(_eb["pre_registered_questions"]["table"]) == 5,
          "ASSEMBLY-3 ENTRY OBJECT written and parses back: WALL_D2_ASSEMBLY3_ENTRY_OBJECT.json "
          "(status TO_BE_DERIVED; Q1-Q5 echoed verbatim; slot map %d slots; corrected F1 "
          "cited; frozen subtraction cited; PV ordering recorded as NOT RUN)"
          % _eb["tensor_slot_map"]["slots"], gate="R4")
else:
    note("replay NOT green: ASSEMBLY-3 entry object NOT emitted (no partial handoff)")
stamp("R4 done")

print("\nverdict: %s" % ("GREEN" if not FAIL else "RED (%d failures)" % len(FAIL)))
for f_ in FAIL:
    print("  FAIL: " + str(f_))
note("HARD STOP after R4: the finite eps^0 nonlocal response is NOT YET COMPUTED; "
     "ASSEMBLY-3 is a separate task and requires owner review before it begins")
sys.exit(0 if not FAIL else 1)

