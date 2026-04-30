# Path F Stage 0 — Literature on Im(Γ_CTP) on de Sitter for SM-like Matter

**Date:** April 26, 2026
**Scope:** Literature retrieval only. No calculations. No predictions of what F will produce.
**Pause gate:** After this stage, review before F.1.

---

## 1. The target object per V7 §26.2

V7's R involves imaginary structure on Euclidean S⁴, per three explicit V7 statements:

- **§26.1 line 1541:** "On Euclidean S⁴, the Euler-density contribution to the integrated effective action picks up a factor of i from the Wick rotation. In GRUT's CTP formalism, the decoherence-relevant part of the action is Im(Γ_CTP), which sees the Euler-density coefficient (with its coupling corrections encoded in ε), not the free-field ratio."

- **§26.2.3a line 1735:** "GRUT does not need the Gibbons-Hawking rotation. The −100 is not a pathology to be hidden by contour rotation — it is the topological drive for cosmic expansion."

- **§26.2.3a line 1743:** "Throughout this document, R is written as |C_Cosmo/C_FINAL| = 1.15428. C_Cosmo is negative (the conformal instability); C_FINAL is positive (the local anomaly coefficient). The physically correct computation is R = −C_Cosmo/C_FINAL = +1.15428 via explicit negation, not abs(). The sign of C_Cosmo encodes the direction of expansion; the magnitude gives the rate."

**Synthesis:** V7's R is a ratio of two anomaly-related coefficients on Euclidean S⁴, with explicit sign-tracking through Wick rotation. The "imaginary structure" is in:
- (a) C_Cosmo's negative sign from the conformal-mode instability after Wick rotation, AND
- (b) the Euler-density coefficient's i factor from Lorentzian → Euclidean transition

V7 explicitly does NOT use the GHP Ω → iΩ contour rotation. It keeps C_Cosmo negative and tracks signs explicitly.

---

## 2. What the literature actually computes

### 2.1 Im(W) on de Sitter — particle production (Zhou-Zhang 2025, arXiv:2510.13712)

A very recent (October 2025) paper directly addresses the imaginary part of the effective action in de Sitter. Key results from the paper itself (equations quoted directly):

**Eq (1):** `W = −i log⟨Out|In⟩ = −i log ∫ Dφ exp(iS[φ, g])`
Standard definition of effective action for vacuum-to-vacuum amplitude.

**Eq (2):** `|⟨Out|In⟩|² = exp(−2 Im W)`, so particle production probability `P ≈ 2 Im W`.

**Eq (12), Bogoliubov result:**

    Im W_B = −(1/4) ∫ d^d x ∫ d^d k / (2π)^d × log(1 − e^{−2πν})

where `ν = √(m² − d²/4)` for `m > d/2`.

**Section II details:** computed for a free scalar field of mass m in (d+1)-dimensional dS in the Poincaré patch with Hubble rate H = 1 (rescaled). Different regularization schemes (Bogoliubov vs Green's function) give different results in general dS but converge under explicit cutoffs.

**What this is, physically:**
- Im(W) is the *rate of vacuum decay / particle production* per unit volume in de Sitter
- The integrand `log(1 − e^{−2πν})` has the thermal Bose-Einstein structure characteristic of T_GH = H/(2π)
- For m → 0 (massless): ν → ±id/2 (imaginary), requiring analytic continuation

**Critical issue for Path F:** This Im(W) is NOT a ratio of two anomaly coefficients. It's a **dimensionful particle-production rate**. To form V7's dimensionless R, we'd need both:
- A specific Im(Γ) for "C_Cosmo" (presumably some thermal/coupling-corrected piece)
- A specific reference Re(Γ) or free-field Im(Γ) for "C_FINAL"
- Their ratio in a way that produces ~1.15

The published Im(W) for individual species doesn't naturally form such a ratio. **There is a translation gap between "what's published" and "what V7 calls R."**

### 2.2 Foundational references cited by Zhou-Zhang

From the paper's reference list:
- DeWitt, *The Global Approach to Quantum Field Theory* (2003) — foundational for effective action in curved space
- Parker-Toms, *Quantum Field Theory in Curved Spacetime* (2009)
- Birrell-Davies, *Quantum Fields in Curved Space* (1984)
- Vassilevich heat kernel manual (already used for Path D)
- Gelis-Tanji "Schwinger mechanism revisited" (2016) — for Schwinger-effect analog
- Ford "Cosmological particle production: a review" (2021)
- Mottola 1985 "Particle Production in de Sitter Space" — classical reference

These give Im(W) for individual field types (scalar, fermion, vector) but always in the "particle production rate" framing. Not directly as ratios.

### 2.3 Calzetta-Hu — CTP on curved backgrounds

Calzetta-Hu's textbook (*Nonequilibrium Quantum Field Theory*, Cambridge 2008) develops CTP/Schwinger-Keldysh on curved backgrounds. The CTP effective action Γ_CTP includes both real and imaginary parts:

- Re(Γ_CTP): deterministic dynamics (equations of motion)
- Im(Γ_CTP): noise kernel (fluctuation-dissipation)

V7 §5 builds on this: `Im(S_CTP) = (1/2) z_a N z_a` (V7 line 6264).

**For SM matter on dS⁴:** Calzetta-Hu provides the framework but **doesn't tabulate per-species Im(Γ_CTP) values** for SM-like content. The general framework is well-published; the specific calculation for SM on dS is not (in what I've found).

### 2.4 Anastopoulos-Hu 2013 (CQG 30, 165007)

This is V7's foundational reference for the gravitational decoherence noise kernel `N_grav = G/(ℏ|x−x'|)`. The paper computes Im(S_IF) for the Newtonian gravitational influence functional — i.e., **lab-scale gravitational decoherence**, not cosmological-scale Im(Γ) on dS.

V7 explicitly uses this for the decoherence sector (Λ_grav formula), not for the cosmological R calculation.

**Status:** Anastopoulos-Hu gives the noise-kernel piece of V7's decoherence sector. It's adjacent to but not the same as what Path F needs.

### 2.5 Mottola 1985 "Particle Production in de Sitter Space"

Classical reference for particle creation in dS. Computes scalar field Bogoliubov coefficients in the Poincaré patch and the resulting particle production rate. Same kind of object as Zhou-Zhang's Im(W_B), in earlier notation.

**Status:** foundational for the particle-production interpretation of Im(W). Not extended to gauge bosons or fermions in the same paper.

### 2.6 Spradlin-Strominger-Volovich "Les Houches Lectures on de Sitter Space" (2001, hep-th/0110007)

Lecture-style review covering dS QFT, including in/out vacua, Bogoliubov coefficients, and effective action. Pedagogical level; useful for pinning conventions but not for new computational results.

---

## 3. The translation gap

**The published literature gives clear, computable values for:**
- Im(W) for individual field types (scalar, fermion, vector) on de Sitter as particle-production rates
- The Bogoliubov coefficients between Bunch-Davies/in vacuum and out vacuum
- Per-volume rates of vacuum decay
- The thermal Bose-Einstein structure at T_GH = H/(2π)

**The published literature does NOT directly give:**
- A ratio of two anomaly coefficients with imaginary structure that maps onto V7's R = |C_Cosmo/C_FINAL|
- A per-SM-species tabulation of trace-anomaly imaginary contributions designed for cosmological-scale evaluation
- A specific construction matching V7's "C_Cosmo (negative) / C_FINAL (positive)" decomposition

The **translation from published Im(W) to V7's R is not in the literature**. That translation is the gap that V7 §26 leaves open and that Path F was supposed to address.

---

## 4. Assessment of the three Candidate identifications

From the previous brainstorm:

### Candidate I: R = |Im(Γ_CTP) / Re(Γ_CTP)| at a specific scale

**What we'd need:** Im(Γ_CTP) and Re(Γ_CTP) for SM matter on dS⁴ at the same renormalization scale and convention.

**Published support:**
- Im(Γ_CTP) ~ Im(W_particle_production): published per species (Zhou-Zhang, Mottola, et al.)
- Re(Γ_CTP) on dS: trace anomaly determines it on dS via ⟨T_μν⟩ = (1/4) g_μν ⟨T⟩; standard published a, c values give Re(Γ_CTP) at 1-loop

**Tractability:** Computing the ratio is mechanical IF we accept this identification. But:
- Im(W) for massless gauge fields and conformally-coupled scalars is divergent or zero at 1-loop (conformal invariance) → ratio is ill-defined or trivial
- For massive fields, Im(W) involves cutoff-dependent integrals → ratio is regulator-dependent
- **The ratio is not a clean dimensionless number without specific cutoff/normalization choices**

**Verdict:** Candidate I is *computable* but its value depends on regularization choices. The "1.15428" wouldn't naturally fall out of any standard convention.

### Candidate II: R involves the conformal-mode contribution with Wick-rotation i factor

**What we'd need:** The specific contribution of the gravitational conformal mode to the trace anomaly on Euclidean S⁴, with the GHP-rotation i factor explicitly tracked.

**Published support:**
- GHP 1978 paper on Euclidean quantum gravity establishes the conformal-mode-instability problem
- Christensen-Duff 1978 computes graviton trace-anomaly contributions
- The "−100 = −(Σ Y²)²" identification in V7 §26.2.6 attempts to identify the conformal-mode coefficient with the SM hypercharge structure

**Tractability:** The Christensen-Duff graviton trace-anomaly values exist and could be combined with SM hypercharge structure. **This is the closest match to V7's actual narrative** (line 1735: "the −100 is the conformal instability ... topological drive for cosmic expansion").

**Verdict:** Candidate II is the most aligned with V7's stated physical picture. It would require sourcing graviton trace-anomaly values from Christensen-Duff and combining with SM hypercharge sums. Tractable in-pipeline if those values are available.

### Candidate III: R = ratio of CTP forward/backward branch coefficients

**What we'd need:** Specific computation of how the forward and backward CTP branches differ in their Euler-coefficient contribution on dS.

**Published support:**
- Calzetta-Hu provides the general CTP framework
- The forward/backward branch transformation involves complex-conjugation in Schwinger-Keldysh
- Specific calculation for SM on dS is not in the literature I've found

**Verdict:** Candidate III is theoretically motivated but lacks specific published machinery to compute it for SM content. Would require new theoretical work.

---

## 5. Recommended interpretation

**Candidate II (conformal-mode-included anomaly with i factor)** has the cleanest published support and aligns with V7's "−100 is the conformal instability" narrative.

In this reading, V7's R = 1.15428 should be reproducible by:
1. Computing the gravitational conformal-mode trace-anomaly coefficient on S⁴ (Christensen-Duff 1978 type calculation)
2. Including the SM matter trace-anomaly contributions
3. Tracking signs explicitly through Wick rotation (the i factor turns specific terms negative, giving C_Cosmo's sign)
4. Forming the ratio |C_Cosmo / C_FINAL|

**This is essentially the same calculation as the TJI Phase-1 specialist work** that V7 §26.2.5 already identifies as "~3 weeks of specialist work to verify the −100 normalization." Path F under Candidate II reduces to: this is the calculation that would verify V7's R = 1.15 from first principles, and it's a specialist task.

---

## 6. Tractability assessment

| Aspect | Tractable in-pipeline? | Notes |
|:---|:---|:---|
| Compute Im(W_particle_production) for individual SM species on dS | **Yes** | Standard published formulas (Zhou-Zhang, Mottola). Mechanical. |
| Compute Re(Γ_CTP) for SM on dS at 1-loop | **Yes** | This is essentially Path D's a_SM × Euler density on dS. We have it. |
| Form a "natural" Im/Re ratio that gives ~1.15 | **No** | Multiple regularization/scale choices give different ratios; no canonical answer falls out. |
| Sourceable graviton trace-anomaly values for Candidate II | **Probably** | Christensen-Duff 1978 has them; need to fetch and verify. |
| Compute the full conformal-mode + SM contribution to C_Cosmo with sign tracking | **Hard** | This is essentially the TJI Phase-1 specialist task V7 already identified. |
| Verify R = 1.15428 from first principles | **Specialist work, not in-pipeline** | The 3-loop CTP-on-S⁴ machinery V7 §26.2 outlines hasn't been completed in literature. |

**Honest verdict:** Path F as literally specified (compute Im(Γ_CTP) on dS and form V7's R from it) is **not tractable in-pipeline at the level needed to produce 1.15**. The published machinery gives Im(W) for particle production, which is a different object from V7's R.

Two tractable sub-paths emerge:

### Path F-tractable: Compute SM Im(W) on dS for documentation purposes

We can compute the per-species Im(W) values from Zhou-Zhang's Eq (12) and sum over SM content. The result would be a **dimensionful particle-production rate**, not a dimensionless R. It would document "what the SM does on dS in terms of particle production" but wouldn't directly produce V7's 1.15428.

This is a real published-physics calculation, just not the one that gives R.

### Path F-specialist: TJI Phase-1 with conformal-mode tracking

The actual calculation that would verify V7's R = 1.15428 is the 3-loop CTP-on-S⁴ machinery V7 §26.2 already identifies. This is specialist work. Path F doesn't shortcut it.

---

## 7. What this means for the brainstorm

The user's hypothesis "imaginary was necessary in the original derivation" is **structurally correct** for V7's framework — V7 explicitly tracks imaginary structure through Wick rotation and the conformal-mode instability. But the published Im(Γ) literature doesn't directly compute V7's R. There's a translation gap.

**Implication for committing to a number:**

| Number | Source | What it actually computes | Defensibility |
|:---|:---|:---|:---|
| V7's 1.15428 | Original derivation, partially documented in §26 | Trace-anomaly ratio with conformal-mode + SM hypercharge structure on S⁴ | Specialist verification needed |
| Path D's 1.1726 | KS 2011 + Duff 1994 + SM content (1-loop) | SM 1-loop a/c (Euler/Weyl² ratio) | **Fully sourced and verifiable** |
| Path F number (hypothetical) | Im(Γ_CTP) ratio — but the ratio identification is undefined | A particle-production-style quantity, possibly Im(W)_SM | **Cannot be cleanly extracted from published Im(W) without more theoretical work** |

**Path D is the most defensible derivation we have.** Path F would either confirm V7's R (if the specialist TJI calculation is done) or provide a different number (if a less rigorous Im(W)-summing approach is taken). Neither is in-pipeline tractable at the level that produces 1.15.

---

## 8. Recommendation: pause and decide before F.1

Three options for the user's decision:

### Option F-A: Run F.1 as Path F-tractable
Compute Im(W)_SM (sum of per-species particle production rates) on dS at T_GH for SM content. Document the result. Accept that it's not directly V7's R but is a real published-physics calculation for SM on dS. The output will be a dimensionful rate, possibly with specific T_GH-dependence; comparison to "1.15" is not clean.

### Option F-B: Defer F.1 to specialist
Acknowledge that the in-pipeline Path F can't reproduce V7's R, recommend that the TJI Phase-1 specialist task be the route. This effectively closes Path F as an in-pipeline exercise.

### Option F-C: Pivot to Candidate II — sourcing Christensen-Duff graviton anomaly values
Fetch Christensen-Duff 1978 specifically and compute the conformal-mode + SM contribution with sign tracking. This is the closest in-pipeline match to V7's actual physics narrative. Tractable but more work than F-A.

### Option F-Honesty: Commit to Path D as the canonical derivation
Path F's literature scoping has shown that V7's R can't be cleanly derived in-pipeline at the precision V7 originally claimed. **Path D's 1.1726 is the most defensible number we have as a derived R for the cosmological sector.** Reframe V8 §12 around it, document V7's 1.15428 as a heuristic that the specialist TJI work could potentially verify or refine, accept the 4% Planck tension (or 0.01% if Dirac neutrinos) as the honest current prediction.

---

## 9. Sources cited

- [Zhou-Zhang 2025 "On the Imaginary Part of the Effective Action in de Sitter Spacetime with Different Regularization Schemes" (arXiv:2510.13712)](https://arxiv.org/abs/2510.13712) — primary recent reference for Im(W) on dS
- [Cosmological particle production review (Ford 2021)](https://iopscience.iop.org/article/10.1088/1361-6633/ac1b23)
- [Schwinger mechanism revisited (Gelis-Tanji 2016)](https://www.sciencedirect.com/science/article/pii/S0146641015000800)
- Calzetta-Hu, *Nonequilibrium Quantum Field Theory* (Cambridge 2008) — CTP framework
- Anastopoulos-Hu, CQG 30, 165007 (2013) — V7's noise-kernel basis (decoherence sector)
- Mottola 1985 "Particle Production in de Sitter Space" — foundational, accessed via arXiv if needed
- Birrell-Davies, *QFT in Curved Space* (1982) — standard textbook
- Parker-Toms, *QFT in Curved Spacetime* (2009) — modern textbook
- Christensen-Duff 1978 — graviton trace anomaly (not yet fetched; needed for Candidate II)
- V7 local: §26.1 line 1541, §26.2.3a lines 1735, 1743, §5 line 6264
- [Komargodski-Schwimmer 2011 a-theorem](https://arxiv.org/abs/1107.3987) — Path D primary source
- [Duff 1994 "Twenty years of the Weyl anomaly"](https://arxiv.org/abs/hep-th/9308075) — Path D cross-check

## 10. Pause-gate decision

Stage F.0 is complete. Findings:
- V7's R has imaginary structure (sign tracking, Wick rotation, conformal-mode); user's intuition was correct
- Published Im(Γ) on dS gives particle-production rates, not directly V7's R ratio
- The three Candidate identifications have varying support; Candidate II is most aligned with V7's narrative
- **Path F as literally specified is not in-pipeline tractable** at the level that reproduces V7's 1.15428

Awaiting user decision: F-A (mechanical Im(W)_SM), F-B (defer to specialist), F-C (pivot to Candidate II), or F-Honesty (commit to Path D).

**Sources:**
- [Zhou-Zhang 2025 arXiv:2510.13712](https://arxiv.org/abs/2510.13712)
- [Ford 2021 cosmological particle production review](https://iopscience.iop.org/article/10.1088/1361-6633/ac1b23)
- [Komargodski-Schwimmer 2011](https://arxiv.org/abs/1107.3987)
- [Duff 1994](https://arxiv.org/abs/hep-th/9308075)
