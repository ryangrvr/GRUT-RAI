"""ADJUDICATION 03 instrument: is the acoustic two-phonon graviton channel
kinematically empty (the builder's V1b claim) or open (the sealed ledger)?

Three independent tests, no code shared with the builder's file:
  T1  EXACT ROOT EXISTENCE (no tolerance at all): solve
      2 sin((k_par+b)/2) + 2 sin(b/2) = omega,  a = k_par + b,
      for oblique gravitons (|k_par| = mu*omega, |mu| < 1). Interior root
      with machine-precision residual = channel OPEN, full stop.
  T2  WINDOWED-SUM SCALING on the discrete chain (N=256): total shell count
      and weight vs domega. OPEN channel signature: count ~ domega, so
      W ~ domega and W/domega -> const != 0 (the golden-rule density).
      The builder's V1b measures W (no 1/domega) and reads W -> 0 as
      emptiness; this test shows the normalized density converges.
  T3  NEGATIVE CONTROL (what emptiness actually looks like): ALIGNED
      gravitons (k_par = omega exactly). The deficit is finite
      (~omega^3/96 + zero-mode exclusion), so once domega < deficit the
      count crashes to ZERO -- ratios collapse, not hold at 0.5.
"""
import numpy as np
from scipy.optimize import brentq

w = lambda q: 2.0 * np.abs(np.sin(q / 2.0))

print("=" * 72)
print("T1: EXACT ROOTS, oblique modes (opposite-sign channel, a>0>-b)")
print("=" * 72)
open_count, total = 0, 0
for om in (0.3, 0.6, 1.0, 1.5):
    for mu in (0.0, 0.3, 0.6, 0.9):
        kpar = mu * om
        f = lambda b: w(kpar + b) + w(b) - om
        # bracket: b -> 0+ gives w(kpar) - om (negative for kpar < om);
        # b at pi - kpar gives 2 + 2 cos(kpar/2) - om > 0 here
        lo, hi = 1e-12, np.pi - kpar - 1e-12
        total += 1
        if f(lo) < 0 < f(hi):
            b = brentq(f, lo, hi, xtol=1e-15)
            a = kpar + b
            res = abs(w(a) + w(b) - om)
            interior = (a > 1e-10) and (b > 1e-10)
            open_count += interior
            print(f"  om={om:4.2f} mu={mu:3.1f}: a={a:.6f} b={b:.6f} "
                  f"residual={res:.2e} interior={interior}")
        else:
            print(f"  om={om:4.2f} mu={mu:3.1f}: NO bracket (closed)")
print(f"T1 VERDICT: {open_count}/{total} oblique configs have exact interior"
      " on-shell roots -> channel OPEN" if open_count == total else
      f"T1: only {open_count}/{total} open")

print()
print("=" * 72)
print("T2: WINDOWED SUM vs domega, discrete chain N=256, oblique modes")
print("=" * 72)
N = 256
m = np.arange(-(N // 2), N - N // 2)
qs = 2 * np.pi * m / N
om_q = w(qs)
rng = np.random.default_rng(7)
# 400 oblique gravitons: omega in [0.3, 1.5], mu in [-0.9, 0.9]
oms = rng.uniform(0.3, 1.5, 400)
mus = rng.uniform(-0.9, 0.9, 400)
kpars = mus * oms
DOMs = [0.03, 0.015, 0.0075, 0.00375, 0.001875]
totW, totC = [], []
for dom in DOMs:
    Wt, Ct = 0.0, 0
    for om, kp in zip(oms, kpars):
        qp = (kp - qs + np.pi) % (2 * np.pi) - np.pi
        wqp = w(qp)
        ok = (om_q > 1e-12) & (wqp > 1e-12) & \
             (np.abs(om_q + wqp - om) < dom)
        if ok.any():
            B = 0.5 * (np.sqrt(om_q[ok] * wqp[ok])
                       + qs[ok] * qp[ok] / np.sqrt(om_q[ok] * wqp[ok]))
            Wt += (B ** 2).sum() / N
            Ct += int(ok.sum())
    totW.append(Wt)
    totC.append(Ct)
print("  domega     count   W_total       W/domega  (golden-rule density)")
for dom, c, Wt in zip(DOMs, totC, totW):
    print(f"  {dom:8.6f} {c:6d}  {Wt:.6e}  {Wt/dom:.6e}")
r = [totW[i + 1] / totW[i] for i in range(len(totW) - 1)]
rho = [totW[i] / DOMs[i] for i in range(len(totW))]
print(f"  halving ratios of W: {[f'{x:.2f}' for x in r]}  "
      f"(0.5 = open-channel signature under a missing 1/domega)")
print(f"  W/domega drift over 16x tolerance range: "
      f"{max(rho)/min(rho):.3f}x  (convergent => finite density => OPEN)")

print()
print("=" * 72)
print("T3: NEGATIVE CONTROL -- aligned gravitons (k_par = omega): TRUE emptiness")
print("=" * 72)
oms_al = rng.uniform(0.3, 1.5, 400)
print("  domega     count   (empty channel: count crashes to 0, ratios NOT 0.5)")
for dom in DOMs:
    Ct = 0
    for om in oms_al:
        kp = om
        qp = (kp - qs + np.pi) % (2 * np.pi) - np.pi
        wqp = w(qp)
        ok = (om_q > 1e-12) & (wqp > 1e-12) & \
             (np.abs(om_q + wqp - om) < dom)
        Ct += int(ok.sum())
    print(f"  {dom:8.6f} {Ct:6d}")
