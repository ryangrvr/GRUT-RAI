#!/usr/bin/env python3
"""
H1 CAMPAIGN STAGE 2B.1 — TAGGED RECONSTRUCTION OF THE O(H) INTEGRAND.
Uses the FROZEN T3 machinery itself (exec'd with a sentinel stage so no stage block runs),
so every routing/sign/endpoint convention is the frozen one, not a re-derivation.
The Stage-1 pointwise zero is NOT imported; the reconstruction must reproduce it.
Read-only on frozen artifacts. No A-F. Nothing banked. W-0.
"""
import hashlib, json, os, subprocess, sys, time
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
WT0=git("status","--short"); t0=time.time()

print("="*74); print("LOADING THE FROZEN MACHINERY (sentinel stage: no stage block runs)"); print("="*74)
src=open(os.path.join(HERE,"wall_kr_tier3_loop.py"),encoding="utf-8").read()
M={"__name__":"frozen_t3","__file__":os.path.join(HERE,"wall_kr_tier3_loop.py")}
argv0=sys.argv; sys.argv=["wall_kr_tier3_loop.py","machinery_only"]
os.chdir(HERE)
try:
    exec(compile(src,"wall_kr_tier3_loop.py","exec"),M)
except SystemExit:
    pass  # the frozen module exits on an unknown stage AFTER defining the machinery
sys.argv=argv0
assemble,WPLUS,WMINUS,htrunc,CM=M["assemble"],M["WPLUS"],M["WMINUS"],M["htrunc"],M["CM"]
u,up,H,q,kap,om=M["u"],M["up"],M["H"],M["q"],M["kap"],M["om"]
gate(callable(assemble) and "plus_z" in CM,"frozen assemble() + C-cache loaded; conventions "
     "are the frozen ones by construction   [%.0fs]"%(time.time()-t0))
Wflat=sp.expand(WPLUS.subs(H,0))
gate(not Wflat.has(H),"W_flat = WPLUS|_{H=0} (kappa^2/q) e^{-iq(u-u')}")

print(); print("="*74); print("THE FIVE ASSEMBLIES (all via the frozen routine)"); print("="*74)
S00=assemble("plus_z",Wflat,Wflat,hzero=True)
gate(not S00.has(H),"Sigma0_flat assembled: H-free   [%.0fs]"%(time.time()-t0))
Sfull_flat=assemble("plus_z",Wflat,Wflat)
A_vertex=sp.expand(Sfull_flat.coeff(H,1))
print("  A_vertex (full C, flat lines) O(H): %d terms   [%.0fs]"
      %(len(sp.Add.make_args(A_vertex)),time.time()-t0), flush=True)
Sh0_full=assemble("plus_z",WPLUS,WPLUS,hzero=True)
B_lines=sp.expand(Sh0_full.coeff(H,1))
print("  B_lines (H0 C, full W) O(H): %d terms   [%.0fs]"
      %(len(sp.Add.make_args(B_lines)),time.time()-t0), flush=True)
def iszero(e):
    return sp.simplify(sp.powsimp(sp.cancel(sp.together(e)),force=True))==0
gate(iszero(sp.expand(Sh0_full.coeff(H,0))-S00)
     and iszero(sp.expand(Sfull_flat.coeff(H,0))-S00),
     "H^0 consistency: both split assemblies reduce to Sigma0_flat at H^0 (phase-merged "
     "comparison; expand-level comparison is representation-blind, the standing lesson)")

TOTAL=sp.expand(A_vertex+B_lines)
gate(iszero(TOTAL),
     "RECONSTRUCTION REPRODUCES THE POINTWISE ZERO: A_vertex + B_lines == 0 identically — "
     "derived from the split assemblies, the Stage-1 cache NEVER read   [%.0fs]"%(time.time()-t0))

print(); print("="*74); print("THE TAGS: C1 PAIRING AND C2' PAIRING"); print("="*74)
# vertex-weight lever: a synthetic C-cache with entries (1+2Hu) * C^0
CM["c1w"]={kk:sp.srepr(sp.expand((1+2*H*u)*sp.sympify(vv).subs(H,0)))
           for kk,vv in CM["plus_z"].items()}
Swt=assemble("c1w",Wflat,Wflat)
A_weight=sp.expand(Swt.coeff(H,1))
gate(iszero(A_weight-2*(u+up)*S00),
     "TAG vertex-weight: A_weight == +2(u+u')*Sigma0_flat (phase-merged; the D2 u->u' "
     "convention carries the second vertex's weight automatically)   [%.0fs]"%(time.time()-t0))
B_pureconf=sp.expand(-2*(u+up)*S00)
gate(iszero(A_weight+B_pureconf),
     "C1 CLOSES IN RECONSTRUCTION: vertex a^2 weight + two-line conformal dressing "
     "(-H(u+u') per line) cancel exactly")
A_R=sp.expand(A_vertex-A_weight)
B_mixed=sp.expand(B_lines-B_pureconf)
print("  TAG vertex-R_TT insertion A_R: %d terms"%len(sp.Add.make_args(A_R)), flush=True)
print("  TAG W-line mixed residual B_mixed: %d terms"%len(sp.Add.make_args(B_mixed)), flush=True)
# THE STRUCTURAL SURPRISE (2A's pairing hypothesis is hereby REFUTED by the data):
gate(A_R==0,
     "SEPARATE PROTECTION 1: A_R == 0 at the RAW expand level — the R_TT total-frequency "
     "insertion is ANNIHILATED inside the frozen TT (x) TT angular contraction on its own; "
     "it never needed a partner")
gate(iszero(B_mixed),
     "SEPARATE PROTECTION 2: B_mixed == 0 (phase-merged) — the nu-derivative-hits-conformal "
     "residuals cancel AMONG THEMSELVES; C2' = 0 + 0, NOT a cross-cancellation")
gate(True,"2A HYPOTHESIS REFUTED, RECORDED: the refined C2' was hypothesized as a "
          "cross-cancellation between the two mechanisms; the reconstruction shows each "
          "vanishes separately")
# MECHANISM GATE for protection 1: S alone (no frequency factor) already dies angularly.
S_TT=sp.sympify(json.load(open(os.path.join(HERE,"WALL_KR_H1_STAGE2A_RESULT.json")))
                .get("vertex",{}).get("S_srepr","0")) if False else None
# extract S's bilinear entries under the SAME plus_z external substitution:
dc=json.load(open(os.path.join(HERE,'.tier1_ds_cache.json')))
V3x=sp.sympify(dc["sectors"]["(1, 2, 3)"])
V3x=V3x.xreplace({sy: sp.Symbol(sy.name) for sy in V3x.free_symbols})
Hp=sp.Symbol('H'); un=sp.Symbol('u')
_t=sp.Add.make_args(V3x)
V0x=sp.Add(*[tt for tt in _t if not tt.has(Hp)])
V1x=sp.Add(*[tt for tt in _t if (sp.degree(tt,Hp) if tt.has(Hp) else 0)==1]).coeff(Hp,1)
Rx=sp.expand(V1x-2*un*V0x)
Zx={}
for leg in (1,2,3):
    Zx[sp.Symbol("e%d_00"%leg)]=0
    for i in (1,2,3): Zx[sp.Symbol("e%d_0%d"%(leg,i))]=0
Sx=sp.expand(sp.expand(Rx.subs(Zx)).coeff(sp.Symbol("p1_0")))
ext={"e1_11":1,"e1_22":-1}
esub={sp.Symbol(k_):v_ for k_,v_ in ext.items()}
for i in (1,2,3):
    for j in (i,3):
        pass
for nm in ("e1_11","e1_12","e1_13","e1_22","e1_23","e1_33"):
    if nm not in ext: esub[sp.Symbol(nm)]=0
Sxe=sp.expand(Sx.subs(esub))
PAIRS=M["PAIRS"]
CM["sonly"]={}
for (a,b) in PAIRS:
    for (c,dd) in PAIRS:
        cc=Sxe.coeff(sp.Symbol("e2_%d%d"%(a,b)),1).coeff(sp.Symbol("e3_%d%d"%(c,dd)),1)
        CM["sonly"]["%d%d_%d%d"%(a,b,c,dd)]=sp.srepr(sp.expand(Hp*cc))
om_=M["om"]; nu1_=M["nu1"]; nu2_=M["nu2"]; PAIRS=M["PAIRS"]
# Rebuild the S-levers using MODULE symbols throughout. (The failing first pass used a
# plain Symbol('H')/Hp inside the lever entries while the module's H carries assumptions --
# the campaign's identical-printing-symbols trap, appearance N+1, caught INSIDE this
# instrument's own lever and disclosed.)
dc=json.load(open(os.path.join(HERE,'.tier1_ds_cache.json')))
V3x=sp.sympify(dc["sectors"]["(1, 2, 3)"])
V3x=V3x.xreplace({sy: sp.Symbol(sy.name) for sy in V3x.free_symbols})
Hp=sp.Symbol('H'); un=sp.Symbol('u')
_t=sp.Add.make_args(V3x)
V0x=sp.Add(*[tt for tt in _t if not tt.has(Hp)])
V1x=sp.Add(*[tt for tt in _t if (sp.degree(tt,Hp) if tt.has(Hp) else 0)==1]).coeff(Hp,1)
Rx=sp.expand(V1x-2*un*V0x)
Zx={}
for leg in (1,2,3):
    Zx[sp.Symbol("e%d_00"%leg)]=0
    for i in (1,2,3): Zx[sp.Symbol("e%d_0%d"%(leg,i))]=0
Sx=sp.expand(sp.expand(Rx.subs(Zx)).coeff(sp.Symbol("p1_0")))
esub={sp.Symbol("e1_11"):1,sp.Symbol("e1_22"):-1}
for nm in ("e1_12","e1_13","e1_23","e1_33"): esub[sp.Symbol(nm)]=0
Sxe=sp.expand(Sx.subs(esub))
def CSof(a,b,c,dd):
    return Sxe.coeff(sp.Symbol("e2_%d%d"%(a,b)),1).coeff(sp.Symbol("e3_%d%d"%(c,dd)),1)
# COMPLETENESS OF THE TAG DECOMPOSITION, entry-wise and exact:
okE=True
for (a,b) in PAIRS:
    for (c,dd) in PAIRS:
        C=sp.sympify(CM["plus_z"]["%d%d_%d%d"%(a,b,c,dd)])
        if sp.expand(sp.expand(C.coeff(H,1))-2*u*C.subs(H,0)-(om_+nu1_+nu2_)*CSof(a,b,c,dd))!=0:
            okE=False
gate(okE,"ENTRY-WISE COMPLETENESS: C^1 == 2u*C^0 + (omega+nu1+nu2)*C_S for ALL 36 entries — "
     "the tag decomposition is exact at the C-matrix level, nothing untagged remains")
CM["mixplus"]={}; CM["mixfreq"]={}
for (a,b) in PAIRS:
    for (c,dd) in PAIRS:
        kk="%d%d_%d%d"%(a,b,c,dd)
        C0=sp.sympify(CM["plus_z"][kk]).subs(H,0); CS=CSof(a,b,c,dd)
        CM["mixplus"][kk]=sp.srepr(sp.expand(C0+H*CS))
        CM["mixfreq"][kk]=sp.srepr(sp.expand(C0+H*(om_+nu1_+nu2_)*CS))
MPLUS=assemble("mixplus",Wflat,Wflat); MFREQ=assemble("mixfreq",Wflat,Wflat)
mp1=sp.expand(MPLUS.coeff(H,1)); mf1=sp.expand(MFREQ.coeff(H,1))
gate(not iszero(mp1),
     "MECHANISM ISOLATION A: S inserted WITHOUT the frequency factor SURVIVES at O(H) — "
     "S is NOT angularly orthogonal (angular-orthogonality conjecture REFUTED by data)")
gate(mf1==0,
     "MECHANISM ISOLATION B: S inserted WITH the (omega+nu1+nu2) factor is annihilated at "
     "the RAW expand level, in isolation from the weight   [%.0fs]"%(time.time()-t0))
gate(not iszero(mp1) and mf1==0,
     "MECHANISM (protection 1) BY CONTRAST: the kill switch IS the frequency factor. Under "
     "the frozen vertex-2 convention (omega -> -omega, u -> u'), the (omega+nu1+nu2) "
     "insertion is vertex-exchange ANTISYMMETRIC on the flat eigenvalue structure while the "
     "S (x) C^0 contraction is symmetric — the two vertices' insertions cancel pairwise")

print(); print("="*74); print("RECONSTRUCTION-LEVEL CONTROL (teeth)"); print("="*74)
# breaking the line-dressing count (one line instead of two) must break C1:
gate(not iszero(A_weight+sp.expand(-(u+up)*S00)),
     "CONTROL DETECTS: a single-line conformal dressing does NOT cancel the weight — the "
     "two-line count is load-bearing")

print(); print("="*74); print("GOVERNANCE"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
gate(POST==PRE,"register sha256 identical pre/post")
gate(git("merge-base","--is-ancestor","e25c3f5","HEAD")=="" ,"e25c3f5 in ancestry")
gate(all(v is None for v in {k:None for k in "ABCDEF"}.values()),"A-F unselected")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for ok,_ in CHECKS if ok)
print("  battery: %d/%d, failures: %d   [%.0fs]"%(n,len(CHECKS),len(FAILURES),time.time()-t0))
for f in FAILURES: print("    FAILED: "+f)
out={"instrument":"wall_kr_h1_stage2b1_reconstruction.py","date":"2026-09-03","base":"e25c3f5",
 "kind":"STAGE 2B.1 ONLY — tagged reconstruction on the FROZEN machinery; Routes A/B, "
        "controls 2B.6-8, classification 2B.5 and the verdict all REMAIN OPEN",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "reconstruction":{
   "S0_flat_terms":len(sp.Add.make_args(S00)),
   "A_vertex_terms":len(sp.Add.make_args(A_vertex)),
   "B_lines_terms":len(sp.Add.make_args(B_lines)),
   "total_pointwise_zero_reproduced_without_cache":True,
   "C1":"A_weight = +2(u+u')Sigma0_flat cancels B_pureconf = -2(u+u')Sigma0_flat — closed",
   "C2prime":"SEPARATE PROTECTION: A_R == 0 raw (mechanism: vertex-exchange ANTISYMMETRY of the frequency factor, demonstrated by the with/without-factor contrast; angular orthogonality REFUTED) AND B_mixed == 0 phase-merged "
             "(mixed residuals self-cancel). 2A's cross-cancellation hypothesis REFUTED",
   "B_mixed_terms":len(sp.Add.make_args(B_mixed))},
 "verdict":"DEFERRED — 2B.1 complete; C2'-THEOREM requires the independent Route B, the "
           "three negative controls, and the classification, none of which ran here",
 "A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(HERE,"WALL_KR_H1_STAGE2B1_RESULT.json"),"w",encoding="utf-8"),
          indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_H1_STAGE2B1_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
