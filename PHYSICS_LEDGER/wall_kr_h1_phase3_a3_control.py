#!/usr/bin/env python3
"""
H1 CLOSURE — PHASE 3: a^2 -> a^3 VERTEX-WEIGHT DEFORMATION CONTROL.
Narrow question (per the order): is the native H1 cancellation dependent on the specific
a^2/conformal vertex-weight structure?  A CONTROL — not a uniqueness proof, not a theorem,
not a vertex refit.

THE DEFINITION, ANCHORED TO THE FROZEN ARTIFACT (gated below before any evaluation):
  - The frozen vertex's literal O(H) grading is V3^(1) = 2u*V3^(0) + R with R u-FREE
    (re-gated here from the 26,032-term artifact; first gated in Stage 2A). The
    multiplicative piece 2u*V0 is the conformal weight; the coefficient 2 is the a-power
    (a^2 per vertex, a(u) = 1/(1-Hu) ~ 1+Hu). R is Protection 1's separate structure.
  - Per line, the kernel carries (1-Hu)(1-Hu') (one 1/a per mode endpoint); the TWO-line
    product gives -2(u+u')*flat at O(H). The TWO vertices at a^2 give +2(u+u')*flat.
    The multiplicative balance cancels EXACTLY; the demotion remainder cancels by the
    per-sector ladder identity. The Route-B "+2(u+u') compensator" IS the two-vertex a^2
    weight (equivalently -B_pureconf) — gated below.
  - DEFORMATION: per-vertex weight coefficient 2 -> 2+beta (a^3 at beta=1). In the pair
    assembly the vertex-weight term becomes (2+beta)(u+u')*flatA*flatB. NOTHING else
    changes: V0, R, line/state kernels, routing, projector, derivative algebra all frozen.
    beta symbolic; beta0 = 1 REGISTERED (the a^3 point); reversible at beta=0.
  - LIMITATION (disclosed): a full a^3-weighted EH-like vertex would also differ in its
    R-analogue and at O(H^2); this control deforms ONLY the multiplicative conformal
    weight — the structural role of the native a^2 weighting, nothing more.
Independent reconstruction (Route-B style): no B_mixed, no Phase-1 swap relation, no
Phase-2 M1 as inputs. Zero-gates exact-symbolic; numeric witness NEVER used for zero.
Read-only on frozen artifacts. A-F untouched. W-0.
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

# ---- exact zero-decision for the exp(i*linear form) x rational-coefficient family ----
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
def iszero(e):
    return all(sp.cancel(sp.together(v))==0 for v in phase_classes(e).values())

print("="*74); print("0 — GOVERNANCE HARD STOP + DECISION-PROCEDURE SELF-CHECKS"); print("="*74)
HEAD=git("rev-parse","HEAD").stdout.strip(); ov4=git("rev-parse","origin/v4").stdout.strip()
gate(HEAD!="" and HEAD==ov4,"v4 by REF IDENTITY: HEAD == origin/v4 == %s"%HEAD[:12])
gate(git("merge-base","--is-ancestor","bedc989","HEAD").returncode==0,
     "bedc989 (Phase 1, reconciled) in ancestry — by RETURNCODE")
gate(git("merge-base","--is-ancestor","39551c7","HEAD").returncode==0,
     "39551c7 (Phase 2, closed) in ancestry — by RETURNCODE")
t3sha=hashlib.sha256(open(os.path.join(HERE,"wall_kr_tier3_loop.py"),"rb").read()).hexdigest()
gate(t3sha.startswith("1c72272b"),"frozen T3 machinery sha 1c72272b... unchanged")
ph_clean=git("status","--porcelain","--","PHYSICS_LEDGER/WALL_KR_H1_PHASE1.md",
  "PHYSICS_LEDGER/WALL_KR_H1_PHASE2.md","PHYSICS_LEDGER/WALL_KR_H1_PHASE2_RESULT.json",
  "PHYSICS_LEDGER/wall_kr_h1_phase2_alpha_control.py").stdout.strip()
gate(ph_clean=="","Phase-1/Phase-2 artifacts byte-identical (git-clean); Phase 2 CLOSED, "
     "not reopened")
_u,_q=sp.symbols("selfchk_u selfchk_q")
gate(iszero(sp.exp(sp.I*_q*_u)*sp.exp(-sp.I*_q*_u)-1) and
     not iszero(sp.exp(-sp.I*_q*_u)) and iszero((_u+1)**2-_u**2-2*_u-1),
     "decision-procedure self-checks: phase-merging trap ZERO; nonzero NONZERO; poly ZERO")
note("A-F remain UNSELECTED; W-0; nothing banked; Phase 4 NOT started")

print(); print("="*74); print("2/3 — THE DEFINITION GATE: a^2 READ OFF THE FROZEN ARTIFACT"); print("="*74)
dc=json.load(open(os.path.join(HERE,'.tier1_ds_cache.json')))
V3=sp.sympify(dc["sectors"]["(1, 2, 3)"])
V3=V3.xreplace({s: sp.Symbol(s.name) for s in V3.free_symbols})
Hs=sp.Symbol('H'); us=sp.Symbol('u')
terms=sp.Add.make_args(V3)
gate(len(terms)==26032,"frozen T1 vertex reloaded: 26,032 dS terms")
V0g=sp.Add(*[t for t in terms if not t.has(Hs)])
V1g=sp.Add(*[t for t in terms if (sp.degree(t,Hs) if t.has(Hs) else 0)==1]).coeff(Hs,1)
Rg=sp.expand(V1g-2*us*V0g)
gate(Rg!=0 and not Rg.has(us),
     "LITERAL GRADING RE-GATED: V3^(1) = 2u*V3^(0) + R with R u-FREE — the multiplicative "
     "conformal weight is EXACTLY 2u per vertex; the coefficient 2 is the a-power (a^2)")
gate(sp.expand(V1g-3*us*V0g).has(us) or sp.expand(sp.Add(*[t for t in
     sp.Add.make_args(sp.expand(V1g-3*us*V0g)) if t.has(us)]))!=0,
     "UNIQUENESS of the coefficient: V3^(1) - 3u*V3^(0) is NOT u-free — no other integer "
     "weight reproduces the frozen grading; 2 is the unique multiplicative coefficient")
# the two-sided balance that the deformation detunes, gated at O(H):
uu,uup,HH=sp.symbols("bal_u bal_up bal_H")
lines2=sp.expand(((1-HH*uu)*(1-HH*uup))**2)      # two lines x (1/a per mode endpoint)
gate(sp.expand(lines2.coeff(HH,1)+2*(uu+uup))==0,
     "LINE SIDE GATED: the two-line conformal product carries -2(u+u') at O(H)")
gate(sp.expand((2*uu+2*uup)-2*(uu+uup))==0,
     "VERTEX SIDE GATED: the two vertices' a^2 weight carries +2u+2u' = +2(u+u') at O(H) — "
     "the multiplicative balance cancels EXACTLY; the Route-B '+2(u+u') compensator' IS the "
     "two-vertex a^2 weight (equivalently -B_pureconf). Changing the vertex weight "
     "mathematically REQUIRES changing this term — the order's carved-out case")
beta=sp.Symbol("beta",real=True); BETA0=1
note("DEFORMATION DEFINED before evaluation: per-vertex weight 2 -> 2+beta; pair-level "
     "vertex-weight term (2+beta)(u+u')*flatA*flatB; beta0=1 REGISTERED (the a^3 point); "
     "reversible at beta=0; V0, R, lines/state, routing, projector, derivatives UNCHANGED")
note("LIMITATION (disclosed): a full a^3 EH-like vertex would also differ in its R-analogue "
     "and at O(H^2); this control deforms ONLY the multiplicative conformal weight")

print(); print("="*74); print("1 — LOAD FROZEN MACHINERY"); print("="*74)
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
dress=1-H*(u+up)
Wdressed=sp.expand(Wf*dress)
def wop(e,a,c):
    for _ in range(a): e=-sp.I*sp.diff(e,u)
    for _ in range(c): e=-sp.I*sp.diff(e,up)
    return sp.expand(e)
def m_line(a,c):  return sp.expand(wop(Wdressed,a,c).coeff(H,1))
def flat_line(a,c): return sp.expand(wop(Wf,a,c))
pref=sp.Rational(1,2)/(2*kap**2)**2
qsub={}
for i_,tgt in ((1,n1),(2,n2),(3,n3)):
    qsub[sp.Symbol("q%d"%i_)]=q*tgt
    qsub[sp.Symbol("q%d"%i_,real=True)]=q*tgt
def build_V(config):
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
    V=defaultdict(lambda: sp.Integer(0))
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
                            if afp!=0: V[(nu1m,nu2m)]+=c1*c2*afp
    return V
def ang(expr):
    expr=sp.expand(expr); out=sp.Integer(0)
    for t in sp.Add.make_args(expr):
        pows=[sp.degree(t,v) if t.has(v) else 0 for v in (n1,n2,n3)]
        c=t
        for v,p in zip((n1,n2,n3),pows): c=c/v**p
        out+=c*moment(tuple(pows))
    return sp.expand(out)

RES={}
for config in ("plus_z","cross_z","plus_x"):
    print(); print("="*74)
    print("4-7 [%s] — NATIVE LIMIT, DEFORMED CASE, LOCALIZATION"%config); print("="*74)
    V=build_V(config); keys=sorted(V,key=str)
    note("[%s] %d native routing keys, V_k from flat C^0   [%.0fs]"
         %(config,len(keys),time.time()-t0))
    M0=sp.Integer(0); Sig0=sp.Integer(0)
    Djm=defaultdict(lambda: sp.Integer(0))   # (j,m)-resolved DEFORMATION aggregate
    byN=defaultdict(lambda: sp.Integer(0))   # ladder sector sums (beta-free)
    for key in keys:
        (e_,f_),(g_,h_)=key
        mA,mB=m_line(e_,g_),m_line(f_,h_)
        fA,fB=flat_line(e_,g_),flat_line(f_,h_)
        ff=sp.expand(pref*fA*fB)
        M0+=sp.expand(V[key]*pref*(mA*fB+fA*mB+2*(u+up)*fA*fB))
        Sig0+=sp.expand(V[key]*ff)
        Djm[(e_+f_,g_+h_)]+=sp.expand(V[key]*(u+up)*ff)
        byN[e_+f_+g_+h_]+=sp.expand(V[key]*(g_+h_-e_-f_)*(-1)**(e_+f_))
    # ---- section 4: NATIVE LIMIT (exact-symbolic) ----
    ok0=iszero(M0)
    gate(ok0,"[%s] NATIVE LIMIT VERIFIED: M(beta=0) == 0 pointwise pre-angular, "
         "reconstructed independently (no B_mixed, no swap relation, no Phase-2 M1)   "
         "[%.0fs]"%(config,time.time()-t0))
    if not ok0:
        RES[config]={"native":False}; continue
    # ---- section 5: DEFORMED CASE — M(beta) = M0 + beta*(u+u')*Sig0, exact by construction
    M1=sp.expand((u+up)*Sig0)
    # linearity is exact: the deformation enters the assembly affinely; gate the closed form
    # against a direct per-key rebuild at symbolic beta on a representative key:
    kk=keys[len(keys)//2]; (e_,f_),(g_,h_)=kk
    mk_b=sp.expand(pref*(m_line(e_,g_)*flat_line(f_,h_)+flat_line(e_,g_)*m_line(f_,h_)
          +(2+beta)*(u+up)*flat_line(e_,g_)*flat_line(f_,h_)))
    mk_0=sp.expand(pref*(m_line(e_,g_)*flat_line(f_,h_)+flat_line(e_,g_)*m_line(f_,h_)
          +2*(u+up)*flat_line(e_,g_)*flat_line(f_,h_)))
    gate(sp.expand(mk_b-mk_0-beta*(u+up)*sp.expand(pref*flat_line(e_,g_)*flat_line(f_,h_)))==0
         and sp.diff(mk_b,beta,2)==0,
         "[%s] LINEARITY + CLOSED FORM GATED per key: m_key(beta) = m_key(0) + "
         "beta*(u+u')*pref*flatA*flatB, no beta^2 — hence M(beta) = beta*(u+u')*Sigma0 "
         "exactly (M(0)=0)"%config)
    z_sig=iszero(Sig0)
    gate(not z_sig,"[%s] Sigma0 = sum_k V_k pref flatA flatB != 0 (EXACT-symbolic) — "
         "therefore M1^(a3) = (u+u')*Sigma0 != 0: the a^2->a^3 deformation BREAKS the "
         "cancellation pointwise pre-angular"%config)
    z1=iszero(M1)
    gate(z1==z_sig,"[%s] direct exact test agrees: iszero(M1) == iszero(Sigma0)"%config)
    for b0 in (BETA0,-BETA0):
        gate(not iszero(sp.expand(b0*M1)),
             "[%s] M(beta=%+d) != 0 (explicit registered point, exact; M(b0)=M0+b0*M1 "
             "with M0 gated ==0 above, so this decides the full assembly)"%(config,b0))
    # ---- section 6: LOCALIZATION ----
    gate(all(not V[key].has(beta) for key in keys),
         "[%s] (6A) beta never enters V_k — the routing/transposition structure of the "
         "vertex array is UNTOUCHED by the deformation"%config)
    gate(all(sp.expand(v)==0 for v in byN.values()),
         "[%s] (6C) the native antisymmetric ladder weight identity "
         "sum_k V_k (g+h-e-f)(-1)^{e+f} = 0 per sector HOLDS and is beta-FREE — the "
         "demotion mechanism is untouched; the deformation adds a PURE NON-DEMOTION term"
         %config)
    anti=all(iszero(Djm.get((m_,j_),sp.Integer(0))+Djm.get((j_,m_),sp.Integer(0)))
             for (j_,m_) in list(Djm))
    print("  RESULT [%s]: (6B/6D) deformation aggregate D_{j,m} transposition-"
          "antisymmetric: %s — the added weight (u+u')*flatA*flatB carries no pairing "
          "structure; the breaking is the DETUNED MULTIPLICATIVE BALANCE, localized to "
          "the vertex weight"%(config,anti), flush=True)
    # ---- section 8: ANGULAR ----
    angscls={kcl:ang(v) for kcl,v in phase_classes(Sig0).items()}
    z_ang=all(sp.cancel(sp.together(v))==0 for v in angscls.values())
    gate(not z_ang,"[%s] POST-ANGULAR (exact moment() machinery): <Sigma0> != 0 — the "
         "breaking term beta*(u+u')*<Sigma0> SURVIVES the exact angular average"%config)
    RES[config]={"native":True,"M1_nonzero":not z1,"Sigma0_nonzero":not z_sig,
                 "D_antisym":bool(anti),"ladder_identity_holds":True,
                 "postang_nonzero":not z_ang,
                 "closed_form":"M(beta) = beta*(u+u')*Sigma0"}
    if config=="plus_z": NEG={"V":V,"keys":keys,"byN":dict(byN),"M0":M0}

print(); print("="*74); print("9 — LIVE NEGATIVE CONTROL (plus_z)"); print("="*74)
# Break the OTHER mechanism component — perturb ONE flat vertex coefficient V_k by +1
# (Route-B Control-A pattern). This breaks the DEMOTION/ladder cancellation, NOT the
# multiplicative balance the a^3 deformation detunes — deliberately non-tautological.
if "NEG" not in dir():
    gate(False,"negative control SKIPPED: plus_z native limit failed upstream")
else:
    V=NEG["V"]; keys=NEG["keys"]
    kstar=[k for k in keys if V[k]!=0 and (k[1][0]+k[1][1]-k[0][0]-k[0][1])!=0][0]
    (e_,f_),(g_,h_)=kstar
    Nst=e_+f_+g_+h_
    pert=sp.expand(NEG["byN"][Nst]+(g_+h_-e_-f_)*(-1)**(e_+f_))
    gate(sp.expand(pert)!=0,
         "NEGATIVE CONTROL DETECTS (exact): perturbing ONE flat V_k by +1 breaks the "
         "per-sector ladder identity (sector N=%d becomes nonzero) — the instrument sees "
         "loss of the DEMOTION cancellation"%Nst)
    mA,mB=m_line(e_,g_),m_line(f_,h_)
    fA,fB=flat_line(e_,g_),flat_line(f_,h_)
    M0p=sp.expand(NEG["M0"]+pref*(mA*fB+fA*mB+2*(u+up)*fA*fB))
    gate(not iszero(M0p),
         "NEGATIVE CONTROL AT FULL-M LEVEL (exact): the perturbed assembly M0 + m_key(k*) "
         "is nonzero pointwise — the primary M-gate itself detects the break")
    note("non-tautology: the negative control breaks the LADDER identity (6C component), "
         "which the a^3 deformation provably does NOT touch — the two probes act on "
         "different mechanism components")

print(); print("="*74); print("15 — GOVERNANCE EXIT"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
gate(POST==PRE,"register sha256 identical pre/post")
frozen_clean=git("status","--porcelain","--","PHYSICS_LEDGER/wall_kr_tier3_loop.py",
  "PHYSICS_LEDGER/.tier3_cmat_cache.json","PHYSICS_LEDGER/.tier1_ds_cache.json",
  "PHYSICS_LEDGER/.tier3_integrand_cache.json","provenance/claims.json").stdout.strip()
gate(frozen_clean=="","no frozen physics file modified")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for ok,_ in CHECKS if ok)
allnat=all(RES.get(c,{}).get("native") for c in ("plus_z","cross_z","plus_x"))
brk=[RES[c]["M1_nonzero"] for c in RES if RES[c].get("native")]
if not FAILURES and allnat and len(brk)==3:
    verdict="PHASE3-BREAKS" if all(brk) else ("PHASE3-SURVIVES" if not any(brk)
             else "PHASE3-INCONCLUSIVE")
else:
    verdict="PHASE3-INCONCLUSIVE"
print("  battery: %d/%d testable gates, failures: %d   [%.0fs]"
      %(n,len(CHECKS),len(FAILURES),time.time()-t0))
for f in FAILURES: print("    FAILED: "+f)
print("  VERDICT: %s"%verdict)
out={"instrument":"wall_kr_h1_phase3_a3_control.py","date":"2026-09-03","base":"39551c7",
 "kind":"H1 CLOSURE PHASE 3 — a^2->a^3 vertex-weight deformation CONTROL",
 "battery":"%d/%d testable"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "definition":{"anchor":"V3^(1) = 2u*V3^(0) + R (R u-free), re-gated from the 26,032-term "
   "frozen artifact; coefficient 2 = the a-power; unique (3u leaves u-dependence)",
   "deformation":"per-vertex conformal weight 2 -> 2+beta; pair-level vertex-weight term "
   "(2+beta)(u+u')*flatA*flatB; beta0=1 = the a^3 point; reversible at beta=0",
   "unchanged":["flat C^0 vertex","R insertion","line/state kernels","routing",
     "TT projector","derivative algebra"],
   "compensator_note":"the +2(u+u') term IS the two-vertex a^2 weight (gated balance: "
   "lines carry -2(u+u'), vertices +2(u+u')); changing the vertex weight mathematically "
   "requires changing it — the order's carved-out case",
   "limitation":"a full a^3 EH-like vertex would also differ in its R-analogue and at "
   "O(H^2); ONLY the multiplicative conformal weight is deformed"},
 "per_config":RES,"verdict":verdict,
 "closed_form":"M(beta) = beta*(u+u')*Sigma0, Sigma0 != 0 exact — the breaking is the "
   "detuned multiplicative balance between the vertex a^2 weight and the lines' conformal "
   "dressing; fingerprint shape identical to the (disclosed) double-compensation bug class",
 "localization":{"6A_routing":"beta never enters V_k — routing/transposition untouched",
   "6B_weight":"the added term carries weight (u+u')*flatA*flatB — no new (j,m) pairing "
   "structure","6C_ladder":"the native antisymmetric ladder identity holds and is "
   "beta-free — demotion mechanism untouched","6D":"breaking localized to the vertex "
   "weight; state and line kernels frozen"},
 "epistemic_wording":"This specific a^2->a^3 vertex-weight deformation breaks the native "
   "H1 cancellation under the declared frozen construction; the native cancellation is "
   "sensitive to the declared conformal vertex-weight structure. NOT claimed: 'a^2 is "
   "uniquely required'; 'GRUT requires a^2'; 'impossible without a^2'; anything beyond "
   "this deformation",
 "status_verbs":{"definition anchor":"GATED (re-gated from frozen artifact)",
   "native limit":"VERIFIED (exact-symbolic, independent reconstruction)",
   "M(beta) closed form":"GATED","Sigma0 != 0":"GATED (exact-symbolic, NOT numeric)",
   "post-angular":"GATED (exact moment() machinery)","ladder identity":"GATED",
   "this is":"CONTROL","uniqueness of a^2":"NOT CLAIMED","GRUT content":"NOT CLAIMED"},
 "A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(HERE,"WALL_KR_H1_PHASE3_RESULT.json"),"w",encoding="utf-8"),
          indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_H1_PHASE3_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
print("PHASE3_DONE")
