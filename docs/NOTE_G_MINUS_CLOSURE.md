# NOTE — g_- CLOSURE STATUS AUDIT

**Classification:** `static_source_vanishes_under_galley_projection__g_minus_zero_not_guaranteed_due_to_homogeneous_modes__component_b_implausible_not_impossible`
**Date:** 2026-03-28
**Depends on:** route_b_component_b.py, metric_closure_program.py (Appendix K), interior_metric_closure.py (Appendix J), galley_truncation.py
**Implementation:** `grut/g_minus_closure_audit.py`
**Tests:** `tests/test_g_minus_closure_audit.py`

---

## Purpose

Appendix K (metric_closure_program.py) catalogued six candidate energy-density sources and left one explicit open door:

> *"Route B g_- / doubled-metric sector: energy density NOT computed in closed form; 1/r² cannot be ruled out"*

This note resolves that open door as far as it can be resolved without computing the g_- energy density in closed form.

**Result: conditional partial closure.**
- The source-driven path is closed.
- The homogeneous path remains open.
- This is stronger than "unresolved" and weaker than a universal no-go.

---

## The Structural Argument

The g_- field equation in the Galley doubled formalism takes the form:

```
L[g_-] = T^Phi_1_munu - T^Phi_2_munu
```

where L is the linearized (wrong-sign) Einstein operator and the right-hand side is the stress-energy difference between the two doubled fields.

At GRUT static equilibrium (Φ_1 = Φ_2 = Φ_eq, Φ̇ = 0):

```
T^Phi_1_munu = T^Phi_2_munu = rho_eq   (same field, same solution)
source = T^Phi_1 - T^Phi_2 = 0  (exactly)
```

If g_- = 0 follows from source = 0, then g_- contributes nothing to the effective stress-energy entering the g_+ equation — and no Component B can arise.

The catch is that **"source = 0 ⟹ g_- = 0" requires three explicit conditions**, not all of which are established.

---

## The Three Conditions

| Condition | Description | Status |
|-----------|-------------|--------|
| **1. Static boundary conditions** | Φ_1 and Φ_2 satisfy the same equilibrium BCs (same equation, same source X = M/r², Φ̇ = 0) | **Satisfied** — under GRUT static equilibrium assumption |
| **2. Absence of homogeneous solutions** | L[g_-] = 0 has no growing solutions (no unstable modes of the wrong-sign EH action) | **LIKELY FALSE** — wrong-sign EH is expected unstable (route_b_component_b.py); homogeneous modes expected to exist |
| **3. Galley projection assumption** | The physical limit g_- → 0 is a consistent truncation of the doubled system | **Assumed** — Galley formalism assumption; NOT an attractor (galley_truncation.py) |

Because **Condition 2 is likely false** (wrong-sign EH expected unstable), the inference is split into two paths:

### Source-driven path (conditions 1+3)
Both conditions 1 and 3 hold. Source = 0 under the Galley projection. On this path, g_- = 0 and its contribution to the effective stress-energy is zero. **No Component B from the source-driven path. CLOSED.**

### Homogeneous path (requires condition 2)
Even with source = 0, the wrong-sign EH action L[g_-] = 0 may admit non-trivial solutions from initial conditions or unstable modes. Whether these homogeneous solutions:
- (a) develop significant amplitude, and
- (b) have 1/r² spatial profile
cannot be established without computing the spectrum of L[g_-] = 0. **This path remains open.**

---

## Phi_- Scalar Sector (Confirmation)

The Phi_- (scalar difference) sector is already closed by route_b_component_b.py Result B:
- Kinetic sign = −1 (ghost)
- Radial power = 4 (Component A profile, not 1/r²)
- Provides Component B: **No**

Confirmed here without new analysis.

---

## Dynamic Case

When Φ̇ ≠ 0, the source T^Φ_1 − T^Φ_2 is nonzero and g_- is actively driven. However:
- The dynamic Killing horizon (f = 0 at A ≥ A_crit ≈ 1.062) is fully explained by kinetic Component A alone — this is the Appendix J locked result.
- The g_- correction enters at first order in g_-, subleading relative to the dominant kinetic cancellation.
- Any dynamically-sourced g_- is time-dependent, not a static source of Component B.

Dynamic g_- does not open a new static closure path.

---

## Verdict

```
source_path_closed   = True   (source-driven path: closed under conditions 1+3)
homogeneous_path_open = True  (homogeneous path: open, condition 2 likely_false)
universal_no_go      = False  (nonclaim: not a universal theorem)

verdict: "static_source_vanishes_under_galley_projection__
          g_minus_zero_not_guaranteed_due_to_homogeneous_modes__
          component_b_implausible_not_impossible"
```

**Position relative to prior status:**
- Prior (route_b_component_b.py): `"unresolved"` — 1/r² cannot be ruled out
- This note: `conditional partial closure` — source path ruled out; homogeneous path characterised as the specific remaining unknown

The remaining unknown is well-characterised: it is the stability spectrum of the linearized wrong-sign Einstein-Hilbert equation L[g_-] = 0. This is a defined mathematical object, not an amorphous "unknown unknown."

---

## Nonclaims

1. **This note does NOT compute the g_- energy density.** The closure is at the source level.
2. **Component B from homogeneous g_- solutions is NOT ruled out.** The homogeneous path is open.
3. **This note does NOT apply to non-Galley CTP formalisms.** Only the Galley doubled-field construction is assessed.
4. **The source-path closure is conditional on Φ_1 = Φ_2 = Φ_eq** — the GRUT static equilibrium assumption inherited from tov_interior.py.
5. **universal_no_go = False.** The Component B search for the current architecture is not exhaustively closed.

---

## Summary Table

| Channel | Status | Component B? |
|---------|--------|-------------|
| Post-projection Route B | Closed (= Route C, 1/r⁴) | No |
| Φ_- scalar sector | Closed (ghost, 1/r⁴) | No |
| g_- source-driven path | **Closed** (source = 0 at static equilibrium) | No |
| g_- homogeneous path | **Open** (wrong-sign EH stability unknown) | Undetermined |
| Dynamic g_- (A ≥ A_crit) | Subsumed under A_crit scenario | Not a new mechanism |
| O(3) hedgehog | Algebraically viable; not GRUT-native | Yes (not native) |
