# APPENDIX E — STABILITY AND CONSISTENCY AUDIT OF THE GRUT ARCHITECTURE
## PASS 2: Four Deterministic Checks on the Three Root Failures

**Date:** 2026-03-27
**Follows:** APPENDIX_E_STABILITY_AUDIT_PASS1.md
**Status:** PASS 2 ONLY — four checks, no new physics, no broad simulation

---

## 1. EXECUTIVE PASS 2 DETERMINATION

> **`locally_consistent_globally_underdetermined` — CLASSIFICATION UNCHANGED**

The four checks do not justify an upgrade. They sharpen the picture without resolving it. One root failure is upgraded from "mismatch" to "structurally split formula" (Check 1). One is partially resolved at the endpoint specifically (Check 3). Two remain intact (Checks 2 and 4).

The most significant finding of PASS 2: the structural identity ω₀·τ = 1 is a property of the **local dynamical time** (τ_local = τ₀·t_dyn/(t_dyn+τ₀)), not of the **constitutive memory timescale** (τ_eff = τ₀/(1+(|V/R|·τ₀)²)). These differ by a factor of ω₀·τ₀ ~ 10^19 for astrophysical masses. The two τ formulas are structurally different prescriptions, not regime-translated versions of the same object.

The second significant finding: T_Q2 as identified in PASS 1 (ℏΩ/k_B from Drude cutoff) was a category error. The Drude bath temperature is an independent parameter in the FDT — Q2 does not constrain it. The temperature deficit from Q4 is unchanged.

---

## 2. DEFINITIONS OF THE FOUR CHECKS

### Check 1 — τ_eff self-consistency ratio per sector
**Tests:** Whether the frequency argument ω in τ_eff = τ₀/(1+(ωτ₀)²) refers to the same physical object across sectors, and whether using different ω substitutions constitutes a regime translation or a structural split.
**Relevant root failure:** Root failure 1 (τ_eff non-covariance).
**Criteria:**
- *Bounded consistency:* ω substitutions are all monotonically related to a single covariant quantity (e.g., a local expansion rate), and the substitution changes values but not meaning.
- *Tension:* ω substitutions refer to genuinely different physical quantities that are correlated but not equal.
- *Contradiction:* The same formula evaluated with different ω at the same physical point gives values that cannot both be correct.
- *Unresolved ambiguity:* The physical identification of ω in one or more sectors cannot be read off from the code.

### Check 2 — Q from three independent routes
**Tests:** Whether the three derivation paths for Q ~ 6 are genuinely independent, or share hidden assumptions that make the agreement trivial.
**Relevant root failure:** Root failure 1 (implicit — Q depends on τ_eff) and Root failure 3 (Q used to define temperature candidate).
**Criteria:**
- *Triangulated:* Three routes use distinct physical inputs and agree → real constraint.
- *Consistent but assumption-loaded:* Routes share one or more hidden assumptions but still provide partial corroboration.
- *Numerically aligned but not independent:* All routes reduce to the same formula under the same assumptions.
- *Incoherent:* Routes disagree.

### Check 3 — Φ boundary condition at endpoint
**Tests:** Whether the collapse barrier order parameter and the constitutive scalar field can be consistently related at the equilibrium endpoint R = R_eq.
**Relevant root failure:** Root failure 2 (Φ dual-use).
**Criteria:**
- *Viable:* The two Φ objects are formally consistent at the endpoint (same value or provably related by a defined mapping).
- *Tensioned:* They are consistent at the endpoint but diverge off-equilibrium in a way that undermines the identification.
- *Notational only:* The shared symbol is pure notation — no physical identification claimed or needed.
- *Structural conflict:* The two objects cannot be consistently related even at the endpoint.
- *Underdetermined:* The source term for the constitutive ODE is unknown, preventing numerical comparison.

### Check 4 — T_Q2 extraction and comparison to thermodynamic candidates
**Tests:** Whether the Drude bath cutoff from Q2 (Ω = 1/τ₀) implies a temperature that narrows the Appendix D temperature underdetermination.
**Relevant root failure:** Root failure 3 (temperature underdetermination).
**Criteria:**
- *Supports one candidate:* T_Q2 matches one Appendix D candidate within a factor of 2.
- *Narrows but does not resolve:* T_Q2 excludes some candidates but does not uniquely select one.
- *Non-informative:* T_Q2 does not constrain the Appendix D candidates.
- *Conflicts:* T_Q2 is inconsistent with all Appendix D candidates.

---

## 3. CHECK 1 RESULT: τ_eff SELF-CONSISTENCY RATIO PER SECTOR

### Sector inventory

**Cosmological sector** (engine.py, operators.py):
```
τ_eff = τ₀ / (1 + (H · τ₀)²)
ω = H (Hubble rate, s⁻¹)
```
Physical meaning of ω: local expansion rate of the universe. A global isotropic frequency.

**Collapse sector** (collapse.py):
```
τ_eff = τ₀ / (1 + (|V/R| · τ₀)²)
ω = |V/R| (velocity-over-radius ratio, s⁻¹)
```
Physical meaning of ω: instantaneous fractional contraction rate of the collapsing shell. A dynamical frequency local to the shell. Note: this is dimensionally equivalent to H, but physically distinct — H is a background field, |V/R| is a mechanical state variable.

**Interior PDE sector** (interior_pde.py, interior_waves.py):
```
τ_local = τ₀ · t_dyn / (t_dyn + τ₀)     [tier-0 closure, evaluated at V=0]
t_dyn = sqrt(R_eq³ / (2GM))
```
Physical meaning: τ_local is NOT τ_eff evaluated at ω = ω₀. It is a different formula — the harmonic mean of τ₀ and the local dynamical time t_dyn. This is the "tier-0 local closure," not a substitution into the dynamic formula.

### Critical structural split

The interior PDE does NOT use τ_eff = τ₀/(1+(ωτ₀)²) at ω = ω₀. It uses a distinct formula:

```
τ_local = τ₀ · t_dyn / (t_dyn + τ₀)
```

For astrophysical masses where t_dyn ≪ τ₀:
```
τ_local ≈ t_dyn
```

This is the local gravitational dynamical timescale, not the frequency-filtered constitutive relaxation time.

### Self-consistency ratios at equilibrium (reference: 30 M_sun BH)

Reference quantities:
- τ₀ = 1.3225 × 10¹⁵ s
- M = 30 × 1.989 × 10³⁰ = 5.967 × 10³¹ kg
- r_s = 8.849 × 10⁴ m
- R_eq = r_s/3 = 2.950 × 10⁴ m
- t_dyn = sqrt(R_eq³/(2GM)) = sqrt((2.950×10⁴)³/(2 × 6.674×10⁻¹¹ × 5.967×10³¹)) = 5.68 × 10⁻⁵ s
- ω₀ = sqrt(β_Q · GM/R_eq³) = sqrt(2 · 1.549×10⁸) = 1.760 × 10⁴ rad/s

**At equilibrium (V=0):**

| Sector | Formula | τ value | Physical regime |
|--------|---------|---------|----------------|
| Collapse (V=0) | τ₀/(1+0²) = τ₀ | 1.32 × 10¹⁵ s | Cosmic timescale |
| Interior PDE | τ₀·t_dyn/(t_dyn+τ₀) ≈ t_dyn | 5.68 × 10⁻⁵ s | Dynamical timescale |
| Ratio | τ_collapse/τ_PDE | **2.33 × 10¹⁹** | — |

The ratio is ω₀ · τ₀ = (1.760 × 10⁴) × (1.3225 × 10¹⁵) = 2.33 × 10¹⁹.

### Interpretation

The structural identity ω₀ · τ_local = 1 holds exactly by the tier-0 closure (since τ_local ≈ t_dyn ≈ 1/ω₀ for astrophysical masses). But it is a GRAVITATIONAL SCALING IDENTITY — it encodes that the BDCC oscillation frequency equals the inverse dynamical time. It is NOT a property of the constitutive memory relaxation time τ_eff evaluated at the mode frequency.

If one substituted ω = ω₀ into the dynamic formula:
```
τ_eff(ω₀) = τ₀ / (1 + (ω₀ · τ₀)²) ≈ τ₀ / (ω₀ · τ₀)² = 1/(ω₀² · τ₀)
           ≈ 1 / ((1.760×10⁴)² × 1.3225×10¹⁵) = 2.44 × 10⁻²⁴ s
```

This is 19 orders of magnitude below even τ_local. The dynamic formula at ω = ω₀ gives a τ that is unphysical for interior mode analysis.

The two formulas serve different purposes:
- τ_eff = τ₀/(1+(ωτ₀)²): memory relaxation time during DYNAMIC EVOLUTION (V ≠ 0, H ≠ 0)
- τ_local = τ₀·t_dyn/(t_dyn+τ₀): local equilibrium timescale for LINEARIZED MODE ANALYSIS at V=0

At equilibrium (V=0), the two prescriptions diverge by ~10^19. This is not a regime translation. The two formulas are structurally different closures applied in structurally different contexts.

### What this means for the Q2 resonance condition

Q2 identifies the Drude bath cutoff Ω = 1/τ₀. The resonance condition stated in Q2 is:
```
ω₀ · τ_eff = 1   ↔   ω₀ = Ω
```

This would require τ_eff = τ_local ≈ 1/ω₀, NOT τ_eff = τ₀.

So Q2's resonance condition is satisfied by the INTERIOR PDE's τ_local, not by the constitutive τ_eff from the dynamic formula. The claimed resonance between the system frequency and the bath cutoff is:
```
ω₀ = Ω   means   ω₀ = 1/τ₀
```
But ω₀ = 1.760 × 10⁴ rad/s while 1/τ₀ = 7.56 × 10⁻¹⁶ rad/s. These differ by 10^19.

The resonance condition holds between ω₀ and 1/t_dyn (local scale), not between ω₀ and 1/τ₀ (cosmological scale). The Q2 Drude cutoff Ω = 1/τ₀ is a COSMOLOGICAL scale, not an astrophysical one. The resonance claim imports the interior PDE's τ_local into a formula where the cutoff is τ₀ — a silent equivocation.

### Check 1 classification

> **`tau_eff_tensioned_across_sectors`**

Not `tau_eff_structurally_contradictory` because the two τ formulas are explicitly used in different contexts (dynamic vs. equilibrium) and the interior PDE documents the tier-0 closure as a distinct prescription. They are not claimed to be the same object in the same context.

But the tension is real and substantial: the structural identity ω₀·τ = 1 is a gravitational scaling relation using τ_local, not a statement about the constitutive τ_eff. The Q2 resonance claim conflates the two. Any cross-sector argument that imports ω₀·τ = 1 as a property of the constitutive law (rather than the gravitational structure) is using a misidentified τ.

The self-consistency ratio at equilibrium is ~10^19. This is not a translation; it is a structural split between dynamical and equilibrium closures.

---

## 4. CHECK 2 RESULT: Q FROM THREE INDEPENDENT ROUTES

### Route A — Formula route (canon)
```
Q = β_Q / α_vac = 2 / (1/3) = 6
```
Derivation status: algebraic identity from two canonical parameters.
Assumptions: β_Q = 2 (assumed, not derived), α_vac = 1/3 (locked).

### Route B — Interior PDE damping route (interior_pde.py)
```
γ_PDE = α_vac · ω_g² · τ_eff / (1 + (ω_PDE · τ_eff)²)
evaluated at ω_PDE = ω₀ with ω₀·τ_local = 1:
γ_PDE = α_vac · (ω₀²/β_Q) · τ_local / 2

Q_PDE = ω_eff / (2 · γ_PDE) ≈ ω₀ / (2 · γ_PDE)
      = ω₀ / (α_vac · ω₀² · τ_local / β_Q)
      = β_Q · τ_local · ω₀⁻¹ / α_vac ... wait
      = β_Q / (α_vac · ω₀ · τ_local)
      = β_Q / (α_vac · 1)             [using ω₀·τ_local = 1]
      = β_Q / α_vac = 6
```
Result: identical to Route A.
Derivation status: derived from PDE damping formula, but reduces to Route A algebraically.
Hidden shared assumption: ω₀·τ_local = 1 (the structural identity, itself a gravitational scaling relation).

### Route C — Interior waves damping route (interior_waves.py)
```
γ_mem = α_vac · ω₀² · τ_local / (2 · (1 + (ω₀ · τ_local)²))
      = α_vac · ω₀² · τ_local / 4     [using ω₀·τ_local = 1]

Q_waves = ω₀ / (2 · γ_mem)
        = ω₀ / (α_vac · ω₀² · τ_local / 2)
        = 2 / (α_vac · ω₀ · τ_local)
        = 2 / α_vac                   [using ω₀·τ_local = 1]
        = 6
```
Result: identical to Routes A and B.
Hidden shared assumption: ω₀·τ_local = 1.

Note: Route C gives Q = 2/α_vac, while Route B gives Q = β_Q/α_vac. These agree only because β_Q = 2. If β_Q were not 2, Routes B and C would disagree. The check reveals that β_Q = 2 is doing triple duty: it appears in the formula, in the PDE damping, and in the waves damping (through the ω_g²/β_Q factor).

### Independence assessment

All three routes reduce to Q = (structural factor)/α_vac, where the structural factor equals β_Q after applying ω₀·τ = 1. The routes share:
- α_vac = 1/3 (locked constant, same in all three)
- β_Q = 2 (assumed parameter, same in all three)
- ω₀·τ = 1 (structural identity, same in all three, itself a gravitational scaling relation not derived from the constitutive law)

Routes B and C also share the interior PDE formalism. The "three routes" are three algebraic paths through the same parameter set, not three physically independent measurements.

### W4 test: does β_Q = 2 silently dominate?

Yes. If β_Q ≠ 2:
- Route A: Q = β_Q/α_vac → shifts linearly
- Route B: Q = β_Q/α_vac → shifts linearly (same formula)
- Route C: Q = 2/α_vac → DOES NOT SHIFT (Route C is independent of β_Q)

This means Routes A and B are identical (degenerate), while Route C is actually independent of β_Q. The three routes reduce to TWO: {A=B, which depend on β_Q} and {C, which does not}. The "agreement" between all three at β_Q = 2 is therefore a consequence of choosing β_Q = 2 specifically. At β_Q ≠ 2, Routes A and B would give Q ≠ 6 while Route C would still give Q = 6 (= 2/α_vac).

This is the most important finding of Check 2: Routes A and B are degenerate, and their agreement with Route C at Q = 6 is a specific consequence of β_Q = 2. The Q = 6 result is not triangulated — it is a single-parameter consequence of α_vac = 1/3 at β_Q = 2.

The claimed "Q ~ 6–7.5 range" would arise from β_Q ∈ [2, 2.5] via Routes A and B, but Route C always gives Q = 2/α_vac = 6.0 regardless. So Route C provides a β_Q-independent anchor at Q = 6, while Routes A and B are β_Q-dependent.

### Check 2 classification

> **`q_numerically_aligned_but_not_independent`**

Routes A and B are algebraically identical. All three share ω₀·τ = 1 as a hidden assumption. Route C is β_Q-independent and provides a partial anchor, but it still shares α_vac = 1/3 and the structural identity. The agreement at Q = 6 is consistent with internal self-consistency, not with cross-sector independence. The W4 risk is confirmed: β_Q = 2 is silently assumed in Routes A and B, and their alignment with Route C at β_Q = 2 is a verification of the assumed value, not an independent check.

---

## 5. CHECK 3 RESULT: Φ BOUNDARY CONDITION AT ENDPOINT

### Identifying the two Φ objects from code

**Φ_barrier (collapse sector):**
The collapse module (collapse.py) does not define an explicit Φ variable. The barrier physics enters as the quantum pressure acceleration:
```
a_Q = (GM/R²) · ε_Q · (r_s/R)^β_Q
```
The barrier "order parameter" derived from this is:
```
Φ_barrier(R) = a_Q / a_grav = ε_Q · (r_s/R)^β_Q = (1/9) · (r_s/R)²
```
At equilibrium (R = R_eq = r_s/3):
```
Φ_barrier(R_eq) = (1/9) · (r_s/(r_s/3))² = (1/9) · 9 = 1
```

**Φ_constitutive (constitutive memory field):**
The constitutive ODE governs M_drive:
```
τ_eff · dM_drive/dt + M_drive = a_grav = GM/R²
```
The normalized memory saturation is:
```
Φ_constitutive(t) = M_drive(t) / a_grav_current
```
At equilibrium (M_drive → a_grav, V=0):
```
Φ_constitutive(R_eq) = M_drive/a_grav = 1
```

### Endpoint comparison

At R = R_eq:
- Φ_barrier = 1 (full barrier engagement)
- Φ_constitutive = 1 (full memory saturation)

They agree: both equal 1 at the endpoint. This is a formal consistency.

### Why agreement at the endpoint does not establish identity

The agreement Φ_barrier = Φ_constitutive = 1 at R_eq is not an independent verification — it is how R_eq is defined. The endpoint law R_eq/r_s = 1/3 was derived from the condition that a_Q = a_inward at equilibrium, which is exactly the condition Φ_barrier = 1. The memory saturation M_drive = a_grav at equilibrium is the steady-state of the constitutive ODE. So both equal 1 at R_eq by construction of R_eq, not by independent tracking of the same physical field.

**Off-equilibrium behavior:**

Φ_barrier(R) = ε_Q·(r_s/R)² — a function of R only; no memory, no time dependence.

Φ_constitutive(t) = M_drive(t)/a_grav(t) — a history-dependent ODE solution; tracks with a lag determined by τ_eff; depends on the collapse trajectory, not just the current R.

During collapse toward R_eq:
- Φ_barrier activates continuously as R decreases (grows as R^{-2})
- Φ_constitutive lags behind a_grav by the memory timescale; at early times M_drive ≈ a_grav (slow collapse), at late times M_drive may be displaced from a_grav (rapid collapse)

The two objects track R differently and have genuinely different functional forms. Their equality at R_eq is a consequence of the endpoint law, not of being the same field.

### What the action principle adds

In the action principle (barrier_action_sector.py, S_macro[Φ,g]), Φ is a scalar field governed by an Euler-Lagrange equation. The zero-spatial-gradient limit of this field equation should recover the constitutive ODE. The value of Φ at R_eq is then the steady-state of the field equation, which — in the zero-gradient limit — equals X_endpoint (the covariant source at the endpoint). Since X is not explicitly computed (described as "schematic/effective"), this comparison is incomplete.

However, the constitutive ODE steady-state gives Φ = a_grav/a_grav = 1 (in the M_drive/a_grav normalization). The field-theoretic Φ in S_macro has a different normalization that is not documented in the current architecture. Without the explicit covariant source term, the comparison at the action-principle level is **underdetermined**.

### Check 3 classification

> **`phi_endpoint_relation_viable`** (endpoint only)
> Off-equilibrium: **`phi_relation_underdetermined`**

At the endpoint specifically, the two Φ objects are formally consistent (both equal 1 in normalized units), but this consistency is a consequence of the endpoint law derivation, not of tracking the same physical field. Off-equilibrium, they are genuinely different objects: one is an instantaneous function of R, the other is a history-dependent ODE solution. The dual-use is **structural, not merely notational**: the two Φ's encode different physics at the same point in configuration space. Their equality at R_eq is a calibration point, not a physical identification.

The action-principle Φ comparison remains underdetermined because the covariant source term is not explicit.

---

## 6. CHECK 4 RESULT: T_Q2 EXTRACTION VS THERMODYNAMIC CANDIDATES

### Correcting the PASS 1 gap identification

PASS 1 identified T_Q2 = ℏΩ/k_B = ℏ/(k_B·τ₀) as the "bath-implied temperature." This is a category error. In the Drude bath model:
```
J(ω) = η · ω · Ω² / (ω² + Ω²),   Ω = 1/τ₀
```
The temperature T is an **independent parameter** that enters through the FDT separately:
```
S(ω) = 2k_BT · Im[χ(ω)] / ℏω   (quantum FDT)
S(ω) ≈ 2k_BT · Im[χ(ω)] / ω    (classical limit, ℏω ≪ k_BT)
```
The quantity ℏΩ/k_B = ℏ/(k_B·τ₀) is the energy of a bath photon at the cutoff frequency — it is NOT the bath temperature. In standard quantum Brownian motion, the bath has temperature T (an independent thermodynamic parameter), and the cutoff Ω specifies the spectral shape. Setting T = ℏΩ/k_B would be the condition that the bath is at its own "cutoff temperature," which is not a general result and is not implied by the Drude structural match.

Numerically:
```
T_Q2(wrong) = ℏ/(k_B · τ₀) = (1.055×10⁻³⁴) / (1.381×10⁻²³ × 1.3225×10¹⁵)
             ≈ 5.78 × 10⁻²⁷ K
```
This is 18–28 orders of magnitude below all four thermodynamic candidates.

### Correct statement of what Q2 provides

Q2 identifies:
1. **Bath spectral shape:** Drude/Lorentzian — J(ω) ∝ ω·Ω²/(ω²+Ω²)
2. **Bath cutoff scale:** Ω = 1/τ₀ (cosmological timescale)
3. **Noise kernel shape:** K_noise(t) ∝ exp(−t/τ₀) (exponential, determined up to amplitude)
4. **FDT constraint form:** S(ω) ∝ T · Im[χ(ω)] — structure known, amplitude requires T

What Q2 does NOT identify: the value of T. Temperature enters the FDT as a multiplicative constant and remains a free parameter even after the bath spectral shape is specified.

### The resonance condition revisited

Q2 states: "At equilibrium, ω₀·τ_eff = 1. This is the condition that the system frequency matches the bath cutoff: ω₀ = Ω = 1/τ₀."

From Check 1: ω₀ ≈ 1.76 × 10⁴ rad/s while Ω = 1/τ₀ ≈ 7.56 × 10⁻¹⁶ rad/s. These differ by 10^19. The resonance condition ω₀ = Ω is **not satisfied numerically** — it holds symbolically because ω₀·τ_local = 1 and τ_local ≈ t_dyn ≠ τ₀.

The Q2 resonance condition conflates τ_local (PDE equilibrium timescale) with τ₀ (cosmological memory timescale). The structural identity ω₀·τ = 1 uses τ = τ_local, not τ₀. The bath cutoff Ω = 1/τ₀ is 10^19 times smaller than the system frequency ω₀. The system is NOT at the bath cutoff resonance — it is 10^19 times above the bath cutoff.

### Comparison to the four Appendix D temperature candidates (at 30 M_sun)

The code defines 4 candidates (not 6 as stated in PASS 1 — the PASS 1 count was an overestimate):

| Candidate | Formula | Value (30 M_sun) | GRUT-native? |
|-----------|---------|-----------------|-------------|
| T_surface_gravity | ℏ·ω₀²·R_eq/(2π·k_B) | ~11 K | No (analog) |
| T_dissipation | ℏ·ω₀/(Q·k_B) | ~2.24 × 10⁻⁸ K | Yes |
| T_structural | ℏ·ω₀/k_B | ~1.34 × 10⁻⁷ K | Yes |
| T_hawking | ℏ·c³/(8π·G·M·k_B) | ~2.06 × 10⁻⁹ K | No (imported) |

The two GRUT-native candidates (T_dissipation and T_structural) differ by a factor of Q ~ 6. They converge within one order of magnitude (the code's convergence criterion), so the code classifies them as "converged but ambiguous."

Q2 provides no additional constraint on which of these is correct, because T is a free parameter in the FDT relation regardless of the bath spectral shape. The bath shape specifies the noise correlation structure; the temperature specifies the overall noise amplitude.

### Check 4 classification

> **`q2_temperature_noninformative`**

The Drude bath identification in Q2 specifies the bath spectral shape and the cutoff Ω = 1/τ₀. It does not constrain the bath temperature T, which enters the FDT as an independent multiplicative constant. The "T_Q2" extraction proposed in PASS 1 was a category error (confusing cutoff energy ℏΩ with bath temperature k_BT). The four Appendix D candidates remain equally plausible after Check 4. The Q4 temperature deficit is unchanged.

Additionally, the Q2 resonance condition (ω₀ = Ω) is numerically false for astrophysical masses: ω₀ ~ 10^4 rad/s while Ω = 1/τ₀ ~ 10⁻¹⁵ rad/s, differing by ~10^19. The resonance holds only between ω₀ and 1/τ_local (≠ 1/τ₀).

---

## 7. INTEGRATED PASS 2 ASSESSMENT

### Which root failure was most reduced?

**Root failure 2 (Φ dual-use):** Most reduced. Check 3 establishes that at the equilibrium endpoint, the two Φ objects are formally consistent (both = 1 in normalized units). This provides a narrow positive result: the endpoint calibration is viable. The tension is recharacterized: not "same symbol hides a contradiction" but "same symbol hides genuinely different off-equilibrium physics, consistent only at the endpoint by construction." This is a real resolution at the endpoint, a real tension off-equilibrium.

### Which root failure remains the strongest blocker?

**Root failure 1 (τ_eff non-covariance):** Sharpest blocker. Check 1 reveals that the structural identity ω₀·τ = 1 uses τ_local (gravitational scaling relation, τ_local ≈ t_dyn), while the constitutive law uses τ_eff = τ₀/(1+(|V/R|·τ₀)²). At equilibrium (V=0), τ_eff = τ₀ while τ_local = t_dyn — differing by ω₀·τ₀ ~ 10^19. The Q2 resonance condition (ω₀ = Ω = 1/τ₀) is numerically false by this same factor. The structural identity is a gravitational scaling property, not a constitutive law property.

This means: any cross-sector argument that imports ω₀·τ = 1 as a constitutive law property is using the wrong τ. The constitutive law at equilibrium gives τ_eff = τ₀ (cosmic scale), not τ_local = t_dyn (astrophysical scale).

**Root failure 3 (temperature underdetermination):** Unchanged by PASS 2. Check 4 reveals that T_Q2 was a category error. The temperature remains underdetermined; Q4 remains open; FDT remains conditional.

### Should the Appendix E classification change?

**No. Classification remains `locally_consistent_globally_underdetermined`.**

The checks do not reveal an internal contradiction within any sector. Each sector is self-consistent using its own τ, its own Φ, and its own temperature candidate. But:
- The cross-sector τ tension is real and quantified (~10^19 factor at equilibrium)
- Q is not independently triangulated (all routes share the same assumptions)
- Temperature remains underdetermined (Q4 gap unchanged, T_Q2 was a category error)
- Φ is consistent at the endpoint but genuinely different off-equilibrium

The upgrade to `coherent_but_tensioned` is not warranted because the τ-split at equilibrium is not a "tension" — it is a structural difference between two distinct physical regimes being modeled by formulas from different derivational contexts. That is harder to resolve than a tension.

The downgrade to `inconsistency_visible` is not warranted because no sector-internal inconsistency is found. The two τ formulas are used in different contexts where each is appropriate, and the mismatch is explicit in the code (interior_pde.py documents "tier-0 local tau" as distinct from the dynamic formula).

---

## 8. CODE-WORTHINESS DECISION

**Yes, a narrow deterministic audit module is warranted.**

The four checks are fully deterministic:
- Check 1 computes τ ratios at equilibrium from canonical parameters
- Check 2 computes Q from three routes and tests their algebraic independence
- Check 3 computes Φ values at R_eq from the endpoint law
- Check 4 computes T_Q2 and notes the category error, then compares the four candidates numerically

None of these require simulation. All produce specific numerical verdicts with explicit classification strings.

**Files to create:**
- `grut/stability_consistency_audit.py`
- `tests/test_stability_consistency_audit.py`

**Files created:** (see Section 9)

---

## 9. CODE SUMMARY

### Files created

- `grut/stability_consistency_audit.py`
- `tests/test_stability_consistency_audit.py`

### Exact purpose

`stability_consistency_audit.py` implements the four Pass 2 checks as deterministic functions that:
- Use only published canonical parameters (τ₀, α_vac, β_Q, ε_Q)
- Compute τ ratios, Q routes, Φ values, and temperature scales at a reference mass
- Return structured dicts with classification strings, numerical values, and explicit assumption lists
- Include a `run_pass2_audit()` entry point that returns all four check results

`test_stability_consistency_audit.py` verifies that:
- Check 1 produces the correct τ ratio (~10^19 for 30 M_sun)
- Check 1 classifies as `tau_eff_tensioned_across_sectors`
- Check 2 shows Routes A and B are algebraically degenerate
- Check 2 classifies as `q_numerically_aligned_but_not_independent`
- Check 3 shows Φ_barrier = Φ_constitutive = 1 at R_eq
- Check 3 classifies as `phi_endpoint_relation_viable`
- Check 4 identifies T_Q2 as a category error
- Check 4 classifies as `q2_temperature_noninformative`
- No test asserts "fully_consistent" or equivalent unsupported claim
- The forbidden-claim guard is functional

### Assumptions exposed by the module

1. τ_local = τ₀·t_dyn/(t_dyn+τ₀) is the correct interior PDE τ (from interior_pde.py)
2. τ_eff = τ₀/(1+(|V/R|·τ₀)²) is the correct collapse/cosmology τ (from collapse.py, Q2)
3. At equilibrium: V=0, M_drive = a_grav, R = R_eq = r_s/3
4. ω₀ = sqrt(β_Q · GM/R_eq³) at R_eq (from interior_pde.py)
5. Q routes: Route A = β_Q/α_vac, Route B = β_Q/(α_vac·ω₀·τ_local), Route C = 2/(α_vac·ω₀·τ_local)
6. Φ_barrier = ε_Q·(r_s/R_eq)^β_Q (from collapse.py force decomposition)
7. Φ_constitutive at equilibrium = 1 (steady-state of τ dM/dt + M = a_grav)
8. Four temperature candidates from thermodynamic_sector.py: T_surface_gravity, T_dissipation, T_structural, T_hawking
9. T_Q2 = ℏ·Ω/k_B where Ω = 1/τ₀ is NOT a bath temperature (explicitly flagged as category error)

### What the module does NOT claim

- It does NOT claim the τ tension is resolved
- It does NOT claim Q is independently triangulated
- It does NOT claim Φ duality is resolved (only that the endpoint is consistent)
- It does NOT claim temperature is determined
- It does NOT upgrade the Appendix E classification from `locally_consistent_globally_underdetermined`
- It does NOT assess any claim not directly in the four checks
- It does NOT run any simulation or solve any ODE

### Test summary

8 tests in `test_stability_consistency_audit.py`:
1. `test_check1_tau_ratio_at_reference_mass` — τ ratio ~10^19 at 30 M_sun
2. `test_check1_classification` — `tau_eff_tensioned_across_sectors`
3. `test_check2_routes_degenerate` — Routes A and B algebraically identical
4. `test_check2_classification` — `q_numerically_aligned_but_not_independent`
5. `test_check3_phi_at_endpoint` — Φ_barrier = Φ_constitutive = 1.0
6. `test_check3_classification` — `phi_endpoint_relation_viable`
7. `test_check4_t_q2_is_category_error` — T_Q2 not a bath temperature, 18+ OOM below all candidates
8. `test_check4_classification` — `q2_temperature_noninformative`
Plus 1 guard test: `test_no_full_consistency_claim` — asserts the overall verdict is NOT `appears_coherent_in_claimed_regimes`.

---

## 10. DOCUMENT-BUILDING CONSTRAINTS FOR LATER USE

### Claims a future Appendix E document MAY safely make (after Pass 2)

1. The structural identity ω₀·τ = 1 is a gravitational scaling relation (ω₀ ~ 1/t_dyn) using the interior PDE's tier-0 local τ. It is NOT a property of the constitutive memory relaxation time τ_eff = τ₀/(1+(|V/R|·τ₀)²).

2. At equilibrium, the constitutive τ_eff = τ₀ (cosmic scale) while the interior PDE τ_local ≈ t_dyn (astrophysical scale). These differ by a factor ω₀·τ₀ ~ 10^19 for a 30 M_sun BH. This is a structural split between dynamical and equilibrium closures, not a regime translation.

3. Q = 6 is derivable from three routes, but all three routes share the assumptions α_vac = 1/3, β_Q = 2, and ω₀·τ = 1. Routes A and B are algebraically degenerate. Route C is β_Q-independent but not otherwise independent.

4. At the equilibrium endpoint R_eq, the barrier order parameter Φ_barrier = 1 and the memory saturation Φ_constitutive = 1. This endpoint consistency is a consequence of the endpoint law derivation, not independent tracking.

5. The Drude bath cutoff Ω = 1/τ₀ identified in Q2 specifies the bath spectral shape; temperature T enters the FDT as an independent free parameter and is not constrained by the bath cutoff alone.

6. The four thermodynamic temperature candidates span from ~10⁻⁹ K (Hawking) to ~11 K (surface gravity analog) at 30 M_sun. The two GRUT-native candidates differ by a factor of Q ~ 6. Temperature remains underdetermined after Pass 2.

7. The Q2 resonance condition "ω₀ = Ω = 1/τ₀" is numerically false for astrophysical masses (ω₀ ~ 10^4 rad/s, 1/τ₀ ~ 10⁻¹⁵ rad/s). The resonance holds between ω₀ and 1/τ_local (≠ 1/τ₀).

### Claims a future Appendix E document MUST NOT make

1. That the structural identity ω₀·τ = 1 validates the constitutive memory timescale τ₀ in the interior mode sector. It validates τ_local = t_dyn, not τ₀.

2. That the Q2 bath cutoff Ω = 1/τ₀ is in resonance with the BDCC oscillation frequency ω₀. These differ by ~10^19.

3. That Q ~ 6 is independently triangulated. All routes share the same hidden assumptions.

4. That Φ in collapse and Φ in the constitutive law are the same physical field. They are consistent at the endpoint by construction but genuinely different off-equilibrium.

5. That T_Q2 = ℏ/(k_B·τ₀) is the bath temperature. This conflates the cutoff energy with the thermodynamic temperature.

6. That Pass 2 resolves any of the three root failures. It sharpens them. Temperature remains underdetermined; τ tension is quantified but not resolved; Φ endpoint is consistent but field identity is not established.

7. That β_Q = 2 is confirmed by the Q routes. All routes assume β_Q = 2; the routes do not independently verify it.

### Strongest defensible classification for Appendix E after Pass 2

> **`locally_consistent_globally_underdetermined`** — unchanged from Pass 1.

Pass 2 sharpens the picture: the τ split is quantified at ~10^19, Q non-independence is algebraically demonstrated, Φ endpoint consistency is established (viable but not identity), and T_Q2 is identified as a category error. None of these results justify a classification upgrade. The architecture is internally consistent within each sector; cross-sector connections remain carried by structural assumption rather than derivation.
