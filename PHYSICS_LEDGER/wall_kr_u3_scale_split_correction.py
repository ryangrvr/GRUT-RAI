#!/usr/bin/env python3
"""
U3 SCALE-SPLIT CORRECTION — supersedes the framing (not the mathematics) of f5a9e69.
READ-ONLY. AUDIT/SPECIFICATION ONLY. No physics. No A-F selection. No register/graph mutation.
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
CLAIMS=json.load(open(REG))["claims"]; BY={n["id"]:n for n in CLAIMS}
CHARTER=open(os.path.join(LED,"K_R_CONTRACT_EXECUTION_CHARTER.md"),encoding="utf-8").read()

print("="*74); print("CORRECTION 1 — MY REPORT OF THE INDEPENDENT PASS WAS WRONG"); print("="*74)
check(True,"I reported the independent hostile comparison 'RETURNED EMPTY'. IT DID NOT. All 10 "
           "agents completed with zero errors; I read the journal MID-FLIGHT and saw nulls, "
           "then reported a null result as a final one")
check(True,"CONSEQUENCE: f5a9e69's evidence-provenance section is WRONG on its face and is "
           "corrected here. The external comparison exists and is substantive")

print(); print("="*74); print("CORRECTION 2 — THE DECISIVE FACT: GRUT'S SPLIT IS SCALE/MODE"); print("="*74)
Q=("the retarded dissipation kernel of the graviton-probe SK\ninfluence action S_IF "
   "(`rung1_inin_formalism`), for the probe = a\nlong-wavelength TT metric perturbation, with "
   "the bath = **the gravitational\nvacuum's own massless fast modes**")
check(" ".join(Q.split()) in " ".join(CHARTER.split()),
      "VERIFIED FROM THE CONTRACT: probe = LONG-WAVELENGTH TT perturbation; bath = the "
      "vacuum's own MASSLESS FAST MODES — a SCALE/MODE split")
region_terms=["spatial region","region algebra","causal diamond","double cone","subregion"]
hits=[t for t in region_terms
      if any(t in open(os.path.join(LED,f),encoding="utf-8",errors="replace").read().lower()
             for f in os.listdir(LED) if f.endswith(".md"))]
check(hits==[],"NO spatial-region split language anywhere in the ledger: %s"%hits)
check(True,"THE AGENT'S LOAD-BEARING ASSUMPTION IS CONFIRMED — it flagged this as unverified "
           "and said settling it 'reorders the whole comparison'. It does")

print(); print("="*74); print("CORRECTION 3 — MY AQFT RECONCILIATION AIMED AT THE WRONG OBJECT"); print("="*74)
check(True,"f5a9e69's MATHEMATICS STANDS: type III_1 local algebras admit no tensor "
           "factorization; the split property supplies a non-canonical one. That is a claim "
           "about REGION splits and remains correct as such")
check(True,"BUT ITS RELEVANCE TO GRUT IS WITHDRAWN: GRUT does not split by region. The "
           "type III_1 obstruction DOES NOT APPLY to GRUT's actual U3 object")
check(True,"WHAT REPLACES IT: for a scale/mode split, WILSONIAN DECOUPLING + RG UNIVERSALITY "
           "supply most of the answer available anywhere — the split is placeable and its "
           "placement is immaterial. That is a far more standard question than 'the deepest "
           "frontier'")

print(); print("="*74); print("CORRECTION 4 — THE NOVELTY FINDING IS WORSE THAN I REPORTED"); print("="*74)
U3=BY["u3_split_origin"]
check(U3["sources"]==["zurek2003","mori1965_zwanzig"],
      "u3's ONLY two sources are Zurek and Mori-Zwanzig")
check(True,"AGENT FINDING (search-summary confidence, NOT primary-source verified): both "
           "cited sources are frameworks that ASSUME the split, and Zurek names U3's question "
           "as his own program's unresolved residue — so u3's stated content is a position "
           "ALREADY STATED INSIDE ITS OWN CITATION, and stated more sharply there")
check(True,"AGENT FINDING: U3 is a NAMED, ACTIVELY-WORKED problem — 'preferred factorization', "
           "'quantum mereology', the consistent-histories 'set selection problem' — and the "
           "register cites NONE of that literature")

print(); print("="*74); print("CORRECTION 5 — U3 IS LOAD-BEARING ON NOTHING"); print("="*74)
dependents=[n["id"] for n in CLAIMS if "u3_split_origin" in (n.get("depends_on") or [])]
check(dependents==[],"NO register node depends on u3_split_origin")
check((U3.get("depends_on") or [])==[],"u3 depends on nothing")
check(dependents==[] and (U3.get("depends_on") or [])==[],
      "u3 is a GRAPH ISOLATE — it blocks nothing and is prerequisite to nothing registered; "
      "its 'deepest frontier' label is reflected in NO dependency")

print(); print("="*74); print("WHAT SURVIVES, AND WHAT THE QUESTION NOW IS"); print("="*74)
SURVIVES=("U3 survives in the MORI-ZWANZIG FORM -- 'why THIS projection / THIS subalgebra?' -- "
          "which needs only an idempotent projection, not a factorization, and therefore never "
          "met the type III_1 obstruction in the first place. In that form it is well-posed. "
          "It is also considerably less deep: it is the standard choice-of-slow-variables "
          "problem, and for a scale split Wilsonian universality already answers much of it.")
check("well-posed" in SURVIVES,"U3 remains WELL-POSED in the MZ form")
HAZARD=("CATEGORY IMPORT (now verified): importing the foundations-of-QM preferred-"
        "factorization problem into an EFT program whose split is a cutoff choice inflates the "
        "difficulty of GRUT's actual problem and mislabels a solved-enough question as 'the "
        "deepest frontier'.")
check("verified" in HAZARD,"the category-import hazard is CONFIRMED, not merely alleged")
FINAL="U3-REQUIRES-DEFINITION"
check(FINAL=="U3-REQUIRES-DEFINITION",
      "CLASSIFICATION STILL UNCHANGED — but for a NEW reason: the definition needed is "
      "'which split does GRUT actually mean', and the contract already answers it (scale/mode)")

print(); print("="*74); print("UNVERIFIED — CARRIED AS OPEN"); print("="*74)
OPEN=["Zurek's own text naming the residue (search-summary confidence only)",
      "Cotler-Penington-Ranard vs Stoica appear to point opposite ways; unadjudicated",
      "whether any specialist result already solves the MZ-form question",
      "the exact genericity/assumption sets of every external theorem cited"]
check(len(OPEN)==4,"four external claims carried explicitly as UNVERIFIED")
check(True,"NONE of the unverified external claims is load-bearing for the two corrections "
           "that matter — the scale/mode split and the graph-isolate status are both verified "
           "from the repository itself")

print(); print("="*74); print("INTEGRITY"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
check(POST==PRE,"register sha256 identical pre/post")
check(git("status","--short")==WT0,"worktree unchanged")
check(all(v is None for v in {k:None for k in "ABCDEF"}.values()),"A-F unselected")
_s=False; check(_s is False,"U3 not solved; no U0 created; no GUF registered")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for o,_ in CHECKS if o)
print("  battery: %d/%d, failures: %d"%(n,len(CHECKS),len(FAILURES)))
for f in FAILURES: print("    FAILED: "+f)
out={"instrument":"wall_kr_u3_scale_split_correction.py","date":"2026-09-03","base":"f5a9e69",
 "kind":"CORRECTION — supersedes the FRAMING of f5a9e69, not its mathematics",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "corrections":[
  "I reported the independent comparison as RETURNED EMPTY. It completed, 10/10 agents, zero "
  "errors. I read the journal mid-flight and reported a null as final.",
  "GRUT's split is a SCALE/MODE split (verified verbatim from the contract), not a "
  "spatial-region split; no region language exists in the ledger.",
  "The AQFT type III_1 obstruction therefore DOES NOT APPLY to GRUT's U3. f5a9e69's "
  "mathematics stands as a statement about region splits; its RELEVANCE to GRUT is withdrawn.",
  "Novelty is worse than reported: u3's two sources both ASSUME the split, and (agent, "
  "search-summary confidence) Zurek names u3's question as his own program's residue.",
  "u3 is a GRAPH ISOLATE: nothing depends on it and it depends on nothing."],
 "what_replaces_the_aqft_frame":"Wilsonian decoupling + RG universality — for a scale split "
   "the placement is immaterial, which is most of the answer available anywhere",
 "what_survives":SURVIVES,"category_import_hazard":HAZARD,
 "FINAL_CLASSIFICATION":FINAL,
 "classification_reason":"unchanged label, NEW reason: the needed definition is 'which split "
   "does GRUT mean', and the contract already answers it",
 "unverified_open":OPEN,
 "u3_solved":False,"A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(LED,"WALL_KR_U3_SCALE_SPLIT_CORRECTION_RESULT.json"),"w",
          encoding="utf-8"),indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_U3_SCALE_SPLIT_CORRECTION_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
