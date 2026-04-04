# Program W0 — Deep Derivation of the Carrier Barrier

## Formal Bridge-Debt Reduction Audit (Parallel Side-Program)

**Type:** Bridge-debt reduction audit — NOT a mainline Book stage
**Predecessor:** Book VII Terminal Capstone (carrier provisionally committed; ΔG ≥ 28 kT unproven)
**Function:** Determine whether the Book VII carrier barrier can be supported or derived from existing lower-stack geometry
**Entry cost:** 15/9/1/6 (unchanged by W0 unless debt status changes)

---

## 1. Executive Verdict

**Global verdict: (B) — The carrier barrier is materially supported by lower-stack structure, reducing but not erasing debt.**

**Outcome class: B — barrier_partially_supported_but_not_forced.**

The existing lower-stack architecture — specifically the SU(2) gauge bridge, the K=2 composite bound-state spectrum, the hard-core boundary, and the quantum transition selection rules — provides genuine structural support for a carrier barrier in the robust M4 regime. The support operates through two independent mechanisms:

**Mechanism 1 — Selection-rule metastability:** The K=2 composite supports a discrete hydrogenic bound-state spectrum (Book IV Beta). The first excited shell (N=2) contains a state at (N=2, ℓ=0, S=0) that is protected against single-gauge-boson decay by the dipole selection rule (Δℓ = ±1 forbids ℓ=0 → ℓ=0 transitions). This creates a quantum-mechanically metastable "loaded" state with excitation energy ΔE₁₂ = (3/16)α_g²M_sk, where α_g = g²/(2π) is the gauge coupling and M_sk is the soliton mass. The metastability is generic — it follows from angular momentum conservation and does not require fine-tuning.

**Mechanism 2 — Scale domination:** The excitation energy ΔE₁₂ generically exceeds 28 kT whenever the dimensionless product α_g² × (M_sk/kT) ≥ 149. This condition is satisfied for any scaffold where solitons are thermally stable (M_sk ≫ kT, required independently for the scaffold to function) and gauge coupling is moderate (α_g ≳ 0.2). The robust regime (ΔG ≥ 28 kT) is therefore the **generic expectation**, not a fine-tuned special case.

**Why this reduces debt but does not erase it:**

1. **Two free parameters remain:** α_g and M_sk/kT are not fixed by the lower-stack architecture. The inequality α_g²(M_sk/kT) ≥ 149 constrains but does not determine the barrier.

2. **Mechanism mismatch:** Book VII described the barrier as a classical conformational barrier with Arrhenius kinetics (k_leak = ν₀ exp(−ΔG/kT)). The lower-stack support provides quantum selection-rule metastability, which is structurally stronger but mechanistically different. The connection between the two pictures is not yet formalized.

3. **Decay kinetics not calculated:** The two-gauge-boson decay rate of the (N=2, ℓ=0) state, which sets the actual carrier lifetime, depends on higher-order matrix elements that have not been computed within the scaffold formalism.

4. **Non-hydrogenic corrections unassessed:** Hard-core level shifts, short-range corrections (V_short), and dissipation-background effects on the metastable state are not evaluated.

**What the debt reduction buys:**

- The carrier barrier is no longer a free-floating matched parameter. It is connected to the binding energy of the K=2 composite through a derivable inequality.
- The robust regime is the generic expectation for scaffolds with thermally stable solitons and moderate gauge coupling.
- A specific physical mechanism (selection-rule protection) is identified for the metastability, replacing the ad hoc conformational-switch assumption.
- The carrier bridge debt is partially retired — the parameter ΔG_barrier is constrained by lower-stack physics, though not determined.

**What the debt reduction does NOT buy:**

- Unconditional M4. The carrier commitment remains provisional.
- Erasure of the HIC bridge debt. W0 addresses only the carrier barrier.
- A specific numerical value for ΔG_barrier. Only an inequality is derived.
- Proof that the quantum selection-rule mechanism matches the Book VII operational model.

---

## 2. Why W0 Is Worth Running in Parallel

Book VII provisionally committed the carrier bridge with the explicit caveat: "If future analysis shows the carrier's barrier is structurally limited below 28 kT, the commitment fails." The barrier height was described as "physically plausible for a K=2-scale composite with covalent-like bond distortion — comparable in magnitude to half the gauge binding energy" but not derived.

W0 tests whether this plausibility can be sharpened into derivational support using the lower-stack architecture that is already established. If it can, the epistemic status of Book VII improves — the carrier commitment becomes less vulnerable to revocation. If it cannot, the vulnerability is precisely characterized.

W0 runs in parallel because:
1. It does not modify the mainline Book VIII sequence (downstream domain reassessment proceeds regardless).
2. It addresses a specific vulnerability in the program's foundation.
3. The answer — whether the barrier is supported or not — does not change what Book VIII tests, only how confidently Book VIII's M4 assumption is held.

---

## 3. Restatement of the Book VII Carrier Vulnerability

### What Book VII Established

| Achievement | Authority | Status |
|------------|-----------|--------|
| Carrier bridge (Family J, K=2 composite) | Book VII Beta | Designed |
| Three-regime structure (weak/marginal/robust) | Book VII Gamma | Verified |
| M4-conditional in robust regime (ΔG ≥ 28 kT) | Book VII Gamma | CONDITIONAL |
| Carrier provisionally committed | Book VII Gamma | PROVISIONAL |
| η_carrier > 0.95 in robust regime | Book VII Gamma | Verified |
| Directed fraction ~30–34% in robust regime | Book VII Gamma | Verified |

### What Book VII Did NOT Establish

1. **ΔG_barrier is not derived.** Book VII Gamma stated: "28 kT ≈ half the K=2 gauge binding energy; conformational distortion of this magnitude is structurally available for covalently bonded composites." This is a plausibility argument, not a derivation.

2. **The loaded state is not specified.** The carrier has a "loaded/unloaded conformational switch," but the physical nature of the loaded state — what conformational distortion stores the energy, and what prevents spontaneous relaxation — is postulated, not derived.

3. **The leak rate is assumed Arrhenius.** k_leak = ν₀ exp(−ΔG/kT) assumes a classical barrier in a free-energy landscape. Whether the K=2 composite actually has such a landscape is not shown.

### Why ΔG ≥ 28 kT Is Load-Bearing

The entire M4 program depends on this single inequality:

- Below ΔG = 23 kT: carrier is non-functional (η < 0.1); scaffold remains at M3.
- At ΔG = 25 kT: marginal (η ~ 0.75); directed fraction ~25–30%; M3-M4 boundary.
- At ΔG ≥ 28 kT: robust (η > 0.95); directed fraction ~30–34%; M4 confirmed.

Every downstream conditional (D4-conditional, L4-approaches, A4-conditional) depends on M4, which depends on ΔG ≥ 28 kT. The barrier inequality is the single most load-bearing unproven assumption in the current scaffold.

### What W0 Tests Beyond Book VII

W0 asks whether the lower-stack architecture (SU(2) gauge bridge, K=2 composite structure, bound-state spectrum, hard core, selection rules) provides derivational support for the barrier — not as a new postulate, but as a consequence of already-installed structure.

---

## 4. Required Barrier Target

### 4.1 Formal Barrier Conditions

| Condition | Requirement | Source |
|-----------|-------------|--------|
| Loaded-state survival | τ_carrier ≫ τ_diffusion (~2 ms for L ~ 1 μm) | Book VII Gamma §5.1 |
| Diffusion timescale | τ_diffusion ~ L²/(6D) ≈ 2 ms | D ~ 10⁻¹⁰ m²/s for K=2 in polymer interior |
| Leak timescale (Arrhenius) | τ_leak = ν₀⁻¹ exp(+ΔG/kT) | Book VII operational model |
| Required inequality | τ_leak ≫ τ_diffusion | η_carrier ≈ 1 − τ_diff/τ_leak for τ_leak ≫ τ_diff |
| Robust regime | ΔG ≥ 28 kT → η > 0.95 → τ_leak/τ_diff > 300 | Book VII Gamma §5.1 |

### 4.2 Regime Classification

| Regime | ΔG (kT) | η_carrier | Directed fraction | Level |
|--------|---------|-----------|------------------|-------|
| Weak | < 23 | < 0.1 | ~15–25% | M3 only |
| Marginal | 23–28 | 0.1–0.6 | ~25–35% | M3–M4 boundary |
| **Robust** | **≥ 28** | **> 0.95** | **~30–45%** | **M4** |

### 4.3 What W0 Must Derive or Bound

W0 does not need to compute ΔG to arbitrary precision. It must determine whether:

1. The lower-stack architecture supports ΔG ≥ 28 kT as a generic expectation (not fine-tuned).
2. A physical mechanism for metastability exists within the K=2 composite structure.
3. The mechanism is consistent with existing bridge-level formalism (no silent new postulates).

---

## 5. Lower-Stack Ingredient Inventory

### 5.1 SU(2) Gauge Attraction Scale

| Ingredient | Value/Structure | Source | Helps/Hurts/Neutral |
|-----------|----------------|--------|---------------------|
| Gauge coupling | α_g = g²/(2π) | Book IV Beta (free parameter) | **HELPS** — sets binding energy scale |
| Singlet-channel potential | V(d) = −α_g/d for d > R_sk | Book IV Beta §7 | **HELPS** — provides attractive well |
| Binding energy (ground state) | E_bind ≈ α_g² M_sk / 4 | Book IV Beta §5 | **HELPS** — sets energy scale for barrier |
| Excitation energy (N=1→N=2) | ΔE₁₂ = (3/4) E_bind = 3α_g² M_sk / 16 | Hydrogenic spectrum | **KEY** — this is the candidate barrier scale |

### 5.2 Composite K=2 Binding Structure

| Ingredient | Value/Structure | Source | Helps/Hurts/Neutral |
|-----------|----------------|--------|---------------------|
| Quantum numbers | (N, ℓ, m_ℓ, S, m_S) with exchange constraints | Book IV Beta §6 | **HELPS** — state classification exists |
| Ground state | (N=1, ℓ=0, S=0): para-singlet | Book IV Beta §7.2 | **NEUTRAL** — defines "unloaded" |
| First excited shell | N=2: (ℓ=0, S=0) + (ℓ=1, S=1) | Book IV Beta §6.2 | **KEY** — candidate loaded states |
| Selection rules | Dipole: Δℓ = ±1 | Standard QM | **KEY** — creates metastability |
| Bohr radius | a₀ = 1/(α_g μ_red) = 2/(α_g M_sk) | Book IV Beta §5 | **NEUTRAL** — size scale |
| Positronium analogy | Equal-mass para/ortho structure | Book IV Beta §8.2 | **HELPS** — 2s metastability is well-known |

### 5.3 Hard-Core / Repulsive-Core Structure

| Ingredient | Value/Structure | Source | Helps/Hurts/Neutral |
|-----------|----------------|--------|---------------------|
| Hard core at R_sk | V → +∞ for d ≤ R_sk | Book IV Beta §4.2 | **HELPS** — prevents collapse; modifies spectrum |
| Degeneracy breaking | ℓ-degeneracy broken: E(N,ℓ=0) > E(N,ℓ=1) | Book IV Beta §5.2 | **HELPS** — s-wave shifted up (less bound) than p-wave |
| Well depth at core | V(R_sk) = −α_g/R_sk | Book IV Beta §4 | **NEUTRAL** — sets maximum well depth |
| Scale hierarchy | a₀ ≫ R_sk in weak coupling | Book IV Beta §5.1 | **HELPS** — hydrogenic approximation valid |

### 5.4 Strain Topology / Conformational Degrees

| Ingredient | Value/Structure | Source | Helps/Hurts/Neutral |
|-----------|----------------|--------|---------------------|
| Relative separation d | Radial collective coordinate | Book IV Alpha §config-space | **HELPS** — deformation degree |
| Relative orientation | SO(3)/SU(2) collective coordinate | Book IV Alpha §config-space | **HELPS** — orientational landscape |
| Gauge redundancy | Orientation → gauge-redundant after SU(2) gauge bridge | Book IV Beta (gauge bridge) | **NEUTRAL** — reduces moduli but doesn't kill conformational freedom |
| Centrifugal barrier (ℓ > 0) | ℓ(ℓ+1)/(2μd²) | Standard QM | **HELPS** — additional barrier for non-s-wave states |

### 5.5 Existing Geometric Locking Structure

| Ingredient | Value/Structure | Source | Helps/Hurts/Neutral |
|-----------|----------------|--------|---------------------|
| Geometry-locked HIC discharge | Backbone strain → geometry-matched target | Book V Delta | **HELPS** — precedent for geometry-locked energy transfer |
| Carrier-discharge pocket | Geometry-locked delivery at compatible sites | Book VII Beta | **Already postulated** — part of the carrier bridge |
| K=2 internal geometry | Dependent on (d, orientation, ℓ) | Lower stack | **HELPS** — rich internal landscape |

### 5.6 Lower-Stack Obstructions to Metastability

| Potential obstruction | Severity | Assessment |
|----------------------|----------|------------|
| Dissipation trivializing metastable states | **MODERATE** | Dissipation (τ dΦ/dt + Φ = X) operates on the field Φ, not on the composite's internal quantum numbers. Bound-state spectrum is a consequence of the gauge + matter bridge, not of the GRUT native field. Dissipation affects the collective-coordinate dynamics but not the selection rules. |
| Gauge-boson radiation draining excited states | **PRESENT but selection-rule suppressed** | Allowed transitions (Δℓ = ±1) decay quickly. Forbidden transitions (Δℓ = 0) are suppressed by orders of magnitude. This is the metastability mechanism. |
| Thermal excitation washing out the barrier | **LOW** | For ΔG ≫ kT, thermal population of the excited state is exponentially small. The barrier exists because the loaded state decays slowly, not because it can't be thermally populated. |
| Non-hydrogenic corrections destroying metastability | **LOW** | Hard-core and short-range corrections shift levels but do not destroy the selection rules. The Δℓ = ±1 selection rule is exact for any central potential; it does not depend on the Coulomb form. |

---

## 6. Candidate Derivation Routes

### Family A — Pure Binding-Depth Route

**Concept:** The carrier barrier arises directly from the gauge binding energy of the K=2 composite. The excitation energy from the ground state to the first excited shell provides the energy scale for the loaded state. The barrier is simply the energy gap between the N=1 and N=2 shells.

**Analysis:**

The excitation energy is:
ΔE₁₂ = E₁ − E₂ = (−α_g²μ/2) − (−α_g²μ/8) = (3/8)α_g²μ = (3/16)α_g²M_sk

For this to exceed 28 kT:
(3/16)α_g²M_sk ≥ 28 kT

Rearranging:
**α_g² × (M_sk/kT) ≥ 149**

Since M_sk/kT ≫ 1 is independently required for soliton thermal stability, and α_g is a moderate gauge coupling, this condition is generically satisfied. Examples:

| α_g | M_sk/kT | α_g²(M_sk/kT) | ΔE₁₂/kT | Robust? |
|-----|---------|---------------|---------|---------|
| 0.20 | 4000 | 160 | 30 | YES |
| 0.25 | 3000 | 188 | 35 | YES |
| 0.30 | 2000 | 180 | 34 | YES |
| 0.15 | 8000 | 180 | 34 | YES |
| 0.10 | 15000 | 150 | 28 | MARGINAL |
| 0.10 | 10000 | 100 | 19 | NO |
| 0.40 | 1000 | 160 | 30 | YES |

The robust regime is accessed across a broad parameter range. Only scaffolds with very weak coupling (α_g < 0.1) AND relatively low soliton-to-thermal mass ratio (M_sk/kT < 15000) fail.

**But this route alone does NOT establish metastability.** The excitation energy is the amount of energy stored, not the barrier preventing its release. If the excited state decays instantly, the energy is released as radiation, not stored. Family A provides the energy scale but not the kinetic trapping.

**Verdict:** Provides energy-scale support. Does NOT provide metastability. Must be combined with a metastability mechanism (Family B or C). **NECESSARY BUT NOT SUFFICIENT.**

### Family B — Binding + Selection-Rule Metastability Route

**Concept:** The barrier arises from the combination of Family A's energy scale with quantum selection-rule protection. The (N=2, ℓ=0, S=0) state of the K=2 composite cannot decay to the ground state (N=1, ℓ=0, S=0) via single gauge-boson emission because the dipole selection rule requires Δℓ = ±1. This creates a genuinely metastable loaded state.

**Analysis:**

The dipole (E1) selection rule Δℓ = ±1 is exact for any central potential — it follows from angular momentum conservation, not from the specific form of the potential. The K=2 composite's gauge-mediated potential is central in the relative coordinate. Therefore:

- (N=2, ℓ=1, S=1) → (N=1, ℓ=0, S=0): **ALLOWED** by E1. Fast decay.
- (N=2, ℓ=0, S=0) → (N=1, ℓ=0, S=0): **FORBIDDEN** by E1. Metastable.

The (N=2, ℓ=0) state can decay only through:
1. **Two-gauge-boson emission** (2E1): rate suppressed by α_g² relative to single-boson; analogous to hydrogen 2s → 1s two-photon decay.
2. **Magnetic dipole (M1)**: suppressed by v/c factors; typically negligible for non-relativistic bound states.
3. **Higher-order multipole (E2, M2, ...)**: even more suppressed.

In hydrogen, the 2s state has lifetime τ_2s ≈ 0.12 s versus τ_2p ≈ 1.6 × 10⁻⁹ s — a factor of ~10⁸. This ratio scales as ~1/α² for a general gauge coupling, making selection-rule suppression even stronger for weaker couplings.

**Carrier operational model under Family B:**

1. **Loading:** HIC discharge excites a K=2 composite from (N=1, ℓ=0) to (N=2, ℓ=0). The HIC backbone relaxation provides energy ΔE₁₂, which is deposited into the composite's internal degree of freedom (radial excitation). This requires the HIC discharge energy to be resonant with ΔE₁₂ — a matching condition that is self-consistent if the HIC is tuned to the K=2 binding scale (which it is, since the HIC operates on K-scale processes).

2. **Diffusion:** The excited (N=2, ℓ=0) composite diffuses through the proto-cell interior. Its diffusion coefficient is similar to the ground-state composite (same size, same mass). During diffusion, the composite is selection-rule-protected against radiative decay. Its effective lifetime τ_carrier ≫ τ_2p.

3. **Discharge at target:** At a compatible target site, the local non-spherically-symmetric potential of the target scaffold breaks the selection-rule protection by mixing ℓ=0 and ℓ=1 states. The composite rapidly de-excites to the ground state, releasing ΔE₁₂ to drive the target process. This is analogous to collisional quenching of the hydrogen 2s state — a well-known atomic-physics mechanism.

4. **Recycling:** The de-excited (N=1, ℓ=0) composite is released and diffuses back to the carrier pool.

**Strengths:**
- Selection-rule protection is exact for any central potential (no fine-tuning).
- The metastability is generic, not dependent on specific K=2 structure details.
- Collisional quenching at target sites provides selective discharge (geometry-locked).
- The energy scale is the same as Family A: ΔE₁₂ = (3/16)α_g²M_sk.

**Weaknesses:**
- The two-gauge-boson decay rate (the actual leak rate) is not computed within the GRUT formalism.
- The matching condition (HIC discharge resonant with ΔE₁₂) is assumed, not derived.
- Dissipation-background effects on the metastable state are not assessed.
- The collisional-quenching mechanism at target sites is structurally plausible but not explicitly derived.

**Verdict:** Provides both energy scale AND metastability mechanism. The strongest route. **SURVIVES — materially supports the barrier but does not force a specific height.**

### Family C — Binding + Repulsive-Core Transition-State Route

**Concept:** The barrier arises from the K=2 composite being loaded into a centrifugally-trapped state. The HIC discharge kicks the composite into an ℓ > 0 state, which has a centrifugal barrier preventing classical infall to the ground configuration.

**Analysis:**

For ℓ = 1, the effective potential has a centrifugal maximum at d_max = ℓ(ℓ+1)/(μα_g) = 2/(μα_g) = 4/(α_g M_sk). The height of the centrifugal barrier above the potential minimum is:

V_barrier ≈ E_bind/4 = α_g²M_sk/16

For this to exceed 28 kT:
α_g²M_sk/16 ≥ 28 kT
α_g²(M_sk/kT) ≥ 448

This is a tighter constraint than Family A/B (which requires ≥ 149). It is still generically satisfied for scaffolds with thermally stable solitons and moderate coupling, but less generously.

**Critical problem:** The ℓ=1 state is NOT selection-rule protected — it decays to the ℓ=0 ground state via allowed E1 transitions. The centrifugal barrier protects against classical radial collapse, but gauge-boson emission can change ℓ quantum-mechanically. The metastability of the ℓ=1 state depends on the radiative lifetime, not the classical barrier height.

For hydrogen 2p: τ_2p ≈ 1.6 ns — extremely short. The K=2 composite's ℓ=1 lifetime would be comparably short (relative to the diffusion timescale of ~2 ms). This makes Family C's ℓ=1 carrier operationally non-viable: it decays during transit.

**Verdict:** Provides a classical barrier but the state is radiatively unstable. The centrifugal barrier is irrelevant because gauge-boson emission bypasses it. **FAILS — radiative instability kills the carrier before delivery.**

### Family D — Collective-Coordinate Metastability Route

**Concept:** The barrier arises in the reduced collective-coordinate energy landscape of the K=2 composite, including both separation and orientation degrees of freedom. A local minimum in the multi-dimensional landscape creates a metastable loaded configuration.

**Analysis:**

The K=2 composite's energy depends on:
- Relative separation d
- Relative orientation (parameterized by Euler angles or equivalent)
- Angular momentum ℓ (quantized)

In the pure radial direction, there is ONE minimum (the bound state) with no second minimum. The potential is V(d) = −α_g/d + V_hard(d) — monotonically attractive for d > R_sk, repulsive for d < R_sk. No classical radial metastability.

In the orientational sector: The interaction between two Skyrmion-type solitons depends on relative orientation. The potential has an angular dependence V(d, Ω) that creates preferred orientational configurations. In the full Skyrme model, the B=2 sector has a rich energy landscape with the toroidal minimum as the global ground state and various saddle points and local minima for other configurations.

**However:** In the GRUT scaffold at weak coupling (a₀ ≫ R_sk), the two solitons are well-separated. Orientational effects are exponentially suppressed at distances d ≫ R_sk (they arise from soliton-profile overlap, which is localized to d ~ R_sk). At the Bohr radius a₀ ≫ R_sk, the orientational interaction is negligible — the potential is effectively central.

For the orientational barrier to be significant, the composite would need to be in a regime where d ~ R_sk, which is the strong-coupling regime. But the GRUT scaffold uses the weak-coupling regime.

**Verdict:** Orientational metastability requires strong coupling, which is outside the regime of the current scaffold analysis. **CONDITIONAL — applies only in strong-coupling regime, which is not the primary analysis regime.**

### Family E — Pseudo-Support Route

**Concept:** The apparent barrier support is merely a restatement of the Book VII matched parameter. The inequality ΔE₁₂ ≥ 28 kT is achieved only by requiring α_g²(M_sk/kT) ≥ 149, which is itself a parameter constraint — not a derivation.

**Analysis:**

This is the adversarial counter to Families A and B. The argument goes:

1. Book VII assumed ΔG ≥ 28 kT (matched parameter).
2. W0 identifies ΔE₁₂ = (3/16)α_g²M_sk as the energy scale (lower-stack connection).
3. W0 states ΔE₁₂ ≥ 28 kT iff α_g²(M_sk/kT) ≥ 149 (inequality).
4. But α_g and M_sk/kT are free parameters. Requiring α_g²(M_sk/kT) ≥ 149 is just translating one free parameter (ΔG_barrier) into a constraint on two others (α_g, M_sk/kT).

**Counter-argument:**

The translation is NOT trivial because:

1. **The connection to binding physics is real.** The barrier is not an arbitrary parameter — it is the excitation energy of the K=2 composite, determined by the same gauge coupling that binds it. The barrier and the binding energy are the same physics.

2. **The parameter regime is independently motivated.** M_sk ≫ kT is required for soliton stability (not invented for the barrier). α_g moderate is required for binding (not invented for the barrier). The condition α_g²(M_sk/kT) ≥ 149 is automatically satisfied in any scaffold that independently has stable solitons and gauge-mediated binding.

3. **The metastability mechanism is new.** Book VII assumed an unspecified conformational switch. W0 identifies a specific mechanism (selection-rule protection of the (N=2, ℓ=0) state). This is not a restatement — it is a structural identification.

4. **The loaded/discharge model is new.** Book VII assumed a loaded/unloaded conformational switch with Arrhenius kinetics. W0 identifies excitation/quenching of a bound-state level with quantum kinetics. This is a different (and more robust) operational model.

**Verdict:** The pseudo-support critique has partial force (the inequality does contain free parameters) but does not invalidate the debt reduction (the physical mechanism and the self-consistency are real). **PARTIALLY APPLIES — warns against overclaiming, but does not kill the reduction.**

---

## 7. Hard-Criteria Evaluation

| Criterion | Family A (binding depth) | Family B (selection rule) | Family C (centrifugal) | Family D (collective coord) | Family E (pseudo) |
|-----------|------------------------|--------------------------|----------------------|---------------------------|-------------------|
| 1. Lower-stack consistency | **YES** — uses existing spectrum | **YES** — uses existing selection rules | **YES** — uses existing QM | **PARTIAL** — strong-coupling regime | N/A |
| 2. Metastable loaded state | **NO** — energy scale only | **YES** — (N=2, ℓ=0) protected | **NO** — ℓ=1 radiatively unstable | **CONDITIONAL** | N/A |
| 3. Barrier in robust regime | **YES** — ΔE₁₂ ≥ 28 kT generic | **YES** — same scale + protection | **YES** — centrifugal height sufficient | **CONDITIONAL** | **PARTIAL** |
| 4. Generic or fine-tuned | **GENERIC** — broad parameter range | **GENERIC** — selection rule is exact | **GENERIC** — but unstable | **FINE-TUNED** (strong coupling) | N/A |
| 5. Uses allowed structure only | **YES** — no new assumptions | **YES** — no new assumptions | **YES** | **PARTIAL** — strong-coupling extrapolation | **N/A** |
| 6. Reduces bridge debt | **PARTIAL** (scale connection only) | **YES** (mechanism + scale) | **NO** (mechanism fails) | **CONDITIONAL** | **NO** |
| 7. Sensitivity to unknowns | MODERATE (α_g, M_sk/kT) | MODERATE (same + decay rate) | HIGH (radiative lifetime) | HIGH (K=2 landscape) | N/A |
| 8. Strengthens Book VII | **PARTIALLY** (scale support) | **YES** (mechanism + scale) | **NO** | **CONDITIONAL** | **NO** |
| **Verdict** | **Necessary ingredient** | **SURVIVES (strongest)** | **FAILS** | **CONDITIONAL (secondary)** | **Warning applied** |

---

## 8. Barrier Estimate / Inequality Analysis

### 8.1 The Central Inequality

The lower-stack architecture yields the following derivable inequality chain:

**Step 1:** The K=2 composite in the singlet channel has a hydrogenic spectrum with binding energy E_bind = α_g²M_sk/4 (Book IV Beta, confirmed in weak coupling).

**Step 2:** The first excitation energy is ΔE₁₂ = (3/4)E_bind = (3/16)α_g²M_sk.

**Step 3:** The state (N=2, ℓ=0, S=0) is selection-rule protected against E1 decay (exact for central potentials).

**Step 4:** The carrier barrier is identified with ΔE₁₂ (the energy stored in the excited state):

**ΔG_barrier ≈ ΔE₁₂ = (3/16) α_g² M_sk**

**Step 5:** For the robust regime:

**(3/16) α_g² M_sk ≥ 28 kT**

**⟹ α_g² × (M_sk / kT) ≥ 149**

### 8.2 Scale Comparison to Gauge Binding Energy

Book VII Gamma stated: "28 kT ≈ half the K=2 gauge binding energy." Let us check:

E_bind = α_g²M_sk/4

28 kT / E_bind = 28 kT / (α_g²M_sk/4) = 112 / (α_g²M_sk/kT)

For α_g = 0.3, M_sk/kT = 2000:
28 kT / E_bind = 112 / (0.09 × 2000) = 112/180 = 0.62

For α_g = 0.2, M_sk/kT = 4000:
28 kT / E_bind = 112 / (0.04 × 4000) = 112/160 = 0.70

The robust barrier (28 kT) is indeed about 60–70% of the binding energy in the typical parameter range. Book VII's qualitative estimate ("half the binding energy") was approximately correct.

### 8.3 Dimensionless Ratios

| Ratio | Expression | Typical value | Interpretation |
|-------|-----------|---------------|---------------|
| ΔE₁₂/kT | (3/16)α_g²(M_sk/kT) | 28–40 | Barrier in thermal units |
| ΔE₁₂/E_bind | 3/4 | 0.75 | Barrier as fraction of total binding |
| kT/M_sk | 1/(M_sk/kT) | 10⁻³–10⁻⁴ | Thermal energy vs soliton mass |
| kT/E_bind | 4/(α_g²M_sk/kT) | 0.02–0.05 | Thermal energy vs binding energy |
| R_sk/a₀ | α_g(M_sk R_sk)/2 | ≪ 1 (weak coupling) | Core/orbit ratio |

### 8.4 Explicit Unknowns and Where They Enter

| Unknown | Where it enters | Effect on barrier | Status |
|---------|----------------|------------------|--------|
| α_g | Barrier ~ α_g²; binding ~ α_g² | Both scale together; ratio fixed at 3/4 | Free parameter; constrained by binding requirement |
| M_sk/kT | Barrier ~ M_sk/kT; soliton stability ~ M_sk/kT | Both require M_sk ≫ kT | Free parameter; constrained by scaffold stability |
| Hard-core corrections | Shift ΔE₁₂ upward for s-wave (less bound); downward for p-wave | Reduces ΔE₁₂ slightly (s-wave shifted up) | Correction < O(R_sk/a₀)² ≪ 1 |
| Two-gauge-boson rate | Sets actual leak rate of (N=2, ℓ=0) state | Determines τ_carrier quantitatively | **NOT COMPUTED** |
| Dissipation coupling | May dampen or dephase the excited state | Could reduce effective lifetime | **NOT ASSESSED** |
| Quenching cross-section | Sets discharge rate at target sites | Determines η_carrier at targets | **NOT COMPUTED** |

### 8.5 What Is Derivable vs What Remains Open

**Derivable:**
- ΔE₁₂ = (3/16)α_g²M_sk (from hydrogenic spectrum)
- Selection-rule protection of (N=2, ℓ=0) state (from angular momentum conservation)
- Robust regime achieved when α_g²(M_sk/kT) ≥ 149 (inequality)
- The condition is generically satisfied for stable scaffolds with moderate coupling

**Open:**
- Absolute value of τ_carrier (requires two-gauge-boson rate calculation)
- Comparison of τ_carrier to τ_diffusion (requires absolute energy/time scales)
- Non-hydrogenic corrections to ΔE₁₂ (requires hard-core level-shift computation)
- Dissipation-background effects (requires dissipation × bound-state interaction analysis)

---

## 9. Debt-Status Classification

### 9.1 Mandatory Definitions

| Term | Definition |
|------|-----------|
| **Matched parameter** | A numerical value chosen to make the model work, with no connection to deeper structure. |
| **Lower-stack support** | The value is connected to lower-stack physics (bounded, scaled, or correlated with other quantities), but not uniquely determined. |
| **Approximate derivation** | The value is determined to within a bounded range by lower-stack physics, with remaining uncertainty traceable to specific unknowns. |
| **Forced consequence** | The value is uniquely determined by lower-stack physics with no remaining free parameters. |
| **Bridge debt** | A postulated quantity required for the model to work, not derived from deeper structure. Full debt: no connection to lower stack. |
| **Debt reduction** | The postulated quantity is partially connected to lower-stack physics, reducing the epistemic distance between the assumption and the foundations. |
| **Debt erasure** | The postulated quantity is fully derived from lower-stack physics. The postulate becomes a theorem. |
| **Robust barrier regime** | ΔG ≥ 28 kT; η_carrier > 0.95; M4 operational. |
| **Native support** | A mechanism or value that exists within the already-installed lower-stack structure, without requiring new postulates. |
| **Native derivation** | A mechanism or value that is uniquely determined by the already-installed lower-stack structure. |

### 9.2 Pre-W0 Status

| Carrier parameter | Pre-W0 status | Epistemic class |
|------------------|--------------|----------------|
| E_carrier (energy content) | Matched to "about half the binding energy" | Matched parameter |
| τ_carrier (lifetime) | Derived from ΔG via Arrhenius | Dependent on matched ΔG |
| ΔG_barrier (barrier height) | "Physically plausible for K=2 composites" | **Matched parameter** |
| Loaded-state identity | "Conformational switch" — unspecified | **Postulated** |
| Metastability mechanism | Assumed (Arrhenius over classical barrier) | **Postulated** |

### 9.3 Post-W0 Status

| Carrier parameter | Post-W0 status | Epistemic class | Change |
|------------------|---------------|----------------|--------|
| E_carrier | Identified with ΔE₁₂ = (3/16)α_g²M_sk | **Lower-stack supported** | ↑ Matched → Supported |
| τ_carrier | Selection-rule-protected; >> τ_allowed | **Lower-stack supported** (qualitatively) | ↑ Matched → Supported |
| ΔG_barrier | Bounded: ΔG ≈ ΔE₁₂; robust when α_g²(M_sk/kT) ≥ 149 | **Approximately derived** (inequality, not value) | ↑ Matched → Approximately derived |
| Loaded-state identity | (N=2, ℓ=0, S=0) excited state of K=2 composite | **Lower-stack identified** | ↑ Postulated → Identified |
| Metastability mechanism | Quantum selection-rule protection (Δℓ=0 forbidden for E1) | **Lower-stack derived** | ↑ Postulated → Derived |

### 9.4 Debt-Status Verdict

**Carrier bridge debt: REDUCED (strong reduction).**

The carrier barrier moves from "matched parameter with plausibility argument" to "approximately derived quantity with lower-stack mechanism." The specific improvements:

1. The barrier height is connected to the binding energy by ΔG ≈ (3/4)E_bind — not a coincidence, but a consequence of the K=2 spectrum.
2. The metastability mechanism is identified as selection-rule protection — a quantum-mechanical fact, not a postulate.
3. The robust regime is shown to be generic for thermally stable scaffolds with moderate coupling.
4. The loaded state has a structural identity: the (N=2, ℓ=0) bound state.

The debt is NOT erased because:
1. α_g and M_sk/kT are undetermined.
2. The two-gauge-boson decay rate is not calculated.
3. Non-hydrogenic corrections are not assessed.
4. The connection between the quantum and classical (Arrhenius) pictures is informal.

**Classification:** The carrier bridge retains 1 postulate (carrier functional class) + 2 parameters (E_carrier, τ_carrier), but the parameters are now lower-stack-supported rather than free-floating. The postulate count does not change; the parameter epistemic quality improves.

---

## 10. Failure / Fragility Audit

| Stress test | Result | Detail |
|------------|--------|--------|
| **1. Hidden assumption: loading resonance** | **MODERATE CONCERN** | Family B requires HIC discharge energy ≈ ΔE₁₂. This matching condition is plausible (HIC operates on K-scale processes) but not derived. If the energies don't match, loading fails. |
| **2. Hidden assumption: quenching at targets** | **MODERATE CONCERN** | Discharge requires collisional quenching of the (N=2, ℓ=0) state at target sites. Quenching requires a non-central perturbation strong enough to mix ℓ=0 and ℓ=1 at close range. This is standard in atomic physics but not explicitly shown for the GRUT scaffold. |
| **3. Geometry sensitivity** | **LOW** | Selection-rule protection is exact for any central potential. It does not depend on the specific form of V(d) or on K=2 structural details. |
| **4. Specific K=2 structure details** | **MODERATE** | The hydrogenic approximation assumes weak coupling (a₀ ≫ R_sk). In intermediate coupling, corrections could shift ΔE₁₂ significantly. The barrier inequality α_g²(M_sk/kT) ≥ 149 assumes the unperturbed hydrogenic formula. |
| **5. Dissipation-background effects** | **OPEN** | The GRUT native dissipation (τ dΦ/dt + Φ = X) could in principle couple to the bound-state dynamics. If dissipation damps the relative motion of the two solitons, it could accelerate de-excitation and shorten the carrier lifetime. This interaction has not been analyzed. |
| **6. Two-gauge-boson rate** | **OPEN** | The actual carrier lifetime depends on the two-gauge-boson decay rate of the (N=2, ℓ=0) state. This is O(α_g²) suppressed relative to the E1 rate but the absolute value is not computed. If it is too fast, the carrier leaks during diffusion. |
| **7. Merely reimports Book VII parameter** | **NO** | The derivation connects ΔG to α_g and M_sk/kT through a specific physical mechanism (spectral excitation + selection rule). This is a genuine structural connection, not a renaming. But the Family E pseudo-support critique correctly notes that free parameters remain. |
| **8. Suggestive but not probative** | **PARTIALLY APPLIES** | The derivation shows the robust regime is generic and identifies a mechanism, but does not compute the leak rate or verify τ_carrier > τ_diffusion absolutely. The support is strong enough for debt reduction but not for debt erasure. |

---

## 11. False-Positive Audit

| False-positive category | Applies? | Reason |
|------------------------|---------|--------|
| **Qualitative plausibility only** | **NO** | W0 provides a derivable inequality and a specific mechanism, not just "it seems right." |
| **Scale similarity without transition-state logic** | **PARTIALLY** | W0 provides the energy scale AND the selection-rule mechanism. But the transition-state geometry (quenching at targets) is assumed, not derived. |
| **Bound estimates too weak for robust regime** | **NO** | The inequality α_g²(M_sk/kT) ≥ 149 is satisfied across a broad parameter range. The bound is not razor-thin. |
| **Support for metastability without barrier height** | **NO** | Both are provided: selection-rule metastability (mechanism) + ΔE₁₂ ≥ 28 kT (height). |
| **Debt reduction rhetoric without derivational content** | **NO** | The content is real: a new physical mechanism is identified, the barrier is connected to binding physics, and the robust regime is shown to be generic. |
| **Carrier support confused with HIC debt erasure** | **NO** | W0 addresses only the carrier barrier. HIC bridge debt is not mentioned or claimed reduced. |
| **One favorable estimate → native closure** | **HONEST CONCERN** | The derivation shows generic support for the robust regime across many parameter values. But "generic" does not mean "forced." The barrier could be below 28 kT for specific (low α_g, low M_sk/kT) parameter choices. W0 should NOT claim the barrier is forced. |

---

## 12. GRUT-RAI Barrier-Reduction State-Model Requirements

Specified in the companion state-model document.

---

## 13. Program Consequence

### Is the Robust Carrier Barrier Natively Supported, Partially Supported, Unsupported, or Undecidable?

**PARTIALLY SUPPORTED (strong partial).** The lower-stack architecture provides:
- A specific physical mechanism for metastability (selection-rule protection)
- A derivable energy scale (ΔE₁₂ = (3/16)α_g²M_sk)
- A computable inequality for the robust regime (α_g²(M_sk/kT) ≥ 149)
- Identification of the loaded state ((N=2, ℓ=0, S=0) excited bound state)

The barrier is not FORCED (free parameters remain). It is not UNSUPPORTED (real structural connection exists). It is not UNDECIDABLE (enough formalism exists to draw bounded conclusions).

### Does W0 Reduce Carrier Bridge Debt?

**YES — significantly.** The carrier parameters (E_carrier, τ_carrier, ΔG_barrier) move from "matched/postulated" to "lower-stack-supported/approximately-derived." The loaded state and metastability mechanism are structurally identified. The robust regime is shown to be generic.

### Does W0 Erase Carrier Bridge Debt?

**NO.** Two free parameters (α_g, M_sk/kT) remain. The two-gauge-boson decay rate is not computed. Non-hydrogenic corrections and dissipation effects are unassessed. The carrier postulate (functional class existence) is NOT retired by W0 — only its parameters are better supported.

### Does W0 Change Book VII's Epistemic Status?

**YES — modestly.** Book VII's conditional M4 status is strengthened:

| Aspect | Pre-W0 | Post-W0 |
|--------|--------|---------|
| ΔG_barrier basis | "Physically plausible" | Approximately derived from binding spectrum |
| Metastability | Assumed (conformational Arrhenius) | Identified (selection-rule quantum protection) |
| Robust regime | Parameter-matched | Shown generic for stable scaffolds |
| Conditional status | ΔG not derived; fully conditional | ΔG bounded; less conditional but still not forced |

The carrier commitment is still provisional. But the probability that the commitment must be revoked is materially lower, because the barrier is now connected to lower-stack physics rather than floating freely.

### Should the Mainline Book VIII Sequence Change Because of W0?

**NO.** Book VIII proceeds with downstream domain reassessment under M4 regardless of W0's outcome. W0 affects the *confidence level* of the M4 assumption, not its operational use. If W0 had found verdict C (barrier not supported), the mainline would still proceed (using M4 as a conditional assumption) but with an explicit warning. Since W0 finds verdict B (barrier materially supported), the mainline proceeds with increased confidence but no structural change.

---

## 14. Final W0 Verdict

**Global verdict: (B) — The carrier barrier is materially supported by lower-stack structure, reducing but not erasing debt.**

The lower-stack architecture provides a specific physical mechanism (selection-rule-protected quantum metastability of the (N=2, ℓ=0) state of the K=2 composite), a derivable inequality (α_g²(M_sk/kT) ≥ 149 for the robust regime), and a structural identification of the loaded state. The robust regime is the generic expectation for any scaffold with thermally stable solitons and moderate gauge coupling. The barrier is not a free-floating matched parameter — it is the excitation energy of the K=2 composite, determined by the same gauge coupling that binds it.

The debt is not erased because two free parameters remain undetermined, the two-gauge-boson decay rate is not computed, and the connection between the quantum metastability picture and the Book VII Arrhenius operational model is informal. The carrier postulate itself (the existence of a carrier functional class) is not retired.

**Carrier bridge debt status:** REDUCED (strong). Parameter quality upgraded from "matched" to "lower-stack-supported." Mechanism upgraded from "postulated" to "identified." Postulate count unchanged.

**Book VIII mainline impact:** None. Proceed with increased confidence in M4-conditional reasoning.

---

## 15. Hard-Gated Summary Table

| Test | Verdict | Reason |
|------|---------|--------|
| Book VII carrier vulnerability remains real | **YES** | ΔG_barrier still not fully derived; free parameters remain |
| At least one lower-stack support route survives | **YES** | Family B (selection-rule metastability) survives all stress tests |
| Robust barrier regime supported | **YES** | Generic for α_g²(M_sk/kT) ≥ 149; broad parameter range |
| Robust barrier regime forced | **NO** | Free parameters α_g and M_sk/kT not determined |
| Carrier bridge debt reduced | **YES** | Mechanism identified; energy scale derived; parameters supported |
| Carrier bridge debt erased | **NO** | Free parameters remain; decay rate not computed |
| Book VII epistemic status strengthened | **YES** | Barrier connected to binding physics; robust regime shown generic |
| Mainline Book VIII should remain unchanged | **YES** | W0 affects confidence level, not operational structure |

---

## 16. Nonclaims

1. NOT_claiming full native derivation of the carrier barrier — the derivation establishes an inequality and a mechanism, not a unique value.
2. NOT_claiming erasure of carrier bridge debt — two free parameters remain; the carrier postulate is not retired.
3. NOT_claiming erasure of HIC bridge debt — W0 addresses only the carrier barrier.
4. NOT_claiming erasure of any other bridge debts — W0 is scoped to the carrier barrier only.
5. NOT_claiming unconditional M4 — the carrier commitment remains provisional.
6. NOT_claiming ATP equivalence — the carrier is a proto-currency regardless of barrier support.
7. NOT_claiming life — this is a side-program debt-reduction audit.
8. NOT_claiming final ToE closure — unchanged.
9. NOT_claiming that plausibility has become derivation — the support is material but the barrier is not forced.
10. NOT_claiming that the quantum (selection-rule) picture has been formally mapped to the classical (Arrhenius) picture — the correspondence is structural but informal.

---

*Program W0 complete. Carrier barrier materially supported by lower-stack structure. Selection-rule-protected (N=2, ℓ=0) excited state identified as loaded-state mechanism. Robust regime generic when α_g²(M_sk/kT) ≥ 149. Debt reduced, not erased. Two free parameters remain. Book VIII mainline unaffected.*
