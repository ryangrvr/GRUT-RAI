# RRT-0 — PREFLIGHT: STRUCTURAL NO-GO (CLOSED LINEAR UNITARY MODEL CLASS)

Status: **BANKED ANALYTIC RESULT — not a diagnostic defect.**

## 1. Exact identity

Registered model class:

```
finite closed system + linear unitary evolution
+ externally specified linear intervention + fixed operational readout
```

Unperturbed and perturbed states evolve under the same closed unitary map:

```
rho_0(t+tau)      = U^tau rho_0(t) U^{-tau}
rho_E(t+tau)      = U^tau E[rho_0(t)] U^{-tau}
```

Injected difference at the intervention event:

```
delta_rho_E(t) = E[rho_0(t)] - rho_0(t)
```

Then, **exactly** (from linearity, no approximation):

```
Delta_rho_E(t,tau) = rho_E(t+tau) - rho_0(t+tau)
                   = U^tau delta_rho_E(t) U^{-tau}
```

For any readout observable `B`:

```
Delta<B>_E(t,tau) = Tr[ B U^tau delta_rho_E(t) U^{-tau} ]
```

## 2. Consequence

The raw influence statistic

```
Phi_{a->b}(t,tau) = sup_{B in B_b, ||B||<=1} | Delta<B> |
```

is fully determined by the supplied structures `{U, E, rho_0, B}`.

**Phi_raw is a propagation/response diagnostic. It is NOT a diagnostic of
irreducible emergence.**

What raw Phi CAN establish:
- operator spreading
- scrambling / mixing
- sensitivity to perturbation
- reachability in the declared dynamical system
- representation (sector) dependence of response

What raw Phi CANNOT establish:
- any causal or influence structure not reducible to the supplied
  dynamics, intervention, and readout structure.

## 3. Reducibility decomposition (NOT a "repair")

```
Delta_rho_raw = Delta_rho_supplied + Delta_rho_residual
Delta_rho_supplied = U^tau ( E[rho] - rho ) U^{-tau}
```

For this model class:

```
Delta_rho_residual = 0        (identically)
```

Numerically, the residual ratio should sit at float64 roundoff
(~1e-14 .. 1e-12 depending on propagation length and conditioning).

Implementation: `rrt0/model/reducibility.py`
- Route A: propagate `delta_rho` directly.
- Route B: propagate `rho_0` and `rho_E` independently, subtract.
- Route C: Heisenberg check `Tr[delta_rho U^{-tau} B U^tau]`.
- Verdict computed from predeclared tolerance ladder; never hard-coded.

## 4. Claim boundaries

- This does NOT show relational emergence is impossible.
- It shows the registered model class cannot demonstrate irreducible
  emergent influence under the reducibility criterion.
- The raw diagnostic remains valid for propagation/scrambling studies.

See `MODEL_CLASS_VERDICT.md` and `PREFLIGHT_FINAL.md`.
