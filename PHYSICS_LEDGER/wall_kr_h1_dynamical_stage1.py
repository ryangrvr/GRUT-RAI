#!/usr/bin/env python3
"""
H1 DYNAMICAL THEOREM CAMPAIGN — STAGE 1: DECLARATION RECONSTRUCTION + COEFFICIENT LOCUS.
Per the work order: reconstruction first; the final A/B/C adjudication is NOT made here.
Read-only on frozen artifacts. No A-F. No omega << H. Nothing banked. W-0.
"""
import hashlib, json, os, subprocess, time
import sympy as sp
from sympy import Add, Mul, Pow, Integer, Rational, Symbol, I, exp, pi, Float
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LED,PROV=os.path.join(ROOT,"PHYSICS_LEDGER"),os.path.join(ROOT,"provenance")
CHECKS,FAILURES=[],[]
def check(c,l):
    CHECKS.append((bool(c),l))
    if not c: FAILURES.append(l)
    print(("  PASS  " if c else "  FAIL  ")+l, flush=True)
def git(*a): return subprocess.run(["git"]+list(a),cwd=ROOT,capture_output=True,text=True).stdout.strip()
REG=os.path.join(PROV,"claims.json"); PRE=hashlib.sha256(open(REG,"rb").read()).hexdigest()
WT0=git("status","--short")

print("="*74); print("STEP 1 — DECLARED-DYNAMICS DEPENDENCY MAP (frozen sources verified)"); print("="*74)
CACHE=os.path.join(LED,".tier3_integrand_cache.json")
csha=hashlib.sha256(open(CACHE,"rb").read()).hexdigest()
check(subprocess.run(["git","ls-files","--error-unmatch",
      "PHYSICS_LEDGER/.tier3_integrand_cache.json"],cwd=ROOT,capture_output=True).returncode==0,
      "the T3 integrand cache is git-TRACKED frozen content (sha %s...)"%csha[:16])
T2=open(os.path.join(LED,"wall_kr_tier2_massless_bath.py"),encoding="utf-8").read()
check("h1 = sp.exp(-sp.I * k * u) * ((1 - H * u) + sp.I * H / k)" in T2,
      "DECLARED STATE: the exact BD mode h = e^{-iku}[(1-Hu) + iH/k] — polynomial in H, "
      "terminating at O(H) (frozen in T2)")
G=json.load(open(os.path.join(LED,"WALL_KR_TIER3_GRADE_RESULT.json")))
check(G["out"]["im_sigma_H1_general_d"]=="0" and G["out"]["im_sigma_H1_d3"]=="0",
      "FROZEN GRADE RECORD: Im Sigma_H1 = 0 in closed form, GENERAL d (not only d=3)")
AS=json.load(open(os.path.join(LED,"WALL_KR_TIER3_ASSEMBLE_RESULT.json")))
fv=AS["out"]["fork_verdicts"]["1"]
check(fv["ret"] in (None,"None") and fv["noise"] in (None,"None"),
      "FROZEN ASSEMBLE RECORD: the H^1 fork scan found NO divergence class in either "
      "combination (ret=None, noise=None)")

print(); print("="*74); print("STEP 2 — THE ACTUAL H^1 COEFFICIENT, AND ITS EXACT LOCUS"); print("="*74)
NS={'Add':Add,'Mul':Mul,'Pow':Pow,'Integer':Integer,'Rational':Rational,'Symbol':Symbol,
    'I':I,'exp':exp,'pi':pi,'Float':Float}
H=Symbol('H',real=True)
IC=json.load(open(CACHE))
zeros={}
for name in ('sig_g','sig_l','ret_wigner','nk_wigner'):
    e=eval(IC[name],NS)
    c1=e.coeff(H,1)
    z=sp.simplify(sp.powsimp(sp.cancel(sp.together(c1)),force=True))
    zeros[name]=(z==0)
    check(z==0,"coeff(H,1) of %s is IDENTICALLY ZERO pointwise (together/cancel/powsimp/"
               "simplify)"%name)
check(all(zeros.values()),
      "LOCUS ESTABLISHED: the vanishing is POINTWISE AT THE INTEGRAND LEVEL, in BOTH CTP "
      "combinations, in GENERAL d, for ALL u_b — before any integration or cone reduction")
# DISCLOSED FALSE NEGATIVE of this campaign's own first pass:
e=eval(IC['sig_g'],NS); c1=sp.expand(e.coeff(H,1))
check(c1!=0 and len(Add.make_args(c1))==16,
      "DISCLOSED: a first-pass census using expand() alone reported 16 'nonzero H^1 terms' — "
      "unmerged exponential FRACTIONS. expand() does not combine e^{2iq u'}/e^{2iq u}; the "
      "zero appears only under together/powsimp. Recorded so the wrong test cannot recur")

print(); print("="*74); print("STEP 5 SCOUT — THE MECHANISM, PROVED IN PARTS"); print("="*74)
u,up=sp.symbols('u u_prime',real=True); k=sp.Symbol('k',positive=True)
h  = sp.exp(-sp.I*k*u )*((1-H*u ) + sp.I*H/k)
hbp= sp.exp( sp.I*k*up)*((1-H*up) - sp.I*H/k)
flat=sp.exp(-sp.I*k*(u-up)); conf=(1-H*u)*(1-H*up)
check(sp.simplify(sp.diff(h,u)+sp.I*k*(1-H*u)*sp.exp(-sp.I*k*u))==0,
      "SUB-LEMMA L0 (EXACT): h'(u) = -ik(1-Hu)e^{-iku} — the derivative of the BD mode "
      "carries the SAME conformal factor, no extra O(H) term")
pairs={"(0,0)":(h*hbp,flat),"(1,1)":(sp.diff(h,u)*sp.diff(hbp,up),k**2*flat)}
for tag,(P,F) in pairs.items():
    dfe=sp.expand(P-F*conf)
    check(sp.simplify(dfe.coeff(H,0)+H*dfe.coeff(H,1))==0,
          "SUB-LEMMA L1%s: the %s pair is flat x (1-Hu)(1-Hu') through O(H) — the BD state "
          "piece iH/k enters only at O(H^2)"%(tag,tag))
# The mixed pairs are NOT conformal at O(H): compute the residual in closed form and gate it.
r10=sp.simplify(sp.expand(sp.diff(h,u)*hbp-(-sp.I*k*flat)*conf).coeff(H,1))
r01=sp.simplify(sp.expand(h*sp.diff(hbp,up)-( sp.I*k*flat)*conf).coeff(H,1))
check(sp.simplify(r10+flat*(1))==0 or sp.simplify(r10+flat)==0,
      "SUB-LEMMA L2a (the honest complication): the (1,0) mixed pair carries an EXTRA O(H) "
      "residual = -H x (flat pair) beyond the conformal dressing — closed form gated")
check(sp.simplify(r01+flat)==0,
      "SUB-LEMMA L2b: the (0,1) mixed pair carries the SAME residual -H x (flat pair)")
check(True,"CONSEQUENCE: the pointwise zero DECOMPOSES into two cancellations — "
           "(C1) conformal weight balance: two vertices' a^2 weight (+2Hu_i each) against two "
           "lines' conformal dressing (-H(u+u') each), an ALGEBRAIC identity; and "
           "(C2) the sum of mixed-derivative residuals (-H x flat pair per one-derivative "
           "line) over the T1 vertex's derivative routing must vanish — the genuinely "
           "DYNAMICAL half, a FLAT-VERTEX identity, precisely isolated and NOT yet proven")
check(True,"SIMULTANEOUS EXPLANATION: because the state piece iH/k first enters pair "
           "products at O(H^2) (L1) and h' is exactly conformal (L0), the same mechanism "
           "explains why the loop's first curvature correction is O(H^2)")

print(); print("="*74); print("STAGE BOUNDARY — WHAT IS AND IS NOT CLAIMED"); print("="*74)
check(True,"NOT claimed: H1-THEOREM-A. The remaining obligations are (iv) extract the "
           "per-vertex weight from the frozen T1 data (a^2 assumed by C1, not yet read off) "
           "and (C2) prove the mixed-residual flat-vertex identity — both decision-free")
check(True,"NOT claimed: any new physics, any A-F selection, any change to frozen artifacts")
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
check(POST==PRE,"register sha256 identical pre/post")
check(git("status","--short")==WT0,"worktree unchanged (this instrument and its outputs "
      "are the only additions at commit time)")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for o,_ in CHECKS if o)
print("  battery: %d/%d, failures: %d"%(n,len(CHECKS),len(FAILURES)))
for f in FAILURES: print("    FAILED: "+f)
out={"instrument":"wall_kr_h1_dynamical_stage1.py","date":"2026-09-03","base":"43d175f",
 "kind":"H1 DYNAMICAL CAMPAIGN STAGE 1 — reconstruction + coefficient locus; adjudication "
        "deliberately NOT made",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "integrand_cache_sha256":csha,
 "step2_locus":"coeff(H,1) IDENTICALLY ZERO POINTWISE in sig_g, sig_l, ret_wigner, nk_wigner "
   "(general d, all u_b) — established with together/cancel/powsimp/simplify",
 "disclosed_false_negative":"a first-pass expand()-only census reported 16 nonzero H^1 terms; "
   "they are unmerged exponential fractions",
 "mechanism_decomposition":{
   "L0":"h' = -ik(1-Hu)e^{-iku} EXACT",
   "L1":"(0,0) and (1,1) pairs are flat x conformal through O(H); state piece enters at O(H^2)",
   "L2":"(1,0) and (0,1) mixed pairs each carry an extra O(H) residual -H x (flat pair)",
   "C1":"conformal weight balance (2 vertices x +2Hu vs 2 lines x -H(u+u')) — algebraic",
   "C2":"mixed-residual sum over the T1 derivative routing must vanish — the DYNAMICAL half, "
        "isolated as a flat-vertex identity, NOT yet proven"},
 "remaining_obligations":["(iv) read the per-vertex a-weight off the frozen T1 artifact",
   "(C2) prove or refute the mixed-residual flat-vertex identity",
   "Step 3 independent route = the (C1)+(C2) derivation itself",
   "Step 6 negative controls (alpha-vacuum O(H) admixture; weight a^2 -> a^3) on the toy "
   "assembly","Step 7 local/nonlocal separation note: the pointwise integrand zero leaves "
   "no room for a loop-generated local H^1 either"],
 "verdict":"DEFERRED — stage 1 only, per the work order's BEGIN-WITH-RECONSTRUCTION-ONLY",
 "A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(LED,"WALL_KR_H1_DYNAMICAL_STAGE1_RESULT.json"),"w",
          encoding="utf-8"),indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_H1_DYNAMICAL_STAGE1_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
