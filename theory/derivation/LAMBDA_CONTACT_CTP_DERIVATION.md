# Λ_contact from CTP — Stage 1: Scope and Pre-commitments

**Date opened:** 2026-04-29
**Trigger:** External review (deep-research-report.md) flagged that the Schrödinger-in-the-Box program needs Λ_contact derived from the CTP reduced-density-matrix machinery rather than asserted as a separate threshold. Forward-derivation work to upgrade the observer module from anchored to computed.
**Status:** STAGE 1 — scope and pre-commits. No computation yet. Pause point for review.

---

## Why this work

Chapter 11 currently registers four anchored claims:
- `schrodinger_in_box_inversion` (anchored)
- `bayesian_observer_filtering` (anchored)
- `wigner_friend_dissolution` (anchored)
- `gravitational_entanglement_formation_rate` (anchored)

Plus one computed:
- `measurement_resolution` (computed) — the 6-leg crystallinity harness

The external report's recommendation: derive a contact-formation rate Λ_contact from the CTP reduced-density-matrix / influence-functional machinery itself, so the observer module becomes a fully computed measurement-theory module rather than interpretive scaffolding.

This investigation pre-commits to outcomes and frames what is actually derivable before any computation.

---

## What the framework already has (audit)

The framework's existing infrastructure is more complete than the external report assumed. Specifically:

**`grut/foundation/noise_kernel.py`** — The gravitational noise kernel is documented:

```
N_grav(x, x') = G / (ℏ |x - x'|)
```

The docstring at line 23 says verbatim: *"Derived from the imaginary part of the CTP influence functional in the Newtonian limit (Anastopoulos & Hu, CQG 30, 165007, 2013)."* This is the standard CTP / influence-functional / stochastic-gravity derivation. **The kernel is already CTP-derived.**

**`lambda_grav(m, l, R)`** — The decoherence rate:

```
Λ_grav = G m² S(l/R) / (ℏ l)
```

This is the off-diagonal decay rate produced when the gravitational noise kernel acts on a single mass in spatial superposition over separation `l`. **The decoherence rate is already CTP-derived.**

**`measurement_resolution` (Ch 11, computed)** — The 6-leg harness verifies that the apparatus crystallinity X_A = Λ_grav,A × τ₀ ≫ 1 dominates the system crystallinity X_B, and that joint coupled X equals the apparatus's. **The pointer-mass-wins logic is already computed.**

So the CTP-to-decoherence-rate derivation is *implicit in the existing framework*. What the external report flagged as missing — Λ_contact derivation from CTP — is largely a **labeling / identification gap**, not a computational gap. The substantive question is: are there any *additional* gaps the existing framework hasn't surfaced?

---

## The five gaps the report named, audited

| # | Report's gap | Status in existing framework | Real work required |
|:---|:---|:---|:---|
| 1 | Concrete pointer-observable definition | Implicit: position eigenbasis at apparatus mass scale (`measurement_resolution` uses gram-scale body parameters). Not stated explicitly anywhere as the pointer-basis choice. | Make the definition explicit. Document why the gravitational coupling selects position eigenstates as the pointer basis. |
| 2 | Explicit reduced-density-matrix derivation | Anchored in Anastopoulos-Hu (cited but not redone in the codebase). The framework uses the result Λ_grav = Gm²S(l/R)/(ℏl) but doesn't reproduce the derivation as a self-contained module. | Worth doing as a self-contained derivation module so reviewers don't have to chase the AH reference. Identifies whether the AH derivation, applied to GRUT's specific noise kernel and screening structure, produces the framework's Λ_grav formula. |
| 3 | μ vs γ distinction (CTP physics vs Bayesian information) | Partially documented in `bayesian_observer_filtering`. The pure-hazard limit μ = Λ_grav is named. The pure-absence limit (γ encoding) is named as epistemic. The relationship is not formally derived. | Sharpen the distinction: μ is the influence-functional decay rate (CTP physics, derives from N_grav). γ is the Bayesian update rate from absence-of-evidence (epistemic, depends on observer's prior on contact frequency). They are independent terms in the filtering equation. |
| 4 | Born rule from noise kernel | **Genuinely not done.** The framework asserts Born-rule probabilities emerge from "the noise kernel weighted by coupling geometry" (Ch 11) but does not derive this. | Honest assessment: deriving Born rule from CTP requires either (a) additional postulates (decoherent-history weighting, einselected pointer basis), or (b) a decoherence-functional approach. GRUT does not currently do either. **This is a real gap, likely outcome (c) honest-negative for this sub-piece.** |
| 5 | Wigner's friend conditional-state proof | Anchored prose at present. The friend's crystallization is computed via `measurement_resolution`; Wigner's outside-of-lab description is consistent with treating the lab as a quantum system with X_lab ≫ 1. The conditional-state mathematics is not written. | Worth doing as a worked conditional-state calculation: ρ_Wigner-conditional-on-friend's-record vs ρ_friend-marginal. Should follow from standard reduced-density-matrix machinery. |

**Summary of gap audit:**
- Gaps #1, #5: presentation work — rewrite existing implicit content as explicit derivation. Light.
- Gap #2: legitimate self-containedness improvement — redo the AH derivation in framework primitives. Medium.
- Gap #3: clarification work — formalize the existing distinction between physical decoherence and Bayesian update. Light.
- **Gap #4: genuine derivation gap.** Born rule from CTP is not in the framework. Will likely close as honest-negative or scoping-tier (requires postulate beyond current machinery).

---

## Pre-commits — Stage 1 explicit choices

### (a) Pointer-observable definition

The pointer observable is the **center-of-mass position operator x̂_P** of macroscopic record-bearing degrees of freedom in the apparatus, evaluated at coarse-graining scales such that X_P = Λ_grav,P × τ₀ ≫ 1.

**Why position basis.** The gravitational coupling H_int ~ −Gm_S m_P / |x_S − x_P| is diagonal in the simultaneous position basis of system and pointer. By Zurek's einselection criterion, the pointer basis is the eigenbasis of the system-environment interaction. In GRUT, the "environment" is the gravitational vacuum medium; the interaction is gravitational. Therefore the pointer basis is the position basis at apparatus mass scale.

**Coarse-graining scale.** The pointer position is defined at the spatial scale where Λ_grav × τ₀ ≫ 1 — i.e., the scale at which gravitational decoherence is fast compared to the constitutive relaxation time. For a gram-scale apparatus at millimeter separation, this is satisfied by ~35 orders of magnitude.

**Limitation acknowledged.** This pointer-basis choice is *natural under the GRUT framework* but inherits the standard pointer-basis assumption: that one specific basis is privileged by the system-environment interaction. The ambiguity is in the noise-kernel structure itself (which is gravitational and selects position) — not in the pointer-basis choice given the kernel.

### (b) Coarse-graining / system-pointer-environment partition

- **System (S):** the quantum object being measured (e.g., nanoparticle in superposition over separation l_S).
- **Pointer (P):** macroscopic position observables of the apparatus + observer body. Mass scale m_P ≫ m_S.
- **Environment (E):** the gravitational vacuum medium itself. Integrated out via the CTP / influence-functional machinery, producing the noise kernel N_grav = G/(ℏ|x−x'|).

The reduced density matrix is ρ_SP(t) = Tr_E [ρ_total(t)]. The coarse-graining is over vacuum modes; the resulting noise kernel is what mediates decoherence between system and pointer.

### (c) Coupling operators

The system-pointer coupling is gravitational:

```
H_int = −G m_S m_P / |x̂_S − x̂_P|
```

In the influence-functional structure, this enters as a bilinear coupling between the system position x̂_S and the pointer position x̂_P (linearized about equilibrium positions). The CTP integration produces an influence action:

```
S_IF[Σ_S, Δ_S; Σ_P, Δ_P] = ∫ Δ D Σ + (i/2) ∫ Δ N Δ
```

where D is the dissipative kernel (constitutive memory τ₀⁻¹ exp(−t/τ₀)) and N is the noise kernel (gravitational N_grav between system and pointer positions).

### (d) Pre-committed expectations

**Most likely outcome (60% prior):** Λ_contact = Λ_grav at observer-pointer scale, with the existing framework's `lambda_grav(m_P, l_P, R_P)` already encoding the answer. The derivation work is *labeling* (explicit identification) rather than *computing* (new value). Tier-promotion of Schrödinger-in-the-Box from anchored to anchored-with-explicit-derivation; full computed status requires gap #4 (Born rule) which probably won't close in this work.

**Second most likely (30% prior):** Λ_contact emerges with a coarse-graining-dependent prefactor that isn't simply Λ_grav. Specifically, the system-pointer joint decoherence may have a kinematic factor depending on the relative configuration that isn't captured by single-particle Λ_grav. Outcome: conditional derivation, anchored stays anchored, sharper closure conditions.

**Third (10% prior):** The reduced-density-matrix calculation produces a form that doesn't naturally identify with Λ_grav, indicating that "contact-formation" is a different physical process than "single-particle decoherence." Outcome: open negative, observer module needs additional structure (different noise kernel for record-formation vs single-mass decoherence?).

**Born rule (gap #4) — separate pre-commit (90% prior outcome (c)):** Born rule does not derive from CTP machinery alone. The framework will need either decoherent-histories weighting or einselection-with-decoherent-history postulates. This is registered as a separate finding, regardless of how Λ_contact lands.

---

## What Stage 2 would actually compute

Given the pre-commits above, Stage 2 work is:

1. **Self-contained AH-style derivation** of single-particle decoherence rate from the gravitational noise kernel, written in framework primitives. Should reproduce Λ_grav = Gm²S(l/R)/(ℏl) — gap #2 closed.

2. **Two-particle (system + pointer) reduced density matrix evolution.** Trace out vacuum modes, derive the joint ρ_SP off-diagonal decay. Identify whether the rate is single-particle Λ_grav at pointer scale or has additional structure.

3. **μ vs γ formal distinction.** Show that the Bayesian filtering equation's μ = (ρ_off / ρ_off|t=0) decay rate from the influence-functional, while γ enters only through the observer's prior on contact frequency (independent of CTP physics). Gap #3 closed.

4. **Wigner's friend conditional-state calculation.** Show ρ_Wigner|friend = ρ_friend ⊗ ρ_lab when the lab is X_lab ≫ 1 deep crystal, demonstrating consistency without paradox. Gap #5 closed (computationally, not just narratively).

5. **Born rule status statement.** Honest documentation of what would be required (decoherent-histories postulate or einselection-plus-history) that is not currently in the framework. Gap #4 marked open with explicit closure condition.

---

## Pause point — Stage 1 deliverables

This investigation log is the Stage 1 deliverable. It establishes:

- The framework's existing CTP machinery already encodes Λ_contact = Λ_grav at apparatus scale, with the AH derivation cited but not redone in the codebase.
- The five gaps the external report named are now audited; three are presentation/labeling work, one is a legitimate self-containedness derivation, and one (Born rule) is a genuine derivation gap that will likely close as open-negative.
- Pre-commits on pointer basis, coarse-graining, and coupling operators are documented before any computation.
- Pre-committed expected outcome distribution is documented (60/30/10 with Born rule sub-finding 90% honest-negative).

**Decision before Stage 2:** the user reviews this scoping. If the pre-commits are accepted, Stage 2 proceeds as a self-contained derivation module (`grut/derived/decoherence/lambda_contact.py`) plus tests. If the pre-commits surface choices the framework hasn't pinned, the investigation closes here as scoping-tier with sharpened closure conditions for Schrödinger-in-the-Box (no tier promotion, but explicit honest-negative for gap #4 and explicit pointer-basis identification for gap #1).

**Either way, this Stage 1 produces a registerable artifact:** the investigation log itself documents what Λ_contact derivation entails in the framework, why the existing infrastructure already provides the substantive content, and where the genuine open derivations (#4 in particular) sit. That's a deposit-relevant clarification regardless of whether Stage 2 lands.

---

## Cross-references

- `grut/foundation/noise_kernel.py` — existing CTP-derived gravitational noise kernel and Λ_grav formula
- `grut/derived/decoherence/entanglement.py` — existing F5 protection / lambda_grav_bell calculation
- `grut/foundation/measurement_resolution.py` — existing 6-leg crystallinity harness
- `grut/derived/decoherence/schrodinger_in_box.py` — existing Bayesian filtering module
- Anastopoulos & Hu, "A Master Equation for Gravitational Decoherence," CQG 30, 165007 (2013) — the cited derivation
- External review document `/Users/mpg/Desktop/deep-research-report.md` — the trigger for this investigation
- GRUT_TOE.md Ch 11 — observer module current state (anchored Schrödinger-in-the-Box claims)
- GRUT_TOE.md Ch 14 completion ladder Tier 2 (Λ_contact derivation listed there as the closure path for the observer module)

---

*Investigation opened by D. R. Grover with Anthropic Claude assistance, April 2026. Stage 1 produced under discipline pattern: scope before computing, pre-commits documented, expected outcomes ranged with priors before Stage 2 work. Pause for review.*

---

## Stage 2 — Completed

**Date completed:** 2026-04-29 (same session as Stage 1).
**Status:** All five external-review observer-module gaps addressed. Three new computed claims registered, one anchored claim registered, one open-negative registered. One existing anchored claim tier-promoted to computed.

### Stage 2 deliverables

**New module:** `grut/derived/decoherence/lambda_contact.py`. Self-contained Anastopoulos-Hu-style derivation in framework primitives. Reproduces Λ_grav exactly from kernel-level CTP calculation. Two-particle reduced-density-matrix calculation showing Λ_contact = Λ_grav at pointer scale. Worked μ-vs-γ distinction. Wigner's friend conditional-state computation. Born rule honest-negative with structural framing.

**New tests:** `tests/derived/test_lambda_contact.py` — 35 tests, all passing. Covers all five gaps. Pinned regression tests for the substantive Stage 2 findings (Λ_contact = Λ_grav identification; Born rule remains a postulate; all four anchored claims addressed by computed work).

**Registry updates** in `grut/toe/registry.py`:
- New claim `lambda_contact_ctp_derivation` (computed, Ch 11) — Stage 2 derivation, with tests
- New claim `pointer_observable_position_basis` (anchored, Ch 11) — explicit pointer-basis choice, with Zurek einselection justification
- New claim `mu_gamma_ontic_epistemic_distinction` (computed, Ch 11) — formal μ vs γ distinction, with tests
- New claim `born_rule_postulate_open_negative` (open_negative, Ch 11, #16) — structural-framing honest-negative
- Promotion: `wigner_friend_dissolution` from anchored to **computed**, statement rewritten to reflect explicit conditional-state mathematics

**Ledger updates** in `grut/toe/ledger.py`: open negative #16 (`born_rule_postulate_open_negative`) registered with closure conditions naming three options (decoherent-histories, einselection-with-history, deeper-symmetry derivation), all tier-flagged as multi-decade research post-deposit.

### Outcome distribution vs pre-commits

Stage 1 pre-commits were:
- 60% Λ_contact = Λ_grav at pointer scale (clean labeling identification)
- 30% conditional with kinematic factor
- 10% honest-negative on rate identification

**Outcome was 60% (clean identification).** The two-particle joint reduced-density-matrix calculation, in the m_P >> m_S limit, reproduces single-particle Λ_grav at pointer scale exactly. No kinematic factor or definitional ambiguity surfaced. The framework's existing infrastructure already encodes the contact-formation rate; what was missing was the explicit identification, now made.

Born rule sub-finding pre-commit was 90% honest-negative. **Outcome was 90% (honest-negative).** Born rule does not derive from N_grav alone. Registered as open negative #16 with structural framing per directed style.

### Five gaps — closure status

| # | Gap | Stage 2 result |
|:---|:---|:---|
| 1 | Concrete pointer-observable definition | **Closed (anchored).** New claim `pointer_observable_position_basis` makes the choice explicit with Zurek einselection justification. Tier kept anchored because the choice is not formally proven as a Zurek-stability theorem within GRUT — closure path: einselection-stability proof. |
| 2 | Explicit reduced-density-matrix derivation | **Closed (computed).** `lambda_off_diagonal_single_particle()` reproduces Λ_grav from kernel-level calculation. `derivation_consistency_check()` verifies match. Self-contained AH-style derivation in framework primitives, no longer requiring chase to AH 2013. |
| 3 | μ vs γ distinction | **Closed (computed).** `mu_gamma_distinction()` formalizes μ as ontic CTP rate (Λ_grav at pointer) and γ as epistemic Bayesian update (independent of CTP primitives). |
| 4 | Born rule from noise kernel | **Closed as honest-negative (open_negative #16).** `born_rule_status()` documents what N_grav gives (rate of decoherence) vs what's missing (probability weights). Structural framing: CTP machinery produces decoherence rates and noise structure but does not on its own produce probability assignments. |
| 5 | Wigner's friend conditional-state proof | **Closed (computed).** `wigner_friend_consistency()` produces the conditional-state calculation explicitly. Existing `wigner_friend_dissolution` claim tier-promoted from anchored to computed. |

### Test results

- **Λ_contact tests:** 35/35 passing in 0.27 s.
- **Full TOE-suite tests:** 259/259 passing in 2.45 s (after dependency-fix iteration).
- **Full repository regression:** 1397/1397 passing in 137 s. **Baseline was 1362; net +35 tests, no regressions.**

### Registry tally — before / after

| Tier | Before | After | Change |
|:---|---:|---:|:---|
| Total | 87 | 91 | +4 |
| Computed | 48 | 51 | +2 new + 1 promotion |
| Anchored | 13 | 13 | +1 new − 1 promotion |
| Open_negative | 15 | 16 | +1 |
| Meta | 6 | 6 | 0 |
| Conjectural | 3 | 3 | 0 |
| Foundational | 2 | 2 | 0 |

Sums verify: 51 + 13 + 16 + 6 + 3 + 2 = 91 ✓

### What Stage 2 did NOT do

- **Did not derive Born rule.** Per pre-commit, this stays open. The framework now has an explicit honest-negative on this point with closure conditions.
- **Did not add new physics.** All Stage 2 work surfaces what was implicit in the existing framework (Λ_grav as the off-diagonal decay rate from CTP). The substantive contribution is the *explicit identification* Λ_contact = Λ_grav at pointer scale, plus the four formal closures.
- **Did not formally prove Zurek einselection within GRUT.** The position-basis choice for the pointer observable is justified but not proven as a stability theorem. Tier reflects that.

### Cross-references for downstream work

- The Λ_contact = Λ_grav identification is now explicitly available as `lambda_contact` in the framework's API (via `lambda_joint_two_particle().lambda_contact`).
- The Born rule open-negative is registered as #16 in `ledger.py` with closure paths named.
- The observer module is no longer "anchored interpretive scaffolding" — it is *computed measurement-theory module with one explicit honest-negative carve-out (Born rule)*.
- This work upgrades the deposit document Chapter 11; downstream document updates: tier annotations on claims, count synchronization (87→91, 1362→1397, 15→16 open negatives), Ch 14 ledger updated to surface born_rule as #16, completion ladder Tier 4 may need to mention Born rule as a sub-target.

### Decision deferred to v2 deposits

- Decoherent-histories formalism integration (closure path (a) for Born rule)
- Formal Zurek einselection-stability theorem under N_grav (would tier-promote `pointer_observable_position_basis` from anchored to computed)
- The two paths above are research-tier work that legitimately follows the deposit rather than blocking it.

---

*Stage 2 closed by D. R. Grover with Anthropic Claude assistance, April 29 2026. All five external-review observer-module gaps addressed. Schrödinger-in-the-Box program upgraded from anchored interpretive scaffolding to computed measurement-theory module, with the Born-rule honest-negative as the registered structural carve-out.*
