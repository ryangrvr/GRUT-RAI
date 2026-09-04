#!/usr/bin/env python3
"""
H1 CLOSURE — PHASE 7: EH-TT GENERALITY / THEOREM-BOUNDARY AUDIT.
Sole question: how far does the Phase-6 derivation actually generalize?
Lambda_N == 0 is a TARGET throughout, never a premise; the Gram-form derivation is a
CANDIDATE, reconstructed and then pushed to its boundaries:
  (3) polarization: tensor-level homogeneity on the FULL raw vertex (before slotting) +
      the symmetrized mixed-polarization Gram argument => the FULL TT bilinear space at
      the frozen probe direction, not just the sampled configs;
  (4/8) contraction + vertex class: THE ABSTRACT THEOREM — generic symbolic entries and a
      generic symbolic symmetric pairing; Lambda == 0 as a polynomial identity in ALL
      free coefficients (replacing the random genericity control with a formal proof);
  (6/7/10) the homogeneity boundary: the derivation's true premise is EVENNESS of total
      momentum degree, NOT exactly-degree-2 — predicting degree-0 (cosmological-constant
      -type) contamination is HARMLESS to the ladder while degree-1/3 (odd) break it;
      all three gated;
  (9) d / angular / momentum-conservation / CTP / on-shell / TT: shown absent by the
      abstract theorem's construction (no such symbol or constraint exists in it).
Read-only. Phases 1-6 CLOSED. A-F unselected. W-0.
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
              ("016d84b","P5"),("b10c4d9","P6")):
    gate(git("merge-base","--is-ancestor",c_,"HEAD").returncode==0,
         "%s (%s) in ancestry — by RETURNCODE"%(c_,nm))
t3sha=hashlib.sha256(open(os.path.join(HERE,"wall_kr_tier3_loop.py"),"rb").read()).hexdigest()
gate(t3sha.startswith("1c72272b"),"frozen T3 machinery sha 1c72272b... unchanged")
note("A-F UNSELECTED; W-0; nothing banked; Phase 8 NOT started; Lambda_N==0 is a TARGET "
     "below, never a premise")

print(); print("="*74); print("3a — TENSOR-LEVEL HOMOGENEITY (before slotting/routing)"); print("="*74)
dc=json.load(open(os.path.join(HERE,'.tier1_ds_cache.json')))
V3=sp.sympify(dc["sectors"]["(1, 2, 3)"])
V3=V3.xreplace({s: sp.Symbol(s.name) for s in V3.free_symbols})
Hs=sp.Symbol('H')
flat_terms=[t for t in sp.Add.make_args(V3) if not t.has(Hs)]
psyms=[s for t in flat_terms for s in t.free_symbols if s.name.startswith('p')]
psyms=sorted(set(psyms),key=lambda s:s.name)
ok_t=all(sum(sp.degree(t,s) if t.has(s) else 0 for s in psyms)==2 for t in flat_terms)
gate(len(flat_terms)==7560 and len(psyms)==12 and ok_t,
     "TENSOR-LEVEL HOMOGENEITY: all 7,560 flat vertex terms have total degree EXACTLY 2 "
     "in the full unrouted 4-momenta (12 components p{1,2,3}_{0..3}) — BEFORE any "
     "external slotting, internal routing, or projection. Every slotting is linear with "
     "momentum-free (polarization) coefficients, so premise (i) descends to EVERY "
     "external TT polarization and EVERY routing automatically — the three frozen "
     "configs were representatives FOR PREMISE (i), not load-bearing for it (the probe "
     "direction remains load-bearing for the CONCLUSION's polarization coverage, per "
     "section 3b)")

print(); print("="*74); print("3b — FULL TT POLARIZATION SPACE AT THE FROZEN PROBE DIRECTION"); print("="*74)
src=open(os.path.join(HERE,"wall_kr_tier3_loop.py"),encoding="utf-8").read()
M={"__name__":"frozen_t3","__file__":os.path.join(HERE,"wall_kr_tier3_loop.py")}
argv0=sys.argv; sys.argv=["x","machinery_only"]; os.chdir(HERE)
try: exec(compile(src,"t3","exec"),M)
except SystemExit: pass
sys.argv=argv0
CM,cdecomp,htrunc=M["CM"],M["cdecomp"],M["htrunc"]
H,u,up,om,q=M["H"],M["u"],M["up"],M["om"],M["q"]
n1,n2,n3=M["n1"],M["n2"],M["n3"]; PAIRS=M["PAIRS"]
qsub={}
for i_,tgt in ((1,n1),(2,n2),(3,n3)):
    qsub[sp.Symbol("q%d"%i_)]=q*tgt
    qsub[sp.Symbol("q%d"%i_,real=True)]=q*tgt
def entries(config):
    out={}
    for ck,vv in CM[config].items():
        if ck=="meta": continue
        E0=sp.sympify(vv).subs(H,0)
        if E0!=0: out[ck]=sp.expand(E0.xreplace(qsub))
    return out
def decomp(E):
    D=cdecomp(htrunc(E)); out={}
    for (nm,num),c in D.items():
        out[num]=out.get(num,sp.Integer(0))+sp.expand(
            c*(n1**nm[0])*(n2**nm[1])*(n3**nm[2]))
    return out
def build_VG(entA,entB,proj):
    """slot-1 from entA, slot-2 (D2-transformed for V / untransformed for G) from entB."""
    D1={ck:decomp(E) for ck,E in entA.items()}
    D2={ck:decomp(sp.expand(E.xreplace({q:-q}).subs(om,-om).subs(u,up)))
        for ck,E in entB.items()}
    D2G={ck:decomp(E) for ck,E in entB.items()}
    V=defaultdict(lambda: sp.Integer(0)); G=defaultdict(lambda: sp.Integer(0))
    for (a,b) in PAIRS:
        for (c,dd_) in PAIRS:
            k1="%d%d_%d%d"%(a,b,c,dd_)
            if k1 not in D1: continue
            for (ap,bp) in PAIRS:
                for (cp,dp) in PAIRS:
                    k2="%d%d_%d%d"%(ap,bp,cp,dp)
                    if k2 not in D2: continue
                    PP=sp.expand(proj(a,b,ap,bp)*proj(c,dd_,cp,dp))
                    if PP==0: continue
                    for m1,c1 in D1[k1].items():
                        for m2,c2 in D2[k2].items():
                            V[(m1,m2)]+=sp.expand(c1*c2*PP)
                        for m2,c2 in D2G[k2].items():
                            G[(m1,m2)]+=sp.expand(c1*c2*PP)
    return V,G
def lam_of(V):
    byN=defaultdict(lambda: sp.Integer(0))
    for key in V:
        (e_,f_),(g_,h_)=key
        byN[e_+f_+g_+h_]+=sp.expand(V[key]*(g_+h_-e_-f_)*(-1)**(e_+f_))
    return byN
Ptt=M["Ptt"]
EP=entries("plus_z"); EC=entries("cross_z")
Vpc,Gpc=build_VG(EP,EC,Ptt)
Vcp,Gcp=build_VG(EC,EP,Ptt)
keys=sorted(set(Vpc)|set(Vcp)|set(Gpc)|set(Gcp),key=str)
gate(all(sp.expand(Gpc.get(k,0)-Gcp.get((k[1],k[0]),0))==0 for k in keys),
     "MIXED-POLARIZATION CROSS-SYMMETRY: (G^{pc})_k == (G^{cp})_{k^T} — the symmetrized "
     "mixed Gram pair is transposition-symmetric (slot exchange maps one mixed array to "
     "the other)")
gate(all(sp.expand(Vpc.get(k,0)-(-1)**(k[1][0]+k[1][1])*Gpc.get(k,0))==0 for k in keys)
     and all(sp.expand(Vcp.get(k,0)-(-1)**(k[1][0]+k[1][1])*Gcp.get(k,0))==0 for k in keys),
     "MIXED bridge/grading: V^{pc} and V^{cp} are each the graded mixed Gram array "
     "(premise (i) is per-entry, so it never cared which polarization the entry came "
     "from)")
lpc=lam_of(Vpc); lcp=lam_of(Vcp)
gate(all(sp.expand(lpc.get(N_,0)+lcp.get(N_,0))==0 for N_ in set(lpc)|set(lcp)),
     "SYMMETRIZED MIXED LADDER: Lambda^{pc}_N + Lambda^{cp}_N == 0 for every sector — "
     "the cross-polarization blocks cancel through the SAME antisymmetric-weight-vs-"
     "symmetrized-Gram mechanism")
# the bilinearity consequence, gated DIRECTLY (adopted from the adversarial legs):
aa,bb=sp.symbols("a b",real=True)
Eab={}
for ck in set(EP)|set(EC):
    Eab[ck]=sp.expand(aa*EP.get(ck,sp.Integer(0))+bb*EC.get(ck,sp.Integer(0)))
Vab,_=build_VG(Eab,Eab,Ptt)
gate(all(sp.expand(v)==0 for v in lam_of(Vab).values()),
     "ARBITRARY TT POLARIZATION, gated directly: with the superposed entries "
     "E(e) = a*E(plus) + b*E(cross) at the frozen probe direction z, Lambda_N(e) == 0 "
     "IDENTICALLY in symbolic (a,b), every sector — the full 2-parameter TT space, no "
     "longer resting on the bilinearity note alone")
note("CONSEQUENCE (exact bilinearity, from the gates above — a derivation note, not a "
     "separate test): for the ARBITRARY TT polarization e = a*plus + b*cross at the "
     "frozen probe direction, Lambda_N(e) = a^2 L^{pp} + ab (L^{pc}+L^{cp}) + b^2 "
     "L^{cc} == 0 identically in (a,b) — the pp/cc blocks are the P6-gated native "
     "zeros, the mixed block is gated above. SPAN: the FULL 2-parameter TT polarization "
     "space at probe direction z; probe-DIRECTION generality is NOT claimed (plus_x "
     "probes a second direction with its 1-parameter family; no cross_x in the frozen "
     "cache)")

print(); print("="*74); print("4/8 — THE ABSTRACT THEOREM (formal, replaces the random control)"); print("="*74)
# Generic entries: A^{(r)}(om,nu1,nu2) with FREE symbolic coefficients on the full
# even-degree basis {deg 2} + {deg 0}; generic SYMMETRIC pairing pi_{rs} = pi_{sr}.
nu1s,nu2s,oms=sp.symbols("NU1 NU2 OM")
mon2=[oms**2,oms*nu1s,oms*nu2s,nu1s**2,nu1s*nu2s,nu2s**2]
mon0=[sp.Integer(1)]
mon1=[oms,nu1s,nu2s]
NENT=3
def gen_entries(monlist,tag):
    ents={}
    for r in range(NENT):
        E=sp.Integer(0)
        for i_,m_ in enumerate(monlist):
            E+=sp.Symbol("c%s_%d_%d"%(tag,r,i_))*m_
        ents[r]=sp.expand(E)
    return ents
PIs={}
for r in range(NENT):
    for s_ in range(r,NENT):
        PIs[(r,s_)]=PIs[(s_,r)]=sp.Symbol("pi_%d_%d"%(r,s_))
def nu_decomp(E):
    out={}
    p=sp.Poly(E,nu1s,nu2s)
    for mono,co in zip(p.monoms(),p.coeffs()):
        out[mono]=out.get(mono,sp.Integer(0))+co
    return out
def abstract_lambda(ents):
    """V from slot-2 reflection transform (OM->-OM with nu kept: the D2 analogue is the
    total reflection acting on (om); nu graded), G untransformed; pairing pi symmetric."""
    D1={r:nu_decomp(E) for r,E in ents.items()}
    # the D2 analogue at q-free level is om -> -om ONLY (nu symbols kept), exactly
    # matching the frozen convention on the q-free TT entries (P6 leg-A finding):
    D2={r:nu_decomp(sp.expand(E.subs(oms,-oms))) for r,E in ents.items()}
    V=defaultdict(lambda: sp.Integer(0)); G=defaultdict(lambda: sp.Integer(0))
    for r in range(NENT):
        for s_ in range(NENT):
            for m1,c1 in D1[r].items():
                for m2,c2 in D2[s_].items():
                    V[(m1,m2)]+=sp.expand(PIs[(r,s_)]*c1*c2)
                for m2,c2 in D1[s_].items():
                    G[(m1,m2)]+=sp.expand(PIs[(r,s_)]*c1*c2)
    byN=defaultdict(lambda: sp.Integer(0))
    for key,val in V.items():
        (e_,f_),(g_,h_)=key
        byN[e_+f_+g_+h_]+=sp.expand(val*(g_+h_-e_-f_)*(-1)**(e_+f_))
    okg=all(sp.expand(V.get(k,0)-(-1)**(k[1][0]+k[1][1])*G.get(k,0))==0 for k in set(V)|set(G))
    oks=all(sp.expand(G.get(k,0)-G.get((k[1],k[0]),0))==0 for k in set(G))
    okz=all(sp.expand(v)==0 for v in byN.values())
    return okg,oks,okz
okg,oks,okz=abstract_lambda(gen_entries(mon2,"d2"))
gate(okg and oks and okz,
     "ABSTRACT THEOREM (pure degree 2): for GENERIC entries with free symbolic "
     "coefficients on the full degree-2 basis and a GENERIC symbolic symmetric pairing, "
     "V == graded G, G symmetric, and Lambda_N == 0 hold as POLYNOMIAL IDENTITIES in "
     "all %d free coefficients — a formal theorem for the two-derivative class, not a "
     "random sample"%(NENT*len(mon2)+len(set(PIs.values()))))
ents02=gen_entries(mon2,"e2")
for r in range(NENT):
    ents02[r]=sp.expand(ents02[r]+sp.Symbol("z_%d"%r)*mon0[0])
okg0,oks0,okz0=abstract_lambda(ents02)
gate(okg0 and oks0 and okz0,
     "DEGREE-0 HARMLESS: adding GENERIC DEGREE-0 terms (cosmological-constant-type, no "
     "derivatives) leaves the whole chain intact — Lambda_N == 0 still a polynomial "
     "identity; a generic cosmological-constant (degree-0) term would NOT break the "
     "ladder identity")
# degree-4 (even) — closing the gated support for the even-class quantifier at source
# (adopted from both adversarial legs, whose independent runs pass):
mon4=[oms**4,oms**3*nu1s,oms**3*nu2s,oms**2*nu1s**2,oms**2*nu1s*nu2s,oms**2*nu2s**2,
      oms*nu1s**3,oms*nu1s**2*nu2s,oms*nu1s*nu2s**2,oms*nu2s**3,
      nu1s**4,nu1s**3*nu2s,nu1s**2*nu2s**2,nu1s*nu2s**3,nu2s**4]
ents4=gen_entries(mon2,"h2")
for r in range(NENT):
    E=ents4[r]
    for i_,m_ in enumerate(mon4):
        E+=sp.Symbol("v_%d_%d"%(r,i_))*m_
    ents4[r]=sp.expand(E)
okg4,oks4,okz4=abstract_lambda(ents4)
gate(okg4 and oks4 and okz4,
     "DEGREE-4 HARMLESS (complete 15-monomial basis): generic degree-4 admixture keeps "
     "the whole chain intact — Lambda_N == 0 a polynomial identity through sector N=8")
note("THE BOUNDARY, with its support stated precisely: the derivation's true premise "
     "is EVENNESS of total momentum degree, NOT exactly-degree-2 — GATED at degrees "
     "{0, 2, 4} (complete bases) with odd counterexamples at {1, 3}; higher even "
     "degrees follow from the same parity identity ((-1)^{OM-deg} = (-1)^{total deg} "
     "x (-1)^{nu-deg}), a DERIVATION, not separately gated. Phase 6's exactly-2 "
     "premise was stronger than needed")
ents1=gen_entries(mon2,"f2")
for r in range(NENT):
    E=ents1[r]
    for i_,m_ in enumerate(mon1):
        E+=sp.Symbol("w_%d_%d"%(r,i_))*m_
    ents1[r]=sp.expand(E)
okg1,oks1,okz1=abstract_lambda(ents1)
gate((not okg1) and (not okz1),
     "THE ODD-DEGREE BOUNDARY: generic DEGREE-1 admixtures break the graded bridge "
     "(V != graded G) AND leave Lambda_N a NONZERO polynomial — odd-degree content is "
     "the precise obstruction (the odd part acquires an extra (-1) under the "
     "reflection, splitting the grading)")
ents3=gen_entries(mon2,"g2")
mon3=[oms**3,oms**2*nu1s,oms**2*nu2s,oms*nu1s**2,oms*nu1s*nu2s,oms*nu2s**2,
      nu1s**3,nu1s**2*nu2s,nu1s*nu2s**2,nu2s**3]   # complete 10-monomial basis
for r in range(NENT):
    E=ents3[r]
    for i_,m_ in enumerate(mon3):
        E+=sp.Symbol("y_%d_%d"%(r,i_))*m_
    ents3[r]=sp.expand(E)
okg3,oks3,okz3=abstract_lambda(ents3)
gate((not okg3) and (not okz3),
     "degree-3 (odd, COMPLETE basis) contamination likewise breaks the bridge and "
     "leaves Lambda a nonzero polynomial")

print(); print("="*74); print("5/9 — ROUTING/INGREDIENT CLASSIFICATION"); print("="*74)
EX=entries("plus_x")
gate(all(not E.has(q) for E in EP.values()) and all(not E.has(q) for E in EC.values())
     and all(not E.has(q) for E in EX.values()),
     "the frozen TT flat entries are q-FREE (all three configs) — the D2 transform's "
     "q->-q leg is vacuous at flat level and the +/-q routing convention cannot enter "
     "any derivation step; spatial-momentum routing is an upstream cache-construction "
     "fact, outside the theorem (P6 leg-A finding, now gated)")
gate(all(not E.has(u) and not E.has(up) for EE in (EP,EC,EX) for E in EE.values()),
     "COMPANION ASSUMPTION GATED (adopted from Leg A): the flat entries are also "
     "u,u'-FREE (all three configs) — the frozen D2's subs(u,u') leg is likewise "
     "vacuous, so the abstract theorem's om->-om-only D2 analogue is FAITHFUL to the "
     "full frozen convention (q->-q, om->-om, u->u') on these entries")
note("INGREDIENT CLASSIFICATION (section 5/9): dummy-index relabeling and slot "
     "exchange = mathematical identities (the abstract theorem uses only these); the "
     "D2 representation = frozen convention whose entire flat-level content is om->-om, "
     "DERIVED equal to the nu-reflection by the bridge; q-sign and momentum assignment "
     "= upstream conventions, vacuous at flat level (gated above); d, angular "
     "averaging, momentum conservation, CTP, retarded prescription, on-shell, TT "
     "projection = ABSENT from the abstract theorem BY CONSTRUCTION — no such symbol "
     "or constraint exists in it (the strongest form of the section-9 independence "
     "proof: inspection of a complete formal object, not citation of prior controls)")

print(); print("="*74); print("11 — NECESSITY / SUFFICIENCY FOR THE GENERALIZED THEOREM"); print("="*74)
note("EVEN-degree homogeneity: SUFFICIENT (abstract theorem, polynomial identity); "
     "NECESSARY at generic level (generic odd admixture leaves Lambda a nonzero "
     "polynomial — gated; special odd entries could still cancel, so necessity is "
     "generic, not universal). Symmetric slot pairing: SUFFICIENT (abstract theorem); "
     "NOT NECESSARY (P6 refinement: entry-proportionality is an alternative route — "
     "cited, closed). Additional EH-specific condition: NONE — the abstract theorem "
     "needs no EH input beyond membership in the even-degree class; EH ENTERS ONLY as "
     "the provenance of that membership (two-derivative action, tensor-level gate).")

print(); print("="*74); print("16 — GOVERNANCE EXIT"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
gate(POST==PRE,"register sha256 identical pre/post")
frozen_clean=git("status","--porcelain","--","PHYSICS_LEDGER/wall_kr_tier3_loop.py",
  "PHYSICS_LEDGER/.tier3_cmat_cache.json","PHYSICS_LEDGER/.tier1_ds_cache.json",
  "provenance/claims.json").stdout.strip()
gate(frozen_clean=="","no frozen physics file modified")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for ok,_ in CHECKS if ok)
core=(ok_t and okg and oks and okz and okg0 and okz0 and okg4 and okz4
      and (not okz1) and (not okz3))
verdict="TWO-DERIVATIVE-CLASS-GENERALIZED" if (not FAILURES and core) else \
        ("PARTIALLY-GENERALIZED" if core else "INCONCLUSIVE")
print("  battery: %d/%d testable gates, failures: %d   [%.0fs]"
      %(n,len(CHECKS),len(FAILURES),time.time()-t0))
for f in FAILURES: print("    FAILED: "+f)
print("  VERDICT: %s"%verdict)
out={"instrument":"wall_kr_h1_phase7_generality.py","date":"2026-09-03","base":"b10c4d9",
 "kind":"H1 CLOSURE PHASE 7 — generality audit OF the EH-TT ladder derivation "
   "(theorem-boundary attack; the kind names the question, not an achieved property)",
 "battery":"%d/%d testable"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "generalizations":{
  "tensor_level":"homogeneity gated on ALL 7,560 flat vertex terms in the full unrouted "
    "4-momenta, BEFORE slotting/routing/projection — premise (i) descends to every "
    "external TT polarization and every routing (slotting is linear with momentum-free "
    "coefficients)",
  "polarization":"FULL 2-parameter TT polarization space at the frozen probe direction "
    "z, via the symmetrized mixed Gram (Lambda^{pc}+Lambda^{cp} == 0 gated); "
    "probe-DIRECTION generality NOT claimed",
  "abstract_theorem":"for GENERIC symbolic entries on the even-degree basis and a "
    "GENERIC symbolic symmetric pairing, Lambda_N == 0 is a POLYNOMIAL IDENTITY — the "
    "random genericity control is replaced by a formal class theorem",
  "boundary":"the true premise is EVEN total momentum degree, not exactly-2 — GATED at "
    "degrees {0,2,4} (complete bases) with odd counterexamples at {1,3} (complete "
    "bases); higher even degrees follow from the parity identity (derivation, not "
    "separately gated). Degree-0 (cosmological-constant-type) contamination HARMLESS; "
    "the exact obstruction is the extra (-1) the odd part acquires under reflection",
  "routing":"q-freeness of the flat TT entries gated: the +/-q routing cannot enter "
    "any derivation step; d/angular/momentum-conservation/CTP/on-shell/TT absent from "
    "the abstract theorem by construction"},
 "necessity_sufficiency":{"even_homogeneity":"sufficient (identity); necessary at "
   "generic level (gated); universal necessity not claimed",
   "symmetric_pairing":"sufficient; not necessary (P6 refinement, cited)",
   "EH_specific_condition":"NONE — EH enters only as provenance of even-class "
   "membership"},
 "verdict":verdict,
 "not_claimed":["probe-direction generality (two directions probed; no cross_x in the "
   "frozen cache)","'every EH graviton calculation of this class necessarily has "
   "H1=0' (only the LADDER leg is generalized here; the S and W legs keep their own "
   "provenances)","universal necessity of even-homogeneity (generic only)",
   "any GRUT-specific content"],
 "A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(HERE,"WALL_KR_H1_PHASE7_RESULT.json"),"w",encoding="utf-8"),
          indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_H1_PHASE7_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
print("PHASE7_DONE")
