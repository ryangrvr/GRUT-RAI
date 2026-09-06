# RRT0_SPEC.md — PRE-REGISTERED, FROZEN BEFORE SIMULATION
Status: UNBANKED / PRE-REGISTERED / EXPLORATORY / NOT GRUT EVIDENCE / NOT A TOE CLAIM
Freeze commit: recorded in RRT0_FREEZE.json at first commit on branch rrt-0-hostile-test.

## Model
U_N = (S_N, R_N, star, D_N, I_N), d = 4 (dim C^d), N sectors.
S_N = density matrices on H = C^d. D_N: rho_{t+1} = U rho U^dagger (CLOSED UNITARY).
U = exp(-i H dt), H drawn ONCE per seed from GUE(d), plus declared perturbations.
No site/graph meaning attached to any index. "Model update parameter" t = integer
update steps. NOT physical time.

## H0 relation
s1 ~ s2 iff for all E in E_int: |omega_{t+tau}^{(E,s1)}(B) - omega_{t+tau}^{(E,s2)}(B)|
< epsilon_tau for all B in the full operator basis, over declared window. P_phys = S/~.
Nontriviality test: |S/~| > 1 and < |S|.

## Internal operations E_int (pre-registered family)
For each candidate sector alpha (discovered by algorithm below):
E_alpha(rho) = U^{tau_op} ( (1-lam) rho + lam sigma_alpha ) U^{-tau_op} with
lam = 0.05, sigma_alpha = normalized projector onto the sector support,
tau_op = 3 update steps. This is a closed-model-internal operation: no external
laboratory is invoked; sigma_alpha is built only from the model's own operators.

## Sector discovery (PRIMARY, frozen)
Algorithm S1: k-means (k=N) on rows of the influence matrix computed at
amplitude lam_probe = 0.05, tau = 5, on operator basis observables (Gell-Mann
generators, normalized). Clustering of RESPONSE rows, not of indices.

## Influence statistic (factorization-free)
Phi_{a->b}(t,tau) = sup_{B in basis_b, ||B||<=1} |omega_{t+tau}^{(E_a)}(B) - omega_{t+tau}^{(0)}(B)|
with basis_b = operator basis restricted to sector b support. Edge declared iff
Phi > epsilon = 0.01 in BOTH halves of a two-half repeatability split (time halves
t in [0,T/2), [T/2,T)).

## Observation window
T_obs = 200 update steps, sampled every 2 steps. States: maximally mixed + 5
random pure states per seed, all reported (no cherry-picking).

## Thresholds (frozen ladder)
epsilon in {0.005, 0.01, 0.02, 0.05} — ALL reported, primary = 0.01.
lam in {0.02, 0.05, 0.1} — primary = 0.05.

## Precision
float64. Convergence ladder: dt in {0.1, 0.05}, lam ladder above, N in {4,6,8}.

## Reconstruction maps (frozen before any result)
d1(alpha,beta) = 1 - |M_ab| / max|M| where M_ab = |Tr(O_a O_b rho_t) - Tr(O_a rho_t)Tr(O_b rho_t)| averaged.
d2(alpha,beta) = 1/(1 + Phi_{a->b} + Phi_{b->a}) (asymmetric-sum form).
d3 (independence check) = Euclidean distance between influence-row vectors.
Agreement: Spearman rank correlation on held-out pairs. H5 gate requires
all three pairwise Spearman > 0.7 on held-out data, stable across seeds.

## Decision gates (frozen)
G1 (calibration): planted-positive detected with Phi-delta > 5x epsilon on >=95% of
planted edges; null yields < 5% false edges at every epsilon in ladder.
G2 (influence): edge set nonempty, repeatable across both time halves and >= 4/5
initial states.
G3 (reduction test): edge set NOT isomorphic to any single supplied connectivity
pattern, and agreement with supplied structure measured (input-vs-output comparison,
Section 34).
G4 (matched controls): G_eff computed for H, H' (isospectral rewiring), permuted-
coupling, conjugate dynamics; classification into OUTCOMES A-E of Section 11.
G5 (reconstruction): d1/d2/d3 agreement on held-out sectors.
Promotion to H5 requires G1-G5 all met. Any failure -> record, do not rescue.

## Claim firewall
Report generator greps for forbidden transitions (Section 23 list) -> CI fail.
Labels restricted to Section 22 vocabulary.
