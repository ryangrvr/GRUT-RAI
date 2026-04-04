# Book XVI -- Target Beta: Irreducible Constitutive Gravity and Tau-Constraint Audit

## Formal Weak-Field Gravity Stage -- Second Book XVI Stage (Gravity Side)

**Predecessor:** Book XVI Alpha (D7/D8 sign error; compact-object frontier collapsed). Book XVI Beta Structural Claim Audit (irreducible claim identified as dissipation + equilibrium T^Phi).
**Function:** Test whether the surviving weak-field equilibrium T^Phi prediction is (a) irreducible to GR + matter, (b) detectable by precision gravity, and (c) constrains tau nontrivially from observation.
**Source code:** grut/weak_field_tau_constraint.py

---

## 1. Executive Verdict

**(A) -- The weak-field constitutive gravity claim is REDUCIBLE at equilibrium and OBSERVATIONALLY SILENT at all physical tau values.**

The equilibrium scalar stress-energy T^Phi, when evaluated on a Schwarzschild exterior, produces a metric correction delta_f(r) = -4*pi*M^2 / (tau^2 * r^2). This correction is:

1. **REDUCIBLE.** At equilibrium, the static T^Phi is identical to what GR + a massive scalar field (m_phi = 1/tau) sourced by gravity produces. The structural novelty of the constitutive equation lies in the DYNAMICS (first-order relaxation, native Lyapunov stability, broken time-reversal), not in the equilibrium gravitational coupling.

2. **OBSERVATIONALLY SILENT.** At every physical tau value in the GRUT program (tau_dyn for Mercury ~ 6e5 s, Earth ~ 3.5e6 s, solar surface ~ 1126 s), the effective PPN deviation |delta_beta| is 10^-16 or smaller. Current precision gravity (Cassini, LLR, Mercury precession) constrains |delta_beta| at the 10^-5 level. The gap is eleven orders of magnitude.

3. **SOURCE-AMBIGUOUS.** In the Schwarzschild exterior, the Ricci scalar R = 0. If X is Ricci-sourced (X ~ R), the scalar equation gives Phi = 0 in vacuum, producing NO correction. The correction computed here requires X = M/r^2 (gravitational acceleration), which is a specific choice not uniquely determined by the theory.

Even in the most favorable identification (X = M/r^2), tau must be below 2.5 milliseconds to produce a Cassini-detectable deviation. No physical tau in the GRUT program approaches this scale. The gravity frontier weakens sharply. GRUT's structural novelty lies in the DYNAMICS (native dissipation, Lyapunov stability, broken time-reversal), not in the equilibrium gravitational coupling.

---

## 2. Why Book XVI Beta Is Now Necessary

Book XVI Alpha identified the D7/D8 sign error in compact-object source amplification: the A_eff factor was a calculation artifact, and the compact-object frontier (mass deficit, tidal Love numbers) collapsed. The XVI Beta Structural Claim Audit identified the surviving irreducible claim as (1) native time-reversal breaking + (2) Phase 4 equilibrium T^Phi. The claim was validated against three criteria (C1-C3) and five adversarial attack vectors.

What was NOT done in that audit: quantitative confrontation of T^Phi with precision gravity observations. The claim that GRUT produces rho_eq = -X^2/(2tau^2) in the vacuum exterior is algebraically verified, but the question of whether this correction is (a) distinguishable from a generic massive scalar, (b) large enough to detect, and (c) capable of constraining tau was left open.

This document closes that gap. The result is adverse.

---

## 3. Reconstruction of the Post-XVI Gravity Problem (WORKSTREAM 1)

After XVI Alpha, the gravity-side program stands as follows:

- **Phase 4 (xAct-verified):** T^Phi exists, rho_eq = -X^2/(2tau^2), w = -1, NEC-saturated. Algebraically correct.
- **Book XIII (compact objects):** Collapsed. The strong-field interior predictions (f = -17.71, mass deficit, tidal Love) depended on source amplification that contained a sign error. These predictions are withdrawn.
- **Book XIV (TOV equilibrium):** Conditional. The equilibrium structure survives algebraically but produces no observationally distinct compact-object signature after XIII collapse.
- **Book XV (Layer 3 backreaction):** The time-dependent regime mismatch was identified; the static equilibrium does not require Layer 3.

The remaining gravity-side frontier is the WEAK-FIELD exterior: does T^Phi modify the Schwarzschild metric at detectable levels? This is the only precision-gravity question that survives XIII collapse.

---

## 4. Explicit Irreducible Claim Formulation (WORKSTREAM 2)

**Claim (gravity side):** The constitutive scalar Phi, governed by tau*dPhi/dt + Phi = X and minimally coupled to Einstein gravity, produces an equilibrium stress-energy in the vacuum exterior of a Schwarzschild source with mass M:

```
rho_eq(r) = -X^2 / (2*tau^2)
```

where X = M/r^2 in geometric units. This generates a metric correction:

```
delta_f(r) = -4*pi*M^2 / (tau^2 * r^2)
```

and an effective PPN deviation:

```
delta_beta = 4*pi / tau^2_geometric
```

**The claim asserts:** This correction is (1) structurally irreducible to GR + standard matter, (2) observable in principle, and (3) constrains the free parameter tau from existing data.

---

## 5. Irreducibility Audit (WORKSTREAM 3)

### vs GR + massive scalar field

A massive scalar field phi with mass m_phi = 1/tau, minimally coupled to gravity and sourced by the local gravitational potential, satisfies:

```
(Box - m_phi^2) phi = J
```

At static equilibrium (Box phi -> -m_phi^2 * phi = J), the scalar acquires phi = -J/m_phi^2 = -J*tau^2. The resulting stress-energy at equilibrium is a function of phi^2/tau^2, which reproduces the same scaling rho ~ -X^2/(2*tau^2) after identification of J with X/tau.

**Verdict: REDUCIBLE AT EQUILIBRIUM.** The equilibrium T^Phi is identical in form and scaling to the T_ab of a massive scalar with m_phi = 1/tau sourced by gravity. The two theories differ in DYNAMICS: the constitutive equation is first-order (dissipative, irreversible), while the Klein-Gordon equation is second-order (oscillatory, reversible). At static equilibrium, this dynamical distinction vanishes.

### vs R^2 gravity (Starobinsky)

R^2 corrections to the Schwarzschild exterior produce metric deviations scaling as ~ 1/r^6 (Yukawa suppression from the massive scalar degree of freedom in R^2 gravity). The GRUT correction scales as 1/r^2 (power-law from the equilibrium profile). The two are NOT equivalent: different radial dependence, different parametric scaling.

**Verdict: NOT EQUIVALENT.** Different scaling excludes identification with f(R) gravity.

### vs semiclassical vacuum polarization

Semiclassical corrections to the Schwarzschild exterior (Casimir-like vacuum energy) scale as ~ l_P^2 * M / r^5. The GRUT correction scales as M^2 / (tau^2 * r^2). Different powers of M, different powers of r, different suppression scales.

**Verdict: NOT EQUIVALENT.** Different origin and scaling.

### Overall irreducibility assessment

The constitutive gravity claim is NOT reducible to f(R) gravity or semiclassical corrections. It IS reducible to GR + a massive scalar at equilibrium. The irreducibility of GRUT therefore rests entirely on the DYNAMICAL distinction (first-order vs second-order), which is invisible in the static/equilibrium regime probed by precision gravity.

---

## 6. Weak-Field / Exterior Derivation (WORKSTREAM 4)

Starting from the equilibrium scalar energy density rho_eq(r) = -M^2 / (2*tau^2 * r^4), the perturbation to the Schwarzschild metric component f(r) = 1 - 2M/r is obtained by solving the linearized Einstein equation with this source.

The metric correction is:

```
delta_f(r) = -8*pi * integral[r, inf] (rho_eq(r') * r'^2 / r) dr'
           = -8*pi * integral[r, inf] (-M^2/(2*tau^2 * r'^4)) * (r'^2/r) dr'
           = 4*pi*M^2 / (tau^2 * r^2)  [with sign from negative rho]
```

Result: delta_f(r) = -4*pi*M^2 / (tau^2 * r^2).

At the solar surface (r ~ R_sun ~ 7e8 m, M_sun ~ 1.5 km in geometric units): the fractional correction to f(r) is delta_f / f ~ 4*pi * (1.5e3)^2 / (tau^2 * (7e8)^2) ~ 6e-11 / tau^2_geometric.

### Source identification ambiguity

The derivation assumes X = M/r^2 (gravitational acceleration). However, in the Schwarzschild exterior, R_ab = 0 and R = 0. If the source X is identified with curvature invariants (X ~ R, X ~ R_ab R^ab, etc.), then X = 0 in vacuum, Phi = 0 at equilibrium, and there is NO correction whatsoever. The entire weak-field prediction depends on the choice of source identification, which is not uniquely determined by the constitutive equation alone.

This is not a technical subtlety. It is a foundational ambiguity. The constitutive equation tau*dPhi/dt + Phi = X does not specify what X IS in terms of geometric quantities. Different identifications yield predictions ranging from zero to the values computed here.

---

## 7. PPN / Precision-Gravity Consequence Audit (WORKSTREAM 5)

The effective PPN deviation from the GRUT scalar at equilibrium:

```
delta_beta = 4*pi / tau^2_geometric
```

Evaluated at physical tau values (converting physical seconds to geometric units via c):

| Source | tau (seconds) | tau_geometric (m) | |delta_beta| |
|--------|--------------|-------------------|-------------|
| Mercury (t_dyn ~ 6e5 s) | 6e5 | 1.8e14 | 3.8e-22 |
| Earth (t_dyn ~ 3.5e6 s) | 3.5e6 | 1.05e15 | 1.1e-23 |
| Solar surface (t_dyn ~ 1126 s) | 1126 | 3.4e11 | 1.1e-16 |
| Aggressive (tau = 1 s) | 1 | 3e8 | 1.4e-10 |

Current experimental bounds on PPN parameters:

| Experiment | Parameter | Bound |
|-----------|-----------|-------|
| Cassini (2003) | |gamma - 1| | < 2.3e-5 |
| Nordtvedt / LLR | |beta - 1| | < 1.1e-4 |
| Mercury precession | combined | < 1e-3 |

At every physical tau value from the GRUT program, |delta_beta| is at least 11 orders of magnitude below the Cassini bound. The scalar tau = 1 s (which has no physical motivation in GRUT) produces a deviation 5 orders of magnitude below Cassini. The correction is observationally invisible.

---

## 8. Tau-Constraint Audit (WORKSTREAM 6)

Inverting the PPN deviation formula to obtain lower bounds on tau:

```
tau > sqrt(4*pi / delta_beta_max)
```

| Experiment | delta_beta_max | tau_min (geometric, m) | tau_min (seconds) |
|-----------|---------------|----------------------|------------------|
| Cassini | 2.3e-5 | 739 | 2.5e-3 |
| Nordtvedt / LLR | 1.1e-4 | 355 | 1.2e-3 |
| Mercury precession | 1e-3 | 112 | 3.7e-4 |

The strongest constraint is tau > 2.5 milliseconds from Cassini. This is a trivially weak bound. Every physical tau in the GRUT program (tau_0 ~ 10^-44 s at Planck scale excluded; t_dyn ~ 10^3 to 10^6 s for astrophysical systems) satisfies this bound by at least six orders of magnitude. The constraint provides no new information about the GRUT parameter space.

At the Cassini-bound value tau = 2.5 ms: |delta_beta| = 2.3e-5 by construction. This is not a prediction; it is the bound tautologically saturated.

---

## 9. Hard-Criteria Evaluation (WORKSTREAM 7)

| Criterion | Requirement | Status |
|-----------|------------|--------|
| Irreducible to GR + matter at equilibrium | Must differ from any known scalar theory | **FAILS** -- identical to GR + massive scalar |
| Irreducible dynamically | Must differ from second-order scalar | **PASSES** -- first-order vs second-order |
| Observable at physical tau | |delta_beta| > experimental bound | **FAILS** -- 11+ orders of magnitude below |
| Observable at any tau | Exists a tau where detectable | **PASSES** -- tau < 2.5 ms, but unphysical |
| Tau nontrivially constrained | Bound excludes program-relevant tau values | **FAILS** -- bound is tau > 2.5 ms; all physical tau >> this |
| Source identification unambiguous | X determined by theory | **FAILS** -- X = R gives zero; X = M/r^2 gives nonzero |

Four of six hard criteria fail. The surviving passes (dynamical irreducibility, unphysical-tau observability) do not constitute a viable gravity-frontier claim.

---

## 10. Failure / Limitation Localization (WORKSTREAM 8)

The failures localize to three independent causes:

**Cause 1: Equilibrium reducibility.** The constitutive equation's structural novelty is dissipation (first-order, irreversible). At equilibrium, dissipation has completed. The equilibrium state is static, and static scalar profiles are common to all scalar-tensor theories. The GRUT-specific content (the arrow, the Lyapunov decay) is absent at equilibrium. This is not a bug; it is the definition of equilibrium.

**Cause 2: tau^2 suppression.** The correction scales as 1/tau^2. Any physical tau (even the solar dynamical timescale ~ 1126 s) produces tau_geometric ~ 3e11 m. The squared denominator kills the correction. This suppression is structural: it comes from the equilibrium energy density rho_eq ~ 1/tau^2, which is the defining feature of the constitutive potential V = Phi^2/(2tau^2). Larger tau means weaker self-interaction, hence smaller backreaction.

**Cause 3: Source ambiguity.** The constitutive equation does not specify X in terms of geometry. The most natural geometric identification (X ~ R) gives X = 0 in vacuum and no correction at all. The correction computed here requires X = M/r^2, which imports Newtonian content not derivable from the constitutive equation alone.

None of these causes is remediable within the current GRUT framework without changing the constitutive equation or adding new postulates.

---

## 11. Frontier Consequence Audit (WORKSTREAM 9)

The gravity-side frontier after this audit:

- **Strong-field / compact objects:** COLLAPSED (XVI Alpha, D7/D8 sign error).
- **Weak-field / precision gravity:** COLLAPSED (this document; reducible + silent).
- **Cosmological T^Phi:** PARTIALLY SURVIVES. The FRW setting has R != 0, so X is nonzero under Ricci identification. The 3-regime H*tau analysis (Book XII) remains algebraically valid. However, the rho_eq < 0 result is cosmologically anti-accelerating, which conflicts with observed acceleration.
- **Dynamical regime:** SURVIVES. The first-order relaxation, Lyapunov stability, and broken time-reversal are irreducible, not shared by GR + massive scalar, and not probed by equilibrium observations. This is where GRUT's structural content resides.

The gravity frontier has narrowed from three sectors (strong-field, weak-field, cosmological) to one partial sector (cosmological, with sign conflict) plus the dynamical regime, which is a theoretical rather than observational frontier.

---

## 12. False-Positive Audit (WORKSTREAM 10)

Potential false positives that this audit guards against:

1. **"The correction is nonzero, therefore GRUT is testable."** FALSE. A nonzero correction that is 11 orders of magnitude below experimental sensitivity is not testable. Testability requires the correction to be within reach of current or planned experiments.

2. **"Dynamical irreducibility implies equilibrium irreducibility."** FALSE. The dynamical difference (first-order vs second-order) vanishes at equilibrium. Equilibrium is the time-independent limit, and both first-order and second-order dynamics reach the same static state (for appropriate parameter identification).

3. **"The tau constraint is meaningful."** FALSE. The constraint tau > 2.5 ms excludes no physically motivated tau value. A constraint that is satisfied by every candidate value constrains nothing.

4. **"The source ambiguity can be resolved later."** PARTIALLY TRUE, but the resolution determines whether the prediction is zero or nonzero. Until resolved, the weak-field prediction is not well-defined.

5. **"Planned experiments (LISA, next-gen LLR) will close the gap."** FALSE at physical tau. Even a factor-of-1000 improvement in PPN precision (to 10^-8) leaves a gap of 8 orders of magnitude at solar-surface tau. The gap is structural, not technological.

---

## 13. GRUT-RAI Weak-Field State-Model Requirements (WORKSTREAM 11)

The GRUT-RAI state model must record:

| Field | Value |
|-------|-------|
| weak_field_claim_status | REDUCIBLE_AT_EQUILIBRIUM |
| weak_field_observational_status | SILENT (corrections <= 10^-16 at physical tau) |
| source_identification_status | AMBIGUOUS (X = R gives 0; X = M/r^2 gives nonzero) |
| tau_constraint_from_gravity | tau > 2.5 ms (trivially satisfied) |
| gravity_frontier_status | WEAKENED -- strong-field collapsed (XVI Alpha), weak-field silent (this document) |
| irreducibility_locus | DYNAMICS ONLY (first-order relaxation, Lyapunov, arrow) |
| equilibrium_irreducibility | NONE (reducible to GR + massive scalar m_phi = 1/tau) |

These fields must propagate to any downstream audit that invokes gravity-side claims.

---

## 14. Program Consequence (WORKSTREAM 12)

The consequences for the GRUT program are:

1. **The gravity frontier is no longer a leading sector.** After XVI Alpha (strong-field collapse) and this document (weak-field silence), gravity provides no observationally accessible prediction at physical tau values. The program cannot claim precision-gravity testability.

2. **The irreducible content of GRUT is dynamical, not gravitational.** The first-order dissipation, Lyapunov stability, and native time-reversal breaking survive all audits. These are genuine structural novelties not present in GR + any second-order scalar. But they are theoretical properties of the equation, not gravitational observables.

3. **The equilibrium T^Phi remains algebraically valid.** The xAct-verified result rho_eq = -X^2/(2tau^2) is not retracted. It is correct. It is simply (a) reducible to a massive scalar at equilibrium, and (b) too small to observe at physical tau.

4. **Future program directions.** If the gravity frontier is to be revived, it requires either: (i) a dynamical (non-equilibrium) observable where the first-order vs second-order distinction is measurable, (ii) a new identification of tau that places it in the sub-second regime with physical motivation, or (iii) a coupling mechanism beyond minimal coupling that enhances the correction. None of these currently exists in the program.

5. **The biology scaffold, cosmological analysis, and quantum (Lindblad) extensions are unaffected.** These do not depend on weak-field gravity detectability.

---

## 15. Final Verdict

**VERDICT: (A)**

The weak-field constitutive gravity claim is reducible at equilibrium (identical to GR + massive scalar with m_phi = 1/tau), observationally silent at all physical tau values (corrections at or below 10^-16 in PPN), and source-ambiguous (X = 0 under Ricci identification). The gravity frontier weakens sharply.

GRUT's structural novelty -- the constitutive dissipation, the forward semigroup, the Lyapunov-guaranteed irreversibility -- survives intact. But it resides in the dynamics, not in the equilibrium gravitational coupling. Precision gravity cannot see it.

---

## Hard-Gated Summary Table

| Test | Verdict |
|------|---------|
| Irreducible claim written explicitly | YES |
| Irreducibility audited seriously | YES -- FAILS at equilibrium (reducible to GR + massive scalar) |
| Weak-field correction derived or bounded | YES -- delta_f = -4*pi*M^2/(tau^2 * r^2) |
| Tau constrained from observation | YES -- tau > 2.5 ms from Cassini; but physical tau >> this |
| Observational distinctness survives or collapses clearly | COLLAPSES -- corrections 10^-16 at physical tau |
| Frontier consequence determined | YES -- gravity frontier weakens sharply |
| Book XVI Beta changes gravity interpretation | YES -- equilibrium claim is reducible + silent |

---

*Document generated by GRUT-RAI adversarial audit. No protection applied to the gravity frontier.*
