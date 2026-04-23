# TJI Phase-1 Calculation Plan — Euclidean S⁴ Evaluation

**Status:** Phase-0 infrastructure complete. Phase-1 (curved-space evaluation) not started.
**Audience:** curved-space QFT specialist (Bei-Lok Hu, Enric Verdaguer, Albert Roura, or equivalent), plus any successor automated pipeline that attempts the calculation.
**Purpose:** Specify the exact integral, propagator form, boundary conditions, and Laurent-extraction protocol required to upgrade V8 §12's `R` from CONDITIONAL to COMPUTED.

---

## 1. The target integral

The 3-propagator 2-loop massless sunset integral, in Tarcer notation:

    TJI[D, k², {{1,0},{1,0},{1,0}}]

on Euclidean S⁴ (the compact 4-sphere, Wick-rotated de Sitter) with Hartle-Hawking thermal state at Gibbons-Hawking temperature T_GH = H_inf / (2π).

Target rational (the structural claim we are testing):

    ε⁰ finite rational = −100 = −(Σ_SM Y²)²

per V7 §26.2.6 / Correction #16, as the curved-space signature of the Gibbons-Hawking conformal-factor instability combined with SM hypercharge species-sum weighting.

If the calculation yields −100: V8 §12 upgrades from CONDITIONAL to fully COMPUTED, Ω_Λ = 0.6886 becomes a parameter-free consequence, and the framework closes on its core cosmological prediction.

If the calculation yields any other rational: the structural claim still survives at a weaker level (magnitude and sign arguments are independent) but the specific integer identification requires revision.

---

## 2. Phase-0 infrastructure already delivered

### Flat-space symbolic pipeline (`grut/derivation/tji/flat_space.py`)

The 2-loop T_2 reduction prefactor × master-integral gamma-ratio is implemented symbolically in pure Python/SymPy. Exact Laurent expansion around D = 4 − 2ε yields:

| Coefficient | Exact rational (raw scheme) |
|:---|:---|
| 1/ε² | **−1/64** |
| 1/ε (rational part, γ_E → 0) | **−25/384** |
| ε⁰ (pure rational: γ_E → 0, π² → 0, ζ(3) → 0) | **−541/2304** |

Pinned by regression tests `tests/derivation/tji/test_flat_space.py`.

### The FeynCalc reference value

V7 §26.2.3's FeynCalc run reported the ε⁰ rational as **7/4** in a specific MS-bar convention. The raw-scheme value −541/2304 differs from 7/4 by scheme-dependent finite renormalization terms (Γ(1+ε) per-loop absorption, (4π)^ε absorption, the 1/ε̄ definition).

**Reconciliation to the FeynCalc 7/4 is Phase-0.5**: identify the exact MS-bar / Γ-absorption convention FeynCalc used in the V7 session, implement it in the SymPy pipeline, and verify the pipeline reproduces 7/4 exactly. This is a bounded symbolic algebra task (~1–2 sessions) that should land before Phase-1 begins, so the curved-space calculation is measured against a scheme-matched flat-space baseline.

### Allen-Jacobson interface stub (`grut/derivation/tji/allen_jacobson.py`)

The Phase-1 interface is pinned. Two functions:

- `s4_propagator(Z, D, m_squared, H_inf)` — scalar propagator on Euclidean S⁴.
- `tji_on_s4(D, k_squared, indices, H_inf)` — curved-space analog of TJI.

Both currently raise `Phase1Pending`. The interface spec is locked by regression tests; any Phase-1 implementation must preserve function names, argument lists, and target rational (−100).

---

## 3. Phase-1 task — the curved-space evaluation

### 3.1 Propagator

Allen-Jacobson 1986 (Commun. Math. Phys. 103, 669) gives the scalar propagator on a maximally symmetric space of dimension D:

    G(Z) = [Γ(h₊) Γ(h₋) / ((4π)^(D/2) Γ(D/2))] · ₂F₁(h₊, h₋; D/2; (1+Z)/2)

where Z = cos(H_inf · d(x, x')) is the chordal distance (Z = 1 coincident, Z = −1 antipodal), and

    h± = (D−1)/2 ± √[(D−1)²/4 − m²/H_inf²]

For a massless scalar (m² = 0) in D = 4 − 2ε: h₊ = 3 − 2ε, h₋ = 2ε.

**Implementation note.** The ₂F₁ with h₋ → 0 is a degenerate case requiring careful analytic handling — the log divergence at short distance and the IR structure on S⁴ both surface here. Mathematica's `Hypergeometric2F1` handles these cleanly; SymPy's does not always. Specialist tooling (xAct for tensor algebra, HypExp for ε-expansion of hypergeometrics) may be required.

### 3.2 2-loop sunset composition

The 2-loop TJI sunset has three propagators arranged in a sunset topology:

    TJI_S⁴(x, x') = ∫_{S⁴} dy √g(y) [G(Z(x,y))]³ × [propagator structure for internal lines]

with the Tarcer indices {{1,0},{1,0},{1,0}} meaning each propagator is raised to the first power with no irreducible numerator insertions.

By S⁴ isometry, the double position-space integral reduces to a single integral over the angle between x and y (or equivalently over Z). The problem is therefore one-dimensional in the radial integration variable.

### 3.3 Hartle-Hawking thermal state

The Euclidean continuation of de Sitter to S⁴ is the Hartle-Hawking vacuum, which is automatically thermal at T_GH = H_inf/(2π). Concretely: the propagator on the compact S⁴ with standard boundary conditions IS the HH thermal propagator — no separate thermal average is required.

However, the CTP forward/backward structure requires care:

- The forward branch sees the vacuum anomaly coefficient (C_Final in V7 notation).
- The backward branch sees the thermally-corrected coefficient (C_Cosmo).
- Their ratio R = |C_Cosmo / C_Final| = 1.15428 (V7 §26.2.1).

On S⁴ with HH state, both branches are implemented by the same integral with opposite iε prescription. The sign flip between C_Final and C_Cosmo is tracked through the Γ(2ε − 1) expansion (sign of the first-pole residue).

### 3.4 Laurent expansion and ε⁰ extraction

After S⁴ integration, the result is a Laurent series in ε = (4−D)/2. Extract:

    c₋₂ : double pole (UV subtraction constant)
    c₋₁ : single pole (scheme-dependent)
    c₀  : finite part — the pure rational (γ_E, π², log(4π), ζ(3), log(H_inf²/μ²) absorbed by MS-bar)

Assert c₀ = −100 exactly.

### 3.5 Reconciliation with flat-space limit

As a sanity check: the flat-space limit (H_inf → 0, Z → 1) must reproduce the Phase-0 flat-space result in the same MS-bar scheme. This is the Phase-0.5 scheme-matching item — once Phase-0.5 lands the raw-scheme 7/4 reconciliation, the flat-space limit of Phase-1 is measured against 7/4.

---

## 4. Anticipated obstacles (Phase-0 identified)

### 4.1 SymPy coverage limit

SymPy's symbolic hypergeometric engine handles ₂F₁ with generic parameters but can struggle when parameters approach integer values (the h₋ → 0 limit in massless D = 4 is exactly this regime). Expected outcome: SymPy produces a result but may leave unevaluated ₂F₁ symbols or fail to simplify to a closed form. Workaround: switch to Mathematica + HypExp for the Laurent expansion of the hypergeometric, then import the resulting series back into SymPy for the combination with the prefactor.

### 4.2 Species-sum assembly

The target −100 = −(Σ_SM Y²)² comes from two factors:

    (Σ_SM Y²)² = 10² = 100

with Σ_SM Y² = 10/3 per generation, 3 generations = 10. The squared form arises from the 2-loop sunset topology (species sum × species sum through the sub-insertion). The Phase-1 calculation must produce the factor of 100 via the species sum, not by hand.

### 4.3 The −1 sign (Gibbons-Hawking instability)

The MINUS sign in −100 is the conformal-factor instability (negative kinetic term for the Weyl mode on Euclidean gravity; V7 §26.2.3a and Correction #16). On S⁴ this manifests through the Γ(2ε − 1) pole residue having the "wrong" sign compared to the corresponding flat-space term. The sign tracking in the calculation is as important as the magnitude.

### 4.4 Scheme ambiguity

The ε⁰ rational depends on the absorption scheme for Γ(1+ε), (4π)^ε, γ_E, log(4π). The target −100 is asserted in the MS-bar convention GRUT uses throughout V7 §26.2. This convention must be made explicit and used consistently.

---

## 5. Verification protocol

When Phase-1 lands, the following tests must pass:

1. `tji_on_s4(D=4-2ε, k²=1, indices=((1,0),(1,0),(1,0)))` returns a SymPy expression with a Laurent expansion around ε = 0.

2. The ε^(−2) coefficient matches the flat-space double pole (within scheme-dependent finite renormalization) — provides a reality check that the curved-space calculation has the correct UV structure.

3. The ε⁰ coefficient, after standard MS-bar subtractions, equals `Fraction(-100, 1)` exactly.

4. The flat-space limit H_inf → 0 reproduces the Phase-0 flat-space result (MS-bar-matched after Phase-0.5).

5. The species-sum factor of 100 emerges from the hypercharge group-theoretic weighting, not from a manual prefactor.

All assertions are exact-rational, not float-approximate.

---

## 6. Decision protocol after Phase-1

### 6.1 Best case: c₀ = −100 exactly

V7 §26.2.6 / Correction #16 is confirmed at the level of the master-integral evaluation. V8 §12 upgrades from CONDITIONAL to COMPUTED. The Ω_Λ = 0.6886 prediction becomes parameter-free given v_EW and the SM field content. Publish as a companion to V7/V8 with the specialist as co-author.

### 6.2 Middle case: c₀ = some other rational

The structural claim (Gibbons-Hawking conformal-mode instability regulated by τ_0; V7 §26.2.3a) survives independently — it does not depend on the specific integer. The Correction #16 identification `−100 = −(Σ Y²)²` is weakened but the mechanism interpretation remains. V8 §12 stays CONDITIONAL but the conditionality is sharpened: "the rational is X, which is structurally Y, and differs from the hypercharge-squared identification by Z".

### 6.3 Worst case: the calculation cannot be closed

Phase-1 hits a specific technical obstacle that the pipeline cannot resolve (e.g., the hypergeometric has no closed-form Laurent expansion at the required order, or S⁴ integration produces non-convergent radial integrals). Document the obstacle precisely. The specialist outreach then has a concrete bounded question, not an open-ended one.

---

## 7. Reference material

- Allen, B. and Jacobson, T. (1986). "Vector two-point functions in maximally symmetric spaces." Commun. Math. Phys. 103, 669.
- Birrell, N. D. and Davies, P. C. W. (1982). *Quantum Fields in Curved Space*. Cambridge University Press.
- Gibbons, G. W. and Hawking, S. W. (1977). "Cosmological event horizons, thermodynamics, and particle creation." Phys. Rev. D 15, 2738.
- Anastopoulos, C. and Hu, B. L. (2013). "Gravitational decoherence of a quantum system." Class. Quantum Grav. 30, 165007. [V7's decoherence sector foundation.]
- V7 `theory/GRUT_V7_FULL.md` §26.2 — anomaly coefficient structure.
- V7 `theory/derivation/FEYNCALC_VERIFICATION_LOG.md` — flat-space reduction yielding 7/4 (Phase-0.5 reconciliation target).
- V7 `theory/derivation/MINUS_100_RESOLUTION.md` — the Gibbons-Hawking conformal-mode narrative for the −100 sign.
- V7 `theory/derivation/MINUS_100_FINAL_STATEMENT.md` — structural and numerical arguments for −100 = −(Σ Y²)².

---

## 8. Deliverable sequence

| Phase | Task | Status |
|:---|:---|:---|
| 0 | Flat-space SymPy pipeline, Laurent expansion, regression tests | **COMPLETE** (this session) |
| 0.5 | Reconcile raw-scheme −541/2304 to FeynCalc MS-bar 7/4 | PENDING (~1–2 sessions) |
| 1 | Allen-Jacobson S⁴ propagator implementation | NOT STARTED |
| 2 | 2-loop sunset composition on S⁴ | NOT STARTED |
| 3 | Laurent expansion and ε⁰ extraction | NOT STARTED |
| 4 | Verification: c₀ == Fraction(−100, 1) exactly | NOT STARTED |
| 5 | Write-up and specialist review | NOT STARTED |

Phase-0 closes here. Phase-0.5 may be attempted in-pipeline or handed to a specialist. Phases 1–5 require curved-space QFT specialist expertise.
