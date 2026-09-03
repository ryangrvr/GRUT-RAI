#!/usr/bin/env python3
"""
H1 CLOSURE — PHASE 2: alpha-vacuum-like O(H) STATE DEFORMATION CONTROL.
Question (narrow, per the order): is the H1 cancellation dependent on the particular O(H)
state ingredient of the native construction?  This is a CONTROL — not a replacement state,
not a licence to modify frozen inputs, not a theorem stage.

DEFORMATION (defined before computing, section 2):
    native BD mode      h(u)      = e^{-iqu} [ (1-Hu) + iH/q ]
    deformed mode       h_a(u)    = h(u) + alpha (H/q) hbar(u)         (Bogoliubov-like
                                    mixing whose coefficient is EXPLICITLY O(H))
    deformation param   alpha     : real, dimensionless, SYMBOLIC (alpha0 = 1 registered)
    native O(H) state term in the pair kernel  = 0   (the +-iH/q pieces cancel; gated)
    deformed O(H) state term in the pair kernel = alpha H (kap^2/q^2)
                                    ( e^{+iq(u+u')} + e^{-iq(u+u')} )  (derived from the
                                    modes in-run; gated)
    products changed    : BOTH internal line kernels (the state feeds every line)
    unchanged           : flat kernel, conformal dressing, vertex, projector, routing,
                          derivative algebra, compensator, angular machinery, htrunc
    reversible          : alpha -> 0 recovers the native pair identically (gated)
    order-pure          : the alpha^2 pair term is O(H^2), killed by htrunc (gated) —
                          M(alpha) is EXACTLY linear in alpha at O(H) (gated)
This is an "alpha-vacuum-LIKE O(H) state deformation control": a true dS alpha-vacuum
carries a CONSTANT Bogoliubov angle; nothing here is claimed about that family.
Route-B construction (independent: no B_mixed, no Phase-1 swap relation as input).
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
# ZERO-DECISION PROCEDURE (re-representation, 20-minute rule): every expression this
# instrument tests lives in the ring  polynomials(u,u',q,om,n,kap) x exp(i * linear form).
# Merge phases (powsimp force merges exp(a)exp(b)->exp(a+b), always valid), group terms by
# the CANONICALIZED exponent, and decide each phase-class coefficient at expand level.
# Distinct exponentials of distinct linear forms are linearly independent over the
# polynomial coefficients, so this is sound AND complete in both directions for this
# family — no simplify() heuristics. (The first run's simplify-based test agreed on every
# verdict it completed but stalled >40 min on the negative control; re-represented per the
# standing rule. Self-checks below include the exp(a)exp(-a) phase-merging trap.)
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
            dcls=phase_classes(den)   # a denominator in this family is single-phase
            assert len(dcls)==1,"multi-phase denominator: %s"%den
            (kd,cd),=dcls.items()
            karg-=kd; den=cd
        key=sp.expand(karg)
        classes[key]=classes.get(key,sp.Integer(0))+sp.Mul(*co_n)/den
    return classes
def iszero(e):
    # complete for this family: rational-function coefficients per phase class, distinct
    # linear-form exponentials independent over them
    return all(sp.cancel(sp.together(v))==0 for v in phase_classes(e).values())
def accum(acc,e):
    """fold e into a running {phase_arg: coeff} dict WITHOUT ever forming the giant sum —
    keeps the per-term work bounded; used where the assembled sum would be too large to
    re-expand (the negative control stalled >40 min doing exactly that)."""
    for kcl,v in phase_classes(e).items():
        acc[kcl]=acc.get(kcl,sp.Integer(0))+v
    return acc
def classes_nonzero(acc):
    return any(sp.cancel(sp.together(v))!=0 for v in acc.values())

print("="*74); print("0 — GOVERNANCE + DECISION-PROCEDURE SELF-CHECKS"); print("="*74)
_u,_q=sp.symbols("selfchk_u selfchk_q")
gate(iszero(sp.exp(sp.I*_q*_u)*sp.exp(-sp.I*_q*_u)-1),
     "self-check: the exp(a)exp(-a)=1 phase-merging trap decides ZERO correctly")
gate(not iszero(sp.exp(-sp.I*_q*_u)) and not iszero(_u*sp.exp(sp.I*_q*_u)-_u),
     "self-check: nonzero expressions decide NONZERO (incl. mixed phase/no-phase)")
gate(iszero((_u+1)**2-_u**2-2*_u-1),"self-check: pure polynomial zero decides ZERO")
HEAD=git("rev-parse","HEAD").stdout.strip(); ov4=git("rev-parse","origin/v4").stdout.strip()
gate(HEAD!="" and HEAD==ov4,"v4 by REF IDENTITY: HEAD == origin/v4 == %s"%HEAD[:12])
gate(git("merge-base","--is-ancestor","bedc989","HEAD").returncode==0,
     "bedc989 (reconciled Phase 1) in ancestry — by RETURNCODE")
t3sha=hashlib.sha256(open(os.path.join(HERE,"wall_kr_tier3_loop.py"),"rb").read()).hexdigest()
gate(t3sha.startswith("1c72272b"),"frozen T3 machinery sha 1c72272b... unchanged")
note("A-F remain UNSELECTED; W-0; Phase 1 NOT reopened; Phase 3 NOT run; no H1-THEOREM-A/B/C")

print(); print("="*74); print("1 — LOAD FROZEN MACHINERY (non-state ingredients fixed)"); print("="*74)
src=open(os.path.join(HERE,"wall_kr_tier3_loop.py"),encoding="utf-8").read()
M={"__name__":"frozen_t3","__file__":os.path.join(HERE,"wall_kr_tier3_loop.py")}
argv0=sys.argv; sys.argv=["x","machinery_only"]; os.chdir(HERE)
try: exec(compile(src,"t3","exec"),M)
except SystemExit: pass
sys.argv=argv0
CM,cdecomp,Ptt,htrunc=M["CM"],M["cdecomp"],M["Ptt"],M["htrunc"]
H,u,up,om,q,kap=M["H"],M["u"],M["up"],M["om"],M["q"],M["kap"]
n1,n2,n3=M["n1"],M["n2"],M["n3"]; PAIRS=M["PAIRS"]; dsym=M["dsym"]
alpha=sp.Symbol("alpha",real=True)
# NUMERIC WITNESS (for the "is this expression NOT identically zero?" gates only): a
# symbolic expression that is nonzero at even one rational point is provably not identically
# zero. Evaluating at fixed points costs microseconds and needs NO symbolic cancellation —
# the right tool for the negative control (whose broken-kernel coefficients made the exact
# per-phase-class cancellation cost >50 min; disclosed). Three seeds guard against landing
# on an accidental root. Only ever used to CONFIRM nonzero, never to certify zero.
KNOWN={u,up,om,q,kap,n1,n2,n3,dsym}
def witness_nonzero(term_of_key,keys):
    seen_extra=set()
    for seed in range(3):
        sub={u:sp.Rational(3+seed,7),up:sp.Rational(2+seed,11),q:sp.Rational(1,2+seed),
             om:sp.Rational(1,3+seed),kap:sp.Integer(1),dsym:sp.Integer(3),
             n1:sp.Rational(2,5),n2:sp.Rational(1,4),n3:sp.Rational(1,3)}
        tot=0j
        for key in keys:
            t=term_of_key(key); seen_extra|=(t.free_symbols-KNOWN)
            tot+=complex(sp.N(t.subs(sub)))
        assert not seen_extra,"witness: unexpected free symbols %s"%seen_extra
        if abs(tot)>1e-9: return True
    return False
note("FIXED: flat C^0 EH vertex, TT contraction, routing, derivative algebra, external "
     "configs, conformal dressing, compensator, symbolic d/q/n-hat, pre-angular evaluation")

print(); print("="*74); print("2 — THE DEFORMATION, DERIVED FROM THE MODES"); print("="*74)
kk_=sp.Symbol('k',positive=True)
h_  = sp.exp(-sp.I*kk_*u )*((1-H*u ) + sp.I*H/kk_)
hb_ = sp.exp( sp.I*kk_*up)*((1-H*up) - sp.I*H/kk_)
pair_native=htrunc(sp.expand(h_*hb_).xreplace({H**3:0}))
# native O(H) state term = 0 (the +-iH/k mode pieces cancel at O(H)):
conf_oh=sp.expand(sp.exp(-sp.I*kk_*(u-up))*(-(u+up)))
gate(sp.expand(sp.expand(h_*hb_).coeff(H,1)-conf_oh)==0,
     "NATIVE O(H) STATE TERM = 0 (gated): coeff(H,1) of h(u)h*(u') is PURELY CONFORMAL "
     "-(u+u') e^{-ik(u-u')} — the BD +-iH/k state pieces cancel between the two factors")
# deformed mode and pair:
hbu_ = sp.exp( sp.I*kk_*u )*((1-H*u ) - sp.I*H/kk_)   # conjugate mode at u
hup_ = sp.exp(-sp.I*kk_*up)*((1-H*up) + sp.I*H/kk_)   # mode at u'
ha_  = h_  + alpha*(H/kk_)*hbu_
hab_ = hb_ + alpha*(H/kk_)*hup_                        # = conj(h_a)(u') for real alpha
pair_a=sp.expand(ha_*hab_)
gate(sp.expand(pair_a.subs(alpha,0)-sp.expand(h_*hb_))==0,
     "REVERSIBLE (gated): alpha -> 0 recovers the native pair identically")
dstate=sp.expand(pair_a.coeff(H,1)-sp.expand(h_*hb_).coeff(H,1))
gate(sp.expand(dstate-alpha*(sp.exp(sp.I*kk_*(u+up))+sp.exp(-sp.I*kk_*(u+up)))/kk_)==0,
     "DEFORMED O(H) STATE TERM DERIVED from the mode product rule: the pair acquires "
     "alpha (H/k)( e^{+ik(u+u')} + e^{-ik(u+u')} ) at O(H) and nothing else")
gate(sp.expand(pair_a.coeff(H,0)-sp.expand(h_*hb_).coeff(H,0))==0,
     "O(H)-PURE (gated): the deformation does NOT touch the flat O(H^0) pair")
gate(all(sp.expand(sp.expand(pair_a.coeff(alpha,2)).coeff(H,hp))==0 for hp in (0,1)),
     "LINEAR (gated): the alpha^2 pair term is O(H^2) — outside the tested order; "
     "normalization correction likewise O(alpha^2 H^2)")
# W-level deformation, in the frozen kernel normalization (kap^2/q) x pair(k->q):
Wf=(kap**2/q)*sp.exp(-sp.I*q*(u-up))
dress=1-H*(u+up)
Wdressed=sp.expand(Wf*dress)
sdef=(kap**2/q**2)*(sp.exp(sp.I*q*(u+up))+sp.exp(-sp.I*q*(u+up)))
gate(sp.expand((kap**2/q)*dstate.xreplace({kk_:q})-alpha*sdef)==0,
     "W-LEVEL FORM (gated): the deformed line kernel is W_a = W_flat(1-H(u+u')) "
     "+ alpha H (kap^2/q^2)( e^{+iq(u+u')} + e^{-iq(u+u')} ) + O(H^2)")
def wop(e,a,c):
    for _ in range(a): e=-sp.I*sp.diff(e,u)
    for _ in range(c): e=-sp.I*sp.diff(e,up)
    return sp.expand(e)
def m_line(a,c):  return sp.expand(wop(Wdressed,a,c).coeff(H,1))
def flat_line(a,c): return sp.expand(wop(Wf,a,c))
def dm_line(a,c): return sp.expand(wop(sdef,a,c))   # the alpha-part of the O(H) residual
pref=sp.Rational(1,2)/(2*kap**2)**2
ALPHA0=1
note("alpha0 REGISTERED = %d (dimensionless); alpha kept SYMBOLIC throughout"%ALPHA0)

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

RES={}
for config in ("plus_z","cross_z","plus_x"):
    print(); print("="*74)
    print("3-7 [%s] — NATIVE LIMIT, DEFORMED CASE, LOCALIZATION"%config); print("="*74)
    V=build_V(config); keys=sorted(V,key=str)
    note("[%s] %d native routing keys, V_k from flat C^0   [%.0fs]"
         %(config,len(keys),time.time()-t0))
    M0=sp.Integer(0); M1=sp.Integer(0)
    Ajm0=defaultdict(lambda: sp.Integer(0)); Ajm1=defaultdict(lambda: sp.Integer(0))
    Ap=defaultdict(lambda: sp.Integer(0)); Am=defaultdict(lambda: sp.Integer(0))
    Sig0=sp.Integer(0)
    for key in keys:
        (e_,f_),(g_,h_)=key
        mA,mB=m_line(e_,g_),m_line(f_,h_)
        fA,fB=flat_line(e_,g_),flat_line(f_,h_)
        dA,dB=dm_line(e_,g_),dm_line(f_,h_)
        m0=sp.expand(pref*(mA*fB+fA*mB+2*(u+up)*fA*fB))   # native (compensator ONCE)
        m1=sp.expand(pref*(dA*fB+fA*dB))                  # complete alpha-part at O(H)
        M0+=sp.expand(V[key]*m0); M1+=sp.expand(V[key]*m1)
        j_,mm_=e_+f_,g_+h_
        Ajm0[(j_,mm_)]+=sp.expand(V[key]*m0); Ajm1[(j_,mm_)]+=sp.expand(V[key]*m1)
        N_=e_+f_+g_+h_
        Ap[N_]+=sp.expand(V[key]*((-1)**e_+(-1)**f_))
        Am[N_]+=sp.expand(V[key]*(-1)**(e_+f_)*((-1)**g_+(-1)**h_))
        Sig0+=sp.expand(V[key]*pref*fA*fB)
    # ---- section 4: NATIVE LIMIT FIRST ----
    ok0=iszero(M0)
    gate(ok0,"[%s] NATIVE LIMIT VERIFIED: M(alpha=0) == 0 pointwise pre-angular, "
         "reconstructed independently (no B_mixed, no Phase-1 swap relation)   [%.0fs]"
         %(config,time.time()-t0))
    if not ok0:
        note("[%s] STOP per section 4 — native limit failed; deformed case NOT evaluated"
             %config)
        RES[config]={"native":False}; continue
    # ---- section 5: DEFORMED CASE, alpha symbolic ----
    z1=iszero(M1)
    Ma=sp.expand(M0+alpha*M1)   # exact: linearity gated at the pair level above
    gate(iszero(Ma.subs(alpha,0)),"[%s] M(alpha=0) == 0 (explicit point)"%config)
    for a0 in (ALPHA0,-ALPHA0):
        za=iszero(Ma.subs(alpha,a0))
        gate(za==z1,"[%s] M(alpha=%+d) %s — consistent with the symbolic M1 verdict"
             %(config,a0,"== 0" if za else "!= 0"))
    print("  RESULT [%s]: M(alpha) = alpha * M1 with M1 %s"
          %(config,"IDENTICALLY ZERO" if z1 else "NONZERO"), flush=True)
    # ---- section 6: LOCALIZATION, independent of the M sum ----
    # (i) the vertex S-array carries NO state input: alpha cannot enter it (checked by
    #     construction: V built from C^0 only; gate = V has no alpha):
    gate(all(not V[key].has(alpha) for key in keys),
         "[%s] the vertex array (hence the Phase-1 swap relation) is STATE-INDEPENDENT: "
         "alpha does not enter V_k — the deformation CANNOT break F1 itself"%config)
    # (ii) the meaningful deformed analogue: transposition behavior of the (j,m)-resolved
    #      aggregates. Native part: antisymmetric (observable, not input).
    gate(all(iszero(Ajm0.get((mm_,j_),sp.Integer(0))+Ajm0.get((j_,mm_),sp.Integer(0)))
             for (j_,mm_) in list(Ajm0)),
         "[%s] native (j,m)-aggregate A0 is transposition-ANTISYMMETRIC (observable) — "
         "the Phase-1 pairing mechanism operates in the native object"%config)
    anti1=all(iszero(Ajm1.get((mm_,j_),sp.Integer(0))+Ajm1.get((j_,mm_),sp.Integer(0)))
              for (j_,mm_) in list(Ajm1))
    print("  RESULT [%s]: alpha-part (j,m)-aggregate A1 transposition-antisymmetric: %s"
          %(config,anti1), flush=True)
    # (iii) propagator-free reduction of M1 (consistency + localization):
    Xp2=sp.exp(sp.I*q*(2*up)); Xm2=sp.exp(-sp.I*q*(2*u))
    Mrep=sp.Integer(0)
    for N_ in sorted(set(Ap)|set(Am)):
        Mrep+=sp.expand(pref*(kap**4/q**3)*q**N_*(Ap.get(N_,0)*Xp2+Am.get(N_,0)*Xm2))
    repdiff=phase_classes(sp.expand(M1-Mrep))
    badcls=[str(kcl) for kcl,v in repdiff.items() if sp.cancel(sp.together(v))!=0]
    gate(not badcls,
         "[%s] M1 REPRESENTATION (gated): M1 = pref (kap^4/q^3) sum_N q^N "
         "[ A+_N e^{2iqu'} + A-_N e^{-2iqu} ], with A+_N = sum V_k((-1)^e+(-1)^f), "
         "A-_N = sum V_k(-1)^{e+f}((-1)^g+(-1)^h) — NO derivative demotion occurs on the "
         "state term, so the (g+h-e-f) ladder weight NEVER FORMS for it"%config)
    if badcls:
        print("  DIAG [%s]: nonzero phase classes of M1-Mrep: %s"%(config,badcls),flush=True)
    apz={N_:iszero(Ap[N_]) for N_ in sorted(Ap)}; amz={N_:iszero(Am[N_]) for N_ in sorted(Am)}
    print("  RESULT [%s]: A+_N zero-by-sector: %s"%(config,apz), flush=True)
    print("  RESULT [%s]: A-_N zero-by-sector: %s"%(config,amz), flush=True)
    gate(z1==(all(apz.values()) and all(amz.values())),
         "[%s] M1 verdict consistent with the sector reduction"%config)
    RES[config]={"native":True,"M1_zero":z1,"A1_antisym":anti1,
                 "Aplus_zero":{str(a):b for a,b in apz.items()},
                 "Aminus_zero":{str(a):b for a,b in amz.items()},
                 "Sigma0_nonzero":not iszero(Sig0)}
    if config=="plus_z":
        NEG={"V":V,"keys":keys,"Sig0":Sig0}

print(); print("="*74); print("8 — LIVE NEGATIVE CONTROL (plus_z)"); print("="*74)
# Deliberately break the state-PAIR symmetry: W_neg = W_flat (1 - 2Hu) — ALL O(H) weight on
# the u endpoint. NOT realizable by any single-mode deformation (a mode deformation always
# dresses the pair as g(u) + g(u')-symmetric via h(u)h*(u')); it violates exactly the pair
# symmetry the product rule guarantees natively. Detectability precondition Sigma0 != 0 is
# gated, so this control CAN fail and its failure is DETECTED, not assumed.
if "NEG" not in dir():
    gate(False,"negative control SKIPPED: plus_z native limit failed upstream (section-4 STOP)")
else:
    V=NEG["V"]; keys=NEG["keys"]
    gate(not iszero(NEG["Sig0"]),
         "precondition: Sigma0 = sum V_k pref flatA flatB != 0 — the u'-linear part of the "
         "broken construction cannot cancel; the negative control is CAPABLE of failing")
    Wneg=sp.expand(Wf*(1-2*H*u))
    _mnegc={}
    def m_neg(a,c):
        if (a,c) not in _mnegc: _mnegc[(a,c)]=sp.expand(wop(Wneg,a,c).coeff(H,1))
        return _mnegc[(a,c)]
    def neg_term(key):
        (e_,f_),(g_,h_)=key
        nA,nB=m_neg(e_,g_),m_neg(f_,h_); fA,fB=flat_line(e_,g_),flat_line(f_,h_)
        return V[key]*pref*(nA*fB+fA*nB+2*(u+up)*fA*fB)
    gate(witness_nonzero(neg_term,keys),
         "NEGATIVE CONTROL DETECTS: breaking the state-pair symmetry (all O(H) dressing on "
         "the u endpoint) gives M_neg != 0 (numeric witness) — the instrument can see loss "
         "of the cancellation")
    # diagnostic (reported, not a negative control): sign-broken Bogoliubov pair
    # W = W_flat(1-H(u+u')) + alpha H (kap^2/q^2)(e^{+iq(u+u')} - e^{-iq(u+u')}):
    sneg=(kap**2/q**2)*(sp.exp(sp.I*q*(u+up))-sp.exp(-sp.I*q*(u+up)))
    _sgnc={}
    def dsg(a,c):
        if (a,c) not in _sgnc: _sgnc[(a,c)]=sp.expand(wop(sneg,a,c))
        return _sgnc[(a,c)]
    def sgn_term(key):
        (e_,f_),(g_,h_)=key
        dA,dB=dsg(e_,g_),dsg(f_,h_); fA,fB=flat_line(e_,g_),flat_line(f_,h_)
        return V[key]*pref*(dA*fB+fA*dB)
    note("diagnostic: hermiticity-sign-broken Bogoliubov pair gives M_sign %s (numeric "
         "witness; reported only — it probes the SAME A+/A- sums as the primary control, "
         "so it is NOT used as the negative control)"
         %("!= 0" if witness_nonzero(sgn_term,keys) else "== 0"))

print(); print("="*74); print("12 — GOVERNANCE EXIT"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
gate(POST==PRE,"register sha256 identical pre/post")
frozen_clean=git("status","--porcelain","--","wall_kr_tier3_loop.py",
                 ".tier3_cmat_cache.json",".tier1_ds_cache.json",
                 ".tier3_integrand_cache.json").stdout.strip()
gate(frozen_clean=="","no frozen physics file modified (git status clean on the frozen set)")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for ok,_ in CHECKS if ok)
allnat=all(RES.get(c,{}).get("native") for c in ("plus_z","cross_z","plus_x"))
allz=[RES[c]["M1_zero"] for c in RES if RES[c].get("native")]
if not FAILURES and allnat and len(allz)==3:
    verdict="PHASE2-SURVIVES" if all(allz) else ("PHASE2-BREAKS" if not any(allz)
             else "PHASE2-INCONCLUSIVE")
else:
    verdict="PHASE2-INCONCLUSIVE"
print("  battery: %d/%d testable gates, failures: %d   [%.0fs]"
      %(n,len(CHECKS),len(FAILURES),time.time()-t0))
for f in FAILURES: print("    FAILED: "+f)
print("  VERDICT: %s"%verdict)
out={"instrument":"wall_kr_h1_phase2_alpha_control.py","date":"2026-09-03","base":"bedc989",
 "kind":"H1 CLOSURE PHASE 2 — alpha-vacuum-like O(H) state deformation CONTROL",
 "battery":"%d/%d testable"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "deformation":{"mode":"h_a(u) = h(u) + alpha (H/q) hbar(u)","alpha":"real, symbolic",
   "alpha0_registered":ALPHA0,
   "native_OH_state_term":"0 (BD +-iH/q pieces cancel at O(H); gated)",
   "deformed_OH_state_term":"alpha H (kap^2/q^2)(e^{+iq(u+u')}+e^{-iq(u+u')}) per line "
     "(derived from mode product rule; gated)",
   "changed":"both internal line kernels","unchanged":["flat kernel","conformal dressing",
     "vertex","projector","routing","derivative algebra","compensator",
     "angular machinery"],
   "naming":"alpha-vacuum-LIKE (mixing coefficient explicitly O(H)); NOTHING claimed "
     "about the constant-angle dS alpha-vacuum family"},
 "per_config":RES,"verdict":verdict,
 "status_verbs":{"M(alpha)=alpha*M1 linearity":"GATED (pair-level)",
   "native limit M(0)=0":"VERIFIED (independent reconstruction)",
   "M1 pointwise value":"GATED per config","swap relation under deformation":
   "STATE-INDEPENDENT by construction (V_k carries no alpha; gated)",
   "A1 transposition behavior":"GATED observable","this is":"CONTROL",
   "H1-THEOREM-A/B/C":"NOT CLAIMED","alpha-vacuum family":"NOT CLAIMED",
   "GRUT content":"NOT CLAIMED"},
 "A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(HERE,"WALL_KR_H1_PHASE2_RESULT.json"),"w",encoding="utf-8"),
          indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_H1_PHASE2_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
print("PHASE2_DONE")
