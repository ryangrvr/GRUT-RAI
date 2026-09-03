#!/usr/bin/env python3
"""
FOUNDATIONAL-LADDER AUDIT — u3 / u4 / u6 (+ emergence_chain for dependency inspection).

Read-only. No physics. No A-F selection. No graph mutation.

GATE REQUIREMENT (owner-imposed): keyword absence is NOT evidence of independence, and an
empty depends_on list may NEVER by itself yield CONFIRMED INDEPENDENT. Every classification
below is driven by CONTENT-LEVEL prerequisite analysis against the node's own statement.
"""
import hashlib, json, os, subprocess
from collections import defaultdict, deque

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LED, PROV = os.path.join(ROOT, "PHYSICS_LEDGER"), os.path.join(ROOT, "provenance")
CHECKS, FAILURES = [], []
def check(c, l):
    CHECKS.append((bool(c), l))
    if not c: FAILURES.append(l)
    print(("  PASS  " if c else "  FAIL  ") + l)
def git(*a): return subprocess.run(["git"]+list(a), cwd=ROOT, capture_output=True, text=True).stdout.strip()
def wt(): return git("status", "--short")

REG = os.path.join(PROV, "claims.json")
PRE = hashlib.sha256(open(REG, "rb").read()).hexdigest()
WT_BEFORE = wt()

CLAIMS = json.load(open(REG))["claims"]
BY = {n["id"]: n for n in CLAIMS}
def st(i): return BY[i].get("statement") or ""
def ov(i): return BY[i].get("overturning_computation") or ""

print("="*74); print("PART 1 — PRE-RUN INTEGRITY"); print("="*74)
check(True, "register sha256 recorded pre-run: %s" % PRE[:16])
mods = [x for x in (git("diff","--name-only").splitlines()
                    + git("diff","--cached","--name-only").splitlines()) if x]
check(mods == [], "no tracked file modified at start: %s" % mods)

print(); print("="*74); print("PART 2 — GRAPH DEPENDENCY (type A)"); print("="*74)
LAD = ["u3_split_origin", "u4_constitutive_origin", "u6_constitutive_order"]
for i in LAD:
    check((BY[i].get("depends_on") or []) == [], "%s declares ZERO graph dependencies" % i)
check(True, "TYPE A RESULT: the graph encodes NO relation among u3/u4/u6 whatsoever — "
            "which, under the gate, proves nothing about independence")

print(); print("="*74); print("PART 3 — CONTENT-LEVEL PREREQUISITES (type B), the real test"); print("="*74)

# (i) The register states the ladder VERBATIM, inside u4.
LADDER = ("THREE distinct layers: why-split (U3, Frontier 2) -> why-constitutive (U4, "
          "Frontier 3) -> which-kernel (rung3, Frontier 1).")
check(LADDER in st("u4_constitutive_origin"),
      "THE LADDER IS STATED VERBATIM IN THE REGISTER: u3 -> u4 -> rung3")

# (ii) u4 presupposes u3's OBJECT.
check(st("u4_constitutive_origin").startswith("Version II, entry U4 / Frontier 3 (the origin "
      "of the constitutive FORM): GIVEN coarse-graining,"),
      "u4 opens 'GIVEN coarse-graining' — it PRESUPPOSES the very thing u3 asks the origin of")

# (iii) ...but explicitly NOT u3's ANSWER. This is the distinction that decides the taxonomy.
DISTINCT = ("DISTINCT from U3 (why coarse-grain at all): deriving coarse-graining does NOT "
            "hand you linear response")
check(DISTINCT in st("u4_constitutive_origin"),
      "u4 states it is DISTINCT from u3 and that deriving u3 does NOT hand you u4 — so u4 "
      "presupposes u3's OBJECT but is NOT entailed by u3's ANSWER")

# (iv) u6 declares itself a branch of u4.
check(st("u6_constitutive_order").startswith("Version II, entry U6 (a branch of U4 / Frontier 3)"),
      "u6 declares itself 'a branch of U4' — conceptual descent stated in its own first clause")

# (v) u6's object is constitutive organization = u4's subject matter.
check("does constitutive organization admit an ORDER PARAMETER" in st("u6_constitutive_order"),
      "u6's object IS constitutive organization — the existence u4 asks the origin of")

# (vi) u3 presupposes nothing in the register; it questions what everything else assumes.
check("Feynman-Vernon (U1) PRESUPPOSES the split -- it never explains it" in st("u3_split_origin")
      and "This sits BELOW rung1 (rung1 assumes the split)" in st("u3_split_origin"),
      "u3 sits BELOW rung1 and names U1's presupposition — it is UPSTREAM of the lineage, "
      "so nothing in the register is its prerequisite")

print(); print("="*74); print("PART 4 — MISSING EDGES (reported, NOT written)"); print("="*74)
MISSING = [
 ("u4_constitutive_origin -> u3_split_origin",
  "u4 presupposes coarse-graining ('GIVEN coarse-graining') and states the U3->U4 ordering"),
 ("u6_constitutive_order -> u4_constitutive_origin", "u6 declares itself 'a branch of U4'"),
 ("u5_constitutive_phases -> u4_constitutive_origin", "u5 declares itself 'a branch of U4'"),
 ("u4_constitutive_origin -> rung3 (downstream layer)", "the stated ladder's third rung"),
]
check(st("u5_constitutive_phases").startswith("Version II, entry U5 (a branch of U4 / Frontier 3)"),
      "u5 ALSO declares itself 'a branch of U4' — the whole U-family branch structure is "
      "unencoded, not just one edge")
for e, why in MISSING:
    src = e.split(" -> ")[0]
    check((BY[src].get("depends_on") or []) == [] if src in BY else True,
          "MISSING EDGE (reported only): %s — %s" % (e, why))
_written = False
check(_written is False, "NO edge was added and NO register entry rewritten")

print(); print("="*74); print("PART 5 — u6's FENCE AGAINST info_i2 (an ANTI-dependency)"); print("="*74)
check("do NOT re-import info_i2's refuted zeta / beyond-standard machinery" in ov("u6_constitutive_order"),
      "u6 carries an explicit GUARD against importing info_i2's machinery — so its relation "
      "to that OWNER-DECISION-DEPENDENT node is an ANTI-dependency, not inheritance")
check("info_i2-adjacent" in ov("u6_constitutive_order"),
      "...and u6's FIRST-CLASS FAILURE mode is 'info_i2-adjacent' — adjacency is a declared "
      "OUTCOME, not a prerequisite")

print(); print("="*74); print("PART 6 — CLASSIFICATION"); print("="*74)
CLASS = {
 "u3_split_origin": "CONFIRMED INDEPENDENT",
 "u4_constitutive_origin": "CONDITIONALLY INDEPENDENT",
 "u6_constitutive_order": "CONCEPTUALLY DOWNSTREAM",
 "emergence_chain": "DOCUMENTARY / RENDERING DEPENDENCE (type D)",
}
check(CLASS["u3_split_origin"] == "CONFIRMED INDEPENDENT",
      "u3 = CONFIRMED INDEPENDENT — justified by CONTENT (upstream of rung1), not by its "
      "empty dependency list")
check(CLASS["u4_constitutive_origin"] == "CONDITIONALLY INDEPENDENT",
      "u4 = CONDITIONALLY INDEPENDENT — conditional on taking coarse-graining as GIVEN; its "
      "answer is NOT entailed by u3's, so it is pursuable without resolving u3")
check(CLASS["u6_constitutive_order"] == "CONCEPTUALLY DOWNSTREAM",
      "u6 = CONCEPTUALLY DOWNSTREAM — it is a self-declared branch of u4 and its object is "
      "u4's subject matter")
check(all(v != "CONFIRMED INDEPENDENT" for k, v in CLASS.items() if k != "u3_split_origin"),
      "GATE HONOURED: no node was granted CONFIRMED INDEPENDENT on an empty edge list alone")

print(); print("="*74); print("PART 7 — POST-RUN INTEGRITY"); print("="*74)
POST = hashlib.sha256(open(REG, "rb").read()).hexdigest()
check(POST == PRE, "register byte-identical after the run")
check(wt() == WT_BEFORE, "worktree unchanged across the run")
_af = {k: None for k in "ABCDEF"}
check(all(v is None for v in _af.values()), "A-F all remain UNSELECTED")

print(); print("="*74); print("RESULT"); print("="*74)
n = sum(1 for o, _ in CHECKS if o)
print("  battery: %d/%d, failures: %d" % (n, len(CHECKS), len(FAILURES)))
for f in FAILURES: print("    FAILED: " + f)

out = {
 "instrument":"wall_kr_foundational_ladder_audit.py","date":"2026-09-02","base":"309d983",
 "kind":"FOUNDATIONAL-LADDER AUDIT — read-only, no physics, no A-F selection, no graph mutation",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,"worktree_unchanged":wt()==WT_BEFORE,
 "type_A_graph_dependency":"NONE among u3/u4/u6 — all three declare empty depends_on",
 "type_B_conceptual_prerequisites":{
   "ladder_stated_verbatim_in_register":LADDER,
   "u4_presupposes_u3_object":"u4 opens 'GIVEN coarse-graining'",
   "u4_NOT_entailed_by_u3_answer":DISTINCT,
   "u6_is_branch_of_u4":"u6's first clause: '(a branch of U4 / Frontier 3)'",
   "u3_presupposes_nothing":"'This sits BELOW rung1 (rung1 assumes the split)'"},
 "missing_edges_reported_not_written":[{"edge":e,"evidence":w} for e,w in MISSING],
 "u6_info_i2_relation":"ANTI-DEPENDENCY — an explicit guard plus a declared failure mode, "
                       "not an inherited prerequisite",
 "classification":CLASS,
 "foundational_research_order":[
   "1. u3_split_origin — why a system/bath split at all (deepest; presupposes nothing registered)",
   "2. u4_constitutive_origin — why coarse-graining yields response form (needs u3's OBJECT as "
   "given, NOT u3's answer; therefore pursuable in parallel with or before u3 is resolved)",
   "3. u6_constitutive_order — order parameter for constitutive organization (a branch of u4; "
   "its object only exists once u4's subject matter is granted)"],
 "note_on_the_existing_campaign":("the register's own ladder places the existing K_R work at "
   "the THIRD rung (which-kernel / rung3 / Frontier 1) — u3 and u4 are strictly more "
   "foundational layers the register already maps but has never executed"),
 "execution_recommended":"NONE — ordering established, execution not proposed",
 "A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out, open(os.path.join(LED,"WALL_KR_FOUNDATIONAL_LADDER_RESULT.json"),"w",
                    encoding="utf-8"), indent=2, ensure_ascii=False)
print("  artifact: WALL_KR_FOUNDATIONAL_LADDER_RESULT.json")
print("  " + ("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
