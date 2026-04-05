# Book XVII — Target Alpha: Dynamical Theorem Matrix

---

## Table 1 — Theorem Inventory

| # | Theorem | Statement | Assumptions | Authority |
|---|---------|-----------|-------------|-----------|
| 1 | Forward semigroup | S(t) = exp(-t/tau); Phi(t) = X + (Phi_0 - X)S(t); S(t+s) = S(t)S(s); S(t) exists for t >= 0 only | Linear first-order ODE; tau > 0; X constant or quasi-static | LOCKED (Book II) |
| 2 | Lyapunov stability | V = (1/2)(Phi - X_ss)^2; dV/dt = -(2/tau)V < 0; global attractor Phi = X_ss | Same + steady-state X_ss exists | LOCKED (TC) |
| 3 | Dissipative balance | dV/dt + D = 0; D = (Phi - X)^2/tau >= 0; exact identity (autonomous) | Same as Theorem 1 | LOCKED (TC) |
| 4 | Native T-breaking | Equation not invariant under t -> -t; time reversal gives growing mode exp(+t/tau) | First-order form taken as fundamental | LOCKED (Book II) |
| 5 | Monotone contraction | \|\|Phi(t) - X\|\| <= \|\|Phi(0) - X\|\| exp(-t/tau); no overshoot; no oscillation | Same as Theorem 1 | LOCKED (TC) |

---

## Table 2 — Domain-of-Validity Table

| Sector | Th1 (Semigroup) | Th2 (Lyapunov) | Th3 (Balance) | Th4 (T-break) | Th5 (Monotone) |
|--------|-----------------|----------------|---------------|---------------|----------------|
| Vacuum (Phase I-II) | LITERAL | LITERAL | LITERAL | LITERAL | LITERAL |
| Gravity equil. (Phase 4) | LITERAL (static) | LITERAL (static) | LITERAL (static) | LITERAL | LITERAL |
| Quantum (QC5) | RECOVERED (3 limits) | ANALOG | NOT FORMALIZED | INHERITED | RECOVERED |
| Cosmology (App A) | HEURISTIC | CONDITIONAL | CONDITIONAL | ASSUMED | CONDITIONAL |
| Defects (D1-D14) | N/A | N/A | N/A | N/A | N/A |
| Wave propagation (W-F) | N/A | N/A | N/A | N/A | N/A |
| Biology (IV-X) | N/A | N/A | N/A | N/A | N/A |
| Carriers (VII-IX) | N/A | N/A | N/A | N/A | N/A |

**Literal scope: 2 sectors. Recovered/conditional: 1-2 sectors. Excluded: 4 sectors.**

---

## Table 3 — Embeddability Comparison Table

| Candidate Parent | Test Result | What's Reproduced | What's NOT Reproduced | T-Breaking Status |
|-----------------|-------------|-------------------|----------------------|-------------------|
| **Lagrangian (delta S = 0)** | **NOT EMBEDDABLE** | Nothing (produces second-order, reversible EOM) | First-order form; dissipation; semigroup contraction | Survives (native) |
| **Hamiltonian (H, {,})** | **NOT EMBEDDABLE** | Nothing (preserves phase-space volume) | Contraction; Lyapunov; dissipation | Survives (native) |
| **KG scalar + thermal bath** | **EMBEDDABLE (overdamped limit)** | Entire ODE: tau dPhi/dt + Phi = X in overdamped regime | Nothing missing at effective level | Emergent (from bath) |
| **Lindblad + classical limit** | **RECOVERED (3 limits)** | Expectation-value equation matches | Operator content (L postulated); beyond-Markovian regime | Inherited (from Lindblad) |
| **Generic open system** | **GENERIC** | All 5 theorems (shared by any linear first-order dissipative system) | Specific ODE form (tau^2 = 3/2; X = m/r^2 coupling) | Generic (any open system) |

---

## Table 4 — Irreducible-Wedge Table

| Comparison Class | Irreducible? | What GRUT Has | What Comparison Has | Verdict |
|-----------------|--------------|---------------|---------------------|---------|
| vs Conservative (L, H) | **YES** | Dissipation, contraction, semigroup, T-breaking | None of these | **GENUINE WEDGE** |
| vs KG + bath (overdamped) | **NO** | All 5 theorems | All 5 theorems (in overdamped limit) | **NO WEDGE** (embeddable) |
| vs Generic open system | **NO** (structural properties) | Semigroup, Lyapunov, T-breaking | Same (any 1st-order dissipative) | **GENERIC** |
| vs Generic open system | **PARTIAL** (specific content) | tau^2 = 3/2; X = m/r^2; GR coupling | Not these specifically | **SPECIFIC but NARROW** |

**Net irreducible content: CONDITIONAL.** Genuine against conservative. Generic against open systems. Specific ODE is unique but unanchored.

---

## Table 5 — Hard-Criteria Pass/Fail Matrix

| Criterion | Verdict |
|-----------|---------|
| 1. Theorem clarity | **PASS** |
| 2. Scope clarity | **PASS** |
| 3. Embeddability pressure | **PARTIAL** (conservative: clear; open-system: generic) |
| 4. Remaining irreducible content | **CONDITIONAL** |
| 5. Observational consequence potential | **ABSENT** |
| 6. Whole-program value | **MODERATE** |
| 7. Worthiness for frontier work | **CONDITIONAL** |

---

## Table 6 — Limitation/Failure Table

| Limitation | Severity | Detail |
|-----------|----------|--------|
| Structural properties generic | HIGH | Semigroup, Lyapunov, T-breaking shared by ALL 1st-order dissipative systems |
| Observationally unanchored | HIGH | No measurement connects theorems to data |
| Coarse-grained embeddability | MODERATE | ODE reproducible from KG + bath in overdamped limit |
| Ontological not physical | MODERATE | Whether first-order is fundamental = choice, not result |
| Gravity coupling silent | HIGH (inherited) | GR-connected predictions are equilibrium-reducible and weak-field silent |
| Decoherence conditional | MODERATE | tau_dec = tau/2 depends on postulated L |

---

## Table 7 — Frontier Consequence Table

| Aspect | Before XVII Alpha | After XVII Alpha |
|--------|-------------------|------------------|
| Dynamical core | "Surviving irreducible content" | "Conditional wedge; generic among open systems" |
| Theorems | "5 unanchored theorems" | "5 proven, scoped, embeddability-tested theorems" |
| Non-embeddability | Assumed | PROVEN against conservative; FAILS against open-system |
| Observational path | "Search for tau constraint" | "No path identified from dynamics alone" |
| Program identity | "Recentered on dynamics" | "Conditional dynamical wedge; productivity in extensions" |
| Next step | "Dynamical consolidation" | "Deploy architecture in productive sectors (biology, quantum)" |

---

## Table 8 — Final Classification

| Aspect | Status |
|--------|--------|
| **Global verdict** | **(B) Conditional irreducible wedge** |
| Theorem consolidation | COMPLETE (5 theorems, explicit, locked) |
| Scope audit | COMPLETE (2-3 literal, 4 excluded) |
| Embeddability | PROVEN not embeddable in conservative; embeddable in open-system overdamped limit |
| Irreducible content | CONDITIONAL (vs conservative: genuine; vs open-system: generic) |
| Observational anchor | ABSENT |
| T-breaking status | NATIVE against conservative; EMERGENT in coarse-grained picture |
| Gravity frontier | FROZEN (inherited from XVI) |
| Biology scaffold | INTACT |
| Cost | 16/11/1/6 (unchanged) |
| Next step | Deploy architecture where it has leverage; or search for specific-ODE observable |

---

*Dynamical Theorem Matrix complete. 8 tables. 5 theorems. Conditional wedge. Generic properties. Next: productivity.*
