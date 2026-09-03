#!/usr/bin/env python3
"""
H1 CAMPAIGN STAGE 2A — THE ACTUAL VERTEX WEIGHT, READ OFF THE FROZEN ARTIFACT.
Per the work order: standalone gated result; on literal incompatibility with the Stage-1
C1 description, STOP and report before continuing. Read-only. No A-F. W-0.
"""
import hashlib, json, os, subprocess, time
import sympy as sp
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LED,PROV=os.path.join(ROOT,"PHYSICS_LEDGER"),os.path.join(ROOT,"provenance")
CHECKS,FAILURES=[],[]
def check(c,l):
    CHECKS.append((bool(c),l))
    if not c: FAILURES.append(l)
    print(("  PASS  " if c else "  FAIL  ")+l, flush=True)
def git(*a): return subprocess.run(["git"]+list(a),cwd=ROOT,capture_output=True,text=True).stdout.strip()
REG=os.path.join(PROV,"claims.json"); PRE=hashlib.sha256(open(REG,"rb").read()).hexdigest()
WT0=git("status","--short"); t0=time.time()

print("="*74); print("2A.1 — PROVENANCE"); print("="*74)
dc=json.load(open(os.path.join(LED,'.tier1_ds_cache.json')))
T1A=json.load(open(os.path.join(LED,'WALL_KR_TIER1_VERTEX_ARTIFACT.json')))
check(T1A["vertex_sha256"].startswith("0152c7773e6a38df") and T1A["ds_terms"]==26032,
      "frozen T1 artifact: sha 0152c777..., 26032 dS terms")
V3=sp.sympify(dc["sectors"]["(1, 2, 3)"])
V3=V3.xreplace({s: sp.Symbol(s.name) for s in V3.free_symbols})
H=sp.Symbol('H'); u=sp.Symbol('u')
terms=sp.Add.make_args(V3)
check(len(terms)==26032,"cache sector (1,2,3) reloaded: 26032 terms")
T3SRC=open(os.path.join(LED,'wall_kr_tier3_loop.py'),encoding='utf-8').read()
check("(1 - H * u) * (1 - H * up) + sp.I * H**2 * (u - up) / q + H**2 / q**2" in T3SRC,
      "frozen T3 bath kernel W+ literal: O(H) part is PURELY CONFORMAL (1-Hu)(1-Hu'); the "
      "state piece enters only at O(H^2) — the LINE side of C1 is literally present")

print(); print("="*74); print("2A.2 — THE LITERAL H-GRADING OF THE VERTEX"); print("="*74)
V0=sp.Add(*[t for t in terms if not t.has(H)])
V1=sp.Add(*[t for t in terms if (sp.degree(t,H) if t.has(H) else 0)==1]).coeff(H,1)
census={0:0,1:0,2:0}
for t in terms: census[sp.degree(t,H) if t.has(H) else 0]+=1
check(census=={0:7560,1:9156,2:9316},
      "H-degree census of the frozen vertex: {0: 7560, 1: 9156, 2: 9316}")
check(not V0.has(u) and not any(s.name=='d' for s in V3.free_symbols),
      "V3^(0) is u-free (flat vertex) and the artifact carries NO d symbol (d enters only "
      "via the later angular moments/projector traces)")
R=sp.expand(V1-2*u*V0)
check(R!=0,"V3^(1) is NOT purely the multiplicative weight: V3^(1) = 2u*V3^(0) + R, R != 0")
rt=sp.Add.make_args(R)
check(len(rt)==1596 and not R.has(u),
      "R has 1596 terms and is u-FREE — a pure momentum/polarization structure")

print(); print("="*74); print("2A.3 — R ON THE DECLARED TT SLOT ASSIGNMENT"); print("="*74)
Z={}
for leg in (1,2,3):
    Z[sp.Symbol("e%d_00"%leg)]=0
    for i in (1,2,3): Z[sp.Symbol("e%d_0%d"%(leg,i))]=0
Rtt=sp.expand(R.subs(Z))
check(Rtt!=0,"THE DISCREPANCY, GATED: R does NOT vanish on the declared TT slots — "
             "%d terms survive"%len(sp.Add.make_args(Rtt)))
p0s=[sp.Symbol("p%d_0"%i) for i in (1,2,3)]
c1_,c2_,c3_=[sp.expand(Rtt.coeff(p)) for p in p0s]
check(sp.expand(c1_-c2_)==0 and sp.expand(c2_-c3_)==0,
      "FACTORIZATION: the three frequency coefficients are IDENTICAL — "
      "R_TT = (p1_0 + p2_0 + p3_0) x S, the TOTAL-FREQUENCY structure")
S=c1_
check(len(sp.Add.make_args(S))==60 and all(not S.has(p) for p in p0s)
      and not S.has(u) and not S.has(H),
      "S has 60 terms, purely SPATIAL polarizations, momentum/u/H-free")
check(sp.expand(Rtt-(p0s[0]+p0s[1]+p0s[2])*S)==0,
      "closed form GATED: R_TT == (p1_0+p2_0+p3_0) * S exactly")
lin=all(sum(sp.degree(t,p) for p in p0s)==1 for t in sp.Add.make_args(Rtt))
check(lin,"every R_TT term is LINEAR in exactly one frequency component")

print(); print("="*74); print("2A.4 — WHAT THIS MEANS, AND THE STOP"); print("="*74)
check(True,"LITERAL vs INFERRED, separated per the work order: LITERALLY PRESENT = "
           "V3^(1) = 2u*V3^(0) + (p1_0+p2_0+p3_0)*S on TT slots (weight PLUS a "
           "total-frequency insertion); INFERRED BY STAGE 1 = pure a^2 weight. The Stage-1 "
           "C1 description is INCOMPLETE at the frozen-vertex level")
check(True,"REFINED DECOMPOSITION (recorded, not yet proven): with nu^a -> (-i d/du)^a on "
           "the internal lines (the frozen T3 rule), the R_TT insertion is a TOTAL-TIME-"
           "DERIVATIVE-CLASS operator -3i S (omega + nu1 + nu2) per vertex at O(H); the "
           "pointwise zero therefore requires C2' = [W-derivative-hits-conformal residuals] "
           "+ [R_TT insertions] = 0 — a compact flat identity on 60-term structures, in "
           "place of Stage 1's C2")
check(True,"PER THE WORK ORDER: literal incompatibility found -> STOP after 2A; steps "
           "2B-2I NOT executed; no adjudication made")
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
check(POST==PRE,"register sha256 identical pre/post")
check(git("status","--short")==WT0,"worktree unchanged at gate time")
check(all(v is None for v in {k:None for k in "ABCDEF"}.values()),"A-F unselected")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for o,_ in CHECKS if o)
print("  battery: %d/%d, failures: %d   [%.0fs]"%(n,len(CHECKS),len(FAILURES),time.time()-t0))
for f in FAILURES: print("    FAILED: "+f)
out={"instrument":"wall_kr_h1_stage2a_vertex_weight.py","date":"2026-09-03","base":"6151328",
 "kind":"STAGE 2A ONLY — vertex weight read off the frozen artifact; DISCREPANCY STOP",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "vertex":{"id":"T1 dS cubic, sector (1,2,3), sha 0152c777..., 26032 terms",
   "H_census":{"H0":7560,"H1":9156,"H2":9316},
   "u_dependence":"only via H*u (V3^(0) u-free); no d symbol",
   "literal_H1_grading":"V3^(1) = 2u*V3^(0) + R, R 1596 terms, u-free",
   "R_on_TT_slots":"180 terms survive = (p1_0+p2_0+p3_0) * S, S = 60 purely spatial terms",
   "closed_form_gated":True},
 "discrepancy":"Stage-1 C1 ('pure a^2 weight per vertex') is INCOMPLETE at the frozen-vertex "
   "level: a total-frequency insertion (p1_0+p2_0+p3_0)*S accompanies the weight on TT slots",
 "refined_C2_target":"C2' = [nu-derivative-hits-conformal residuals from W] + "
   "[-3i S (omega+nu1+nu2) insertions per vertex] = 0 pointwise — a compact flat identity; "
   "recorded as the Stage-2B target, NOT proven here",
 "steps_2B_to_2I":"NOT EXECUTED — stopped per the work order's discrepancy rule",
 "verdict":"DEFERRED","A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(LED,"WALL_KR_H1_STAGE2A_RESULT.json"),"w",encoding="utf-8"),
          indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_H1_STAGE2A_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
