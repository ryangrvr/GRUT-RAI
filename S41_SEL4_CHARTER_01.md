# S4-1 — CAN Sel-4 BE SELECTED WITHOUT DEFINING GRAVITY AS Sel-4? CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Date:** 2026-09-25 · **Authority:** owner ruling recorded in
`EQ1_S41_OWNER_RULING_01.md`. **Question (owner):** *Can Sel-4 be
selected from 𝔠_full + access + G-2 spectral geometry without defining
gravity to mean Sel-4?* **Outcomes:** DERIVED/SELECTED ·
CONSTRAINED-NONUNIQUE · IRREDUCIBLE-INPUT · FAILS/NULL. **Binding
tightening:** "invisible to a sector's own internal data" is an
operational formulation, not an ontological statement. Every
discriminator below is therefore **unit-invariant but dynamically
sensitive**. Where the question is relative clocks, the discriminator
optimizes away the best common time rescaling and reads what survives.

## 0. DECOMPOSITION AND THE ONE INHERITED CONSTRAINT (stated up front)

Sel-4 ("a constant probe acts on each retained sector as a pure change of
units") has three logically separate parts, and each is tested
separately:
- **Sel-4t (temporal):** a constant probe acts on one sector's dynamics
  as a time-unit change, O ∝ H.
- **Sel-4U (universality):** the unit changes are the same across
  sectors.
- **Sel-4x (spatial/length):** the length part. EQ-1 already showed
  this is not selected by earned structure (the shape coupling
  survives). It is **carried from EQ-1, not re-tested.**

**Inherited constraint C_cons:** *at zero momentum, the probe's constant
limit couples to a conserved local charge*, i.e. its operator O
commutes with H. This is the zero-momentum form of the conservation
constraint CP-1 used and EQ-1 treated as earned. **Every "derived"
component below is conditional on C_cons.** Whether that inheritance is
legitimate is an owner question the verdict will flag. Without C_cons,
leg L-N shows the question collapses.

**Genuinely distinct alternatives (not reparameterizations of O ∝ H):**
- **(i)** a coupling to an extra local conserved charge, which changes
  the intrinsic spectral shape;
- **(ii)** non-universal clocks across sectors, ε_A ≠ ε_B, where each
  sector is internally a unit change, which is exactly the owner's
  quotient worry;
- **(iii)** a non-conserved local coupling.

**Fences:** ω⁷ occupancy only; ℏ located; GR-1 3D red; retained-sector
choice supplied; D = 4 TT/ξ, operator ordering and geometry selection
separate; no Einstein equations.

## 1. MACHINERY (frozen)

Exact finite spin systems. The commutant is computed symbolically in
the Pauli-string algebra, which is exact. Pauli strings are Hermitian,
so [Σ cₖOₖ, H] has purely imaginary string coefficients; dividing by i
gives a real linear map c ↦ [·, H]. The null space comes from the
eigenvalues of its Gram matrix, with tolerance 1e-10 × max. Exact
diagonalization is used where a spectrum or dynamics is needed.

Models:
- **MFIM (generic, non-integrable):** H = Σ ZᵢZᵢ₊₁ + 0.9045 Xᵢ +
  0.8090 Zᵢ.
- **TFIM (integrable):** the same with h_z = 0.
- **XX (free):** H = Σ XᵢXᵢ₊₁ + YᵢYᵢ₊₁. This is the free proxy for a
  retained sector of the phonon type.

All are periodic rings. The local basis is the translation-invariant
sums of Pauli patterns of range ≤ 3 (48 operators).

## 2. THE LEGS (frozen, predictions written before any number)

- **L-T (Sel-4t on a single sector: does locality + C_cons force
  O ∝ H?):** the commutant of H within the range-≤3 basis on L = 8.
  **Predictions:** MFIM dim = **1** (only H); TFIM dim **≥ 2**; XX dim
  **≥ 2**. Frozen consequence:
  - generic sector: temporal Sel-4 DERIVED-IN-CLASS (conditional on
    C_cons);
  - integrable or free sectors: extra local conserved charges survive,
    so temporal Sel-4 is NOT forced (CONSTRAINED-NONUNIQUE);
  - by sector class, this is a CLASS-SPLIT.
- **L-D (discriminator for alternative (i)):** TFIM at L = 6. O₂ is an
  extra conserved charge: a commutant null vector with H projected
  out, gated to have relative residual > 0.1 against H. Take a constant
  probe H + hO, h = 0.05. The unit-invariant observable is the
  normalized spectrum shape sₙ = (Eₙ − E₀)/(E_max − E₀).
  **Predictions:** O = H gives max|Δs| < 1e-10 (a unit change); O = O₂
  gives max|Δs| > 1e-4.
- **L-N (alternative (iii), what excludes it):** MFIM at L = 6,
  O = Σ Xᵢ. **Predictions:**
  - ‖[O, H]‖ > 0: excluded by C_cons, and by C_cons only;
  - the normalized spectrum shape changes by > 1e-4 (intrinsically
    visible);
  - the ground-state two-time Gram over {O(0), O(1), O(2.5)} is PSD
    (𝔠_full admits it);
  - its interaction graph equals H's, so G-2's hop geometry cannot see
    it.
- **L-U (Sel-4U, universality, with the dynamical discriminator):**
  - *Commutant:* two MFIM legs of L = 6. Leg A has (J, h_x, h_z) =
    (1, 0.9045, 0.8090); leg B has (1.3, 0.7, 0.5). The rung coupling
    is g Σ Z_{aᵢ}Z_{bᵢ}. The basis is leg-A range ≤ 2 (12), leg-B
    range ≤ 2 (12) and rung (9). **Predictions:** g = 0 gives dim
    **2** (H_A and H_B separately conserved, so ε_A ≠ ε_B is allowed);
    g = 0.3 gives dim **1** (only H_total, so universality is forced).
  - *Dynamics:* a ladder of 2 × 3 sites (64-dim ED), initial product
    state with leg A all up and leg B all down. The cross-sector
    observable is C(t) = ⟨Z_{a0}Z_{b0}⟩(t) on 41 points in [0, 10].
    Probes: universal (1 + h)H and non-universal H + hH_A, with
    h = 0.05. The discriminator is **Δ = min_c max_t |C_probe(t) −
    C(ct)|**: the best common time rescaling is optimized away (scan
    c ∈ [0.9, 1.1] in steps of 1e-3, then a golden-section refine to
    1e-12).
  - **Predictions, coupled (g = 0.3):** universal Δ < 1e-10
    (halt-grade: exact time rescaling); non-universal Δ > 1e-3.
  - **Predictions, decoupled (g = 0):** universal Δ < 1e-10;
    **non-universal Δ > 1e-3.** Relative clock rates are observable by
    joint access even without interaction, yet conservation does not
    forbid them.
  - Frozen consequence: universality is DERIVED-IN-CLASS for
    interacting sectors (via C_cons) and is **observable but unforced
    for non-interacting sectors: IRREDUCIBLE there.**
  - Also computed: the non-universal probe's interaction graph equals
    H's (G-2 hop geometry blind), and its ground-state Gram is PSD
    (𝔠_full admits it).

## 3. OUTCOME RULE (frozen, mechanical)

- **Sel-4t:** DERIVED-IN-CLASS if MFIM dim = 1; CONSTRAINED-NONUNIQUE
  for a class if its dim ≥ 2 and the L-D discriminator fires.
  CLASS-SPLIT if both hold.
- **Sel-4U:** DERIVED-IN-CLASS (interacting) if the coupled dim = 1 and
  the coupled non-universal Δ > 1e-3. IRREDUCIBLE (non-interacting) if
  the decoupled dim = 2 and the decoupled non-universal Δ > 1e-3
  (observable yet unforced).
- **Sel-4x:** IRREDUCIBLE (carried from EQ-1).
- **𝔠_full and G-2 geometry:** NULL as selectors if L-N and L-U show
  them admitting the alternatives.
- **Overall:** Sel-4 is DERIVED/SELECTED only if all three parts are
  derived in every tested class. Otherwise it is reported per part.
  Every "derived" part carries the explicit condition C_cons.

## 4. CONTROLS

- Halt-grade: the universal-probe Δ (an exact time rescaling).
- Halt-grade: the Pauli-algebra self-check that [H, H] = 0 exactly in
  the symbolic algebra.
- Halt-grade: the ED-vs-symbolic cross-check: the matrix commutator
  norm ‖[O₂, H]‖ < 1e-10 for the extracted TFIM charge.
- The symbolic commutant is recomputed at the ED size (L = 6) wherever
  ED uses it.

## 5. DELIVERABLES AND STOP

1. `calc/s41_sel4.py` (pure stdlib; emits `S41_SEL4_RESULT.json`,
   sha-hashed).
2. `S41_SEL4_VERDICT_01.md` and a closing comment on Issue #2.
3. **HARD STOP at the verdict.**
