# GRUT III — Book C, Stage C3: Model-W Sufficiency Decision and Closure Fork

**Predecessor:** C2 (bounded_open, A8 derived at one-loop, Model W established).
**Inherited findings (C2, exact):** Tree-level Re S_eff = 0 (structural). One-loop |det(J)| selection exists (generic, ratio 2.1 at tested parameters). Model C not realized. Model W = probabilistic weighting.

---

## 1. Sufficiency Criteria (SC)

"Model W is enough" for Book C closure and GRUT-III progression if:

| # | Criterion | Standard |
|---|-----------|---------|
| **SC1** | **Predictive utility.** Model W produces at least one testable prediction that differs from a generic (non-GRUT) stochastic EFT. | Must identify a quantity that Model W predicts and a generic EFT does not, OR honestly state that no such quantity exists yet. |
| **SC2** | **Regime control.** The domain where Model W operates is explicitly bounded and does not rely on uncontrolled extrapolations. | All regime tags from Books A-B must remain valid. No new unsafe zone is entered. |
| **SC3** | **Parameter dependence transparency.** Every parameter that Model W depends on is listed, tagged (derived/assumed/open), and its impact on the A8 selection is stated. | No hidden parameter dependence. |
| **SC4** | **Blacklist compatibility.** Model W does not violate any claim in X1-X10, NF1-NF9, I1-I7. | Checked item by item. |
| **SC5** | **Non-inflation.** The closure claim does not overstate what was derived. "Weighted EFT" is not marketed as "constrained dynamics" or "selection law." | The exact terminology is frozen. |

---

## 2. Necessity Criteria (NC)

"Model W is not enough" for ToE trajectory if:

| # | Criterion | Standard |
|---|-----------|---------|
| **NC1** | **Parameter inevitability gap.** The theory has 11 EFT parameters (τ₁, D_Φ, T_Φ, α, β, κ, τ₂, ε, σ, ν, D_Ψ), none derived from deeper principles. A ToE-viable theory must derive its parameters or reduce their count. | Count free parameters. If > 0 undetermined: gap exists. |
| **NC2** | **No deterministic pruning.** Model W assigns probabilistic weight but does not reject trajectories. A ToE that explains "why this history and not another" needs stronger selection. | If Model C is not realized and no trajectory is forbidden by A8: gap exists. |
| **NC3** | **Generic EFT indistinguishability.** A generic two-field overdamped stochastic system with cubic coupling produces the same bistability and one-loop selection. There is nothing specifically "GRUT" about Model W — any nonlinear open-system EFT has this structure. | If Model W's predictions match a generic EFT with no GRUT-specific content: gap exists. |
| **NC4** | **Missing cross-sector unification.** The USL (Sector 3, gravitational) and the constitutive relaxation (Sectors 1-2, environmental) remain separate. Model W does not unify them. A ToE must explain why both exist and how they are related. | If USL and τ remain independent predictions with independent parameters: gap exists. |
| **NC5** | **Auxiliary field Ψ is unjustified.** Ψ was introduced to produce bistability. Its physical identity is unspecified (CF-C2-6). It adds 6 parameters. A ToE must either derive Ψ or explain why it is necessary. | If Ψ has no physical interpretation and no derivation: gap exists. |

---

## 3. Evaluation Matrix

### Sufficiency criteria (SC1-SC5)

| # | Criterion | Evidence | Result | Confidence |
|---|-----------|---------|:------:|:----------:|
| **SC1** | Predictive utility | Model W predicts that the attractor with smaller |det(J)| is statistically preferred. This prediction is GENERIC to any bistable open system — it is standard one-loop thermodynamics, not GRUT-specific. **However:** the GRUT-specific content is: (a) the USL prediction Λ = Gm²/(ℏl) for the quantum sector, which is independent of Model W and IS specific to GRUT; (b) the constitutive law form τ dΦ/dt + Φ = β + αR, which has a specific curvature coupling. Model W adds attractor selection ON TOP of these GRUT-specific predictions. The USL is the primary testable prediction; Model W is structural. | **PASS** (weakly). The USL remains the primary testable prediction. Model W adds structural content but no new experimental prediction beyond USL. | 0.55 |
| **SC2** | Regime control | Model W operates within the same domain as Books A-B: Markovian, overdamped, linear-around-each-attractor, weak-field, Ohmic. The bistability extends the dynamics to the nonlinear regime, but the one-loop computation is a linearized-fluctuation calculation around each attractor — it does not leave the locally-linear domain. No new unsafe zone. | **PASS** | 0.80 |
| **SC3** | Parameter transparency | Model W depends on all 11 EFT parameters: τ₁, D_Φ, T_Φ, α, β (from Book B), κ, τ₂, ε, σ, ν, D_Ψ (from C1-C2). All listed in the C2 term ledger. A8 selection depends specifically on the Jacobian eigenvalues at each FP, which depend on (a, κ, ε, σ, ν, τ₁, τ₂). Which attractor is preferred is parameter-dependent. | **PASS** | 0.85 |
| **SC4** | Blacklist compatibility | Check against critical blacklist items: X1 (covariance): not claimed. X3 (τ derived): not claimed. X5 (strong-field): not claimed. X10 (ToE): not claimed. NF1 (X unique): not claimed. I1 (constraining admissibility): Model W is weighting, not constraining — I1 is respected. I5 (ToE): not claimed. | **PASS** | 0.95 |
| **SC5** | Non-inflation | The closure statement will say "weighted EFT with one-loop attractor preference." It will NOT say "selection law," "constrained dynamics," or "theory of everything." The exact phrasing is controlled below (Section 6). | **PASS** | 0.90 |

**SC verdict: ALL PASS.** Model W is sufficient for Book C closure at the EFT level.

### Necessity criteria (NC1-NC5)

| # | Criterion | Evidence | Result | Confidence |
|---|-----------|---------|:------:|:----------:|
| **NC1** | Parameter gap | 11 EFT parameters, 0 derived from deeper principles. The coupled CTP action has MORE free parameters than the linear Book B scaffold (which had 5). The complexity has increased without reducing the parameter count. | **GAP EXISTS** | 0.95 |
| **NC2** | No deterministic pruning | C2 proven: Model C not realized. A8 assigns weight, does not reject. Every trajectory satisfying A1-A7 remains admissible. The theory says "attractor A is more probable" but cannot say "trajectory to B is forbidden." | **GAP EXISTS** | 0.95 |
| **NC3** | Generic EFT indistinguishability | The one-loop attractor selection is a STANDARD result in non-equilibrium statistical mechanics. Any bistable Langevin system with two wells has this property. The GRUT-specific content is: (a) the source coupling X = β + αR (curvature-dependent equilibrium), (b) the USL (gravitational dephasing). These are specific. But Model W itself (the selection mechanism) is generic. **Model W adds nothing GRUT-specific to the selection mechanism.** What is GRUT-specific is which system has multiple attractors and what the curvature coupling is — not the one-loop selection principle. | **GAP EXISTS** (for the selection mechanism; not for the constitutive law or USL) | 0.80 |
| **NC4** | Missing cross-sector unification | The USL (Sector 3: Gm²/(ℏl)) and the constitutive relaxation (Sectors 1-2: τ, D from environment) remain structurally independent. Model W does not connect them. The one-loop selection principle involves the Jacobian eigenvalues of the coupled (Φ, Ψ) system, which depend on τ₁, τ₂ but NOT on G or the USL. The quantum and classical sectors are still separate predictions for separate observables (per Alpha-Prime, E16-Q6). | **GAP EXISTS** | 0.90 |
| **NC5** | Ψ unjustified | Ψ was introduced to produce bistability. It has no physical interpretation ("what is the second constitutive mode?"). It adds 6 parameters. It is not derived from the CTP action — it is added to it. If Ψ were removed, bistability vanishes and Model W collapses to the linear Book B scaffold. Ψ is load-bearing but unjustified. | **GAP EXISTS** | 0.90 |

**NC verdict: ALL GAPS EXIST.** Model W is insufficient for ToE trajectory on every necessity criterion.

---

## 4. Decision Fork

### Analysis

The SC and NC results point to a clean split:

- **For EFT closure:** Model W passes all sufficiency criteria. The program has a well-defined, regime-bounded, blacklist-compatible, non-inflated effective field theory with one-loop attractor preference. This is an honest, defensible result. Book C can close at this level.

- **For ToE trajectory:** Model W fails all necessity criteria. The parameter count is high (11), the selection is generic (not GRUT-specific), no deterministic pruning exists, the quantum and classical sectors are unconnected, and the auxiliary field Ψ is unjustified. These are structural gaps, not technical ones — they cannot be resolved by more computation within the current framework.

### Decision

### **split_core_depth**

**Core closure:** Close Book C as a weighted EFT. Freeze the established results (E1-E16 from Book B, plus C1-C2 results). The GRUT-III program at the EFT level is DONE.

**Depth pathway:** The five NC gaps define the agenda for a potential Book D (or GRUT-IV). These are FOUNDATIONAL issues, not EFT extensions:
- Can the parameter count be reduced?
- Can Ψ be derived rather than assumed?
- Can the USL and constitutive sectors be unified?
- Can selection be made deterministic rather than probabilistic?
- What distinguishes GRUT from a generic stochastic EFT?

---

## 5. Next-Phase Contract

### Pathway A: C-depth (geometry-coupled weighting + non-Markovian kernel)

| Item | Content |
|------|---------|
| **Objective** | Determine whether geometric coupling (X = β + αR) modifies the one-loop selection in a GRUT-specific way, and whether non-Markovian memory creates history-dependent basin assignment |
| **Priority** | MEDIUM (extends Model W but does not resolve NC1-NC5) |
| **Gate requirement** | Must show that α-dependent selection differs from α = 0 (otherwise: generic, no GRUT content) |
| **Status** | DEFERRED (not opened unless NC3 demands it) |

### Pathway B: Book D (negative reconstruction test)

| Item | Content |
|------|---------|
| **Objective** | Determine what, if anything, distinguishes the GRUT EFT from a GENERIC two-field overdamped stochastic system with curvature coupling. If nothing: GRUT is a notational variant, not a new theory. If something: identify the distinguishing structure. |
| **Priority** | **HIGH** (this is the existential question for the GRUT program) |
| **Gate requirement** | Must produce at least ONE prediction or structural constraint that a generic EFT does not have, OR honestly conclude that GRUT is a specific parametrization of a known EFT class |
| **First mandatory task** | D1: Write down the most general two-field overdamped stochastic EFT with curvature coupling. Compare term-by-term to the GRUT CTP action. Identify any term that is GRUT-specific (present in GRUT but absent or differently constrained in the generic case). |

**Priority order: B before A.** The negative reconstruction test (Book D) is more important than the C-depth extension because it determines whether the GRUT program has unique content. If GRUT is just a generic EFT, then C-depth extensions add nothing.

---

## 6. Claim Discipline Table

### Claims ALLOWED after C3

| # | Allowed claim | Basis | Regime |
|---|-------------|-------|--------|
| CA1 | "GRUT has a CTP-derived constitutive law: τ dΦ/dt + Φ = β + αR." | Iota-Prime, BA2 | Markovian, overdamped, linear, weak-field |
| CA2 | "The USL Λ = Gm²/(ℏl) is derived as gravitational self-energy dephasing." | Iota-Prime, TF9 | Newtonian, l > 2R |
| CA3 | "The extended-body Diosi integral gives the exact USL for l < 2R." | Kappa-Prime, A1-L10 | All Newtonian |
| CA4 | "The environmental bath provides τ, D, T (not gravity alone in flat space)." | A3 | Flat space, weak field |
| CA5 | "In the nonlinear coupled regime, one-loop attractor preference exists (Model W)." | C2 | Bistable parameter regime, one-loop |
| CA6 | "The CTP tree-level Re S_eff = 0 at all FPs (no tree-level selection)." | C2, U1 | Structural (all regimes) |
| CA7 | "Admissibility is diagnostic (classifier) in the linear regime, probabilistic (weighting) in the bistable regime." | B2, C2 | As stated |
| CA8 | "The corrected USL operating point is 196 fg / 474 nm / USL/gas = 2.9, hardware-limited." | Mu-Prime | Newtonian, point-mass regime |

### Claims FORBIDDEN after C3

| # | Forbidden claim | Reason |
|---|----------------|--------|
| CF1 | "GRUT has dynamical trajectory pruning / constrained admissibility." | C2: Model C not realized. I1 binding. |
| CF2 | "The one-loop attractor selection is GRUT-specific." | NC3: it is generic to any bistable open system. |
| CF3 | "The auxiliary field Ψ is physically motivated." | NC5: Ψ has no physical interpretation. |
| CF4 | "GRUT's parameter count is small or predictive." | NC1: 11 EFT parameters, none derived. |
| CF5 | "The USL and constitutive relaxation are unified." | NC4: they remain separate sectors. |
| CF6 | "GRUT is a Theory of Everything." | X10 (perpetual). |
| CF7 | "GRUT is covariant." | X1, NF4 (perpetual). |
| CF8 | "GRUT is valid at strong curvature." | X5, NF8 (perpetual). |
| CF9 | "τ is predicted by the theory." | X3, NF7, NC1 (perpetual). |
| CF10 | "The USL is testable on a near-term timescale." | X9, V3 (retracted). |

### Statements that must remain OPEN

| # | Open statement | Why |
|---|---------------|-----|
| O1 | Whether Ψ has a physical interpretation | CF-C2-6 |
| O2 | Whether the one-loop selection is modified at two-loop or non-perturbative level | CF-C2-7 |
| O3 | Whether GRUT has any content beyond a generic two-field stochastic EFT | NC3 (Book D mandatory question) |
| O4 | Whether the USL and constitutive sectors can be unified | NC4 |
| O5 | Whether the parameter count can be reduced | NC1 |
| O6 | The value of α and all other EFT parameters | UD1 + NC1 |

---

## Gate Table

| Gate | Criterion | Status | Evidence |
|:----:|-----------|:------:|---------|
| **C3-G1** | SC and NC criteria explicit and non-overlapping | **PASS** | SC1-SC5 test sufficiency for EFT closure. NC1-NC5 test necessity for ToE trajectory. No criterion appears in both sets. SC asks "is this enough for what we have?"; NC asks "is this enough for where we need to go?" — different questions with different standards. |
| **C3-G2** | Criteria evaluation evidence-backed | **PASS** | Every SC and NC evaluation cites specific prior results (Iota-Prime, C2, Book B E-ledger, etc.) with confidence scores. No prose-only verdicts. |
| **C3-G3** | Fork decision operational | **PASS** | split_core_depth: core closure (Book C closes as weighted EFT) + depth pathway (Book D opens with negative reconstruction test). Priority: Book D before C-depth. First task: D1 (generic EFT comparison). |
| **C3-G4** | Claim-permission table frozen | **PASS** | 8 allowed claims (CA1-CA8), 10 forbidden claims (CF1-CF10), 6 open statements (O1-O6). All tagged with basis and regime. |
| **C3-G5** | Next-phase contract unambiguous | **PASS** | Two pathways (A: C-depth, B: Book D). Priority B > A. Book D first task D1 specified. Gate requirements stated. |

---

## Decision Token

### **split_core_depth**

**Core:** Book C closes as a weighted EFT. The GRUT-III EFT program is complete within its declared regime. Results E1-E16 (Book B) and C1-C2 findings are frozen.

**Depth:** Book D opens as a negative reconstruction test. Its first mandatory task is to determine whether GRUT has any structural content beyond a generic two-field stochastic EFT with curvature coupling. This is the existential question. If GRUT has unique content: identify it. If not: honestly state it and determine whether the USL alone constitutes sufficient unique content.

**The honest status of the GRUT program after C3:**
- It has a derived constitutive law (CTP backbone).
- It has a derived quantum prediction (USL, gravitational dephasing).
- It has a derived attractor-preference mechanism (one-loop weighting).
- It has an explicit domain of validity.
- It has 11 undetermined parameters.
- It has no deterministic selection mechanism.
- It has no cross-sector unification.
- It has not yet demonstrated that it is more than a specific instance of a generic EFT class.

The last point is the open question that Book D must answer.

---

*GRUT III Book C Stage C3 complete. Decision: split_core_depth. SC: all 5 pass (Model W sufficient for EFT closure). NC: all 5 gap (Model W insufficient for ToE). Core closure: Book C as weighted EFT. Depth: Book D opens with negative reconstruction test (is GRUT more than a generic EFT?). Priority: Book D before C-depth. 8 allowed claims, 10 forbidden, 6 open. Gates: 5/5 pass.*
