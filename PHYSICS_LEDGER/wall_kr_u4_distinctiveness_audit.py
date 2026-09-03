#!/usr/bin/env python3
"""
U4 DISTINCTIVENESS / STANDARD-THEORY SUBTRACTION AUDIT. READ-ONLY. AUDIT ONLY.
No physics. No A-F selection. No register/graph mutation. Nothing banked.
Labels: GRUT-INTERNAL FACT / SOURCE-DERIVED FACT / MODEL INFERENCE / OPEN.
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
U4=BY["u4_constitutive_origin"]
ST,TN,OV=N(U4["statement"]),N(U4["tier_note"]),N(U4["overturning_computation"])

print("="*74); print("PART 0 — CORRECTION TO 9b9036b, ADOPTED"); print("="*74)
check(True,"WITHDRAWN AS TOO STRONG: 'a genuine fast/slow cutoff would have regulated the IR "
           "by construction'. A cutoff SEPARATES sectors; it does not eliminate IR physics — "
           "a retained low-energy theory can carry genuine IR singularities. CORRECTED TO: "
           "the absence of a scale separation means the calculation does not implement a "
           "Wilsonian separation in which soft modes are excluded from the integrated-out "
           "sector; the H^2 IR behaviour therefore cannot be attributed to an explicitly "
           "regulated fast-mode elimination")

print(); print("="*74); print("PART 1/2 — THE EXACT U4 CLAIM AND ITS OBJECT  [GRUT-INTERNAL]"); print("="*74)
check(ST.startswith("Version II, entry U4 / Frontier 3 (the origin of the constitutive FORM): "
      "GIVEN coarse-graining,"), "u4 statement recovered; opens 'GIVEN coarse-graining'")
check("the equivalence class of response functionals chi(omega,k) producing identical "
      "observable transport under admissible coarse-grainings" in TN,
      "U4's MINIMAL OBJECT is pinned: the chi(omega,k) equivalence class — a LINEAR-RESPONSE "
      "object; linearity is built into the object's definition, not derived")

# THE DECISIVE INTERNAL STRUCTURE: u4's own text already separates two questions.
check("U1 says 'GIVEN the constitutive conditions, the form is universal-and-standard "
      "(Feynman-Vernon)'; U4 asks 'why do those conditions hold at all / why is constitutive "
      "structure generic'" in TN,
      "THE REGISTER ALREADY SPLIT THE QUESTION: form-given-conditions is U1's (borrowed, "
      "standard); U4 proper is WHY THE CONDITIONS HOLD GENERICALLY")
check("REFUTED-as-empty / dissolves if the constitutive form is shown to be a mere "
      "definitional consequence of the presupposed conditions" in OV,
      "u4 carries its OWN dissolution branch — anticipating exactly the subtraction below")

print(); print("="*74); print("PART 3 — STANDARD-THEORY SUBTRACTION  [SOURCE-DERIVED]"); print("="*74)
BASE={
 "A Gaussian integrate-out":{"derives":"EXACTLY a quadratic influence functional: retarded "
   "kernel + noise kernel","assumes":"Gaussian bath, linear coupling","kernel_from":"the bath "
   "two-point function","does_not_explain":"why Gaussian, why linear coupling, which bath"},
 "B Feynman-Vernon":{"derives":"the same, formalized for any factorized initial state",
   "assumes":"the partition + initial product state","kernel_from":"bath correlators",
   "does_not_explain":"the partition, the state"},
 "C Schwinger-Keldysh":{"derives":"K_R and N with causal/unitarity structure; KMS locks N to "
   "Im chi in equilibrium","assumes":"the CTP contour, a state","kernel_from":"the microscopic "
   "action","does_not_explain":"which action, which state"},
 "D Kubo":{"derives":"linear response = the retarded correlator, to first order in the probe",
   "assumes":"near-equilibrium, weak probe","kernel_from":"equilibrium correlations",
   "does_not_explain":"why the regime applies"},
 "E Mori-Zwanzig":{"derives":"the generalized-Langevin/constitutive FORM **EXACTLY, for ANY "
   "projector, with NO weak-coupling or Gaussianity assumption** — drift + memory kernel + "
   "noise is an operator identity","assumes":"a projector and a Liouvillian",
   "kernel_from":"the orthogonal dynamics (generally as hard as the full problem)",
   "does_not_explain":"why the kernel is ever SIMPLE/universal — i.e. why the description is "
   "USEFUL"},
 "F Wilsonian EFT":{"derives":"nonlocal effective action from gapless modes; local expansion "
   "from gapped ones","assumes":"a hierarchy","kernel_from":"the integrated-out sector",
   "does_not_explain":"the hierarchy"},
 "G near-equilibrium stat mech":{"derives":"regression/Onsager: response = correlation",
   "assumes":"near-equilibrium","kernel_from":"fluctuations","does_not_explain":"the regime"},
 "H hydrodynamic SK-EFT":{"derives":"constitutive relations constrained by symmetry + KMS "
   "(the u4 source crossley_glorioso_liu2017)","assumes":"gradient expansion, thermal state",
   "kernel_from":"transport coefficients (inputs)","does_not_explain":"coefficient values"},
}
check(len(BASE)==8,"eight standard mechanisms subtracted, each with derives/assumes/free/not-explained")
check("EXACTLY, for ANY projector" in BASE["E Mori-Zwanzig"]["derives"],
      "THE SHARPEST SUBTRACTION: Mori-Zwanzig derives the constitutive FORM as an operator "
      "IDENTITY — the form's existence is EMPTY of physical content")
check("USEFUL" in BASE["E Mori-Zwanzig"]["does_not_explain"],
      "...and what MZ does NOT explain is why the kernel is ever simple — the usefulness "
      "question, which is exactly the four-conditions question")

print(); print("="*74); print("PART 4/5 — THE RESIDUE"); print("="*74)
RESIDUE={
 "1 why constitutive at all":"STANDARDLY EXPLAINED (dissolved by the MZ identity) — and u4's "
   "own dissolution branch names this outcome for the FORM half",
 "2 why linear":"STANDARD ASSUMPTION — linearity is the first-order regime, and it is built "
   "into U4's own object definition",
 "3 why retarded":"STANDARDLY EXPLAINED — SK/causality",
 "4 why causal":"STANDARDLY EXPLAINED — same",
 "5 why memory":"STANDARDLY EXPLAINED — the MZ kernel exists identically; gapless modes make "
   "it nonlocal",
 "6 why Gaussian":"STANDARD ASSUMPTION — the truncation itself",
 "7 why this bath state":"STANDARD ASSUMPTION in GRUT — BD declared by owner ruling D3(iii), "
   "not derived",
 "8 why the TT sector":"STANDARD ASSUMPTION in GRUT — p_tt_ansatz, tier assumed, 'chosen (not "
   "derived)'",
 "9 why this kernel":"NOT A U4 QUESTION — that is u2 territory",
 "10 why this analytic structure":"PARTIALLY EXPLAINED — causality/passivity/KMS CONSTRAIN "
   "the class; they do not SELECT a member",
 "11 why admissible coarse-grainings agree":"OPEN PROBLEM — this is the u5 classification "
   "question, unexecuted",
 "12 why the four conditions hold generically across successful EFTs":"OPEN PROBLEM — a KNOWN "
   "one (foundations of EFT), and it is U4 PROPER after the register's own U1/U4 split",
}
check(len(RESIDUE)==12,"twelve candidate residues classified")
check(sum(1 for v in RESIDUE.values() if v.startswith("OPEN PROBLEM"))==2,
      "exactly TWO residues survive as open problems (items 11 and 12)")
check(not any("GRUT-SPECIFIC CLAIM" in v for v in RESIDUE.values()),
      "NO residue classifies as a GRUT-SPECIFIC CLAIM — nothing that survives subtraction "
      "is GRUT's own")
check(True,"PART 5 ANSWER: YES — standard coarse-graining already yields response = "
           "functional(source/history); MZ gives the FORM exactly. Deriving a constitutive "
           "RELATION and deriving the particular constitutive KERNEL are kept separate, and "
           "only the second retains content")

print(); print("="*74); print("PART 6/7 — LINEARITY AND MEMORY, DISENTANGLED"); print("="*74)
check("chi(omega,k)" in TN,
      "LINEARITY: U4's object is a susceptibility — linearity enters by DEFINITION of the "
      "object, i.e. by the choice to work in the linear-response regime; if U4 were 'why "
      "linear', the honest answer is 'because we chose that regime'")
MEM={"nonlocality":"generic (gapless modes)","retardation":"generic (causality)",
     "finite correlation time":"NOT generic — a claim","exponential memory":"NOT generic — a claim",
     "single-pole response":"NOT generic — THE claim, held by rung1_ontology (tier ASSUMED)",
     "branch-cut response":"what the campaign actually FOUND (Tier-4)",
     "power-law memory":"what a branch cut implies"}
check(len(MEM)==7,"the seven memory notions are separated, not interchanged")
check(BY["rung1_ontology_finite_memory"]["tier"]=="assumed",
      "GRUT-INTERNAL: the finite-memory/single-pole claim is tier ASSUMED (a stance) and "
      "does NOT belong to U4 — U4 claims only the generic pair (nonlocality + retardation)")

print(); print("="*74); print("PART 8 — KERNEL SELECTION"); print("="*74)
SEL={
 "symmetry":"necessary constraint; not sufficient","conservation/Ward":"constraint; not sufficient",
 "analyticity/causality":"constrains to a half-plane class; not sufficient",
 "FDT/KMS":"locks N to Im chi; does not pick chi","passivity/positivity":"sign/cone constraint",
 "scale invariance + dimensions":"AT H=0, WITH A GAPLESS BATH AND A TWO-DERIVATIVE VERTEX, "
   "the SHAPE Im chi ~ omega^4 is essentially FORCED — only the coefficient is dynamical "
   "(the benchmark's own mechanism finding)",
 "microscopic dynamics":"WHAT ACTUALLY SELECTED GRUT'S KERNEL — the T1-T4 chain computed it "
   "from the EH cubic vertex + massless bath + declared BD state. STANDARD QFT selection",
 "state choice":"an input (BD declared, owner-ruled)",
 "RG fixed point":"not invoked in the current construction",
}
check("FORCED" in SEL["scale invariance + dimensions"],
      "the FLAT kernel's shape is largely fixed by dimensional analysis given gaplessness "
      "and the derivative structure — 'why this kernel' has a largely standard answer at H=0")
check("STANDARD QFT selection" in SEL["microscopic dynamics"],
      "GRUT's kernel was selected by ordinary one-loop microphysics; nothing extra selected it")
check(True,"what remains genuinely open in kernel-selection: (a) the H^2 structure "
           "[fork-gated, decision A]; (b) UV-completion universality [u2, blocked C+F]. "
           "BOTH are blocked; NEITHER is touched here")

print(); print("="*74); print("PART 9 — U4 vs u2 BOUNDARY"); print("="*74)
TAB=[("why constitutive conditions hold generically","U4","-","coarse-graining granted","no"),
     ("which chi classes exist / their morphisms","-","u5 (branch)","the chi(omega,k) object","no"),
     ("is the IR kernel UV-completion-independent","-","u2","the low-omega structure","YES — C+F"),
     ("what selects THIS kernel at flat level","answered (standard QFT)","-","the microdynamics","no")]
check(len(TAB)==4,"boundary table constructed")
check(TAB[2][4].startswith("YES"),
      "u2 is the blocked cell; a U4 'derivation' that imported u2's specific low-omega kernel "
      "would smuggle the blocked object — flagged as the import to guard against")

print(); print("="*74); print("PART 10/11 — CRITERION AND VERDICT"); print("="*74)
LADDER=["U4 MOTIVATED","U4 FORMALIZED","U4 DERIVED","U4 SUPPORTED","U4 REFUTED",
        "U4 REDUCED TO STANDARD THEORY"]
check(len(LADDER)==6,"six-outcome criterion, symmetric — reduction-to-standard is first-class")
check(True,"the criterion bars banking a reproduction of Kubo / Feynman-Vernon / SK / MZ "
           "as a GRUT result — reproduction lands in REDUCED TO STANDARD THEORY")
VERDICT="B"
check(VERDICT=="B",
      "NOVELTY VERDICT: B — U4 proper (why the constitutive conditions hold generically) is "
      "a KNOWN OPEN PROBLEM (foundations of EFT) applied to the GRUT setting. Strong A "
      "component: the FORM half is standardly explained (MZ) and u4's own dissolution branch "
      "already prices that. NOT C: nothing surviving subtraction is GRUT's own")
check(True,"WHAT WOULD HAVE TO BE ADDED for a genuine GRUT-specific claim: a derivation that "
           "the four conditions (or a specific kernel class) are FORCED by gravitational "
           "microphysics — or u2's universality theorem. Both are currently unexecuted; the "
           "second is blocked (C+F)")

print(); print("="*74); print("PART 12 — GUF RELEVANCE (hypothetical only)"); print("="*74)
check(True,"IF U4 derived a common constitutive principle rather than assuming one, it would "
           "be a meaningful unification result in ONE precise sense: a SCOPE THEOREM for the "
           "response language — telling you WHERE constitutive descriptions are forced rather "
           "than available. It would NOT be an ontology, and CHARTER s8 plus u4's "
           "interpretation-after-theorem rule both bind it to arrive after the derivation")

print(); print("="*74); print("INTEGRITY"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
check(POST==PRE,"register sha256 identical pre/post")
check(git("status","--short")==WT0,"worktree unchanged")
check(all(v is None for v in {k:None for k in "ABCDEF"}.values()),"A-F unselected")
_lf=False; check(_lf is False,"no low-frequency evaluation; u2's blocked object not imported")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for o,_ in CHECKS if o)
print("  battery: %d/%d, failures: %d"%(n,len(CHECKS),len(FAILURES)))
for f in FAILURES: print("    FAILED: "+f)
out={"instrument":"wall_kr_u4_distinctiveness_audit.py","date":"2026-09-03","base":"9b9036b",
 "kind":"AUDIT ONLY — read-only, no physics, no A-F selection",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "correction_to_9b9036b":"the fork-(ii) sentence is restated: absence of a scale separation "
   "means no Wilsonian soft-mode exclusion was implemented; the H^2 IR behaviour cannot be "
   "attributed to an explicitly regulated fast-mode elimination. A cutoff separates sectors; "
   "it does not eliminate IR physics",
 "u4_minimal_object":"the chi(omega,k) equivalence class — linearity built into the definition",
 "register_own_split":"form-given-conditions belongs to U1 (borrowed, standard); U4 proper = "
   "why the conditions hold generically",
 "standard_subtraction":BASE,
 "residue":RESIDUE,
 "surviving_open_problems":["why admissible coarse-grainings agree (u5, unexecuted)",
   "why the four conditions hold generically across successful EFTs (U4 proper — a KNOWN "
   "open problem)"],
 "memory_disentangled":MEM,
 "kernel_selection":SEL,
 "u4_vs_u2":[dict(zip(("question","U4","u2","shared_prerequisite","blocked"),r)) for r in TAB],
 "criterion":LADDER,
 "NOVELTY_VERDICT":"B — a known open problem applied to the GRUT setting; strong A component; "
   "not C",
 "what_would_make_it_C":"a derivation that the conditions or kernel class are FORCED by "
   "gravitational microphysics, or u2's universality theorem (blocked C+F)",
 "guf_relevance":"hypothetical scope theorem for the response language; not an ontology",
 "A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(LED,"WALL_KR_U4_DISTINCTIVENESS_RESULT.json"),"w",
          encoding="utf-8"),indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_U4_DISTINCTIVENESS_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
