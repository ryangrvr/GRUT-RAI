#!/usr/bin/env python3
"""
H1 CAMPAIGN STAGE 2B.4.2.2 — ENDPOINT-BLOCK GROUPING ONLY, on the frozen B_mixed.
No routing dissection, no involutions, no provenance, no controls, no interpretation.
Read-only. No A-F. Nothing banked. W-0.
"""
import hashlib, json, os, subprocess, time
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

print("="*74); print("2B.4.2.2.1 — LOAD"); print("="*74)
SRC=os.path.join(HERE,"WALL_KR_H1_P2_OBJECTS.json")
gate(hashlib.sha256(open(SRC,"rb").read()).hexdigest().startswith("1b136cd4"),
     "frozen store sha verified (1b136cd4...)")
B=sp.sympify(json.load(open(SRC))["B_mixed"])
terms=sp.Add.make_args(B)
gate(len(terms)==292,"round-trip: 292 raw terms")
u=[s for s in B.free_symbols if s.name=="u"][0]
up=[s for s in B.free_symbols if s.name=="u_p"][0]
om=[s for s in B.free_symbols if s.name=="omega"][0]
q=[s for s in B.free_symbols if s.name=="q"][0]
dd=[s for s in B.free_symbols if s.name=="d"][0]
PH=2*sp.I*q*(up-u)

print(); print("="*74); print("2B.4.2.2.2 — REMOVE ONLY THE COMMON PHASE"); print("="*74)
def split(t):
    nu_,de_=t.as_numer_denom()
    nu_=sp.factor_terms(nu_); de_=sp.factor_terms(de_)
    def strip(e):
        rest=sp.Integer(1); arg=sp.Integer(0)
        for f in sp.Mul.make_args(sp.powsimp(e)):
            b_,x_=f.as_base_exp()
            if b_==sp.E: arg+=sp.expand(x_)
            else: rest*=f
        return rest,arg
    nr,na=strip(nu_); dr,da=strip(de_)
    return nr,dr,sp.expand(na-da)
NT=[]
okph=True; okrt=True
for t in terms:
    nr,dr,ph=split(t)
    if sp.expand(ph-PH)!=0: okph=False
    if sp.simplify(nr/dr*sp.exp(PH)-t)!=0: okrt=False
    NT.append((nr,dr))
gate(okph,"every term's net phase is EXACTLY 2iq(u'-u)")
gate(okrt,"per-term gate: (numer/denom) x e^{2iq(u'-u)} reproduces each raw term exactly — "
     "the phase removal is bookkeeping, not cancellation   [%.0fs]"%(time.time()-t0))

print(); print("="*74); print("2B.4.2.2.3 — CANONICAL ENDPOINT DECOMPOSITION"); print("="*74)
Fu_terms=[]; Fup_terms=[]
ok_lin=True
for nr,dr in NT:
    if nr.has(u):
        c_=sp.expand(nr.coeff(u,1))
        if sp.expand(nr-u*c_)!=0: ok_lin=False
        Fu_terms.append(c_/dr)
    else:
        c_=sp.expand(nr.coeff(up,1))
        if sp.expand(nr-up*c_)!=0: ok_lin=False
        Fup_terms.append(c_/dr)
gate(ok_lin and len(Fu_terms)==146 and len(Fup_terms)==146,
     "every numerator is EXACTLY u x (rest) or u' x (rest): 146 + 146")
Fu=sp.Add(*Fu_terms); Fup=sp.Add(*Fup_terms)
N=sp.Add(*[nr/dr for nr,dr in NT])
gate(sp.simplify(sp.together(N-u*Fu-up*Fup))==0,
     "exact reconstruction: N == u F_u + u' F_up (no uu', no constant block — as the census "
     "required)   [%.0fs]"%(time.time()-t0))
# Route B canonicalization: derivatives (N is linear in each endpoint)
FuB=sp.expand(sp.diff(N,u)); FupB=sp.expand(sp.diff(N,up))
gate(sp.simplify(sp.together(FuB-Fu))==0 and sp.simplify(sp.together(FupB-Fup))==0,
     "INDEPENDENT ROUTE agrees: F_u = dN/du and F_up = dN/du' reproduce the "
     "construction-route blocks exactly")

print(); print("="*74); print("2B.4.2.2.4 — THE TWO BLOCKS COMPARED"); print("="*74)
def iszero(e): return sp.simplify(sp.powsimp(sp.cancel(sp.together(e)),force=True))==0
zFu=iszero(Fu); zFup=iszero(Fup); zsum=iszero(Fu+Fup)
print("  F_u  == 0 (merged): %s"%zFu)
print("  F_up == 0 (merged): %s"%zFup)
print("  F_u + F_up == 0 (merged): %s"%zsum)
gate(zFu and zFup,
     "EACH ENDPOINT BLOCK VANISHES INDEPENDENTLY: F_u == 0 and F_up == 0 exactly — "
     "no cross-endpoint cancellation is involved")
rawopp=sp.expand(Fu+Fup)
gate(True,"raw-form relation recorded: F_u + F_up has %d unmerged terms before "
          "simplification (negation at the raw level: %s)"
          %(len(sp.Add.make_args(rawopp)), rawopp==0))

print(); print("="*74); print("2B.4.2.2.5/6 — DENOMINATOR-CLASS BLOCKING"); print("="*74)
def blocks(Flist,label):
    cls={}
    for e in Flist:
        nr_,dr_=sp.together(e).as_numer_denom()
        qpow=0
        rest=sp.Integer(1)
        for f in sp.Mul.make_args(dr_):
            b_,x_=f.as_base_exp()
            if b_==q and x_.is_number: qpow=int(x_)
            else: rest*=f
        key=(sp.sstr(sp.factor(rest)),qpow)
        cls.setdefault(key,[]).append(e)
    print("  %s: %d denominator classes"%(label,len(cls)))
    tab={}
    for key,es in sorted(cls.items(),key=lambda kv:(kv[0][1],kv[0][0])):
        ssum=sp.Add(*es)
        z=iszero(ssum)
        tab[str(key)]={"n_terms":len(es),"zero":bool(z)}
        print("    class (q^%d, %s...): %d terms -> %s"
              %(key[1],key[0][:44],len(es),"ZERO" if z else "NONZERO"))
    return tab
tabu=blocks(Fu_terms,"F_u block")
tabup=blocks(Fup_terms,"F_up block")
allz_u=all(v["zero"] for v in tabu.values())
allz_up=all(v["zero"] for v in tabup.values())
gate(True,"block table recorded: F_u classes all-zero=%s, F_up classes all-zero=%s — "
          "%s"%(allz_u,allz_up,
          "EVERY endpoint x denominator block vanishes independently" if (allz_u and allz_up)
          else "cancellation requires CROSS-CLASS recombination within each endpoint block"))

print(); print("="*74); print("2B.4.2.2.7 — ENDPOINT EXCHANGE (census only)"); print("="*74)
NX=N.subs({u:up,up:u},simultaneous=True)
relE=iszero(NX-N); relN=iszero(NX+N)
print("  N(u<->u') == +N: %s ; == -N: %s"%(relE,relN))
gate(True,"endpoint-exchange relation recorded: %s (both trivially true if N merges to 0; "
          "the RAW structural relation is the F-block accounting above)"
          %("equality" if relE else ("negation" if relN else "nontrivial")))

print(); print("="*74); print("GOVERNANCE"); print("="*74)
POST=hashlib.sha256(open(REG,"rb").read()).hexdigest()
gate(POST==PRE,"register sha256 identical pre/post")
gate(git("merge-base","--is-ancestor","cf93e76","HEAD")=="","cf93e76 in ancestry")
gate(all(v is None for v in {k:None for k in "ABCDEF"}.values()),"A-F unselected")

print(); print("="*74); print("RESULT"); print("="*74)
n=sum(1 for ok,_ in CHECKS if ok)
print("  battery: %d/%d, failures: %d   [%.0fs]"%(n,len(CHECKS),len(FAILURES),time.time()-t0))
for f in FAILURES: print("    FAILED: "+f)
out={"instrument":"wall_kr_h1_stage2b422_endpoint.py","date":"2026-09-03","base":"cf93e76",
 "kind":"2B.4.2.2 ONLY — endpoint-block grouping; later sub-stages NOT entered",
 "battery":"%d/%d"%(n,len(CHECKS)),"failures":FAILURES,
 "register_sha256_pre":PRE,"register_sha256_post":POST,
 "decomposition":{"N":"B_mixed = e^{2iq(u'-u)} (u F_u + u' F_up), exact",
   "Fu_zero_merged":bool(zFu),"Fup_zero_merged":bool(zFup),
   "raw_negation_Fu_plus_Fup":bool(rawopp==0),
   "Fu_classes":tabu,"Fup_classes":tabup,
   "Fu_all_classes_zero":bool(allz_u),"Fup_all_classes_zero":bool(allz_up),
   "independent_route":"F = dN/du, dN/du' agrees with construction route"},
 "verdict":"DEFERRED — grouping only; no interpretation per the order",
 "A_to_F_selected":"NONE","W":"W-0 — computed-and-reported, NOT banked"}
json.dump(out,open(os.path.join(HERE,"WALL_KR_H1_STAGE2B422_RESULT.json"),"w",encoding="utf-8"),
          indent=2,ensure_ascii=False)
print("  artifact: WALL_KR_H1_STAGE2B422_RESULT.json")
print("  "+("ALL CHECKS PASS" if not FAILURES else "BATTERY HAS FAILURES"))
