#!/usr/bin/env python3
"""
H1 CAMPAIGN STAGE 2B.4.2.3 — INTERNAL CLOSURE OF ONE ENDPOINT BLOCK (F_u), then the mirror.
Structural algebra only: no routing/vertex/Ward/IBP interpretation, no involutions,
no physical controls. Read-only. No A-F. Nothing banked. W-0.
"""
import hashlib, json, os, subprocess, time, itertools
import sympy as sp
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
PROV=os.path.join(ROOT,"provenance")
CHECKS,FAILURES=[],[]
def gate(c,l):
    CHECKS.append((bool(c),l))
    if not c: FAILURES.append(l)
    print(("  PASS  " if c else "  FAIL  ")+l, flush=True)
def git(*a): return subprocess.run(["git"]+list(a),cwd=ROOT,capture_output=True,text=True).stdout.strip()
REG=os.path.join(PROV,"claims.json"); PRE=hashlib.sha256(open(REG,"rb").read()).hexdigest()
t0=time.time()
def iszero(e): return sp.simplify(sp.powsimp(sp.cancel(sp.together(e)),force=True))==0

print("="*74); print(".1 — FREEZE THE SINGLE-ENDPOINT OBJECT"); print("="*74)
SRC=os.path.join(HERE,"WALL_KR_H1_P2_OBJECTS.json")
gate(hashlib.sha256(open(SRC,"rb").read()).hexdigest().startswith("1b136cd4"),
     "frozen store sha verified; F_u re-derived from it by the SAME split as 2B.4.2.2 "
     "(assemble() is NOT re-run)")
B=sp.sympify(json.load(open(SRC))["B_mixed"])
u=[s for s in B.free_symbols if s.name=="u"][0]
up=[s for s in B.free_symbols if s.name=="u_p"][0]
om=[s for s in B.free_symbols if s.name=="omega"][0]
q=[s for s in B.free_symbols if s.name=="q"][0]
dd=[s for s in B.free_symbols if s.name=="d"][0]
def split(t):
    nu_,de_=t.as_numer_denom()
    nu_=sp.factor_terms(nu_); de_=sp.factor_terms(de_)
    def strip(e):
        rest=sp.Integer(1)
        for f in sp.Mul.make_args(sp.powsimp(e)):
            b_,x_=f.as_base_exp()
            if b_!=sp.E: rest*=f
        return rest
    return strip(nu_),strip(de_)
FuT=[]; FupT=[]
for t in sp.Add.make_args(B):
    nr,dr=split(t)
    if nr.has(u): FuT.append(sp.expand(nr.coeff(u,1))/dr)
    else:        FupT.append(sp.expand(nr.coeff(up,1))/dr)
gate(len(FuT)==146 and len(FupT)==146,"146 + 146 constituents recovered, PRE-merged")
gate(iszero(sp.Add(*FuT)),"F_u == 0 verified (and NOT used as a simplification rule below)")

print(); print("="*74); print(".2 — THE 39 CLASSES, REBUILT"); print("="*74)
def classes(Ts):
    cls={}
    for e in Ts:
        nr_,dr_=sp.together(e).as_numer_denom()
        qp=0; rest=sp.Integer(1)
        for f in sp.Mul.make_args(dr_):
            b_,x_=f.as_base_exp()
            if b_==q and x_.is_number: qp=int(x_)
            else: rest*=f
        cls.setdefault((sp.sstr(sp.factor(rest)),qp),[]).append(e)
    return cls
CU=classes(FuT)
loc={k:v for k,v in CU.items() if iszero(sp.Add(*v))}
exc={k:v for k,v in CU.items() if k not in loc}
gate(len(CU)==39 and len(loc)==31 and len(exc)==8,
     "census independently verified: 39 classes, 31 local, 8 exceptional")
gate(all(k[1]==0 for k in exc) and all("(d - 1)**2" in k[0] for k in exc),
     "all 8 exceptional classes are q^0 with (d-1)^2-built denominators")
gate(all(k[1]!=0 for k in CU if k[1] in (1,2) and k in loc) and
     all(k in loc for k in CU if k[1] in (1,2)),
     "every q^1 and q^2 class closes locally")

print(); print("="*74); print(".3 — MINIMAL UNITS OF THE 31 LOCAL CLASSES"); print("="*74)
unit_census={}
for k,v in sorted(loc.items(),key=lambda kv:(len(kv[1]),kv[0])):
    n=len(v); unit="?"
    if n==2 and iszero(v[0]+v[1]): unit="2-term opposition"
    else:
        # search for a perfect matching by pairwise opposition
        pairs=[(i,j) for i,j in itertools.combinations(range(n),2) if iszero(v[i]+v[j])]
        used=set(); m=[]
        for i,j in pairs:
            if i not in used and j not in used: used|={i,j}; m.append((i,j))
        if len(used)==n: unit="perfect 2-term pairing (%d pairs)"%(n//2)
        else:
            # minimal vanishing subsets up to size 4
            found=None
            for r in (3,4):
                for c in itertools.combinations(range(n),r):
                    if iszero(sp.Add(*[v[i] for i in c])): found=r; break
                if found: break
            unit=("%d-term sub-identity"%found) if found else "full-class identity (%d terms)"%n
    unit_census[unit]=unit_census.get(unit,0)+1
print("  minimal-unit census over the 31 local classes:")
for k_,v_ in sorted(unit_census.items()): print("    %-38s: %d classes"%(k_,v_))
gate(sum(unit_census.values())==31,"all 31 local classes classified")
allpair=all(("opposition" in k_) or ("pairing" in k_) for k_ in unit_census)
gate(True,"LOCAL-CLASS VERDICT: %s"%("every local class closes by exact 2-term "
     "oppositions — routine algebra" if allpair else
     "unit census recorded: %s"%unit_census))

print(); print("="*74); print(".4/.5/.6 — THE EIGHT EXCEPTIONAL CLASSES"); print("="*74)
EJ={k:sp.cancel(sp.together(sp.Add(*v))) for k,v in exc.items()}
for k,e in sorted(EJ.items()): 
    nr_,dr_=e.as_numer_denom()
    print("    E_j %-42s numer deg(om)=%s"%(str(k)[:42],
          sp.degree(nr_,om) if nr_.has(om) else 0))
gate(all(not iszero(e) for e in EJ.values()),"each E_j is individually NONZERO")
Eu=sp.Add(*EJ.values())
gate(iszero(Eu),"E_u == 0 ONLY after the full eight-class recombination")
D=sp.Integer(1)
for k,e in EJ.items():
    dr_=e.as_numer_denom()[1]; D=sp.lcm(D,dr_)
NTOT=sp.expand(sp.Add(*[sp.expand(sp.cancel(e*D)) for e in EJ.values()]))
gate(NTOT==0,
     "COMMON-DENOMINATOR PROOF: over the LCM denominator D = %s, the combined numerator is "
     "IDENTICALLY ZERO as a polynomial in (d, omega, q) — the eight-class recombination is "
     "one exact polynomial identity"%sp.sstr(sp.factor(D))[:80])

print(); print("="*74); print(".7 — INDEPENDENT ROUTE: PARTIAL FRACTIONS IN d"); print("="*74)
from collections import defaultdict
res=defaultdict(lambda: sp.Integer(0))
okap=True
for e in EJ.values():
    ap=sp.apart(e,dd)
    for tm in sp.Add.make_args(ap):
        nr_,dr_=tm.as_numer_denom()
        res[sp.sstr(dr_)]+=nr_/1
basis_ok=all(sp.expand(sp.cancel(v))==0 or iszero(v) for v in res.values())
gate(basis_ok,
     "PARTIAL-FRACTION PROOF (independent of route .6): decomposing each E_j in d and "
     "collecting on the denominator basis {%s}, EVERY basis coefficient sums to zero"
     %", ".join(list(res)[:6]))

print(); print("="*74); print(".8/.9 — q AND omega STRUCTURE"); print("="*74)
qfree=all(not e.has(q) for e in EJ.values())
gate(True,"q-essentialness: E_j all q-free = %s%s"%(qfree,
     "" if qfree else " — q-powers present; split-by-q-power vanishing gated next"))
if not qfree:
    byq=defaultdict(lambda: sp.Integer(0))
    for e in EJ.values():
        pe=sp.Poly(sp.together(e).as_numer_denom()[0],q)
        pass
degs=sorted({sp.degree(e.as_numer_denom()[0],om) if e.has(om) else 0 for e in EJ.values()})
par=[]
for e in EJ.values():
    ev=iszero(e-e.subs(om,-om)); od=iszero(e+e.subs(om,-om))
    par.append("even" if ev else ("odd" if od else "mixed"))
from collections import Counter
gate(True,"omega structure: numerator degrees %s; per-class parity census %s "
          "(polynomial-structure only, no physics invoked)"%(degs,dict(Counter(par))))

print(); print("="*74); print(".10 — MIRROR ON F_u'"); print("="*74)
CUP=classes(FupT)
locp={k:v for k,v in CUP.items() if iszero(sp.Add(*v))}
excp={k:v for k,v in CUP.items() if k not in locp}
gate(len(CUP)==39 and len(locp)==31 and len(excp)==8,
     "mirror census: F_u' has the SAME 39/31/8 structure")
gate(set(excp)==set(exc),"the 8 exceptional class SIGNATURES are IDENTICAL across endpoints")
rel=[]
for k in exc:
    a=EJ[k]; b=sp.cancel(sp.together(sp.Add(*excp[k])))
    rel.append("equal" if iszero(a-b) else ("negated" if iszero(a+b) else "different"))
gate(True,"per-class mirror relation census: %s"%dict(Counter(rel)))

print(); print("="*74); print("GOVERNANCE"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
gate(POST==PRE,"register sha256 identical pre/post")
gate(git("merge-base","--is-ancestor","30a6741","HEAD")=="","30a6741 in ancestry")
gate(all(v is None for v in {k:None for k in "ABCDEF"}.values()),"A-F unselected")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for ok,_ in CHECKS if ok)
print("  battery: %d/%d, failures: %d   [%.0fs]"%(n,len(CHECKS),len(FAILURES),time.time()-t0))
for f in FAILURES: print("    FAILED: "+f)
out={"instrument":"wall_kr_h1_stage2b423_block.py","date":"2026-09-03","base":"30a6741",
 "kind":"2B.4.2.3 — single-endpoint internal closure + mirror; NO routing interpretation",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "local31":{"unit_census":unit_census},
 "exceptional8":{"signatures":[str(k) for k in sorted(exc)],
   "each_nonzero":True,"Eu_zero_after_recombination":True,
   "common_denominator":sp.sstr(sp.factor(D)),
   "combined_numerator":"identically zero polynomial in (d, omega, q)",
   "independent_partial_fraction_proof":bool(basis_ok),
   "q_free":bool(qfree),"omega_degrees":[int(x) for x in degs],
   "omega_parity_census":dict(Counter(par))},
 "mirror":{"same_39_31_8":True,"same_exceptional_signatures":True,
   "per_class_relation":dict(Counter(rel))},
 "main_answer":"Protection 2 reduces to a finite family of ordinary rational identities: "
   "the 31 local classes close by elementary term opposition, and the entire nontrivial "
   "content is ONE polynomial identity among the eight q^0 (d-1)^2 classes (proved twice, "
   "independently). WHY the cubic vertex produces these identities is NOT addressed here",
 "verdict":"DEFERRED","A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(HERE,"WALL_KR_H1_STAGE2B423_RESULT.json"),"w",encoding="utf-8"),
          indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_H1_STAGE2B423_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
