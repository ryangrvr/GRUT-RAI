# GRUT III Book B — Stage B0: Source Coupling Interface Specification

**Inherited constraints:** BA1-BA7, X1-X10 from Book A.

---

## 1. Candidate Family for X[g]

### The structural requirement

X(g_r) is the equilibrium value that Phi_r relaxes toward in the constitutive law:

```
tau dPhi_r/dt + Phi_r = X(g_r)
```

X must be:
- A scalar functional of the metric g_{mu nu} (Phi is a scalar field)
- Local or quasi-local in spacetime (to preserve the Markovian structure in the controlled regime)
- Dimensionless or carry the dimensions of Phi (depending on Phi normalization)
- Reduce to a constant in flat space (X → X_0, the cosmological/background equilibrium)
- Respond to curvature in the way that the GRUT-I Level-1 formula implies

### Candidate A: Minimal (Ricci scalar)

```
X_A[g] = X_0 + alpha R
```

where:
- X_0: background equilibrium value (dimensionless or [Phi], depending on normalization). **Parameter.** [Phi].
- alpha: coupling constant. **Parameter.** [Phi] × [length]^2 (since R has dimensions 1/length^2).
- R: Ricci scalar of g_r. **Derived from metric.**

| Property | Assessment |
|----------|-----------|
| **Simplicity** | Minimal: one coupling constant beyond X_0. The simplest nontrivial scalar built from the metric. |
| **Flat-space limit** | X → X_0. ✓ |
| **Near a Schwarzschild BH** | R = 0 (vacuum Einstein equation: R_{mu nu} = 0 → R = 0). Therefore X_A = X_0 in vacuum. Phi sees NO curvature in the Schwarzschild exterior. |
| **Near a neutron star** | R ≠ 0 (matter present: R = -8 pi G T^{matter} / c^4). X responds to matter, not vacuum curvature. |
| **Compatibility with Level-1** | The Level-1 formula 1/tau_local = 1/tau_0 + 1/t_dyn involves t_dyn ~ 1/sqrt(G rho), which is a matter quantity. X_A = X_0 + alpha R ~ X_0 + alpha × G rho is consistent: curvature sources matter-dependent equilibrium. |
| **Regime** | Controlled in weak field (R << 1/alpha). Caution at moderate curvature. Unsafe at strong curvature (X_0 + alpha R could change sign or diverge). |

**Parameter list:**

| Parameter | Symbol | Dimensions | Status |
|-----------|--------|-----------|:------:|
| Background equilibrium | X_0 | [Phi] | **EFT input** |
| Curvature coupling | alpha | [Phi] × [length]^2 | **EFT input** |

### Candidate B: Kretschner alternative

```
X_B[g] = X_0 + beta sqrt(K)
```

where K = R_{mu nu rho sigma} R^{mu nu rho sigma} is the Kretschner scalar and beta is a coupling constant.

| Property | Assessment |
|----------|-----------|
| **Simplicity** | One coupling constant beyond X_0. Uses the Kretschner scalar, which is nonzero in vacuum (unlike R). |
| **Flat-space limit** | X → X_0. ✓ (K = 0 in flat space) |
| **Near Schwarzschild BH** | K = 48 G^2 M^2 / (c^4 r^6). Nonzero everywhere. sqrt(K) ~ GM/(c^2 r^3). X_B responds to vacuum curvature. |
| **Near a neutron star** | K ≠ 0 (both matter and curvature contribute). |
| **Compatibility with Level-1** | Less clear. sqrt(K) at the surface of a star scales as sqrt(G M / R_star^3) ~ 1/t_dyn. So X_B ~ X_0 + beta/t_dyn, which gives a curvature-dependent equilibrium that tracks the dynamical timescale. This is suggestive but the connection to Level-1 is indirect. |
| **Problem** | sqrt(K) diverges at r → 0 (BH singularity). In the weak-field limit, sqrt(K) is higher-order in Phi_N/c^2 than R. At the surface of the Sun: R ~ 10^-12 m^-2, sqrt(K) ~ 10^-12 m^-2. Similar magnitude — but K contains more geometric information. |
| **Regime** | Controlled in weak field. Caution at moderate curvature. Unsafe near singularities (sqrt(K) → infinity). |

**Parameter list:**

| Parameter | Symbol | Dimensions | Status |
|-----------|--------|-----------|:------:|
| Background equilibrium | X_0 | [Phi] | **EFT input** |
| Kretschner coupling | beta | [Phi] × [length]^2 | **EFT input** |

### Comparison

| Property | Candidate A (R) | Candidate B (sqrt(K)) |
|----------|:---:|:---:|
| Parameters beyond X_0 | 1 (alpha) | 1 (beta) |
| Nonzero in vacuum | **NO** | YES |
| Near-horizon response | None (R=0 in vacuum) | Strong (sqrt(K) ~ 1/r^3) |
| Near-star response | Yes (R ~ G rho) | Yes (sqrt(K) ~ sqrt(G rho)) |
| Level-1 compatibility | Direct (R ~ G rho ~ 1/t_dyn^2) | Indirect (sqrt(K) ~ 1/t_dyn) |
| Singularity behavior | Bounded in smooth spacetimes | Diverges at curvature singularities |
| Simplicity | Maximal | Slightly less |

---

## 2. Regime Tags

| Candidate | Controlled | Caution | Unsafe |
|-----------|:----------:|:-------:|:------:|
| A (Ricci) | Weak field, matter present | Moderate curvature, alpha R ~ X_0 | Strong field; vanishes in vacuum (blind to BH exterior) |
| B (Kretschner) | Weak field | Moderate curvature, beta sqrt(K) ~ X_0 | Near singularities (sqrt(K) → ∞) |

---

## 3. Consistency Checks (from Book A)

| Check | A (Ricci) | B (Kretschner) |
|-------|:---------:|:---------------:|
| BA2: Constitutive law structure preserved? | ✓ (X is a scalar, enters linearly) | ✓ (same) |
| BA4: tau, D, T remain EFT parameters? | ✓ (X does not determine tau) | ✓ |
| X1: No covariance claim? | Both candidates are covariant scalars. But the CTP action is NOT covariant (Newtonian limit). The use of R or K as X does not make the action covariant. No covariance claim is made. | Same |
| X5: No strong-field claim? | Both candidates are specified for the weak-field regime. Strong-field behavior is tagged as CAUTION/UNSAFE. | Same |

---

## 4. Failure Modes and Nonclaims

| # | Failure/Nonclaim | Applies to |
|---|-----------------|:----------:|
| F1 | X_A = X_0 + alpha R vanishes in vacuum Schwarzschild. Phi does not respond to BH exterior curvature. This may be physically wrong if Phi should respond to tidal forces. | A only |
| F2 | X_B diverges at curvature singularities. Phi → ±∞ at r → 0. Requires regularization. | B only |
| F3 | Neither candidate determines alpha or beta from first principles. Both introduce one additional EFT parameter. | Both |
| F4 | Neither candidate has been tested against observational constraints (fifth-force bounds, PPN parameters, etc.). | Both |
| F5 | The choice between A and B cannot be made within the weak-field regime — they give the same leading-order behavior near matter (both ~ G rho). The discriminator is vacuum curvature (R = 0 vs K ≠ 0), which is a moderate-to-strong-field question. | Both |

---

## 5. Decision: Provisional Interface

**Adopted: Candidate A (Ricci scalar), with explicit flag that vacuum-curvature blindness (F1) is a known limitation.**

**Rationale:**
1. Maximal simplicity (one parameter beyond X_0).
2. Direct compatibility with Level-1 (R ~ G rho ~ 1/t_dyn^2, matching the Level-1 matter-density dependence).
3. The weak-field regime — where all Book A claims are controlled — does not distinguish A from B.
4. The vacuum-blindness limitation (F1) is a strong-field issue, which is UNSAFE per Book A. It does not invalidate A in the controlled regime.
5. If a vacuum-curvature response is needed (e.g., BH exterior physics), B is the natural extension. But this is a Book C issue, not Book B.

**Provisional interface:**

```
X[g_r] = X_0 + alpha R(g_r)

Parameters: X_0 (background equilibrium), alpha (curvature coupling)
Regime: weak field (alpha R << X_0)
Status: ASSUMED (provisional)
Confidence: 0.50 (structurally motivated, not derived or tested)
```

**Conflict note (CN-B0-1):** This choice is PROVISIONAL and must be revisited if the program extends to vacuum spacetimes (BH exteriors). In that regime, Candidate B (Kretschner) is the minimal replacement.

---

*B0 complete. X[g_r] = X_0 + alpha R(g_r) adopted as provisional source coupling. One EFT parameter (alpha) beyond the background value X_0. Controlled in weak field. Vacuum-blind (R=0 in Schwarzschild exterior). Alternative B (Kretschner) flagged for strong-field extension.*
