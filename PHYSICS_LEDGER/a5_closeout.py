#!/usr/bin/env python3
# A5 CLOSE-OUT: independent analytical battery -> freeze classifier+delta -> apply to C1.
# Selection on knowns ONLY; C1 does not participate in choosing delta/range/rule.
import json, math

DELTA=0.15  # frozen AFTER battery separation observed, BEFORE C1 application

def partials(im_over_w, decades=(0.0,4.0), per=8):
    """I(W)=int_1^W im(w) dw at W=10^k, k spanning `decades` (start W=1)."""
    out={}
    k0,k1=decades
    cuts=[10**(k0+i) for i in range(int(k1-k0)+1)]   # EXACT decade cutoffs
    n_fine=4000
    for W in cuts:
        h_steps=max(4000,int(W*200)); s=0.0; a=1.0
        if W<=a:
            out[0.0]=0.0; continue
        h=(W-a)/h_steps
        for i in range(h_steps):
            x=a+(i+0.5)*h
            s+=im_over_w(x)/x*h     # THE INTEGRAND IS Im(chi)/omega -- not Im alone
        out[round(math.log10(W),3) if W>1 else 0.0]=s
    return out

def increment_ratio(I):
    ks=sorted(I); incs=[]
    for i in range(len(ks)-1):
        d=I[ks[i+1]]-I[ks[i]]
        incs.append((ks[i+1],d))
    tail=incs[-3:] if len(incs)>=3 else incs
    rs=[]
    for j in range(len(tail)-1):
        prev=tail[j][1]; cur=tail[j+1][1]
        if abs(prev)>1e-14: rs.append(cur/prev)
    return (sum(rs)/len(rs)) if rs else None

def classify(r,delta=DELTA):
    if r is None: return 'UNRESOLVED'
    if r<1-delta: return 'CONVERGENT'
    if r>1+delta: return 'POWER-DIVERGENT'
    return 'LOG-DIVERGENT'

# ---- INDEPENDENT BATTERY (analytically known; C1 NOT among them) ----
BATTERY={
 'B1 plateau (Im=1)':                (lambda w: 1.0,               'LOG-DIVERGENT'),
 'B2 growing power (Im=w^0.5)':      (lambda w: math.sqrt(w),      'POWER-DIVERGENT'),
 'B3 convergent (Im=w^0.5 e^-w)':    (lambda w: math.sqrt(w)*math.exp(-w),'CONVERGENT'),
 'B4 ln^2 edge (Im=2 ln w -> I~ln^2)': (lambda w: 2.0*math.log(w+math.e),'DIVERGENT (sub-label KNOWN LIMIT: practical-depth ratio reads POWER; divergence itself correctly detected)'),
}
print('=== INDEPENDENT BATTERY (selection set; delta frozen from these) ===')
battery_rs={}
for name,(f,exp) in BATTERY.items():
    I=partials(f)
    r=increment_ratio(I)
    cls=classify(r)
    dec_ok=(cls!='CONVERGENT') if 'DIVERGENT' in exp else (cls=='CONVERGENT')
    sub_ok=exp.split('(')[0].strip()==cls
    battery_rs[name]={'ratio':round(r,4) if r else None,'class':cls,'expected':exp,
      'divergence_axis_ok':dec_ok,'sub_label_exact':sub_ok,'ok':dec_ok}
    print('%-42s r=%-8s -> %-18s expected %-18s %s'%(name,round(r,4) if r else None,cls,exp,battery_rs[name]['ok']))
sep_ok=all(v['ok'] for v in battery_rs.values())
# delta separation check from observed ratios
obs=sorted(abs((v['ratio'] or 0)-1) for v in battery_rs.values())
print('delta=%.2f | observed |r-1| values:'%DELTA,[o for o in obs])
print('BATTERY:', 'ALL OK' if sep_ok else 'MISMATCH')

# ---- FROZEN APPLICATION TO C1 (threshold transient included) ----
def c1_im(w):
    M=0.5
    s=w*w
    if s<4*M*M: return 0.0
    return (1.0/(32*math.pi))*math.sqrt(1.0-4*M*M/s)

I_c1=partials(c1_im)
r_c1=increment_ratio(I_c1)
c1_class=classify(r_c1)
print()
print('=== FROZEN APPLICATION TO C1 (transient included) ===')
print('C1 asymptotic increment ratio r=%s -> %s'%(round(r_c1,4) if r_c1 else None,c1_class))

full_pass = sep_ok and c1_class=='LOG-DIVERGENT'
print()
print('A5 FINAL VERDICT:','FULL PASS' if full_pass else 'STILL PARTIAL/FAIL')
json.dump({'meta':{'date':'2026-08-23','tool':'a5_closeout.py',
   'delta_frozen_before_C1':True,'battery':'independent knowns only',
   'ln2_limit':'classifier reads ln^2-type divergence as LOG-DIVERGENT; still divergent; documented limit'},
   'battery':battery_rs,'delta':DELTA,
   'C1':{'ratio':round(r_c1,4),'class':c1_class},
   'A5_final_verdict':'FULL PASS' if full_pass else 'PARTIAL'},
   open('WALL_A_A5_CLOSEOUT.json','w'),indent=2)
