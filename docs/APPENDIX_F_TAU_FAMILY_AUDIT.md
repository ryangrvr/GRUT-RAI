# APPENDIX F — τ_eff UNIFICATION / COVARIANT SCALING AUDIT

**Date:** 2026-03-27
**Follows:** Appendix E Pass 1 and Pass 2
**Status:** Single-pass audit — τ-family problem only

---

## 1. EXECUTIVE DETERMINATION

> **`tau_symbolically_conflated_but_rescuable`**

The GRUT architecture does NOT have one unified τ_eff. It has a coherent two-level family of timescales all derived from the global anchor τ₀, but the family is undocumented, the meta-rule for applying each level is not covariant, and the shared symbol τ_eff obscures structurally distinct objects.

The architecture is **rescuable** because:
1. All sector τ-objects are related to τ₀ by an explicit (but implicit in code) two-level reduction scheme.
2. The two-level structure is present in the code — it is not invented.
3. A translation rule can be stated that preserves all prior appendix results.

The architecture is **conflated** because:
1. The same symbol τ_eff refers to objects differing by ~10^19 at equilibrium.
2. The meta-rule for Level-1 application (tier-0 vs. bare) is a mode switch, not a covariant condition.
3. The Q2 Drude bath (cutoff Ω = 1/τ₀) applies to the cosmological regime; it is misapplied to the interior regime where the relevant cutoff is 1/τ_local ~ 1/t_dyn.
4. The structural identity ω₀·τ = 1 uses τ_local, not τ₀ or τ_eff_cosmo.

**Classification unchanged:** `locally_consistent_globally_underdetermined`

---

## 2. τ-FAMILY OBJECT DEFINITIONS

Seven materially distinct τ-like objects are active in the GRUT architecture.

### Object 1: τ₀ — Global vacuum memory anchor

| Field | Value |
|-------|-------|
| Symbol in code | `tau0`, `tau_0`, `TAU_0_S` |
| Operative formula | τ₀ = 1.3225 × 10¹⁵ s (phenomenological constant) |
| Sector | ALL — this is the base parameter |
| Physical meaning | Bare cosmological memory relaxation constant. Anchored to Phase I phenomenological fit. |
| Derivation status | Phenomenological. Not derived from first principles. |
| Depends on | Nothing — it is the anchor |
| Scope | Global, claimed universal |
| Authority | Tier-0 locked constant |

### Object 2: τ_eff_cosmo — Cosmological effective susceptibility time

| Field | Value |
|-------|-------|
| Symbol in code | `tau_eff` (state variable), `_tau_eff(canon, H)` in operators.py |
| Operative formula | τ_eff = τ₀ / (1 + (H · τ₀)²) |
| Sector | Cosmological (engine.py, operators.py) |
| Physical meaning | Effective memory relaxation time at Hubble rate H. Lorentzian susceptibility. |
| Derivation status | Derived from τ₀ via Lorentzian filter at ω = H |
| Depends on | τ₀, H (Hubble rate — global, not local) |
| Scope | Regime-specific; valid for FLRW background |
| Note | Uses raw τ₀ — no Level-1 reduction applied |

### Object 3: τ_eff_collapse_bare — Collapse effective time (bare mode)

| Field | Value |
|-------|-------|
| Symbol in code | `tau_eff` (in collapse.py with `local_tau_mode="off"`) |
| Operative formula | τ_eff = τ₀ / (1 + (\|V/R\| · τ₀)²) |
| Sector | Collapse — bare mode |
| Physical meaning | Effective memory time at local collapse rate \|V/R\|, using raw τ₀ as base |
| Derivation status | Derived from τ₀ via Lorentzian filter at ω = \|V/R\| |
| Depends on | τ₀, V, R (local shell state) |
| Scope | Regime-specific; collapse trajectory only |
| Note | Functionally identical to τ_eff_cosmo with ω = \|V/R\| instead of H |

### Object 4: τ₀_local — Level-1 locally-reduced anchor

| Field | Value |
|-------|-------|
| Symbol in code | `tau0_local` in `_compute_tau0_local()` (collapse.py, tier-0 mode) |
| Operative formula | τ₀_local = τ₀ · t_dyn / (t_dyn + τ₀), where t_dyn = √(R³/2GM) |
| Sector | Collapse — tier-0 mode; Interior PDE (as τ_local) |
| Physical meaning | τ₀ reduced by the local dynamical time. Harmonic mean of τ₀ and t_dyn. Approaches t_dyn when t_dyn ≪ τ₀. |
| Derivation status | Level-1 reduction — heuristic tier-0 closure, not covariant |
| Depends on | τ₀, R, M (local geometry) |
| Scope | Local; strong-field regime only |
| Authority | Phenomenological closure, labeled "tier-0" |

### Object 5: τ_eff_collapse_tier0 — Two-level collapse effective time

| Field | Value |
|-------|-------|
| Symbol in code | `tau_eff` (in collapse.py with `local_tau_mode="tier0"`) |
| Operative formula | τ_eff = τ₀_local / (1 + (\|V/R\| · τ₀_local)²) |
| Sector | Collapse — tier-0 mode |
| Physical meaning | Two-level effective time: first locally-reduced, then Lorentzian-filtered |
| Derivation status | Two-level: τ₀ → τ₀_local (Level 1) → τ_eff (Level 2) |
| Depends on | τ₀, V, R, M |
| Scope | Local dynamical; strong-field with non-zero velocity |
| At V=0 | Reduces to τ₀_local (Level 2 gives no change when \|V/R\| = 0) |

### Object 6: τ_local — Interior equilibrium timescale

| Field | Value |
|-------|-------|
| Symbol in code | `tau_local` in interior_pde.py, interior_waves.py |
| Operative formula | τ_local = τ₀ · t_dyn / (t_dyn + τ₀) \|_{R=R_eq, V=0} |
| Sector | Interior PDE, Interior Waves |
| Physical meaning | τ₀_local evaluated at the equilibrium endpoint. Local dynamical timescale at R_eq. Satisfies ω₀ · τ_local = 1 (structural identity). |
| Derivation status | **Identical formula to τ₀_local**, evaluated at equilibrium |
| Note | τ_local IS τ₀_local at R = R_eq. No additional formula. |
| Scope | Interior equilibrium — single point in configuration space |
| Authority | The only τ satisfying ω₀·τ = 1 at the BDCC endpoint |

**Key finding:** τ_local is not a separate formula. It is τ₀_local evaluated at R = R_eq. The interior PDE did not introduce a new τ object — it used Level-1 reduction without Level-2 (since V = 0 at equilibrium eliminates the Lorentzian suppression).

### Object 7: τ_bath (= 1/Ω) — Q2 spectral bath cutoff period

| Field | Value |
|-------|-------|
| Symbol in code | Implicit in `Omega = 1/tau_0` (quantum_program_q2.py, q3.py) |
| Operative formula | τ_bath = τ₀ (the bath cutoff period is 1/Ω = τ₀) |
| Sector | Q1–Q4 quantum program |
| Physical meaning | Period corresponding to the Drude/Lorentzian bath cutoff Ω = 1/τ₀. |
| Derivation status | Identified from structural match; τ_bath = τ₀ by definition |
| Scope | Cosmological — this is a cosmological-scale bath |
| Critical note | τ_bath = τ₀ ≠ τ_local. The Q2 bath cutoff is cosmological, not astrophysical. The resonance ω₀ = Ω is numerically false. |

---

## 3. τ-MAP TABLE

| τ-object | Sector | Formula | Physical Interpretation | Scale Type | Relation to τ₀ | Current Status |
|----------|--------|---------|------------------------|-----------|----------------|----------------|
| τ₀ | ALL | 1.3225×10¹⁵ s | Global vacuum memory anchor | bare constant | identical | clearly_distinct |
| τ_eff_cosmo | Cosmological | τ₀/(1+(H·τ₀)²) | Effective susceptibility at Hubble rate | effective susceptibility | scaled from τ₀ | clearly_distinct |
| τ_eff_collapse_bare | Collapse (off) | τ₀/(1+(\|V/R\|·τ₀)²) | Effective time at collapse rate, bare base | effective susceptibility | scaled from τ₀ | **maybe_translatable** (same formula as τ_eff_cosmo) |
| τ₀_local | Collapse (tier0) | τ₀·t_dyn/(t_dyn+τ₀) | Locally-reduced anchor; Level-1 reduction | local dynamical | reduced from τ₀ | clearly_distinct |
| τ_eff_collapse_tier0 | Collapse (tier0) | τ₀_local/(1+(\|V/R\|·τ₀_local)²) | Two-level effective time | effective susceptibility | scaled from τ₀ (two levels) | clearly_distinct |
| τ_local | Interior PDE/Waves | τ₀·t_dyn/(t_dyn+τ₀)\|_{R_eq} | Interior equilibrium timescale | local dynamical | reduced from τ₀ | **symbolically_conflated** with τ_eff |
| τ_bath (1/Ω) | Q1–Q4 | τ₀ | Drude bath cutoff period | spectral cutoff | identical to τ₀ | **symbolically_conflated** (called τ_eff in Q2/Q3 text) |
| t_dyn | Interior, Collapse | √(R³/(2GM)) | Local gravitational dynamical time | local dynamical | independent | clearly_distinct |

### Summary of symbolic conflation sites

- **Q2/Q3** write "τ_eff" when referring to the formula τ₀/(1+(ω·τ₀)²) with τ₀ as the base. This is the COSMOLOGICAL formula, not the interior one. The structural identity they invoke — ω₀·τ_eff = 1 — requires τ = τ_local, not τ_eff_cosmo.

- **Interior PDE** uses `tau_local` in code but calls it "τ_eff" in equations and documentation, creating the false impression that τ_local = τ_eff_cosmo|_{ω=ω₀}.

- **Collapse sector**: when `local_tau_mode="off"`, τ_eff = τ₀ at V=0. When `local_tau_mode="tier0"`, τ_eff = τ₀_local at V=0. The same variable name `tau_eff` in the code output array covers both.

---

## 4. RESOLUTION A/B/C AUDIT

### Resolution A — True unification

**Claim:** One underlying τ object; all sector uses are regime translations.

**What must be true:** The same formula, evaluated at different values of ω_local (H for cosmology, \|V/R\| for collapse, ω₀ for interior modes), gives the same τ object at the appropriate scale for each sector.

**Evidence supporting:**
- τ_eff_cosmo and τ_eff_collapse_bare share the identical formula τ₀/(1+(ω·τ₀)²); they differ only in ω. These ARE regime translations of the same object.
- The Level-2 Lorentzian filter is universal: the same functional form applies in all active sectors.

**Evidence undermining:**
- The cosmological sector uses τ₀ as the base; the interior sector uses τ_local = t_dyn (which is much smaller than τ₀) as the effective timescale at V=0. These cannot be reconciled as "same formula at different ω" because τ_local is not the result of applying the Lorentzian filter to τ₀ at any ω — it requires the Level-1 reduction first.
- τ_eff_cosmo|_{H→0} = τ₀ (cosmic scale, ~10¹⁵ s). τ_local|_{R=R_eq} = t_dyn (astrophysical, ~10⁻⁵ s). These are the same "static limit" of each sector's formula, and they differ by 10²⁰.
- There is no covariant scalar field ω_local that smoothly interpolates between H (cosmological) and \|V/R\| (collapse) in a diffeomorphism-covariant way.

**Verdict:** **reject**

True unification requires a single covariant formula with one τ object. The Level-1 reduction is an essential structural feature, not a regime translation.

---

### Resolution B — Disciplined family

**Claim:** No single τ_eff, but a coherent family of timescales derived from τ₀ by explicit rules.

**What must be true:** An explicit meta-rule exists (or can be stated) that predicts which τ-object applies in each sector, with no free choices.

**Proposed meta-rule (extracted from code):**

```
τ_base(sector) = τ₀                           [if no strong local gravity]
               = τ₀ · t_dyn / (t_dyn + τ₀)   [if strong local gravity: t_dyn ≪ τ₀]

τ_eff(sector) = τ_base / (1 + (ω_local · τ_base)²)

ω_local = H         [cosmological]
         = |V/R|    [collapse]
         = 0        [interior equilibrium, V=0]
```

This meta-rule correctly recovers:
- τ_eff_cosmo = τ₀/(1+(H·τ₀)²)              ✓
- τ_eff_collapse_bare = τ₀/(1+(|V/R|·τ₀)²)  ✓  [off mode]
- τ_eff_collapse_tier0 = τ₀_local/(1+(|V/R|·τ₀_local)²)  ✓  [tier0 mode]
- τ_local = τ₀_local|_{V=0} = τ₀·t_dyn/(t_dyn+τ₀)       ✓  [interior PDE]

**Evidence supporting:**
- The code explicitly implements both Level-1 (`_compute_tau0_local` with tier0 mode) and Level-2 (Lorentzian filter) in collapse.py.
- Interior PDE's τ_local IS τ₀_local at V=0 — same formula, same code path.
- The Level-2 functional form is identical in all sectors.
- The two-level structure is latent in the code — it is not invented.

**Evidence undermining:**
- The Level-1 application condition ("strong local gravity: t_dyn ≪ τ₀") is a mode switch (`local_tau_mode`), not a covariant criterion. In the cosmological sector, Level-1 is never applied even at the early universe where t_dyn can be comparable to τ₀.
- The meta-rule predicts τ_base for each sector, but the CHOICE of τ_base for a given sector is not derived — it is set by the user (mode parameter).
- The Q2 Drude bath (cutoff Ω = 1/τ₀) belongs to the Level-0 (τ₀) layer. It does not automatically generalize to the Level-1 layer (τ_local with cutoff 1/t_dyn). The structural identity ω₀·τ_local = 1 and the Q2 resonance ω₀ = Ω = 1/τ₀ are irreconcilable: they refer to different τ objects.
- The Level-1 rule is not derived from the action principle. It is a "tier-0 closure" — a heuristic approximation.

**Verdict:** **possible_but_unproven**

Resolution B is the strongest available description. The two-level family exists in the code and is self-consistent. But it is undocumented, the Level-1 application condition is not covariant, and the Q2 bath identification applies only to the Level-0 layer.

---

### Resolution C — Structural split

**Claim:** The sectors are using fundamentally different physical timescales; the notation masks a real non-unification.

**What must be true:** There is no meta-rule that coherently connects all sector τ's to a single principle.

**Evidence supporting:**
- The cosmological and interior τ's differ by ~10²⁰ at static limits. No smooth interpolation with physical meaning.
- The Q2 Drude bath cutoff (Ω = 1/τ₀) is a cosmological-scale frequency (~10⁻¹⁵ rad/s). The relevant interior-sector frequency is 1/τ_local ~ 1/t_dyn (~10⁴ rad/s). These are different baths in different regimes.
- The structural identity ω₀·τ = 1 uses τ_local (interior), while Q2/Q3 invoke it as if it applies to τ₀ (cosmological). This is a genuine cross-sector equivocation.

**Evidence undermining:**
- All τ-objects ARE traceable to τ₀. None is introduced independently.
- The Level-1 and Level-2 rules DO correctly predict each sector τ from τ₀, even if the meta-rule is not covariant.
- The architecture has not produced an internal contradiction within any sector — the split is in the cross-sector notation, not in the within-sector physics.

**Verdict:** **weak**

The split is real in the sense that the sectors use different physical timescales. But calling it "structural" overstates the case: all τ's are related by an explicit (if uncodified) derivation chain from τ₀. The situation is better described as Resolution B (undocumented family) than Resolution C (genuine split).

---

## 5. KEY IDENTITY AUDIT

### Identity 1: τ = τ₀ at equilibrium

**Claim (implicit in Q2 resonance and collapse-bare mode):** At equilibrium (V=0), τ_eff = τ₀.

**Analysis:** TRUE for collapse-bare mode. At V=0, τ_eff = τ₀/(1+0) = τ₀. But FALSE for collapse-tier0 mode and interior PDE. At V=0 with tier0, τ_eff = τ₀_local ≈ t_dyn ≪ τ₀.

**Classification:** `valid_in_own_sector` (bare/cosmological mode) / `false_as_cross_sector_identity`

---

### Identity 2: τ_local ≈ t_dyn

**Claim (interior PDE):** τ_local = τ₀·t_dyn/(t_dyn+τ₀) ≈ t_dyn for astrophysical masses.

**Analysis:** TRUE. For t_dyn ≪ τ₀: τ_local = τ₀·t_dyn/(t_dyn+τ₀) → t_dyn. The approximation error is t_dyn/τ₀ < 10⁻²⁰ for a 30 M_sun BH. Exact formula is τ_local = t_dyn/(1+t_dyn/τ₀).

**Classification:** `valid_in_own_sector` — accurate interior PDE identity.

---

### Identity 3: ω₀·τ = 1 (structural identity)

**Claim (interior PDE, Q2/Q3):** The BDCC oscillation frequency satisfies ω₀·τ = 1.

**Analysis:** TRUE with τ = τ_local. Since τ_local ≈ t_dyn and ω₀ = √(β_Q·GM/R_eq³) ≈ 1/t_dyn (gravitational scaling), the identity ω₀·τ_local = 1 holds to ~5%.

TRUE also from the interior PDE definition: τ_local is DEFINED as τ₀·t_dyn/(t_dyn+τ₀), and ω₀·τ_local ≈ ω₀·t_dyn = 1 by gravitational scaling.

FALSE as a cross-sector identity: ω₀·τ₀ = ω₀·τ_bath ~ 10¹⁹. The identity says nothing about τ₀.

**Classification:** `valid_only_under_assumptions` (τ = τ_local, gravitational scaling); `symbolically_misleading_across_sectors` (Q2/Q3 invoke it with τ = τ₀ implicitly)

---

### Identity 4: Ω = 1/τ₀ (Q2 bath resonance with ω₀)

**Claim (Q2):** The Drude bath cutoff Ω = 1/τ₀ satisfies ω₀ = Ω at the BDCC equilibrium.

**Analysis:** FALSE numerically. For 30 M_sun: ω₀ ~ 1.76×10⁴ rad/s, while Ω = 1/τ₀ ~ 7.56×10⁻¹⁶ rad/s. Ratio ~ 2.3×10¹⁹. The Q2 claim "ω₀ = Ω" conflates τ_local with τ₀.

The correct resonance statement is: ω₀ = 1/τ_local (which is true by the gravitational scaling ω₀ ~ 1/t_dyn and τ_local ~ t_dyn). The Q2 bath cutoff Ω = 1/τ₀ does NOT resonate with ω₀.

**Classification:** `false_as_cross_sector_identity` — a category error arising from equating τ_local with τ₀.

---

### Identity 5: τ_eff_cosmo formula with H as driver

**Claim (operators.py, engine.py):** τ_eff = τ₀/(1+(H·τ₀)²) where H is the Hubble rate.

**Analysis:** TRUE within the cosmological sector. The formula is applied consistently with H computed from the Friedmann equation. The Lorentzian filter is appropriate: τ_eff → τ₀ as H → 0 (late universe); τ_eff → 1/(H·τ₀) as H·τ₀ ≫ 1 (early universe). No level-1 reduction is applied.

**Classification:** `valid_in_own_sector` — no conflict within cosmological sector.

---

### Identity 6: τ_eff_collapse_bare = τ_eff_cosmo with ω = |V/R|

**Claim (Q2 doc string):** The formulas are the same with ω substituted.

**Analysis:** TRUE formally. The substitution H → |V/R| gives the same Lorentzian formula. The physical identification of |V/R| as the "collapse Hubble rate" (the local expansion-analog) is explicit in the collapse.py comments.

**Classification:** `valid_only_under_assumptions` — the analogy H ↔ |V/R| is a physical identification, not a derivation from a covariant scalar quantity.

---

## 6. META-TRANSLATION RULE TEST

### Proposed translation rule

**The Two-Level τ-Family Rule:**

```
LEVEL 0 — GLOBAL ANCHOR:
    τ₀ = 1.3225 × 10¹⁵ s  [phenomenological, locked]

LEVEL 1 — LOCAL REDUCTION (applies in strong-field sectors only):
    τ_base = τ₀ · t_dyn(R, M) / (t_dyn(R, M) + τ₀)
    where t_dyn = √(R³/(2GM))
    [applied when t_dyn ≪ τ₀, i.e., astrophysical strong-field]

LEVEL 2 — LORENTZIAN FILTER (always applied with local rate ω_local):
    τ_eff(sector) = τ_base(sector) / (1 + (ω_local · τ_base(sector))²)
    where ω_local = H (cosmological), |V/R| (collapse), 0 (interior at V=0)

SECTOR ASSIGNMENTS:
    Cosmological:              τ_base = τ₀      [skip Level 1]
    Collapse (bare):           τ_base = τ₀      [skip Level 1]
    Collapse (tier-0):         τ_base = τ₀_local [Level 1 applied]
    Interior PDE (at V=0):     τ = τ_local = τ₀_local|_{R=R_eq}  [Level 1 only, Level 2 trivial]

BATH IDENTIFICATION SCOPE:
    Q2 Drude bath (cutoff Ω = 1/τ₀):  applies to LEVEL-0 objects (τ₀, τ_eff_cosmo)
    Interior bath (if sought):          would have cutoff Ω_interior ~ 1/τ_local ~ 1/t_dyn
    These are DIFFERENT BATHS with DIFFERENT CUTOFFS.

STRUCTURAL IDENTITY SCOPE:
    ω₀ · τ_local = 1 is a LEVEL-1 identity (gravitational scaling).
    It does NOT apply to τ₀ or τ_eff_cosmo.
```

### Does this rule genuinely clarify the architecture?

**Yes, in the following ways:**
- It correctly predicts all seven τ-objects from τ₀ using explicit operations.
- It resolves the Q2 resonance confusion: ω₀ = Ω is false (that was a Level-0 claim); ω₀ = 1/τ_local is true (Level-1 identity).
- It correctly scopes the Drude bath to the cosmological/Level-0 layer.
- It preserves prior appendix results: Q = 6 uses τ_local, which is a Level-1 object; the thermodynamic candidates T_dissipation and T_structural use ω₀ = 1/τ_local, which is the Level-1 structural identity.
- No prior classification is weakened.

**No, in the following ways:**
- The criterion for applying Level 1 ("strong-field: t_dyn ≪ τ₀") is a heuristic, not a covariant condition. In a covariant theory, the same rule should emerge from a single covariant expression for τ without sector-specific mode switches.
- The Level-1 rule requires τ_base to change across sectors. A fully unified theory would have one τ field with one covariant equation of motion, not a mode switch.
- The distinction between collapse-bare (no Level 1) and collapse-tier0 (Level 1) is a USER CHOICE in the current code, not a derived condition from physics.

### Classification

> **`translation_rule_partially_viable`**

The rule correctly classifies all sector τ's, resolves the resonance confusion, scopes the Q2 bath, and preserves prior appendices. It fails to be covariant: the Level-1 application condition is a heuristic mode switch, not derived from the field equations. It is adequate as a documentation clarification; it is inadequate as a fundamental architectural claim.

---

## 7. CROSS-SECTOR IMPACT AUDIT

### A. Appendix D thermodynamics

**Does τ clarification change temperature candidate status?**

The two GRUT-native temperature candidates are:
- T_dissipation = ℏω₀/(Q·k_B) — uses ω₀ = 1/τ_local (Level-1 identity)
- T_structural = ℏω₀/k_B — same ω₀

Both use the Level-1 identity ω₀·τ_local = 1. This is now precisely characterized as a gravitational scaling identity (ω₀ ~ 1/t_dyn) rather than a constitutive law property. This does NOT change the candidate values or their derivation status — they remain defined from interior quantities, well-characterized.

**Impact on FDT:** The FDT requires bath temperature T (still undetermined). The Q2 Drude bath (Level-0) has cutoff 1/τ₀ — a cosmological frequency. The FDT thermal scale relevant to the interior would require a Level-1 bath with cutoff 1/τ_local. These are not the same FDT. The FDT conditional status of Appendix D is unchanged; it is now more precisely scoped: the Q2/Drude FDT is a cosmological-sector FDT, not an interior-sector FDT.

**Net impact: MARGINAL.** The temperature candidates are unchanged. The FDT is now more precisely scoped but still conditional.

---

### B. Q1–Q4 quantum phase

**Does τ clarification weaken or reinterpret the Q2/Q3 Lorentzian story?**

The Q2 Drude identification (J(ω) ~ η·ω·Ω²/(ω²+Ω²), Ω = 1/τ₀) is now more precisely characterized as applying to the **cosmological/Level-0 layer** of the τ family. The bath it identifies has cutoff Ω = 1/τ₀ = 7.56×10⁻¹⁶ rad/s — a cosmological frequency.

The Q3 Lorentzian grounding — showing that the interior PDE dispersion relation contains a 1/(1+iωτ) factor — now has a corrected τ interpretation: the τ in the interior PDE's 1/(1+iωτ) is τ_local (Level-1), NOT τ₀. The cutoff of the interior Lorentzian is 1/τ_local ~ 1/t_dyn ~ 10⁴ rad/s, not 1/τ₀.

**The Q2/Q3 Drude identification and the Q3 interior Lorentzian grounding are therefore referring to different Lorentzians with different cutoffs.** Q2 identified the bath for the cosmological constitutive law. Q3 grounded the Lorentzian in the interior PDE. These are NOT the same Lorentzian.

This is a **reinterpretation** (not a contradiction) of Q2/Q3: the Q2 bath applies at cosmological scales; the interior PDE contains a separate Lorentzian at astrophysical scales. The structural identity ω₀·τ = 1 applies to the interior Lorentzian's τ_local, not to the Q2 bath's τ₀.

Q2 resolution: `bath_dof_unspecified` — unchanged. The bath type (Drude) is identified for the cosmological sector. An interior bath with cutoff 1/τ_local remains unidentified.

**Net impact: REINTERPRETATION.** The Q2 bath scope is now restricted to the cosmological layer. The Q3 Lorentzian in the interior PDE is a separate object. No prior classification is weakened; the scope is sharpened.

---

### C. Constitutive / collapse sector

**Does τ clarification preserve the present constitutive law?**

YES — the constitutive law (τ dM_drive/dt + M_drive = a_grav) is preserved exactly. The τ in this law is τ_eff_collapse (bare or tier-0, depending on mode). The two modes give different relaxation timescales but the same functional form of law.

**Does it expose a false universality claim?**

YES — there is an implicit claim that the constitutive law has one relaxation timescale τ_eff. In reality, the relaxation timescale is:
- τ₀ ~ 10¹⁵ s at V=0 in bare mode (cosmic-scale relaxation — M_drive relaxes to a_grav over cosmic time)
- τ_local ~ 10⁻⁵ s at V=0 in tier-0 mode (astrophysical-scale relaxation — M_drive relaxes to a_grav over dynamical time)

These are physically different systems. In the bare mode at equilibrium, memory essentially NEVER relaxes (τ = τ₀ is a cosmic timescale). In the tier-0 mode at equilibrium, memory relaxes quickly relative to the BDCC mode period.

The constitutive law is the same formula in both cases, but its physical implications differ radically. This is NOT a contradiction within any sector — each mode is internally consistent. But the claim that τ_eff is one universal constitutive timescale is FALSE.

**Net impact: MODERATE CLARIFICATION.** The constitutive law is preserved. The mode-dependence of τ at equilibrium (10^20 ratio) is now explicitly characterized as a physical difference, not a notational one.

---

### D. Cosmological / phenomenological sector

**Does τ clarification destabilize cosmological usage?**

NO. The cosmological sector uses τ_eff = τ₀/(1+(H·τ₀)²) consistently. This is a Level-0 → Level-2 operation (no Level-1 reduction). The clarification only confirms that Level-1 is not applied here, which is consistent with the code.

The H_cap (stiffness cap) in the cosmological engine is unchanged. The Drude bath identification (Level-0) continues to apply to the cosmological memory constitutive law.

**Net impact: NONE.** Cosmological sector is unaffected. The clarification is that Level-1 does not apply here — which was already implicit in the code.

---

## 8. CODE-WORTHINESS DECISION

**Yes, a narrow deterministic module is warranted.**

The τ-family audit is fully deterministic:
- Seven τ-objects with explicit formulas
- Classification of each object's sector and status
- Level-1/Level-2 factorization test
- Resolution A/B/C verdicts
- Key identity classifications
- Translation rule assessment
- Cross-sector impact summary

None of these require simulation. All produce explicit classification strings with numerical support.

**Files to create:**
- `grut/tau_family_audit.py`
- `tests/test_tau_family_audit.py`

---

## 9. FILES CREATED

### `grut/tau_family_audit.py`

**Exact purpose:** Defines the seven τ-family objects with explicit formulas; tests Level-1/Level-2 factorization; audits Resolutions A/B/C; classifies key identities; evaluates translation rule; exports to dict. Blocks "tau_unified" claim.

**Assumptions:** All formulas are taken directly from code (collapse.py, operators.py, interior_pde.py, quantum_program_q2.py). No new physics. Reference mass: 30 M_sun. τ₀ = 1.3225×10¹⁵ s. β_Q = 2, α_vac = 1/3.

**What the module does NOT claim:**
- Does not claim τ is unified
- Does not claim Level-1 is covariant (it is not)
- Does not claim the Q2 bath applies to the interior sector
- Does not claim the structural identity ω₀·τ = 1 applies at τ = τ₀
- Does not upgrade Appendix E classification

### `tests/test_tau_family_audit.py`

**Test summary:** 40+ tests covering object definitions, Level-1/Level-2 factorization, Resolution verdicts, identity classifications, translation rule, cross-sector impacts, forbidden claims, and serialization.

---

## 10. DOCUMENT-BUILDING CONSTRAINTS FOR LATER USE

### Claims a future Appendix F document MAY safely make

1. The GRUT architecture uses a family of timescales, all derived from τ₀, organized by an implicit two-level reduction scheme: Level-1 (local gravitational reduction: τ₀ → τ₀_local = τ₀·t_dyn/(t_dyn+τ₀)) and Level-2 (Lorentzian filter: τ_base → τ_eff = τ_base/(1+(ω_local·τ_base)²)).

2. τ_local (interior PDE) and τ₀_local (collapse tier-0) are the same formula evaluated at equilibrium. Neither is an independent derivation; both are Level-1 reductions of τ₀.

3. The structural identity ω₀·τ_local = 1 is a gravitational scaling identity (ω₀ ~ 1/t_dyn and τ_local ~ t_dyn), not a constitutive law property. It does not apply to τ₀ or τ_eff_cosmo.

4. The Q2 Drude bath (cutoff Ω = 1/τ₀) applies to the cosmological/Level-0 layer of the τ family. It is a cosmological-scale bath (Ω ~ 10⁻¹⁵ rad/s). An interior-sector bath (if one exists) would have cutoff Ω_interior ~ 1/τ_local ~ 10⁴ rad/s — 10¹⁹ times higher. Q2 and Q3 refer to different Lorentzians.

5. The translation rule is partially viable: it correctly classifies all sector τ's and resolves the resonance confusion, but requires the Level-1 application condition to be covariantized (currently a mode switch, not a derived criterion).

6. The constitutive law τ dM_drive/dt + M_drive = X is preserved in all sectors. The τ in this law is sector-specific (τ₀ in cosmological, τ₀_local in interior), differing by ~10²⁰ at static equilibrium for astrophysical masses. This is a physically meaningful difference in relaxation behavior, not a notational ambiguity.

7. τ_eff_cosmo (H-scale) and τ_eff_collapse_bare (|V/R|-scale) are genuine regime translations of the same Level-2 formula. The analogy H ↔ |V/R| is explicit in the code and is the strongest translatable pair.

### Claims a future Appendix F document MUST NOT make

1. That all τ-objects are the same unified quantity. They are related but NOT unified.

2. That the structural identity ω₀·τ = 1 implies ω₀ = 1/τ₀ (the Q2 resonance condition). These differ by ~10¹⁹.

3. That the Q2 Drude bath (cutoff 1/τ₀) is the bath relevant to the interior PDE sector. The relevant interior bath would have a 10¹⁹ times higher cutoff.

4. That the Level-1 reduction rule is covariant. It is a heuristic tier-0 closure, not derived from the field equations.

5. That the translation rule resolves the τ non-covariance. It clarifies it; it does not resolve the underlying structural issue (the lack of a covariant single τ field equation).

6. That the cosmological sector's τ_eff and the interior PDE's τ_local are at different regimes of the same formula. They require different base objects (τ₀ vs. τ₀_local) that differ by ~10²⁰ at static equilibrium.

7. That the Appendix E classification is upgraded to "coherent_but_tensioned" or "appears_coherent." The τ non-covariance is partially tamed by the two-level family description, but the meta-rule is not covariant and the Q2 bath scope confusion is a real structural issue.

### Strongest defensible classification after Appendix F

> **`tau_symbolically_conflated_but_rescuable`**

The τ-family is a coherent but undocumented two-level reduction scheme. All sector τ's are traceable to τ₀. The conflation is real (same symbol for objects differing by 10²⁰), the rescue is partial (translation rule is valid but not covariant), and the Q2 bath scope restriction is a genuine architectural correction.

Appendix E classification remains: **`locally_consistent_globally_underdetermined`**

Appendix F adds: the global underdetermination is now more precisely located. It lives in the absence of a covariant Level-1 application rule, and in the equivocation between the cosmological Drude bath (τ₀-scale) and the interior Lorentzian (τ_local-scale).
