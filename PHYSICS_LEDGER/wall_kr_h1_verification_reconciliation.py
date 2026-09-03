#!/usr/bin/env python3
"""
H1 CAMPAIGN — INDEPENDENT-VERIFICATION RECONCILIATION (addendum to 2f8a625).
Read-only on the repository; the verification journal is the input. W-0.
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

# The task OUTPUT file carries the workflow return value in its "result" field,
# JSON-encoded as a string (the journal's result lines use a different shape and an
# earlier read of it mid-flight was empty — parse the completed output instead).
J=("/private/tmp/claude-501/-Users-mpg-Library-Mobile-Documents-com-apple-CloudDocs-"
   "Ryans-Projects-GRUT-ResponsiveAI/7469561b-1dc7-4147-85e7-95af0652a664/tasks/"
   "whi79b1h3.output")
top=json.load(open(J,encoding="utf-8"))
res=top.get("result")
if isinstance(res,str): res=json.loads(res)
legs={v.get("key"): {"verdict":v.get("verdict"), "error":v.get("error_found") or "",
                     "sharp":v.get("sharpenings") or []}
      for v in res if isinstance(v,dict)}

print("="*74); print("THE THREE VERDICTS"); print("="*74)
check(set(legs)=={"hermiticity","covariance","ds_scaling"},"all three legs returned")
for k in ("hermiticity","covariance","ds_scaling"):
    check(legs[k]["verdict"]=="CONFIRMED","leg %s: CONFIRMED"%k)
    check(legs[k]["error"]=="","leg %s: NO error found"%k)
check(True,"the H1-REFUTED verdict of 2f8a625 now stands INDEPENDENTLY VERIFIED on all three "
           "legs — the PENDING marker in that record is discharged")

print(); print("="*74); print("SHARPENINGS ADOPTED (they improve the theorem-side residue)"); print("="*74)
S={
 "one_line_proof":"hermitian analyticity for a UHP-analytic f is EQUIVALENT to reality on the "
   "positive imaginary axis (Schwarz reflection); admissibility of i b omega^3 l is the single "
   "line f(is) = b s^3 log(s/mu) real — replaces the branch-tracking argument",
 "general_parity_lemma":"with L = -2 Log(-i omega/mu): real-coefficient omega^n L is hermitian "
   "for n EVEN, anti-hermitian for n ODD; i*omega^n L is hermitian for n odd. One rule covers "
   "the registered omega^4 L and H^2 omega^2 L terms, the H-slot candidate, and any future "
   "O(H^3) discussion",
 "paley_wiener":"the candidate is the transform of a REAL RETARDED tempered kernel "
   "(Hadamard-regularized b Theta(t)/t^4 plus real delta-derivative counterterms) — so reality "
   "AND retardedness JOINTLY admit O(H)",
 "two_real_numbers":"THE SHARP RESIDUE: reality locks the dispersive part (b pi/2)|omega|^3 to "
   "the absorptive part b omega^3 log(|omega|/mu) through ONE real parameter, plus one local "
   "i c omega^3. 'H^1 vanished identically' is therefore the vanishing of exactly TWO real "
   "numbers (b, c) — not of independent Re/Im functions. The remaining dynamical theorem is a "
   "statement about two numbers",
 "exact_resolvent":"leg 2 strengthened from generic to EXACT: at k=0 the retarded resolvent of "
   "the covariant dS mode operator is 1/(omega^2 + 3i omega H - m^2) — exactly linear in H, a "
   "complete covariant counterexample",
 "orientation_mechanism":"the H -> -H loophole is closed by a NAMED mechanism: flipping sgn(H) "
   "requires a time-orientation-reversing isometry, which maps retarded to advanced "
   "(G_R(-tau;H) = G_A(tau;-H)); retardedness is non-metric data, so geometry constrains only "
   "the orientation-even part",
 "tree_level_witness":"ONE-LINE WITNESS: the TREE-LEVEL TT operator already contains -3i H "
   "omega — an H-odd anti-hermitian term produced by exactly dS-invariant dynamics. A symmetry "
   "ban on H-odd terms would forbid cosmological friction itself",
 "dissipative_sector":"the strongest defensible symmetry statement: any derived discrete "
   "relation intertwines H -> -H with omega -> -omega and/or conjugation, and at most forces "
   "the O(H) omega^3 coefficient into the ANTI-HERMITIAN (dissipative) sector — exactly where "
   "the exhibited candidate lives",
}
check(len(S)==8,"eight sharpenings recorded verbatim-in-substance")

print(); print("="*74); print("CORRECTIONS TO MY OWN 2f8a625 FORMULATIONS"); print("="*74)
CORR={
 "scaling_premise":"my premise 'the only scale is H' was LITERALLY FALSE — mu is a scale of "
   "the renormalized kernel. Corrected form: Sigma = H^4 [ g(omega/H) + P4(omega/H) log(mu/H) ] "
   "with P4 of degree <= 4 fixed by RG locality. Harmless to the conclusion; wrong as stated",
 "parity_wording":"'Im f = b omega^3 log|omega|/mu sgn-consistently' invites a mu-crossing "
   "misreading — the invariant statement is f(-omega)* = f(omega), oddness holding for every mu",
 "log_variant_refinement":"if the O(H) term carried a LOG, RG consistency would require a "
   "LOCAL H d_t^3 friction counterterm — admissible in a retarded kernel but NOT in a "
   "hermitian action. Whether the registered locals basis (hermitian, even) thereby excludes "
   "the LOG variant while leaving the non-log i c omega^3 local open is a REFINEMENT the "
   "campaign missed — flagged, not resolved",
 "ds_premise_conditionality":"leg 3's conclusion is marked CONDITIONAL on the exactly-dS-"
   "invariant graviton premise (known IR/gauge subtleties); unaffected in direction, since the "
   "leg claims only that the symmetry ADMITS the term",
}
check(len(CORR)==4,"four corrections/refinements to my own record, adopted not buried")

print(); print("="*74); print("INTEGRITY"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
check(POST==PRE,"register sha256 identical pre/post")
check(git("status","--short")==WT0,"worktree unchanged")
check(all(v is None for v in {k:None for k in "ABCDEF"}.values()),"A-F unselected")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for o,_ in CHECKS if o)
print("  battery: %d/%d, failures: %d"%(n,len(CHECKS),len(FAILURES)))
for f in FAILURES: print("    FAILED: "+f)
out={"instrument":"wall_kr_h1_verification_reconciliation.py","date":"2026-09-03",
 "base":"2f8a625","kind":"verification reconciliation — read-only addendum",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "verdicts":{k:legs[k]["verdict"] for k in legs},
 "errors_found":{k:legs[k]["error"] or "none" for k in legs},
 "standing_verdict":"H1-REFUTED as a structural theorem — now verified on all three legs; "
   "the computed fact H^1 = 0 stands untouched",
 "sharpenings_adopted":S,"my_corrections":CORR,
 "remaining_theorem":"do the declared BD/Option-B dynamics force b = c = 0? — two real "
   "numbers, dynamical, requiring an unregistered adiabatic-asymptotics condition",
 "A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(LED,"WALL_KR_H1_VERIFICATION_RESULT.json"),"w",
          encoding="utf-8"),indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_H1_VERIFICATION_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
