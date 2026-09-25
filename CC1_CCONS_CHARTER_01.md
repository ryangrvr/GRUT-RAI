# CC-1 — CAN C_cons BE DERIVED FROM EARNED STRUCTURE? CHARTER + PRE-REGISTRATION (frozen before evaluation)

**Date:** 2026-09-25 · **Authority:** GitHub Issue #2, owner comment
**5835662238**. FS-1 was accepted at recorded strength, with this
binding status: C_cons is an unresolved import and GeoInv is an
unresolved candidate, not absorbed into 𝒯.

**Target (owner, verbatim):** *Can the requirement that the constant
gravitational probe couple to a conserved local quantity be derived from
the already-earned structure (𝔠_full + access + G-2 geometry + the
established local-dynamics framework), rather than imposed as a
definition?*

**Outcomes:** DERIVED/SELECTED · CONSTRAINED BUT NONUNIQUE · CLASS-SPLIT ·
IRREDUCIBLE INPUT · FAILS/NULL.

**Required structure, and how this charter meets it:**
1. *A genuinely non-conservation-based selector battery, frozen.* No
   selector below mentions [O, H]. They are 𝔠_full, G-2 geometry
   (hop + resistance), intrinsic spectral shape, static-limit
   regularity, and positivity of probe-mediated influence.
2. *Non-conserved couplings that remain 𝔠_full-admissible and
   geometry-compatible are included*, so C_cons is attacked rather than
   assumed.
3. *"Conservation is dynamically necessary for stationary influence" is
   kept separate from "so the fundamental coupling must be conserved."*
   Leg L-S tests both.
4. *Both generic interacting and free/gapless sectors are tested.*
5. *No Noether smuggling.* Where conservation follows only from a
   supplied symmetry or field content, the dependency is reported
   (leg L-P).
6. GeoInv stays separate and unearned. Its satisfaction is recorded,
   never used as a selector.
7. The retained-sector choice stays separate.
8. ω⁷ occupancy only; GR-1 3D red; ℏ located; D = 4 TT/ξ, operator
   ordering and geometry selection fenced. Leg L-P uses D = 4
   propagator residues only as an algebraic positivity test. It does
   not address the TT/ξ channel or kinematics.

## 1. THE LEGS (frozen, predictions written before any number)

- **L-A (the counterexample battery: non-conserved couplings that
  survive every earned constant-level selector).**
  - **A1, free phonon ring (N = 20, FS-1's sector).** The mass
    modulation O_M = ½Σpᵢ² (pp₀ only).
    **Predictions:**
    - non-conserved (‖AJM_H − M_HJA‖ > 0);
    - 𝔠_full: H + hO_M is PSD (h = 0.05);
    - G-2 hop geometry unchanged (|d̂ − d| < 0.3 for d = 1..4);
    - static resistance R(0,8) unchanged (ratio 1 to 1e-12; the
      stiffness block is untouched);
    - **spectrally a unit change:** the normalized mode-frequency shape
      is unchanged to < 1e-12, because ω′ = √(1+h)·ω exactly (a mass
      change is a squeeze plus a time rescaling);
    - **static-limit regular:** the static susceptibility is extensive,
      with χ(N=40)/χ(N=20) ∈ [1.8, 2.2].
    - It also satisfies GeoInv. This is recorded only.
  - **A1′, the contrast.** The pinning modulation O_pin = ½Σuᵢ²
    (non-conserved) is **IR-singular**: χ(40)/χ(20) > 4 (predicted
    ~N³). It is excluded by static-limit regularity.
  - **A2, generic MFIM (L = 6).** O_X = ΣXᵢ. **Predictions:**
    non-conserved; ground-state Gram PSD (𝔠_full); interaction graph
    unchanged; static χ finite (a gapped finite system); normalized
    spectral shape changes by > 1e-4. Only the (unearned) Sel-4 would
    object to it.

  Frozen consequence: if O_M passes every earned constant-level
  selector, then **C_cons is not selected at the constant level**.
  Static regularity cuts only IR-singular couplings, which is
  CONSTRAINED-NONUNIQUE.
- **L-S (the owner's required separation: stationarity vs.
  fundamentality).**
  - (i) The driven-stationarity weight is D(O) = Σ over pairs with
    |E_m − E_n| > 1e-9 of |O_mn|², i.e. the spectral weight at nonzero
    frequency. It is tested on MFIM L = 6 against the commutator norm,
    for O ∈ {H, ΣXᵢ, ΣZᵢ, H²}. **Prediction (halt-grade identity):**
    D(O) = 0 ⇔ ‖[O, H]‖ = 0 for all four. Frozen consequence: "the
    probe must be stationary under driving" is **logically equivalent
    to C_cons**, a restatement. It adds no independent ground.
  - (ii) A constant probe needs no conservation to be stationary. In
    the ground state of H + hΣXᵢ, the two-time correlator depends only
    on the time difference (three pairs, equal to 1e-12).
  - (iii) **A blanket C_cons contradicts the program's own
    gravitational channel.** On the phonon ring, H's pair amplitude is
    exactly 0 (conserved). The geometric (T_xx, CP-1) vertex has
    nonzero dynamic weight Σ_k V_metric(k)² > 1e-6. Frozen
    consequence: C_cons can at most be **component-specific** (the
    clock/energy component). A blanket "the probe couples only to
    conserved quantities" would delete GR-1's channel.
- **L-P (the positivity route: can 𝔠_full force conservation, and at
  what price?).** Tested with probe-mediated exchange residues in D = 4
  (η = diag(−1, 1, 1, 1)) over 200 random real sources per case:
  - *Massless vector at null k* (Feynman numerator η): **conserved**
    sources give residue ≥ −1e-12, equal to the physical transverse
    sum |J_⊥|² to 1e-12. **Non-conserved** sources give min residue
    < −1e-3 (a negative-norm/ghost contribution, i.e. a 𝔠_full
    violation).
  - *Massless spin-2 at null k* (numerator ½(ηη + ηη − ηη)):
    **conserved** T (from the null space of k_μT^{μν}) gives residue
    ≥ −1e-12, equal to the physical helicity-±2 sum to 1e-10.
    **Non-conserved** T gives min < −1e-3.
  - *Massive vector (Proca, m = 1) and massive spin-2 (Fierz–Pauli,
    m = 1), on shell:* residue ≥ −1e-12 for **all** sources.

  Frozen consequence: 𝔠_full positivity forces source conservation
  **if and only if** the probe is a massless gauge field (covariant,
  with redundant polarizations). That field content is **supplied**,
  so C_cons is **reduced to it, not derived**: CLASS-SPLIT by probe
  field content, with the dependency reported. The conservation so
  obtained is *current* conservation (k_μT^{μν} = 0). Its
  zero-momentum time component gives S4-1's clock C_cons while leaving
  T_xx a non-conserved flux, which is consistent with L-S(iii).

## 2. OUTCOME RULE (frozen, mechanical)

- **Constant level:** if any non-conserved coupling passes every earned
  constant-level selector (𝔠_full, G-2 hop + resistance, static
  regularity), C_cons is **not selected**. If static regularity
  excludes some non-conserved couplings, that component is
  **CONSTRAINED-NONUNIQUE**.
- **Stationarity:** if the L-S(i) equivalence holds, recorded as a
  restatement (dependency), not a derivation.
- **Positivity route:** if the massless cases force conservation and
  the massive ones do not, the component is **CLASS-SPLIT by field
  content**, derivation conditional on the supplied massless-gauge
  content.
- **DERIVED/SELECTED** only if an earned selector excludes every
  non-conserved candidate with **no** supplied structure. Otherwise the
  overall verdict is **IRREDUCIBLE INPUT**, reduced to the named
  supplied structure.

## 3. CONTROLS

- Halt-grade: the L-S(i) identity.
- Halt-grade: the equality of covariant and physical residues for
  conserved sources.
- Halt-grade: the exact unit-change spectrum of O_M.
- Matched checks: FS-1's conserved H passes every selector trivially;
  S4-1's ΣXᵢ numbers are recomputed, not copied.
- Seed 20260925 for random sources.

## 4. DELIVERABLES AND STOP

1. `calc/cc1_ccons.py` (pure stdlib; emits `CC1_CCONS_RESULT.json`,
   sha-hashed).
2. `CC1_CCONS_VERDICT_01.md` and a closing comment on Issue #2.
3. **HARD STOP after the C_cons verdict.** No advance to universality,
   the retained sector or geometry selection.
