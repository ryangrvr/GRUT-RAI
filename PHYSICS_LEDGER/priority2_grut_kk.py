#!/usr/bin/env python3
# PRIORITY 2A - registered GRUT KK probe, validity-gated. wc=1 units.
import json, math

# identity: P int dw'/(w'^2-w^2)=0 over [0,inf) => Re chi=(2/pi)int[g(w')-g(w)]/(w'^2-w^2)
def re_chi(w0, g, wmax, n):
    h=wmax/n; s=0.0; g0=g(w0)
    for i in range(n):
        a=wmax*i/n; b=a+h
        fa=(g(a)-g0)/(a*a-w0*w0) if abs(a-w0)>1e-9 else 0.0
        fb=(g(b)-g0)/(b*b-w0*w0) if abs(b-w0)>1e-9 else 0.0
        s+=0.5*(fa+fb)*h
    return (2.0/math.pi)*s

# CALIBRATION on Debye exact pair: Im=w/(1+w^2) -> g=w^2/(1+w^2), exact Re=1/(1+w^2)
def g_debye(w): return w*w/(1.0+w*w)
cal=[]
for w0 in (0.5,1.0,2.0,3.0):
    num=re_chi(w0,g_debye,600.0,300000); ex=1.0/(1.0+w0*w0)
    rel=abs(num-ex)/ex; cal.append((w0,round(100*rel,3))); ok=(rel<0.02)
print('CALIBRATION:',cal,'pass' if ok else 'FAIL')
if not ok: raise SystemExit('STOP: calibration failed')

def find_zero(g,wmax,n,lo=0.05,hi=6.0,steps=240):
    prev=None; zeros=[]
    for i in range(steps+1):
        x=lo+(hi-lo)*i/steps
        v=re_chi(x,g,wmax,n)
        if prev is not None and prev* v<0:
            # bisect
            a,b=lo+(hi-lo)*(i-1)/steps,x
            for _ in range(40):
                m=0.5*(a+b)
                if re_chi(m,g,wmax,n)*re_chi(a,g,wmax,n)<=0: b=m
                else: a=m
            zeros.append(round(0.5*(a+b),4))
        prev=v
    return zeros

J3=lambda x: x**3*math.exp(-x*x)                      # s=3 friction spectral shape
S_T1=lambda x: J3(x)/math.tanh(max(x,1e-9)/2.0)        # noise at T=1; guarded
SHAPES={
 's=3 registered J (Gaussian)': {'g':lambda x: J3(x), 'variants':{
    'exponential cutoff': lambda x: x**3*math.exp(-x),
    'hard cutoff': lambda x: x**3 if x<1.0 else 0.0,
    'soft power-law': lambda x: x**3/(1+x**2)**2}},
 'noise-based S at T=1': {'g':lambda x: S_T1(x), 'variants':{}}}

report={}
for name,spec in SHAPES.items():
    entry={'zero_x':None,'convergence':{},'cutoff_shape_variants':{}}
    z25=find_zero(spec['g'],60.0,120000)
    z50=find_zero(spec['g'],120.0,240000)
    entry['zero_x']=z25; entry['convergence']={'wmax60_n120k':z25,'wmax120_n240k':z50,
      'stable': z25==z50}
    for vname,vf in spec['variants'].items():
        zv=find_zero(vf,60.0,120000)
        entry['cutoff_shape_variants'][vname]={'zeros':zv,
          'matches_gaussian_position': any(abs(z-(z25[0] if z25 else -9))<0.15 for z in zv) if zv and z25 else None}
    # low-frequency check: sign of Re chi well below cutoff
    low=[(x,round(re_chi(x,spec['g'],60.0,120000),5)) for x in (0.01,0.05,0.1,0.3)]
    entry['low_frequency_Re_chi']=low
    report[name]=entry
    print(name,'| zeros:',entry['zero_x'],'| stable:',entry['convergence']['stable'])
    print('  low-w Re chi:',low)
    for vn,vv in entry['cutoff_shape_variants'].items():
        print('  variant',vn,'->',vv['zeros'])

json.dump({'meta':{'date':'2026-08-23','tool':'priority2_grut_kk.py',
  'convention':'Im chi = J/omega (friction, registered); noise variant S=J coth(w/2T) also run',
  'validity':'VALIDITY-UNDECLARED in register; implied domain w << wc (low-w claims)',
  'calibration':{'debye_rel_err_pct':[c[1] for c in cal],'threshold':2}},
  'probe':report},open('PRIORITY2_GRUT_KK_PROBE.json','w'),indent=2)
print('saved PRIORITY2_GRUT_KK_PROBE.json')
