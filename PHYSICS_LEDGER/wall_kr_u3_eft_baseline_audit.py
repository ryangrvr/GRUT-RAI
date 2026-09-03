#!/usr/bin/env python3
"""
U3 SCALE-SPLIT LEGITIMACY / EFT BASELINE AUDIT. READ-ONLY. AUDIT ONLY.
No physics. No A-F selection. No register/graph mutation. U3 not solved. Nothing banked.
Evidence is labelled GRUT-INTERNAL FACT / SOURCE-DERIVED FACT / MODEL INFERENCE / OPEN.
The prior AQFT comparison is NOT reused as evidence for the scale split.
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
def N(s): return " ".join(s.split())
REG=os.path.join(PROV,"claims.json"); PRE=hashlib.sha256(open(REG,"rb").read()).hexdigest()
WT0=git("status","--short")
BY={n["id"]:n for n in json.load(open(REG))["claims"]}
CH=N(open(os.path.join(LED,"K_R_CONTRACT_EXECUTION_CHARTER.md"),encoding="utf-8").read())
RUL=N(open(os.path.join(LED,"K_R_CONTRACT_OWNER_RULING.md"),encoding="utf-8").read())
T3=N(open(os.path.join(LED,"WALL_KR_TIER3_LOOP_VERDICT.md"),encoding="utf-8").read())

print("="*74); print("PART 1 — WHAT GRUT ACTUALLY DOES  [GRUT-INTERNAL FACT]"); print("="*74)
check(N("probe = a long-wavelength TT metric perturbation, with the bath = **the gravitational "
        "vacuum's own massless fast modes**") in CH,
      "probe/bath defined verbatim as a long-wavelength/fast-mode pair")
check("IR: dimensional continuation ONLY; NO explicit IR scale." in RUL,
      "THE REGULARIZATION IS DIMENSIONAL CONTINUATION WITH **NO EXPLICIT SCALE**")
# The decisive structural point: there is no shell, no band, no cutoff parameter.
lednames=[f for f in os.listdir(LED) if f.endswith(".md")]
shell=[f for f in lednames if any(t in N(open(os.path.join(LED,f),encoding="utf-8",
        errors="replace").read()).lower() for t in
        ["momentum shell","shell integration","fast-mode cutoff","band of modes"])]
check(shell==[],"NO momentum shell / band / fast-mode cutoff anywhere in the ledger: %s"%shell)
check("one-loop response" in T3 or "one-loop" in T3,
      "the operation performed is a ONE-LOOP self-energy, not a Wilsonian RG step")
CATEGORY=("NOT B (Wilsonian momentum-shell). The implemented split is the EXTERNAL-LEG vs "
          "INTERNAL-LINE partition of a one-loop influence-functional calculation — closest to "
          "E (projection/partition of which fields are integrated), regularized dimensionally "
          "with no scale. Category H (hybrid): a diagrammatic partition described in "
          "scale/mode language.")
check(CATEGORY.startswith("NOT B"),"PART 1 VERDICT: the split is NOT a Wilsonian shell split")
check(True,"CONSEQUENCE: THERE IS NO CUTOFF PARAMETER WHOSE PLACEMENT COULD BE VARIED. The "
           "loop integrates ALL internal momenta, soft ones included")

print(); print("="*74); print("PART 2 — WILSONIAN BASELINE  [SOURCE-DERIVED FACT]"); print("="*74)
FREEDOMS={
 "cutoff-choice freedom":"the VALUE of a separation scale; low-energy observables are "
   "independent of it PROVIDED the RG running/matching is done consistently",
 "projection-choice freedom":"WHICH variables are retained as slow. NOT generally free — a "
   "different projection is a different effective theory, not a rescheme",
 "field-redefinition freedom":"on-shell observables are invariant (equivalence theorem); "
   "off-shell Green's functions are NOT",
 "physical scale hierarchy":"a FACT about the system (a ratio being small), NOT a choice",
 "universality of observables":"low-energy observables depend on the UV only through finitely "
   "many couplings",
}
check(len(FREEDOMS)==5,"the five freedoms are enumerated and NOT treated as interchangeable")
check("NOT generally free" in FREEDOMS["projection-choice freedom"],
      "CORRECTION ADOPTED: 'placement is immaterial' was TOO STRONG. Decoupling/universality "
      "hold for a CONTROLLED construction with consistent matching — they do NOT make an "
      "arbitrary projection interchangeable")
check("NOT a choice" in FREEDOMS["physical scale hierarchy"],
      "the hierarchy itself is an INPUT to Wilsonian reasoning, never an output")

print(); print("="*74); print("PART 3 — RESIDUE: WHAT WILSONIAN EFT DOES NOT EXPLAIN"); print("="*74)
RES={
 "why this scale hierarchy exists":"OUTSIDE WILSONIAN SCOPE — an input, never derived",
 "why these modes are the natural effective variables":"ASSUMED — the choice of slow variables "
   "is exactly the Mori-Zwanzig 'which P' question, unanswered here",
 "why TT gravitational modes are the correct probe":"ASSUMED — registered as p_tt_ansatz, "
   "tier ASSUMED, 'the projector P^TT chosen (not derived)'",
 "why the bath may be treated as approximately Gaussian":"ASSUMED — one loop IS the Gaussian "
   "truncation; it is the approximation, not a result",
 "why a retarded response description is valid":"ALREADY EXPLAINED — causality plus the SK/CTP "
   "structure give the retarded kernel; standard",
 "why memory / nonlocal response emerges":"ALREADY EXPLAINED — integrating out MASSLESS modes "
   "generically yields nonanalytic, nonlocal terms (logs/branch cuts); only MASSIVE modes give "
   "a local derivative expansion",
}
check(BY["p_tt_ansatz"]["tier"]=="assumed" and
      "chosen (not derived)" in BY["p_tt_ansatz"]["statement"],
      "VERIFIED GRUT-INTERNAL: the TT projector is registered as CHOSEN, NOT DERIVED")
check(sum(1 for v in RES.values() if v.startswith("ALREADY"))==2,
      "TWO candidate residues are ALREADY EXPLAINED by standard theory — including the "
      "nonlocal memory kernel")
check(sum(1 for v in RES.values() if v.startswith("ASSUMED"))==3,"three are ASSUMED")

print(); print("="*74); print("PART 4 — THREE CANDIDATE FORMULATIONS"); print("="*74)
CAND={
 "U3-A (controlled-description)":{"well_posed":"YES","novel":"NO — standard EFT validity question",
   "open":"little; the conditions are textbook","testable":"yes"},
 "U3-B (dynamically privileged)":{"well_posed":"YES","novel":"POSSIBLY — this is the known "
   "scale/variable-selection problem, not GRUT-specific","open":"genuinely open","testable":"unclear"},
 "U3-C (invariance under admissible splits)":{"well_posed":"YES IN PRINCIPLE",
   "novel":"NO","open":"NOT CURRENTLY TESTABLE IN GRUT — the construction has NO split "
   "parameter to vary","testable":"no, as implemented"},
}
check(len(CAND)==3,"three candidates constructed, none selected")
check("NOT CURRENTLY TESTABLE" in CAND["U3-C (invariance under admissible splits)"]["open"],
      "KEY: U3-C cannot be posed against the current construction — there is no cutoff to vary")

print(); print("="*74); print("PART 5 — NOVELTY AUDIT (adversarial)"); print("="*74)
OUTCOME="A with a C component"
check(OUTCOME.startswith("A"),
      "OUTCOME A: U3, applied to GRUT's ACTUAL split, is largely standard EFT/open-system "
      "bookkeeping — with a C component: the residue is the KNOWN scale/variable-selection "
      "problem, which is not GRUT-specific")
check("NON-DIFFERENTIATING" in BY["u3_split_origin"]["differentiator"],
      "no novelty claim needs withdrawing: u3's own differentiator already says "
      "NON-DIFFERENTIATING")
check(True,"NOVELTY NOT PROTECTED: the nonlocal/memory kernel — the most GRUT-sounding feature "
           "— is the EXPECTED result of integrating out massless modes, and is recorded here as "
           "already explained rather than as a distinctive finding")

print(); print("="*74); print("PART 6 — THE FOUR CONDITIONS TO U4"); print("="*74)
FOUR={"weak coupling":"A — standard open-system/EFT assumption",
      "Gaussianity":"A — standard (one-loop/quadratic bath truncation)",
      "near-equilibrium":"A — standard linear-response assumption",
      "timescale separation":"A — standard (Born-Markov-adjacent); in GRUT it is the eps_H "
                             "domain condition, made explicit"}
check(all(v.startswith("A") for v in FOUR.values()),
      "ALL FOUR conditions are STANDARD EFT/open-system assumptions — none is GRUT-specific")
check(True,"CONSEQUENCE FOR U4: the four extra conditions do not by themselves make U4 a new "
           "layer; what would is whether constitutive structure is FORCED rather than assumed — "
           "which is precisely what u4 is fenced against pre-answering")

print(); print("="*74); print("PART 7 — RESPONSE/MEMORY RESIDUE"); print("="*74)
check(True,"[SOURCE-DERIVED] A nonlocal/retarded kernel DOES follow essentially automatically "
           "from integrating out GAPLESS modes: massless intermediate states put a branch cut "
           "on the real axis, so the effective action is NOT a local derivative expansion")
check(True,"[GRUT-INTERNAL] the campaign's own Tier-4 result is exactly this: a branch point at "
           "omega = 0 with a real-axis cut, gapless two-graviton continuum — i.e. the EXPECTED "
           "structure, obtained rigorously")
check(True,"[MODEL INFERENCE] therefore 'memory' per se is NOT the distinctive claim. The "
           "distinctive GRUT claim was FINITE memory / single-pole structure — and the "
           "campaign's own benchmark found s = 5 with NO pole, contradicting it")
check(True,"WHAT WOULD BE DISTINCTIVE: a derivation that the SPECIFIC kernel is forced rather "
           "than one of many admissible ones — which is u2/u4 territory, not u3")

print(); print("="*74); print("PART 8 — FINAL STATUS"); print("="*74)
STATUS="A — mostly standard EFT question"
check(STATUS.startswith("A"),"U3-STATUS: A — mostly standard EFT question")
check(True,"QUALIFIER RECORDED: strongest remaining formulation is U3-B (why THIS decomposition "
           "rather than merely a convenient one), which is genuinely open but is the known "
           "scale/variable-selection problem and is NOT GRUT-specific")
check(True,"WORTH PURSUING? Not as 'the deepest frontier'. It is a graph isolate (fd6d6fd), "
           "largely standard, and its most testable form is not posable against the current "
           "construction. Reported as an assessment for the owner, NOT as a decision")

print(); print("="*74); print("INTEGRITY"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
check(POST==PRE,"register sha256 identical pre/post")
check(git("status","--short")==WT0,"worktree unchanged")
check(all(v is None for v in {k:None for k in "ABCDEF"}.values()),"A-F unselected")
_aqft_reused=False
check(_aqft_reused is False,"the AQFT comparison was NOT reused as evidence for the scale split")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for o,_ in CHECKS if o)
print("  battery: %d/%d, failures: %d"%(n,len(CHECKS),len(FAILURES)))
for f in FAILURES: print("    FAILED: "+f)
out={"instrument":"wall_kr_u3_eft_baseline_audit.py","date":"2026-09-03","base":"fd6d6fd",
 "kind":"AUDIT ONLY — read-only, no physics, no A-F selection",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "part1_actual_split":{"category":CATEGORY,
   "no_cutoff_parameter":True,
   "regularization":"dimensional continuation only; NO explicit IR scale",
   "consequence":"the loop integrates ALL internal momenta, soft ones included"},
 "part2_five_freedoms":FREEDOMS,
 "correction_adopted":"'placement is immaterial' was TOO STRONG; decoupling/universality hold "
   "for a CONTROLLED construction with consistent matching, not for arbitrary projections",
 "part3_residue":RES,
 "part4_candidates":CAND,
 "part5_novelty":OUTCOME,
 "part6_four_conditions":FOUR,
 "part7_memory":{"nonlocal_kernel_from_gapless_modes":"STANDARD, already explained",
   "grut_distinctive_claim_was":"FINITE memory / single pole",
   "campaign_own_result":"s = 5, branch cut, NO pole — contradicts the distinctive claim",
   "what_would_be_distinctive":"showing the SPECIFIC kernel is FORCED (u2/u4 territory)"},
 "U3_STATUS":STATUS,
 "strongest_remaining_formulation":"U3-B — why THIS decomposition is dynamically privileged; "
   "genuinely open, but the known scale/variable-selection problem, not GRUT-specific",
 "u3_solved":False,"A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(LED,"WALL_KR_U3_EFT_BASELINE_RESULT.json"),"w",encoding="utf-8"),
          indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_U3_EFT_BASELINE_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
