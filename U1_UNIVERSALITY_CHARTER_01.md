# U-1 — CAN CLOCK UNIVERSALITY FOR GENUINELY NON-INTERACTING SECTORS BE DERIVED? CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Date:** 2026-09-25 · **Authority:** GitHub Issue #2, owner comment
**5835886532**. CC-1 was accepted at recorded strength. **Binding
status:** C_cons is an IRREDUCIBLE INPUT, reduced to the supplied
massless gauge-field/gauge-redundancy structure (including the Lorentz
covariance the positivity argument uses), for the clock/current
component. The blanket form is rejected. GeoInv is unearned and outside
𝒯. The architecture has three layers:
1. earned influence/access geometry;
2. supplied probe field structure (massless plus gauge/Lorentz
   redundancy);
3. the component-specific conservation consequence.

**Target (owner, verbatim):** *Can cross-sector clock universality for
genuinely non-interacting sectors be derived from anything already
earned plus the now-explicit probe-field structure, or is universality
itself an irreducible input?*

**Outcomes:** DERIVED/SELECTED · CONSTRAINED-NONUNIQUE · CLASS-SPLIT ·
IRREDUCIBLE INPUT · FAILS/NULL.

**Required design, and how it is met:**
1. *Genuinely decoupled sectors:* leg L-C, with rung coupling g = 0
   exactly.
2. *Distinct non-universal clock couplings that are C_cons-compatible
   and 𝔠_full-admissible:* O = ε_A H_A + ε_B H_B with
   (ε_A, ε_B) = (1, 0.6).
3. *Joint-access observables with the common time rescaling optimized
   out:* the S4-1 discriminator Δ = min_c max_t |C_probe(t) − C(ct)|
   on the cross-sector correlation ⟨Z_{a0}Z_{b0}⟩.
4. *Test every earned or supplied candidate for forcing equality:*
   earned symmetry, the supplied gauge structure, influence positivity,
   and spectral geometry are each tested.
5. *No smuggling of universality into "same units":* the only
   units-fixing step is the single common rescaling c, optimized. No
   per-sector rescaling is allowed, since that would *be* the
   universality assumption.
6. *The g → 0 issue:* a finite small-coupling sequence is tested
   separately from the exact endpoint (leg L-g).
7. *Fences:* the retained-sector choice, spatial/length equivalence,
   D = 4 TT/ξ, operator ordering, geometry selection, ω⁷, the GR-1 3D
   red, and ℏ are untouched. GeoInv is not used.

## 1. THE LEGS (frozen, predictions written before any number)

Models (reused from S4-1):
- **Ladder:** two MFIM legs of 3 sites (64-dim ED). Leg A has
  (J, h_x, h_z) = (1, 0.9045, 0.8090); leg B has (1.3, 0.7, 0.5); the
  rung coupling is g Σ Z_{aᵢ}Z_{bᵢ}.
- **Initial state:** leg A all up, leg B all down.
- **Probe strength:** h = 0.05.

- **L-C (the decoupled counterexample battery, g = 0).** The coupling
  O = H_A + 0.6 H_B. **Predictions:**
  - C_cons-compatible: ‖[O, H]‖ < 1e-12;
  - 𝔠_full: the ground-state two-time Gram of O is PSD;
  - interaction graph of H + hO equals that of H (G-2 hop geometry
    blind);
  - **each sector internally a pure unit change:** the normalized
    spectrum shape of H_A(1 + h) and of H_B(1 + 0.6h) is unchanged,
    each < 1e-12;
  - **joint-access discriminator:** Δ_non-universal > 1e-3 and
    Δ_universal < 1e-10 (halt-grade).

  Also recorded (P-6 carried): no earned symmetry relates the two
  (different) sectors. For identical sectors, swap covariance of the
  probe would force equality only if it were supplied. Frozen
  consequence: a non-universal clock coupling satisfies everything
  earned plus C_cons, yet is observable jointly.
- **L-G (the supplied gauge structure: does it force equality?).**
  - *Setup:* D = 4 soft-emission gauge variation of a massless tensor
    probe, q_μM^{μν} = Σₙ κ_{s(n)} ηₙ pₙ^ν, with sector charges
    κ = (1, 0.6) and 100 random configurations per class.
  - *Class I (genuinely decoupled):* momentum conserved separately,
    ΣA ηp = 0 and ΣB ηp = 0.
  - *Class II (exchanging):* ΣA ηp = −ΣB ηp = Δ ≠ 0.
  - **Predictions:** class I variation < 1e-12 for κ_A ≠ κ_B (NOT
    forced); class II variation > 1e-3 for κ_A ≠ κ_B, and < 1e-12
    for κ_A = κ_B (forced).
  - Frozen consequence: the supplied gauge structure forces
    universality **exactly when the sectors exchange energy-momentum**,
    and not for genuinely decoupled sectors.
- **L-D (does a dynamical probe itself create an exchange channel?).**
  - *Setup:* two 2-site MFIM sectors (A as above; B with parameters
    (1.3, 0.7, 0.5)) plus a probe oscillator (ω_b = 1, 5 levels,
    80-dim total), coupled by (b + b†)(κ_A O_A + κ_B O_B) with
    (κ_A, κ_B) = (0.3, 0.18).
  - *Initial state:* sectors in the Z-product state, probe in vacuum.
  - **(i) Clock-only probe (O_s = H_s):** ‖[H_A, H_full]‖ < 1e-12, and
    ⟨H_B⟩(t) is constant to 1e-10 on t ∈ [0, 10]. The probe mediates
    no energy exchange, so L-G class I applies and equality is not
    forced.
  - **(ii) Probe with non-conserved (T_xx-type) components
    (O_s = ΣXᵢ):** ‖[H_A, H_full]‖ > 1e-3, and ⟨H_B⟩(t) varies by
    > 1e-4. The probe IS an exchange channel, so L-G class II applies
    and equality is forced, given the supplied gauge structure.
- **L-g (the approach to the decoupled endpoint, kept separate).**
  The ladder with g ∈ {0.01, 0.003, 0.001} and g = 0, with
  O = H_A + 0.6 H_B. **Predictions:**
  - (i) ‖[O, H]‖/‖O‖ is exactly linear in g: successive ratios equal
    the g ratios to 1e-8, and the value is 0 at g = 0.
  - (ii) The observable non-conservation, max_t |⟨O⟩(t) − ⟨O⟩(0)| on
    [0, 10], has log-slopes vs g in [0.8, 1.2], and is < 1e-12 at
    g = 0.
  - Frozen consequence: C_cons forces universality exactly for any
    g ≠ 0. But the violation it forbids has strength ∝ g, detectable
    only on timescales ~1/g, and vanishes continuously at the endpoint.
    The g → 0 "singularity" is a property of treating C_cons as an
    exact constraint, not a physical discontinuity.

## 2. OUTCOME RULE (frozen, mechanical)

- **Genuinely decoupled sectors:**
  - DERIVED only if some earned element, or the supplied gauge
    structure (L-G class I), forces ε_A = ε_B.
  - If the L-C survivor passes all of them and L-G class I shows no
    forcing: **IRREDUCIBLE INPUT**.
- **Exchanging sectors:** if L-G class II forces and L-D(ii) shows that
  a dynamical probe with non-conserved components creates exchange:
  **DERIVED-IN-CLASS, conditional on the supplied gauge structure.**
- **Overall:** **CLASS-SPLIT** if both hold, with the residual named
  exactly: *whether every sector couples to a dynamical probe through
  exchange-carrying (non-conserved) components.* That is supplied.
- **g → 0:** recorded as continuous. The forcing is exact for g ≠ 0
  but operationally ∝ g.

## 3. CONTROLS

- Halt-grade: the universal-probe Δ, since an exact time rescaling
  must give zero.
- Halt-grade: the L-C C_cons commutator.
- Halt-grade: the clock-only probe's [H_A, H_full] = 0 (exact even
  under oscillator truncation, since H_A acts on A alone).
- Seed 20260925.
- The ladder models, the discriminator and gram_psd are reused
  verbatim from the validated S4-1 instrument.

## 4. DELIVERABLES AND STOP

1. `calc/u1_universality.py` (pure stdlib; emits
   `U1_UNIVERSALITY_RESULT.json`, sha-hashed).
2. `U1_UNIVERSALITY_VERDICT_01.md` and a closing comment on Issue #2.
3. **HARD STOP after the universality verdict.**
