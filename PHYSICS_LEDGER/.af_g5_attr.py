#!/usr/bin/env python3
"""All-samples verification of the planned G5 H^1-attribution gate: for every
operator and every K-sample, the H^1 correction must be generated exclusively by
structures whose O(H) dressings carry a linear-in-u term (B'(0) ~ O(H)), with the
complement contributing exactly zero.  Also prints the H^1 inventory."""
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
K_SAMPLES = ns['K_SAMPLES']
master = ns['master']
old_kernel_of = ns['old_kernel_of']
cascade_split = ns['cascade_split']
table_of = ns['table_of']


def h1_generators(tab):
    out = {}
    for (p, q), B in tab.items():
        d1 = sp.expand(B.coeff(H, 1))
        if sp.expand(sp.diff(d1, uu).subs(uu, 0)) != 0:
            out[(p, q)] = B
    return out


t0 = time.time()
allok = True
for _i, (_ov, _kv) in enumerate(K_SAMPLES):
    dens, r0 = cascade_split(_kv, gates=False)
    print('[%.1fs] cascade K=(%s,%s) done' % (time.time() - t0, _ov, _kv))
    sys.stdout.flush()
    for op in OPS:
        tab = table_of(dens[op])
        gen = h1_generators(tab)
        nongen = dict((k, v) for k, v in tab.items() if k not in gen)
        kfull = sp.expand(master(tab, 'P').subs(om, _ov))
        kold = sp.expand(old_kernel_of(tab).subs(om, _ov))
        corr_full = sp.expand(kfull.coeff(H, 1) - kold.coeff(H, 1))
        kg = sp.expand(master(gen, 'P').subs(om, _ov))
        kog = sp.expand(old_kernel_of(gen).subs(om, _ov))
        corr_gen = sp.expand(kg.coeff(H, 1) - kog.coeff(H, 1))
        kn = sp.expand(master(nongen, 'P').subs(om, _ov))
        kon = sp.expand(old_kernel_of(nongen).subs(om, _ov))
        corr_nongen = sp.expand(kn.coeff(H, 1) - kon.coeff(H, 1))
        ok = (sp.expand(corr_gen - corr_full) == 0) and corr_nongen == 0
        allok &= ok
        print('  K=(%s,%s) %s: H1corr==0: %s | gen=%s | gen==full: %s | nongen==0: %s'
              % (_ov, _kv, op, corr_full == 0, sorted(gen.keys()),
                 sp.expand(corr_gen - corr_full) == 0, corr_nongen == 0))
        sys.stdout.flush()
print('\nALL-SAMPLES ATTRIBUTION:', 'OK' if allok else 'FAILS')
print('[%.1fs] done' % (time.time() - t0))
