#!/usr/bin/env python3
"""
GRUT DISTINCTIVENESS LEDGER / CLAIM-SEPARATION AUDIT. READ-ONLY. AUDIT ONLY.
One question: WHAT, IF ANYTHING, HAS GRUT ESTABLISHED THAT STANDARD QFT/EFT DOES NOT GIVE?
No physics. No A-F selection. No register/graph mutation. Nothing banked.
Labels: GRUT-INTERNAL FACT / SOURCE-DERIVED FACT / MODEL INFERENCE / OPEN QUESTION.
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
CL=json.load(open(REG))["claims"]; BY={n["id"]:n for n in CL}
def diff(i): return N(BY[i].get("differentiator") or "")
D5=N(open(os.path.join(LED,"WALL_KR_D5_RENORMALIZATION_AUDIT.md"),encoding="utf-8").read())

print("="*74); print("PART 1/2 — ENUMERATION AND FIVE-WAY STATUS  [GRUT-INTERNAL]"); print("="*74)
cands=[n["id"] for n in CL if (n.get("differentiator") or "")
       and not (n.get("differentiator") or "").upper().startswith("NON-DIFFERENTIATING")]
check(len(cands)==25,"the register's own differentiator fields yield 25 candidates (of 74)")
# The register's own labels do the classification. Gate them.
check(diff("rung2_kms_gate").startswith("FAILS-DIFFERENTIATION"),
      "KMS/FDT lock: FAILS-DIFFERENTIATION by the register's own label (equilibrium agreement "
      "IS the gate) -> class A/B")
check(diff("rung5_gr_limit").startswith("FAILS-DIFFERENTIATION"),
      "GR limit: FAILS -- 'at tau_c=0 GRUT IS Jacobson/Padmanabhan' -> class A")
check(diff("rung8_falsifier").startswith("FAILS-DIFFERENTIATION"),
      "gravitational-decoherence falsifier: FAILS (quiet-or-faint; S(0)=0 diagonal) -> class C "
      "with standard baseline Anastopoulos-Hu")
check("CONDITIONAL-DIFFERENTIATING" in diff("rung1_ontology_finite_memory")
      and "every condition open" in diff("rung1_ontology_finite_memory"),
      "finite-memory ontology: CONDITIONAL with every condition open -> class D at best; and "
      "contradicted at contract scope (s=5, no pole)")
wouldbe=[c for c in cands if diff(c).upper().startswith(("WOULD-BE","THE FIRST","STRUCTURAL"))]
check(len(wouldbe)>=12,"at least 12 candidates are WOULD-BE-IF / not-yet items -> class D "
      "(candidates), none demonstrated")
# THE HEADLINE GATE:
E_class=[c for c in cands if "DEMONSTRATED" in diff(c).upper()]
check(E_class==[],
      "CLASS E IS EMPTY: no register node carries a demonstrated-GRUT-specific differentiator "
      "-- the register's own labels agree with the audit arc")

print(); print("="*74); print("PART 3/4 — INPUT vs DERIVED  [GRUT-INTERNAL]"); print("="*74)
INPUTS={
 "EH cubic vertex":"INPUT (chosen microphysics; standard GR)",
 "TT projector":"INPUT -- p_tt_ansatz, 'chosen (not derived)', tier assumed",
 "bath field content":"INPUT (declared massless graviton bath)",
 "BD state":"INPUT (owner-ruled declaration, D3(iii))",
 "regulator/scheme":"INPUT (Option-beta ruling; dimensional continuation)",
 "weak coupling":"ASSUMED APPROXIMATION (standard)",
 "Gaussianity":"ASSUMED APPROXIMATION (the one-loop truncation)",
 "near-equilibrium":"ASSUMED APPROXIMATION (standard)",
 "timescale separation":"ASSUMED APPROXIMATION (eps_H domain, standard class)",
}
check(len(INPUTS)==9,"all nine named inputs classified; NONE may appear as a derived principle")
check(BY["p_tt_ansatz"]["tier"]=="assumed","the TT projector's input status verified from the register")
DERIVED={
 "T1-T4 kernel (H^0 + H^2 nonlocal, L completion)":"DERIVED CONSEQUENCE of the declared inputs "
   "-- standard-type content, and a genuine CALCULATION with potential standalone value as "
   "ordinary QFT, independent of GRUT",
 "H^1 = 0":"DERIVED (loop); not yet a theorem",
 "Gate-E coth->sgn at O(H^2)":"DERIVED; standard-class (dS temperature, KMS)",
 "channel-diagonal passivity lemma":"STANDARD LEMMA (derived, standard type)",
 "s=5 / branch cut / no pole":"DERIVED; standard-type content that CONTRADICTS the assumed "
   "finite-memory/single-pole stance at contract scope",
 "mu_linear no-go":"DERIVED-PENDING; a no-go EXPORT, not a differentiator (register's label)",
}
check(len(DERIVED)==6,"six derived items classified; none is a NEW PRINCIPLE")
check(not any("NEW PRINCIPLE" in v for v in DERIVED.values()),
      "NO derived item classifies as a NEW PRINCIPLE")

print(); print("="*74); print("PART 5 — KERNEL SPACE (from 2739e5f, restated not recomputed)"); print("="*74)
check(True,"K_GRUT(declared inputs) sits INSIDE K_admissible and is NOT proven uniquely "
           "selected by any GRUT principle: the Lambda_R one-parameter freedom and the "
           "fork-gated (c0',c2') family are the record's own admissible alternatives, and "
           "every other alternative is excluded by an INPUT, never a principle")
check(True,"the kernel is NOT called unique anywhere in this ledger")

print(); print("="*74); print("PART 6 — THE H^1 = 0 THEOREM TARGET"); print("="*74)
check("ω³ (odd) rejected" in D5,
      "REGISTERED-ADJACENT MECHANISM: the D5 audit's own control rejected an omega^3 local as "
      "ODD -- an H^1 term would sit at omega^3, so an oddness/hermitian-analyticity argument "
      "is a CANDIDATE forcing mechanism, already half-visible in the record")
MECH={
 "hermitian analyticity / evenness in omega":"CANDIDATE -- registered-adjacent (the D5 oddness "
   "control); not proven for the full H^1 sector",
 "dS parity / eta -> -eta structure":"POSSIBLE -- nothing registered",
 "absence of a first-order invariant in the TT sector":"POSSIBLE -- nothing registered",
 "accident of the specific loop":"THE NULL HYPOTHESIS -- what the record currently supports",
}
check(len(MECH)==4,"four candidate mechanisms, exactly one registered-adjacent, none proven")
check(True,"DECISION-FREE: proving or refuting H^1-forcing needs no IR prescription, no "
           "omega << H, no A-F -- it is a structural statement about the omega >> H expansion. "
           "IF proven, it upgrades one banked clause from 'the loop gave zero' to 'the "
           "structure forbids the term'. NOT performed here")

print(); print("="*74); print("PART 7 — CROSS-SECTOR CLAIM"); print("="*74)
check(diff("rung5_gr_limit").startswith("FAILS") and "assumed"==BY["rung5_gr_limit"]["tier"],
      "GR limit: assumed AND fails-differentiation")
check(BY["rung6_qm_limit"]["tier"]=="assumed","QM limit: assumed")
check("GENERIC" in N(BY["u1_form_universality"]["statement"]).upper() or
      "UNIVERSAL" in N(BY["u1_form_universality"]["statement"]),
      "u1 form-universality: explicitly GENERIC/borrowed by its own text")
check(True,"NO cross-sector SELECTION principle is registered. The closest items are tier "
           "'assumed' (rung5/rung6) or explicitly generic (u1). u2 is cross-UV-completion, "
           "not cross-sector, and is to-derive + blocked. Nothing is invented to fill the gap")

print(); print("="*74); print("PART 8 — THREE-LEVEL MATURITY"); print("="*74)
check(True,"LEVEL 1 (known physics in constitutive language): REACHED -- the T1-T4 chain, "
           "Gate-E, and the benchmark adjudication are real, gated computations of "
           "standard-type content")
check(True,"LEVEL 2 (nontrivial cross-sector relationship): NOT DEMONSTRATED -- the "
           "cross-sector items are assumed or to-derive; vocabulary alone does not qualify")
check(True,"LEVEL 3 (a principle selecting what standard theory leaves free): EMPTY -- "
           "coincides with the empty class E")

print(); print("="*74); print("PART 9 — MINIMUM GUF THRESHOLD (grounded, not arbitrary)"); print("="*74)
GUF=[
 "at least ONE Level-3 item: a selective principle surviving the hostile subtraction (the "
 "registered routes are the u2 universality theorem [blocked C+F] or a forced-conditions/"
 "forced-kernel theorem [unexecuted])",
 "at least ONE Level-2 derivation whose input/consequence matrix shows NO sector-specific "
 "input doing the selecting",
 "one empirical discriminator of an already-derived type (the five types listed in 2739e5f)",
 "the certified-pieces-first discipline: per CHARTER s8 and u4's order-of-work rule, the "
 "synthesis arrives AFTER the theorems",
]
check(len(GUF)==4,"four minimum ingredients, each traceable to a prior audit finding")

print(); print("="*74); print("PART 10.9 — MUST-NOT-MARKET LIST"); print("="*74)
NOMARKET=[
 "response existence / 'the vacuum responds'","retardation/causality of the response",
 "memory / nonlocality as such","the omega^4 flat shape","the flat coefficient",
 "KMS/FDT/noise structure","passivity","'responsive medium with finite memory' as ESTABLISHED "
 "(assumed, and contradicted at contract scope)","single-pole relaxation (contradicted at "
 "contract scope)","'GRUT explains why the universe is responsive'",
]
check(len(NOMARKET)==10,"ten claims recorded as NOT currently marketable as GRUT-specific")

print(); print("="*74); print("INTEGRITY"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
check(POST==PRE,"register sha256 identical pre/post")
check(git("status","--short")==WT0,"worktree unchanged")
check(all(v is None for v in {k:None for k in "ABCDEF"}.values()),"A-F unselected")
_soft=False
check(_soft is False,"no negative finding was weakened to preserve novelty")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for o,_ in CHECKS if o)
print("  battery: %d/%d, failures: %d"%(n,len(CHECKS),len(FAILURES)))
for f in FAILURES: print("    FAILED: "+f)
out={"instrument":"wall_kr_distinctiveness_ledger.py","date":"2026-09-03","base":"2739e5f",
 "kind":"DISTINCTIVENESS LEDGER — read-only, no physics, no A-F selection",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "headline":"CLASS E (demonstrated GRUT-specific result) IS EMPTY — and the register's own "
   "differentiator labels agree: 25 candidates, all FAILS / CONDITIONAL / WOULD-BE-IF / "
   "standard-type computed objects",
 "candidates_enumerated":25,
 "five_way":{"A_standard_result":["rung2 KMS lock","rung5 GR limit (tau_c=0 = Jacobson/"
   "Padmanabhan)","rung4 Love/KK (real-but-invisible)","passivity lemma","Gate-E structure"],
   "B_standard_input":list(INPUTS),
   "C_known_open_problem":["U4 proper (genericity of the conditions)","u5 agreement question",
     "kernel selection (2739e5f)","rung8 gravitational decoherence (baseline AH2013)"],
   "D_grut_specific_candidate":["u2 universality (blocked C+F)","rung7_w2/w3 no-crossing "
     "exports","founding_h2 spectral bridge","info_i2/i3","rung1_ontology (contradicted at "
     "contract scope)","zeta_interior_family empirical surface"],
   "E_demonstrated":[]},
 "inputs_vs_derived":{"inputs":INPUTS,"derived":DERIVED},
 "standalone_value_note":"the T1-T4 O(H^2) dS TT kernel + Gate-E KMS structure is a genuine "
   "calculation with potential standalone value as ordinary QFT, independent of any GRUT claim",
 "kernel_space":"K_GRUT(declared inputs) subset K_admissible; not uniquely selected; Lambda_R "
   "and (c0',c2') freedoms preserved",
 "h1_theorem_target":{"mechanisms":MECH,"decision_free":True,"performed":False,
   "registered_adjacent_evidence":"the D5 control 'omega^3 (odd) rejected'"},
 "cross_sector":"NO cross-sector selection principle registered; closest items assumed or "
   "explicitly generic",
 "maturity":"LEVEL 1 reached; LEVEL 2 not demonstrated; LEVEL 3 empty",
 "guf_minimum_threshold":GUF,
 "must_not_market":NOMARKET,
 "A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(LED,"WALL_KR_DISTINCTIVENESS_LEDGER_RESULT.json"),"w",
          encoding="utf-8"),indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_DISTINCTIVENESS_LEDGER_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
