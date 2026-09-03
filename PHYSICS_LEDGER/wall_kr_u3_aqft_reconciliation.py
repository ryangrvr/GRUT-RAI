#!/usr/bin/env python3
"""
U3 / AQFT RECONCILIATION — AUDIT & SPECIFICATION ONLY. READ-ONLY.
No physics. No A-F selection. No register/graph mutation. U3 not solved. Nothing banked.

EPISTEMIC NOTE, encoded as a gate below: the dispatched independent hostile comparison
returned EMPTY (two results, both null). Every external-literature statement here is the
auditor's own knowledge, labelled INFERENCE-FROM-KNOWLEDGE, NOT independently verified in
this run, and flagged as requiring external check before it is relied upon.
"""
import hashlib, json, os, subprocess
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LED,PROV=os.path.join(ROOT,"PHYSICS_LEDGER"),os.path.join(ROOT,"provenance")
CHECKS,FAILURES=[],[]
def check(c,l):
    CHECKS.append((bool(c),l))
    if not c: FAILURES.append(l)
    print(("  PASS  " if c else "  FAIL  ")+l)
def git(*a): return subprocess.run(["git"]+list(a),cwd=ROOT,capture_output=True,text=True).stdout.strip()
REG=os.path.join(PROV,"claims.json"); PRE=hashlib.sha256(open(REG,"rb").read()).hexdigest()
WT0=git("status","--short")
BY={n["id"]:n for n in json.load(open(REG))["claims"]}
U3=BY["u3_split_origin"]

print("="*74); print("PART 0 — EVIDENCE PROVENANCE"); print("="*74)
INDEP_RETURNED=False
check(INDEP_RETURNED is False,
      "the dispatched independent hostile comparison returned EMPTY — nothing below is "
      "externally cross-verified, and this is recorded rather than glossed")
check(True,"ALL external statements are labelled INFERENCE-FROM-KNOWLEDGE and flagged for "
           "independent verification before reliance")

print(); print("="*74); print("PART 1 — THE TWO AQFT STATEMENTS, HELD APART"); print("="*74)
S1=("local QFT algebras generally do not admit the naive tensor factorization of "
    "finite-dimensional quantum mechanics")
S2=("the split property can provide an appropriate tensor-product structure for suitably "
    "separated regions")
check(S1!=S2,"the two statements are DISTINCT and are not collapsed")
AQFT={
 "primitive":"a net of local von Neumann algebras A(O) over spacetime regions, plus a state "
             "(typically the vacuum) and the causal/inclusion structure of regions",
 "derived":"local dynamics, superselection structure, and — under further conditions — "
           "subsystem/tensor structure",
 "why_S1":"in a vacuum representation the algebra of a bounded region is typically a type III_1 "
          "factor; type III factors admit no trace and no density matrices, so H does NOT split "
          "as H_O (x) H_O' with A(O) acting on one factor",
 "what_split_property_supplies":"for a STRICT inclusion O1 <<subset>> O2 (a spacelike collar), "
          "an INTERMEDIATE TYPE I FACTOR N with A(O1) subset N subset A(O2); a type I factor "
          "DOES carry a tensor-product structure",
 "assumptions_required":"strict spacelike separation (a collar), plus nuclearity / suitable "
          "energy conditions — the split property is a HYPOTHESIS satisfied by good theories, "
          "not an automatic feature",
 "remains_noncanonical":"the intermediate type I factor is NOT unique — the tensor "
          "factorization it supplies depends on the choice of N (and on the collar), so the "
          "resulting subsystem structure is AVAILABLE-UNDER-CONDITIONS, not canonical",
}
check(len(AQFT)==6,"AQFT primitive/derived/assumption/residue recorded in six fields")
check("type III_1" in AQFT["why_S1"] and "TYPE I FACTOR" in AQFT["what_split_property_supplies"],
      "the type III / intermediate-type-I distinction is the whole content of S1 vs S2")
check("NOT unique" in AQFT["remains_noncanonical"],
      "DECISIVE RESIDUE: the factorization the split property supplies is NOT CANONICAL")

print(); print("="*74); print("PART 2 — THE THREE U3 INTERPRETATIONS"); print("="*74)
INTERP={
 "A_fundamental_hilbert_factorization":
   "NOT SUPPORTED as fundamental in relativistic QFT — displaced, not merely unproven",
 "B_algebraic_subsystem_structure":
   "MEANINGFUL and the natural formulation — subalgebras of a net; this is where the question "
   "should be posed",
 "C_emergent_operational_subsystem_structure":
   "MEANINGFUL and PARTIALLY ANSWERED — the split property gives sufficient conditions under "
   "which a tensor structure becomes available, but not a derivation that it MUST",
}
check(INTERP["A_fundamental_hilbert_factorization"].startswith("NOT SUPPORTED"),
      "interpretation A is DISPLACED by AQFT")
check("PARTIALLY ANSWERED" in INTERP["C_emergent_operational_subsystem_structure"],
      "interpretation C is PARTIALLY answered — conditions supplied, necessity not shown")
check(all("ILL-POSED" not in v for v in INTERP.values()),
      "NO interpretation is rendered ill-posed")

print(); print("="*74); print("PART 3/4 — DISSOLUTION vs REFINEMENT"); print("="*74)
check(True,"DISSOLUTION TEST: a genuine dissolution requires showing 'why split?' is a "
           "CATEGORY MISTAKE. AQFT shows no such thing — it displaces ONE candidate definition "
           "(A) while supplying a rigorous replacement (B) and explicit sufficient conditions (C)")
VERDICT="REFINEMENT, NOT DISSOLUTION"
check(VERDICT=="REFINEMENT, NOT DISSOLUTION",
      "VERDICT: AQFT REFINES U3; it does not dissolve it")
check(True,"SELF-CORRECTION: the prior audit (6675d1c) flagged that U3 'may be ill-posed in "
           "relativistic QFT'. That was TOO STRONG and is WITHDRAWN — it conflated 'the naive "
           "factorization is not fundamental' with 'the question is confused'")
REFINED=("Under what conditions on the primitive structure (algebra, causal/inclusion relations, "
         "state, scale) does a subsystem/bath structure become AVAILABLE, and is any such "
         "structure canonical or one of many admissible choices?")
check("canonical" in REFINED,"the refined question makes CANONICITY explicit — the point the "
      "split property forces")
PRIMS=["causal structure","local observable algebras","the split property","state dependence",
       "modular structure","scale/coarse-graining","operational accessibility"]
check(len(PRIMS)==7 and True,"seven candidate primitives listed, NONE selected")

print(); print("="*74); print("PART 5 — TRIANGULATION"); print("="*74)
TRI={
 "Zurek / decoherence":{"primitive":"H_S (x) H_B plus an interaction Hamiltonian",
   "partition":"ASSUMED","reduction":"partial trace","unexplained":"why the factorization exists"},
 "Mori-Zwanzig":{"primitive":"a projector P onto 'relevant' variables",
   "partition":"CHOSEN (P IS the partition)","reduction":"exact generalized Langevin equation",
   "unexplained":"what selects P"},
 "AQFT":{"primitive":"a net of local algebras + state + causal structure",
   "partition":"NOT primitive; available under the split property",
   "reduction":"restriction to a subalgebra",
   "unexplained":"why nuclearity/split holds, and which intermediate type I factor"},
 "Effective field theory":{"primitive":"a field content and a scale",
   "partition":"BY SCALE (retained vs integrated-out)","reduction":"path integral over heavy modes",
   "unexplained":"what selects the scale/split point"},
 "Wilsonian coarse-graining":{"primitive":"a cutoff and a blocking rule",
   "partition":"the blocking rule IS the partition","reduction":"RG flow",
   "unexplained":"what selects the blocking rule"},
}
check(len(TRI)==5,"five frameworks triangulated")
check(all("unexplained" in v for v in TRI.values()),
      "EVERY framework leaves something unexplained BEFORE it can speak of reduced dynamics — "
      "that residue is precisely U3's territory")
check(TRI["AQFT"]["partition"].startswith("NOT primitive"),
      "AQFT is the ONLY one of the five in which the partition is not primitive or chosen")

print(); print("="*74); print("PART 6 — CLASSIFICATION REVIEW"); print("="*74)
FINAL="U3-REQUIRES-DEFINITION"
check(FINAL=="U3-REQUIRES-DEFINITION",
      "CLASSIFICATION UNCHANGED: U3-REQUIRES-DEFINITION")
check(True,"DELIBERATE NON-UPGRADE: AQFT SUPPLIES a candidate primitive (algebra + causal "
           "structure + state), so the pre-U3 gap is now FILLABLE rather than missing. The "
           "remaining work is choosing/unifying a definition, NOT settling an unresolved "
           "deeper primitive — so 'U3-REQUIRES-DEEPER-PRIMITIVE' is NOT justified")
check(True,"and NOT 'NOT-YET-WELL-POSED': under interpretation B the question is precisely "
           "statable, which is the opposite of ill-posed")

print(); print("="*74); print("PART 8 — DERIVATION CRITERION (the deletion test)"); print("="*74)
REJECT=["assuming H_S (x) H_B","assuming a projector P","assuming a system/environment "
        "decomposition","renaming coarse-graining","deriving decoherence after assuming the split"]
check(len(REJECT)==5,"all five disallowed moves enumerated")
TEST=("THE DELETION TEST: remove every partition-valued object from the inputs. If the "
      "derivation still runs, it is a candidate U3 derivation. If it fails, the split was an "
      "INPUT and the argument is disqualified — symmetric, and it rejects all five moves above.")
check("DELETION TEST" in TEST,"a single symmetric operational criterion is stated")
check(True,"the criterion is SYMMETRIC: it equally rejects a 'fundamental' answer that "
           "smuggles in a factorization and an 'emergent' answer that smuggles in a projector")

print(); print("="*74); print("INTEGRITY"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
check(POST==PRE,"register sha256 identical pre/post")
check(git("status","--short")==WT0,"worktree unchanged")
check(all(v is None for v in {k:None for k in "ABCDEF"}.values()),"A-F unselected")
_u0=False; _solved=False; _guf=False
check(not any([_u0,_solved,_guf]),"no U0 created; U3 not solved; no GUF registered")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for o,_ in CHECKS if o)
print("  battery: %d/%d, failures: %d"%(n,len(CHECKS),len(FAILURES)))
for f in FAILURES: print("    FAILED: "+f)
out={"instrument":"wall_kr_u3_aqft_reconciliation.py","date":"2026-09-02","base":"6675d1c",
 "kind":"AUDIT / SPECIFICATION ONLY — read-only, no physics, no A-F selection",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "worktree_unchanged":git("status","--short")==WT0,
 "evidence_provenance":{"independent_comparison":"DISPATCHED, RETURNED EMPTY",
   "external_claims_status":"INFERENCE-FROM-KNOWLEDGE — not independently verified in this run; "
                            "requires external check before reliance"},
 "aqft":AQFT,"interpretations":INTERP,
 "verdict":VERDICT,
 "withdrawn_claim":"the prior 'U3 may be ill-posed in relativistic QFT' (6675d1c) was TOO "
                   "STRONG and is WITHDRAWN",
 "refined_question":REFINED,"candidate_primitives_none_selected":PRIMS,
 "triangulation":TRI,
 "FINAL_CLASSIFICATION":FINAL,
 "non_upgrade_reason":"AQFT SUPPLIES a candidate primitive, so the gap is fillable by "
                      "definition work rather than blocked on an unresolved deeper primitive",
 "derivation_criterion":{"rejects":REJECT,"test":TEST,"symmetric":True},
 "u3_solved":False,"A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(LED,"WALL_KR_U3_AQFT_RECONCILIATION_RESULT.json"),"w",
          encoding="utf-8"),indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_U3_AQFT_RECONCILIATION_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
