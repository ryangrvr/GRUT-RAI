# APPENDIX I — FIRST-LAW GAP AUDIT

**Date:** 2026-03-27
**Status:** AUDIT COMPLETE — all three candidate resolutions evaluated; gap confirmed structural
**Executive determination:** `gap_structural_no_external_free_parameter`
**Classification basis:** Appendix H inheritance + three resolution audits

---

## 1. QUESTION BEING ANSWERED

From Appendix H, the first-law ratio is:

```
R = k_B · T_diss · (dS/dM) / c² = 4π√3/(3Q) = 2π√3/9 ≈ 1.209
```

R ≠ 1. The first law (dE = T dS) is not satisfied simultaneously by T_dissipation and the
endpoint area entropy S_eq = πR_eq²/l_P². This appendix answers:

> **Is the gap fixed by (a) revising the entropy proxy, (b) revising the selected temperature,
> or (c) adding a missing work/memory term?**

---

## 2. SETUP: THE FIRST LAW AT THE GRUT ENDPOINT

The GRUT endpoint is defined by R_eq = r_s/3 (equivalently, C = 1/3 at the collapse barrier
activation point). The standard thermodynamic first law applied to a black-hole-like object
at this endpoint is:

```
dE = T dS    (no work terms, W = 0)
```

With:
```
  E = Mc²                       (rest energy)
  S = S_eq = π R_eq² / l_P²    (area-law entropy proxy)
```

The first law selects T_1stlaw = ∂E/∂S = c²/(k_B · dS/dM). Appendix H showed:

```
  T_1stlaw = 9 · T_Hawking
```

But the GRUT-native temperature candidate from the dissipative sector is:

```
  T_diss = ℏω₀ / (Q · k_B)
```

The ratio of these is the gap:

```
  R = T_diss / T_1stlaw = k_B · T_diss · (dS/dM) / c²
    = 4π√3 / (3Q) = 2π√3/9 ≈ 1.209
```

T_diss exceeds T_1stlaw by ~20.9%. The gap is the question for this appendix.

---

## 3. OPTION (c): MISSING WORK TERM

### 3.1 The Question

Does the modified first law dE = T dS + W (with W = work done by the barrier or memory
sector) restore R = 1?

### 3.2 Barrier Potential at Equilibrium

The barrier potential in the GRUT collapse sector takes the form:

```
V_Q(R) = -GM · ε_Q · r_s^β_Q / ((1 + β_Q) · R^(1+β_Q))
```

At the equilibrium endpoint R_eq = r_s · ε_Q^(1/β_Q), one can verify the exact identity:

```
ε_Q · (r_s/R_eq)^β_Q = ε_Q · ε_Q^(-1) = 1
```

Therefore:

```
V_Q(R_eq) = -GM · ε_Q · r_s^β_Q / ((1+β_Q) · R_eq^(1+β_Q))
           = -GM · [ε_Q · (r_s/R_eq)^β_Q] / ((1+β_Q) · R_eq)
           = -GM / ((1+β_Q) · R_eq)
           = -GM / (3 · r_s/3)           [using β_Q=2, R_eq=r_s/3]
           = -GM / r_s
           = -c²/2
```

**Key result: V_Q(R_eq)/c² = −1/2 exactly, for all M.**

This is mass-independent because the Schwarzschild relation r_s = 2GM/c² absorbs both G and M.

### 3.3 Mass Derivative of the Barrier Potential

```
V_Q(R_eq) = -c²/2  ∀M  →  dV_Q/dM = 0
```

The barrier does **zero thermodynamic work** for any quasi-static mass change δM.

### 3.4 Memory Sector Work at Equilibrium

The memory ODE is:

```
τ_eff dM_drive/dt + M_drive = a_grav
```

At the equilibrium endpoint, velocity V = 0. The gravitational drive a_grav is computed from
the barrier at rest. In the equilibrium state, dM_drive/dt = 0, so M_drive = a_grav (no
transient). Since the memory sector is dissipative (τ_eff > 0), all work done by the memory
field is dissipated, not stored. No thermodynamic work term enters the first law from memory.

### 3.5 Verdict

> **CLOSED**

Both the barrier potential and the memory sector contribute zero work at the GRUT equilibrium
endpoint. Option (c) — missing work term — is eliminated. The gap persists even with a
complete barrier + memory work accounting.

---

## 4. OPTION (a): ENTROPY REVISION

### 4.1 The Question

What entropy S_correct would make T_diss satisfy the first law exactly?

### 4.2 Required Entropy

From dE = T_diss dS_correct:

```
T_diss = c² / (k_B · dS_correct/dM)

dS_correct/dM = c² / (k_B · T_diss)

Since dS_eq/dM = c² / (k_B · T_1stlaw) = (1/R) × c² / (k_B · T_diss):

→ dS_correct/dM = R × dS_eq/dM
→ S_correct = R × S_eq ... wait — no.

T_diss = c²/(k_B · dS_correct/dM)
       = c²·R / (k_B · T_diss · dS_eq/dM · dS_correct/dM) ... let's use T_1stlaw:

T_diss = R · T_1stlaw = R · c²/(k_B · dS_eq/dM)

So: T_diss = c²/(k_B · dS_correct/dM)
→ dS_correct/dM = c²/(k_B · T_diss) = (1/R) · dS_eq/dM
→ S_correct = S_eq / R
```

The required entropy is:

```
S_correct = S_eq / R ≈ 0.827 × S_eq
```

In area-law form, this corresponds to an effective radius:

```
S_correct = π R_eff² / l_P²    where R_eff = R_eq/√R ≈ 0.909 × R_eq
```

### 4.3 Mass Scaling

```
S_eq ∝ R_eq² ∝ M²    →    S_correct = S_eq/R ∝ M²
```

The required entropy has the **same mass scaling** as the current proxy. Only the
coefficient changes by the factor 1/R ≈ 0.827.

### 4.4 Is There a GRUT-Native Geometric Ratio Equal to 1/√R?

```
1/√R = √(9/(2π√3)) = 3/√(2π√3)
```

This factor does not simplify in terms of the GRUT canonical parameters:
- α_vac = 1/3
- β_Q = 2
- ε_Q = 1/9
- Q = 6
- R_eq/r_s = 1/3

The number 0.909 is not a ratio of any two GRUT-locked quantities. It is not
(R_eq/r_s)^n for any rational n, and it does not equal any combination of α_vac and β_Q.

Alternatively, one might ask whether the Schwarzschild horizon entropy S_horizon = πr_s²/l_P²
is the "correct" entropy. This gives:

```
S_horizon = π r_s² / l_P² = 9 × S_eq
→ T_from_S_horizon = T_1stlaw/9 = T_Hawking
```

This selects T_Hawking, not T_diss — it does not close the gap, it creates a larger one.

### 4.5 Verdict

> **STRUCTURALLY_POSSIBLE_NO_GRUT_MOTIVATION**

Revising S_eq → S_eq/R closes the gap exactly with T_diss. The revision is a multiplicative
factor with no change in mass scaling. But the factor 1/√R ≈ 0.909 has no GRUT-native
geometric meaning. There is no GRUT quantity that motivates using an effective radius
0.909 × R_eq instead of R_eq.

---

## 5. OPTION (b): TEMPERATURE REVISION

### 5.1 The Question

What temperature would satisfy the first law exactly with S_eq?

### 5.2 T_1stlaw

Appendix H derives this directly:

```
T_1stlaw = c² / (k_B · dS_eq/dM) = 9 · T_Hawking = 9ℏc³/(8πGMk_B)
```

This temperature satisfies the first law **exactly** with S_eq and E = Mc².

### 5.3 Relation to T_diss

```
T_1stlaw / T_diss = 1/R ≈ 0.827
```

T_1stlaw is colder than T_diss by ~17.3%.

### 5.4 Can T_1stlaw Be Expressed Without T_Hawking?

Using the Schwarzschild light-crossing time τ_Schwarz = r_s/c = 2GM/c³:

```
T_1stlaw = 9ℏc³/(8πGMk_B) = 9ℏ/(4π · k_B · τ_Schwarz)
```

This does not import T_Hawking by name, but τ_Schwarz = r_s/c is the same parameter that
appears in T_Hawking = ℏ/(4π · k_B · τ_Schwarz). The structure is identical — T_1stlaw =
9·T_Hawking is the irreducible form.

### 5.5 Consequences If T_1stlaw Is Correct

If T_1stlaw is the correct GRUT temperature:

1. T_diss is wrong by factor R ≈ 1.21.
2. T_structural is wrong by factor R·Q = 2π√3/9 · 6 ≈ 7.26.
3. The FDT noise floor changes from S(0) = 2ℏ/Q to a mass-dependent expression.
4. The Q-factor retains its PDE meaning but loses its thermodynamic interpretation.

### 5.6 Verdict

> **VIABLE_NO_NEW_GRUT_STRUCTURE**

T_1stlaw = 9·T_Hawking closes the gap exactly with S_eq. It is accessible without quantum-state
input (no Appendix C blocker). But it is not a GRUT-native quantity — it equals 9 times the
imported Hawking temperature, derived from the same Schwarzschild structure. No new GRUT
structure is required; no new GRUT structure is provided.

---

## 6. GAP STRUCTURE: THE ORIGIN OF R = 4π√3/(3Q)

### 6.1 Algebraic Origin

The gap arises from combining two independent GRUT results:

```
  T_diss = ℏω₀ / (Q · k_B)      [barrier damping mode]
  dS/dM  = 8πG²M / (9c⁴l_P²)   [area law at R_eq = r_s/3]
```

Substituting ω₀ = √(β_Q·GM/R_eq³) = 3√3c³/(2GM):

```
  R = k_B · T_diss · (dS/dM) / c²
    = [ℏ · 3√3c³/(2GM·Q)] · [8πG²M/(9c⁴l_P²)] / c²   · (k_B/k_B)
    = ℏ · 3√3 · 8π / (2Q · 9 · c³ · l_P²/G)
    = 8π · 3√3 / (18Q)          [using l_P² = ℏG/c³]
    = 4π√3 / (3Q)
```

The factor 4π√3 comes entirely from ω₀ expressed in terms of M.
The factor Q is the barrier quality factor β_Q/α_vac.

### 6.2 Why R Cannot Equal 1 With Current Parameters

```
R = 1 would require Q = 4π√3/3 ≈ 7.255
```

With α_vac = 1/3 locked: β_Q = Q·α_vac ≈ 2.418 (not 2).
With β_Q = 2 locked: α_vac = β_Q/Q ≈ 0.276 (not 1/3).

Either change would modify the endpoint law:
```
R_eq/r_s = ε_Q^(1/β_Q) = (α_vac²)^(1/2) = α_vac
```

With α_vac ≈ 0.276: R_eq/r_s ≈ 0.276 (not 1/3).

The locked endpoint law R_eq/r_s = 1/3 — derived from Phase V and confirmed by five
independent sector checks — cannot accommodate R = 1 with a Lorentzian damping structure.

### 6.3 Could a Different Entropy Exponent Close the Gap?

If S ∝ R^n instead of R² (area law), then:

```
dS/dM ∝ M^(n/2 - 1)
T_1stlaw ∝ M^(1 - n/2)
```

For n = 1 (linear scaling, Bekenstein-Mukhanov): T_1stlaw ∝ M^(1/2), slower cooling than
T_diss ∝ M^(-1). The gap R would become mass-dependent, closing at one mass and reopening
at others. For n = 2 (area law): T_1stlaw ∝ M^(-1), same scaling as T_diss. R is
mass-independent — this is the current case.

No GRUT quantity motivates S ∝ R^n for n ≠ 2.

---

## 7. EXECUTIVE DETERMINATION

> **`gap_structural_no_external_free_parameter`**

1. **Option (c) — missing work term:** CLOSED. The barrier potential V_Q(R_eq) = −c²/2 is
   mass-independent (dV_Q/dM = 0). Memory does no work at V = 0. No work term can close
   the gap.

2. **Option (a) — entropy revision:** STRUCTURALLY_POSSIBLE. S_correct = S_eq/R closes
   the gap exactly. The revision is a factor 1/R ≈ 0.827 in the entropy coefficient,
   corresponding to R_eff ≈ 0.909 R_eq. No GRUT-native geometry provides this factor.

3. **Option (b) — temperature revision:** VIABLE. T_1stlaw = 9·T_Hawking closes the gap
   with no new GRUT structure and no quantum-state input. But T_1stlaw imports the
   Schwarzschild structure and is not independently GRUT-native.

4. **Parametric impossibility:** The gap cannot be closed by adjusting any GRUT-locked
   parameter (α_vac, β_Q, or Q) without violating the endpoint law R_eq/r_s = 1/3.

5. **Mass independence:** R = 4π√3/(3Q) depends only on Q = β_Q/α_vac. It is the same
   for any black hole mass. The gap is a universal feature of the GRUT thermodynamic sector.

---

## 8. SAFE AND UNSAFE CLAIMS

### Safe Claims

1. V_Q(R_eq) = −c²/2 exactly, independent of mass. This follows algebraically from
   ε_Q·(r_s/R_eq)^β_Q = 1 at the equilibrium endpoint.

2. The barrier does zero thermodynamic work for quasi-static mass changes: dV_Q/dM = 0.

3. The memory sector does zero work at the equilibrium endpoint (V = 0 → dM_drive/dt = 0).

4. Option (c) — missing work term — is eliminated.

5. S_correct = S_eq/R (= S_eq × 9/(2π√3)) is the unique entropy that makes T_diss satisfy
   the first law. The factor 1/√R ≈ 0.909 has no GRUT-native geometric interpretation.

6. T_1stlaw = 9·T_Hawking closes the gap exactly with S_eq. It can be expressed as
   9ℏ/(4π·k_B·τ_Schwarz) without naming T_Hawking, but is not independently GRUT-native.

7. R = 1 (exact first law with T_diss and S_eq) requires α_vac ≈ 0.276 or β_Q ≈ 2.42,
   incompatible with the locked endpoint law R_eq/r_s = 1/3.

8. The gap R = 4π√3/(3Q) is mass-independent. It is a universal feature of the current
   GRUT thermodynamic sector.

### Unsafe Claims

1. The gap is due to a missing physical term. (Option (c) is closed.)
2. Revising S to S_eq/R is GRUT-motivated. (No GRUT geometry provides factor 1/√R.)
3. T_1stlaw = 9·T_Hawking is GRUT-native. (It imports the Schwarzschild structure.)
4. The gap is closed. (It is not — both option (a) and option (b) require external input.)
5. The gap reveals an error in GRUT. (The gap is a structural consequence, not a
   contradiction.)

---

## 9. INHERITED CLASSIFICATIONS (UNCHANGED)

All prior appendix determinations are unchanged. Appendix I narrows the gap's origin
to two remaining options, but does not resolve either.

- **Appendix D:** `thermodynamic_sector_partially_consistent` — UNCHANGED.
  The gap does not constitute an internal inconsistency; it constrains the temperature
  and entropy choices.

- **Appendix E:** `locally_consistent_globally_underdetermined` — UNCHANGED.
  The barrier sector and the thermodynamic sector are each internally consistent; their
  cross-sector combination is underdetermined (temperature not selected).

- **Appendix H:** `temperature_selectable_conditionally_not_uniquely` — UNCHANGED.
  The first-law gap confirms the status: T_1stlaw is viable but not GRUT-native;
  T_diss is GRUT-native but fails the first law by factor R.

---

## 10. CODE ARTIFACTS

| File | Description |
|------|-------------|
| `grut/first_law_gap_audit.py` | Three option audits, gap structure analysis, barrier work proof |
| `tests/test_first_law_gap_audit.py` | 123 tests, all passing |

**Key numeric results (mass-independent where noted):**

| Result | Value | Mass-independent? |
|--------|-------|-------------------|
| V_Q(R_eq)/c² | −0.5 (exact) | YES |
| dV_Q/dM | 0.0 (exact) | YES |
| R_GAP = T_diss/T_1stlaw | 2π√3/9 ≈ 1.209 | YES |
| S_correct/S_eq = 1/R | ≈ 0.827 | YES |
| R_eff/R_eq = 1/√R | ≈ 0.909 | YES |
| T_1stlaw/T_diss = 1/R | ≈ 0.827 | NO (both ∝ 1/M) |
| α_vac needed for R=1 | ≈ 0.276 | YES |
| Q needed for R=1 | 4π√3/3 ≈ 7.255 | YES |
