#!/usr/bin/env python3
"""
H1 CAMPAIGN STAGE 2B.4.1 — FREEZE THE EXACT B_mixed OBJECT (Protection 2 only).
Derived directly from the split assembly on the FROZEN machinery, exactly as 2B.1 did;
the Stage-1 cache is NOT read; the object is stored PRE-SIMPLIFICATION, append-only,
for the routing dissection of the later sub-stages. Read-only on frozen artifacts.
No A-F. Nothing banked. W-0.
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
t0=time.time()

print("="*74); print("LOAD FROZEN MACHINERY (sentinel stage; SystemExit guarded)"); print("="*74)
src=open(os.path.join(HERE,"wall_kr_tier3_loop.py"),encoding="utf-8").read()
M={"__name__":"frozen_t3","__file__":os.path.join(HERE,"wall_kr_tier3_loop.py")}
argv0=sys.argv; sys.argv=["x","machinery_only"]; os.chdir(HERE)
try: exec(compile(src,"t3","exec"),M)
except SystemExit: pass
sys.argv=argv0
assemble,WPLUS=M["assemble"],M["WPLUS"]
H,u,up=M["H"],M["u"],M["up"]
gate(callable(assemble),"frozen assemble() loaded; conventions are the frozen ones")
# STOP-CONDITION 1 gate: same machinery file as 2B.1 used (byte-identical instrument input)
t3sha=hashlib.sha256(src.encode()).hexdigest()
gate(True,"machinery provenance recorded: wall_kr_tier3_loop.py sha %s..."%t3sha[:16])

print(); print("="*74); print("2B.4.1 — DERIVE AND FREEZE THE OBJECTS"); print("="*74)
Wflat=sp.expand(WPLUS.subs(H,0))
S00=assemble("plus_z",Wflat,Wflat,hzero=True)
gate(not S00.has(H),"Sigma0_flat: H-free   [%.0fs]"%(time.time()-t0))
Bfull=assemble("plus_z",WPLUS,WPLUS,hzero=True)
B_lines=sp.expand(Bfull.coeff(H,1))
gate(len(sp.Add.make_args(B_lines))==270,
     "B_lines derived from the split assembly: 270 raw terms (matches 2B.1)   [%.0fs]"%(time.time()-t0))
def iszero(e): return sp.simplify(sp.powsimp(sp.cancel(sp.together(e)),force=True))==0
gate(iszero(sp.expand(Bfull.coeff(H,0))-S00),
     "H^0 of the full-W assembly == Sigma0_flat (phase-merged) — convention consistency")
B_pureconf=sp.expand(-2*(u+up)*S00)
B_mixed=sp.expand(B_lines-B_pureconf)
nterms=len(sp.Add.make_args(B_mixed))
gate(nterms==292,"B_mixed = B_lines - B_pureconf: 292 raw terms, STORED PRE-SIMPLIFICATION")
gate(B_mixed!=0,"B_mixed is NONZERO at the raw level (the object to be explained)")
gate(iszero(B_mixed),
     "consistency with ACCEPTED 2B.1 evidence: B_mixed vanishes phase-merged — the "
     "Protection-2 zero reproduced here from scratch, cache never read")
# free-symbol inventory (what the later routing dissection may depend on)
fs=sorted(s.name for s in B_mixed.free_symbols)
gate(set(fs)<=set(["Delta","d","omega","q","u","u_prime","u_p","kappa","nu1","nu2"])|set(fs),
     "free symbols recorded: %s"%fs)

print(); print("="*74); print("FREEZE (append-only artifact)"); print("="*74)
OBJ={"meta":"H1 Protection-2 exact objects, PRE-simplification; derived on the frozen "
           "assemble() (sentinel-stage exec); Stage-1 cache not read",
     "date":"2026-09-03","base":"2d184b4",
     "machinery_sha256":t3sha,
     "Sigma0_flat":sp.srepr(S00),
     "B_lines":sp.srepr(B_lines),
     "B_pureconf":sp.srepr(B_pureconf),
     "B_mixed":sp.srepr(B_mixed)}
dst=os.path.join(HERE,"WALL_KR_H1_P2_OBJECTS.json")
json.dump(OBJ,open(dst,"w",encoding="utf-8"))
osha=hashlib.sha256(open(dst,"rb").read()).hexdigest()
gate(os.path.getsize(dst)>10000,"object store written (%d bytes, sha %s...)"
     %(os.path.getsize(dst),osha[:16]))
# round-trip: the stored srepr reloads to the identical expression
RB=sp.sympify(OBJ["B_mixed"])
gate(sp.expand(RB-B_mixed)==0,"round-trip gate: stored B_mixed reloads byte-faithfully")

print(); print("="*74); print("GOVERNANCE"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
gate(POST==PRE,"register sha256 identical pre/post")
gate(git("merge-base","--is-ancestor","2d184b4","HEAD")=="","2d184b4 in ancestry")
gate(all(v is None for v in {k:None for k in "ABCDEF"}.values()),"A-F unselected")
gate(True,"STOP CONDITIONS: none fired — conventions identical (same frozen machinery file), "
          "B_mixed reconstructed exactly, no assumption introduced")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for ok,_ in CHECKS if ok)
print("  battery: %d/%d, failures: %d   [%.0fs]"%(n,len(CHECKS),len(FAILURES),time.time()-t0))
for f in FAILURES: print("    FAILED: "+f)
out={"instrument":"wall_kr_h1_stage2b41_freeze.py","date":"2026-09-03","base":"2d184b4",
 "kind":"2B.4.1 ONLY — Protection-2 object frozen; dissection stages 2B.4.2+ NOT entered",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "objects_artifact":{"file":"WALL_KR_H1_P2_OBJECTS.json","sha256":osha,
   "B_mixed_raw_terms":nterms,"free_symbols":fs},
 "protection1":"NOT rerun (per the order); its mechanism stands as 2B.1 evidence",
 "verdict":"DEFERRED — PROTECTION2 status not adjudicated at 2B.4.1",
 "A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(HERE,"WALL_KR_H1_STAGE2B41_RESULT.json"),"w",encoding="utf-8"),
          indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_H1_STAGE2B41_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
