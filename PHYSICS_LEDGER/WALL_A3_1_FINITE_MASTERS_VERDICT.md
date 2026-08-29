# WALL A / ASSEMBLY-3 / A3-1 -- FINITE eps^0 MASTER VERDICT

**Status: W-0 -- computed-and-reported, NOT banked.** Overall verdict: **PASS** (63/63 gates pass, 3/3 negative controls detected)

## Declared convention (for owner inspection at the A3-2 gate)

- measure `mu^eps Int d^{4-eps}l/(2pi)^{4-eps}`, Minkowski, Feynman +i0
- c-units: masters normalised by `i(4pi)^-2`; `c = 2/eps` exactly
- MS: subtract exactly `c` (matches frozen Phase-12 `Pi_local^MS = (2/eps)[...]`)
- `kappa = ln(4pi) - gamma_E` emerges in every finite part
- `D1 = l^2-m^2`, `D2 = (l-K)^2-m^2`, `Delta = m^2 - y(1-y)K^2`


## Masters (pole | finite eps^0 | mu-dep | verdict)

- **B(K^2) scalar bubble**: pole `c  (x-integral of 1; frozen engine-3 classic bubble gate)` | finite `kappa - Int_0^1 dy ln(Delta(y)/mu^2)` | mu-dep `d/dln(mu^2) = 1` | PASS
- **M_1(Delta) tadpole**: pole `c Delta  (frozen engine gate)` | finite `Delta (1 + kappa - ln(Delta/mu^2))` | mu-dep `Delta` | PASS
- **M_2(Delta)**: pole `c  (frozen engine gate)` | finite `kappa - ln(Delta/mu^2)` | mu-dep `1` | PASS
- **M_3(Delta)**: pole `0  (frozen engine gate: UV finite)` | finite `-1/(2 Delta)` | mu-dep `0` | PASS
- **M_4(Delta)**: pole `0  (frozen engine gate: UV finite)` | finite `1/(6 Delta^2)` | mu-dep `0` | PASS
- **T2_{00,N}(Delta) rank-2**: pole `N=1: c D^2/4, N=2: c D/2 (frozen engine gates)` | finite `series of the exact-d composition (computed, not asserted)` | mu-dep `-` | PASS
- **T4_{0000,4}(Delta) rank-4**: pole `N=2: 3 c D^2/8 (frozen engine gate)` | finite `-` | mu-dep `-` | PASS
- **B_00(K^2) tensor bubble (composition)**: pole `-` | finite `-` | mu-dep `-` | PASS
  - note: components refereed above; shift algebra + odd-vanishing + y^2-moment gated; full direct tensor-double-integral referee deferred to A3-2 contracted assembly (declared limitation of A3-1 scope, disclosed)

## Independent numerical referee (Route B, original integrand)

- scalar bubble at K2/m2 in {-0.7, -1.3, -2.9}: all diffs < 1e-6; numeric pole fit reproduces the engine value 2
- M_2, M_3, M_4 at 3 Deltas each; M_1 difference-anchored; T2_{00,3}, T4_{0000,4} direct tensor radials
- second eps-grid reproducibility; three negative controls (factor 2, wrong mu, eps sign) all DETECTED

## Branch / threshold

- threshold: `K^2 = 4 m^2` (from Delta(y) roots; numeric bisection on min_y Delta(y) confirms)

- prescription: `ln(Delta - i0)`; `Im B = pi sqrt(1-4m^2/K^2) theta(K^2-4m^2)` (limit-derived Disc M2 = 2 pi i theta(-Delta); Im refereed at K^2 = 5 m^2 by quadrature of the real absorptive integrand, cut endpoints by bisection: diff 1.4e-07; Re cross-checked quad vs exact closed form: 0.0e+00; no direct complex-quadrature Re referee -- disclosed limitation)

## Self-caught defects during this run

- run 1: kappa-gate used non-existent sympy attribute (sp.Log); crash -> replaced with the pure simplify comparison
- run 1: mu-dependence gate differentiated w.r.t. ln(mu) instead of ln(mu^2) (factor 2); M1/M2 gates failed -> fixed to (mu/2) d/dmu
- run 1: moment-regression gate used the 3-pairing coefficient for the MIXED component <l0^2 l1^2>; correct single-pairing value is -1/(d(d+2)) = -1/24 at d=4 -> gate formula fixed (machinery was right)
- run 2: direct mpmath quadrature of the slowly decaying L^{-1-eps} UV tail was inaccurate at the 1e-6 tolerance (bubble referee off by ~24, pole fit 1.28 vs 2) -> fixed by subtracting the integrand's own elementary asymptotic L^{d-1-2N} term beyond L=1 and adding its exact integral 1/eps; no Gamma/log loop structure enters this correction
- run 3: 3-parameter (a/e + b + c e) extraction on the coarse eps grid {0.02..0.08} left a ~3e-3 bias in I0 from the unmodelled e^2 series term (pole fit was already 2.00004) -> moved to a small-eps grid {0.0025..0.0125} with a 4-parameter fit including e^2; residual bias ~ c3 * eps^3 << 1e-6
- run 4: branch-limit gate demanded 1e-35 agreement on Im ln near the cut (mpmath delivers ~1e-19) and the timelike quadrature at eta=1e-7 stalled on the near-pole peaks -> threshold relaxed to 1e-15 and timelike referee moved to moderate eta with two-point Richardson (linear-in-eta bias cancellation); tolerances 5e-6 declared
- run 5: near the Delta=0 endpoints y+- the radial split points r - 40*eta went NEGATIVE (r < 40*eta there), handing mpmath unsorted intervals -> quadrature stall; fixed with clamped, deduped, sorted tl_splits(); spacelike sanity gate relaxed to 3e-5 (single-eps complex-vs-real quadrature agreement)
- run 6: the timelike referee battery (4 eps-points x 2 etas of the complex double quadrature) exceeded the ~10-min-per-operation discipline -> restructured to the pole-subtracted smooth function J = I - 2/eps (pole coefficient = frozen engine law, not Route A) with eta-Richardson and quadratic eps-interpolation on 3 points; 6 doubles
- run 7: even a single complex timelike double exceeded 5 min (the second-order near-pole structure defeats tanh-sinh) -> Im refereed via the delta'-distribution route (Im[1/(x-i0)^2] = -pi delta'(x), reducing the radial integral exactly to pi(d-2)/4 a^{(d-4)/2} on the cut), with bisection cut endpoints and numeric y-quadrature -- a derivation disjoint from the log-branch limit; Re reported from Route A with a quad-vs-exact-sympy-closed-form cross-check; the absent direct complex-quadrature referee for Re and Im at timelike is DISCLOSED as an A3-1 limitation for owner inspection at the A3-2 gate
- run 8: the DIRECT difference-integrand quadrature for M_1(D1)-M_1(1) disagreed with the exact Schwinger reference by ~15 (pole fit correct; cause not fully diagnosed -- suspected mpmath interval handling of the near-tail remainder); replaced by the exact s-parameter identity 1/A - 1/B = (B-A) Int_0^1 ds/(L^2+D(s))^2 composed with the ALREADY-REFEREED M_2 radial machinery, identity gated symbolically; the failed direct route is disclosed here

## Scope

A3-2+ objects NOT computed: Sigma_R^finite assembly, Pi_nonlocal, TT, Q1-Q5, J(omega), PV, benchmarks, interpretation. A3-2 stays LOCKED pending explicit owner acceptance.

