#!/usr/bin/env python3
"""
H1 PHASE 3 — d=3 POST-ANGULAR NOTE (gated addendum, adopted from adversarial Leg B).
The Phase-3 post-angular gate certifies <Sigma0> != 0 at SYMBOLIC d; in principle a
symbolic-d nonzero could still vanish at the physical dimension. This addendum gates
<Sigma0> != 0 both at symbolic d AND at d=3, per configuration, exact-symbolic.
Read-only. W-0.
"""
import hashlib, json, os, subprocess, sys, time
import sympy as sp
from collections import defaultdict
HERE=os.path.dirname(os.path.abspath(__file__))
CHECKS,FAILURES=[],[]
def gate(c,l):
    CHECKS.append((bool(c),l))
    if not c: FAILURES.append(l)
    print(("  PASS  " if c else "  FAIL  ")+l, flush=True)
t0=time.time()
def phase_classes(e):
    classes={}
    for t in sp.Add.make_args(sp.expand(e)):
        num,den=t.as_numer_denom()
        karg=sp.Integer(0); co_n=[]
        for f in sp.Mul.make_args(num):
            if isinstance(f,sp.exp): karg+=f.args[0]
            elif f.is_Pow and isinstance(f.base,sp.exp): karg+=f.exp*f.base.args[0]
            else:
                assert not f.atoms(sp.exp),"exp in numerator non-exp factor: %s"%f
                co_n.append(f)
        if den.atoms(sp.exp):
            dcls=phase_classes(den)
            assert len(dcls)==1,"multi-phase denominator: %s"%den
            (kd,cd),=dcls.items()
            karg-=kd; den=cd
        key=sp.expand(karg)
        classes[key]=classes.get(key,sp.Integer(0))+sp.Mul(*co_n)/den
    return classes
src=open(os.path.join(HERE,"wall_kr_tier3_loop.py"),encoding="utf-8").read()
M={"__name__":"frozen_t3","__file__":os.path.join(HERE,"wall_kr_tier3_loop.py")}
argv0=sys.argv; sys.argv=["x","machinery_only"]; os.chdir(HERE)
try: exec(compile(src,"t3","exec"),M)
except SystemExit: pass
sys.argv=argv0
CM,cdecomp,moment,Ptt,htrunc=M["CM"],M["cdecomp"],M["moment"],M["Ptt"],M["htrunc"]
H,u,up,om,q,kap=M["H"],M["u"],M["up"],M["om"],M["q"],M["kap"]
n1,n2,n3=M["n1"],M["n2"],M["n3"]; PAIRS=M["PAIRS"]; dsym=M["dsym"]
Wf=(kap**2/q)*sp.exp(-sp.I*q*(u-up))
def wop(e,a,c):
    for _ in range(a): e=-sp.I*sp.diff(e,u)
    for _ in range(c): e=-sp.I*sp.diff(e,up)
    return sp.expand(e)
def flat_line(a,c): return sp.expand(wop(Wf,a,c))
pref=sp.Rational(1,2)/(2*kap**2)**2
qsub={}
for i_,tgt in ((1,n1),(2,n2),(3,n3)):
    qsub[sp.Symbol("q%d"%i_)]=q*tgt
    qsub[sp.Symbol("q%d"%i_,real=True)]=q*tgt
def ang(expr):
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
    Sig0=sp.Integer(0)
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
                    pab=sp.Poly(sp.expand(PA*PB),n1,n2,n3)
                    PABL=list(zip(pab.monoms(),pab.coeffs()))
                    for (nm1,nu1m),c1 in D1[k1].items():
                        for (nm2,nu2m),c2 in D2[k2].items():
                            npart=(nm1[0]+nm2[0],nm1[1]+nm2[1],nm1[2]+nm2[2])
                            afp=sum(cP*(n1**(npart[0]+mP[0]))*(n2**(npart[1]+mP[1]))
                                    *(n3**(npart[2]+mP[2])) for mP,cP in PABL)
                            if afp!=0:
                                (e_,f_),(g_,h_)=nu1m,nu2m
                                Sig0+=sp.expand(c1*c2*afp*pref
                                     *flat_line(e_,g_)*flat_line(f_,h_))
    cls={kcl:ang(v) for kcl,v in phase_classes(Sig0).items()}
    nz_sym=[v for v in cls.values() if sp.cancel(sp.together(v))!=0]
    nz_d3=[v for v in nz_sym if sp.cancel(sp.together(v.subs(dsym,3)))!=0]
    gate(len(nz_sym)>0 and len(nz_d3)>0,
         "[%s] <Sigma0> != 0 at SYMBOLIC d AND at d=3 (exact) — the Phase-3 breaking "
         "survives the angular average at the physical dimension; no hidden (d-3) factor"
         "   [%.0fs]"%(config,time.time()-t0))
    OUT[config]={"postang_nonzero_symbolic_d":len(nz_sym)>0,
                 "postang_nonzero_d3":len(nz_d3)>0}
n=sum(1 for ok,_ in CHECKS if ok)
res={"instrument":"wall_kr_h1_phase3_d3_note.py","date":"2026-09-03",
 "kind":"gated addendum (adopted from adversarial Leg B): <Sigma0> nonzero at d=3",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,"per_config":OUT,"W":"W-0"}
json.dump(res,open(os.path.join(HERE,"WALL_KR_H1_PHASE3_D3_NOTE.json"),"w",
          encoding="utf-8"),indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_H1_PHASE3_D3_NOTE.json")
print("D3_DONE")
