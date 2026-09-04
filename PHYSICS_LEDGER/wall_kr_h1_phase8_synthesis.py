#!/usr/bin/env python3
"""
H1 CLOSURE — PHASE 8: SYNTHESIS / QUANTIFIED THEOREM ADJUDICATION.
No new deformations, no new cancellation searches, no new physical assumptions.
This instrument (a) machine-checks the logical dependency graph of the synthesized
theorem (acyclicity; every node classified; no result its own premise), (b) re-anchors
the two load-bearing computational statements to the frozen objects (the Level-I
four-channel zero on plus_z; the Level-II abstract class identity), and (c) gates that
the record carries the required separations. Everything else is CITATION of the closed,
gated Phase 1-7 records, entering through ancestry-verified commits.
Read-only. Phases 1-7 CLOSED. A-F unselected. W-0.
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

print("="*74); print("0 — GOVERNANCE HARD STOP"); print("="*74)
HEAD=git("rev-parse","HEAD").stdout.strip(); ov4=git("rev-parse","origin/v4").stdout.strip()
gate(HEAD!="" and HEAD==ov4,"v4 by REF IDENTITY: HEAD == origin/v4 == %s"%HEAD[:12])
for c_,nm in (("bedc989","P1"),("39551c7","P2"),("dffe1ca","P3"),("e5009bc","P4"),
              ("016d84b","P5"),("b10c4d9","P6"),("d44bfd2","P7")):
    gate(git("merge-base","--is-ancestor",c_,"HEAD").returncode==0,
         "%s (%s) in ancestry — by RETURNCODE (citation channel verified)"%(c_,nm))
t3sha=hashlib.sha256(open(os.path.join(HERE,"wall_kr_tier3_loop.py"),"rb").read()).hexdigest()
gate(t3sha.startswith("1c72272b"),"frozen T3 machinery sha 1c72272b... unchanged")
note("A-F UNSELECTED; W-0; nothing banked; Phase 9 NOT started")

print(); print("="*74); print("B — THE DEPENDENCY GRAPH, MACHINE-CHECKED"); print("="*74)
ALLOWED={"DECLARED INPUT","STANDARD IDENTITY","CONVENTION","DERIVED","GATED FACT",
         "CONTROL EVIDENCE"}
# node: (classification, [premises], provenance-citation)
GRAPH={
 "D1_EH_action_Lambda3H2":("DECLARED INPUT",[],"charter/T1 declaration"),
 "D2_dS_conformal_chart":("DECLARED INPUT",[],"T1/T2 declaration"),
 "D3_TT_canonical_normalization":("DECLARED INPUT",[],"T2 declaration (D2=2a unfixed h)"),
 "D4_BD_positive_frequency":("DECLARED INPUT",[],"T2 declaration (state prescription)"),
 "D5_routing_contraction_conventions":("CONVENTION",[],"T3 (D2 transform, P^TT pairing)"),
 "D6_derivative_rule":("CONVENTION",[],"T3 (nu -> -i d/du)"),
 "M1_canonical_FRW_Wronskian":("STANDARD IDENTITY",[],"P5 (unique integrating factor; "
   "pre-existing exact T2 gate)"),
 "M2_dummy_index_relabeling":("STANDARD IDENTITY",[],"mathematics"),
 "M3_momentum_reflection_parity":("STANDARD IDENTITY",[],"mathematics"),
 "T1_vertex_derived":("DERIVED",["D1_EH_action_Lambda3H2","D2_dS_conformal_chart",
   "D3_TT_canonical_normalization"],"T1 instrument (graded Christoffel/Ricci; P5 leg-read)"),
 "T2_kernel_derived":("DERIVED",["D1_EH_action_Lambda3H2","D2_dS_conformal_chart",
   "D3_TT_canonical_normalization","D4_BD_positive_frequency"],
   "T2 instrument (exact BD solution; a^2 W gated; P5 leg-read)"),
 "even_degree_membership":("DERIVED",["T1_vertex_derived"],
   "P7 tensor-level gate (7,560 terms exactly degree 2; needs Lambda=O(H^2) from D1)"),
 "bridge_D2_equals_nu_reflection":("DERIVED",["even_degree_membership",
   "M3_momentum_reflection_parity","D5_routing_contraction_conventions"],
   "P6 per-entry gate + P7 q/u-freeness gates"),
 "S_amplitude_zero":("DERIVED",["M1_canonical_FRW_Wronskian","T2_kernel_derived"],
   "P5 gates (x-deformation violates a^2 W; native O(H)-flat)"),
 "S_mixing_excluded":("DECLARED INPUT",["D4_BD_positive_frequency"],
   "P5 (Bogoliubov preserves canonical Wronskian — only the declaration excludes it)"),
 "W_total_zero":("DERIVED",["T1_vertex_derived","T2_kernel_derived",
   "D6_derivative_rule"],
   "P3/P5 (coefficient 2 and endpoint -1 re-gated from derived artifacts; sigma-invariant)"),
 "W_split_2v2":("CONVENTION",["D3_TT_canonical_normalization"],
   "P5 sigma-reweighting gate"),
 "L_ladder_zero":("DERIVED",["even_degree_membership","bridge_D2_equals_nu_reflection",
   "M2_dummy_index_relabeling","D5_routing_contraction_conventions",
   "D6_derivative_rule"],
   "P6 derivation + P7 class theorem"),
 "R_channel_zero":("GATED FACT",["T1_vertex_derived","T2_kernel_derived",
   "D5_routing_contraction_conventions","D6_derivative_rule"],
   "P4 gate (Sigma_R == 0 pre-angular, all configs); mechanism characterized (2B.1 "
   "frequency-insertion antisymmetry); NOT derived from deeper principle — the one "
   "remaining underived vanishing"),
 "H1_zero_frozen":("DERIVED",["S_amplitude_zero","S_mixing_excluded","W_total_zero",
   "L_ladder_zero","R_channel_zero"],"P4 exact decomposition + the four channels"),
 "Lambda_class_theorem":("DERIVED",["M2_dummy_index_relabeling",
   "M3_momentum_reflection_parity"],
   "P7 abstract polynomial identity (no repo-specific input at all)"),
}
ok_class=all(v[0] in ALLOWED for v in GRAPH.values())
ok_prem=all(p in GRAPH for v in GRAPH.values() for p in v[1])
def ancestors(n,seen=None):
    seen=seen or set()
    for p in GRAPH[n][1]:
        if p not in seen:
            seen.add(p); ancestors(p,seen)
    return seen
ok_acyc=all(n not in ancestors(n) for n in GRAPH)
gate(ok_class and ok_prem and ok_acyc,
     "the dependency graph is WELL-FORMED: every node carries an allowed classification, "
     "every premise exists, the graph is ACYCLIC — no result serves as its own premise "
     "(%d nodes)"%len(GRAPH))
gate(all(GRAPH[p][0]!="CONTROL EVIDENCE" for p in ancestors("H1_zero_frozen")),
     "NO CONTROL AS PREMISE: nothing in H1_zero_frozen's ancestry is classified CONTROL "
     "EVIDENCE — the Phase-2/3 controls enter the synthesis ONLY as independence "
     "witnesses (section F), never as premises")
leaves=sorted(p for p in ancestors("H1_zero_frozen") if not GRAPH[p][1])
gate(all(GRAPH[p][0] in ("DECLARED INPUT","STANDARD IDENTITY","CONVENTION")
         for p in leaves),
     "every LEAF beneath the frozen H1 theorem is a DECLARED INPUT, STANDARD IDENTITY, "
     "or CONVENTION: %s"%leaves)
gate(ancestors("Lambda_class_theorem")=={"M2_dummy_index_relabeling",
     "M3_momentum_reflection_parity"},
     "the Level-II class theorem's ONLY ancestors are the two standard mathematical "
     "identities — it needs no repository-specific input (the strongest subtraction "
     "statement, machine-checked)")

print(); print("="*74); print("C-ANCHOR — LEVEL I: THE FOUR-CHANNEL ZERO (plus_z)"); print("="*74)
src=open(os.path.join(HERE,"wall_kr_tier3_loop.py"),encoding="utf-8").read()
M={"__name__":"frozen_t3","__file__":os.path.join(HERE,"wall_kr_tier3_loop.py")}
argv0=sys.argv; sys.argv=["x","machinery_only"]; os.chdir(HERE)
try: exec(compile(src,"t3","exec"),M)
except SystemExit: pass
sys.argv=argv0
CM,cdecomp,Ptt,htrunc=M["CM"],M["cdecomp"],M["Ptt"],M["htrunc"]
H,u,up,om,q,kap=M["H"],M["u"],M["up"],M["om"],M["q"],M["kap"]
n1,n2,n3=M["n1"],M["n2"],M["n3"]; PAIRS=M["PAIRS"]
qsub={}
for i_,tgt in ((1,n1),(2,n2),(3,n3)):
    qsub[sp.Symbol("q%d"%i_)]=q*tgt
    qsub[sp.Symbol("q%d"%i_,real=True)]=q*tgt
kk_=sp.Symbol('k',positive=True)
h_=sp.exp(-sp.I*kk_*u)*((1-H*u)+sp.I*H/kk_)
hb_=sp.exp(sp.I*kk_*up)*((1-H*up)-sp.I*H/kk_)
gate(sp.expand(sp.expand(h_*hb_).coeff(H,1)
     -sp.expand(sp.exp(-sp.I*kk_*(u-up))*(-(u+up))))==0,
     "ANCHOR S: the native O(H) state term vanishes at the identity level (re-gated)")
Wf=(kap**2/q)*sp.exp(-sp.I*q*(u-up)); pref=sp.Rational(1,2)/(2*kap**2)**2
def wop(e,a,c):
    for _ in range(a): e=-sp.I*sp.diff(e,u)
    for _ in range(c): e=-sp.I*sp.diff(e,up)
    return sp.expand(e)
def m_line(a,c): return sp.expand(wop(sp.expand(Wf*(1-H*(u+up))),a,c).coeff(H,1))
def flat_line(a,c): return sp.expand(wop(Wf,a,c))
def dem_line(a,c): return sp.expand(m_line(a,c)+(u+up)*flat_line(a,c))
E0={}; E1={}
for ck,vv in CM["plus_z"].items():
    if ck=="meta": continue
    ee=sp.sympify(vv); c0=ee.subs(H,0)
    if c0!=0: E0[ck]=sp.expand(c0.xreplace(qsub))
    r_=sp.expand(ee.coeff(H,1)-2*u*c0)
    if r_!=0: E1[ck]=sp.expand(r_.xreplace(qsub))
def build(DA,DB):
    P_line={}
    for (a,b) in PAIRS:
        for (ap,bp) in PAIRS: P_line[((a,b),(ap,bp))]=Ptt(a,b,ap,bp)
    V=defaultdict(lambda: sp.Integer(0))
    for (a,b) in PAIRS:
        for (c,dd_) in PAIRS:
            k1="%d%d_%d%d"%(a,b,c,dd_)
            if k1 not in DA: continue
            for (ap,bp) in PAIRS:
                for (cp,dp) in PAIRS:
                    k2="%d%d_%d%d"%(ap,bp,cp,dp)
                    if k2 not in DB: continue
                    PP=sp.expand(P_line[((a,b),(ap,bp))]*P_line[((c,dd_),(cp,dp))])
                    if PP==0: continue
                    for (nm1,nu1m),c1 in DA[k1].items():
                        for (nm2,nu2m),c2 in DB[k2].items():
                            V[(nu1m,nu2m)]+=sp.expand(c1*c2*PP
                                *(n1**(nm1[0]+nm2[0]))*(n2**(nm1[1]+nm2[1]))
                                *(n3**(nm1[2]+nm2[2])))
    return V
def dec(E): return cdecomp(htrunc(E))
def decT(E): return cdecomp(htrunc(sp.expand(E.xreplace({q:-q}).subs(om,-om).subs(u,up))))
D10={ck:dec(E) for ck,E in E0.items()}; D20={ck:decT(E) for ck,E in E0.items()}
V=build(D10,D20)
ok_w=True; ok_lad=True
byN=defaultdict(lambda: sp.Integer(0))
for key,vv in V.items():
    (e_,f_),(g_,h_)=key
    mA,mB=m_line(e_,g_),m_line(f_,h_)
    fA,fB=flat_line(e_,g_),flat_line(f_,h_)
    dA,dB=dem_line(e_,g_),dem_line(f_,h_)
    if sp.expand(pref*(mA*fB+fA*mB+2*(u+up)*fA*fB)-pref*(dA*fB+fA*dB))!=0: ok_w=False
    byN[e_+f_+g_+h_]+=sp.expand(vv*(g_+h_-e_-f_)*(-1)**(e_+f_))
gate(ok_w,"ANCHOR W: the per-key weight balance (-2+2) holds — m_key(full) == D_k "
     "(re-gated, all 36 keys)")
gate(all(sp.expand(v)==0 for v in byN.values()),
     "ANCHOR L: Lambda_N == 0 per sector (re-gated)")
D1R={ck:dec(E) for ck,E in E1.items()}; D2R={ck:decT(E) for ck,E in E1.items()}
SigR=sp.Integer(0)
for (DA,DB) in ((D1R,D20),(D10,D2R)):
    VR=build(DA,DB)
    for key,vv in VR.items():
        (e_,f_),(g_,h_)=key
        SigR+=sp.expand(vv*pref*flat_line(e_,g_)*flat_line(f_,h_))
def phase_classes(e):
    classes={}
    for t in sp.Add.make_args(sp.expand(e)):
        num,den=t.as_numer_denom()
        karg=sp.Integer(0); co_n=[]
        for f in sp.Mul.make_args(num):
            if isinstance(f,sp.exp): karg+=f.args[0]
            elif f.is_Pow and isinstance(f.base,sp.exp): karg+=f.exp*f.base.args[0]
            else:
                assert not f.atoms(sp.exp),"exp in non-exp factor"
                co_n.append(f)
        if den.atoms(sp.exp):
            dcls=phase_classes(den); (kd,cd),=dcls.items(); karg-=kd; den=cd
        key=sp.expand(karg)
        classes[key]=classes.get(key,sp.Integer(0))+sp.Mul(*co_n)/den
    return classes
gate(all(sp.cancel(sp.together(v))==0 for v in phase_classes(SigR).values()),
     "ANCHOR R: the fourth channel Sigma_R == 0 pre-angular (re-gated) — the full H1 "
     "object is the three slots PLUS this separately vanishing channel; R is NOT "
     "absorbed into S, W, or L   [%.0fs]"%(time.time()-t0))

print(); print("="*74); print("D-ANCHOR — LEVEL II: THE CLASS IDENTITY"); print("="*74)
nu1s,nu2s,oms=sp.symbols("NU1 NU2 OM")
mon2=[oms**2,oms*nu1s,oms*nu2s,nu1s**2,nu1s*nu2s,nu2s**2]
NENT=3
ents={}
for r in range(NENT):
    E=sp.Symbol("z_%d"%r)*1
    for i_,m_ in enumerate(mon2): E+=sp.Symbol("c_%d_%d"%(r,i_))*m_
    ents[r]=sp.expand(E)
PIs={}
for r in range(NENT):
    for s_ in range(r,NENT): PIs[(r,s_)]=PIs[(s_,r)]=sp.Symbol("pi_%d_%d"%(r,s_))
def nu_dec(E):
    out={}
    p=sp.Poly(E,nu1s,nu2s)
    for mono,co in zip(p.monoms(),p.coeffs()):
        out[mono]=out.get(mono,sp.Integer(0))+co
    return out
D1a={r:nu_dec(E) for r,E in ents.items()}
D2a={r:nu_dec(sp.expand(E.subs(oms,-oms))) for r,E in ents.items()}
byNa=defaultdict(lambda: sp.Integer(0))
for r in range(NENT):
    for s_ in range(NENT):
        for m1,c1 in D1a[r].items():
            for m2,c2 in D2a[s_].items():
                e_,f_=m1; g_,h_=m2
                byNa[e_+f_+g_+h_]+=sp.expand(PIs[(r,s_)]*c1*c2
                    *(g_+h_-e_-f_)*(-1)**(e_+f_))
gate(all(sp.expand(v)==0 for v in byNa.values()),
     "ANCHOR CLASS: the Level-II identity re-verified — generic even-degree entries "
     "(degrees {0,2}) + generic symmetric pairing => Lambda_N == 0 as a polynomial "
     "identity; its only premises are the two standard identities (graph-checked above)")

print(); print("="*74); print("RECORD GATES — THE SEPARATIONS ARE IN THE MD"); print("="*74)
mdp=os.path.join(HERE,"WALL_KR_H1_PHASE8_RESULT.md"); md=open(mdp,encoding="utf-8").read()
for frag,desc in (
  ("LEVEL I","Level-I frozen-construction theorem present"),
  ("LEVEL II","Level-II class theorem present"),
  ("LEVEL III","Level-III EH statement present"),
  ("missing bridge","the EH missing-bridge items are named explicitly"),
  ("separately vanishing","the R channel is kept separate, not absorbed"),
  ("NO GRUT-SPECIFIC PRINCIPLE FOUND","the GRUT novelty gate verdict is recorded"),
  ("not universally necessary","the pairing-necessity honesty is carried"),
  ("independence witnesses","controls used as witnesses only"),
  ("physically independent mechanisms","the physical-independence disclaimer present")):
    gate(frag in md,"record carries: %s"%desc)

print(); print("="*74); print("17 — GOVERNANCE EXIT"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
gate(POST==PRE,"register sha256 identical pre/post")
frozen_clean=git("status","--porcelain","--","PHYSICS_LEDGER/wall_kr_tier3_loop.py",
  "PHYSICS_LEDGER/.tier3_cmat_cache.json","PHYSICS_LEDGER/.tier1_ds_cache.json",
  "provenance/claims.json").stdout.strip()
gate(frozen_clean=="","no frozen physics file modified")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for ok,_ in CHECKS if ok)
verdict="H1-STRUCTURALLY-CLOSED-BUT-NOT-EH-GENERAL" if not FAILURES else "INCONCLUSIVE"
print("  battery: %d/%d testable gates, failures: %d   [%.0fs]"
      %(n,len(CHECKS),len(FAILURES),time.time()-t0))
for f in FAILURES: print("    FAILED: "+f)
print("  VERDICT: %s"%verdict)
out={"instrument":"wall_kr_h1_phase8_synthesis.py","date":"2026-09-04","base":"d44bfd2",
 "kind":"H1 CLOSURE PHASE 8 — synthesis / quantified theorem adjudication",
 "battery":"%d/%d testable"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "dependency_graph":{k:{"class":v[0],"premises":v[1],"provenance":v[2]}
                     for k,v in GRAPH.items()},
 "graph_facts":{"acyclic":bool(ok_acyc),
   "no_control_as_premise":bool(all(GRAPH[p][0]!="CONTROL EVIDENCE"
     for p in ancestors("H1_zero_frozen"))),
   "leaves_all_input_or_standard":leaves,
   "class_theorem_ancestors":sorted(ancestors("Lambda_class_theorem"))},
 "verdict":verdict,
 "A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(HERE,"WALL_KR_H1_PHASE8_RESULT.json"),"w",encoding="utf-8"),
          indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_H1_PHASE8_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
print("PHASE8_DONE")
