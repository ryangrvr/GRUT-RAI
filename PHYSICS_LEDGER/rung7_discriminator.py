#!/usr/bin/env python3
# RUNG7_W3 DISCRIMINATOR - single-pole vs passive-channel one-signedness.
import json, math

def H(a, Om=0.3, OL=0.7): return (Om/a**3+OL)**0.5
def chi_single(x): return complex(1.0,x)/(1.0+x*x)
def chi_two_real(x,A1,A2,t1,t2):
    return A1/complex(1.0,-x*t1)+A2/complex(1.0,-x*t2)
def chi_osc(x,g=0.4,Om=0.6):
    # damped oscillator: chi=1/(Om^2-x^2-i g x); Im>0 forall x>0 (passive);
    # Re changes sign at x=Om -> in-band elastic crossing
    return 1.0/complex(Om*Om-x*x,-g*x)
def chi_cole(x,alpha=0.6):
    ph=-1.5707963267948966*alpha
    d=1.0+(x**alpha)*complex(math.cos(ph),math.sin(ph))
    return 1.0/d
def chi_three_real(x):
    return chi_two_real(x,0.5,0.3,0.5,1.0)+0.2/complex(1.0,-x*2.0)

def check_passivity(chi,n=200):
    worst=min(chi(0.01*i).imag for i in range(1,n+1))
    return {'min_Im_chi_w_pos':worst,'passive':worst>=-1e-12}

def check_kk(chi,xmax=20.0,n=4000):
    xs=[xmax*i/n for i in range(n+1)]
    re=[chi(x).real for x in xs]
    dx=xs[1]-xs[0]; num=[]; tru=[]
    for k in range(0,n+1,50):
        xk=xs[k]; s=0.0
        for j in range(n+1):
            if abs(xs[j]-xk)<1e-9: continue
            s+=re[j]*xs[j]/(xs[j]*xs[j]-xk*xk)
        num.append(s*dx*2/math.pi); tru.append(chi(xk).imag)
    sc=max(1e-9,max(abs(t) for t in tru))
    return {'kk_max_rel_residual':round(max(abs(a-b) for a,b in zip(num,tru))/sc,4)}

def classify(vals,ref):
    sc=any(v>0 for v in vals) and any(v<0 for v in vals)
    scr=any(v>0 for v in ref) and any(v<0 for v in ref)
    if sc and scr: return 'TRUE CROSSING'
    if sc: return 'NUMERICAL ARTIFACT'
    if min(abs(v) for v in vals)<1e-6: return 'TANGENCY'
    if not sc: return 'APPROACH WITHOUT CROSSING'
    return 'UNRESOLVED'

def run_kernel(name,chi,params=''):
    out={'kernel':name,'params':params,'crossing_by_framing':{}}
    for frame,key in (('phase-lag/elastic','real'),('dissipative','imag')):
        vals=[]; ref=[]
        for N,acc in ((400,vals),(1600,ref)):
            for i in range(N):
                a=0.02+0.98*i/(N-1)
                acc.append(getattr(chi(a*H(a)),key))
        out['crossing_by_framing'][frame]=classify(vals,ref)
    out['passivity']=check_passivity(chi)
    out['KK']=check_kk(chi)
    return out

def main():
    K=[('single-pole Debye (control)',lambda x:chi_single(x),'tau=1'),
       ('two REAL poles',lambda x:chi_two_real(x,0.6,0.4,0.5,3.0),'A=(0.6,0.4) tau=(0.5,3)'),
       ('complex-conjugate OSCILLATORY pair',lambda x:chi_osc(x,0.5,2.0),'gamma=0.5 Omega=2 (flip w*=2 in band [1,3.9])'),
       ('one-channel NON-Debye Cole-Cole',lambda x:chi_cole(x,0.6),'alpha=0.6'),
       ('three REAL poles (control)',chi_three_real,'A=(0.5,0.3,0.2) tau=(0.5,1,2)'),
       ('PLANT corrupted sign',lambda x:complex(chi_single(x).real,-abs(chi_single(x).imag)),'flip Im')]
    res=[run_kernel(n,f,p) for n,f,p in K]
    json.dump({'meta':{'date':'2026-08-23','tool':'rung7_discriminator.py',
        'criterion':'TRUE CROSSING iff sign change persists at 4x refinement'},
        'results':res},open('RUNG7_TWO_POLE_COMPARISON.json','w'),indent=2)
    for r in res:
        print(r['kernel'],'|',r['crossing_by_framing'],'| passive:',r['passivity']['passive'])

main()