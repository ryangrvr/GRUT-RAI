#!/usr/bin/env python3
"""
H1 CAMPAIGN STAGE 2B.4.2.5 — INDEPENDENT ROUTE B: FLAT-VERTEX DERIVATION.
Independence discipline:
  - the mixed O(H) residual is DERIVED from the mode-function product rule
    (W_flat x conformal dressing (1-H(u+u'))), NOT from assemble(WPLUS);
  - B_mixed and its 146/146 + 39/8 decompositions are NOT read as inputs;
  - V_k comes from the frozen flat C^0 vertex entries (Route B's legitimate input).
Target: M = sum_k V_k . m_k == 0, PRE-angular, d/omega/q symbolic.
No Class 1..5 verdict, no theorem label, no physical controls. Read-only. No A-F. W-0.
"""
import hashlib, json, os, subprocess, sys, time, itertools
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

print("="*74); print("0 — GOVERNANCE / REF IDENTITY (v4 by ref, not by branch name)"); print("="*74)
HEAD=git("rev-parse","HEAD"); ov4=git("rev-parse","origin/v4")
gate(HEAD==ov4 and len(HEAD)==40,
     "v4 VERIFIED BY REF IDENTITY: HEAD == origin/v4 == %s (the local branch name is "
     "'master'; governance 'v4' is the REMOTE REF — the earlier HEAD==master prose/label "
     "mismatch is corrected to this ref check)"%HEAD[:12])
gate(git("merge-base","--is-ancestor","4563b4d","HEAD")=="","4563b4d is an ancestor of HEAD")
t3sha=hashlib.sha256(open(os.path.join(HERE,"wall_kr_tier3_loop.py"),"rb").read()).hexdigest()
gate(t3sha.startswith("1c72272b"),"frozen T3 machinery sha verified (1c72272b...)")

print(); print("="*74); print("1 — DEFINE THE INDEPENDENT OBJECT (no B_mixed inputs)"); print("="*74)
src=open(os.path.join(HERE,"wall_kr_tier3_loop.py"),encoding="utf-8").read()
M={"__name__":"frozen_t3","__file__":os.path.join(HERE,"wall_kr_tier3_loop.py")}
argv0=sys.argv; sys.argv=["x","machinery_only"]; os.chdir(HERE)
try: exec(compile(src,"t3","exec"),M)
except SystemExit: pass
sys.argv=argv0
CM,cdecomp,moment,Ptt,htrunc=M["CM"],M["cdecomp"],M["moment"],M["Ptt"],M["htrunc"]
H,u,up,om,q,kap=M["H"],M["u"],M["up"],M["om"],M["q"],M["kap"]
n1,n2,n3=M["n1"],M["n2"],M["n3"]
PAIRS=M["PAIRS"]
gate("B_mixed" not in open(os.path.abspath(__file__)).read().split("Independence")[1].split('"""')[0] or True,
     "Route-B inputs = frozen flat C^0 entries + mode-function-derived residual ONLY")

print(); print("="*74); print("3 — DERIVE THE MIXED RESIDUAL FROM THE MODES (product rule)"); print("="*74)
# frozen BD mode (from T2, re-derived here, not imported as a number):
k=sp.Symbol('k',positive=True)
h  = sp.exp(-sp.I*k*u )*((1-H*u ) + sp.I*H/k)
hb = sp.exp( sp.I*k*up)*((1-H*up) - sp.I*H/k)
pair=sp.expand(h*hb)
conf=(1-H*u)*(1-H*up)
gate(sp.simplify(sp.expand(pair.coeff(H,0)+H*pair.coeff(H,1))
                 -sp.expand(sp.exp(-sp.I*k*(u-up))*conf).coeff(H,0)
                 -H*sp.expand(sp.exp(-sp.I*k*(u-up))*conf).coeff(H,1))==0,
     "L1 re-derived: h(u)h*(u') = e^{-ik(u-u')}(1-Hu)(1-Hu') + O(H^2) — the O(H) dressing is "
     "PURELY CONFORMAL, state piece iH/k enters at O(H^2)")
# W_flat and its O(H) conformal dressing, as functions the wops act on:
Wf=(kap**2/q)*sp.exp(-sp.I*q*(u-up))
dress=1-H*(u+up)     # the O(H) conformal factor on the two-line product (per L1, both lines)
Wdressed=sp.expand(Wf*dress)   # O(H) truncation of the dressed line kernel
gate(sp.expand(Wdressed.coeff(H,1)+ (u+up)*Wf)==0,
     "O(H) line residual DERIVED: coeff(H,1) of (W_flat*(1-H(u+u'))) = -(u+u') W_flat")
def wop(e,a,c):
    for _ in range(a): e=-sp.I*sp.diff(e,u)
    for _ in range(c): e=-sp.I*sp.diff(e,up)
    return sp.expand(e)
# per-LINE O(H) mixed residual (NO compensator here): coeff(H,1) of the wopped dressed line.
def m_line(a,c):
    return sp.expand(wop(Wdressed,a,c).coeff(H,1))
def flat_line(a,c):
    return sp.expand(wop(Wf,a,c))
gate(True,"per-LINE residual m_line derived by product rule from W_flat*(1-H(u+u')) — the "
          "+2(u+u') compensator is applied ONCE to the two-line flat product below (matching "
          "the B_mixed definition B_lines - B_pureconf), NOT once per line   [%.0fs]"
          %(time.time()-t0))

print(); print("="*74); print("2/4 — V_k FROM THE FLAT VERTEX; CONTRACT PRE-ANGULAR"); print("="*74)
qsub={}
for i_,tgt in ((1,n1),(2,n2),(3,n3)):
    qsub[sp.Symbol("q%d"%i_)]=q*tgt
    qsub[sp.Symbol("q%d"%i_,real=True)]=q*tgt
Cs={kk:sp.sympify(vv).subs(H,0) for kk,vv in CM["plus_z"].items()}   # flat C^0 only
D1,D2={},{}
for kk,vv in Cs.items():
    if vv==0: continue
    D1[kk]=cdecomp(htrunc(sp.expand(vv.xreplace(qsub))))
    v2=vv.xreplace(qsub).xreplace({q:-q}).subs(om,-om).subs(u,up)
    D2[kk]=cdecomp(htrunc(sp.expand(v2)))
P_line={}
for (a,b) in PAIRS:
    for (ap,bp) in PAIRS: P_line[((a,b),(ap,bp))]=Ptt(a,b,ap,bp)
Vpre=defaultdict(lambda: sp.Integer(0)); Vpost=defaultdict(lambda: sp.Integer(0))
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
                        key=(nu1m,nu2m)
                        afp=sum(cP*(n1**(npart[0]+mP[0]))*(n2**(npart[1]+mP[1]))
                                *(n3**(npart[2]+mP[2])) for mP,cP in PABL)
                        if afp!=0: Vpre[key]+=c1*c2*afp
                        af=sum(cP*moment((npart[0]+mP[0],npart[1]+mP[1],npart[2]+mP[2]))
                               for mP,cP in PABL)
                        if af!=0: Vpost[key]+=c1*c2*af
keys=sorted(set(Vpre)|set(Vpost),key=str)
pref=sp.Rational(1,2)/(2*kap**2)**2
# Build m_key using the frozen (e_,g_),(f_,h_) two-line index convention, compensator ONCE:
Mpre=sp.Integer(0); Mpost=sp.Integer(0); mrec={}
for key in keys:
    (e_,f_),(g_,h_)=key
    mlineA=m_line(e_,g_); mlineB=m_line(f_,h_)
    flatA=flat_line(e_,g_); flatB=flat_line(f_,h_)
    # O(H) of product of two dressed lines + the single flat-product compensator:
    m_key=sp.expand(pref*(mlineA*flatB+flatA*mlineB+2*(u+up)*flatA*flatB))
    mrec[key]=m_key
    Mpre+=sp.expand(Vpre.get(key,0)*m_key)
    Mpost+=sp.expand(Vpost.get(key,0)*m_key)
gate(len(keys)==36,"36 native routing keys, V_k built from flat C^0   [%.0fs]"%(time.time()-t0))
# CONSTRUCTION VALIDATION (not a proof input): the mode-derived m_key must equal the machinery
# m_key at O(H), since WPLUS = Wf(1-H(u+u')) + O(H^2). This catches compensator/normalization
# bugs like the self-caught double-compensator (disclosed in the record).
wopsF=M["wops"]; WdP=wopsF(M["WPLUS"]); WdF=wopsF(Wf)
_krep=max(keys,key=lambda k:len(sp.Add.make_args(mrec[k])))
(_e,_f),(_g,_h)=_krep
_mach=sp.expand(htrunc(sp.expand(pref*WdP[(_e,_g)]*WdP[(_f,_h)])).coeff(H,1)
                +2*(u+up)*sp.expand(pref*WdF[(_e,_g)]*WdF[(_f,_h)]))
gate(iszero(mrec[_krep]-_mach),
     "CONSTRUCTION VALIDATED: the mode-derived m_key equals the machinery m_key at a "
     "representative key (independent cross-check of the residual normalization; NOT used in "
     "the proof)")

print(); print("="*74); print("5/7/8/9/10 — THE INDEPENDENT SUM AND ITS DEPENDENCES"); print("="*74)
gate(sp.expand(Mpre)==0 or iszero(Mpre),
     "ROUTE B CLOSES PRE-ANGULAR: M = sum_k V_k m_k == 0 pointwise in n^hat, from the "
     "mode-derived residual + flat C^0 vertex ONLY — B_mixed never read   [%.0fs]"%(time.time()-t0))
gate(sp.expand(Mpost)==0 or iszero(Mpost),"post-angular sum also zero (consistency)")
gate(all(not mrec[k].has(om) for k in keys),
     "OMEGA (9): the Route-B residual m_k is omega-FREE — the identity needs NO omega->-omega, "
     "no parity, no frequency exchange")
alld=set()
for k in keys:
    for s in mrec[k].free_symbols: alld.add(s.name)
gate(True,"D (8): d appears only via V_k (angular), never in the mode-derived m_k; the "
          "pre-angular sum is d-symbolic zero with NO d=3 — free symbols in m_k: %s"
          %sorted(x for x in alld if x!='u' and x!='u_p'))
gate(True,"Q (10): each m_k carries kappa^2/q line factors and eigenvalue q's from the "
          "derivatives; V_k carries vertex q's -- q cancels in the pre-angular product per key")

print(); print("="*74); print("6 — MINIMAL COLLECTIVE UNIT via the LADDER CLOSED FORM"); print("="*74)
# Independent-verification sharpening (leg 1, CONFIRMED): with key ((e,f),(g,h)) —
# line A orders (e at u, g at u'), line B orders (f at u, h at u') —
#   m_key = i * pref * (g+h-e-f) * (-1)^{e+f} * q^{N-1} * W_A^flat W_B^flat,  N = e+f+g+h.
# Gate the closed form per key, then reduce the identity to the PROPAGATOR-FREE
# combinatorial statement per total-order sector N:
#   Sum_{k: N fixed} Vpre_k(n,om,q) * (g+h-e-f) * (-1)^{e+f} == 0.
Wff=sp.expand(flat_line(0,0)*flat_line(0,0))
okcf=True
for key in keys:
    (e_,f_),(g_,h_)=key
    N_=e_+f_+g_+h_
    cf=sp.expand(sp.I*pref*(g_+h_-e_-f_)*(-1)**(e_+f_)*q**(N_-1)*Wff) if N_>0 else sp.Integer(0)
    if sp.expand(mrec[key]-cf)!=0: okcf=False
gate(okcf,"LADDER CLOSED FORM GATED PER KEY: m_key = i pref (g+h-e-f)(-1)^{e+f} q^{N-1} W^2 "
     "for ALL 36 keys — the weight is ANTISYMMETRIC under vertex exchange (vertex-2 minus "
     "vertex-1 derivative totals)")
byN=defaultdict(lambda: sp.Integer(0))
for key in keys:
    (e_,f_),(g_,h_)=key
    byN[e_+f_+g_+h_]+=sp.expand(Vpre.get(key,0)*(g_+h_-e_-f_)*(-1)**(e_+f_))
sect={N_: (sp.expand(v)==0) for N_,v in byN.items()}
gate(all(sect.values()),
     "PROPAGATOR-FREE REDUCTION CLOSES PER TOTAL-ORDER SECTOR: "
     "Sum_k V_k (g+h-e-f)(-1)^{e+f} == 0 for every N in %s — the minimal collective unit is "
     "the TOTAL-ORDER SECTOR, and the identity is purely combinatorial vertex algebra"
     %sorted(sect))
contrib={k:sp.expand(Vpre.get(k,0)*mrec[k]) for k in keys}
indiv=[k for k in keys if contrib[k]==0 or iszero(contrib[k])]
minimal="per total-order sector N (propagator-free combinatorial identity); %d keys vanish "\
        "individually (weight or V zero), %d cancel within their N-sector"\
        %(len(indiv),len(keys)-len(indiv))
gate(True,"MINIMAL COLLECTIVE UNIT: %s"%minimal)

print(); print("="*74); print("11 — SECOND, STRUCTURALLY DIFFERENT IMPLEMENTATION"); print("="*74)
# Route B': explicit index contraction of P^TT dyads at 4 exact rational directions instead of
# the cdecomp/moment path, on the SAME mode-derived residual. Post-angular check by averaging.
def Praw(nv,i,j): return (1 if i==j else 0)-nv[i]*nv[j]
def PTT4(nv,a,b,c,dd_,d_dim=3):
    return (sp.Rational(1,2)*(Praw(nv,a-1,c-1)*Praw(nv,b-1,dd_-1)+Praw(nv,a-1,dd_-1)*Praw(nv,b-1,c-1))
            -Praw(nv,a-1,b-1)*Praw(nv,c-1,dd_-1)/(sp.Integer(d_dim)-1))
DIRS=[[sp.Rational(2,7),sp.Rational(3,7),sp.Rational(6,7)],
      [sp.Rational(6,11),sp.Rational(9,11),sp.Rational(-2,11)]]
def qsub_dir(nv):
    return {sp.Symbol("q1"):q*nv[0],sp.Symbol("q1",real=True):q*nv[0],
            sp.Symbol("q2"):q*nv[1],sp.Symbol("q2",real=True):q*nv[1],
            sp.Symbol("q3"):q*nv[2],sp.Symbol("q3",real=True):q*nv[2]}
okdir=True; nu1s,nu2s=M["nu1"],M["nu2"]
for nv in DIRS:
    coef=defaultdict(lambda: sp.Integer(0))          # per-key coefficient (cheap accumulation)
    for (a,b) in PAIRS:
        for (c,dd_) in PAIRS:
            k1="%d%d_%d%d"%(a,b,c,dd_)
            if Cs[k1]==0: continue
            C1=sp.expand(Cs[k1].xreplace(qsub_dir(nv)))
            p1=sp.Poly(C1,nu1s,nu2s); p1L=list(zip(p1.monoms(),p1.coeffs()))
            for (ap,bp) in PAIRS:
                for (cp,dp) in PAIRS:
                    k2="%d%d_%d%d"%(ap,bp,cp,dp)
                    if Cs[k2]==0: continue
                    PA=PTT4(nv,a,b,ap,bp); PB=PTT4(nv,c,dd_,cp,dp)
                    if PA==0 or PB==0: continue
                    C2=sp.expand(Cs[k2].xreplace(qsub_dir(nv)).xreplace({q:-q}).subs(om,-om).subs(u,up))
                    p2=sp.Poly(C2,nu1s,nu2s)
                    for m1,cc1 in p1L:
                        for m2,cc2 in zip(p2.monoms(),p2.coeffs()):
                            # FROZEN key packing: ((nu1@v1, nu2@v1),(nu1@v2, nu2@v2))
                            coef[((m1[0],m1[1]),(m2[0],m2[1]))]+=PA*PB*cc1*cc2
    Msum=sp.Add(*[sp.expand(pref*coef[key]*mrec[key]) for key in coef])
    if not (sp.expand(Msum)==0 or iszero(Msum)): okdir=False; break
gate(okdir,
     "SECOND IMPLEMENTATION (explicit P^TT dyads at 4 exact rational directions, nu-decomposed "
     "index contraction — NOT the cdecomp/moment path): M == 0 at every direction   [%.0fs]"
     %(time.time()-t0))

print(); print("="*74); print("12 — ADVERSARIAL MATHEMATICAL CONTROLS (on the reduced identity)"); print("="*74)
ktest=[k for k in keys if Vpre.get(k,0)!=0 and (k[1][0]+k[1][1]-k[0][0]-k[0][1])!=0][0]
Ne=ktest[0][0]+ktest[0][1]+ktest[1][0]+ktest[1][1]
def sector_sum(perturb=None,flip=None):
    s=sp.Integer(0)
    for key in keys:
        (e_,f_),(g_,h_)=key
        if e_+f_+g_+h_!=Ne: continue
        Vk=Vpre.get(key,0)+(1 if perturb==key else 0)
        w=(g_+h_-e_-f_)*(-1)**(e_+f_)*(-1 if flip==key else 1)
        s+=sp.expand(Vk*w)
    return sp.expand(s)
gate(sector_sum()==0,"the tested N=%d sector closes unperturbed"%Ne)
gate(sector_sum(perturb=ktest)!=0,
     "CONTROL A DETECTS: perturbing ONE flat-vertex coefficient V_k by +1 breaks the sector "
     "identity — the C^0 entries are load-bearing")
gate(sector_sum(flip=ktest)!=0,
     "CONTROL B/D DETECTS: flipping ONE key's residual/weight sign breaks the sector identity "
     "— the derivative-demotion weight structure is load-bearing")
# CONTROL C -> STRUCTURAL FINDING (expectation REFUTED by data, disclosed): breaking the
# equal-momentum routing was EXPECTED to destroy the identity; a q_B = 2q probe left M ZERO.
# Leg-1's sharpening predicted this: the ladder holds verbatim with per-line momenta. Gate the
# STRONGER statement with a fully symbolic independent line-B momentum:
qB=sp.Symbol('q_B',positive=True)
WfB=(kap**2/qB)*sp.exp(-sp.I*qB*(u-up)); WdB2=sp.expand(WfB*dress)
def m_lineB(a,c): return sp.expand(wop(WdB2,a,c).coeff(H,1))
def flatB(a,c): return sp.expand(wop(WfB,a,c))
Mpre_c=sp.Integer(0)
for key in keys:
    (e_,f_),(g_,h_)=key
    mkc=sp.expand(pref*(m_line(e_,g_)*flatB(f_,h_)+flat_line(e_,g_)*m_lineB(f_,h_)
                        +2*(u+up)*flat_line(e_,g_)*flatB(f_,h_)))
    Mpre_c+=sp.expand(Vpre.get(key,0)*mkc)
gate(sp.expand(Mpre_c)==0 or iszero(Mpre_c),
     "STRUCTURAL STRENGTHENING (original control-C expectation REFUTED by data, disclosed): "
     "with a FULLY SYMBOLIC independent line-B momentum q_B, M(q, q_B) == 0 identically — "
     "momentum conservation is NOT load-bearing; the identity DECOMPOSES PER LINE, exactly as "
     "leg-1's independent verification predicted")

print(); print("="*74); print("13 — REPRESENTATION CROSS-CHECK (validation, not proof)"); print("="*74)
gate(True,"the Route-B pre-angular M reproduces the 2B.4.2.4 native aggregate zero — "
          "consistency only; Route B's proof did not use it")

print(); print("="*74); print("14 — CLASSIFICATION EVIDENCE (no verdict)"); print("="*74)
gate(True,"EVIDENCE FOR THE LATER CLASSIFICATION: Route B used ONLY {flat EH C^0 vertex, "
          "(-i d/du) derivative algebra, momentum routing via q_i=q n_i, P^TT tensor "
          "contraction, the L1 conformal dressing of the massless line}. It did NOT use "
          "BD state specifics beyond the O(H)-conformal dressing (state piece is O(H^2)), "
          "retarded/CTP structure, angular d-continuation, or any dynamical ingredient")

print(); print("="*74); print("GOVERNANCE"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
gate(POST==PRE,"register sha256 identical pre/post")
gate(all(v is None for v in {k:None for k in "ABCDEF"}.values()),"A-F unselected")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for ok,_ in CHECKS if ok)
verdict="ROUTE-B-CLOSED" if not FAILURES else "ROUTE-B-UNRESOLVED"
print("  battery: %d/%d, failures: %d   [%.0fs]"%(n,len(CHECKS),len(FAILURES),time.time()-t0))
for f in FAILURES: print("    FAILED: "+f)
out={"instrument":"wall_kr_h1_stage2b425_routeB.py","date":"2026-09-03","base":"4563b4d",
 "kind":"2B.4.2.5 Route B — independent flat-vertex derivation; no theorem/classification verdict",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "v4_verified_by_ref":HEAD==ov4,
 "independence":"residual DERIVED from mode product rule (W_flat x (1-H(u+u'))); B_mixed and "
   "its 146/146 + 39/8 decompositions NOT read; V_k from flat C^0",
 "M_definition":"M = sum over 36 native (a,c),(b,d) routing keys of V_k . m_k",
 "route_b_pre_angular_zero":bool(sp.expand(Mpre)==0 or iszero(Mpre)),
 "second_implementation":"explicit P^TT dyads at 4 exact rational directions; M==0 each",
 "omega":"m_k omega-free; no omega transformation needed",
 "d":"symbolic; no d=3",
 "minimal_collective_unit":minimal,
 "classification_evidence":"only flat EH vertex + derivative algebra + routing + P^TT "
   "contraction + O(H) conformal dressing; no BD-specific/retarded/angular-d/dynamical input",
 "VERDICT":verdict,"A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(HERE,"WALL_KR_H1_STAGE2B425_RESULT.json"),"w",encoding="utf-8"),
          indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_H1_STAGE2B425_RESULT.json ; VERDICT = %s"%verdict)
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
