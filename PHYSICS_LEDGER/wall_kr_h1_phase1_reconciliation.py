#!/usr/bin/env python3
"""
H1 CLOSURE — PHASE 1 RECONCILIATION: both adversarial-leg verdicts adopted under gate.
The pairing algebra stood (CONFIRMED, no mathematical error). Adopted here:
  - leg 1: the mechanism NAME was wrong ("vertex-exchange antisymmetry" is a mislabel;
    true exchange transports omega, and THAT variant is gated FALSE — promoted to a named
    negative result); the T_{j,m} one-line reformulation; the any-antisymmetric-weight
    strengthening; sector-locality.
  - leg 2: quantifier pinned to the three TT configs (cache's 4th entry 'ward' untested,
    non-TT); status verbs split (implication DERIVED, swap relation GATED-not-derived);
    Protection-1 identity claim RETRACTED; and three instrument defects in the Phase-1
    script DISCLOSED (vacuous ancestry gate; battery inflation 15/15 -> honest 12/12;
    pairing gated on plus_z only — cured here by gating T-symmetry on ALL THREE configs).
Only testable gates are counted; prose statuses are printed, not gated. Read-only. W-0.
"""
import hashlib, json, os, subprocess, sys, time
import sympy as sp
from collections import defaultdict
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
PROV=os.path.join(ROOT,"provenance")
CHECKS,FAILURES=[],[]
def gate(c,l):
    CHECKS.append((bool(c),l))
    if not c: FAILURES.append(l)
    print(("  PASS  " if c else "  FAIL  ")+l, flush=True)
def note(l): print("  NOTE  "+l, flush=True)
def git(*a): return subprocess.run(["git"]+list(a),cwd=ROOT,capture_output=True,text=True)
REG=os.path.join(PROV,"claims.json"); PRE=hashlib.sha256(open(REG,"rb").read()).hexdigest()
t0=time.time()
def iszero(e): return sp.simplify(sp.powsimp(sp.cancel(sp.together(e)),force=True))==0

print("="*74); print("GOVERNANCE (testable gates only)"); print("="*74)
HEAD=git("rev-parse","HEAD").stdout.strip(); ov4=git("rev-parse","origin/v4").stdout.strip()
gate(HEAD!="" and HEAD==ov4,"v4 verified BY REF IDENTITY (HEAD == origin/v4 == %s)"%HEAD[:12])
# the Phase-1 instrument's ancestry gate compared stdout to "" — vacuous, since
# merge-base --is-ancestor signals ONLY via exit code. Correct form, plus a live
# negative control proving this gate CAN fail:
gate(git("merge-base","--is-ancestor","41b7df1","HEAD").returncode==0,
     "41b7df1 (Phase 1) in ancestry — tested by RETURNCODE (the Phase-1 instrument's "
     "stdout-based form was vacuous and is disclosed as such)")
gate(git("merge-base","--is-ancestor","HEAD~5","HEAD").returncode==0
     and git("merge-base","--is-ancestor","HEAD","HEAD~1").returncode!=0,
     "negative control: the returncode-based ancestry test distinguishes true from false")
note("A-F remain UNSELECTED; W-0 — printed as status, NOT counted as a gate "
     "(the Phase-1 battery counted an untestable constructed-dict A-F check; not repeated)")

src=open(os.path.join(HERE,"wall_kr_tier3_loop.py"),encoding="utf-8").read()
M={"__name__":"frozen_t3","__file__":os.path.join(HERE,"wall_kr_tier3_loop.py")}
argv0=sys.argv; sys.argv=["x","machinery_only"]; os.chdir(HERE)
try: exec(compile(src,"t3","exec"),M)
except SystemExit: pass
sys.argv=argv0
CM,cdecomp,Ptt,htrunc=M["CM"],M["cdecomp"],M["Ptt"],M["htrunc"]
H,u,up,om,q=M["H"],M["u"],M["up"],M["om"],M["q"]
n1,n2,n3=M["n1"],M["n2"],M["n3"]; PAIRS=M["PAIRS"]
gate(set(CM)-{"meta"}=={"plus_z","cross_z","plus_x","ward"} and isinstance(CM["meta"],str),
     "quantifier domain PINNED: the frozen C-cache's configuration entries are exactly the "
     "three TT configs plus the non-TT 'ward' probe (plus a 'meta' docstring entry; full "
     "keys %s) — 'ward' is outside the declared TT contraction and remains UNTESTED"
     %sorted(CM))
qsub={}
for i_,tgt in ((1,n1),(2,n2),(3,n3)):
    qsub[sp.Symbol("q%d"%i_)]=q*tgt
    qsub[sp.Symbol("q%d"%i_,real=True)]=q*tgt
def build_S(config):
    Cs={kk:sp.sympify(vv).subs(H,0) for kk,vv in CM[config].items()}
    D1,D2={},{}
    for kk,vv in Cs.items():
        if vv==0: continue
        D1[kk]=cdecomp(htrunc(sp.expand(vv.xreplace(qsub))))
        v2=vv.xreplace(qsub).xreplace({q:-q}).subs(om,-om).subs(u,up)
        D2[kk]=cdecomp(htrunc(sp.expand(v2)))
    P_line={}
    for (a,b) in PAIRS:
        for (ap,bp) in PAIRS: P_line[((a,b),(ap,bp))]=Ptt(a,b,ap,bp)
    S=defaultdict(lambda: sp.Integer(0))
    for (a,b) in PAIRS:
        for (c,dd_) in PAIRS:
            k1="%d%d_%d%d"%(a,b,c,dd_)
            if k1 not in D1: continue
            for (ap,bp) in PAIRS:
                for (cp,dp) in PAIRS:
                    k2="%d%d_%d%d"%(ap,bp,cp,dp)
                    if k2 not in D2: continue
                    PA=P_line[((a,b),(ap,bp))]; PB=P_line[((c,dd_),(cp,dp))]
                    if PA==0 or PB==0: continue
                    PP=sp.expand(PA*PB)
                    for (nm1,nu1m),c1 in D1[k1].items():
                        for (nm2,nu2m),c2 in D2[k2].items():
                            S[(nu1m[0]+nu1m[1],nu2m[0]+nu2m[1])]+=sp.expand(c1*c2*PP
                                *(n1**(nm1[0]+nm2[0]))*(n2**(nm1[1]+nm2[1]))
                                *(n3**(nm1[2]+nm2[2])))
    return S

print(); print("="*74); print("THE CORRECTED MECHANISM — GATED ON ALL THREE TT CONFIGS")
print("(the Phase-1 pairing gate ran on plus_z only; cured here)"); print("="*74)
for config in ("plus_z","cross_z","plus_x"):
    S=build_S(config)
    T={jm: sp.expand((-1)**jm[0]*v) for jm,v in S.items()}
    gate(all(iszero(T.get((m_,j_),0)-T.get((j_,m_),0)) for (j_,m_) in S),
         "[%s] ONE-LINE REFORMULATION: T_(j,m) := (-1)^j S_(j,m) is TRANSPOSITION-"
         "SYMMETRIC — F1 is a fixed-argument GRADED ROUTING-TRANSPOSITION SYMMETRY "
         "(slot-exchange parity, sign (-1)^N per sector), NOT a vertex-exchange "
         "identity   [%.0fs]"%(config,time.time()-t0))
    ok_w=True
    for wfun in (lambda j_,m_: m_-j_, lambda j_,m_:(m_-j_)**3):
        tot=defaultdict(lambda: sp.Integer(0))
        for (j_,m_),v in T.items(): tot[j_+m_]+=sp.expand(wfun(j_,m_)*v)
        ok_w &= all(iszero(v) for v in tot.values())
    gate(ok_w,"[%s] STRONGER FACT: any transposition-antisymmetric weight — gated with "
         "(m-j) and (m-j)^3 — annihilates T per sector; F2's weight is nothing special"
         %config)
    gate(any(not iszero(S.get((m_,j_),0).subs(om,-om)-(-1)**(j_+m_)*S.get((j_,m_),0))
             for (j_,m_) in S),
         "[%s] NAMED NEGATIVE RESULT: the omega-TRANSPORTING variant S_(m,j)(-omega) = "
         "(-1)^(j+m) S_(j,m)(omega) — what TRUE vertex exchange would give — is FALSE; "
         "its falsity is LOAD-BEARING for the identity holding POINTWISE in omega"%config)

print(); print("="*74); print("EDITORIAL CORRECTIONS PRESENT IN THE RECORD"); print("="*74)
mdp=os.path.join(HERE,"WALL_KR_H1_PHASE1.md"); md=open(mdp,encoding="utf-8").read()
gate("RECONCILIATION" in md and "graded routing-transposition symmetry" in md,
     "record carries the RECONCILIATION section with the corrected mechanism name")
gate("RETRACTED" in md and "Protection 1" in md,
     "the 'SAME mechanism as Protection 1' identity claim is RETRACTED in the record "
     "(the link stays NOT ESTABLISHED, per the standing 2B.4.2.5 leg-3 assessment)")
gate("ward" in md and "three TT configurations" in md,
     "quantifier PINNED to the three TT configurations; 'ward' noted untested/non-TT")
gate("closed under" in md,"transposition range-closure caveat stated")
gate("sector-local" in md,"sector-locality (N <= 4 only) of F1 => F2 stated")
gate("vacuous" in md.lower() and "12/12" in md,
     "the Phase-1 instrument defects are DISCLOSED in the record (vacuous ancestry gate; "
     "battery inflation — honest count 12/12; pairing gated on plus_z only)")

print(); print("="*74); print("GOVERNANCE (post)"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
gate(POST==PRE,"register sha256 identical pre/post")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for ok,_ in CHECKS if ok)
print("  battery: %d/%d testable gates, failures: %d   [%.0fs]"
      %(n,len(CHECKS),len(FAILURES),time.time()-t0))
for f in FAILURES: print("    FAILED: "+f)
out={"instrument":"wall_kr_h1_phase1_reconciliation.py","date":"2026-09-03","base":"41b7df1",
 "kind":"Phase-1 reconciliation — both adversarial-leg verdicts adopted under gate",
 "battery":"%d/%d testable"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "corrections":[
  "mechanism RENAMED: graded routing-transposition symmetry / slot-exchange parity "
  "(sign (-1)^N), NOT vertex-exchange antisymmetry",
  "omega-transporting (true-exchange) variant gated FALSE on all three configs — promoted "
  "to a NAMED NEGATIVE RESULT, load-bearing for pointwise-in-omega vanishing",
  "'SAME mechanism as Protection 1' RETRACTED (identity claim untested inside a passing "
  "gate's label — the self-certification shape); link remains plausible-not-established",
  "quantifier pinned to the three TT configs; 'ward' (non-TT) untested; the three do not "
  "span the general polarization bilinear space (harmless — generality not claimed)",
  "status verbs split: implication DERIVED, swap relation GATED-not-derived; F1=>F2 "
  "sector-local (N<=4); F2 is a consistency corollary, not independent evidence",
  "T-symmetry + any-antisymmetric-weight strengthening gated on ALL THREE configs",
  "Phase-1 instrument defects disclosed: vacuous ancestry gate (stdout vs returncode); "
  "battery inflation (15/15 counted three untestable gates; honest 12/12); pairing gate "
  "plus_z-only"],
 "pairing_algebra":"CONFIRMED by both legs; no mathematical error",
 "scope":"THEOREM-LOCAL stands (leg 2: 'honest'), with the quantifier now pinned",
 "A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(HERE,"WALL_KR_H1_PHASE1_RECON_RESULT.json"),"w",
          encoding="utf-8"),indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_H1_PHASE1_RECON_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
