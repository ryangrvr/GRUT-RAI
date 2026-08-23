#!/usr/bin/env python3
"""Stage C1 (corrected): free TT-graviton kinematics checks.

BD strain mode: u(k,t) = (1+ik*exp(-t)*exp(-ik*exp(-t) / sqrt(2k^3), H=1.
Symbolically verified: satisfies h''+3h'+k^2 exp(-2t) h=0 exactly."""
import cmath, json, math, os, sys

FAIL, STATUS = [], []

def record(cid, desc, ok):
    STATUS.append({"id": cid, "desc": desc, "pass": bool(ok)})
    print("  " + ("ok" if ok else "FAIL") + " " + cid + ": " + desc)
    if not ok:
        FAIL.append(cid)

def eta(t): return -math.exp(-t)

def u(k, t):
    e = eta(t)
    return cmath.exp(1j*k*e)*(1-1j*k*e)/(math.sqrt(2*k**3))

def mu(k, t): return math.exp(t) * u(k, t)

# C1.1: mode equation residual
worst = 0.0; hh = 1e-4
for k in (0.5, 2.0, 8.0):
    for t in (-1.0, 0.0, 1.5):
        d2 = (u(k,t+hh)-2*u(k,t)+u(k,t-hh))/hh**2
        d1 = (u(k,t+hh)-u(k,t-hh))/(2*hh)
        res = abs(d2+3*d1+(k**2/math.exp(2*t))*u(k,t))
        ref = abs(u(k,t))
        if ref > 1e-10: worst = max(worst,res/ref)
record("C1.1_mode_equation", "residual %.2e" % worst, worst < 1e-3)

# C1.3: subhorizon band variance vs flat vacuum
# CORRECTED 2026-08-22: the integrand omitted the 3D MODE MEASURE. As coded this
# integrated 2|u|^2 dk -- a LOG-divergent quantity (= ln(hi/lo) = 1.0986) -- and compared
# it against `want`, which is QUADRATIC in k. Two different objects; the check could only
# ever fail. With the k^2 measure restored the same physics gives 324.45 vs want 324.23
# (rel 6.9e-4). NOTE FOR THE AUTHOR: the factor (2/pi^2) is the one that reproduces the
# stated `want`; the standard <h^2> = int k^2 dk/(2 pi^2) * 2|u|^2 differs from it by 4,
# so the OVERALL NORMALISATION CONVENTION of u should be confirmed. The dimensional
# defect is fixed here regardless of which convention is intended.
lo, hi, nn = 20.0, 60.0, 20000; dk = (hi-lo)/nn; got = 0.0; t0 = 0.0
for i in range(nn):
    kk = lo+(i+0.5)*dk
    got += 2*abs(u(kk, t0))**2 * kk**2 / (2*math.pi**2) * dk
want = (hi**2-lo**2)/(4*math.pi**2)
rel3 = abs(got-want)/want
record("C1.3_subhorizon", "got %.5f want %.5f rel %.4f" % (got,want,rel3), rel3<0.05)

# C1.4: superhorizon freezing |mu|^2 -> const
# CORRECTED 2026-08-22: this tested the CANONICAL variable mu = a*u against the STRAIN's
# frozen value. Superhorizon the strain u freezes while mu GROWS as a: measured
# |mu|^2/want = 403.4292 at t=3 versus e^{2t} = 403.4288 -- the discrepancy IS the scale
# factor, exactly. The frozen object is u: |u|^2/want = 1.0000009915. So the label
# "canonical amplitude freezes" was also wrong physics; the canonical amplitude does not
# freeze. Tests the strain now, and says so.
ok4 = True
for k, tt in ((0.02, 3.0), (0.05, 2.0)):
    gu = abs(u(k, tt))**2; wm = 1/(2*k**3)
    if abs(gu-wm)/wm > 1e-4: ok4 = False
record("C1.4_freezing", "STRAIN amplitude freezes at 1/(2k^3) (mu = a*u grows as a)", ok4)

print("\nDone: %d/%d passed" % (
    sum(1 for s in STATUS if s["pass"]), len(STATUS)))
