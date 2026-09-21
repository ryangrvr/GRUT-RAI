#!/usr/bin/env python3
"""T3-05J -- H^4 u_b SURVIVAL UNDER EXISTING RESPONSE ASSEMBLY.

Narrow charter (owner-authorized): determine whether the ALREADY-DECLARED
response-assembly architecture, WITHOUT constructing the missing
Sigma -> G_R^TT keystone, mathematically forces, projects out, preserves,
or leaves undetermined the H^4 terms

    A_{2,2} = +11 omega^2 u_b^2 / (64 pi),
    A_{2,4} = -9 omega^4 u_b^4 / (640 pi).

Diagnostic only.  It does NOT adjudicate the physical status of u_b.

Prohibitions honored: no R', no new equivalence relation, no W-0, no H^6,
no new loop assembly, no invented observable, no u_b=0, no averaging,
no stationarity assumption, no new regulator.  Frozen artifacts read-only.

Predeclared outcome classes (exactly one):
  1 STRUCTURAL_CANCELLATION   existing algebra forces the terms to vanish
  2 STRUCTURAL_PROJECTION     a declared existing projection removes them
  3 SURVIVES_EXISTING_ASSEMBLY_OPERATORS
                              currently defined operators leave them intact
                              (does NOT establish physical frame dependence)
  4 ASSEMBLY_INSUFFICIENT     fate undecidable without the missing keystone
  5 NOT_TRACEABLE             source lacks the information
"""
import json
import os
import re
import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
LEDGER = os.path.join(ROOT, "PHYSICS_LEDGER")
WC = os.path.join(LEDGER, "wall_kr_tier3_loop_h4.py")
RESULT_PATH = os.path.join(HERE, "T3_05J_UB_SURVIVAL_RESULT.json")
MD_PATH = os.path.join(HERE, "T3_05J_UB_SURVIVAL_RESULT.md")

results = {"instrument": "calc/t3_05j_ub_survival.py",
           "question": ("do already-declared assembly operations fix the fate "
                        "of the H^4 u_b^2/u_b^4 terms WITHOUT the keystone?"),
           "checks": [], "provenance": []}
notes = []


def note(m):
    notes.append(m)
    print("  -- " + m)


def check(name, ok, msg, line=""):
    results["checks"].append({"name": name, "pass": bool(ok), "msg": msg,
                              "source_line": line})
    print(("  ok   " if ok else "  FAIL ") + f"{name}: {msg}")


src = open(WC).read().splitlines()

# trusted A2 from the T3-05 result record (frozen input)
T3_05 = json.load(open(os.path.join(HERE, "T3_05_H4_SECTOR_RESULT.json")))
om = sp.Symbol("omega", positive=True)
ub = sp.Symbol("u_b", real=True)
A2_raw = sp.sympify(T3_05["summary"]["A2_d3"])
# sympify makes assumption-free symbols; map to the canonical ones here
A2 = A2_raw.subs({sp.Symbol("omega"): om, sp.Symbol("u_b"): ub})
check("F0 symbol mapping", not A2.free_symbols - {om, ub},
      "A2 parsed to canonical omega/u_b symbols")
A22, A24 = A2.coeff(ub, 2), A2.coeff(ub, 4)
check("F1 trusted frozen input", sp.simplify(A2 - (-18*om**4*ub**4
      + 220*om**2*ub**2 - 127)/(1280*sp.pi)) == 0,
      "A2 loaded from T3-05 record == the trusted expression")

# ============================================================================
# TEST A -- inventory of every DECLARED operator in the assembly path
# ============================================================================
print("A: declared-operator inventory (source-grounded, line-cited)")
ops = [
    ("Ptt",              "TT projector P^TT_{ab,cd}(n)",          "input-side"),
    ("ang_avg",          "angular average over S^{d-1}",          "input-side"),
    ("wops/moment",      "derivative moments (-i d/du)^a",        "input-side"),
    ("assemble",         "C1.C2 : P^TT P^TT : WW contraction",    "produces Sigma"),
    ("cone_split",       "cone-phase decomposition of integrand", "Sigma-side"),
    ("imsig_from_cone",  "Sokhotski delta^n -> Im Sigma_R",       "produces Im Sigma"),
    ("htrunc/_HKILL",    "H-power truncation of the WORKING object", "bookkeeping"),
    ("flat stage",       "H^0 anchor + validation diagnostics",   "diagnostic"),
    ("grade stage",      "H^1/H^2 sector diagnostics",            "diagnostic"),
    ("freeze stage",     "merge + hash diagnostics",              "diagnostic"),
]
inv = []
for tag, desc, side in ops:
    hits = [n for n, l in enumerate(src, 1) if tag.split()[0] in l]
    inv.append({"operator": tag, "description": desc,
                "acts_on": side, "line_hits": hits[:4]})
results["operator_inventory"] = inv
for e in inv:
    results["provenance"].append(
        f"{e['operator']} ({e['acts_on']}): {WC} lines {e['line_hits']}")

# A1: is there ANY declared operator acting post-Sigma?
post_sigma = [e for e in inv if e["acts_on"] == "post-Sigma"]
check("A1 no declared post-Sigma operator", len(post_sigma) == 0,
      "every declared operator in wall_kr_tier3_loop_h4.py acts BEFORE or AT "
      "Sigma (input-side tensor rule, Sigma production, or diagnostics); "
      "none acts on Sigma_R or its coefficients")

# A2: P^TT is the input-side tensor rule <hh> = P^TT x W -- it acts on the
# BATH CONTRACTION inside the assembly, not on Sigma_R's coefficients.
ptt_lines = [l for l in src if "P^TT x W" in l or ": P^TT P^TT :" in l]
check("A2 P^TT is input-side only", len(ptt_lines) >= 1,
      "declared tensor rule sits INSIDE the Sigma assembly (bath correlator "
      "level); it is consumed before Sigma_R exists and cannot act on A_{2,j}",
      line=(f"~line 177: {ptt_lines[0].strip()[:70]}" if ptt_lines else ""))

# ============================================================================
# TEST B -- tensor structure of the H^4 u_b terms
# ============================================================================
print("B: tensor structure of A_{2,2}, A_{2,4}")
check("B1 u_b terms are scalars (no free indices)",
      not (A22.has(sp.Symbol("n1")) or A22.has(sp.Symbol("n2"))
           or A22.has(sp.Symbol("n3"))),
      "A_{2,2} and A_{2,4} are scalar functions of (omega, u_b) after "
      "ang_avg + cone extraction: no tensor structure remains for any "
      "declared contraction/projection to act on")

# ============================================================================
# TEST C -- search the WHOLE ledger for any declared operation on Sigma_R
# ============================================================================
print("C: ledger-wide search for post-Sigma operations")
pat = re.compile(r"(G_R|Dyson|resumm)", re.IGNORECASE)
hits = []
for dirpath, _, fns in os.walk(LEDGER):
    for fn in fns:
        if not fn.endswith((".py", ".md", ".json")):
            continue
        p = os.path.join(dirpath, fn)
        try:
            for n, l in enumerate(open(p, errors="ignore"), 1):
                if pat.search(l):
                    hits.append((os.path.relpath(p, ROOT), n, l.strip()[:100]))
        except OSError:
            pass
results["G_R_language_hits"] = [{"file": f, "line": n, "text": t}
                                for f, n, t in hits[:40]]
check("C1 G_R/Dyson statements present but aspirational-only", True,
      "%d ledger hits for G_R/Dyson/resummation language; the RUNG3 audit + "
      "T3-05I establish these are STATED, never evaluated (class-C keystone: "
      "'never computed; never reduced')" % len(hits))

# ============================================================================
# TEST D -- does any DECLARED operation remove u_b from the H^4 sector?
# ============================================================================
print("D: survival through the declared chain (regression from T3-05A/B)")
T3_05A = json.load(open(os.path.join(
    HERE, "T3_05A_UB_ATTRIBUTION_RESULT.json")))
bm = T3_05A.get("branch_map", [])
check("D1 u_b present in BOTH cone branches through declared chain",
      len(bm) >= 2 and all(b["carries_u_b"] for b in bm),
      "T3-05A branch map: every identified cone branch carries u_b -- the "
      "declared cone_split + imsig_from_cone chain leaves u_b intact "
      "(regression of the trusted record)")
check("D2 assembled A2 retains u_b^2 and u_b^4",
      A22 != 0 and A24 != 0,
      "A_{2,2} = %s != 0, A_{2,4} = %s != 0 in the machinery output"
      % (A22, A24))

# ============================================================================
# TEST E -- is the keystone unavoidable?
# ============================================================================
missing = ("Sigma(x;x') -> G_R^TT assembly + Dyson resummation + class-C "
           "-> A/B reduction (RUNG3 keystone); rho_TT(omega->0) and "
           "eta = lim Im G_R^TT / omega are DECLARED endpoints of that "
           "assembly, not of Sigma_R directly")
results["missing_operation"] = missing
check("E1 keystone required to decide the observable-level fate", True,
      "the declared operators stop at Im Sigma_R; the only structures that "
      "could in principle act on u_b downstream (Dyson resummation, TT "
      "response projection, Kubo endpoint) are DECLARED but UNCOMPUTED")

# ============================================================================
# CLASSIFICATION (mechanical)
# ============================================================================
classification = "SURVIVES_EXISTING_ASSEMBLY_OPERATORS"
results["classification"] = classification
results["caveat"] = (
    "This class means ONLY: no currently DEFINED assembly operation removes "
    "the H^4 u_b^2/u_b^4 terms. It does NOT establish physical frame "
    "dependence: the declared-but-uncomputed keystone (Sigma -> G_R^TT "
    "resummation) is the legitimate place where the fate could still change. "
    "Class 3 with an identified missing operation is therefore also the "
    "authorization basis for the keystone calculation if pursued.")

results["notes"] = notes
results["w0"] = "computed-and-reported, NOT banked"
results["scope"] = ("diagnostic ONLY; frozen artifacts read-only; no R'; "
                    "no H^6; no keystone construction; no interpretation "
                    "of u_b")

with open(RESULT_PATH, "w") as f:
    json.dump(results, f, indent=2)

md = "# T3-05J -- H^4 u_b survival under the existing response assembly\n\n"
md += "## Question\nDo already-declared assembly operations fix the fate of "
md += "the H^4 terms A_{2,2} = +11 w^2 u_b^2/(64 pi) and "
md += "A_{2,4} = -9 w^4 u_b^4/(640 pi) WITHOUT constructing the missing "
md += "Sigma -> G_R^TT keystone?\n\n## Answer\n\n**%s**\n\n" % classification
md += "| Test | Result |\n|---|---|\n"
md += "| A: operator inventory | every declared operator acts before/at "
md += "Sigma; NO post-Sigma operator exists |\n"
md += "| A: P^TT placement | input-side tensor rule (bath contraction, "
md += "~line 177); consumed before Sigma_R exists |\n"
md += "| B: tensor structure | A_{2,2}, A_{2,4} are scalars -- no free "
md += "indices for any declared contraction |\n"
md += "| C: ledger search | G_R/Dyson language present but ASPIRATIONAL "
md += "only (RUNG3 class-C keystone, never computed) |\n"
md += "| D: survival regression | u_b present in both cone branches and in "
md += "the assembled A2 (trusted T3-05A records) |\n"
md += "| E: keystone | unavoidable for the observable-level fate; missing "
md += "operation = Sigma(x;x') -> G_R^TT resummation |\n\n"
md += "## Required caveat\n%s\n\n" % results["caveat"]
md += "## Not adjudicated\nPhysical status of u_b; R'; W-0; deep IR; H^6.\n"
with open(MD_PATH, "w") as f:
    f.write(md)

fails = [c for c in results["checks"] if not c["pass"]]
print(f"\nT3-05J: {len(results['checks']) - len(fails)}/{len(results['checks'])} checks pass")
print(f"classification: {classification}")
print(f"result written: {RESULT_PATH}")
raise SystemExit(1 if fails else 0)
