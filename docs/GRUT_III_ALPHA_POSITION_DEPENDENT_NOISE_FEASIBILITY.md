# GRUT-III Alpha — Position-Dependent Constitutive Noise Feasibility Audit

## Dipping Our Toes Into the Successor's Successor

**Predecessor:** GRUT-II Zeta (primitive universal D falsified by O4a; population integral kills signal by 23 orders)
**Function:** Determine whether D(r) — position-dependent constitutive noise — can evade the population bound while remaining internally coherent

---

## 1. Why GRUT-III

GRUT-II died honestly. The primitive universal D postulate was the simplest possible stochastic extension. Existing gravitational-wave data kills it: every BH in the universe contributes to an isotropic background that O4a constrains 23 orders of magnitude below the interesting regime.

The population integral kills D = constant because:
- Large D → large near-horizon fluctuations → large Omega_GW → EXCLUDED
- Small D → negligible fluctuations everywhere → indistinguishable from GRUT

There is no surviving window for constant D.

GRUT-III asks: what if D is NOT constant?

---

## 2. The Minimal GRUT-III Move

### The equation

```
tau_local(r) dPhi/dt + Phi = X(r) + xi(r, t)

<xi(r,t) xi(r',t')> = 2 D(r) delta(r - r') delta(t - t')
```

D(r) is now a FUNCTION of position, not a constant.

### What changed from GRUT-II

| | GRUT-II | GRUT-III |
|---|---|---|
| D | Constant (one number) | D(r) (function of position) |
| Ontology | Primitive constitutive constant | Constitutive field property (varies with environment) |
| Cost | +1P, +1p | +1P, +1 functional form |
| GRUT recovery | D → 0 | D(r) → 0 everywhere |
| Zeta bound | D < 10^-23 D_max (killed) | Depends on D(r) |

### The key question

What functional form D(r) simultaneously:
1. Evades the O4a population bound (suppresses near-horizon contribution)
2. Allows nontrivial fluctuations SOMEWHERE (otherwise trivial)
3. Has a physical motivation (not just tuned to evade the bound)
4. Reduces to a coherent theory (not just D = 0 with exceptions)

---

## 3. Candidate Functional Forms

### Candidate A: Gravitational suppression (D ~ f(r))

```
D(r) = D_0 * f(r) = D_0 * (1 - r_s/r)
```

Physical motivation: the noise strength is proportional to the metric function f(r). Near the horizon (r → r_s), f → 0, so D → 0. Far from sources (r → infinity), f → 1, so D → D_0.

**What this does to the population integral:**
- Near-horizon (r ~ r_s): D ≈ 0, sigma^2 ≈ 0. No contribution.
- At ISCO (r = 3 r_s): D = D_0 (2/3). Sigma^2 = D_0 (2/3) / tau_local. Reduced by factor 2/3.
- Far from source: D = D_0. Standard GRUT-II behavior.

**Problem:** The suppression at ISCO is only factor 2/3. The population bound requires suppression by 23 orders. This doesn't work.

**Verdict: INSUFFICIENT SUPPRESSION.**

### Candidate B: Exponential horizon suppression

```
D(r) = D_0 * exp(-(r_s/r)^n)
```

For n large enough, D drops sharply near the horizon.

**Problem:** This is pure parameter tuning. There is no physical mechanism for exponential suppression. The exponent n is a free parameter chosen to evade the bound.

**Verdict: AD HOC. Not a theory — a fit.**

### Candidate C: Fluctuation-dissipation consistency (D/tau = const)

```
D(r) = D_0 * tau_local(r) / tau_0
```

This maintains sigma^2 = D(r)/tau_local(r) = D_0/tau_0 = constant everywhere. The fluctuation amplitude is position-independent. The FDT relation D = k_B T tau is satisfied with T = constant.

**What this does:**
- sigma^2 = D_0/tau_0 everywhere (uniform fluctuation amplitude)
- Near horizon: D is SMALL (because tau_local is small)
- Far from source: D = D_0 (because tau_local = tau_0)

This is equivalent to GRUT-II with constant sigma^2 instead of constant D. The Langevin equation becomes:

```
tau_local dPhi/dt + Phi = X + xi(r,t)
<xi xi'> = 2 (D_0 tau_local / tau_0) delta delta
```

**Population integral:**
Omega_GW now depends on sigma^2 = D_0/tau_0, which is position-independent. The near-horizon contribution is:

```
delta_rho ~ drho/dPhi * sigma ~ sigma (position-independent)
delta_m ~ delta_rho * V_corr ~ sigma * tau_local^3 (DECREASING near horizon because V_corr ~ tau_local^3)
h ~ delta_m * omega^2 / R ~ sigma * tau_local^3 * (1/tau_local)^2 / R = sigma * tau_local / R
```

Near horizon, tau_local → 0, so h → 0 per source. The near-horizon enhancement VANISHES. The signal is now dominated by the FAR-FIELD regime where tau_local ~ tau_0 — which is the solar-system regime, already tested in XVIII Beta and found to be negligible (10^-16).

**This evades the population bound completely.** But it also produces no interesting signal anywhere. The fluctuations are uniform and tiny everywhere.

**Let me check the numbers:**

sigma^2 = D_0/tau_0. For D_0 = 0.01 tau_0 (from Delta bound): sigma^2 = 0.01.

The far-field signal: each source at distance R contributes h ~ sigma * tau_0 / R (in geometric units).

In SI at 10 kpc: tau_0 ~ 10^15 s (cosmological). tau_0 in geometric: tau_0 * c / r_s ~ 10^{20} for a solar-mass BH.

Actually, the far-field signal uses the COSMOLOGICAL tau_0, not the local t_dyn. Since tau_0 ~ 10^15 s:

```
h_single ~ sigma * tau_0_geom / R_geom
```

This is ENORMOUS (tau_0 is huge). Wait — that can't be right. Let me think again.

In the far field (r >> r_s), the constitutive equation is tau_0 dPhi/dt + Phi = X + xi with sigma^2 = 0.01. But X(r) ~ M/r^2 → 0. So Phi_eq → 0, and the fluctuation sigma is around zero.

The energy density fluctuation: delta_rho ~ drho/dPhi * sigma. But drho/dPhi = X(1-tau)/tau^2. In the far field, X → 0, so drho/dPhi → 0 (it depends linearly on X). Therefore delta_rho → 0 in the far field.

**The signal from each source is concentrated in the region where BOTH X is large AND D is not suppressed.** For Candidate C: X is large near the horizon but sigma is small there (tau_local small → V_corr small → h small). X is small far from the source. The maximum signal comes from an INTERMEDIATE radius where X * tau_local is maximized.

Let me compute where X(r) * tau_local(r) peaks:

```
X * tau_local ~ (M/r^2) * sqrt(r^3/(2M)) = sqrt(M/(2r))
```

This DECREASES with r. Maximum at r = r_s (the smallest radius). So the signal is ALWAYS dominated by the near-horizon contribution — but for Candidate C, the correlation volume V_corr ~ tau_local^3 shrinks faster than X grows.

The net h per source:

```
h ~ delta_rho * V_corr * omega^2 * sqrt(N) / R
  ~ (drho/dPhi * sigma) * tau^3 * (1/tau)^2 * 1 / R
  ~ drho/dPhi * sigma * tau / R
  ~ X * (1-tau)/tau^2 * sigma * tau / R
  ~ X * (1-tau) * sigma / (tau * R)
```

For Candidate C (sigma = const, tau = tau_local(r)):

```
h ~ X * sigma / (tau_local * R) ~ (M/r^2) * sigma / (sqrt(r^3/2M) * R)
  = sigma * M / (r^2 * sqrt(r^3/2M) * R)
  = sigma * sqrt(2M^3) / (r^{7/2} * R)
```

This peaks at small r (near horizon). But h is finite everywhere (no divergence at the horizon because r ≥ r_s).

At r = 3 r_s (ISCO): h ~ sigma * sqrt(2 M^3) / ((3r_s)^{3.5} * R).

Let me compute numerically for 10 M_sun at 10 kpc:

```
M_geom = 0.5 (in r_s units)
r_geom = 3
sigma = sqrt(0.01) = 0.1
h ~ 0.1 * sqrt(2 * 0.125) / (3^3.5 * R_geom)
  = 0.1 * 0.5 / (46.8 * 1.04e16)
  = 0.05 / (4.87e17)
  ~ 1.0e-19
```

At 10 kpc, h ~ 10^-19 per source. That's smaller than the GRUT-II D_max estimate (5e-17) by a factor ~500 — because the correlation volume shrinks (the signal is suppressed by tau_local^3 instead of being amplified).

Population integral: Omega ~ n * h^2 * R * tau * f^3 / H_0^2. With h ~ 10^-19:

```
Omega ~ 10^6 * (10^-19)^2 * (3e20)^2 * 5e-4 * (250)^3 * 1.4e26 / (3e22)^3 / (2.18e-18)^2
```

This needs careful computation. But the key point: h is 500x smaller, so h^2 is 2.5 × 10^5 times smaller, and the population Omega is reduced from 1.5 × 10^14 to about 6 × 10^8. Still above 2.8 × 10^-9 by a factor ~2 × 10^17.

**Candidate C ALSO fails the population bound.** The reduction from constant-D to FDT-consistent D(r) = D_0 tau_local/tau_0 only suppresses the per-source signal by ~500x. The population integral still overwhelms the O4a limit by 17 orders.

**Verdict: INSUFFICIENT. FDT-consistent D(r) still killed by population integral.**

### Candidate D: D proportional to curvature (D ~ R_abcd R^abcd)

```
D(r) = D_0 * (K(r) / K_ref)^alpha
```

where K = R_abcd R^abcd is the Kretschner scalar and alpha > 0.

For Schwarzschild: K = 48 M^2 / r^6. This PEAKS near the horizon and falls off far away.

**This gives LARGE D near the horizon and SMALL D far away — the OPPOSITE of what we need.** The population bound is dominated by near-horizon contributions. Making D LARGER there makes the problem WORSE.

**Verdict: WRONG DIRECTION.**

### Candidate E: D ~ 0 everywhere except asymptotically

```
D(r) = D_0 * (1 - exp(-r/r_noise))
```

where r_noise >> r_s is a large-scale cutoff. D is zero near the source and approaches D_0 far away, where the signal per source is negligible (X → 0).

**This would evade the population bound** because:
- Near horizon: D ≈ 0, no contribution
- Far from source: D = D_0, but X → 0, so delta_rho → 0 anyway

**Problem:** What sets r_noise? This is an entirely new length scale with no GRUT motivation. It's parameter tuning disguised as a functional form.

**Verdict: EVASION but not a theory. No physical motivation for r_noise.**

---

## 4. The Structural Diagnosis

### Why ALL reasonable D(r) fail

The population bound is:

```
Omega_GW ~ integral_0^{R_Hubble} n_BH * h^2(R) * S * dR / something
```

where h^2 from each BH is dominated by the near-horizon contribution (where X is large). For h to be small enough, either:

1. **D is small near the horizon** → suppresses fluctuations where they matter
2. **The coupling mechanism is suppressed** → fluctuations exist but don't radiate

Option 1 (Candidates A-E above) requires fine-tuning D(r) to be small precisely where the Level-1 rule makes tau small and the signal large. This is anti-correlated with the natural expectation (noise where there's dynamics) and requires a new mechanism.

Option 2 was tested in Epsilon (monopole vs quadrupole). The quadrupole radiation is O(1) unsuppressed because l_corr ~ r at ISCO. There is no natural coupling suppression.

### The root cause

The root cause is that the Level-1 rule (tau → t_dyn near horizon) makes the DAMPING FAST but the FLUCTUATION LARGE (if D is constant) or the SIGNAL CONCENTRATED (if D tracks tau). The constitutive architecture is designed so that the relaxation is most active near compact objects. Any noise that couples to this relaxation inherits the same spatial concentration. The more active the constitutive dynamics, the more the noise radiates. This is built into the architecture.

**The constitutive architecture is self-defeating for stochastic extensions: the regime where dynamics are richest (near compact objects) is the regime where noise is most observable (and most constrained).**

---

## 5. The Honest Assessment

### Is there ANY D(r) that works?

Technically yes: D(r) = 0 everywhere (= closed GRUT). Or D(r) = epsilon for astronomically tiny epsilon, which is observationally identical to D = 0.

No physically motivated, non-trivial D(r) evades the population bound. Every candidate either:
- Has insufficient suppression (Candidates A, C)
- Goes the wrong direction (Candidate D)
- Is unmotivated parameter tuning (Candidates B, E)
- Reduces to D ≈ 0 (no stochastic content)

### What this means for GRUT-III

GRUT-III (position-dependent D) does not solve the problem. The population integral is too powerful a constraint. The ~10^19 BHs in the observable universe, each contributing a near-horizon constitutive signal, create an isotropic background that existing data constrains to negligibility.

The issue is not the specific functional form of D(r). The issue is that ANY nonzero D in a regime where the constitutive dynamics are active (tau_local small, X large) produces a population-level signal that violates O4a.

---

## 6. What Remains

### The program after GRUT-III Alpha

The stochastic extension route — in ALL tested forms — is observationally dead:

| Version | D structure | Killed by |
|---------|------------|-----------|
| GRUT-II (Alpha-Delta) | D = constant | O4a population bound (Zeta: 23 orders) |
| GRUT-III Candidate A | D ~ f(r) | Insufficient suppression |
| GRUT-III Candidate C | D ~ tau_local | Still 17 orders above O4a |
| GRUT-III Candidate D | D ~ curvature | Wrong direction (amplifies near-horizon) |
| GRUT-III Candidate B, E | Tuned suppression | Ad hoc; not a theory |

### The architectural lesson

The GRUT constitutive architecture (Level-1 tau reduction → fast relaxation near compact objects) is STRUCTURALLY INCOMPATIBLE with any significant stochastic extension. The same mechanism that makes the constitutive dynamics physically interesting (active near compact objects) makes them observationally constrained (the universe is full of compact objects that LIGO can hear).

This is not a failure of imagination. It is a CONSTRAINT FROM REALITY. The constitutive architecture is good at organizing irreversible dynamics. It is observationally silent in gravity and observationally excluded in stochastic extensions.

### Where the program stands

```
GRUT:       CLOSED (Book XXI Terminal). Deterministic. Honest. Silent.
GRUT-II:    FALSIFIED (Zeta). Primitive universal D excluded by O4a.
GRUT-III:   NO VIABLE D(r) FOUND. Position-dependent noise fails.
```

The deterministic constitutive architecture (tau dPhi/dt + Phi = X) is the program's stable form. Every extension toward probability, noise, or observational contact with gravitational-wave data has been tested and excluded or found insufficient.

---

## 7. Final Verdict

**GRUT-III Alpha finds no viable position-dependent noise structure.**

The population integral constraint from ~10^19 astrophysical BHs is too powerful for any D(r) to evade without either reducing to D ≈ 0 (recovering closed GRUT) or introducing unmotivated fine-tuning.

The constitutive architecture's strength (Level-1 tau reduction → active dynamics near compact objects) is the same feature that makes any stochastic extension observationally excluded.

The program's honest terminal identity: **a deterministic irreversible constitutive framework that organizes physics from vacuum through biology, whose stochastic extensions are falsified by existing gravitational-wave data.**

---

*GRUT-III Alpha complete. Five candidate D(r) forms tested. None viable. Population integral kills all non-trivial extensions. The deterministic constitutive architecture is the program's stable endpoint.*
