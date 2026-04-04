# Book XIII — Target Delta: Strong-Field Correction, Reclassification, and Compact-Object Path Decision

## Formal Correction and Path-Decision Stage — Fourth Book XIII Stage

**Predecessor:** Book XIII Gamma (CRITICAL CORRECTION: scalar-only TOV worsens interior; prior structural predictions incorrect)
**Function:** Freeze the Gamma correction; reclassify all prior XIII claims; decide the surviving compact-object path
**Entry cost:** 16/11/1/6 (committed; GGB uncommitted)

---

## 1. Executive Verdict

**Global verdict: (B) — The compact-object frontier survives, but only in narrowed and corrected form. The surviving path is a dual-track program: (Track 1) combined scalar+defect equilibrium program conditional on self-consistent TOV, and (Track 2) transient collapse-processing phenomenology conditional on physical realization of A > A_crit.**

The Gamma correction is real and load-bearing. It eliminates the scalar-only equilibrium narrative that Books XIII Alpha and Beta were built on. But it does NOT eliminate all strong-field content. Two genuine physics results survive:

1. **The D1–D10 combined (scalar + defect) result:** f_min = +0.37 to +0.46 on a fixed Schwarzschild background with Picard proxy closure. The defect sector (Component B, η²/r²) provides the crucial positive-energy support that the scalar sector alone cannot. This is CONDITIONAL — it has not been verified on a self-consistent background — but it is real numerical work with convergent iteration across a tested parameter range.

2. **The transient supercritical processing result:** At A > A_crit ≈ 1.062, the scalar field's kinetic energy exceeds the equilibrium deficit, driving f → 0. This is TRANSIENT (decays on timescale τ) and A_crit is NOT shown to be physically realized — but the mathematical structure is locked and the threshold is quantified.

Neither of these is what Alpha/Beta claimed. Both are weaker. Both are conditional. But both are real physics, not empty narrative.

---

## 2. Why Book XIII Delta Is Now Necessary

Gamma produced a critical correction that broke the XIII Alpha/Beta surplus narrative. Without Delta, the program would carry forward claims that the canon's own locked code contradicts. Delta freezes the correction, reclassifies every prior claim, and determines what compact-object work is honest going forward.

---

## 3. Pre-Gamma Book XIII Narrative (What Alpha/Beta Assumed)

### What Alpha Claimed

- "Singularity resolution: DEMONSTRATED (D1–D10; f_min > 0)" — presented as a permanent equilibrium feature
- "Two structural signature families survive: modified compactness limit and GRUT ultra-compact remnant"
- The mechanism was described as: "negative ρ_eq reduces interior mass → metric positivity restored"

### What Beta Claimed

- "Modified TOV system is closed" — TRUE
- "Three EOS-independent structural predictions: relaxed Buchdahl bound, two-zone architecture, non-monotonic mass profile" — ALL based on the assumption that ρ_eq < 0 reduces interior mass
- "The system is numerically integrable and would produce comparison-ready M-R curves"

### What Both Assumed (Implicitly)

That the static equilibrium of the GRUT Φ field (Φ = X, Φ̇ = 0) with ρ_eq = −X²/(2τ²) < 0 is the mechanism for singularity resolution. This is the Phase 4 §E narrative: "the mass function DECREASES toward the center."

**This assumption is WRONG.** The locked code (tov_interior.py, Result 1) explicitly corrects this: mass INCREASES toward the center. The static equilibrium makes the interior WORSE, not better.

---

## 4. Gamma Correction Reconstruction

### The Five-Layer Interior (Locked)

| Layer | f(R_eq) | Mechanism | Corrected understanding |
|-------|---------|-----------|----------------------|
| 1. Schwarzschild (GR) | −2.0 | Pure GR baseline | REFERENCE |
| 2. Constitutive correction | −1.0 | Phase V post-Newtonian | MODEST IMPROVEMENT |
| 3. **Static scalar TOV** | **−17.71** | **ρ_eq < 0 → mass ACCUMULATES inward** | **WORSENS by ~9× relative to GR** |
| 4. Dynamic natural rate (A=1) | −2.0 | Kinetic energy exactly cancels equilibrium deficit | RECOVERS Schwarzschild |
| 5. Supercritical (A > A_crit) | → 0 | Kinetic overshoot → metric approaches positivity | **TRANSIENT; decays on τ** |

### The Phase 4 Sign Error

Phase 4 §E stated: "The mass function DECREASES toward the center."

tov_interior.py (LOCKED, Result 1) corrects: "The interior mass function m(r) INCREASES toward the center (dm/dr < 0 means m decreases with increasing r, equivalently m increases with decreasing r). This is a CORRECTION to the Phase 4 sign interpretation."

**This correction is not a reinterpretation. It is a locked numerical result that overrides the earlier analytical sign claim.**

### The D1–D10 Combined Result (What Actually Produces f > 0)

The D1–D10 program operates DIFFERENTLY from the scalar-only TOV:
- Uses a **fixed Schwarzschild background** (not self-consistent metric)
- Adds the **O(3) hedgehog defect** (Component B: ε ~ η²/r²)
- Uses **Picard proxy closure** (not full coupled field equations)
- The DEFECT sector provides the positive-energy support that makes f > 0
- The scalar sector ALONE makes f worse

### The Transient Processing (What Happens Dynamically)

At Layer 4 (A = 1): kinetic energy from Φ̇ exactly cancels the equilibrium deficit → f recovers to −2.0 (Schwarzschild).

At Layer 5 (A > A_crit ≈ 1.062): kinetic energy exceeds the deficit → f → 0 (horizon threshold). BUT:
- This requires supercritical processing (6.2% above the natural rate)
- The processing decays as exp(−t/τ)
- After one τ, f returns to −17.71 (static value)
- A_crit > 1 is NOT shown to be physically realized
- The metric positivity window is O(τ)

---

## 5. Claim Reclassification Ledger

| # | Prior claim (Alpha/Beta) | Source | Corrected status | Action |
|---|-------------------------|--------|-----------------|--------|
| 1 | "Singularity resolution: DEMONSTRATED" | XIII Alpha | **OVERSTATED** — scalar-only worsens; combined is conditional; transient is temporary | **DOWNGRADED** to: "conditional in combined system; transient in scalar dynamics" |
| 2 | "ρ_eq < 0 reduces interior mass" | Phase 4 §E; XIII Alpha | **INCORRECT** — mass INCREASES inward (tov_interior.py locked correction) | **RETRACTED** |
| 3 | "Relaxed Buchdahl bound (C > 8/9)" | XIII Alpha/Beta | **INCORRECT for scalar-only** — scalar sector violates Buchdahl in wrong direction | **RETRACTED** (scalar-only); **OPEN** for combined system |
| 4 | "Two-zone architecture (nuclear + GRUT inner)" | XIII Beta | **INCORRECT** — scalar interior worsens, not supports | **RETRACTED** (scalar-only); **OPEN** for combined system |
| 5 | "Non-monotonic mass profile (dm/dr < 0)" | XIII Beta | **INCORRECT** — mass monotonically INCREASES inward in scalar-only sector | **RETRACTED** |
| 6 | "Modified TOV system is closed" | XIII Beta | **CORRECT** — four coupled ODEs; all T^Φ components specified | **RETAINED** |
| 7 | "Ultra-compact remnant class" | XIII Alpha | **OVERSTATED** — depends on mechanism that is conditional or transient | **DOWNGRADED** to: "potential remnant from combined system or transient processing; not established" |
| 8 | "Compact-object observational signatures" | XIII Alpha | **OVERSTATED** — signatures relied on the retracted static narrative | **DOWNGRADED** to: "conditional signatures from combined system; pending self-consistent TOV" |
| 9 | "D1–D10 f > 0 demonstrated" | D1–D10 (pre-XIII) | **RETAINED as conditional** — combined scalar+defect on fixed BG with proxy closure; defect essential | **NARROWED** — conditional, not absolute |
| 10 | "Transient A > A_crit processing" | interior_metric_closure.py | **RETAINED as conditional** — real mathematical result; A_crit not physically realized | **RETAINED** with caveats |

### Summary

| Action | Count | Claims |
|--------|-------|--------|
| **RETAINED** | 3 | Closed TOV system; D1–D10 combined (conditional); transient processing (conditional) |
| **NARROWED/DOWNGRADED** | 3 | Singularity resolution; ultra-compact remnant; observational signatures |
| **RETRACTED** | 4 | Mass reduction; Buchdahl relaxation; two-zone; non-monotonic profile |

---

## 6. Surviving Strong-Field Content

### 6.1 What Genuinely Survives

| # | Content | Authority | Regime | Caveats |
|---|---------|----------|--------|---------|
| 1 | **Static scalar-only TOV: f = −17.71** | C1 (LOCKED) | Static equilibrium | This is ADVERSE — the scalar sector worsens the interior. It survives as established negative physics. |
| 2 | **Modified TOV system is closed** | C1 (system definition) | All | Four ODEs; T^Φ algebraic; boundary conditions defined. This is a mathematical fact. |
| 3 | **Dynamic natural-rate cancellation (A=1)** | C1 (LOCKED) | Dynamic processing | Kinetic exactly cancels equilibrium → f recovers to Schwarzschild. Mathematical fact. |
| 4 | **Supercritical threshold A_crit ≈ 1.062** | C2 (frontier) | Transient dynamic | f → 0 at A = A_crit. TRANSIENT (decays on τ). A_crit NOT shown physically realized. |
| 5 | **D1–D10 combined f > 0** | C2 (frontier) | Combined scalar+defect on fixed BG | f_min = +0.37 to +0.46 across tested λ. CONDITIONAL on proxy closure + fixed background + defect sector. |
| 6 | **Phase 4 T^Φ components** | C1 (derived) | All static spherical | ρ, p_r, p_⊥ fully specified; NEC-saturating at equilibrium; anisotropic. Mathematical derivation. |

### 6.2 What Does NOT Survive

- Static scalar equilibrium as a singularity-resolution mechanism
- ρ_eq < 0 as a mass-reducing mechanism (sign error)
- Scalar-only Buchdahl relaxation
- Scalar-only two-zone architecture
- Scalar-only non-monotonic mass profile
- Stable ultra-compact remnant from scalar sector alone

---

## 7. Compact-Object Path Decision

### Option A — Equilibrium TOV Branch Program (Combined System)

**What it studies:** Self-consistent TOV integration of the FULL five-sector action (S_grav + S_macro + S_defect + S_trigger + S_portal) to determine whether equilibrium solutions with f > 0 exist on a self-consistent (not fixed-Schwarzschild) background.

**What it assumes:** That the D1–D10 result (f > 0 on fixed BG) survives on a self-consistent background. This is UNPROVEN.

**What survives from Gamma:** The D1–D10 combined result (C2) provides the motivation. The defect sector provides the support mechanism. The closed TOV system (C1) provides the integration framework.

**Main weakness:** The full five-sector self-consistent TOV is substantially harder than the scalar-only TOV. It requires coupled scalar + defect field equations on a self-consistent metric. D9's Picard iteration provides a strategy but not a guarantee of convergence on a non-Schwarzschild background. This is a significant computational undertaking.

### Option B — Transient Collapse-Processing Signature Program

**What it studies:** Whether the transient supercritical processing (A > A_crit, f → 0 for duration ~τ) produces observable signatures during gravitational collapse — e.g., modified collapse timescales, transient quasi-normal modes, or gravitational-wave signatures from the processing phase.

**What it assumes:** That A > A_crit can be physically realized during dynamic collapse (not at static equilibrium). This is PLAUSIBLE but UNPROVEN — active collapse dynamics could produce kinetic overshoot naturally.

**What survives from Gamma:** The A_crit threshold (C2) is locked. The transient processing mathematics is exact. The dynamic collapse regime is where supercritical rates are most plausible (matter is infalling rapidly → Φ̇ is large → A > 1 is natural during infall).

**Main weakness:** This requires dynamical analysis (not static TOV). The formalism for time-dependent GR + T^Φ is not fully developed (Appendix A attempted FRW; collapse.py exists but uses simplified dynamics). The observational signatures of a TRANSIENT effect are inherently harder to detect than those of a permanent feature.

### Option C — Dual-Track Program

**What it studies:** Both Option A (combined equilibrium) and Option B (transient collapse) as parallel tracks with explicit separation.

**What survives from Gamma:** Everything from both options.

**Main weakness:** Doubles the scope without doubling the available formalism. Neither track is currently strong enough to carry the frontier alone.

### Option D — Neither; Frontier Too Weak

**What it implies:** The compact-object path is closed for now. The frontier retains the D1–D10 result as conditional historical work but does not pursue further compact-object phenomenology until the combined self-consistent TOV is computed (which could take substantial effort).

### Decision

**Option C (Dual-Track) is the most honest path, but only if the two tracks are kept explicitly separate and neither is overclaimed.**

Track 1 (combined equilibrium) is the higher-leverage path because it directly addresses the D1–D10 result — the frontier's strongest remaining piece. If the combined self-consistent TOV confirms f > 0, the frontier is substantially restored. If it fails, the equilibrium path is closed.

Track 2 (transient processing) is the more speculative but also more physically interesting path because dynamic collapse is the natural regime for supercritical processing. If A > A_crit is shown to arise during infall, the transient processing becomes a genuine collapse-era phenomenology — distinct from any GR prediction.

**Neither track should be pursued until the program honestly acknowledges the Gamma correction.** That is the purpose of this document.

---

## 8. Hard-Criteria Evaluation

| Criterion | Track 1 (combined equilibrium) | Track 2 (transient collapse) |
|-----------|-------------------------------|------------------------------|
| 1. Compatible with Gamma correction | **YES** — combined system is not contradicted | **YES** — transient processing is not contradicted |
| 2. Dependence on supercritical realization | NO (equilibrium; not A > 1) | **YES** — requires A > A_crit during collapse |
| 3. Dependence on defect sector | **YES** — defect is essential for f > 0 | NO (transient is scalar-only kinetic overshoot) |
| 4. Exact vs proxy/fixed-BG reliance | **CRITICAL GAP** — D1–D10 is proxy+fixed | MODERATE (dynamics are less background-dependent) |
| 5. Compact-object specificity | HIGH (equilibrium solutions → M-R curves) | MODERATE (transient signatures less specific) |
| 6. Risk of overclaim | MODERATE (if combined TOV fails, equilibrium path dies) | MODERATE (if A > A_crit is not realized, transient path dies) |
| 7. Worth next-stage follow-up | **YES** (the actual gap: combined self-consistent TOV) | **YES** (if dynamical analysis is developed) |

---

## 9. Failure / Limitation Localization

| Limitation | Track affected | Severity |
|-----------|---------------|----------|
| **Scalar-only equilibrium WORSENS interior** | Track 1 (must use combined) | **RESOLVED by requiring combined system** |
| **D1–D10 is proxy + fixed background** | Track 1 | **KEY GAP — self-consistent integration needed** |
| **A_crit not physically realized** | Track 2 | **KEY GAP — dynamic collapse analysis needed** |
| **Transient decays on τ** | Track 2 | Inherent — transient signature is brief |
| **Full five-sector coupled system is hard** | Track 1 | Computational challenge |
| **Collapse dynamics formalism incomplete** | Track 2 | Formalism gap |

---

## 10. Frontier Consequence Audit

### Is the Frontier Weakened?

**YES — the frontier is weakened relative to pre-Gamma claims.** The scalar-only equilibrium narrative (Alpha/Beta's foundation) is eliminated. The surviving content is conditional (combined D1–D10) or transient (supercritical processing). The "demonstrated singularity resolution" must be replaced with "conditional interior support in combined system with proxy closure."

### Does Compact-Object Work Still Justify Keeping the Frontier Active?

**YES — conditionally.** The D1–D10 combined result IS real numerical work with convergent iteration. The transient processing IS a locked mathematical result. The combined self-consistent TOV IS the defined next computation. These justify continued frontier activity — not at the level previously claimed, but at a narrowed, honest level.

### Does Bridge-Worthiness Change?

**WEAKENED FURTHER.** The GGB commitment case was already weak (1 demonstrated + 1 conditional surplus after XII). Now the "demonstrated" surplus is downgraded to "conditional in combined system." The portfolio is effectively 0 demonstrated + 2 conditional + 0 GW. Bridge commitment is further from justified.

---

## 11. False-Positive Audit

| False-positive | Status | Guard |
|---------------|--------|-------|
| Transient positivity as stable remnant | **MUST NOT CLAIM** | Layer 5 decays on τ; not permanent |
| Scalar-only TOV as supportive | **MUST NOT CLAIM** | Layer 3: f = −17.71; WORSENS |
| Combined fixed-BG = full equilibrium | **MUST NOT CLAIM** | D1–D10 is proxy; self-consistent unverified |
| Alpha/Beta wording unchanged | **MUST NOT DO** | Gamma broke the foundation; wording must update |
| Old narrative shortcuts | **MUST NOT USE** | "ρ reduces mass" is the sign error |

---

## 12. GRUT-RAI Correction State-Model Requirements

Specified in the companion state-model document.

---

## 13. Program Consequence

### What Exactly Survives After Gamma?

1. The closed modified TOV system (mathematical fact; C1)
2. The D1–D10 combined result (f > 0; C2; conditional on proxy + fixed BG + defect)
3. The transient supercritical processing (A > A_crit → f → 0; C2; conditional on physical realization)
4. The Phase 4 T^Φ components (mathematical derivation; C1)
5. The adverse scalar-only static result (f = −17.71; C1; locked correction)

### What Exact Compact-Object Path Remains Honest?

**Dual-track (Option C):**
- Track 1: Combined (scalar + defect) self-consistent TOV → equilibrium compact objects
- Track 2: Transient collapse-processing phenomenology → dynamic signatures

Both tracks are conditional. Neither is the "demonstrated singularity resolution" previously claimed.

### What Should No Longer Be Claimed?

- "Singularity resolution demonstrated" (downgraded to conditional)
- "ρ_eq < 0 reduces interior mass" (retracted; sign error)
- "Relaxed Buchdahl bound" (retracted for scalar-only)
- "Two-zone architecture" (retracted for scalar-only)
- "Non-monotonic mass profile" (retracted)
- "Ultra-compact remnant class" (downgraded to conditional in combined system)
- "Comparison-ready compact-object phenomenology" (downgraded; pending combined TOV)

### What Is the Next Correct Book XIII Stage?

**Book XIII Terminal Capstone** — freeze the corrected XIII status, state the dual-track program, define the handoff for future computation (combined TOV and/or collapse dynamics).

---

## 14. Hard-Gated Summary Table

| Test | Verdict | Reason |
|------|---------|--------|
| Gamma correction fully acknowledged | **YES** | Scalar-only static TOV worsens; sign error corrected; five-layer structure stated |
| Scalar-only static TOV is adverse | **YES** | f = −17.71; LOCKED (tov_interior.py) |
| Transient supercritical positivity survives | **YES (conditional)** | A > A_crit → f → 0; transient; A_crit not realized |
| Combined scalar+defect positivity survives in bounded form | **YES (conditional)** | D1–D10: f_min > 0 on fixed BG with proxy; defect essential |
| Pre-Gamma claims reclassified honestly | **YES** | 3 retained, 3 downgraded, 4 retracted |
| At least one compact-object path remains | **YES** | Dual-track: combined equilibrium + transient collapse |
| Book XIII Delta changes frontier status | **YES** | Frontier weakened; surplus downgraded from "demonstrated" to "conditional"; path redirected to dual-track |

---

## 15. Final Verdict

**The compact-object frontier survives, but only in narrowed and corrected form.** The Gamma correction eliminates the scalar-only equilibrium narrative. The surviving content is the combined scalar+defect D1–D10 result (conditional on self-consistent verification) and the transient supercritical processing (conditional on physical realization). A dual-track program (combined equilibrium + transient collapse) is the honest next path. The frontier is weakened but retains real physics. Four prior claims are retracted, three downgraded, three retained.

---

*Strong-Field Correction, Reclassification, and Compact-Object Path Decision complete. Gamma correction frozen. 4 claims retracted. 3 claims downgraded. 3 claims retained. Dual-track program selected: combined equilibrium + transient collapse. Frontier narrowed but alive. Book XIII terminal capstone recommended.*
