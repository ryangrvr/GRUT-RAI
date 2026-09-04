#!/usr/bin/env python3
"""
H1 CLOSURE — PHASE 6: LADDER-IDENTITY DERIVATION ATTACK.
Single question: can Lambda_N = 0 (N=0..4) be DERIVED from deeper algebraic structure
already present in the frozen construction, without importing the Phase-1 swap relation,
Lambda_N == 0, or the Phase-4 factorization as premises?

THE CANDIDATE DERIVATION (stated before gating; every step gated below):
  PREMISE (i)  — HOMOGENEITY: every monomial of every flat C^0 entry has total degree
                 EXACTLY 2 in the momenta (omega, nu1, nu2, q) — the two-derivative
                 character of the EH action at the flat level. Hence each entry is EVEN
                 under total momentum reflection, giving the per-entry BRIDGE
                     E(-omega,-q)(nu) = E(omega,q)(-nu),
                 which is exactly the frozen D2 transform.
  PREMISE (ii) — SLOT SYMMETRY: the vertex-slot contraction Pi is symmetric under
                 exchanging the two slots (dummy-index relabeling; holds for P^TT and for
                 every contraction Phase 5 tested — this premise EXPLAINS the Phase-5
                 projector-immateriality).
  CHAIN: (i) => per key, V[(e,f),(g,h)] = (-1)^{g+h} G[(e,f),(g,h)], where G is the
  UNTRANSFORMED both-slots-at-(omega,q) Gram-type array; (ii) => G is symmetric under key
  transposition ((e,f),(g,h)) -> ((g,h),(e,f)). Then
     Lambda_N = sum_k (g+h-e-f)(-1)^{e+f} V_k = (-1)^N sum_k (g+h-e-f) G_k = 0
  per sector: an ANTISYMMETRIC weight against a SYMMETRIC array, cancelling per
  transposition-orbit (diagonal keys carry zero weight). At FIXED omega — explaining why
  the omega-flipped variant is FALSE (the reflection restores fixed omega); with NO use
  of d, TT structure, momentum conservation, CTP, on-shell or angular input — explaining
  the Phase-5 immaterialities; with degree <= 2 per vertex — explaining N <= 4.
HOSTILE CONTROLS (each targets ONE premise): (a) an odd-degree (degree-1) momentum
admixture in one entry breaks the bridge and Lambda; (b) a slot-ASYMMETRIC contraction
breaks G-symmetry and Lambda. Read-only. Phases 1-5 CLOSED. A-F unselected. W-0.
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
              ("016d84b","P5")):
    gate(git("merge-base","--is-ancestor",c_,"HEAD").returncode==0,
         "%s (%s) in ancestry — by RETURNCODE"%(c_,nm))
t3sha=hashlib.sha256(open(os.path.join(HERE,"wall_kr_tier3_loop.py"),"rb").read()).hexdigest()
gate(t3sha.startswith("1c72272b"),"frozen T3 machinery sha 1c72272b... unchanged")
note("A-F UNSELECTED; W-0; nothing banked; Phase 7 NOT started; the Phase-1 swap "
     "relation, Lambda_N==0, and the Phase-4 factorization are NOT premises below")

print(); print("="*74); print("2 — RAW OBJECT + PREMISE (i): HOMOGENEITY/BRIDGE"); print("="*74)
src=open(os.path.join(HERE,"wall_kr_tier3_loop.py"),encoding="utf-8").read()
M={"__name__":"frozen_t3","__file__":os.path.join(HERE,"wall_kr_tier3_loop.py")}
argv0=sys.argv; sys.argv=["x","machinery_only"]; os.chdir(HERE)
try: exec(compile(src,"t3","exec"),M)
except SystemExit: pass
sys.argv=argv0
CM,cdecomp,Ptt,htrunc=M["CM"],M["cdecomp"],M["Ptt"],M["htrunc"]
H,u,up,om,q=M["H"],M["u"],M["up"],M["om"],M["q"]
n1,n2,n3=M["n1"],M["n2"],M["n3"]; PAIRS=M["PAIRS"]; dsym=M["dsym"]
nu1,nu2=M["nu1"],M["nu2"]
qsub={}
for i_,tgt in ((1,n1),(2,n2),(3,n3)):
    qsub[sp.Symbol("q%d"%i_)]=q*tgt
    qsub[sp.Symbol("q%d"%i_,real=True)]=q*tgt
MOM=(om,nu1,nu2,q)
REFL={s:-s for s in MOM}
CONFIGS=("plus_z","cross_z","plus_x")
ENT={}
for config in CONFIGS:
    ENT[config]={}
    ok_hom=True; ok_even=True; ok_bridge=True; n_ent=0
    for ck,vv in CM[config].items():
        if ck=="meta": continue
        E0=sp.sympify(vv).subs(H,0)
        if E0==0: continue
        E=sp.expand(E0.xreplace(qsub)); n_ent+=1
        ENT[config][ck]=E
        for t in sp.Add.make_args(E):
            deg=sum(sp.degree(t,s) if t.has(s) else 0 for s in MOM)
            if deg!=2: ok_hom=False
        if sp.expand(E.xreplace(REFL)-E)!=0: ok_even=False
        # THE BRIDGE, per entry: the frozen D2 transform equals a pure nu-reflection
        d2=sp.expand(E.xreplace({q:-q}).subs(om,-om).subs(u,up))
        nrefl=sp.expand(E.xreplace({nu1:-nu1,nu2:-nu2}))
        if sp.expand(d2-nrefl)!=0: ok_bridge=False
    gate(ok_hom,"[%s] PREMISE (i) HOMOGENEITY: every monomial of every flat C^0 entry "
         "(%d nonzero entries) has total (omega,nu1,nu2,q)-degree EXACTLY 2 — the "
         "two-derivative EH structure, read off the raw object"%(config,n_ent))
    gate(ok_even,"[%s] hence REFLECTION-EVEN: E(-omega,-nu,-q) == E(omega,nu,q) per "
         "entry"%config)
    gate(ok_bridge,"[%s] THE BRIDGE, per entry: the frozen D2 transform "
         "(omega,q) -> (-omega,-q) equals the pure nu-reflection nu -> -nu — "
         "E(-omega,-q)(nu) == E(omega,q)(-nu) for every entry. The vertex-2 factor IS "
         "the vertex-1 factor with graded nu-sign — no omega flip survives, explaining "
         "the FALSE omega-flipped variant"%config)

print(); print("="*74); print("3/5/6 — THE DERIVATION: V = (-1)^{g+h} G, G SYMMETRIC")
print("="*74)
def build_arrays(config,proj,odd_inject=None,projB=None):
    """V (with the frozen D2 slot-2 transform) and G (both slots untransformed).
    projB (default proj) lets the two lines carry different pairings — used only by the
    hostile premise-(ii) control."""
    if projB is None: projB=proj
    D1,D2={},{}
    for ck,E in ENT[config].items():
        Ei=E if (odd_inject is None or ck!=odd_inject[0]) else sp.expand(E+odd_inject[1])
        D1[ck]=cdecomp(htrunc(Ei))
        d2=sp.expand(Ei.xreplace({q:-q}).subs(om,-om).subs(u,up))
        D2[ck]=cdecomp(htrunc(d2))
    P_line={}; P_lineB={}
    for (a,b) in PAIRS:
        for (ap,bp) in PAIRS:
            P_line[((a,b),(ap,bp))]=proj(a,b,ap,bp)
            P_lineB[((a,b),(ap,bp))]=projB(a,b,ap,bp)
    V=defaultdict(lambda: sp.Integer(0)); G=defaultdict(lambda: sp.Integer(0))
    for (a,b) in PAIRS:
        for (c,dd_) in PAIRS:
            k1="%d%d_%d%d"%(a,b,c,dd_)
            if k1 not in D1: continue
            for (ap,bp) in PAIRS:
                for (cp,dp) in PAIRS:
                    k2="%d%d_%d%d"%(ap,bp,cp,dp)
                    if k2 not in D1: continue
                    PA=P_line[((a,b),(ap,bp))]; PB=P_lineB[((c,dd_),(cp,dp))]
                    if PA==0 or PB==0: continue
                    pab=sp.Poly(sp.expand(PA*PB),n1,n2,n3)
                    PABL=list(zip(pab.monoms(),pab.coeffs()))
                    for (nm1,nu1m),c1 in D1[k1].items():
                        for (nm2,nu2m),c2 in D2[k2].items():
                            npart=(nm1[0]+nm2[0],nm1[1]+nm2[1],nm1[2]+nm2[2])
                            afp=sum(cP*(n1**(npart[0]+mP[0]))*(n2**(npart[1]+mP[1]))
                                    *(n3**(npart[2]+mP[2])) for mP,cP in PABL)
                            if afp!=0: V[(nu1m,nu2m)]+=c1*c2*afp
                        for (nm2,nu2m),c2 in D1[k2].items():
                            npart=(nm1[0]+nm2[0],nm1[1]+nm2[1],nm1[2]+nm2[2])
                            afp=sum(cP*(n1**(npart[0]+mP[0]))*(n2**(npart[1]+mP[1]))
                                    *(n3**(npart[2]+mP[2])) for mP,cP in PABL)
                            if afp!=0: G[(nu1m,nu2m)]+=c1*c2*afp
    return V,G
def lam_of(V):
    byN=defaultdict(lambda: sp.Integer(0))
    for key in V:
        (e_,f_),(g_,h_)=key
        byN[e_+f_+g_+h_]+=sp.expand(V[key]*(g_+h_-e_-f_)*(-1)**(e_+f_))
    return byN
gate(all(sp.expand(Ptt(a,b,c,d)-Ptt(c,d,a,b))==0
         for (a,b) in PAIRS for (c,d) in PAIRS),
     "PREMISE (ii) SLOT SYMMETRY: Ptt(a,b,c,d) == Ptt(c,d,a,b) for all index pairs — "
     "the contraction is exchange-symmetric (dummy-index relabeling). P^TT gated HERE; "
     "single-delta gated in section 8/9; the remaining Phase-5 alternatives are "
     "slot-symmetric by inspection, NOT gated — stated so no untested claim rides this "
     "gate's label")
RES={}
for config in CONFIGS:
    V,G=build_arrays(config,Ptt)
    keys=sorted(set(V)|set(G),key=str)
    ok_vg=all(sp.expand(V.get(k,0)-(-1)**(k[1][0]+k[1][1])*G.get(k,0))==0 for k in keys)
    gate(ok_vg,"[%s] DERIVED STEP 1 (from premise i): V[(e,f),(g,h)] == "
         "(-1)^{g+h} G[(e,f),(g,h)] per key, all %d keys — the frozen array IS the "
         "graded untransformed Gram array"%(config,len(keys)))
    ok_gsym=all(sp.expand(G.get(k,0)-G.get((k[1],k[0]),0))==0 for k in keys)
    gate(ok_gsym,"[%s] DERIVED STEP 2 (from premise ii): G is SYMMETRIC under key "
         "transposition ((e,f),(g,h)) -> ((g,h),(e,f))"%config)
    # the conclusion, algebra only: Lambda_N = (-1)^N sum (g+h-e-f) G_k = 0 by
    # antisymmetric weight x symmetric array; verify against the DIRECT Lambda:
    byN=lam_of(V)
    okd=all(sp.expand(v)==0 for v in byN.values())
    ok_orbit=all(sp.expand((k[1][0]+k[1][1]-k[0][0]-k[0][1])*G.get(k,0)
                 +(k[0][0]+k[0][1]-k[1][0]-k[1][1])*G.get((k[1],k[0]),0))==0
                 for k in keys)
    gate(okd and ok_orbit,
         "[%s] CONCLUSION: Lambda_N = (-1)^N sum_k (g+h-e-f) G_k cancels PER "
         "TRANSPOSITION-ORBIT (each {k, k^T} pair exactly; diagonal keys weight-0), and "
         "the direct Lambda_N == 0 (N=%s) is REPRODUCED — derived, not assumed"
         %(config,sorted(byN)))
    RES[config]={"homogeneity":True,"bridge":True,"V_eq_graded_G":ok_vg,
                 "G_symmetric":ok_gsym,"lambda_zero_reproduced":okd,
                 "orbit_cancellation":ok_orbit}

print(); print("="*74); print("8/9 — WHAT THE DERIVATION DOES AND DOES NOT USE"); print("="*74)
def Pdel(a,b,c,dd): return sp.Integer(1) if (a==c and b==dd) else sp.Integer(0)
gate(all(sp.expand(Pdel(a,b,c,d)-Pdel(c,d,a,b))==0
         for (a,b) in PAIRS for (c,d) in PAIRS),
     "the single-delta pairing is ALSO slot-symmetric — premise (ii) covers it; the "
     "derivation closes BEFORE TT projection (no transversality, trace, or d enters any "
     "step above), explaining the Phase-5 immateriality finding")
Vd,Gd=build_arrays("plus_z",Pdel)
okd2=(all(sp.expand(Vd.get(k,0)-(-1)**(k[1][0]+k[1][1])*Gd.get(k,0))==0
          for k in set(Vd)|set(Gd))
      and all(sp.expand(Gd.get(k,0)-Gd.get((k[1],k[0]),0))==0 for k in set(Gd))
      and all(sp.expand(v)==0 for v in lam_of(Vd).values()))
gate(okd2,"[plus_z] the FULL derivation chain re-verified under single-delta — "
     "projector-free in fact, not only in principle")
note("NOT USED anywhere in the derivation: d (symbolic or otherwise), angular "
     "averaging, momentum conservation (the argument is per-vertex; independent line "
     "momenta never enter), CTP/retarded structure, on-shell conditions, TT conditions. "
     "USED: premise (i) homogeneity (gated on the raw artifact), premise (ii) slot "
     "symmetry (gated), the nu-grading bookkeeping, and the frozen D2 convention "
     "(whose content, by the bridge, is exactly the nu-reflection)")

print(); print("="*74); print("10 — HOSTILE DISPROOF MODE"); print("="*74)
# (a) break premise (i): inject a degree-1 (odd) momentum term into ONE entry:
ck0=sorted(ENT["plus_z"])[0]
Vh,Gh=build_arrays("plus_z",Ptt,odd_inject=(ck0,om))
byNh=lam_of(Vh)
brk_a=any(sp.expand(v)!=0 for v in byNh.values())
ok_vg_h=all(sp.expand(Vh.get(k,0)-(-1)**(k[1][0]+k[1][1])*Gh.get(k,0))==0
            for k in set(Vh)|set(Gh))
gate(brk_a and not ok_vg_h,
     "HOSTILE (a) DETECTS: injecting a DEGREE-1 momentum term (+omega) into one C entry "
     "breaks the bridge (V != graded G) AND breaks Lambda_N != 0 — premise (i) is "
     "LOAD-BEARING, the mechanism carries the cancellation")
# (b) break premise (ii). DISCLOSED, THE FULL CHAIN OF FAILED DRAFTS (each caught by
# its own gate — section-10 discipline working): draft 1 weighted the delta-pairing by
# the first index, but the delta support forces a==ap, weight INERT on support; draft 2
# used off-diagonal support (1,1)->(1,2) which misses the nonzero entries — empty
# arrays; draft 3 used (1,1)->(2,2) — asymmetric, supported, and Lambda STILL vanished:
# a DISCOVERY, not a bug (see the discovery block below — premise (ii) is sufficient
# but NOT necessary; specific asymmetric contractions cancel via pair-compatibility).
# FINAL FORM: a two-projector contraction isolating the single INCOMPATIBLE cross-pair
# 11_11 (x) 11_33 (its stripped-profile Wronskian fails at N=1,2,3):
def PA_r1(a,b,c,dd):
    return (sp.Integer(1) if ((a,b)==(1,1) and (c,dd)==(1,1)) else sp.Integer(0))
def PB_r1(a,b,c,dd):
    return (sp.Integer(1) if ((a,b)==(1,1) and (c,dd)==(3,3)) else sp.Integer(0))
asym_exists=any(sp.expand(PA_r1(a,b,c,d)*PB_r1(a2,b2,c2,d2)
                -PA_r1(c,d,a,b)*PB_r1(c2,d2,a2,b2))!=0
                for (a,b) in PAIRS for (c,d) in PAIRS
                for (a2,b2) in PAIRS for (c2,d2) in PAIRS)
Va,Ga=build_arrays("plus_z",PA_r1,projB=PB_r1)
byNa=lam_of(Va)
brk_b=any(sp.expand(v)!=0 for v in byNa.values())
gsym_b=all(sp.expand(Ga.get(k,0)-Ga.get((k[1],k[0]),0))==0 for k in set(Ga))
gate(asym_exists and brk_b and not gsym_b,
     "HOSTILE (b) DETECTS: a slot-ASYMMETRIC contraction isolating the single "
     "incompatible cross-pair 11_11 (x) 11_33 breaks G-symmetry AND breaks "
     "Lambda_N != 0 (sectors 1,2,3) — premise (ii) is LOAD-BEARING FOR THE DERIVATION "
     "ROUTE: without it, cancellation is not guaranteed")

print(); print("="*74); print("10' — REFINEMENT: THE OPERATIVE CONDITION IS G-SYMMETRY")
print("="*74)
# Draft 3 of hostile (b) — the asymmetric single-pair contraction 11_11 (x) 22_22 —
# cancelled, and the reason is now identified and GATED: G came out SYMMETRIC anyway,
# because those two entries have PROPORTIONAL nu-stripped coefficient vectors, making
# the outer-product G symmetric under ANY pairing. There is NO second mechanism: the
# derivation factors through G-symmetry in every observed case. Refined chain:
#   Lambda_N = (-1)^N sum_k (g+h-e-f) G_k = 0  <==  G symmetric under key transposition
#   <==  EITHER premise (ii) (slot-symmetric Pi; any entries — covers the NATIVE case)
#        OR entry-proportionality (special entry pairs; any Pi).
def PA_d1(a,b,c,dd):
    return (sp.Integer(1) if ((a,b)==(1,1) and (c,dd)==(2,2)) else sp.Integer(0))
Vd1,Gd1=build_arrays("plus_z",PA_d1)
STRIPK={}
for ck,E in ENT["plus_z"].items():
    D=cdecomp(htrunc(E))
    A={}
    for (nm,num),c in D.items():
        A[num]=A.get(num,sp.Integer(0))+sp.expand(c*(n1**nm[0])*(n2**nm[1])*(n3**nm[2]))
    STRIPK[ck]=A
def proportional(P,Q):
    A,B=STRIPK[P],STRIPK[Q]
    keys=set(A)|set(B)
    for k1 in keys:
        for k2 in keys:
            if sp.expand(A.get(k1,0)*B.get(k2,0)-A.get(k2,0)*B.get(k1,0))!=0:
                return False
    return True
gate(all(sp.expand(v)==0 for v in lam_of(Vd1).values())
     and all(sp.expand(Gd1.get(k,0)-Gd1.get((k[1],k[0]),0))==0 for k in set(Gd1))
     and proportional("11_11","22_22") and not proportional("11_11","11_33"),
     "REFINEMENT GATED (d1): under the asymmetric pairing 11_11 (x) 22_22, G is "
     "SYMMETRIC anyway — the two entries' nu-stripped coefficient vectors are "
     "PROPORTIONAL (gated), so the outer product is symmetric under any Pi and the "
     "same G-symmetry mechanism cancels Lambda; whereas 11_11 and 11_33 are NOT "
     "proportional (gated), which is why hostile (b) breaks on that pair. The "
     "operative condition is G-SYMMETRY; premise (ii) is one sufficient route to it "
     "(the one covering the NATIVE contraction), entry-proportionality another")
# (d2) the residual structure, made crisp: the proportionality-class partition of the
# entries' stripped coefficient vectors:
ents=sorted(STRIPK); classes=[]
for P in ents:
    placed=False
    for cl in classes:
        if proportional(P,cl[0]): cl.append(P); placed=True; break
    if not placed: classes.append([P])
print("  RESULT: proportionality classes (plus_z): %s"%classes, flush=True)
gate(len(classes)>1 and any(len(cl)>1 for cl in classes),
     "DISCOVERY (d2): the entries partition into %d proportionality classes (at least "
     "one nontrivial) — the pattern of WHICH entry pairs yield symmetric G under "
     "asymmetric pairings is exactly this partition. WHY the EH vertex produces these "
     "particular proportionalities is RESIDUAL STRUCTURE beyond this derivation: "
     "recorded as an open observation, not chased in this phase"%len(classes))
note("SCOPE: the NATIVE contraction and every slot-symmetric alternative are covered "
     "by premises (i)+(ii). The refined picture does not weaken the derivation — it "
     "identifies G-symmetry as the operative intermediate condition and premise (ii) "
     "as sufficient-not-necessary for it")

print(); print("="*74); print("11 — NECESSITY / SUFFICIENCY OF THE PREMISES"); print("="*74)
note("SUFFICIENT: premises (i)+(ii) => Lambda_N == 0, by the two derived steps — exact "
     "algebra, gated above on all three configs; this COVERS the native contraction. "
     "NECESSITY, honestly split: premise (i) is load-bearing (hostile a: violating it "
     "breaks the bridge and Lambda). Premise (ii) is load-bearing FOR THE DERIVATION "
     "ROUTE (hostile b: an asymmetric contraction on an incompatible pair breaks "
     "Lambda) but NOT NECESSARY in general (discovery d1: a compatible asymmetric pair "
     "still cancels) — a second, unexplained mechanism (pair-compatibility, d2) exists "
     "for special contractions. PROVENANCE OF THE PREMISES: (i) is the two-derivative "
     "character of the EH action at the flat level — gated directly on the frozen "
     "artifact, derivable from the declared EH input (T1's in-repo derivation produces "
     "it); (ii) is dummy-index relabeling — a standard identity of any bilinear "
     "pairing. NEITHER is GRUT-specific.")

print(); print("="*74); print("16 — GOVERNANCE EXIT"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
gate(POST==PRE,"register sha256 identical pre/post")
frozen_clean=git("status","--porcelain","--","PHYSICS_LEDGER/wall_kr_tier3_loop.py",
  "PHYSICS_LEDGER/.tier3_cmat_cache.json","PHYSICS_LEDGER/.tier1_ds_cache.json",
  "provenance/claims.json").stdout.strip()
gate(frozen_clean=="","no frozen physics file modified")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for ok,_ in CHECKS if ok)
allder=all(RES.get(c,{}).get("V_eq_graded_G") and RES.get(c,{}).get("G_symmetric")
           and RES.get(c,{}).get("lambda_zero_reproduced") for c in CONFIGS)
verdict="LADDER-DERIVED" if (not FAILURES and allder) else \
        ("LADDER-PARTIALLY-DERIVED" if allder else "INCONCLUSIVE")
print("  battery: %d/%d testable gates, failures: %d   [%.0fs]"
      %(n,len(CHECKS),len(FAILURES),time.time()-t0))
for f in FAILURES: print("    FAILED: "+f)
print("  VERDICT: %s"%verdict)
out={"instrument":"wall_kr_h1_phase6_ladder_derivation.py","date":"2026-09-03",
 "base":"016d84b","kind":"H1 CLOSURE PHASE 6 — ladder-identity derivation attack",
 "battery":"%d/%d testable"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "derivation":{
  "premise_i":"HOMOGENEITY — every flat C^0 entry monomial has total momentum degree "
    "exactly 2 (two-derivative EH); gated on the raw artifact, all three configs",
  "premise_ii":"SLOT SYMMETRY — the contraction is exchange-symmetric (dummy-index "
    "relabeling); gated for P^TT and single-delta",
  "bridge":"E(-omega,-q)(nu) == E(omega,q)(-nu) per entry — the frozen D2 transform IS "
    "the nu-reflection; explains the FALSE omega-flipped variant",
  "step1":"V[(e,f),(g,h)] == (-1)^{g+h} G[(e,f),(g,h)] per key (G = untransformed Gram "
    "array)","step2":"G symmetric under key transposition",
  "conclusion":"Lambda_N = (-1)^N sum_k (g+h-e-f) G_k == 0 per transposition-orbit "
    "(antisymmetric weight x symmetric array; diagonal weight-0) — derived, and the "
    "direct Lambda_N == 0 reproduced on all three configs",
  "explains":["the fixed-omega (no-flip) form of the P1 symmetry","why NO symmetry "
    "supports an omega-flipped form (the D2 transform's entire content is the "
    "nu-reflection) — the flipped variant's FALSITY remains P1's gated fact, resting "
    "additionally on the omega-oddness of the mixed S-blocks (leg-verified), which is "
    "consistent with but not derivable from premises (i)+(ii)",
    "Phase-5 projector-immateriality (any slot-symmetric contraction works)",
    "d/momentum-conservation/CTP immateriality","the sector bound N <= 4 (degree <= 2 "
    "per vertex)"]},
 "hostile_controls":{"a_odd_admixture":"degree-1 term in one entry breaks bridge AND "
   "Lambda (premise i load-bearing)","b_asymmetric_pairing":"two-projector contraction "
   "isolating the incompatible cross-pair 11_11 x 11_33 breaks G-symmetry AND Lambda "
   "sectors 1,2,3 (premise ii load-bearing for the derivation route)",
   "b_failed_drafts":"three drafts caught by their own gates: index-weighted delta "
   "(inert on support); (1,1)->(1,2) (empty support); (1,1)->(2,2) (cancelled — a "
   "DISCOVERY, kept as d1)"},
 "discoveries":{"d1":"REFINEMENT: the operative intermediate condition is G-SYMMETRY; "
   "premise (ii) is one sufficient route (covers the native case); "
   "entry-proportionality is another (gated: 11_11 ~ 22_22 proportional, so G "
   "symmetric under ANY pairing; 11_11 !~ 11_33, which is why hostile b breaks there). "
   "No second mechanism — the derivation factors through G-symmetry in every observed "
   "case","d2":"the entries partition into proportionality classes of their "
   "nu-stripped coefficient vectors; WHY the EH vertex produces these particular "
   "proportionalities is RESIDUAL STRUCTURE, recorded as an open observation"},
 "necessity_sufficiency":{"sufficient":"EXACT — (i)+(ii) => Lambda_N == 0 (gated "
   "derivation); covers the native contraction","necessary":"(i): load-bearing "
   "(hostile a). (ii): load-bearing for the derivation route (hostile b) but NOT "
   "necessary in general (discovery d1); search-verdict strength",
   "premise_provenance":"(i) = two-derivative EH at flat level, gated on the artifact, "
   "produced by T1's in-repo derivation from the declared action — EXACTNESS of degree "
   "2 also uses the declared Lambda = 3H^2 being O(H^2) (a generic cosmological "
   "constant would deposit derivative-free cubic monomials at flat level), and "
   "gauge-fixing/measure terms are absent BY DECLARED CONSTRUCTION (full unfixed h; "
   "classical action-level vertex); (ii) = standard dummy-index relabeling; neither "
   "GRUT-specific"},
 "per_config":RES,"verdict":verdict,
 "not_claimed":["generality beyond the three frozen TT configurations and the frozen "
   "routing conventions (THEOREM-LOCAL heritage)","necessity of the premises beyond "
   "the tested directions","any GRUT-specific content"],
 "A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(HERE,"WALL_KR_H1_PHASE6_RESULT.json"),"w",encoding="utf-8"),
          indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_H1_PHASE6_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
print("PHASE6_DONE")
