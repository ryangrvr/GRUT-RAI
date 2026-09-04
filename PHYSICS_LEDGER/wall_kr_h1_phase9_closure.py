#!/usr/bin/env python3
"""
H1 CAMPAIGN — PHASE 9: CLOSURE MEMORANDUM / FINAL EPISTEMIC FREEZE.
Not a new physics calculation. This instrument (a) verifies governance, (b) re-anchors
the four-channel exhaustion of the frozen O(H) object one final time, and (c) gates that
the closure memorandum carries every element the order requires (channel table, the four
levels uncollapsed, R = CLOSED-AS-GATED, the quantified statement, the subtraction and
no-GRUT-premise sentence, the can/cannot-test rule, the open-items register, the freeze
declaration). Read-only. Phases 1-8 CLOSED. A-F unselected. W-0.
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
              ("016d84b","P5"),("b10c4d9","P6"),("d44bfd2","P7"),("c90d684","P8")):
    gate(git("merge-base","--is-ancestor",c_,"HEAD").returncode==0,
         "%s (%s) in ancestry — by RETURNCODE"%(c_,nm))
t3sha=hashlib.sha256(open(os.path.join(HERE,"wall_kr_tier3_loop.py"),"rb").read()).hexdigest()
gate(t3sha.startswith("1c72272b"),"frozen T3 machinery sha 1c72272b... unchanged")
note("A-F UNSELECTED; W-0; nothing banked; Phase 10 NOT started; no new physics below")

print(); print("="*74); print("2 — THE FOUR CHANNELS EXHAUST THE O(H) OBJECT (final re-anchor)")
print("="*74)
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
     "S: identity-level zero (re-anchored)")
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
# EXHAUSTION at the entry level: the O(H) grading of every C entry is EXACTLY the
# 2u-weight (W) plus the u-free remainder R (R-channel) — nothing else exists:
# DISCLOSED (adversarial Leg A, adopted at source): the first draft "gated" the identity
# C1 == 2u*C0 + R. Since R is DEFINED as C1 - 2u*C0, that identity is TRUE BY
# CONSTRUCTION — the leg proved the check passes on random junk entries and on a
# deliberately wrong 7u dressing. It carried zero evidence. It is demoted to a note, and
# replaced below by the three facts that actually give the W|R split its content.
note("BY CONSTRUCTION (not a gate): C1 == 2u*C0 + R holds definitionally, since R := "
     "C1 - 2u*C0. Demoted from the first draft's gate per Leg A — the substantive "
     "content is gated in the three checks that follow")
# (1) SUBSTANTIVE: R is u-FREE — this is what makes the split meaningful, licenses
#     'R is not absorbed into W', and (with C0 u-free and nonzero) pins the weight to 2.
ok_ufree=True; ok_pin=True; nR={}
for cfg in ("plus_z","cross_z","plus_x","ward"):
    cnt=0
    for ck,vv in CM[cfg].items():
        if ck=="meta": continue
        ee=sp.sympify(vv); c0=ee.subs(H,0)
        r_=sp.expand(ee.coeff(H,1)-2*u*c0)
        if r_!=0:
            cnt+=1
            if r_.has(u): ok_ufree=False
        # the coefficient is pinned: c != 2 leaves a u-DEPENDENT remainder whenever
        # C0 != 0 (C0 is u-free), so 2 is the unique u-stripping weight
        if c0!=0:
            for c_ in (1,3):
                if not sp.expand(ee.coeff(H,1)-c_*u*c0).has(u): ok_pin=False
    nR[cfg]=cnt
gate(ok_ufree,
     "SUBSTANTIVE (replaces the tautology): the vertex-grading remainder R is u-FREE in "
     "EVERY entry of ALL FOUR cache configurations (nonzero-R entries %s) — R is "
     "therefore a genuinely different structure from the u-linear weight channel, which "
     "is what licenses 'R is NOT absorbed into W' and P4's u-degree separation"
     %{k:v for k,v in nR.items()})
gate(ok_pin,
     "SUBSTANTIVE: the weight coefficient 2 is PINNED by the same fact — c = 1 and c = 3 "
     "both leave a u-DEPENDENT remainder (C^0 is u-free and nonzero), so 2 is the unique "
     "u-stripping weight; the '2' the W channel uses is re-anchored here, not hard-coded")
# (2) SUBSTANTIVE: the assembly is H-FREE and multilinear, so Leibniz gives exactly
#     C1*flat*flat + C0*(m_A flat_B + flat_A m_B) and NOTHING ELSE at O(H).
asm_H=[Ptt(1,1,1,1),Ptt(1,2,1,3),M["moment"]((2,0,0)),M["moment"]((0,2,2)),pref]
gate(not any(sp.sympify(x).has(H) for x in asm_H),
     "SUBSTANTIVE: the assembly carries NO H — projector entries, angular moments and "
     "the prefactor are all H-free (sampled and checked) — so the O(H) part of "
     "(C)x(line)x(line) is EXACTLY C1*flat*flat + C0*(m_A flat_B + flat_A m_B) by "
     "multilinearity: with the vertex side split W|R (u-linear | u-free) and the line "
     "side split into dressing + state term (state term ZERO, gated above), the four "
     "channels EXHAUST the declared O(H) object")
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
ok_w=True; byN=defaultdict(lambda: sp.Integer(0))
for key,vv in V.items():
    (e_,f_),(g_,h_)=key
    mA,mB=m_line(e_,g_),m_line(f_,h_)
    fA,fB=flat_line(e_,g_),flat_line(f_,h_)
    dA,dB=dem_line(e_,g_),dem_line(f_,h_)
    if sp.expand(pref*(mA*fB+fA*mB+2*(u+up)*fA*fB)-pref*(dA*fB+fA*dB))!=0: ok_w=False
    byN[e_+f_+g_+h_]+=sp.expand(vv*(g_+h_-e_-f_)*(-1)**(e_+f_))
note("BY CONSTRUCTION (not a gate, per Leg A): the per-key balance dA*fB + fA*dB == "
     "mA*fB + fA*mB + 2(u+up)*fA*fB is Leibniz-automatic given dem_line := m_line + "
     "(u+up)*flat_line — the leg showed it passes even with a wrong 1-H(3u+5up) "
     "dressing. W's real anchors are the coefficient-2 pinning above and P3/P5; "
     "consistency value only: %s"%ok_w)
gate(all(sp.expand(v)==0 for v in byN.values()),
     "L: Lambda_N == 0 per sector (SUBSTANTIVE re-anchor, plus_z; three-config coverage "
     "INHERITED from P4/P6 by citation, not recomputed here)")
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
     "R: Sigma_R == 0 (SUBSTANTIVE re-anchor, plus_z; all-three-config coverage "
     "INHERITED from P4 by citation)   [%.0fs]"%(time.time()-t0))
# THE GAP LEG A FOUND AND CLOSED: the sec.6 Domain's polarization clause governs the
# FULL four-channel statement, but P7's (a,b) gate covers the LADDER leg only. R's
# mixed plus-x-cross terms were gated NOWHERE in P1-P8. Gated here:
EC={}
for ck,vv in CM["cross_z"].items():
    if ck=="meta": continue
    ee=sp.sympify(vv); c0=ee.subs(H,0)
    if c0!=0: EC[ck]=sp.expand(c0.xreplace(qsub))
EC1={}
for ck,vv in CM["cross_z"].items():
    if ck=="meta": continue
    ee=sp.sympify(vv)
    r_=sp.expand(ee.coeff(H,1)-2*u*ee.subs(H,0))
    if r_!=0: EC1[ck]=sp.expand(r_.xreplace(qsub))
D10c={ck:dec(E) for ck,E in EC.items()}; D20c={ck:decT(E) for ck,E in EC.items()}
D1Rc={ck:dec(E) for ck,E in EC1.items()}; D2Rc={ck:decT(E) for ck,E in EC1.items()}
def sigR_of(DA_R,DB_0,DA_0,DB_R):
    S_=sp.Integer(0)
    for (DA,DB) in ((DA_R,DB_0),(DA_0,DB_R)):
        for key,vv in build(DA,DB).items():
            (e_,f_),(g_,h_)=key
            S_+=sp.expand(vv*pref*flat_line(e_,g_)*flat_line(f_,h_))
    return S_
SigR_pc=sigR_of(D1R,D20c,D10,D2Rc)
SigR_cp=sigR_of(D1Rc,D20,D10c,D2R)
z_pc=all(sp.cancel(sp.together(v))==0 for v in phase_classes(SigR_pc).values())
z_cp=all(sp.cancel(sp.together(v))==0 for v in phase_classes(SigR_cp).values())
gate(z_pc and z_cp,
     "R MIXED-POLARIZATION GATE (new; the gap Leg A identified): Sigma_R(plus,cross) == "
     "0 AND Sigma_R(cross,plus) == 0 exactly — so the R channel, unlike the ladder "
     "(whose mixed blocks are individually NONZERO and cancel only in the sum), "
     "vanishes blockwise. The full four-channel statement therefore extends to the "
     "arbitrary TT superposition a*plus + b*cross at probe direction z — previously "
     "ASSUMED by the Domain clause, now GATED   [%.0fs]"%(time.time()-t0))

print(); print("="*74); print("MEMORANDUM CONTENT GATES"); print("="*74)
mdp=os.path.join(HERE,"WALL_KR_H1_PHASE9_CLOSURE.md"); md=open(mdp,encoding="utf-8").read()
# whitespace-normalize AND strip blockquote markers: line-wrapped quote gates are a
# known trap, and "> " continuation markers land inside wrapped fragments
md=" ".join(md.replace(">"," ").split())
for frag,desc in (
  ("F_{\\text{state}} + F_{\\text{weight}} + F_{\\text{ladder}} + F_R",
   "the four-channel equation is stated"),
  ("EXHAUST","channel exhaustion asserted (and re-anchored above)"),
  ("LEVEL I","Level I present"),("LEVEL II","Level II present"),
  ("LEVEL III","Level III present"),
  ("LEVEL IV — GRUT: NO GRUT-SPECIFIC CONSEQUENCE ESTABLISHED",
   "Level IV states the legitimate negative result"),
  ("CLOSED-AS-GATED","the R channel classified CLOSED-AS-GATED"),
  ("NOT derived from the Level-II theorem","R non-promotion sentence present"),
  ("H¹ CLOSURE THEOREM","the final quantified statement present"),
  ("NOT generalized:","the not-generalized list inside the theorem"),
  ("No GRUT-specific premise occurs in the H¹ ancestry",
   "the subtraction conclusion stated verbatim"),
  ("not a proof of absence","the search-verdict qualifier RESTORED (Leg A)"),
  ("benchmark classification","framed as a benchmark classification"),
  ("COMPUTED IDENTITY","the R5 downgrade from 'consistency requirement' adopted"),
  ("NOT a discriminator in favor of GRUT","the cannot-test rule stated"),
  ("must not be cited as evidence for GRUT in ANY downstream record",
   "R2: the loophole deleted and covered forms widened"),
  ("PROPOSED STANDING RULE — AWAITING OWNER RATIFICATION",
   "R3: authority correctly marked, not self-conferred"),
  ("has left the frozen scope and is not thereby a GRUT discriminator either",
   "R1: the scope contradiction closed in both directions"),
  ("one gated-only and underived (R)","R4: the channel count stated correctly"),
  ("NON-FALSIFIABLE","the two tautological gates DISCLOSED at source"),
  ("u-freeness","R's u-freeness — the substantive replacement fact — is in the record"),
  ("mixed-polarization gate","the new R-mixed gate is recorded"),
  ("whether and where","open item 7 stated neutrally (Leg B)"),
  ("Disclosed objection to the label itself",
   "the freeze-label objection recorded, not overridden"),
  ("FINAL OPEN-ITEMS REGISTER","the open-items register present"),
  ("R-channel deeper derivation","open item: R derivation"),
  ("EH-generality bridge","open item: EH bridge"),
  ("proportionality-class residual","open item: d2 residual"),
  ("ward","open item: the ward config"),
  ("q-DEPENDENT V deformations","open item: aggregate-vs-per-sector nuance"),
  ("GRUT-specific observables","open item: the forest question"),
  ("FROZEN — CLOSED FOR EPISTEMIC PURPOSES","the freeze declaration present"),
  ("governance freeze","freeze scoped as governance, not mathematical completeness"),
  ("claims register is untouched","freeze does not touch the register")):
    gate(frag in md,"memorandum carries: %s"%desc)

print(); print("="*74); print("14 — GOVERNANCE EXIT"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
gate(POST==PRE,"register sha256 identical pre/post")
frozen_clean=git("status","--porcelain","--","PHYSICS_LEDGER/wall_kr_tier3_loop.py",
  "PHYSICS_LEDGER/.tier3_cmat_cache.json","PHYSICS_LEDGER/.tier1_ds_cache.json",
  "provenance/claims.json").stdout.strip()
gate(frozen_clean=="","no frozen physics file modified")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for ok,_ in CHECKS if ok)
status="FROZEN — CLOSED FOR EPISTEMIC PURPOSES" if not FAILURES else "NOT FROZEN (failures)"
# HONEST BATTERY ACCOUNTING (adopted from Leg A, which showed the first draft's count
# included two gates that could not fail): categories printed, not merged.
n_gov=12; n_str=sum(1 for _,l in CHECKS if l.startswith("memorandum carries:"))
n_math=len(CHECKS)-n_gov-n_str
print("  battery: %d/%d, failures: %d — CATEGORIES: %d governance, %d "
      "record-content string checks (on the memorandum this instrument does NOT write), "
      "%d SUBSTANTIVE symbolic checks (S identity, R u-freeness x4 configs, "
      "coefficient-2 pinning, assembly H-freeness, L, R, R-mixed x2); the two "
      "non-falsifiable identities of the first draft are DEMOTED to notes and counted "
      "nowhere   [%.0fs]"
      %(n,len(CHECKS),len(FAILURES),n_gov,n_str,n_math,time.time()-t0))
for f in FAILURES: print("    FAILED: "+f)
print("  H1 CAMPAIGN STATUS: %s"%status)
out={"instrument":"wall_kr_h1_phase9_closure.py","date":"2026-09-04","base":"c90d684",
 "kind":"H1 CAMPAIGN PHASE 9 — closure memorandum / final epistemic freeze",
 "battery":"%d/%d testable"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "campaign_status":status,
 "channel_status":{"S":"DERIVED (amplitude) + DECLARED INPUT (mixing)",
   "W":"DERIVED (total) + CONVENTION (split)","L":"DERIVED (class-level)",
   "R":"GATED FACT — CLOSED-AS-GATED; derivation = open item"},
 "levels":{"I":"frozen construction: fully closed (3 derived + 1 gated channel)",
   "II":"even-degree class, ladder leg only: fully closed (pure mathematics)",
   "III":"EH: membership=>even-degree ESTABLISHED; 'every EH calc' NOT established",
   "IV":"GRUT: NO GRUT-SPECIFIC CONSEQUENCE ESTABLISHED"},
 "binding_interpretation":"H1 cancellation is a consistency benchmark for any "
   "construction reproducing the declared standard ingredients; NOT a discriminator "
   "for GRUT; must not be cited as GRUT evidence absent an independently introduced "
   "and tested GRUT-specific difference",
 "open_items":["R-channel deeper derivation","EH-generality bridge (4 items)",
   "polarization-direction generality","d2 proportionality-class residual",
   "ward configuration","per-sector vs aggregate vs q-dependent V",
   "genuinely GRUT-specific observables (the forest question)"],
 "A_to_F_selected":"NONE","W":"W-0 — the freeze is a governance status in this record; "
   "nothing banked; register untouched"}
json.dump(out,open(os.path.join(HERE,"WALL_KR_H1_PHASE9_CLOSURE.json"),"w",
          encoding="utf-8"),indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_H1_PHASE9_CLOSURE.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
print("PHASE9_DONE")
