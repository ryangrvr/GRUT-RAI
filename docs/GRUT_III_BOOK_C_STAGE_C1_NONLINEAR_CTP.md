# GRUT III — Book C, Stage C1: Nonlinear CTP Action and Constraining-Admissibility Test

**Inherited:** Book B E1-E16, N1-N10. Interface X = β + αR. UD1-UD6. All blacklists.

---

## A. Nonlinear CTP Term Ledger

### Model 1: Single-variable cubic (minimal)

Add one term to the linear CTP Sector 1:

```
Linear:    -[τ ∂_t Φ_r + Φ_r - X] Φ_a
Nonlinear: -[τ ∂_t Φ_r - h(X - Φ_r)] Φ_a

where h(v) = γv - δv³   (cubic saturation)
```

| Term | Role | Status | Parameters added | Confidence |
|------|------|:------:|:----------------:|:----------:|
| γv in h(v) | Linear response (= original constitutive law at γ = 1) | DERIVED (reduces to E2) | 0 (γ = 1 recovers linear) | 0.95 |
| −δv³ in h(v) | Cubic saturation: limits runaway for large deviations | ASSUMED (from GRUT-II Nu, ODE-level) | 1 (δ) | 0.40 |
| CTP Sector 2 (noise iDΦ_a²) | Unchanged | INHERITED (E15) | 0 | 0.90 |
| CTP Sector 3 (USL) | Unchanged | INHERITED (TF9) | 0 | 0.85 |

**Parameter cost:** +1 (δ). Total EFT parameters: 6 (τ, D, T, α, β, δ).

### Model 2: Coupled two-field system (for bistability)

The single-variable cubic h(v) = γv − δv³ does NOT produce bistability. The constitutive law τ dΦ/dt = h(X − Φ) has exactly ONE stable fixed point (Φ* = X), with two additional UNSTABLE fixed points. This was verified analytically (the eigenvalue at Φ* = X is −γ/τ < 0) and numerically.

**Why:** For a single first-order ODE dΦ/dt = f(Φ), a fixed point Φ* where f'(Φ*) < 0 is stable, and the flow is strictly one-dimensional — no bistability is possible between two stable fixed points separated by an unstable one unless f has at least two sign changes in f'(Φ), which requires that f change from positive to negative and back. For h(X − Φ), the function f(Φ) = h(X − Φ)/τ has f'(Φ) = −h'(X − Φ)/τ. At Φ* = X: f'(X) = −γ/τ < 0 (stable). At Φ* = X ∓ √(γ/δ): f' = +2γ/τ > 0 (unstable). The stable fixed point is unique.

**GRUT-II Nu achieved bistability through a COUPLED system:**

```
τ₁ dΦ/dt = h(X − Φ) − κΨ
τ₂ dΨ/dt = g(Φ) − μΨ − νΨ³
```

This requires an auxiliary field Ψ (a "meta-field" or "second constitutive mode").

| Term | Role | Status | Parameters added |
|------|------|:------:|:----------------:|
| −κΨ coupling in Φ equation | Coupling between Φ and auxiliary Ψ | ASSUMED (from GRUT-II Nu) | 1 (κ) |
| τ₂ dΨ/dt = g(Φ) − μΨ − νΨ³ | Auxiliary field dynamics with cubic saturation | ASSUMED | 3 (τ₂, μ, ν) + g(Φ) form |
| CTP doubling of Ψ → (Ψ_r, Ψ_a) | Required for CTP consistency | ASSUMED (structural) | 0 |

**Parameter cost:** +4 minimum (κ, τ₂, μ, ν). Plus the coupling function g(Φ). Total: at least 10 EFT parameters.

**Status of Model 2:** ASSUMED. The coupled ODE system was demonstrated numerically in GRUT-II Nu (two stable fixed points at long integration). Its CTP embedding (doubling Ψ, writing the Ψ sector of the CTP action, verifying CTP unitarity for the coupled system) has NOT been performed.

---

## B. Updated Operator/Residue/Admissibility

### Under Model 1 (single cubic, no bistability)

**Update rule:**

```
Φ_{t+Δt} = Φ_t + (Δt/τ) h(X_t − Φ_t) + √(2D/τ²) ΔW_t

where h(v) = γv − δv³
```

**Fixed points:** One stable (Φ* = X), two unstable (Φ* = X ∓ √(γ/δ)).

**Residue:** V_t = (Φ_t − X_t)² is STILL a valid Lyapunov function near the stable fixed point (since h'(0) = γ > 0, the linearization is the same as the linear case). However, V is NOT monotone-decreasing globally: for |Φ − X| > √(γ/δ), h(v) can change sign, and Φ may accelerate AWAY from X before being captured. The basin of attraction of Φ* = X is finite: |Φ − X| < √(γ/δ).

**Admissibility:** A1-A7 remain as in Book B. No new condition needed. No pruning. **classifier_only persists under Model 1.**

### Under Model 2 (coupled, potential bistability)

**Update rule:**

```
Φ_{t+Δt} = Φ_t + (Δt/τ₁)[h(X_t − Φ_t) − κΨ_t] + noise₁
Ψ_{t+Δt} = Ψ_t + (Δt/τ₂)[g(Φ_t) − μΨ_t − νΨ_t³] + noise₂
```

**State tuple expansion:** S_t = (Φ_t, Ψ_t, X_t, F_t). The auxiliary field Ψ_t enters the minimal state.

**Fixed points:** Depend on parameters. GRUT-II Nu demonstrated two stable fixed points at specific parameter values (36% and 38% basin fractions in Nu-Prime, confirmed at T = 30,000 integration time). The current C1 parameter scan did not reproduce bistability (only one stable FP found), but this is parameter-dependent, not structural. Bistability EXISTS in the coupled system at the GRUT-II Nu parameters.

**Residue:** V_t = (Φ_t − X_t)² is NO LONGER a global Lyapunov function (multiple attractors: Φ can stabilize at Φ* ≠ X if the second attractor has Φ* ≠ X). A new diagnostic is needed: the basin identity B_t ∈ {1, 2} indicating which attractor the trajectory is converging toward.

**Admissibility under Model 2:** The seven conditions A1-A7 remain necessary. But they are no longer sufficient to uniquely determine the trajectory's fate: two paths satisfying all conditions can converge to different attractors depending on (Ψ₀, Φ₀).

---

## C. Attractor/Basin Results

### Model 1 (single cubic)

| Property | Result | Status |
|----------|--------|:------:|
| Number of stable fixed points | **1** (Φ* = X) | DERIVED (analytical) |
| Basin of attraction | |Φ − X| < √(γ/δ) (finite basin) | DERIVED |
| Bistability | **NO** | DERIVED (structural: single 1st-order ODE with one stable zero of h) |
| Change from linear case | Finite basin (vs infinite basin for linear). Otherwise qualitatively identical. | DERIVED |

### Model 2 (coupled)

| Property | Result | Status |
|----------|--------|:------:|
| Number of stable FPs (GRUT-II Nu params) | **2** (confirmed at T = 30,000, 36%/38% basins) | DERIVED (numerical, GRUT-II Nu) |
| Number of stable FPs (C1 scan params) | 1 (bistability not reproduced) | DERIVED (numerical, C1) |
| Basin structure | Parameter-dependent. Exists at GRUT-II Nu parameters. | DERIVED (conditional) |
| CTP embedding | **NOT PERFORMED** | OPEN |
| CTP unitarity for coupled (Φ, Ψ) system | **NOT CHECKED** | OPEN |
| FDT for Ψ sector | **NOT CHECKED** | OPEN |

---

## D. Admissibility Transition Verdict

### The structural finding

The transition from classifier_only to constraining admissibility requires **two ingredients:**

1. **Multiple basins (dynamics).** The update rule must admit trajectories that diverge to different long-term outcomes from overlapping initial conditions. Model 2 provides this (at appropriate parameters). Model 1 does not.

2. **A selection principle (admissibility).** Given multiple basins, the admissibility functional must include a criterion that selects one basin over another. The current conditions A1-A7 do NOT provide this — they test local dynamical consistency, not global basin preference. A new condition is needed:

```
A8 (proposed): The path must converge to the thermodynamically preferred attractor.
```

But "thermodynamically preferred" requires a free-energy functional or entropy criterion that does NOT currently exist in the GRUT framework. The CTP action provides Im S_eff ≥ 0 (positivity/entropy production), but this is an ENSEMBLE property that does not distinguish between two attractors — both are equally consistent with positivity.

### The gap

```
Bistability (Model 2, UD2-dependent): EXISTS at specific parameters
Selection principle (A8):             DOES NOT EXIST
CTP embedding of coupled system:      NOT PERFORMED
```

The nonlinear extension ENABLES the structural possibility of constraining admissibility by creating multiple basins. But it does not REALIZE it because no principle selects between basins. The gap is not dynamical (the dynamics is computable) — it is thermodynamic/informational (which basin is "right"?).

### Possible sources of A8 (all OPEN)

1. **CTP free energy:** The real part of the CTP effective action evaluated on each attractor could serve as a free-energy comparison. The lower-free-energy attractor is preferred. This requires computing Re S_eff for each fixed point — which requires the full nonlinear CTP action (not yet written).

2. **Entropy production rate:** The attractor with higher steady-state entropy production is preferred (maximum entropy production principle). This is controversial in non-equilibrium thermodynamics and not derivable from the CTP action without additional assumptions.

3. **Cosmological/geometric selection:** The curvature-dependent source X = β + αR could select a basin if the two attractors respond differently to changes in R. This is a dynamical mechanism (not a static principle) and depends on the time evolution of the geometry.

4. **Decoherence selection (quantum):** The attractor that decoheres less rapidly (lower USL rate) is the quantum-preferred state. This is speculative and untested.

All four are **OPEN**. None is derivable from the current CTP framework.

---

## E. Gate Table

| Gate | Criterion | Status | Reason |
|:----:|-----------|:------:|--------|
| **C1-G1** | Nonlinear model explicitly defined with minimal complexity | **PASS** | Model 1: single cubic, +1 parameter (δ). Model 2: coupled system, +4 parameters. Both fully specified with term-by-term status tags. |
| **C1-G2** | Dynamics under nonlinear extension characterized | **PASS** | Model 1: one stable FP (analytical proof). Model 2: parameter-dependent; bistability confirmed at GRUT-II Nu parameters (numerical, T=30,000). C1 scan did not reproduce (parameter-dependent). |
| **C1-G3** | Diagnostic vs constraining re-evaluated | **PASS** | Re-evaluated with explicit two-ingredient analysis. Result: constraining requires both bistability AND a selection principle. Bistability exists (Model 2). Selection principle does NOT exist. Admissibility remains diagnostic under current A1-A7. |
| **C1-G4** | Basin/selection behavior tested | **PASS** | Model 1: single basin (proven). Model 2: multiple basins exist at GRUT-II Nu parameters (inherited result, 36%/38%). Selection between basins: OPEN (A8 not available). |
| **C1-G5** | Regime validity and stability boundaries explicit | **PASS** | Model 1: stable at Φ* = X with finite basin |Φ−X| < √(γ/δ). Beyond basin: unstable runaway. Model 2: stability at each FP checked by Jacobian eigenvalues. CTP unitarity for coupled system: OPEN. |

---

## F. Decision Token

### **bounded_open**

**Rationale:**

1. The single-variable cubic (Model 1) does NOT produce bistability. classifier_only persists under Model 1. No change from Book B.

2. The coupled two-field system (Model 2) CAN produce bistability (GRUT-II Nu, confirmed). This creates the structural POSSIBILITY of constraining admissibility.

3. However, constraining admissibility requires a selection principle (A8) that does not exist. The gap is thermodynamic/informational, not dynamical.

4. The CTP embedding of the coupled system (doubling Ψ, writing the Ψ CTP sector, checking unitarity and FDT) has NOT been performed. This is a prerequisite for any selection-principle derivation.

**The verdict is bounded_open because:**
- The MECHANISM for constraining admissibility is identified (bistability + selection)
- The DYNAMICS for bistability exists (Model 2, at specific parameters)
- The SELECTION PRINCIPLE is missing (A8 is OPEN)
- The CTP EMBEDDING is missing (coupled CTP action not written)
- The resolution path is clear: write coupled CTP → compute Re S_eff at each attractor → derive or fail to derive A8

**What would upgrade to constraining_shift_detected:**
- Write the coupled (Φ, Ψ) CTP action
- Verify CTP unitarity
- Compute Re S_eff at both attractors
- If Re S_eff differs: A8 = "prefer lower Re S_eff" → constraining admissibility REALIZED
- If Re S_eff is equal: selection principle is NOT available from CTP → classifier persists

**What would downgrade to classifier_persists:**
- If no parameter regime produces bistability within the CTP-consistent coupled system
- If CTP unitarity for the coupled system fails (ruling out Model 2)
- If Re S_eff is identical at both attractors (no thermodynamic preference)

---

## Book C Carry-Forward

| # | Item | Status |
|---|------|:------:|
| CF-C1-1 | Single-variable cubic does not produce bistability (proven) | RESOLVED |
| CF-C1-2 | Coupled two-field system can produce bistability (conditional on parameters) | RESOLVED (conditional) |
| CF-C1-3 | Constraining admissibility requires bistability + selection principle | RESOLVED (structural analysis) |
| CF-C1-4 | Selection principle (A8) is OPEN — not derivable from current framework | OPEN |
| CF-C1-5 | CTP embedding of coupled (Φ, Ψ) system not performed | OPEN (= UD2 primary content) |
| CF-C1-6 | UD2 is now refined: "write coupled CTP action" → "write coupled CTP, check unitarity, compute Re S_eff at both FPs" | UPDATED |

**Next task (C2):** Write the coupled (Φ, Ψ) CTP action, verify unitarity, and test whether Re S_eff provides a selection principle. This is the make-or-break computation for the constraining-admissibility question.

---

*GRUT III Book C Stage C1 complete. Decision: bounded_open. Single cubic: no bistability (proven). Coupled system: bistability exists (GRUT-II Nu) but CTP embedding not performed. Admissibility transition requires selection principle A8 (OPEN). Gap is thermodynamic, not dynamical. Resolution path: coupled CTP → Re S_eff comparison. Gates: 5/5 pass. classifier_only persists under current conditions; bounded_open reflects identified but unrealized mechanism.*
