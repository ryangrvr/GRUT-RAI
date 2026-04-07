# GRUT III — Book D, Stage D2: Meta-Principle Elevation (Ansatz vs Necessity)

**Predecessor:** D1 (generic_reconstruction_success). All Book-C outputs reproduced generically. Sole remaining uniqueness candidate: the meta-principle "Φ relaxes toward geometry-determined equilibrium."

---

## 1. Theorem-Candidate Table

### Candidate A: Thermodynamic necessity

```
ASSUMPTIONS:
  A-1. Φ is a scalar field coupled to gravity on a CTP contour.
  A-2. The dynamics of Φ is first-order dissipative (overdamped).
  A-3. The system is in thermal equilibrium with a bath at temperature T > 0.
  A-4. The CTP action satisfies unitarity (U1-U3) and the KMS symmetry
       (fluctuation-dissipation theorem).

CLAIM:
  The equilibrium value Φ* must be a functional of the metric: Φ* = X[g].
  Specifically: the KMS condition, combined with general covariance of the
  background, forces the equilibrium to be a scalar constructed from g_{μν}.

SCOPE:
  Weak-curvature, Markovian, overdamped, thermal equilibrium.

FAILURE CONDITIONS:
  - If Φ has no coupling to gravity at all (pure matter sector): Φ* is
    independent of g, and the claim is trivially false.
  - If Φ is not in equilibrium (transient dynamics): Φ* is not reached.
```

### Candidate B: Admissibility-geometric tracking

```
ASSUMPTIONS:
  B-1. Same as A-1, A-2.
  B-2. The admissibility functional A requires that Φ approaches a fixed
       point Φ* in finite time (convergence/attractor condition).
  B-3. The background geometry g_{μν} is a solution of Einstein's equation
       (on-shell metric).
  B-4. Φ couples to g through the action (not just through initial conditions).

CLAIM:
  If Φ must converge to a fixed point that is consistent with the on-shell
  metric, then Φ* is constrained to be a functional of the on-shell geometry:
  Φ* = X[g_{on-shell}].

SCOPE:
  Same as A. Plus: g must be on-shell (satisfies Einstein equation).

FAILURE CONDITIONS:
  - If the convergence condition (B-2) is dropped: Φ may never reach
    equilibrium, and Φ* is undefined.
  - If Φ does not couple to g (B-4 violated): Φ* is geometry-independent.
```

### Candidate C: Cross-sector consistency (USL ↔ constitutive)

```
ASSUMPTIONS:
  C-1. The USL rate is Λ = Gm²/(ℏl), derived from the gravitational
       self-energy in the CTP influence functional (Sector 3).
  C-2. The constitutive relaxation rate is 1/τ, from the environmental
       bath (Sectors 1-2).
  C-3. Both arise from the SAME CTP action.
  C-4. The action is self-consistent: the semiclassical Einstein equation
       is satisfied (backreaction of Φ on g is perturbatively included).

CLAIM:
  Self-consistency of the semiclassical Einstein equation, combined with
  the CTP structure, imposes a relation among {τ, α, β, D} that reduces
  the independent parameter count.

SCOPE:
  Weak curvature, perturbative backreaction (|αR| << β).

FAILURE CONDITIONS:
  - If backreaction is negligible (test-field limit): no constraint is imposed.
    The Φ sector decouples from the Einstein equation and all parameters
    are free.
  - If the backreaction is important but the Einstein equation is not checked:
    the constraint exists in principle but is uncomputed.
```

---

## 2. Derivation / Impossibility Results

### Candidate A: Thermodynamic necessity

**Attempt:**

The KMS condition states that in thermal equilibrium, the CTP effective action is invariant under the KMS transformation:

```
φ_r(t) → φ_r(−t)
φ_a(t) → φ_a(−t) + iβ ∂_{−t} φ_r(−t)
```

where β = 1/(k_BT). This constrains the relationship between dissipation and noise (FDT). Does it also constrain the equilibrium value Φ*?

**Analysis:** The KMS condition constrains the FLUCTUATIONS around equilibrium, not the equilibrium VALUE itself. For a general force function F(φ, g):

- The fixed point is determined by F(Φ*, g) = 0.
- The KMS condition then requires D = k_BT × (−∂F/∂φ)|_{Φ*} × τ / 2 (the FDT relation for fluctuations around Φ*).
- The KMS condition does NOT determine what Φ* IS — only how the fluctuations around it relate to the dissipation.

**Key test:** Set F(φ, g) = c₀ + c₁ g_{00} − c₂ φ (an arbitrary force that depends on both φ and g). The fixed point is Φ* = (c₀ + c₁ g_{00})/c₂, which is a functional of g. But THIS WAS PUT IN BY HAND through the choice of F. The KMS condition does not force F to depend on g.

**Alternatively:** Set F(φ) = c₀ − c₂ φ (no g-dependence). The fixed point is Φ* = c₀/c₂, independent of geometry. The KMS condition is satisfied. No inconsistency.

**Result:** The KMS/FDT condition does NOT force Φ* to depend on geometry. The geometry-dependence of Φ* is determined by the choice of F, which the thermodynamic conditions leave unconstrained.

**Verdict: NOT DERIVABLE.** The thermodynamic necessity argument fails because KMS constrains fluctuations, not the equilibrium target.

**Missing assumption that would complete it:** A principle that forces F to depend on g — such as "Φ universally couples to all geometry" or "Φ is the response field of the metric." These are ADDITIONAL POSTULATES, not consequences of thermodynamic consistency.

### Candidate B: Admissibility-geometric tracking

**Attempt:**

If Φ must converge to a fixed point (assumption B-2), and Φ couples to g (B-4), then the fixed point equation is:

```
F(Φ*, ψ*, g) = 0
G(Φ*, ψ*, g) = 0
```

Solving these for Φ*, ψ* generically yields functions of g: Φ* = Φ*(g), ψ* = ψ*(g). These are geometry-determined.

**But:** This is trivially true for ANY system that (a) has a fixed point and (b) couples to g. It says nothing SPECIFIC about GRUT. Any member of the generic D1 class that couples to g and has a convergent fixed point will have Φ* = Φ*(g).

**The argument proves too much:** It applies to every coupled system, not specifically to the GRUT constitutive law. The "relaxation toward geometric equilibrium" is not a special GRUT feature — it is a GENERIC consequence of "has a fixed point + couples to geometry."

**Result:** The claim is TRUE but TRIVIAL. It does not elevate the GRUT meta-principle because it applies equally to every member of the generic D1 class.

**Verdict: TRIVIALLY TRUE, NOT DISCRIMINATING.** The meta-principle "Φ relaxes toward X(g)" is a consequence of "Φ has a stable fixed point and couples to g" — which is generic, not GRUT-specific.

### Candidate C: Cross-sector consistency (parameter constraint)

**Attempt:**

The semiclassical Einstein equation with Φ backreaction:

```
G_{μν}(g) = 8πG [T^{matter}_{μν} + T^{Φ}_{μν}]
```

At the Φ fixed point (Φ* = β + αR), the Φ stress-energy is:

```
T^{Φ}_{00} = ρ_Φ = −(Φ*)² / (2τ²) = −(β + αR)² / (2τ²)
```

(from GRUT-II Phase 4). Substituting into the trace of the Einstein equation:

```
R = −8πG(T^{matter} + T^{Φ}) / c⁴
R = −8πG T^{matter}/c⁴ − 8πG(−(β+αR)²/(2τ²))/c⁴
R = −8πG T^{matter}/c⁴ + 4πG(β+αR)²/(τ²c⁴)
```

This is a SELF-CONSISTENCY equation for R (R appears on both sides). Expanding to linear order in αR:

```
R = −8πG T^{matter}/c⁴ + 4πGβ²/(τ²c⁴) + 8πGαβR/(τ²c⁴) + O(α²R²)
```

Collecting R terms:

```
R [1 − 8πGαβ/(τ²c⁴)] = −8πG T^{matter}/c⁴ + 4πGβ²/(τ²c⁴)
```

This gives:

```
R_eff = [−8πG T^{matter}/c⁴ + 4πGβ²/(τ²c⁴)] / [1 − 8πGαβ/(τ²c⁴)]
```

**Does this constrain the parameters?** Only if we demand:

1. **No pole:** The denominator 1 − 8πGαβ/(τ²c⁴) ≠ 0. This gives: τ² ≠ 8πGαβ/c⁴. This is a CONSISTENCY BOUND, not a parameter relation.

2. **Perturbative control:** |8πGαβ/(τ²c⁴)| << 1. This gives: τ² >> 8πGαβ/c⁴. For β ~ 1, α ~ 1 m²: τ >> √(8πG/c⁴) ~ 10⁻²⁶ s. Satisfied trivially for any macroscopic τ.

3. **Effective cosmological constant:** The constant term 4πGβ²/(τ²c⁴) acts as an effective cosmological constant Λ_eff = 4πGβ²/(τ²c²). If we DEMAND that Λ_eff matches the observed cosmological constant Λ_obs ~ 10⁻⁵² m⁻²:

```
4πGβ²/(τ²c²) = Λ_obs
β²/τ² = Λ_obs c²/(4πG) ~ 10⁻⁵² × 9×10¹⁶ / (4π × 6.67×10⁻¹¹) ~ 10⁻²⁵ s⁻²
β/τ ~ 3 × 10⁻¹³ s⁻¹
```

This IS a relation between β and τ. But it requires the EXTERNAL INPUT of Λ_obs — it is not a self-consistency condition of the theory. It is a phenomenological matching condition.

**Result:** The semiclassical Einstein equation provides:
- One consistency bound (no pole): τ² ≠ 8πGαβ/c⁴ (trivially satisfied)
- One matching condition (Λ_eff = Λ_obs): relates β/τ to the observed cosmological constant
- No PARAMETER COLLAPSE from internal self-consistency alone

**Verdict: NOT DERIVABLE as internal necessity.** The only parameter relation comes from matching to external data (Λ_obs), not from self-consistency. The theory's parameters remain free.

---

## 3. Parameter-Collapse Pressure Test

### Dimensional analysis

| Quantity | Dimensions | Can it be related to fundamental constants? |
|----------|-----------|:-------------------------------------------:|
| τ | [time] | Only if related to 1/H₀, √(ℏG/c⁵), or another fundamental timescale. No derivation. |
| α | [Φ][length²] | Only if related to ℏ/c, G/c⁴, or Planck area. No derivation. |
| β | [Φ] | Dimensionless if Φ is dimensionless. No constraint. |
| D | [Φ²/time] | Fixed by FDT: D = k_BT τ/2. NOT independent if T and τ are given. |

**Result:** D is determined by T and τ (via FDT). This reduces the independent parameters from 5 (Book B: τ, D, T, α, β) to 4 (τ, T, α, β). But this was already known (E15/BA5). No new collapse.

### Thermodynamic constraints

FDT requires D > 0, which requires T > 0 and τ > 0. This is a positivity constraint, not a parameter relation. No collapse.

### Renormalization consistency

In the weak-field, overdamped regime, the theory is super-renormalizable (first-order in time, no loop divergences beyond the standard CTP one-loop). No renormalization group running is expected at tree level. No parameter relation from RG. No collapse.

### Einstein-sector coupling

The backreaction analysis (Candidate C above) gives one matching condition (β/τ from Λ_obs) but no internal collapse.

### Summary

| Test | Relations found | Internal or external? |
|------|:---------------:|:---------------------:|
| FDT | D = k_BT τ/2 | Internal (already known) |
| Positivity | T > 0, τ > 0 | Internal (constraint, not relation) |
| Λ_eff matching | β/τ ~ 3×10⁻¹³ s⁻¹ | **External** (requires Λ_obs input) |
| Dimensional | None | — |
| RG | None | — |

**Parameter-collapse verdict: NO internal collapse.** One external matching condition (β/τ from Λ_obs). Parameter count: 4 independent (τ, T, α, β), with D fixed by FDT and β/τ matchable to Λ_obs.

---

## 4. Cross-Sector Locking Test

### Test: does any relation emerge between the USL and the constitutive sector?

**USL structure:** Λ_USL = Gm²/(ℏl). Depends on: G, m, l. Does NOT depend on: τ, α, β, D, T, or any constitutive parameter.

**Constitutive structure:** τ dΦ/dt + Φ = β + αR. Depends on: τ, α, β, R. Does NOT depend on: G (except through R = −8πGT^m/c⁴), m, l, or ℏ.

**Intersection:** Both depend on G (the USL through Gm²; the constitutive sector through R which involves G via the Einstein equation). But this is a SHARED DEPENDENCE ON A FUNDAMENTAL CONSTANT, not a dynamical locking between sectors.

**Test: can varying τ change Λ_USL?** No. Λ_USL is determined by (G, m, l), none of which depend on τ.

**Test: can varying l change τ?** No. τ is an EFT parameter from the environmental bath, independent of superposition geometry.

**Test: does the Φ backreaction modify the Diosi integral?** In principle: yes, because T^{Φ}_{μν} contributes to the metric, which modifies the gravitational potential, which modifies the Diosi integral. In practice: T^{Φ} ~ β²/τ² ~ (3×10⁻¹³)² s⁻² ~ 10⁻²⁵ s⁻² is negligibly small compared to the matter stress-energy driving the gravitational potential. The Φ backreaction on the Diosi integral is suppressed by ~10⁻²⁵ relative to the matter contribution.

**Result: NO cross-sector locking.** The USL and constitutive sectors coexist in the same CTP action but do not constrain each other's parameters. They share the gravitational coupling constant G but this is a universal constant, not a dynamical lock. The Φ backreaction on the Diosi integral is negligible by ~25 orders of magnitude.

**Verdict: Coexistence without locking.** The Alpha-Prime separation (USL ≠ Level-1, different predictions for different observables) is not just a working assumption — it is a STRUCTURAL CONSEQUENCE of the parameter independence between the two sectors.

---

## 5. Final D2 Classification Memo

### Axis-by-axis classification

| Axis | Candidate | Result | Confidence | Evidence |
|------|-----------|:------:|:----------:|---------|
| **Thermodynamic necessity (A)** | KMS/FDT forces Φ* = X(g) | **meta_principle_still_ansatz** | 0.85 | KMS constrains fluctuations, not equilibrium target. F's dependence on g is a CHOICE, not a consequence of thermodynamics. |
| **Geometric tracking (B)** | Admissibility + coupling → Φ* = Φ*(g) | **Trivially true, not discriminating** | 0.90 | Any system with a fixed point and coupling to g has Φ* = Φ*(g). This is generic, not GRUT-specific. |
| **Cross-sector constraint (C)** | Backreaction gives parameter relation | **meta_principle_still_ansatz** | 0.80 | Only relation: β/τ from Λ_obs (external matching). No internal parameter collapse. No cross-sector locking. |

### Composite verdict

The meta-principle "Φ relaxes toward geometry-determined equilibrium" cannot be elevated from ansatz to necessity by any of the three tested routes:

1. Thermodynamics does not force Φ* to depend on geometry.
2. The "geometric tracking" property is trivially true for any coupled system with a fixed point — it does not distinguish GRUT from the generic class.
3. No internal parameter constraint emerges from self-consistency. The only parameter relation requires external input (Λ_obs).

**The meta-principle remains an ANSATZ.** It is a specific, physically motivated choice of functional form F = X(g) − Φ within the generic class. It is not derivable from deeper principles accessible within the current framework.

### What this means for GRUT

GRUT at the GRUT-III level is:
1. **A specific ansatz** within the class of two-field overdamped CTP EFTs on curved backgrounds.
2. **Distinguished by:** the choice F = X(g) − Φ (relaxation toward curvature-determined equilibrium), the Level-1 formula for τ(g), and the specific curvature coupling X = β + αR.
3. **These are all INPUT CHOICES**, not derived consequences.
4. **The USL is the primary unique-seeming prediction**, but it is a property of Newtonian gravity, not of the GRUT constitutive sector.
5. **The constitutive sector's uniqueness is entirely carried by the ansatz**, which is physically motivated but formally arbitrary.

---

## F. Gate Table

| Gate | Criterion | Status | Evidence |
|:----:|-----------|:------:|---------|
| **D2-G1** | A/B/C theorem candidates formally stated | **PASS** | Section 1: three candidates with assumptions, claim, scope, failure conditions. |
| **D2-G2** | Derivation or impossibility for each | **PASS** | Section 2: A — not derivable (KMS doesn't constrain equilibrium). B — trivially true, not discriminating. C — only external matching, no internal collapse. |
| **D2-G3** | Parameter-collapse attempt explicit | **PASS** | Section 3: five tests (dimensional, thermodynamic, RG, Einstein, FDT). One known relation (D from FDT). One external matching (β/τ from Λ_obs). No internal collapse. |
| **D2-G4** | USL↔constitutive locking tested | **PASS** | Section 4: no cross-sector locking. Φ backreaction on Diosi negligible by 25 orders. Alpha-Prime separation is structural, not accidental. |
| **D2-G5** | Classification not rhetorical | **PASS** | Section 5: three axes with specific verdicts backed by specific arguments. Composite: ansatz_persists. |

## Decision Token

### **ansatz_persists**

The meta-principle "constitutive relaxation toward geometric equilibrium" is not derivable from thermodynamic consistency, admissibility, or cross-sector self-consistency within the current framework. It remains an ANSATZ — a specific, physically motivated functional choice within the generic D1 class. The GRUT program's structural content beyond the generic class is carried entirely by this ansatz and the associated parameter choices (X = β + αR, Level-1 formula for τ). None is derived from deeper principles.

---

*GRUT III Book D Stage D2 complete. Decision: ansatz_persists. Thermodynamic necessity: fails (KMS doesn't constrain Φ*). Geometric tracking: trivially true, generic. Cross-sector locking: none (25-order suppression of Φ backreaction on Diosi). Parameter collapse: none internal (one external matching β/τ ~ Λ_obs). The meta-principle is an ANSATZ. GRUT is a specific parametrization of a generic EFT class, distinguished by its functional-form choices, not by derived structural constraints. Gates: 5/5 pass.*
