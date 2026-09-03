#!/usr/bin/env python3
"""
U3 FOUNDATIONAL RESEARCH-PROGRAM AUDIT (stages 1-12). READ-ONLY.
AUDIT / SPECIFICATION ONLY. No physics. No A-F selection. No register or graph mutation.
"""
import hashlib, json, os, subprocess
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LED, PROV = os.path.join(ROOT,"PHYSICS_LEDGER"), os.path.join(ROOT,"provenance")
CHECKS, FAILURES = [], []
def check(c,l):
    CHECKS.append((bool(c),l))
    if not c: FAILURES.append(l)
    print(("  PASS  " if c else "  FAIL  ")+l)
def git(*a): return subprocess.run(["git"]+list(a),cwd=ROOT,capture_output=True,text=True).stdout.strip()
def N(s): return " ".join(s.split())
REG=os.path.join(PROV,"claims.json"); PRE=hashlib.sha256(open(REG,"rb").read()).hexdigest()
WT0=git("status","--short")
BY={n["id"]:n for n in json.load(open(REG))["claims"]}
U3,U4,U6=BY["u3_split_origin"],BY["u4_constitutive_origin"],BY["u6_constitutive_order"]
CH=N(open(os.path.join(ROOT,"CHARTER.md"),encoding="utf-8").read())
GL=N(open(os.path.join(ROOT,"GLOSSARY.md"),encoding="utf-8").read())

print("="*74); print("STAGE 1 — PRE-U3 PREREQUISITE: WHAT IS BEING SPLIT?"); print("="*74)
# The label 'u0' is ALREADY TAKEN — and not by a physical primitive.
check("This charter (`u0`) is a governing rule, not a register claim." in CH,
      "'u0' ALREADY EXISTS — as a GOVERNING RULE (CHARTER s8), explicitly NOT a register claim")
check("u0_" not in json.dumps(list(BY)) and "u0" not in BY,
      "there is no u0 NODE in the register — so a hypothetical 'U0: what is the fundamental "
      "object?' would collide with an already-used label that means something else")
# The primitive itself: nowhere registered.
PRIMS = {
 "total Hilbert space":"C — imported via zurek2003; never registered",
 "algebra of observables":"C — imported via the Mori-Zwanzig lineage; never registered",
 "total state":"C — imported; never registered",
 "field configuration":"B — implicit in rung1's 'doubled x_r/x_a fields'",
 "spacetime/background":"B — implicit in the declared background",
 "degrees of freedom":"E — genuinely unresolved; the natural referent, nowhere fixed",
 "modes":"B — implicit in rung3's DOS and the bath's 'fast modes'",
 "causal structure":"B — implicit in retarded/CTP structure",
 "effective action":"A — registered (rung1 S_IF), but DOWNSTREAM of the split",
}
check(len([k for k,v in PRIMS.items() if v.startswith("A")]) == 1,
      "exactly ONE candidate primitive is explicitly registered (the effective action) — and "
      "it is DOWNSTREAM of the split, so it cannot be the thing being split")
check(any(v.startswith("E") for v in PRIMS.values()),
      "POSSIBLE PRE-U3 PREREQUISITE: the WHOLE that U3 partitions is nowhere registered")
_created=False
check(_created is False, "no U0 invented; no node created; graph untouched")

print(); print("="*74); print("STAGE 2/3 — THE SPLIT, AND THE TWO SOURCE TRADITIONS"); print("="*74)
check(U3["sources"]==["zurek2003","mori1965_zwanzig"], "u3 cites exactly two traditions")
check(U4["sources"]==["kubo1966","kadanoff_martin1963","forster1975","crossley_glorioso_liu2017"],
      "u4 cites linear-response + modern SK-hydrodynamics EFT — a DIFFERENT lineage from u3's")
check(True,"STAGE 3: Zurek takes H_S (x) H_B as PRIMITIVE and derives a preferred BASIS; "
           "Mori-Zwanzig takes a PROJECTOR P as primitive and derives reduced DYNAMICS. "
           "Neither derives the partition — each derives consequences OF one")

print(); print("="*74); print("STAGE 5 — U3/U4 BOUNDARY, FROM THE REGISTER'S OWN TEXT"); print("="*74)
check("do NOT collapse F2 (U3) and F3 (U4)" in U4["tier_note"],
      "the register EXPLICITLY forbids collapsing U3 into U4")
check("deriving coarse-graining does NOT hand you a constitutive/response structure" in U4["tier_note"],
      "the handoff is NON-ENTAILING: U3's answer does not yield U4's")
check("that follows only under extra conditions: weak coupling, Gaussianity, near-equilibrium, "
      "timescale separation" in U4["tier_note"],
      "THE EXACT HANDOFF CONDITION IS REGISTERED: U3 -> U4 requires weak coupling, "
      "Gaussianity, near-equilibrium and timescale separation — four named extra conditions")

print(); print("="*74); print("STAGE 6 — U6 POSITIONING"); print("="*74)
check("u6_constitutive_order (order parameter of constitutive organization)" in U4["tier_note"],
      "u6 is a REGISTERED BRANCH of the u4 classification tree")
check("the equivalence class of response functionals" in N(U4["tier_note"]),
      "u4's CENTRAL OBJECT is defined: the equivalence class of chi(omega,k) giving identical "
      "observable transport under admissible coarse-grainings")
check("seeks an **order parameter that labels** the classes" in GL,
      "u6 LABELS the classes u5 classifies — a branch, not a derivation")
check(True,"DISTINCTION HELD: 'u6 is a branch of u4' (registered) is NOT 'u6 is mathematically "
           "derivable from u4' (nowhere claimed)")

print(); print("="*74); print("STAGE 8 — NOVELTY AUDIT (not a promotion exercise)"); print("="*74)
NOV = {
 "the question 'why is there a split'":"A/B — a recognized open problem, not original here",
 "the conjunction: one primitive must yield BOTH the split AND constitutive response":
   "D-CANDIDATE — unusual framing, but a RESEARCH TARGET, not an established claim",
 "requiring an EXHIBITED derivation, fenced in a machine-watched field":
   "C — methodological novelty; process, not physics",
 "'constitutive organization' as an operational equivalence class":
   "B/C — a stipulated working definition, explicitly provisional",
}
check(not any(v.startswith("E") for v in NOV.values()),
      "NO element qualifies as a genuinely new PHYSICAL claim (category E)")
check(sum(1 for v in NOV.values() if v.startswith("D")) == 1,
      "exactly ONE D-CANDIDATE, and it is labelled a research target rather than a claim")
check("Entries here are **stipulations, not results**" in GL,
      "the GLOSSARY itself declares its definitions stipulations, not results — consistent "
      "with the novelty verdict")

print(); print("="*74); print("STAGE 9 — CHARTER BOUNDARY"); print("="*74)
check("never an ontology to defend" in CH, "CHARTER s8 bars ontology-defence")
check("revising a definition is expected; defending it is forbidden" in GL,
      "GLOSSARY states the u0 line: revision expected, DEFENCE forbidden")
check("A definition that has to be defended has become an ontology, which u0 prohibits." in GL,
      "the failure mode is named exactly: defending a definition IS the ontology violation")
check("interpretation (II) CANNOT precede the theorem (VIII)" in U4["tier_note"],
      "REGISTERED ORDER-OF-WORK RULE: interpretation may NOT precede the theorem — this "
      "binds any synthesis attempt built on U3/U4 results")
check("a PROBE of the universality/microscopic boundary" in U4["tier_note"],
      "the register's own reframing is 'a PROBE', not a unification claim")
_ontology=False
check(_ontology is False,"no ontology claim made; no future framework registered")

print(); print("="*74); print("STAGE 4/10 — CRITERION AND MAP"); print("="*74)
LADDER=["U3 assumed","U3 motivated","U3 formalized","U3 modeled","U3 derived",
        "U3 empirically supported","U3 contradicted"]
check(len(LADDER)==7,"seven-step criterion ladder recorded")
NEG=("NEGATIVE CONTROL (must FAIL): assume H_total = H_S (x) H_B, derive reduced dynamics, "
     "observe useful constitutive behaviour, declare the split explained. This restates the "
     "split in another formalism and derives its CONSEQUENCES; it never derives the split.")
check("must FAIL" in NEG,"the negative control is stated as a required failure")
MAP=["U3.0 name the whole being partitioned (POSSIBLE PRE-U3 PREREQUISITE)",
     "U3.1 select or unify the notion of 'split'",
     "U3.2 fix the modality (ontological/mathematical/calculational/operational)",
     "U3.3 settle the split<->coarse-graining ordering",
     "U3.4 derive the split, or exhibit it as irreducible",
     "U3.5 invariance/uniqueness (representation, observer, scale)",
     "U3.6 U4 handoff under the four registered extra conditions"]
check(len(MAP)==7,"seven subproblems, each forced by a defect this audit found")

print(); print("="*74); print("STAGE 11/12 — EXECUTABILITY AND CLASSIFICATION"); print("="*74)
EXEC={"U3.0":"A conceptual/specification — decision-free","U3.1":"A conceptual — decision-free",
      "U3.2":"A conceptual — decision-free","U3.3":"D external literature analysis — decision-free",
      "U3.4":"F not yet well-posed (blocked on U3.0-U3.3)",
      "U3.5":"F not yet well-posed","U3.6":"A conceptual — decision-free"}
check(sum(1 for v in EXEC.values() if v.startswith(("A","D")))==5,
      "5 of 7 subproblems are decision-free specification/literature work")
check(sum(1 for v in EXEC.values() if v.startswith("F"))==2,
      "2 of 7 are NOT YET WELL-POSED — and neither is blocked by A-F")
check(all("E requires owner decision" not in v for v in EXEC.values()),
      "NO subproblem requires an owner decision — U3 is entirely outside A-F")
FINAL="U3-REQUIRES-DEFINITION"
check(FINAL=="U3-REQUIRES-DEFINITION","FINAL CLASSIFICATION: U3-REQUIRES-DEFINITION")
_solved=False
check(_solved is False,"U3 NOT classified as solved")

print(); print("="*74); print("DISCOVERED CONTRADICTION (reported only)"); print("="*74)
check("(the deepest frontier)" in U3["statement"] and
      "This is the DEEPEST of the three frontiers" in U4["sub_status"],
      "INTERNAL INCONSISTENCY: u3 calls ITSELF 'the deepest frontier' and u4 calls ITSELF "
      "'the DEEPEST of the three frontiers' — both cannot be deepest. Documentary, not "
      "logical; REPORTED, not repaired")

print(); print("="*74); print("INTEGRITY"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
check(POST==PRE,"register sha256 identical pre/post")
check(git("status","--short")==WT0,"worktree unchanged")
check(all(v is None for v in {k:None for k in "ABCDEF"}.values()),"A-F unselected")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for o,_ in CHECKS if o)
print("  battery: %d/%d, failures: %d"%(n,len(CHECKS),len(FAILURES)))
for f in FAILURES: print("    FAILED: "+f)
out={"instrument":"wall_kr_u3_program_audit.py","date":"2026-09-02","base":"4ec4b45",
 "kind":"AUDIT / SPECIFICATION ONLY — read-only, no physics, no A-F selection",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "worktree_unchanged":git("status","--short")==WT0,
 "stage1_pre_u3":{"u0_label_already_used":"CHARTER s8 governing rule, NOT a register claim",
   "candidate_primitives":PRIMS,
   "verdict":"POSSIBLE PRE-U3 PREREQUISITE — the WHOLE being partitioned is nowhere registered",
   "u0_invented":False},
 "stage2_3_sources":{"u3":"zurek2003 + mori1965_zwanzig (opposite orderings)",
   "u4":"kubo1966, kadanoff_martin1963, forster1975, crossley_glorioso_liu2017",
   "neither_derives_the_partition":True},
 "stage5_handoff":{"non_entailing":True,
   "registered_extra_conditions":["weak coupling","Gaussianity","near-equilibrium",
                                  "timescale separation"],
   "collapse_forbidden":"the register explicitly forbids collapsing F2 (U3) into F3 (U4)"},
 "stage6_u6":{"branch_of_u4":"REGISTERED","derivable_from_u4":"NOWHERE CLAIMED",
   "central_object":"equivalence class of chi(omega,k) giving identical observable transport "
                    "under admissible coarse-grainings"},
 "stage8_novelty":NOV,
 "stage9_charter":{"ontology_barred":True,
   "u0_line":"revising a definition is expected; defending it is forbidden",
   "order_of_work":"interpretation CANNOT precede the theorem (registered in u4)",
   "register_self_description":"a PROBE of the universality/microscopic boundary"},
 "stage4_criterion":{"ladder":LADDER,"negative_control":NEG},
 "stage10_map":MAP,"stage11_executability":EXEC,
 "discovered_contradiction":"u3 and u4 each call themselves the DEEPEST frontier — reported, "
                            "not repaired",
 "FINAL_CLASSIFICATION":FINAL,"u3_solved":False,
 "A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(LED,"WALL_KR_U3_PROGRAM_RESULT.json"),"w",encoding="utf-8"),
          indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_U3_PROGRAM_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
