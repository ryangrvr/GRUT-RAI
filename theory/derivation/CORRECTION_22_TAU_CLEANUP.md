# Correction #22 — τ-cleanup: separating τ₀ from τ_micro

**Date:** 2026-04-30
**Status:** Dimensional bug CLOSED. Relation derivation OPEN (sharper question).
**Roadmap:** v8→v2 deposit, Priority 1.

---

## TL;DR

The framework was conflating two physically distinct relaxation timescales of the responsive vacuum under one symbol (τ₀). The pre-correction formula `T_c = 1/(τ₀ × k_B)` was dimensionally invalid — units K/(J·s), not K — and the "v9 natural-units convention" defense did not survive a proper natural-units check.

**Resolution.** Introduce `τ_micro ≡ ℏ/(k_B × T_c) ≈ 1.396×10⁻¹⁹ s` as a separate constant in the thermal sector, anchored empirically by the cosmological-chronology pin T_c = 54.7 MK at t ≈ 1 hour post-Big Bang. The SI-correct formula `T_c = ℏ/(τ_micro × k_B)` recovers 54.7 MK exactly. The 34-orders-of-magnitude separation between τ₀ (gravitational, 41.9 Myr) and τ_micro (thermal, ~10⁻¹⁹ s) is now named explicitly. The question of whether τ₀ and τ_micro are linked by a derivable relation, identified with a known timescale, or fundamentally independent becomes a sharp open question (`tau_zero_to_tau_micro_relation_open_question`, Ch 12).

| | Before | After |
|:---|:---|:---|
| T_c formula | `1/(τ₀ × k_B)` (units K/(J·s) — invalid) | `ℏ/(τ_micro × k_B)` (SI-correct) |
| T_c numerical value | 54.7 MK (by dimensionally invalid coincidence) | 54.7 MK (by definition of τ_micro from T_c anchor) |
| τ scales in framework | One (τ₀), used for both gravity and thermal | Two (τ₀ and τ_micro), with explicit naming |
| Free-parameter framing | "Zero free parameters in the predictive core" | "Zero in gravitational core; one anchored in thermal sector" — pending relation derivation |
| Affected predictions | None — load-bearing predictions all use τ₀ unambiguously | None changed — only T_c provenance |
| `test_T_c_is_54p7_MK` | Passes via numerical coincidence | Passes via SI-correct formula (pinned) |
| New tests | — | 7 in `test_closure_protocol.py::TestCanonicalConstants` |

---

## What was wrong (re-stated for posterity)

Pre-Correction-#22, `closure_protocol.py` defined:

```python
T_C_KELVIN: float = 1.0 / (TAU_0_SEC * K_B)
```

This produces a number ≈ 5.47×10⁷ that the docstring labels as a temperature in K. But dimensionally:

```
1/(s × J/K) = K/(J·s) ≠ K
```

The "v9 natural-units convention (ℏ=1)" defense in the same docstring claimed this was fine because in natural units ℏ = 1 and time has units of inverse-energy. Audit check (`T_C_PROVENANCE.md`) found this defense does not hold:

```
τ₀ in natural units (eV⁻¹) = τ₀ [s] / ℏ [eV·s]
                            = 1.32×10¹⁵ / 6.58×10⁻¹⁶
                            = 2.0×10³⁰ eV⁻¹
1/τ₀_nat                    = 5.0×10⁻³¹ eV
                            = 5.78×10⁻²⁷ K  (correct SI conversion)
```

The natural-units formula `T_c = 1/τ₀` (with ℏ = k_B = 1) gives **5.78×10⁻²⁷ K**, NOT 54.7 MK. The 34-orders-of-magnitude gap means natural units does not rescue the value.

The 54.7 MK value emerges *only* by treating the pure SI numerical operation `1/(1.32×10¹⁵ × 1.38×10⁻²³)` as a temperature. That is dimensionally invalid.

Cross-check: `MU_0_EV = HBAR / TAU_0_SEC / E_CHARGE` is computed correctly (with ℏ) in the same file, gives ~10⁻³¹ eV ≈ 5.78×10⁻²⁷ K when expressed as a temperature — contradicting the "T_c = 54.7 MK" line right next to it.

**Audit verdict (T_C_PROVENANCE.md):** the framework's prose, V7 §0.5, V7 §22, and the cosmological narrative *require* T_c at MK scale (T at t ≈ 1 h post-BB ≈ 10⁸ K), but no formula derivable from τ₀ produces 54.7 MK in either SI or natural units. The framework was using one symbol for two distinct physical scales.

---

## What the resolution does

### 1. Empirical anchor

```python
T_C_KELVIN_CANONICAL: float = 5.47e7
"""Empirical anchor for the metric-memory transition temperature.
Source: standard-cosmology temperature at t ≈ 1 hour post-Big Bang."""
```

This is the cosmological-chronology pin. It comes from standard radiation-era thermodynamics, not from GRUT — the framework adopts it as input, the same way `H_0` and the Bullet Cluster offset are inputs.

### 2. Microscopic τ defined from the anchor

```python
TAU_MICRO_SEC: float = HBAR / (K_B * T_C_KELVIN_CANONICAL)
# ≈ 1.396 × 10⁻¹⁹ s
```

This is the SI-correct dual of T_c. Femtosecond-scale, comparable to atomic-transition timescales. **Distinct** from τ₀ = 41.9 Myr.

### 3. T_c recomputed via SI-correct formula

```python
T_C_KELVIN: float = HBAR / (TAU_MICRO_SEC * K_B)
T_C_MK: float = T_C_KELVIN / 1e6
```

By construction, `T_C_KELVIN == T_C_KELVIN_CANONICAL` exactly. The `test_T_c_is_54p7_MK` pin (5% tolerance, value 54.7) is preserved without modification.

### 4. Convention declaration in the module docstring

The module docstring now lists τ₀ and τ_micro as **separate** constants, explains the two-τ-scale convention, and points to this correction document.

### 5. Registry updates

- New claim `tau_micro_thermal_scale` (Ch 8, anchored tier): tracks τ_micro with its empirical anchor and tests.
- `t_c_thermal_transition` (Ch 8) updated: formula now references τ_micro.
- Old `t_c_provenance_inconsistency_open_negative` retired; replaced by:
  - `t_c_provenance_inconsistency_resolved` (Ch 12, meta tier) — documents the closure.
  - `tau_zero_to_tau_micro_relation_open_question` (Ch 12, open_negative tier) — sharper question that remains.

### 6. Ledger update

- New ledger entry `tau_zero_to_tau_micro_relation_open_question` replaces the old `t_c_provenance_inconsistency_open_negative` entry. Closure paths (a)/(b)/(c) are research-tier; path (d) — BBN-mediated bridge — was already FALSIFIED by `bbn_thermal_buffer_negligible` and is recorded as ruled out.

### 7. Tests

7 new tests in `tests/foundation/test_closure_protocol.py::TestCanonicalConstants`:
- `test_T_c_canonical_anchor_is_5p47e7_K`
- `test_tau_micro_is_femtosecond_scale`
- `test_T_c_formula_is_SI_correct`
- `test_T_c_recovered_value_matches_canonical`
- `test_two_tau_scales_separated_by_thirty_plus_orders`
- `test_T_c_old_dimensionally_invalid_formula_NOT_used`

Plus the existing `test_T_c_is_54p7_MK` is preserved unchanged. All 64 tests in `test_closure_protocol.py` and `test_thermal_transition.py` pass after the change.

---

## What this resolution does NOT do

It does NOT:
- Derive τ_micro from τ₀ or any other GRUT primitive. The 34-orders-of-magnitude separation is unexplained.
- Change any τ₀-bearing prediction. Λ_grav (decoherence plateau), n_g(ω) (refractive index), the τ₀ ↔ Ω_Λ bridge, the cluster-merger v×τ₀ scaling, the H₀ = 1/(S × τ₀) cosmic-baseline relation — all use τ₀ unambiguously and stand intact.
- Update prose in `theory/GRUT_TOE.md`. The auto-rendered chapters will pick up the new claim IDs and updated registry entries on the next render pass; explicit prose revisions for Ch 1, Ch 2, Ch 4, Ch 9, Ch 13.3-13.4, Appendix C are deferred to the document-composition session.
- Resolve the consequence for the framework's "zero free parameters in the predictive core" framing. Under the two-scale convention this is INCOMPLETE — τ_micro is an additional anchored input. The honest framing is "zero in gravitational core; one anchored in thermal sector," and whether this constitutes a credibility loss (versus "zero free parameters") is a posture question for the v2 deposit. The registry treats it as open via `tau_zero_to_tau_micro_relation_open_question`.

---

## Closure paths for the relation question

Per the new open question's notes, four paths to closure:

1. **Derive τ_micro from CTP plasma dynamics.** The v9 noise kernel evaluated at the BBN-era thermal scale might produce τ_micro as a thermal-decoupling timescale. This is research-tier work, plausibly connected to `n_g_omega_cosmological_covariance_open_question` (#9) since both involve cosmological-plasma physics not yet formalized in GRUT.

2. **Identify τ_micro with a known atomic/nuclear timescale.** Dimensional analysis: ℏ/(k_B × 54.7 MK) ≈ 1.4 fs corresponds to ~5 keV photon energies. Soft-X-ray scale, atomic-inner-shell-transition timescale. Whether this is *the* relevant atomic process for vacuum-microstate thermal decoupling needs first-principles motivation.

3. **Acknowledge two independent inputs.** The honest-negative outcome: τ₀ and τ_micro are fundamentally separate empirically anchored quantities. The framework's "zero free parameters" claim downgrades to "zero in gravitational core; one anchored in thermal sector." This would be a meaningful but survivable credibility loss — comparable to MOND's a₀ anchoring.

4. **BBN-mediated bridge (FALSIFIED).** Path tested via the BBN thermal-buffer calculation; result was ten orders of magnitude too small to provide any cosmological-narrative bridge between the scales. Falsified, recorded; ruled out.

The v2 deposit's posture statement should reflect this honestly: the framework currently has *two* empirically anchored timescales in the predictive core, with a sharp open question about their relation. The dimensional inconsistency that motivated this correction is closed; the structural question remains.

---

## Strategic observation

This correction is the cleanest possible Priority-1 win for the v8→v2 roadmap: a foundational provenance issue the framework's own documentation flagged is now explicitly resolved, with no test regressions and no change to the framework's load-bearing predictions. The framework's credibility-honesty posture improves: instead of one number computed via an invalid formula, two named scales with an explicit open question.

The natural Priority-2 follow-on (deriving Φ_μν from S_CTP) is the biggest gravity gate. With the τ-cleanup landed, the framework's foundational layer is dimensionally clean and the derivation of Φ_μν starts from a consistent baseline.

---

## Files touched

| File | Change |
|:---|:---|
| `grut/foundation/closure_protocol.py` | New constants `T_C_KELVIN_CANONICAL`, `TAU_MICRO_SEC`; SI-correct `T_C_KELVIN`; module docstring updated with two-τ-scale convention |
| `tests/foundation/test_closure_protocol.py` | +7 new tests in `TestCanonicalConstants`; existing `test_T_c_is_54p7_MK` preserved |
| `grut/toe/registry.py` | New `tau_micro_thermal_scale` claim; updated `t_c_thermal_transition`; replaced `t_c_provenance_inconsistency_open_negative` with `t_c_provenance_inconsistency_resolved` (meta) and `tau_zero_to_tau_micro_relation_open_question` (open_negative) |
| `grut/toe/ledger.py` | Ledger entry replaced to track the relation-derivation question post-resolution |
| `grut/derived/cosmology/thermal_transition.py` | Module docstring updated; `__main__` block reports both τ scales |
| `grut/derived/cosmology/sm_crystallization_schedule.py` | Quarantine notice updated to point at the new claim ID |
| `grut/derived/cosmology/bbn_thermal_buffer.py` | Connection-to-framework note updated |
| `grut/derived/cosmology/genesis_noise_kernel.py` | Two cross-references updated |
| `theory/foundations_audit/T_C_PROVENANCE.md` | Closing addendum (Correction #22 result) |
| `theory/derivation/CORRECTION_22_TAU_CLEANUP.md` | This file |

---

*D. Ryan Grover, with Claude Code, 2026-04-30. Same discipline pattern as Corrections #11 (τ_0 audit) and #21 (TJI Phase-0.5).*
