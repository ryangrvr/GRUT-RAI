# APPENDIX H — TEMPERATURE SELECTION AND FIRST FLUCTUATION CONSEQUENCE

**Date:** 2026-03-27
**Status:** AUDIT COMPLETE — partial selection achieved; first non-circular prediction derived
**Executive determination:** `temperature_selectable_conditionally_not_uniquely`
**Classification basis:** Appendix D inheritance + three new selection criteria

---

## 1. QUESTIONS BEING ANSWERED

**Task 2 (Temperature Selection):** Can temperature be SELECTED, not just defined? Is there a
GRUT-native criterion that privileges one temperature candidate over the others,
without importing external physics not already in the GRUT framework?

**Task 3 (First Fluctuation Consequence):** Is there a constrained form, required scaling, or
necessary incompatibility that acts as a quantum-side discriminator with real bite?

---

## 2. INHERITED TEMPERATURE CANDIDATES

From Appendix D (`thermodynamic_sector.py`), four candidates were identified. This appendix
adds a fifth derived from the first law:

| Candidate | Formula | GRUT-native | Value (30 M_sun) | T/T_H |
|-----------|---------|-------------|-----------------|-------|
| T_structural | ℏω₀/k_B | YES | ~1.35×10⁻⁷ K | ~65.3 |
| T_dissipation | ℏω₀/(Q·k_B) | YES | ~2.24×10⁻⁸ K | ~10.9 |
| T_1stlaw | c²/(k_B·dS/dM) | YES* | ~1.85×10⁻⁸ K | ~9.0 |
| T_surface_gravity | ℏκ_eff/(2π·k_B) | NO | — | — |
| T_hawking | ℏc³/(8πGMk_B) | NO (imported) | ~2.06×10⁻⁹ K | 1.0 |

*T_1stlaw is derived entirely from GRUT quantities (R_eq = r_s/3, E = Mc²) but requires an
entropy ansatz (S = πR_eq²/l_P²).

**Key structural relation:**
```
T_structural = Q × T_dissipation    (Q = β_Q/α_vac = 6, GRUT-locked)
T_1stlaw     = 9 × T_Hawking        (derived below; ≈ 0.83 × T_dissipation)
```

---

## 3. THREE SELECTION CRITERIA

### Criterion 1 — FDT Inversion

**Formula:**
```
S_FF(ω₀) = 2k_B · T · Im[χ(ω₀)] / ω₀
```

Inverting for T requires the noise power spectrum S_FF(ω₀) — the amplitude of fluctuations
in the gravitational drive at the barrier frequency.

**Verdict: BLOCKED**

S_FF(ω₀) requires knowledge of the quantum state of the GRUT interior. This is one of the
hard Appendix C blockers. The classical ODE system (dM_drive/dt = ...) does not supply
fluctuations — it gives a deterministic trajectory. Without the quantum state, FDT inversion
cannot proceed.

---

### Criterion 2 — KMS Periodicity (Thermal Time Identification)

**Physical idea:** In a KMS (Kubo-Martin-Schwinger) thermal equilibrium state at temperature T,
correlation functions are periodic with imaginary-time period β = ℏ/(k_B·T). This period is the
"thermal time." If the memory relaxation timescale τ_local IS the thermal time, then:

```
τ_local = ℏ/(k_B · T_KMS)
T_KMS = ℏ/(k_B · τ_local) = ℏω₀/k_B = T_structural
```

(using the structural identity ω₀·τ_local = 1 from Appendix G).

**Verdict: CONDITIONAL**

This selects **T_structural** but requires the GRUT interior state to be a KMS thermal
equilibrium state. Establishing this requires:
- Proving the GRUT interior is at thermodynamic equilibrium.
- Identifying the physical bath that thermalizesthe interior.
- Showing the equilibrium is stable.

All three are blocked by Appendix C. However, this is the most natural candidate for
eventual selection: if equilibrium is ever established, T_structural is the unique result
of the KMS condition combined with the structural identity ω₀·τ_local = 1.

---

### Criterion 3 — First-Law Self-Consistency

**Setup:** The first law of thermodynamics requires dE = T·dS. With:
```
  E = M · c²                          (rest mass energy)
  S = π · R_eq² / l_P²               (area law at the GRUT endpoint)
```

The first law uniquely determines:
```
  T_1stlaw = ∂E/∂S = c² / (k_B · dS/dM)
```

**Computing dS/dM:**
```
  S = π · R_eq² / l_P²
    = π · (r_s/3)² / l_P²
    = π · (2GM/(3c²))² / l_P²

  dS/dM = 8π · G²M / (9c⁴ · l_P²)

  T_1stlaw = c² / (k_B · 8πG²M/(9c⁴l_P²))
           = 9c⁶ · l_P² / (8πG²M · k_B)
           = 9ℏc³ / (8πGMk_B)    [using l_P² = ℏG/c³]
           = 9 · T_Hawking
```

**This is an exact result** — T_1stlaw = 9·T_Hawking for any mass.

**Verdict: VIABLE_WITH_ASSUMPTIONS**

T_1stlaw selects a unique temperature using NO quantum-state input (no Appendix C blocker).
But it requires:
1. E = Mc² is the appropriate energy (not an ADM mass or binding energy correction).
2. S = πR_eq²/l_P² is the correct entropy (area proxy, not microstate count).
3. No work terms (the barrier does no thermodynamic work at the endpoint).

None of these three is derived from first principles in GRUT. Assumptions (1) and (2) are
standard in the literature; assumption (3) is not verified.

**T_1stlaw compared to other candidates:**
- T_1stlaw ≈ 0.827 × T_dissipation
- T_1stlaw ≈ 0.138 × T_structural
- T_1stlaw = 9 × T_Hawking (exact)

T_1stlaw lies between T_Hawking and T_dissipation, but is not equal to either.

---

## 4. THE FIRST NON-CIRCULAR FLUCTUATION CONSEQUENCE

### 4.1 The Prediction

Define the **first-law ratio**:
```
  R = k_B · T_diss · (dS/dM) / c²
```

This measures how well T_dissipation satisfies the first law with endpoint entropy. Substituting:

```
  T_diss = ℏω₀/(Q·k_B)
  ω₀ = 3√3·c³/(2GM)          [derived from R_eq = r_s/3 and ω₀ = sqrt(β_Q·GM/R_eq³)]
  dS/dM = 8πG²M/(9c⁴l_P²)
  l_P² = ℏG/c³

  R = k_B · (ℏω₀/Qk_B) · 8πG²M/(9c⁶·ℏG/c³) / c²
    = ω₀ · 8πGM/(9Qc³)
    = [3√3·c³/(2GM)] · 8πGM/(9Qc³)
    = 8π · 3√3 / (18Q)
    = 4π√3 / (3Q)
```

**For Q = 6 (canonical GRUT):**
```
  R = 4π√3/18 = 2π√3/9 ≈ 1.209
```

### 4.2 Why This Is Non-Circular

R is computed from:
- T_dissipation (which uses Q = β_Q/α_vac and ω₀ = sqrt(β_Q·GM/R_eq³))
- The endpoint entropy (which uses R_eq = r_s/3)

T is NOT an input — T is the output that makes R = 1. The ratio R = 1.209 ≠ 1
means T_dissipation "overshoots" the first-law temperature by 20.9%.

If someone measures the GRUT endpoint temperature externally (e.g., from a future
observable), they can test whether T_obs = T_diss or T_obs = T_1stlaw = T_diss/R.
This is a genuine discriminating prediction.

### 4.3 Mass Independence

R = 4π√3/(3Q) depends only on Q = β_Q/α_vac — not on M, G, ℏ, c, or k_B separately.

| Parameter | Dependence | Status |
|-----------|-----------|--------|
| R | α_vac, β_Q only | mass-independent |
| T_dissipation | ∝ 1/M | mass-dependent |
| T_1stlaw | ∝ 1/M | mass-dependent |
| R = T_diss/T_1stlaw | dimensionless | mass-independent |

**Consequence:** The ratio T_dissipation/T_1stlaw = R = 2π√3/9 ≈ 1.209 is the same
for any black hole mass. If either T can be measured, the other is predicted by GRUT.

### 4.4 FDT Noise Floor (Conditional)

With T_dissipation and the structural identity ω₀·τ_local = 1, the FDT gives:
```
  S_classical(ω=0) = 2k_B · T_diss · τ_local
                   = 2 · (ℏω₀/Q) · (1/ω₀)      [using k_B·T_diss = ℏω₀/Q]
                   = 2ℏ/Q
                   = ℏ/3    (for Q=6)
```

This is a **dimensionful prediction** for the zero-frequency noise floor of the memory
field, conditional on:
- The interior bath being physical (not just a structural observation).
- The classical FDT applying (not the quantum version).
- T_dissipation being the correct temperature.

If these conditions hold, the noise floor S(0) = ℏ/3 (in units where the bath is
properly normalized) is independent of mass and BH parameters.

---

## 5. WHY T_STRUCTURAL AND T_DISSIPATION CANNOT BE DISTINGUISHED

T_structural = Q × T_dissipation, with Q = β_Q/α_vac = 6 (a GRUT-locked parameter).
No GRUT-native criterion distinguishes them without external input:

- **FDT:** Would select one IF the fluctuation amplitude S_FF(ω₀) is known (blocked by Appendix C).
- **First law:** Selects T_1stlaw ≈ 0.83·T_dissipation, which is neither T_structural nor T_dissipation.
- **KMS:** Would select T_structural IF the state is thermal (blocked by Appendix C).
- **Dimensional analysis:** Both are proportional to ℏω₀/k_B; the difference is only the factor Q.

The factor Q = 6 is the ambiguity: it encodes the ratio of "energy per mode" (T_structural)
to "energy dissipated per cycle" (T_dissipation). Distinguishing these requires knowing
whether the relevant thermal energy is the bare mode energy or the dissipated cycle energy.
In a quantum damped oscillator, the two are related by the Q-factor — but selecting one
requires a physical argument about what "temperature" means in this context.

---

## 6. EXECUTIVE DETERMINATION

> **`temperature_selectable_conditionally_not_uniquely`**

1. **FDT inversion:** BLOCKED (quantum state required — Appendix C).

2. **KMS periodicity:** CONDITIONAL — selects **T_structural** if the interior is a KMS
   thermal state. This is the strongest candidate for eventual selection.

3. **First law self-consistency:** VIABLE_WITH_ASSUMPTIONS — selects **T_1stlaw = 9·T_Hawking
   ≈ 0.83·T_dissipation** without quantum-state input.

4. **First non-circular prediction:** R = 2π√3/9 ≈ 1.209 (mass-independent first-law ratio).
   This is the first dimensionless GRUT prediction that constrains the thermodynamic sector
   without circular dependence on the temperature choice.

5. **Conditional noise floor:** S(0) = ℏ/3 (for Q=6), if the interior bath is physical
   and classical FDT applies.

---

## 7. SAFE AND UNSAFE CLAIMS

### Safe Claims

1. T_1stlaw = 9·T_Hawking is the unique temperature selected by the first law
   with E = Mc² and S = πR_eq²/l_P². It uses no quantum-state input.

2. T_dissipation does NOT exactly satisfy the first law with endpoint area entropy:
   R = k_B·T_diss·(dS/dM)/c² = 2π√3/9 ≈ 1.21 ≠ 1.

3. R = 2π√3/9 is mass-independent — it is the same for any BH mass. It depends only
   on Q = β_Q/α_vac = 6 and the endpoint structure.

4. T_structural and T_dissipation differ by exactly Q = 6 (a GRUT-locked parameter).
   No GRUT-native criterion distinguishes them without quantum-state input.

5. The KMS criterion would select T_structural IF the interior state is a KMS thermal
   equilibrium state — this is conditional on Appendix C resolution.

6. The FDT noise at ω = 0 is S(0) = 2ℏ/Q = ℏ/3 (for Q=6) when using T_dissipation,
   conditional on the interior bath being physical and classical FDT applying.

### Unsafe Claims

1. Any specific temperature is proven correct.
2. T_dissipation satisfies the first law (it gives R ≈ 1.21, not 1.0).
3. T_structural is the KMS temperature without proving the state is thermal.
4. The first-law selection proves the endpoint area entropy is correct.
5. The FDT noise floor is a derived prediction (it is conditional on three assumptions).

---

## 8. INHERITED CLASSIFICATIONS (UNCHANGED)

- **Appendix D:** `thermodynamic_sector_partially_consistent` — UNCHANGED.
  The selection audit refines the Appendix D picture but does not resolve the
  temperature ambiguity. T_1stlaw is a new selection-viable candidate, but the
  entropy ansatz it requires is the same proxy as before.

- **Appendix E:** `locally_consistent_globally_underdetermined` — UNCHANGED.

---

## 9. CODE ARTIFACTS

| File | Description |
|------|-------------|
| `grut/temperature_selection_audit.py` | Three selection criteria, first-law analysis, fluctuation consequence |
| `tests/test_temperature_selection_audit.py` | 77 tests, all passing |

**Key numeric results (30 M_sun, mass-independent where noted):**

| Result | Value | Mass-independent? |
|--------|-------|-------------------|
| T_1stlaw/T_Hawking | 9.000 (exact) | NO — both ∝ 1/M |
| R = T_diss/T_1stlaw | 1.2090 = 2π√3/9 | YES |
| T_structural/T_dissipation | 6.0 (= Q) | YES |
| FDT noise S(0) = 2ℏ/Q | ℏ/3 | YES (conditional) |
