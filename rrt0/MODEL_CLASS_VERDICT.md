# RRT-0 — MODEL CLASS VERDICT

Status: **DERIVED IN PREFLIGHT — registered before any battery run.**

## Verdict

For the model class

```
finite closed system + linear unitary evolution
+ externally specified linear intervention + fixed operational readout
```

the intervention influence statistic is **fully reducible**:

```
Delta_rho(t,tau) = U^tau ( E[rho0(t)] - rho0(t) ) U^{-tau}    (exact)
Delta_rho_residual = 0                                        (identically)
```

Therefore raw Phi in this class is a **propagation / response diagnostic**,
not a diagnostic of irreducible emergence.

## What remains scientifically meaningful in this class

- operator spreading and scrambling (Phi_raw magnitude and support growth)
- sector-dependent response (representation dependence)
- numerical conditioning of long-time unitary propagation
- reachability of sectors under the declared dynamics

## What is ruled out as a claim in this class

- irreducible emergent influence
- causal structure not supplied by U, E, and B
- "emergence" verdicts from raw Phi alone

## Scope of the verdict

Derived analytically; to be confirmed numerically by the preflight
reducibility check (`model/reducibility.py`) at float64 roundoff.
A numerical residual above the predeclared tolerance (`1e-10`)
triggers `NUMERICALLY_UNRESOLVED` / `RESIDUAL_REQUIRES_AUDIT`, not a
refutation of the analytic identity.

No claim is extended beyond the registered model class.
