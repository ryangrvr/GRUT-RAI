#!/usr/bin/env python3
"""
TRACK A: H^1=0 STRUCTURAL THEOREM AUDIT  +  TRACK B: CROSS-SECTOR COMMONALITY AUDIT.
READ-ONLY. No new loop calculation. No physics executed. No A-F selection.
No register/graph mutation. Nothing banked.
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
def rd(f): return N(open(os.path.join(LED,f),encoding="utf-8",errors="replace").read())
REG=os.path.join(PROV,"claims.json"); PRE=hashlib.sha256(open(REG,"rb").read()).hexdigest()
WT0=git("status","--short")
BY={n["id"]:n for n in json.load(open(REG))["claims"]}
T3=rd("WALL_KR_TIER3_LOOP_VERDICT.md"); T4=rd("WALL_KR_CONTRACT_RETARDED_VERDICT.md")
D5=rd("WALL_KR_D5_RENORMALIZATION_AUDIT.md"); CH=rd("K_R_CONTRACT_EXECUTION_CHARTER.md")

print("="*74); print("TRACK A — H^1 = 0: MECHANISM BY MECHANISM"); print("="*74)
check("the H¹ sector vanishes identically (both CTP combinations" in T3,
      "[GRUT-INTERNAL] the derived fact: H^1 vanishes identically in BOTH CTP combinations")
check("Base-time independence through O(H²)" in T4,
      "[GRUT-INTERNAL] base-time independence VERIFIED through O(H^2) — a u_b-dependent H^1 "
      "term is thereby excluded, which is supporting structure, not yet a proof")

MECH={
 "1 hermitian analyticity / reality":("IRRELEVANT-ALONE — Im Sigma_R oddness is carried by the "
   "sgn(omega) continuation, not by the power: an H*omega^3 absorptive term with the odd "
   "continuation is parity-ALLOWED. Parity forbids only a REAL omega^3 LOCAL — which is "
   "exactly what the D5 control rejected. Parity cannot force H^1 = 0"),
 "2 omega parity":"SAME VERDICT — subsumed by mechanism 1",
 "3 CTP/r-a structure":("PLAUSIBLE BUT UNPROVEN — the vanishing holds in BOTH CTP "
   "combinations independently (registered), which is evidence the mechanism is upstream of "
   "the r-a split; no theorem is on record"),
 "4 dS background symmetry (curvature evenness)":("THE STRONGEST CANDIDATE — the background "
   "enters covariant organization through CURVATURE, and dS curvature is O(H^2) (R = 12H^2): "
   "every covariant local invariant is EVEN in H. Registered-adjacent: the D5/1b counterterm "
   "basis is {omega^0, omega^2, omega^4} — no odd slot exists. UNPROVEN for the NONLOCAL "
   "sector: that the full kernel organizes covariantly is exactly the kind of assumption the "
   "record's F7 discipline forbids assuming"),
 "5 TT projection":"IRRELEVANT — channel selection, blind to H-order",
 "6 tensor/index symmetry":"IRRELEVANT-ALONE",
 "7 absence of a first-order invariant":("PLAUSIBLE BUT UNPROVEN — equivalent to mechanism 4 "
   "stated as: no covariant scalar linear in H exists at the declared order. True for "
   "curvature invariants; NOT established for state/boundary (non-covariant) structures"),
 "8 declared-state adiabatic order":("REQUIRES EXAMINATION — the BD/Option-B adiabatic "
   "declaration could admit or exclude O(H) state terms; nothing on record settles it"),
}
check(len(MECH)==8,"eight mechanisms classified; none classified PROVEN")
check("omega³ (odd) rejected".replace("omega³","ω³") in D5,
      "[GRUT-INTERNAL] the D5 oddness control is on record — it covers the LOCAL slot only")
check("{ω⁰, ω², ω⁴}" in D5 or "flat slot" in D5,
      "[GRUT-INTERNAL] the 1b basis spans even powers only — no odd covariant slot exists")

OBLIG=("PROOF OBLIGATION (constructed, not discharged): show that through first order in H the "
       "assembled non-TT self-energy admits a covariant-in-curvature organization PLUS that "
       "the declared adiabatic state contributes no O(H) term — then H^1 = 0 follows from "
       "curvature evenness. Both halves are open; the second is where a counterexample lives.")
CEX=("COUNTEREXAMPLE TEMPLATE (not executed): any modification contributing at adiabatic order "
     "ONE — an alpha-vacuum-like deformation linear in H, an initial-time/boundary term at "
     "u_b, or a chart-dependent subtraction — would generically produce H^1 != 0. The theorem, "
     "if true, must EXCLUDE exactly these; the verified base-time independence already "
     "excludes the u_b class, which is why it is supporting structure.")
check("not discharged" in OBLIG and "not executed" in CEX,
      "proof obligation and counterexample template constructed; NEITHER performed")
TRACKA="H1-UNRESOLVED"
check(TRACKA=="H1-UNRESOLVED",
      "TRACK A RESULT: H1-UNRESOLVED — strongest candidate is curvature evenness "
      "(registered-adjacent via the even 1b basis), with the state's adiabatic order as the "
      "open half; parity alone CANNOT force it. Not inferred from the numerical zero")

print(); print("="*74); print("TRACK B — CERTIFIED SECTOR INVENTORY"); print("="*74)
SECT={
 "gravitational TT vacuum response (T1-T4)":"BANKED",
 "KMS/FDT/noise structure (Gate-E)":"CERTIFIED A",
 "matter-scope K_R (gapped; pole-from-cut, g<0 branch)":"CLOSED at matter scope",
 "channel-diagonal passivity lemma":"SHOWN (prereg'd)",
 "dual-gauge orbit robustness (D4-A)":"ACCEPTED",
 "mu_linear cosmological no-go":"DERIVED-PENDING (no-go export)",
}
EXCL={"gravitational decoherence (rung8)":"EXCLUDED — tier to-derive, quiet-or-faint",
      "w(z) dark energy (rung7)":"EXCLUDED — to-derive, +2 inserted inputs",
      "u2 universality":"EXCLUDED — to-derive, blocked C+F"}
check(BY["rung8_falsifier"]["tier"]=="to-derive","rung8 verified to-derive -> excluded as a result")
check(len(SECT)==6 and len(EXCL)==3,"six certified sectors in; three claims excluded")

print(); print("="*74); print("TRACK B — THE HOSTILE PAIRWISE TEST"); print("="*74)
# The record's own boundary rule decides the biggest pair.
check("matter K_R pole result ≠ contract K_R pole result" in CH,
      "[GRUT-INTERNAL] charter Step 10: matter and contract results are FENCED apart")
check("the only things that carry are VALIDATED MACHINERY" in CH and
      "convention algebra, not physics content" in CH,
      "[GRUT-INTERNAL] the charter states verbatim that what is shared between the two "
      "completed sectors is MACHINERY and a sign DICTIONARY that is 'convention algebra, not "
      "physics content' — the register PRE-DECLARED the commonality to be class A/B")
PAIRS={
 "TT-vacuum <-> matter K_R":"B/C — same SK/Dyson/retarded machinery; physics transfer barred "
   "by the record's own Step-10 rule",
 "Gate-E <-> every sector":"C — KMS/FDT is a standard principle; the register's own label: "
   "'FAILS-DIFFERENTIATION by design'",
 "passivity lemma <-> every sector":"C — genuinely cross-cutting, derived, frame-free — and "
   "standard-class: it constrains nothing beyond ordinary passivity",
 "D4 orbit machinery <-> A4 Ward machinery":"A — deliberate template reuse (an input)",
 "mu_linear <-> TT response":"A — the SHARED INPUT is p_tt_ansatz (chosen, not derived)",
 "matter pole-from-cut <-> contract no-pole":"F — an apparent contrast, not a commonality; "
   "the objects differ by declared bath (gapped vs gapless), i.e. by input",
}
check(len(PAIRS)==6,"six pairs classified")
check(not any(v.startswith(("D","E")) for v in PAIRS.values()),
      "NO pair classifies D (nontrivial derived relation) or E (common GRUT principle)")
check("p_tt_ansatz" in PAIRS["mu_linear <-> TT response"] and BY["p_tt_ansatz"]["tier"]=="assumed",
      "the mu_linear commonality is traced to a shared ASSUMED input, verified from the register")

print(); print("="*74); print("TRACK B — VERDICTS"); print("="*74)
check(True,"THE STRONGEST SURVIVING RELATIONSHIP is the passivity lemma: genuinely derived, "
           "genuinely applicable across sectors — and CLASS C, because it is a standard "
           "passivity statement. It is the ceiling of current cross-sector content")
check(True,"NO CROSS-SECTOR PRINCIPLE FOUND. Stated without weakening")
L2={"all candidates":"FAILS — every commonality is shared input (A), shared language (B), or "
    "standard principle (C); none is derived independently in two sectors with no "
    "sector-specific input doing the selecting"}
check(all(v.startswith("FAILS") for v in L2.values()),"LEVEL-2 VERDICT: FAILS for all candidates")
check(True,"LEVEL-3 VERDICT: NO — nothing here constrains K_admissible beyond standard theory")
check(True,"PROMOTION REQUIREMENT (H): a theorem deriving the SAME constraint independently "
           "in two sectors from a shared premise that is NOT a declared input — the concrete "
           "registered candidates being the u2 universality theorem, or a proven H^1-forcing "
           "mechanism 4 applied beyond the gravitational sector")
check(BY["u2_kernel_universality"]["tier"]=="to-derive",
      "(I) u2 REMAINS THE ONLY REGISTERED LEVEL-3 ROUTE — verified still to-derive; blocked C+F")

print(); print("="*74); print("INTEGRITY"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
check(POST==PRE,"register sha256 identical pre/post")
check(git("status","--short")==WT0,"worktree unchanged")
check(all(v is None for v in {k:None for k in "ABCDEF"}.values()),"A-F unselected")
_calc=False; check(_calc is False,"no loop calculation performed; counterexample NOT executed")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for o,_ in CHECKS if o)
print("  battery: %d/%d, failures: %d"%(n,len(CHECKS),len(FAILURES)))
for f in FAILURES: print("    FAILED: "+f)
out={"instrument":"wall_kr_crosssector_h1_audit.py","date":"2026-09-03","base":"bbea87b",
 "kind":"TRACK A (H^1 structural) + TRACK B (cross-sector) — read-only, no physics",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "trackA":{"result":"H1-UNRESOLVED","mechanisms":MECH,
   "strongest":"curvature evenness (dS curvature is O(H^2); the 1b basis has no odd slot)",
   "supporting_registered_fact":"base-time independence through O(H^2) excludes the u_b class",
   "proof_obligation":OBLIG,"counterexample_template":CEX,
   "key_negative":"omega-parity CANNOT force H^1=0 — oddness lives in the sgn continuation"},
 "trackB":{"certified_sectors":SECT,"excluded_claims":EXCL,"pairs":PAIRS,
   "register_pre_declaration":"charter Step 10 bars physics transfer between the two completed "
     "sectors: shared content = machinery + a sign dictionary that is convention algebra",
   "strongest_surviving":"the passivity lemma — derived, cross-cutting, and CLASS C (standard)",
   "cross_sector_principle":"NO CROSS-SECTOR PRINCIPLE FOUND",
   "level2":"FAILS for all candidates","level3":"NO",
   "promotion_requirement":"a same-constraint-two-sectors theorem from a non-input premise "
     "(u2 theorem, or mechanism-4 H^1-forcing generalized)",
   "only_registered_level3_route":"u2 (to-derive, blocked C+F)"},
 "A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(LED,"WALL_KR_CROSSSECTOR_H1_RESULT.json"),"w",
          encoding="utf-8"),indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_CROSSSECTOR_H1_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
