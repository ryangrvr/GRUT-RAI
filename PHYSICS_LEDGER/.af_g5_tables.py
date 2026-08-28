#!/usr/bin/env python3
"""Table-dump diagnostic: run the cascade at K=(3,2) once, dump all four B-tables
(srepr) to .af_g5_tables.json, then analyse EH's H^1 correction structure:
per-structure attribution, hermiticity B_pq(E,P) vs B_qp(P,E), actual expressions."""
import json
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
kk = ns['kk']
OPS = ns['OPS']
e1m = ns['e1m']
e2m = ns['e2m']
master = ns['master']
old_kernel_of = ns['old_kernel_of']
cascade_split = ns['cascade_split']
table_of = ns['table_of']

t0 = time.time()
dens, r0 = cascade_split(sp.Rational(2), gates=False)
print('[%.1fs] cascade done' % (time.time() - t0))
sys.stdout.flush()

TAB = {}
for op in OPS:
    TAB[op] = table_of(dens[op])
json.dump({op: {('%d,%d' % pq): sp.srepr(B) for pq, B in tab.items()}
           for op, tab in TAB.items()},
          open('.af_g5_tables.json', 'w'))
print('tables dumped to .af_g5_tables.json')
sys.stdout.flush()


def hgrade(e, n):
    return sp.expand(sp.expand(e).coeff(H, n))


def udep(e):
    e = sp.expand(e)
    return sp.simplify(sp.diff(e, uu)) != 0


# hermiticity check: B_pq(E,P) vs B_qp(P,E) at each H grade
sw = {e1m[i, j]: e2m[i, j] for i in range(4) for j in range(4)}
sw.update({e2m[i, j]: e1m[i, j] for i in range(4) for j in range(4)})


def swap_ep(e):
    return sp.expand(e.subs(sw, simultaneous=True))


print('\n===== HERMITICITY B_pq(E,P) vs B_qp(P,E) =====')
for op in OPS:
    tab = TAB[op]
    for (p, q) in sorted(tab):
        if p < q and (q, p) in tab:
            for n in (0, 1, 2):
                a = hgrade(tab[(p, q)], n)
                b = swap_ep(hgrade(tab[(q, p)], n))
                if sp.expand(a - b) != 0:
                    print('%s (%d,%d) H^%d: NOT exchange-symmetric' % (op, p, q, n))
    print('%s: exchange check done' % op)
    sys.stdout.flush()

print('\n===== EH PER-STRUCTURE H^1 CORRECTIONS (master - old, per structure) =====')
tab = TAB['EH']
for (p, q) in sorted(tab):
    t1 = {(p, q): tab[(p, q)]}
    c1 = sp.expand(master(t1, 'P') - old_kernel_of(t1)).coeff(H, 1)
    if c1 != 0:
        print('  (%d,%d): %s' % (p, q, sp.expand(c1.subs(om, 3))))
print('full EH H1 corr (om=3):', sp.expand(master(tab, 'P').subs(om, 3).coeff(H, 1)
                                           - old_kernel_of(tab).subs(om, 3).coeff(H, 1)))
print('full EH H1 corr (symbolic):', sp.expand(master(tab, 'P') - old_kernel_of(tab)).coeff(H, 1))

print('\n===== EH ODD-STRUCTURE DRESSINGS (the mechanism) =====')
for (p, q) in sorted(tab):
    if (p + q) % 2 == 1:
        print('  (%d,%d) H^0: %s' % (p, q, hgrade(tab[(p, q)], 0)))
        print('  (%d,%d) H^1: %s   (u-dep: %s)' % (p, q, hgrade(tab[(p, q)], 1),
                                                   udep(hgrade(tab[(p, q)], 1))))

print('\n===== EH (2,0)/(0,2) DRESSINGS at O(H) (the even-pair question) =====')
for key in ((2, 0), (0, 2), (1, 1)):
    if key in tab:
        print('  %s H^1: %s   (u-dep: %s)' % (key, hgrade(tab[key], 1), udep(hgrade(tab[key], 1))))

print('\n[%.1fs] done' % (time.time() - t0))
