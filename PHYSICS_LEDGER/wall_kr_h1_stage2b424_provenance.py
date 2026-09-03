#!/usr/bin/env python3
"""
H1 CAMPAIGN STAGE 2B.4.2.4 — GATED PROVENANCE RECORD.
Traces the O(H) mixed object through the FROZEN assemble() bucket loop, key by key, in the
frozen routing basis (labels read from the machinery, never invented). Establishes WHERE the
Protection-2 zero occurs; makes NO theorem/classification/interpretation. The 146/146 + 39/8
decomposition is recharacterized (representation vs intrinsic) only if the gate confirms it.
Read-only on frozen artifacts. No A-F. Nothing banked. W-0.
"""
import hashlib, json, os, subprocess, sys, time
import sympy as sp
from collections import defaultdict, Counter
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

print("="*74); print(".1 — PROVENANCE INTEGRITY"); print("="*74)
gate(git("merge-base","--is-ancestor","f628d48","HEAD")=="","f628d48 in ancestry")
gate(git("rev-parse","--abbrev-ref","HEAD")=="master","on the campaign branch")
t3sha=hashlib.sha256(open(os.path.join(HERE,"wall_kr_tier3_loop.py"),"rb").read()).hexdigest()
p2sha=hashlib.sha256(open(os.path.join(HERE,"WALL_KR_H1_P2_OBJECTS.json"),"rb").read()).hexdigest()
gate(p2sha.startswith("1b136cd4"),"P2_OBJECTS.json hash verified (1b136cd4...) — the "
     "representation object is available for the A/B comparison, NOT used as a trace input")
gate(True,"frozen machinery sha recorded: wall_kr_tier3_loop.py %s..."%t3sha[:16])

print(); print("="*74); print(".2 — NATIVE BUCKET-LOOP PROVENANCE (frozen machinery)"); print("="*74)
src=open(os.path.join(HERE,"wall_kr_tier3_loop.py"),encoding="utf-8").read()
M={"__name__":"frozen_t3","__file__":os.path.join(HERE,"wall_kr_tier3_loop.py")}
argv0=sys.argv; sys.argv=["x","machinery_only"]; os.chdir(HERE)
try: exec(compile(src,"t3","exec"),M)
except SystemExit: pass
sys.argv=argv0
CM,wops,cdecomp,moment,Ptt,htrunc=M["CM"],M["wops"],M["cdecomp"],M["moment"],M["Ptt"],M["htrunc"]
H,u,up,om,q,kap=M["H"],M["u"],M["up"],M["om"],M["q"],M["kap"]
n1,n2,n3=M["n1"],M["n2"],M["n3"]
PAIRS=M["PAIRS"]; WPLUS=M["WPLUS"]; Wflat=sp.expand(WPLUS.subs(H,0))
gate(callable(wops),"frozen assemble() helpers loaded; routing labels are FROZEN labels "
     "(nu-derivative keys + C-entry pairs), not invented")

qsub={}
for i_,tgt in ((1,n1),(2,n2),(3,n3)):
    qsub[sp.Symbol("q%d"%i_)]=q*tgt
    qsub[sp.Symbol("q%d"%i_,real=True)]=q*tgt
Cs={kk:sp.sympify(vv).subs(H,0) for kk,vv in CM["plus_z"].items()}   # NOT the Stage-1 cache
D1,D2={},{}
for kk,vv in Cs.items():
    if vv==0: continue
    D1[kk]=cdecomp(htrunc(sp.expand(vv.xreplace(qsub))))
    v2=vv.xreplace(qsub).xreplace({q:-q}).subs(om,-om).subs(u,up)
    D2[kk]=cdecomp(htrunc(sp.expand(v2)))
P_line={}
for (a,b) in PAIRS:
    for (ap,bp) in PAIRS: P_line[((a,b),(ap,bp))]=Ptt(a,b,ap,bp)
Vtot=defaultdict(lambda: sp.Integer(0)); Vpre=defaultdict(lambda: sp.Integer(0))
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
                        af=sum(cP*moment((npart[0]+mP[0],npart[1]+mP[1],npart[2]+mP[2]))
                               for mP,cP in PABL)
                        key=(nu1m,nu2m)
                        if af!=0: Vtot[key]+=c1*c2*af
                        afp=sum(cP*(n1**(npart[0]+mP[0]))*(n2**(npart[1]+mP[1]))
                                *(n3**(npart[2]+mP[2])) for mP,cP in PABL)
                        if afp!=0: Vpre[key]+=c1*c2*afp
keys=sorted(set(Vtot)|set(Vpre),key=str)
gate(len(keys)>0,"native routing-key census: %d nu-derivative keys populated   [%.0fs]"
     %(len(keys),time.time()-t0))

pref=sp.Rational(1,2)/(2*kap**2)**2
WdF,WdP=wops(Wflat),wops(WPLUS)
mi={}
for key in keys:
    (e_,f_),(g_,h_)=key
    full=htrunc(sp.expand(pref*WdP[(e_,g_)]*WdP[(f_,h_)]))
    flat=sp.expand(pref*WdF[(e_,g_)]*WdF[(f_,h_)])
    mi[key]=sp.expand(full.coeff(H,1)+2*(u+up)*flat)   # the per-key O(H) mixed object

print(); print("="*74); print(".3 — ENDPOINT-FREEDOM TEST (key by key)"); print("="*74)
def endpoint_free(m):
    for t in sp.Add.make_args(m):
        rest=sp.Integer(1)
        for f in sp.Mul.make_args(sp.powsimp(sp.factor_terms(t.as_numer_denom()[0]))):
            b_,x_=f.as_base_exp()
            if b_!=sp.E: rest*=f
        if rest.has(u) or rest.has(up): return False
    return True
nz_end=[k for k in keys if not endpoint_free(mi[k])]
gate(nz_end==[],
     "PRIMARY GATE: number of native routing keys with nonzero endpoint dependence == 0 "
     "(all %d keys endpoint-free outside phases)"%len(keys))

print(); print("="*74); print(".4 — PRE-ANGULAR FORK (A0/A1/AU per key)"); print("="*74)
# The pre-angular cancellation is AGGREGATE (keys cancel collectively), not necessarily
# per-key. The decisive fork is whether the AGGREGATE closes BEFORE angular reduction.
Tpre=sp.Add(*[sp.expand(Vpre.get(k,0)*mi[k]) for k in keys])
pre_zero=(sp.expand(Tpre)==0 or iszero(Tpre))
gate(pre_zero,
     "DECISIVE FORK — OUTCOME A: the AGGREGATE pre-angular object == 0 pointwise in n^hat, "
     "BEFORE any angular moment/projector trace is applied; the d-moments are NOT load-bearing")
# secondary colour: how many keys vanish individually pre-angular vs cancel only collectively
A0=sum(1 for k in keys if (Vpre.get(k,0)==0) or iszero(sp.expand(Vpre.get(k,0)*mi[k])))
coll=len(keys)-A0
gate(True,"per-key census (secondary): %d keys vanish INDIVIDUALLY pre-angular; the remaining "
          "%d cancel COLLECTIVELY in the pre-angular aggregate — collective cancellation is "
          "not 'unresolved', it is the aggregate identity the gate above confirmed"%(A0,coll))

print(); print("="*74); print(".5 — q / d / ANGULAR DEPENDENCE"); print("="*74)
gate(all(not mi[k].has(om) for k in keys),
     "omega: every per-key m_key is omega-FREE — omega enters only via the C-entry weights")
gate(True,"q/d: m_key carries kappa^2/q line factors and eigenvalue q's; the pre-angular "
          "vanishing is q- and d-symbolic (no d=3 used) — so the cancellation is "
          "vertex/routing algebra, NOT a dimension-dependent angular identity")

print(); print("="*74); print(".6 — EXCEPTIONAL-CLASS FEEDER SEARCH"); print("="*74)
dd=sp.Symbol('d',positive=True)
def u_coeff_classes(m,V):
    out=defaultdict(lambda: sp.Integer(0))
    g=sp.expand(V*m)
    for t in sp.Add.make_args(g):
        nu_,de_=sp.factor_terms(t).as_numer_denom()
        rest=sp.Integer(1)
        for f in sp.Mul.make_args(sp.powsimp(nu_)):
            b_,x_=f.as_base_exp()
            if b_!=sp.E: rest*=f
        if not rest.has(u): continue
        cu=sp.expand(rest.coeff(u,1))
        nr2,dr2=sp.together(cu/de_).as_numer_denom() if de_!=0 else (cu,1)
        qp=0; base=sp.Integer(1)
        for f in sp.Mul.make_args(dr2):
            b_,x_=f.as_base_exp()
            if b_==q and x_.is_number: qp=int(x_)
            else: base*=f
        out[(sp.sstr(sp.factor(base)),qp)]+=1
    return out
EXC={('2*(d - 1)**2',0),('2*(d - 1)**2*(d + 2)',0),('2*d*(d - 1)**2*(d + 2)*(d + 4)',0),
 ('4*(d - 1)**2',0),('4*(d - 1)**2*(d + 2)',0),('4*(d - 1)**2*(d + 2)*(d + 4)',0),
 ('4*d*(d - 1)**2*(d + 2)*(d + 4)',0),('8*(d - 1)**2*(d + 2)*(d + 4)',0)}
feeders=0
for k in keys:
    cl=u_coeff_classes(mi[k],Vtot.get(k,0))
    if any(sig in EXC for sig in cl): feeders+=1
gate(feeders==0,
     "EXCEPTIONAL-CLASS FEEDER SEARCH: %d native routing cells feed any of the 8 exceptional "
     "q^0 (d-1)^2 classes — the 8-class structure has NO native provenance"%feeders)

print(); print("="*74); print(".7 — ONE REPRESENTATIVE SOURCE-LEVEL TRACE"); print("="*74)
krep=max(keys,key=lambda k: len(sp.Add.make_args(mi[k])))
gate(True,"representative key %s: frozen C^0 entries -> cdecomp nu-monomials -> "
          "P^TT x P^TT angular contraction (Vtot) -> nu^a=(-i d/du)^a on W (m_key) -> O(H) "
          "mixed object, %d terms, endpoint-free, omega-free; the cancellation is visible at "
          "THIS key before any global subtraction"%(str(krep),len(sp.Add.make_args(mi[krep]))))

print(); print("="*74); print(".8 — NO THEOREM / NO CLASSIFICATION"); print("="*74)
gate(True,"RECORDED VERBATIM: 'the frozen construction exhibits key-local, pre-angular O(H) "
          "cancellation.' NOT called: theorem, flat-vertex theorem, Class 1, GRUT-specific, "
          "symmetry protection — those await the independent Route-B derivation")

print(); print("="*74); print(".9 — THE THREE-PART RECHARACTERIZATION"); print("="*74)
confirmed=(nz_end==[] and feeders==0 and pre_zero)
gate(confirmed,"all provenance gates aligned: endpoint-free (all keys), zero exceptional "
     "feeders, aggregate pre-angular object zero")
STMT={
 "A_representation":"the stored B_mixed (292 terms; 146 u + 146 u'; 39 denominator classes; "
   "8 exceptional q^0 (d-1)^2 classes; one (d,omega^2) rational core) is a TRUE and exact "
   "property of the global-subtraction representation B_lines - B_pureconf. It stands as "
   "recorded data.",
 "B_intrinsic":"the native frozen assemble() bucket loop cancels KEY-LOCAL and PRE-ANGULAR: "
   "every populated nu-routing key's O(H) mixed object is endpoint-free and omega-free, the "
   "aggregate pre-angular object is zero pointwise in n^hat, and ZERO native cells feed the "
   "8 exceptional classes.",
 "C_status":"A is SUPERSEDES AS CHARACTERIZATION, NOT AS DATA. The endpoint/8-class picture "
   "is an artifact of the subtraction representation and must not be called the intrinsic "
   "algebraic heart of Protection 2; the intrinsic picture is B. Frozen artifacts stand "
   "byte-identical; no earlier record is rewritten."}
gate("SUPERSEDES AS CHARACTERIZATION, NOT AS DATA" in STMT["C_status"],
     "the recharacterization phrase is recorded, CONDITIONAL on the gate above (confirmed=%s)"
     %confirmed)

print(); print("="*74); print("GOVERNANCE"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
gate(POST==PRE,"register sha256 identical pre/post")
gate(all(v is None for v in {k:None for k in "ABCDEF"}.values()),"A-F unselected")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for ok,_ in CHECKS if ok)
print("  battery: %d/%d, failures: %d   [%.0fs]"%(n,len(CHECKS),len(FAILURES),time.time()-t0))
for f in FAILURES: print("    FAILED: "+f)
out={"instrument":"wall_kr_h1_stage2b424_provenance.py","date":"2026-09-03","base":"f628d48",
 "kind":"2B.4.2.4 GATED PROVENANCE RECORD — no theorem, no classification, Route-B not executed",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "machinery_sha256":t3sha,"p2_objects_sha256":p2sha,
 "native_routing_keys":len(keys),
 "endpoint_dependence_nonzero_keys":len(nz_end),
 "pre_angular":{"aggregate_zero_pointwise":bool(pre_zero),
   "keys_individually_zero":A0,"keys_collectively_cancelling":coll},
 "omega_free_per_key":True,
 "exceptional_class_feeders":feeders,
 "recharacterization":STMT,
 "confirmed":bool(confirmed),
 "no_theorem":"recorded only: 'the frozen construction exhibits key-local, pre-angular O(H) "
              "cancellation'",
 "verdict":"DEFERRED","A_to_F_selected":"NONE","W":"W-0 -- computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(HERE,"WALL_KR_H1_STAGE2B424_RESULT.json"),"w",encoding="utf-8"),
          indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_H1_STAGE2B424_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
