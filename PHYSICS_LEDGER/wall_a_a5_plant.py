#!/usr/bin/env python3
# WALL A / A5 - SYNTHETIC SELF-ENERGY PLANT (runs FIRST per W-1: validate the consumer
# before the expensive vertex exists).
# Pipeline under test: given sampled Im Sigma_R^TT(w):
#   (i)  passivity gate (Im >= 0 forall w>0)
#   (ii) multi-point log-log low-w fit (no exponent forced on non-power-law)
#   (iii) Re Sigma via the CALIBRATED singularity-subtracted PV integrator
#   (iv) convergence integral Re Sigma(0), cutoff-dependence check
# Controls:
#   C1 flat-space one-loop scalar bubble: Im S = lam^2/32pi * sqrt(1-4m^2/s) theta(s-4m^2),
#      s=w^2, threshold at w=2m (analytic, known)
#   C2 Lorentz oscillator (passivity-validated earlier this session), closed form
#   C3 corrupted sign flip -> MUST FAIL the passivity gate
import json, math

WMAX=200.0; NINT=120000
CONV_TOL=0.10

def passivity_gate(im_vals):
    pos=[v for v in im_vals]
    return {'min_Im':min(pos),'passed':min(pos)>=-1e-12}

def fit_loww_loglog(spec,probe_band=(0.02,1.0)):
    xs=sorted(w for w in spec if probe_band[0]<=w<=probe_band[1] and spec[w]>0)
    pts=[(math.log(x),math.log(spec[x])) for x in xs]
    if len(pts)<4: return None,len(pts)
    k=len(pts); sx=sum(p[0] for p in pts); sy=sum(p[1] for p in pts)
    sxx=sum(p[0]**2 for p in pts); sxy=sum(p[0]*p[1] for p in pts)
    return (k*sxy-sx*sy)/(k*sxx-sx*sx),k

def re_sigma_pv(w0,imspec,W=WMAX,N=NINT):
    # calibrated subtraction identity: P int dw'/(w'^2-w^2)=0
    h=W/N; g=lambda w: w*imspec(w); g0=g(w0); s=0.0
    for i in range(N):
        a=W*i/N; b=a+h
        fa=(g(a)-g0)/(a*a-w0*w0) if abs(a-w0)>1e-9 else 0.0
        fb=(g(b)-g0)/(b*b-w0*w0) if abs(b-w0)>1e-9 else 0.0
        s+=0.5*(fa+fb)*h
    return (2.0/math.pi)*s   # NOTE: for Im-chi KK the exact prefactor/log term is
                             # convention-dependent; here used as CONSISTENT comparator
                             # across plants (same operator applied to all).

def convergence_class(spec,wlo=0.05):
    def part(hi):
        ws=sorted(w for w in spec if wlo<=w<=hi); s=0.0; prev=None
        for i,w in enumerate(ws):
            term=spec[w]/w
            if prev is not None: s+=0.5*(prev+term)*(ws[i]-ws[i-1])
            prev=term
        return s
    p1,p2,p4=part(2.0),part(6.0),part(WMAX)
    growing=abs(p4-p2)>abs(p2)*0.25 or abs(p2-p1)>abs(p2)*0.25
    ratio=abs(p4)/max(abs(p2),1e-12)
    cls='CONVERGENT'
    if growing:
        cls='POWER-DIVERGENT' if ratio>3.0 else 'LOG-DIVERGENT'
    return {'partial_2':round(p1,4),'partial_6':round(p2,3),'partial_full':round(p4,3),
            'growth_ratio':round(ratio,2),
            'class':'CONVERGENT' if not growing else cls}

# ---- controls ----
M=0.5; LAM=1.0
def im_scalar_bubble(w):
    s=w*w
    if s<4*M*M: return 0.0
    return (LAM**2/(32*math.pi))*math.sqrt(1.0-4*M*M/s)

def im_lorentz(w,g=0.4,w0=2.0):
    d=w0*w0-w*w
    return g*w0*w0*w/(d*d+g*g*w*w)

def make_spec(imfn,wmax=WMAX,n=4000):
    return {round(wmax*(i+0.5)/n,5):imfn(wmax*(i+0.5)/n) for i in range(n)}

def run_control(name,imfn,expect_loww,expect_conv):
    spec=make_spec(imfn)
    pg=passivity_gate(list(spec.values()))
    slope,npts=fit_loww_loglog(spec)
    conv=convergence_class(spec)
    res={'control':name,'passivity':pg,'loww_fit_slope':(round(slope,4) if slope is not None else None),
         'fit_points':npts,'expected_loww':expect_loww,'convergence':conv,
         'expected_convergence':expect_conv}
    res['recovered']=((slope is not None and abs(slope-expect_loww)<0.15) if expect_loww!='ZERO-BELOW-THRESHOLD'
                      else all(v==0 for k,v in spec.items() if float(k)<1.8*M))
    res['conv_recovered']=(conv['class']==expect_conv)
    return res

def main():
    results=[]
    results.append(run_control('C1 scalar one-loop bubble',im_scalar_bubble,'ZERO-BELOW-THRESHOLD','LOG-DIVERGENT'))
    results.append(run_control('C2 Lorentz oscillator',im_lorentz,1.0,'DIVERGENT'))
    # C3 corrupted plant: negative Im -> gate must reject
    bad=make_spec(lambda w:-im_lorentz(w))
    pg=passivity_gate(list(bad.values()))
    c3={'control':'C3 corrupted sign (must FAIL)','passivity':pg,
        'rejected_by_gate':not pg['passed']}
    results.append(c3)
    # C4 white-floor control: constant Im -> slope 0 divergent
    results.append(run_control('C4 white floor',lambda w:1.0,0.0,'DIVERGENT'))
    core_ok=all(r.get('plant_recovered',r.get('recovered')) and
                r.get('conv_recovered',True) for r in results if 'C3' not in r['control'])
    gate_ok=c3['rejected_by_gate']
    verdict='PASS' if (core_ok and gate_ok) else 'FAIL - consumer pipeline not validated'
    json.dump({'meta':{'date':'2026-08-23','tool':'wall_a_a5_plant.py',
       'W0_fence':'COMPUTED-AND-REPORTED, NOT BANKED (charter:73 frontier fence)',
       'controls':results,'gate_ok':gate_ok,'verdict':verdict},
       },open('WALL_A_A5_RESULT.json','w'),indent=2,default=str)
    for r in results:
        cv=r.get('convergence',{})
        print('%-40s pass=%-5s slope=%-8s npts=%-3s conv=%s'%(
            r['control'],r.get('passivity',{}).get('passed'),r.get('loww_fit_slope'),
            r.get('fit_points'),cv.get('class','n/a')))
    print()
    print('A5 VERDICT:',verdict)

main()