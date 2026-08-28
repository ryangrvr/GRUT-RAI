#!/usr/bin/env python3
"""Tensor-side diagnostic for the G5/G6 rewrite: one split cascade at K=(3,2),
then per-operator H^1 correction inventory, odd/even attribution, and a preview
of every G6 control at H^0/H^1/H^2.  No machinery exec."""
import os
import sys
import time

src = open('wall_d2_phase11_af_basis.py').read()
pre = src.split('print("\\n=== STEP M:')[0]
stepC = 'print("\\n=== STEP C:' + src.split('print("\\n=== STEP C:')[1].split('print("\\n=== STEP K:')[0]
ns = {'__name__': '__main__', '__file__': os.path.abspath('wall_d2_phase11_af_basis.py')}
exec(compile(pre + stepC, 'diag_prefix', 'exec'), ns)

sp = ns['sp']
om = ns['om']
H = ns['H']
uu = ns['uu']
OPS = ns['OPS']
master = ns['master']
old_kernel_of = ns['old_kernel_of']
master_broken = ns['master_broken']
cascade_split = ns['cascade_split']
table_of = ns['table_of']

t0 = time.time()
dens, r0 = cascade_split(sp.Rational(2), gates=False)
print('[%.1fs] cascade done' % (time.time() - t0))
sys.stdout.flush()
for op in OPS:
    tab = table_of(dens[op])
    print('\n== %s == structures: %s' % (op, sorted(tab.keys())))
    sys.stdout.flush()
    kP = master(tab, 'P')
    kold = old_kernel_of(tab)
    corr1 = sp.expand(kP - kold).coeff(H, 1)
    corr2 = sp.expand(kP - kold).coeff(H, 2)
    print('  H1 corr symbolic==0:', corr1 == 0,
          '| at om=3==0:', sp.expand(corr1.subs(om, 3)) == 0)
    print('  H2 corr at om=3==0:', sp.expand(corr2.subs(om, 3)) == 0)
    tabo = dict((k, v) for k, v in tab.items() if (k[0] + k[1]) % 2 == 1)
    tabe = dict((k, v) for k, v in tab.items() if (k[0] + k[1]) % 2 == 0)
    c1o = sp.expand(master(tabo, 'P') - old_kernel_of(tabo)).coeff(H, 1)
    c1e = sp.expand(master(tabe, 'P') - old_kernel_of(tabe)).coeff(H, 1)
    print('  odd-only H1 corr == full:', sp.expand(c1o - corr1) == 0)
    print('  even-only H1 corr == 0  :', c1e == 0)
    for (p, q), B in sorted(tab.items()):
        if (p + q) % 2 == 1:
            d1 = sp.expand(B.coeff(H, 1))
            if sp.diff(d1, uu) != 0:
                print('  odd structure with u-dependent O(H) coeff:', (p, q))
    for w in ('A', 'B', 'C', 'Cp', 'D'):
        kb = master_broken(tab, w)
        s0 = sp.expand(kb.coeff(H, 0) - kP.coeff(H, 0)) == 0
        d1 = sp.expand(kb.coeff(H, 1) - kP.coeff(H, 1)) != 0
        d2 = sp.expand(kb.coeff(H, 2) - kP.coeff(H, 2)) != 0
        print('  ctl %2s: sameH0=%s diffH1=%s diffH2=%s' % (w, s0, d1, d2))
    kbc = master(tab, 'P', conj=True)
    print('  conj: sameH0=%s diffH1=%s diffH2=%s' % (
        sp.expand(kbc.coeff(H, 0) - kP.coeff(H, 0)) == 0,
        sp.expand(kbc.coeff(H, 1) - kP.coeff(H, 1)) != 0,
        sp.expand(kbc.coeff(H, 2) - kP.coeff(H, 2)) != 0))
    sys.stdout.flush()
print('\n[%.1fs] diag done' % (time.time() - t0))
