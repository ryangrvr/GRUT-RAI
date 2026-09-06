# RRT0_RECONSTRUCTION_SPEC.md — frozen before results
Three maps, none selected post hoc:

d1(alpha,beta) = 1 - |M_ab|/max|M|, M_ab = time-averaged absolute covariance
  |<O_a O_b> - <O_a><O_b>| on the Gell-Mann basis restricted to sector supports.
  Correlation-based. Not influence-based.

d2(alpha,beta) = 1/(1 + Phi_{a->b} + Phi_{b->a}).
  Influence-based. Not correlation-based.

d3(alpha,beta) = ||row_a(Phi) - row_b(Phi)||_2 (full outgoing influence profile).
  Structural. Distinct from both.

H5 gate (only if reached): pairwise Spearman(d_i, d_j) > 0.7 on HELD-OUT sector
pairs (30% of pairs excluded from any tuning), stable across >=4/5 seeds, and
d2 must not be a monotone rescaling of d1 (verified: Spearman of raw quantities
< 0.95 while embedded distances agree, else maps declared equivalent and
"non-equivalent maps" requirement FAILS -> no geometry proxy claim).

If maps agree only because one is a rescaling of the other: record as
REPRESENTATION/DIAGNOSTIC DEPENDENCE (Outcome E). No promotion.
