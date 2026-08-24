#!/usr/bin/env python3
# KK/DOS probe v2 - calibrated PV scheme (subtraction; calibrated on Debye exact pair).
import json, math

def re_chi_pv(w0, imchi, wmax=600.0, n=300000):
    h=wmax/n; s=0.0
    i0=imchi(w0)
    for i in range(n):
        a=wmax*i/n; b=a+h
        ia=imchi(a); ib=imchi(b)
        fa=(a*ia-w0*i0)/(a*a-w0*w0) if abs(a-w0)>1e-9 else 0.0
        fb=(b*ib-w0*i0)/(b*b-w0*w0) if abs(b-w0)>1e-9 else 0.0
        s+=0.5*(fa+fb)*h
    pv_log=0.5*math.log(abs((wmax*wmax-w0*w0))/(w0*w0))
    return (2.0/math.pi)*(s+i0*pv_log)

print('CALIBRATION (Debye Im=w/(1+w^2); exact Re=1/(1+w^2)):')
ok=True
for w0 in (0.5,1.0,2.0,3.0):
    num=re_chi_pv(w0,lambda w:w/(1+w*w))
    ex=1.0/(1.0+w0*w0)
    rel=abs(num-ex)/ex; ok = ok and rel<0.02
    print('  w0=%.1f numeric=%.4f exact=%.4f rel=%.2f%%'%(w0,num,ex,100*rel))
if not ok:
    print('STOP: calibration failed; no physics reading'); raise SystemExit(1)

probe=[0.8,1.5,2.5,4.0]
shapes={
 'smooth super-Ohmic w^3/(1+w)^6': lambda w: w**3/(1.0+w)**6,
 'super-Ohmic + narrow bump at w=2': lambda w: w**3/(1.0+w)**6 + 0.002*math.exp(-((w-2.0)/0.08)**2),
}
out={}
for name,f in shapes.items():
    vals=[(w0,round(re_chi_pv(w0,f),6)) for w0 in probe]
    flip=any(vals[i][1]*vals[i+1][1]<0 for i in range(len(vals)-1))
    out[name]={'Re_chi':dict(vals),'sign_change_in_band':flip,
               'any_negative':any(v<0 for _,v in vals)}
    print(name,'->',out[name])
json.dump(out,open('KK_DOS_SIGNCHANGE_PROBE.json','w'),indent=1)
print('saved')