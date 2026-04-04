# APPENDIX G — LEVEL-1 τ REDUCTION: DERIVATION AND JUSTIFICATION AUDIT

**Date:** 2026-03-27
**Status:** DERIVATION AUDIT COMPLETE — three routes evaluated, one partially viable
**Executive determination:** `structurally_motivated_heuristic_not_derived`
**Classification basis:** Full codebase analysis + algebraic verification

---

## 1. QUESTION BEING ANSWERED

The GRUT collapse solver (`collapse.py`) implements a local gravitational timescale reduction as a **mode switch**:

```
local_tau_mode = "off"   →  use bare τ₀ (cosmological anchor)
local_tau_mode = "tier0" →  τ_local = τ₀ · t_dyn / (t_dyn + τ₀)
```

where `t_dyn = sqrt(R³ / (2GM))` is the Newtonian free-fall timescale.

**The question:** Is there a derivable criterion that determines when this reduction should activate, and can the mode switch be replaced by a principled condition?

**Why this matters:** Three prior appendices (E, F, D) inherit the Level-1 rule as an input:
- Appendix E identified τ_eff non-covariance as a root failure.
- Appendix F found that the structural identity ω₀·τ = 1 uses τ_local, not τ₀.
- Appendix D (thermodynamic sector) uses ω₀ derived from τ_local.

Until the Level-1 rule has a principled basis, sectors that depend on it carry this as a heuristic assumption.

---

## 2. THE LEVEL-1 FORMULA: ALGEBRAIC STRUCTURE

### 2.1 The Formula

```
τ_local = τ₀ · t_dyn / (τ₀ + t_dyn)
```

### 2.2 Algebraic Identity: Parallel-Rate Equivalence

The Level-1 formula is algebraically identical to a **parallel-rate sum**:

```
1/τ_local = 1/τ₀ + 1/t_dyn
```

**Proof:** Direct algebra.
```
  1/τ_local = (τ₀ + t_dyn) / (τ₀ · t_dyn)
            = 1/t_dyn + 1/τ₀
```

This is the standard formula for two processes competing in parallel:
the process with rate 1/τ₀ (global cosmological relaxation) and the process
with rate 1/t_dyn (local dynamical decoherence). The combined effective rate
is the sum of the two rates.

### 2.3 Limiting Behavior

| Regime | Condition | τ_local | Physical meaning |
|--------|-----------|---------|-----------------|
| Cosmological limit | t_dyn >> τ₀ | → τ₀ | Global channel dominates; local dynamics slow |
| Local gravitational limit | t_dyn << τ₀ | → t_dyn | Local dynamics fast; global channel negligible |
| Crossover | t_dyn = τ₀ | = τ₀/2 | Equal competition; smooth interpolation |

The crossover is smooth (no discontinuity), which is the only structurally consistent interpolation between the two limits given the parallel-rate structure.

---

## 3. THE STRUCTURAL IDENTITY CONNECTION

### 3.1 The Locked Identity

The interior PDE sector (Phase III-C, locked) establishes:

```
ω₀ · τ = 1     (at the GRUT equilibrium endpoint R_eq = r_s/3)
```

where τ is the memory timescale used in the dispersion relation. The question is: which τ?

### 3.2 Algebraic Derivation of ω₀ · t_dyn = 1

**Claim:** For β_Q = 2, ω₀ · t_dyn(R_eq) = 1 exactly, independent of mass.

**Proof:**
```
  ω₀ = sqrt(β_Q · GM / R_eq³)              [definition from interior PDE]
  t_dyn(R_eq) = sqrt(R_eq³ / (2GM))        [Newtonian free-fall time]

  ω₀ · t_dyn = sqrt(β_Q · GM / R_eq³) · sqrt(R_eq³ / (2GM))
             = sqrt(β_Q · GM · R_eq³ / (R_eq³ · 2GM))
             = sqrt(β_Q / 2)
             = sqrt(2 / 2)    [for β_Q = 2]
             = 1              (exactly)
```

This is a pure algebraic identity, valid for all masses, requiring only β_Q = 2.

### 3.3 Why τ_local ≈ t_dyn for Astrophysical Masses

For a 30 M_sun black hole at R_eq:
- t_dyn(R_eq) ≈ 2.94×10⁻⁴ s
- τ₀ = 1.3225×10¹⁵ s
- Ratio: t_dyn/τ₀ ≈ 2.22×10⁻¹⁹

Therefore: τ_local = τ₀ · t_dyn / (τ₀ + t_dyn) ≈ t_dyn · (1 - t_dyn/τ₀ + ...)

The fractional correction is ≈ 2.22×10⁻¹⁹ — beyond double-precision floating point
resolution. For all practical purposes, τ_local = t_dyn exactly.

### 3.4 Structural Identity Requires τ_local, Not τ₀

| Quantity | Value (30 M_sun at R_eq) | Consistent with ω₀·τ = 1? |
|----------|--------------------------|--------------------------|
| τ₀ | 1.3225×10¹⁵ s | NO — ω₀·τ₀ ≈ 3.9×10¹⁹ >> 1 |
| τ_local | ≈ t_dyn = 2.94×10⁻⁴ s | YES — ω₀·τ_local ≈ 1.0 to 10⁻¹⁹ |
| t_dyn | 2.94×10⁻⁴ s | YES (exactly) — ω₀·t_dyn = 1.0 |

**Conclusion:** The structural identity ω₀·τ = 1 is a locked GRUT result.
For this identity to hold with any physical validity at astrophysical masses,
τ must be τ_local (equivalently, t_dyn), never τ₀.

---

## 4. DERIVATION ROUTES: THREE ATTEMPTS

### Route A — Parallel-Rate (Competing Channels)

**Claim:** Two processes compete to relax the memory state:
1. **Global channel** (rate 1/τ₀): the cosmological memory bath relaxes M_drive toward its cosmological equilibrium with timescale τ₀ (Phase I anchor).
2. **Local channel** (rate 1/t_dyn): the local gravitational dynamics change on timescale t_dyn. When t_dyn << τ₀, the memory cannot track the cosmological equilibrium — it can only track local changes on the scale t_dyn.

The total effective relaxation rate is the sum of both rates:
```
  1/τ_local = 1/τ₀ + 1/t_dyn
```

**Causality argument for the local channel:** The memory integral
`∫ a_grav(t') exp(-(t-t')/τ₀) dt'` averages over a_grav with exponential
weighting over timescale τ₀. If a_grav changes significantly on timescale
t_dyn << τ₀, the integral averages over many dynamical cycles and loses
phase coherence. The effective memory coherence time is therefore capped
by t_dyn. This is a physical causality/information argument, not a derivation
from the GRUT field equations.

**Verdict:** `PARTIALLY_VIABLE`

**What it provides:** The formula for τ_local, given that both channels exist.

**What it does NOT provide:** A derivation that the local channel (rate 1/t_dyn)
necessarily exists as a consequence of the GRUT constitutive equation
τ_eff u^α ∇_α Φ + Φ = X[g, T]. The local channel is motivated by physical
reasoning but not derived from GRUT structure.

---

### Route B — Covariant Reduction from Field Equations

**Claim:** The GRUT covariant field equation
```
  τ_eff u^α ∇_α Φ + Φ = X[g, T]
```
should, in the spherically symmetric collapsing regime, reduce to the
collapse memory ODE with τ_eff = τ_local.

**What is needed:**
1. The interior metric g_μν (to compute u^α and ∇_α in the collapsing frame).
2. The covariant form of τ_eff (how it depends on g_μν and on spacetime geometry).

**Why this is blocked:**
- The covariant interior metric is an **unresolved missing closure** — see
  `PHASE_III_C_COVARIANT_CLOSURE.md`. The interior of the BDCC at R_eq = r_s/3
  (inside the Schwarzschild horizon) does not have a GRUT-derived metric tensor.
  The collapse dynamics are governed by the Newtonian-like ODE system, not by
  a covariant wave equation on a metric spacetime.
- Even if the metric were available, the covariant form of τ_eff has not been
  specified. In the cosmological sector, τ_eff = τ₀/(1+(Hτ₀)²) uses the
  Hubble rate H as the dynamical frequency. In the collapse sector, the
  dynamical frequency is |V/R| ≈ 1/t_dyn near the endpoint. The substitution
  H → 1/t_dyn is a regime translation (see Appendix F), not a covariant law.

**Verdict:** `CLOSED`

**Blocker:** Interior metric + covariant τ_eff formulation, both unresolved
(PHASE_III_C_COVARIANT_CLOSURE.md, PHASE_III_FINAL_FIELD_EQUATIONS.md).

---

### Route C — Structural Consistency (Retroactive)

**Claim:** τ_local is the **unique** timescale consistent with the locked
structural identity ω₀·τ = 1 for all astrophysical masses. This constitutes
a structural necessity argument.

**Verification:** ω₀·t_dyn(R_eq) = 1 (algebraically exact, from Section 3.2).
Therefore any τ in the identity must satisfy τ ≈ t_dyn for astrophysical masses.
τ_local = τ₀·t_dyn/(τ₀+t_dyn) ≈ t_dyn to 19-digit precision for 30 M_sun.

**Why this is a consistency argument, not a derivation:**
The structural identity ω₀·τ = 1 was **itself derived** (in interior_pde.py)
using τ = τ_local. Showing that τ_local is required for the identity to hold
is circular: the identity was built from τ_local, so τ_local trivially satisfies it.
This is a consistency check, not an independent derivation of the Level-1 rule.

The argument does, however, provide this useful statement: **if** the
structural identity ω₀·τ = 1 is treated as a fundamental law (not just
a consequence of the τ choice), then τ_local is the only timescale in the
τ-family that satisfies it for astrophysical masses.

**Verdict:** `CONSISTENCY_ARGUMENT_NOT_DERIVATION`

---

## 5. ACTIVATION CRITERION

### 5.1 Natural Criterion

The Level-1 rule should activate when the local dynamical channel
(rate 1/t_dyn) is comparable to or faster than the global channel (rate 1/τ₀):

```
  t_dyn < τ₀     (Level-1 regime: local dynamics dominate)
  t_dyn > τ₀     (Level-0 regime: cosmological dynamics dominate)
```

This is equivalent to a crossover radius condition:

```
  R < R_cross = (2GM · τ₀²)^{1/3}     →  Level-1 active
  R > R_cross                           →  Level-0 (τ₀ is appropriate)
```

### 5.2 Numerical Values at 30 M_sun

| Quantity | Value |
|----------|-------|
| τ₀ | 1.3225×10¹⁵ s |
| r_s (Schwarzschild radius) | 8.85×10⁴ m (88.5 km) |
| R_eq = r_s/3 (endpoint) | 2.95×10⁴ m |
| R_cross = (2GM·τ₀²)^{1/3} | ~2.39×10¹⁷ m (~25 light-years) |
| R_cross / r_s | ~2.7×10¹² |
| t_dyn(R_eq) | ~2.94×10⁻⁴ s |
| t_dyn(R_eq) / τ₀ | ~2.22×10⁻¹⁹ |

### 5.3 Astrophysical Universality

For any astrophysical BH mass:
```
  R_cross = (2GM · τ₀²)^{1/3}
  r_s     = 2GM / c²

  R_cross / r_s = (2GM · τ₀²)^{1/3} / (2GM/c²)
               = (c²τ₀² / (2GM))^{1/3} · τ₀/r_s × ... [simplifying]
               = (c²τ₀)^{2/3} / (2GM)^{2/3}
               ∝ M^{-2/3}    (decreases with mass, but very slowly)
```

For M = 30 M_sun: R_cross/r_s ~ 10¹².
For M = 10⁹ M_sun (supermassive BH): R_cross/r_s ~ 10⁶.

In all astrophysical cases, R_cross >> r_s >> R_eq, confirming that the Level-1
regime covers the entire physically relevant range of radii. There is no known
astrophysical BH at which the Level-0 approximation would be physically appropriate.

### 5.4 Is the Criterion Covariant?

No. The criterion t_dyn < τ₀ uses `t_dyn = sqrt(R³/(2GM))`, which is a
Newtonian free-fall timescale evaluated in coordinate time. It is not a proper
time, not derived from the metric, and not covariant under general coordinate
transformations. The criterion is **deterministic** (given R, M) but not
**covariant**. Covariant derivation remains blocked by the interior metric closure.

---

## 6. CONSEQUENCES FOR THE MODE SWITCH

### 6.1 Current Implementation

```python
# collapse.py
def _compute_tau0_local(tau0_s, R, M_kg, local_tau_mode):
    if local_tau_mode == "off":
        return tau0_s                    # INCORRECT for astrophysical physics
    if local_tau_mode == "tier0":
        t_dyn_local = sqrt(R³/(2GM))
        return tau0_s * t_dyn_local / (t_dyn_local + tau0_s)  # CORRECT
```

### 6.2 Recommendation

**For all astrophysical BH physics:** Use `local_tau_mode="tier0"`.
The condition t_dyn < τ₀ is satisfied at every astrophysical radius.
Using `local_tau_mode="off"` gives τ₀ as the memory timescale, which:
- Violates the structural identity ω₀·τ = 1 by a factor of ~10¹⁹.
- Gives τ_eff = τ₀/(1+(|V/R|·τ₀)²) ≈ 0 at any non-zero velocity
  (because |V/R|·τ₀ >> 1 during astrophysical collapse).
- Renders the memory ODE dM_drive/dt = (a_grav - M_drive)/τ_eff
  non-physical (effectively instantaneous or frozen depending on
  numerical implementation).

**Valid uses of `local_tau_mode="off"`:**
- Code validation (comparing against analytic limits).
- Testing in hypothetical cosmological parameter ranges (R > R_cross).
- No known astrophysical scenario.

### 6.3 Can the Mode Switch Be Replaced?

In principle: yes. The deterministic criterion `t_dyn < τ₀` (equivalently
`R < R_cross`) could be evaluated at each timestep and the appropriate formula
selected. This would eliminate the manual switch.

However: this replacement is not covariant, and making it the default without
documentation would obscure the underlying derivational gap. **The switch should
be kept as a documented parameter** but the default for physical runs should be
established as "tier0".

---

## 7. CONSEQUENCES FOR OTHER SECTORS

### 7.1 Structural Identity (Interior PDE)

The locked structural identity ω₀·τ = 1 is now understood to be:

```
  ω₀ · t_dyn(R_eq) = 1     [algebraic identity from β_Q = 2]
  ω₀ · τ_local(R_eq) ≈ 1   [because τ_local ≈ t_dyn for astrophysical masses]
  ω₀ · τ₀ >> 1              [τ₀ is WRONG in the structural identity]
```

The identity is not a coincidence — it is a consequence of β_Q = 2 and the
endpoint law R_eq = r_s/3. It would break if either β_Q ≠ 2 or if τ₀ were
used in place of τ_local.

### 7.2 Temperature Candidates (Appendix D)

The temperature candidates T_structural = ℏω₀/k_B and T_dissipation = ℏω₀/(Qk_B)
use ω₀ derived from τ_local via the structural identity. They are therefore
implicitly dependent on the Level-1 rule:

```
  T_structural = ℏω₀/k_B = ℏ/(τ_local · k_B) = ℏ/k_B · 1/t_dyn(R_eq)
```

This is a mass-dependent temperature (since t_dyn(R_eq) ∝ M). The Level-1 rule
propagates into the thermodynamic sector through ω₀. If the Level-1 rule is
revised, T_structural and T_dissipation are revised.

### 7.3 Q-Factor (Interior PDE)

Q = β_Q/α_vac = 6 is derived from parameters, not from τ directly. Q is
independent of the Level-1 rule. However, Q is used in T_dissipation:

```
  T_dissipation = ℏω₀/(Q·k_B) = ℏ/(Q·τ_local·k_B)
```

The Q-factor audit (Appendix E Check 2) found that all three Q-derivation
routes are degenerate (share hidden assumptions). This degeneracy is not
affected by the Level-1 audit.

### 7.4 τ_eff in the Lorentzian Filter (Level 2)

The Level-2 Lorentzian filter (τ_eff = τ_base/(1+(ω·τ_base)²)) uses τ_base:
- In the collapse sector with `local_tau_mode="tier0"`: τ_base = τ_local ≈ t_dyn
- In the cosmological sector: τ_base = τ₀

At the equilibrium endpoint V = 0 (ω = |V/R| = 0): τ_eff = τ_base = τ_local.
The Level-2 filter is transparent at equilibrium, so the Level-2 result
inherits the Level-1 conclusion unchanged.

---

## 8. WHAT A FULL DERIVATION WOULD REQUIRE

A covariant derivation of the Level-1 rule would need to show that the GRUT
constitutive equation τ_eff u^α ∇_α Φ + Φ = X[g, T], reduced to the
spherically symmetric collapsing regime with the appropriate interior metric,
produces an effective timescale

```
  τ_eff_covariant = f(g_μν, u^α) → τ₀ · t_proper / (τ₀ + t_proper)
```

where t_proper is the proper-time analogue of the Newtonian t_dyn.

This requires:
1. The interior covariant metric g_μν at R_eq (MISSING CLOSURE — Phase III-C).
2. The observer 4-velocity u^α in the collapsing frame (depends on metric).
3. A specification of τ_eff as a function of the metric (currently unspecified).
4. A proof that the proper-time version of t_dyn reduces to the Newtonian
   t_dyn = sqrt(R³/(2GM)) in the appropriate limit.

None of these are available. The derivation is not achievable with current
GRUT architecture without resolving the interior covariant closure.

---

## 9. EXECUTIVE DETERMINATION

> **`structurally_motivated_heuristic_not_derived`**

The Level-1 τ reduction rule τ_local = τ₀·t_dyn/(τ₀+t_dyn) is:

1. **Algebraically principled:** equivalent to a parallel-rate sum with
   two physically motivated competing channels (Route A: PARTIALLY_VIABLE).

2. **Structurally consistent:** the only timescale in the τ-family that
   satisfies the locked structural identity ω₀·τ = 1 for all astrophysical
   masses, though this consistency is circular since the identity was derived
   using τ_local (Route C: CONSISTENCY_ARGUMENT_NOT_DERIVATION).

3. **NOT covariant:** the formula uses the Newtonian t_dyn, not a proper time.
   The covariant derivation from GRUT field equations is blocked by the missing
   interior metric closure (Route B: CLOSED).

4. **Astrophysically universal:** the Level-1 regime (t_dyn < τ₀) covers every
   astrophysically realistic BH radius, from far exterior through the equilibrium
   endpoint. The crossover radius R_cross is ~10¹² Schwarzschild radii for 30 M_sun.

5. **Deterministically activatable:** the criterion t_dyn < τ₀ is deterministic
   (given R, M) and could replace the manual mode switch, though it is not covariant.

---

## 10. SAFE AND UNSAFE CLAIMS

### Safe Claims (Post-Appendix G)

1. The Level-1 rule is algebraically equivalent to a parallel-rate sum:
   1/τ_local = 1/τ₀ + 1/t_dyn.

2. For all astrophysical BH masses, t_dyn(R_eq) << τ₀, so τ_local ≈ t_dyn(R_eq)
   to precision far beyond any numerical representation.

3. ω₀·t_dyn(R_eq) = 1 exactly (algebraic identity from β_Q = 2 and R_eq = r_s/3),
   independent of mass.

4. ω₀·τ_local(R_eq) ≈ 1.0 for astrophysical masses (relative error ~ t_dyn/τ₀ ~ 10⁻¹⁹).

5. The Level-1 rule is a NECESSARY CONDITION for the structural identity ω₀·τ = 1
   to hold with physical validity (the identity is violated by a factor ~10¹⁹
   if τ₀ is used instead of τ_local).

6. A deterministic activation criterion exists: Level-1 activates when t_dyn < τ₀,
   equivalently R < R_cross = (2GM·τ₀²)^{1/3}.

7. For 30 M_sun: R_cross/r_s ~ 2.7×10¹², so Level-1 always activates for any
   realistic BH radius.

### Unsafe Claims (Must Not Be Made)

1. That the Level-1 rule is derived from GRUT field equations.
2. That the Level-1 rule is covariant.
3. That the causality argument for the local channel is a proof.
4. That the structural consistency argument (Route C) is an independent derivation.
5. That `local_tau_mode="off"` is physically correct for any astrophysical BH.
6. That the mode switch is obsolete (it remains needed for testing and validation).

---

## 11. INHERITED CLASSIFICATIONS (UNCHANGED)

- **Appendix E:** `locally_consistent_globally_underdetermined` — UNCHANGED.
  The Level-1 audit does not resolve the τ_eff non-covariance identified in
  Appendix E. It provides a stronger justification for τ_local over τ₀, but
  the covariant form of τ_eff remains absent.

- **Appendix F:** `tau_symbolically_conflated_but_rescuable` — UNCHANGED.
  The Level-1 audit reinforces the Appendix F conclusion that the Level-1 rule
  is a "motivated heuristic," not a covariant derivation.

- **Appendix D:** `thermodynamic_sector_partially_consistent` — UNCHANGED.
  The Level-1 audit clarifies that T_structural and T_dissipation implicitly
  depend on the Level-1 rule through ω₀. This dependence was already present
  but not documented.

---

## 12. CODE ARTIFACTS

| File | Description |
|------|-------------|
| `grut/tau_level1_audit.py` | Audit module — timescale profile, three routes, activation criterion |
| `tests/test_tau_level1_audit.py` | 70 tests, all passing |

**Key numeric results (30 M_sun reference):**

| Test | Value | Verdict |
|------|-------|---------|
| ω₀·t_dyn(R_eq) | 1.000000000000 | EXACT (algebraic) |
| ω₀·τ_local(R_eq) | 1.000000000000 | ≈ exact (error ~10⁻¹⁹) |
| ω₀·τ₀ | ~3.9×10¹⁹ | WRONG — τ₀ is not the identity timescale |
| t_dyn(R_eq)/τ₀ | ~2.2×10⁻¹⁹ | Confirms astrophysical Level-1 regime |
| R_cross/r_s | ~2.7×10¹² | Level-1 criterion covers all BH radii |
