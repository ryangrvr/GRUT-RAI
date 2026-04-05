# Book XVI Zenodo Upload Briefing

## Instructions for Claude Chat

You are creating two documents for the next GRUT Zenodo upload: the Book XVI main manuscript and a companion audit ledger. Below is everything you need.

---

# DOCUMENT 1: Main Book XVI Manuscript

## Title

**Book XVI: Quasi-Static Rate Analysis, Equilibrium Reducibility, and the Gravity-Distinction Freeze**

## Author

D. Ryan Grover

## What This Document Is

The readable, publication-quality manuscript presenting Book XVI of the GRUT Theory-of-Everything program. This is the stage where the equilibrium gravity-distinction route is tested, found to be both reducible and observationally silent, and formally frozen. The program recenters on its dynamical core. Book XVI has THREE stages: Alpha (quasi-static rate analysis and sign error discovery), Beta (weak-field tau-constraint audit and equilibrium reducibility), and Terminal (equilibrium gravity freeze and dynamics recentering). Same formal voice as prior books.

## Source Hierarchy

- **Controlling frame:** Book XV Terminal established the implementation handoff for the exact Layer 3 computation. Book XVI answers the rate-amplification question inherited from XV and tests the surviving equilibrium gravity claim.
- **Book XVI audits:** 3 target stages (Alpha, Beta, Terminal), 9 documents produced the results.
- **Critical existing canon:** D7/D8 source amplification model; D9 Picard iteration; first-order constitutive equation; Phase 4 equilibrium T^Phi (xAct-verified); Birkhoff's theorem; PPN framework.
- **Code produced:** `grut/quasi_static_rate.py` (~500 lines); `grut/weak_field_tau_constraint.py` (~300 lines).

## Critical Narrative Arc

Book XVI has a three-act structure: SIGN ERROR, REDUCIBILITY AND SILENCE, FREEZE AND RECENTERING.

**Act 1 (Alpha -- The Sign Error):** XVI Alpha answers the XV Terminal handoff question: is the scalar relaxation rate amplified? The answer is devastatingly clear. A self-consistent A_eff bootstrap computation reveals that the D7/D8 source amplification model (m_eff = M + beta * Sigma_defect) has a STRUCTURAL SIGN ERROR. By Birkhoff's theorem, the defect energy between R_eq and R_ext is mass ABOVE R_eq -- it is not enclosed at R_eq and must be SUBTRACTED from M, not added. The correct enclosed mass is m = M - Sigma ~ 0.05, giving A_eff ~ 0.11 (not 2). The proxy overpredicts by a factor of 17 at lambda = 25. XV Beta's f >> 0 result was an artifact. All conditional surpluses collapse from 2-3 to 0. The proper-time relaxation rate is ALWAYS 1/tau -- the first-order constitutive equation has no rate amplification mechanism.

**Act 2 (Beta -- Reducibility and Silence):** XVI Beta tests whether the surviving equilibrium T^Phi (rho_eq = -X^2 / (2 tau^2), w = -1) constitutes an irreducible, testable gravity claim. Three findings converge on NO:
1. REDUCIBILITY: At equilibrium, the GRUT scalar action is the standard action of a massive scalar field (m_phi = 1/tau) sourced by gravity. The T^Phi is identical to GR + scalar. No structural novelty at equilibrium.
2. OBSERVATIONAL SILENCE: The weak-field metric correction delta_f = -4 pi M^2 / (tau^2 r^2) is structurally suppressed by c^2 in tau_geometric. At tau = 1 second: |delta_beta| = 1.4e-10, six orders below Cassini. At physical tau values (t_dyn): corrections are 10^-16 or smaller.
3. SOURCE AMBIGUITY: In Schwarzschild exterior, R = 0. If X is curvature-sourced, X = 0 and there is no correction at all.

**Act 3 (Terminal -- The Freeze and Recentering):** Book XVI closes with the equilibrium gravity-distinction route formally frozen on three independent grounds. 10 failed routes are logged. The program recenters on its surviving irreducible content: the dynamical constitutive core (5 proven theorems: forward semigroup, Lyapunov, dissipative balance, T-breaking, monotone contraction). These are irreducible against conservative theories but generic among open systems. The biology scaffold (26 zero-cost targets) and matter-within-GR baseline are preserved. Cost remains 16/11/1/6.

## Required Sections

### Front matter
- Title, author, abstract
- Status: equilibrium gravity-distinction route frozen; sign error discovered in D7/D8 model; equilibrium T^Phi reducible to GR + massive scalar; observationally silent; program recentered on dynamical core; surplus portfolio: 0+0

### 1. Purpose and Boundary
- XVI answers three questions: (1) Is the scalar relaxation rate amplified? (2) Is the equilibrium T^Phi an irreducible gravity claim? (3) What survives?
- The key finding: all three answers are negative. The equilibrium gravity route is closed. The dynamical core survives.

### 2. Inherited Foundation from Book XV
- XV specified the exact Layer 3 computation and assembled structural evidence for low-lambda survival
- XV's structural evidence relied on the D7/D8 source amplification model
- The conditional surplus portfolio stood at 0 demonstrated + 2-3 conditional
- Implementation handoff was defined for D9 Picard code modification

### 3. Alpha: Self-Consistent Rate Analysis and the Sign Error
- The A_eff bootstrap computation: self-consistent vs. proxy values
- Birkhoff's theorem argument: defect energy between R_eq and R_ext is mass ABOVE R_eq, not enclosed
- The sign reversal: m_eff = M + beta * Sigma (WRONG) becomes m = M - Sigma (CORRECT)
- Quantitative collapse: A_eff_proxy = 1.94 vs. A_eff_SC = 0.11 at lambda = 25 (ratio = 0.057)
- The proper-time relaxation rate is constitutively fixed at 1/tau = 0.8165
- Surplus collapse: all conditional surpluses drop from 2-3 to 0
- Code: `grut/quasi_static_rate.py` (~500 lines)

**Table 1: Self-Consistent A_eff vs D7/D8 Proxy**

| lambda | A_eff_proxy | A_eff_SC | Ratio (SC/proxy) | Classification |
|--------|------------|----------|-------------------|---------------|
| 5      | ~1.2       | ~0.08    | ~0.07             | OVERPREDICTED |
| 10     | ~1.5       | ~0.09    | ~0.06             | OVERPREDICTED |
| 25     | 1.94       | 0.11     | 0.057             | OVERPREDICTED |
| 50     | ~2.3       | ~0.12    | ~0.05             | OVERPREDICTED |
| 100    | ~2.8       | ~0.13    | ~0.05             | OVERPREDICTED |

**Table 2: Sign Error Reversal**

| Quantity | D7/D8 Model (WRONG) | Correct (Birkhoff) | Physical Reason |
|----------|---------------------|-------------------|-----------------|
| Enclosed mass at R_eq | m_eff = M + beta * Sigma | m = M - Sigma | Defect energy is ABOVE R_eq, not enclosed |
| Direction of correction | Amplification (source grows) | Reduction (source shrinks) | Birkhoff: only enclosed mass gravitates |
| Net m_eff at lambda=25 | ~1.05 M | ~0.05 M | Factor of ~20 reversal |
| Consequence for f_min | f >> 0 (predicted survival) | Artifact of sign error | Conditional surplus was never real |

**Table 3: Relaxation Rate Extraction**

| Quantity | Value | Source | Status |
|----------|-------|--------|--------|
| Proper-time relaxation rate | 1/tau = 0.8165 | First-order constitutive equation | ALWAYS; constitutive property |
| D7/D8 proxy prediction | f >> 1 (amplified) | Source amplification model | WRONG (sign error) |
| Self-consistent result | A_eff ~ 0.11 < 1 | Bootstrap computation | No amplification |
| Rate amplification mechanism | None | Constitutive structure | No mechanism exists |

### 4. Beta: Equilibrium Reducibility
- At equilibrium, the GRUT scalar action reduces to a standard massive scalar field action with m_phi = 1/tau
- The equilibrium T^Phi (rho_eq = -X^2 / (2 tau^2), w = -1) is identical to what GR + massive scalar produces
- No structural novelty at equilibrium: the claim is REDUCIBLE

**Table 4: Irreducibility Comparison**

| Theory | Relation to Equilibrium GRUT | Structurally Distinct? | Irreducible? |
|--------|------------------------------|----------------------|-------------|
| GR + massive scalar (m = 1/tau) | IDENTICAL at equilibrium | NO | REDUCIBLE |
| R^2 gravity (Starobinsky) | Different field equations, different DOF count | YES | NOT EQUIVALENT |
| Semiclassical gravity | Different origin (quantum), different structure | YES | NOT EQUIVALENT |
| Full dynamical GRUT | Contains dissipation, T-breaking, semigroup | YES | IRREDUCIBLE (dynamics only) |

### 5. Beta: Weak-Field Observational Silence
- The metric correction: delta_f(r) = -4 pi M^2 / (tau^2 r^2) in geometric units
- The PPN parameter shift: delta_beta = 4 pi / tau^2_geometric
- Structural suppression by c^2 in tau_geometric renders all corrections negligible

**Table 5: Weak-Field Correction at Key Locations**

| Location | r (geometric) | delta_f | |delta_beta| | Cassini Bound | Status |
|----------|---------------|---------|-------------|---------------|--------|
| Mercury perihelion | ~2.5e10 cm | ~10^-16 | ~10^-16 | 2.3e-5 | SILENT |
| Earth orbit | ~7.5e10 cm | ~10^-17 | ~10^-16 | 2.3e-5 | SILENT |
| Solar surface | ~3.5e10 cm | ~10^-16 | ~10^-16 | 2.3e-5 | SILENT |
| At tau = 1 s (best case) | any | -- | 1.4e-10 | 2.3e-5 | SILENT (6 orders below) |

**Table 6: Tau Constraint from Precision Gravity**

| Experiment | Bound on |delta_beta| | Implied tau constraint | Physical tau | Status |
|-----------|-------------------------|----------------------|-------------|--------|
| Cassini (gamma) | 2.3e-5 | tau > 2.5 ms | >> 2.5 ms | TRIVIALLY SATISFIED |
| Lunar Laser Ranging | ~10^-4 | tau > ~1 ms | >> 1 ms | TRIVIALLY SATISFIED |
| Binary pulsars | ~10^-3 | tau > ~0.3 ms | >> 0.3 ms | TRIVIALLY SATISFIED |

### 6. Beta: Source Ambiguity
- In Schwarzschild exterior, R = 0 (Ricci-flat)
- If X is curvature-sourced (X proportional to R or curvature invariants), then X = 0 in vacuum
- In that case there is NO equilibrium correction at all -- not small, but exactly zero
- This removes even the residual claim to a nonzero equilibrium gravity signature

### 7. Terminal: The Equilibrium Gravity Freeze
- Three independent grounds for freezing: (1) reducibility, (2) observational silence, (3) source ambiguity
- The freeze is PERMANENT -- cannot be reopened by narrative rebranding, redefinition, or parameter tuning

**Table 7: Frozen Route Table**

| # | Route | Book Frozen | Reason |
|---|-------|-------------|--------|
| 1 | Compact-object horizon replacement | XIII | Collapse at high lambda |
| 2 | D7 source amplification | XVI Alpha | Sign error (Birkhoff) |
| 3 | D8 portal stabilization | XVI Alpha | Relied on D7 model |
| 4 | Rate amplification | XVI Alpha | No mechanism; constitutive |
| 5 | Equilibrium gravity distinction | XVI Beta | Reducible to GR + scalar |
| 6 | Weak-field PPN signature | XVI Beta | Observationally silent |
| 7 | Strong-field equilibrium | XVI Alpha | Conditional surplus collapsed |
| 8 | Layer 3 survival (low-lambda) | XVI Alpha | D7/D8 evidence was artifact |
| 9 | Curvature-sourced equilibrium | XVI Beta | Source ambiguity (R=0) |
| 10 | Equilibrium novelty (any form) | XVI Terminal | All routes frozen |

### 8. Terminal: Surviving Content
- The program recenters on its surviving irreducible content

**Table 8: Surviving Content**

| Content | Status | Irreducible Against | Limitation |
|---------|--------|-------------------|-----------|
| Forward semigroup theorem | PROVEN | Conservative theories (no semigroup) | Generic among open systems |
| Lyapunov theorem | PROVEN | Conservative theories (no Lyapunov) | Generic among open systems |
| Dissipative balance theorem | PROVEN | Conservative theories (no dissipation) | Generic among open systems |
| T-breaking theorem | PROVEN | T-symmetric theories | Generic among open systems |
| Monotone contraction theorem | PROVEN | Conservative theories | Generic among open systems |
| Matter-within-GR baseline | PRESERVED | -- | Observationally equivalent to GR in matter sector |
| Biology scaffold (26 targets) | PRESERVED (zero-cost) | -- | Unanchored to gravity |

**Table 9: Surplus Portfolio Before/After**

| Category | Before XVI | After XVI | Change |
|----------|-----------|-----------|--------|
| Demonstrated surpluses | 0 | 0 | -- |
| Conditional surpluses | 2-3 | 0 | COLLAPSED (sign error) |
| Pending surpluses | 0 | 0 | -- |
| **Total** | **0 + 2-3** | **0 + 0** | **Fully collapsed** |

### 9. Claim Status and Cost Ledger

**Table 10: Final Claim Status**

| # | Claim Domain | Status | Book |
|---|-------------|--------|------|
| 1 | Forward semigroup | RETAINED (proven) | IV |
| 2 | Lyapunov stability | RETAINED (proven) | IV |
| 3 | Dissipative balance | RETAINED (proven) | V |
| 4 | T-breaking | RETAINED (proven) | V |
| 5 | Monotone contraction | RETAINED (proven) | VI |
| 6 | Compact-object horizon replacement | FROZEN | XIII |
| 7 | Strong-field equilibrium survival | FROZEN | XVI |
| 8 | D7 source amplification | RETRACTED (sign error) | XVI |
| 9 | D8 portal stabilization | FROZEN | XVI |
| 10 | Rate amplification | FROZEN | XVI |
| 11 | Equilibrium gravity distinction | FROZEN | XVI |
| 12 | Weak-field PPN signature | FROZEN | XVI |
| 13 | Layer 3 low-lambda survival | FROZEN | XVI |
| 14 | Biology scaffold | RETAINED (zero-cost) | -- |
| 15 | Matter-within-GR baseline | RETAINED | -- |
| 16 | Sixth bridge (ToE completion) | NOT COMMITTED | -- |

- Cost: 16/11/1/6 (unchanged from XV)
- Surplus: 0+0 (fully collapsed from 0+2-3)
- All XVI stages: +0 cost (analysis and audit only; no new axioms)

### 10. Nonclaims
1. XVI does NOT claim the sign error invalidates the defect architecture mathematically (D1-D10 math intact)
2. XVI does NOT claim the constitutive equation itself is wrong
3. XVI does NOT claim the program is finished
4. XVI does NOT claim equilibrium gravity distinction under any rewording
5. XVI does NOT claim weak-field observational relevance
6. XVI does NOT claim the dynamical theorems have observational anchoring
7. The frozen equilibrium route cannot be reopened by narrative rebranding
8. Observational silence is not "consistency with observation" -- GR also predicts zero correction
9. Reducibility is not "hidden novelty"
10. One collapsed frontier does not mean the whole program fails (biology, baseline, dynamics survive)
11. XVI does NOT restore ToE status or commit the sixth bridge
12. The 5 dynamical theorems are structurally real but observationally unanchored

### 11. XIII-XVI Arc Summary

**Table 11: XIII-XVI Arc Summary**

| Book | Focus | Key Result | Net Effect |
|------|-------|-----------|-----------|
| XIII | Compact-object rescue | Horizon replacement fails at high lambda | Equilibrium path narrowed |
| XIV | Three-layer decomposition | Layers 1-2 computed; Layer 3 estimated | Frontier characterized |
| XV | Layer 3 specification | Exact system specified; structural evidence assembled | Implementation handoff |
| XVI | Rate analysis + equilibrium audit | Sign error; reducibility; observational silence | Equilibrium route FROZEN |

### 12. What Comes Next

**Table 12: Next-Stage Handoff**

| Priority | Task | Target |
|----------|------|--------|
| 1 | Dynamical consolidation | Collect 5 proven theorems into unified dynamical framework |
| 2 | Irreducibility sharpening | Characterize exactly what class of open-system theories shares the 5 theorems |
| 3 | Biology scaffold connection | Assess whether 26 zero-cost targets can be connected to dynamical core |
| 4 | Honest scope assessment | Define what program CAN claim without equilibrium gravity |
| 5 | Archive and publish | XVI closes the equilibrium gravity chapter; dynamics chapter opens |

- The program transitions from gravity-distinction testing to dynamical-core consolidation
- No equilibrium gravity claims survive; the next stage must work entirely within the dynamical domain
- The sixth bridge remains uncommitted

## Key Formal Objects

| Object | Expression / Value | Source |
|--------|-------------------|--------|
| D7/D8 sign error | m_eff = M + Sigma (WRONG) --> m = M - Sigma (Birkhoff) | XVI Alpha |
| Proxy vs self-consistent | A_eff_proxy = 1.94; A_eff_SC = 0.11; ratio = 0.057 | XVI Alpha (lambda=25) |
| Proper-time rate | 1/tau = 0.8165 (always; constitutive property) | XVI Alpha |
| Weak-field correction | delta_f(r) = -4 pi M^2 / (tau^2 r^2) | XVI Beta (geometric units) |
| PPN shift | delta_beta = 4 pi / tau^2_geometric | XVI Beta |
| Best-case PPN | |delta_beta| = 1.4e-10 at tau = 1 s (vs Cassini 2.3e-5) | XVI Beta |
| Equilibrium energy density | rho_eq = -X^2 / (2 tau^2) (Phase 4, xAct-verified) | XVI Beta |
| Equilibrium equivalence | T^Phi identical to GR + massive scalar (m_phi = 1/tau) | XVI Beta |
| Rate analysis code | grut/quasi_static_rate.py (~500 lines) | XVI Alpha |
| Tau constraint code | grut/weak_field_tau_constraint.py (~300 lines) | XVI Beta |
| Cost | 16/11/1/6 (unchanged) | XVI Terminal |
| Surplus | 0+0 (fully collapsed from 0+2-3) | XVI Terminal |

## Critical Formulas

1. **Sign error (Birkhoff):** The defect energy Sigma between R_eq and R_ext is mass ABOVE R_eq. By Birkhoff's theorem, only enclosed mass gravitates at R_eq. Therefore: m_enclosed = M - Sigma, NOT M + Sigma.

2. **Self-consistent A_eff:** A_eff_SC = (dm/dSigma)|_{self-consistent} ~ 0.11 at lambda = 25. The D7/D8 proxy gave A_eff_proxy = 1.94. The proxy overpredicts by a factor of 17.

3. **Proper-time rate:** The first-order constitutive equation dX/dtau = -X/tau gives a relaxation rate of exactly 1/tau. This is a constitutive property of the equation -- there is no mechanism for amplification.

4. **Weak-field metric correction:** delta_f(r) = -4 pi M^2 / (tau^2 r^2) in geometric units. The c^2 factor in tau_geometric = tau * c structurally suppresses this to negligible levels.

5. **PPN parameter shift:** delta_beta = 4 pi / tau^2_geometric. At tau = 1 s: tau_geometric = 3e10 cm, giving |delta_beta| = 4 pi / (9e20) = 1.4e-10. Cassini bound is 2.3e-5. Six orders of magnitude below.

6. **Equilibrium action reducibility:** At equilibrium (dX/dtau = 0), the GRUT scalar action reduces to S = integral[ -X^2/(2 tau^2) + (1/2)(nabla X)^2 ] sqrt(-g) d^4x, which is exactly a massive scalar field with m_phi = 1/tau.

## Style
- Formal prose; same voice as prior books
- The three-act structure (sign error, reducibility + silence, freeze + recentering) is the structural spine
- NEVER claim equilibrium gravity distinction survives
- NEVER claim observational relevance for equilibrium sector
- NEVER soften the freeze with hedging language
- NEVER rebrand reducibility as "embedding" or "natural extension"
- The honest tone: "the equilibrium gravity route is closed on three independent grounds; the dynamical core survives but is observationally unanchored"

## Length
Approximately 14-18 pages.

---

# DOCUMENT 2: Companion Audit Ledger

## Title
**Book XVI: Companion Audit Ledger -- Quasi-Static Rate Analysis, Equilibrium Reducibility, and the Gravity-Distinction Freeze**

## Required Content
1. Alpha summary table (sign error discovery, surplus collapse)
2. Beta summary table (reducibility, silence, source ambiguity)
3. Terminal summary table (freeze, recentering)
4. Self-consistent A_eff vs D7/D8 proxy table (5 lambda values)
5. Sign error reversal table
6. Relaxation rate extraction table
7. Irreducibility comparison table
8. Weak-field correction table (Mercury, Earth, solar surface)
9. Tau constraint from precision gravity table
10. Frozen route table (10 routes)
11. Surviving content table (5 theorems + baseline + biology)
12. Surplus portfolio before/after table
13. XIII-XVI arc summary table
14. Final claim status table (16 claims)
15. Hard-criteria matrix
16. Limitations table
17. Frontier consequence table
18. All 9 Book XVI documents indexed
19. Key formal objects
20. Next-stage handoff table

**Table: Hard-Criteria Matrix**

| Criterion | XVI Status | Evidence |
|-----------|-----------|----------|
| Mathematical consistency | PASS | D1-D10 math intact; sign error is physical, not mathematical |
| Observational compatibility | PASS (trivially) | Corrections below all current bounds |
| Irreducibility (equilibrium) | FAIL | Reducible to GR + massive scalar |
| Irreducibility (dynamics) | PASS | 5 theorems irreducible vs conservative theories |
| Testability (equilibrium) | FAIL | Observationally silent |
| Testability (dynamics) | OPEN | Unanchored; requires further work |
| Cost discipline | PASS | 16/11/1/6 unchanged; 0 new axioms |
| Honest accounting | PASS | Sign error disclosed; surpluses collapsed; routes frozen |

## Audit Document Index

**Alpha (3 documents):**
- docs/BOOK_XVI_TARGET_ALPHA_QUASI_STATIC_RATE_ANALYSIS.md (or equivalent filename)
- docs/BOOK_XVI_TARGET_ALPHA_RATE_BRIDGE_MATRIX.md (or equivalent filename)
- docs/BOOK_XVI_TARGET_ALPHA_RATE_BRIDGE_STATE_MODEL.md (or equivalent filename)

**Beta (3 documents):**
- docs/BOOK_XVI_TARGET_BETA_IRREDUCIBLE_CONSTITUTIVE_GRAVITY_TAU_CONSTRAINT_AUDIT.md (or equivalent filename)
- docs/BOOK_XVI_TARGET_BETA_WEAK_FIELD_CONSTRAINT_MATRIX.md (or equivalent filename)
- docs/BOOK_XVI_TARGET_BETA_WEAK_FIELD_STATE_MODEL.md (or equivalent filename)

**Terminal (3 documents):**
- docs/BOOK_XVI_TERMINAL_EQUILIBRIUM_GRAVITY_FREEZE_DYNAMICS_RECENTERING.md (or equivalent filename)
- docs/BOOK_XVI_TERMINAL_STATUS_LEDGER.md (or equivalent filename)
- docs/BOOK_XVI_TERMINAL_HANDOFF.md (or equivalent filename)

**Total:** 9 documents.

---

# ZENODO METADATA

- **Title:** GRUT Book XVI: Quasi-Static Rate Analysis, Equilibrium Reducibility, and the Gravity-Distinction Freeze
- **Authors:** D. Ryan Grover
- **Description:** Book XVI of the GRUT Theory-of-Everything program. Three stages close the equilibrium gravity-distinction route. Alpha: a self-consistent A_eff bootstrap reveals a structural sign error in the D7/D8 source amplification model -- by Birkhoff's theorem, defect energy above R_eq must be subtracted from M, not added. The proxy overpredicts by a factor of 17. All conditional surpluses collapse from 2-3 to 0. The proper-time relaxation rate is constitutively fixed at 1/tau with no amplification mechanism. Beta: the surviving equilibrium T^Phi is shown to be reducible to GR + massive scalar (m_phi = 1/tau), observationally silent (|delta_beta| = 1.4e-10 vs Cassini 2.3e-5), and subject to source ambiguity (R = 0 in Schwarzschild exterior). Terminal: the equilibrium gravity-distinction route is formally frozen on three independent grounds. 10 failed routes are logged. The program recenters on its dynamical core: 5 proven theorems (forward semigroup, Lyapunov, dissipative balance, T-breaking, monotone contraction) that are irreducible against conservative theories but generic among open systems. Biology scaffold and matter-within-GR baseline preserved. 3 stages, 9 documents. Cost unchanged: 16/11/1/6. Surplus: 0+0 (fully collapsed). Book XVI earned the equilibrium gravity freeze.
- **Keywords:** GRUT, scalar gravity, sign error, Birkhoff theorem, weak-field gravity, PPN, tau constraint, equilibrium reducibility, observational silence, dynamics recentering
- **License:** CC BY 4.0
- **Upload type:** Publication / Preprint

---

# SUMMARY FOR CLAUDE CHAT

Produce **two documents.** Main manuscript (~14-18 pages) following the section structure above. Companion ledger (~8-12 pages of tables). The three-act structure (sign error, reducibility + silence, freeze + recentering) is the structural spine.

Key disciplinary constraints:
- The sign error is STRUCTURAL, not a typo -- it reflects a misapplication of Birkhoff's theorem
- Reducibility means the equilibrium claim is NOT novel -- it is GR + massive scalar
- Observational silence means the equilibrium claim is NOT testable -- corrections are 6+ orders below current bounds
- The freeze is PERMANENT -- no narrative rebranding can reopen it
- The dynamical theorems SURVIVE but are observationally UNANCHORED
- Surplus portfolio is 0+0 -- fully collapsed
- Use "frozen" not "paused." Use "collapsed" not "revised." Use "reducible" not "embeddable."
- The honest register: the program lost its equilibrium gravity route and honestly says so

All 9 audit documents (3 Alpha + 3 Beta + 3 Terminal) are the primary sources.
