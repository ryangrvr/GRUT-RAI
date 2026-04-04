# Appendix T-B: Native Irreversibility and Semigroup Structure

GRUT Thermodynamic Program -- Phase T-B

---

## Question
Is native GRUT dissipative evolution genuinely irreversible in a purely
dynamical sense?

---

## Core Analysis

The native constitutive equation tau dPhi/dt + Phi = X has exact solution:
    Phi(t) = Phi(0) exp(-t/tau) + (1/tau) int_0^t exp(-(t-s)/tau) X(s) ds

### Forward Contraction Semigroup (Track A)
S(t) = exp(-t/tau) satisfies S(0)=I, S(t+s)=S(t)S(s), ||S(t)||<1 for t>0.
This is a **strongly continuous contraction semigroup**.

### Asymptotic State Forgetting (Track B)
|Phi_1(t) - Phi_2(t)| = |Phi_1(0) - Phi_2(0)| exp(-t/tau).
Initial conditions forgotten exponentially. Backward reconstruction
requires exp(+t/tau) amplification: **physically non-recoverable**.

### Attractor Structure (Track C)
- Free: Phi -> 0 (global attractor)
- Constant: Phi -> X0 (global attractor)
- Driven: tracking manifold

### Genuine Irreversibility (Track D)
Stronger than time asymmetry: contraction + state forgetting +
attractor relaxation + non-recoverability = genuine dynamical
irreversibility.

---

## Evidence Table

| Regime | Forward? | Inverse? | Contractive? | Attractor? | Recoverable? | Verdict |
|--------|----------|----------|-------------|-----------|-------------|---------|
| Free X=0 | Yes | Formal only | Yes exp(-t/tau) | Origin | Lost exp. | irreversible |
| Const X=X0 | Yes | Formal only | Yes | X0 | Lost exp. | irreversible |
| Time-dep X(t) | Yes | Needs history | Yes (diffs) | Tracking | Needs history | conditional |
| Long-time | Yes | Exp. unstable | Yes | Yes | Exp. lost | forgetting |
| Backward | N/A | Amplifying | No | N/A | Non-recoverable | non-physical |
| Nearby states | Yes | N/A | Yes: delta*exp(-t/tau) | N/A | Forgotten | contraction |

---

## Five Hard-Gated Verdicts

| Verdict | Value |
|---------|-------|
| Evolution | forward_semigroup_natively_supported |
| Invertibility | asymptotically_state_forgetting |
| Attractor | relaxation_to_fixed_or_steady_structures_supported |
| Irreversibility | genuine_dynamical_irreversibility_supported |
| Authorization | authorized_to_proceed_to_TC |

**Overall: native_irreversibility_supported_under_dynamical_reading**

---

## Licensed Language
- Forward contraction semigroup
- Exponential state forgetting (rate 1/tau)
- Dynamical non-recoverability
- Global attractor relaxation
- Genuine dynamical irreversibility

## NOT Licensed
- Entropy, entropy production
- Temperature
- Statistical mechanics, ensembles
- Equilibrium thermodynamics
- Bath interpretation
- Free energy, partition function

---

## Authorization
**T-C (Entropy-Like Monotones and Dissipation Functionals) is authorized.**

Native irreversibility is established. T-C may now test whether any
monotonically decreasing/increasing functional exists under the native
dissipative evolution.
