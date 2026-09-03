#!/usr/bin/env python3
"""
H1 PHASE 2 — POST-ANGULAR NOTE (gated addendum to the alpha control).
The Phase-2 verdict is issued at the DECLARED pre-angular scope. This addendum answers the
one obvious follow-up honestly, in both directions: does the breaking survive the exact
angular average, or is it pre-angular-only?  M1's angular content sits entirely in the
sector sums A+_N, A-_N (n-hat polynomials); their moment() averages decide it.
Read-only. No verdict change at declared scope. W-0.
"""
import hashlib, json, os, subprocess, sys, time
import sympy as sp
from collections import defaultdict
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
CHECKS,FAILURES=[],[]
def gate(c,l):
    CHECKS.append((bool(c),l))
    if not c: FAILURES.append(l)
    print(("  PASS  " if c else "  FAIL  ")+l, flush=True)
t0=time.time()
src=open(os.path.join(HERE,"wall_kr_tier3_loop.py"),encoding="utf-8").read()
M={"__name__":"frozen_t3","__file__":os.path.join(HERE,"wall_kr_tier3_loop.py")}
argv0=sys.argv; sys.argv=["x","machinery_only"]; os.chdir(HERE)
try: exec(compile(src,"t3","exec"),M)
except SystemExit: pass
sys.argv=argv0
CM,cdecomp,moment,Ptt,htrunc=M["CM"],M["cdecomp"],M["moment"],M["Ptt"],M["htrunc"]
H,u,up,om,q=M["H"],M["u"],M["up"],M["om"],M["q"]
n1,n2,n3=M["n1"],M["n2"],M["n3"]; PAIRS=M["PAIRS"]; dsym=M["dsym"]
qsub={}
for i_,tgt in ((1,n1),(2,n2),(3,n3)):
    qsub[sp.Symbol("q%d"%i_)]=q*tgt
    qsub[sp.Symbol("q%d"%i_,real=True)]=q*tgt
def ang(expr):
    """exact angular average of an n-polynomial via the frozen moment()"""
    expr=sp.expand(expr); out=sp.Integer(0)
    for t in sp.Add.make_args(expr):
        pows=[sp.degree(t,v) if t.has(v) else 0 for v in (n1,n2,n3)]
        c=t
        for v,p in zip((n1,n2,n3),pows): c=c/v**p
        out+=c*moment(tuple(pows))
    return sp.expand(out)
OUT={}
for config in ("plus_z","cross_z","plus_x"):
    Cs={ck:sp.sympify(vv).subs(H,0) for ck,vv in CM[config].items()}
    D1,D2={},{}
    for ck,vv in Cs.items():
        if vv==0: continue
        D1[ck]=cdecomp(htrunc(sp.expand(vv.xreplace(qsub))))
        v2=vv.xreplace(qsub).xreplace({q:-q}).subs(om,-om).subs(u,up)
        D2[ck]=cdecomp(htrunc(sp.expand(v2)))
    P_line={}
    for (a,b) in PAIRS:
        for (ap,bp) in PAIRS: P_line[((a,b),(ap,bp))]=Ptt(a,b,ap,bp)
    Ap=defaultdict(lambda: sp.Integer(0)); Am=defaultdict(lambda: sp.Integer(0))
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
                            (e_,f_),(g_,h_)=nu1m,nu2m
                            vk=sp.expand(c1*c2*PP*(n1**(nm1[0]+nm2[0]))
                                 *(n2**(nm1[1]+nm2[1]))*(n3**(nm1[2]+nm2[2])))
                            N_=e_+f_+g_+h_
                            Ap[N_]+=sp.expand(vk*((-1)**e_+(-1)**f_))
                            Am[N_]+=sp.expand(vk*(-1)**(e_+f_)*((-1)**g_+(-1)**h_))
    apz={N_:sp.simplify(ang(Ap[N_]))==0 for N_ in sorted(Ap)}
    amz={N_:sp.simplify(ang(Am[N_]))==0 for N_ in sorted(Am)}
    OUT[config]={"postang_Aplus_zero":{str(a):bool(b) for a,b in apz.items()},
                 "postang_Aminus_zero":{str(a):bool(b) for a,b in amz.items()}}
    surv=all(apz.values()) and all(amz.values())
    OUT[config]["breaking_survives_angular_average"]=not surv
    print("  RESULT [%s]: post-angular <A+_N> zero: %s ; <A-_N> zero: %s => breaking %s "
          "the exact angular average   [%.0fs]"
          %(config,apz,amz,"DOES NOT SURVIVE" if surv else "SURVIVES",time.time()-t0),
          flush=True)
allsame=len({o["breaking_survives_angular_average"] for o in OUT.values()})==1
gate(allsame,"post-angular conclusion is uniform across the three TT configurations")
n=sum(1 for ok,_ in CHECKS if ok)
res={"instrument":"wall_kr_h1_phase2_postang_note.py","date":"2026-09-03",
 "kind":"gated addendum: does the Phase-2 breaking survive the exact angular average?",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,"per_config":OUT,
 "scope_note":"the Phase-2 verdict is issued at the declared PRE-ANGULAR scope; this "
   "addendum only reports the post-angular fate of the breaking term",
 "W":"W-0"}
json.dump(res,open(os.path.join(HERE,"WALL_KR_H1_PHASE2_POSTANG_NOTE.json"),"w",
          encoding="utf-8"),indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_H1_PHASE2_POSTANG_NOTE.json")
print("POSTANG_DONE")
