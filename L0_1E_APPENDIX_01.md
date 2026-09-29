# L0-1e — D-DET EXACT APPENDIX 01 (the evaluated record; adds no line, changes no label)

**Date:** 2026-09-29 · **Frozen list:** `L0_1E_THEOREM_01.md` §6,
committed at `550a237` **before** evaluation · **Instrument:**
`calc/l01e_appendix.py` (`b41b00a`) · **Artifact:**
`L0_1E_APPENDIX_RESULT.json` (sha `1aed5c1ee1b85948…`) · **One
evaluation:** 34 exact Lyapunov solves, 93 s.

## Part A — identity verifications: **11/11 passed, zero defects**

The theorem document is confirmed at every point it claimed:
- A1 sealed replication (bit-exact);
- A2 the closed-form spectrum (to 1.8×10⁻¹⁴);
- A3 the exact Lyapunov solutions;
- A4 the odd-moment hierarchy (m₁, m₃, m₅, exact at all 34 profiles);
- **A5 O-3's instantiation:** KΣ = I, mₙ = s_{n−1} for n = 1 … 47,
  exact CM with d_c = 23;
- A6 the detailed-balance break at every nonuniform profile;
- A7 strict positivity of y;
- A8 the identity breaches and interiors;
- A9 Perron;
- A10 cone consistency along every ray, with the float thresholds
  agreeing with the exact statuses (no defect);
- A11 the comparator certification.

## Part B — the evaluated quantities (reported; not gated; not predictions)

**B1 / B2: the cone, located.**

| Family | Exact statuses | Float threshold (from T-2) |
|---|---|---|
| Ramp (hot far end) | G(2) ✓, G(10) ✓, **G(100) ✗**, G(1000) ✗, G(∞) ✗ | **R* ≈ 83.16**, exactly bracketed by G(10) ✓ / G(100) ✗. It lies below T-8's m₃ bound of 139.4. |
| Reversed ramp (hot retained site) | GR(10) ✓, GR(1000) ✓, **GR(∞) ✓** | **R* = ∞** — CM at every strength. The ramp line's lower exit is R₋ ≈ −11.6 < 0, consistent with GR(∞) ∈ 𝒦. |
| Hot spot (site 12) | **H(1000) ✓**, H(∞) ✗ | R* ≈ 9800 |
| Step profiles 1_{[1..m]} | **all 22 ✓** | — |

**B3–B6 (maps):**
- **Memory:** the P_memory^corr envelope comparator reads
  EXPONENTIAL-GRADE at **every** profile, the breach members included.
- **Component (b), monotone decrease, holds at every profile,**
  including every CM breach. So (a) and (b) held everywhere while (c)
  broke beyond threshold: the registry's components are again shown to
  be independent.
- Breaches sit in the **fast** modes (G(100): modes 18–23; G(1000):
  11–23), as Perron requires.
- **FDT-deviation ratios:**
  - near 1 at mild profiles;
  - 0.52 → 0.08 (n = 2 → 5) at G(100);
  - **negative** at G(1000);
  - **exactly 1.000 at H(1000)** for n = 2 … 5. The distant hot spot is
    invisible to low moments, as T-7 said.

## Three findings the frozen list surfaced (labeled precisely)

**1. Post-evaluation corollary (theorem-grade, given B1's exact step
statuses and T-6): every temperature profile that is nonincreasing away
from the retained site yields a completely monotone correlation.**
- Any nonnegative profile with T₁ ≥ T₂ ≥ … ≥ T₂₃ can be written as
  Σ_m (T_m − T_{m+1})·1_{[1..m]} (taking T₂₄ = 0; the m = 23 step is
  U), with nonnegative coefficients.
- All 23 steps are exactly in the cone (22 evaluated exactly in B1, and
  U by identity). The cone is convex.
- **So the whole nonincreasing class lies in 𝒦.**

This answers the orientation question far more strongly than the one
reversed-ramp shape did. *Within this chain: a retained site at least
as hot as everything farther away always carries a completely monotone
autocorrelation, however steep the gradient.* The step profiles were
frozen as T-10's *sufficient route*, before evaluation. The corollary
is the same convexity argument applied to the same frozen data, and it
is labeled as derived after evaluation.

**2. The size of the detailed-balance break does not predict
correlation CM.** The commutator ratio ‖KΣ − ΣK‖/‖KΣ‖, which measures
how far the noise breaks detailed balance:

| Profile | Commutator ratio | Exact CM |
|---|---|---|
| G(100) | 0.075 | fails |
| G(1000) | 0.076 | fails |
| **GR(1000)** | **0.076** (the same) | **passes** |
| **H(1000)** | **0.866** (about 11× larger) | **passes** |

Here, what decides CM is **where the heat sits relative to the retained
site**, not how far the system is from detailed balance. That
strengthens §5 of the theorem document for O-7, with the same scope
caveats.

**3. The exact battery was necessary.** G(100)'s breach is real
(exact, six negative weights). But:
- it **passes the m₃ and m₅ necessary conditions**, so it is a
  higher-order breach;
- its operational trajectory-Gram minimum eigenvalue is only
  **−9.2×10⁻¹³, below the house tolerance of −10⁻¹⁰.**

A time-domain battery at the L0-1c/d tolerance would have **missed** it.
In L0-1d the trajectory Gram was far more sensitive than expected.
Here, one breach sits beneath it. Both results are recorded, and
neither is generalized.

## What this adds, and what it does not

- **O-3 (DISCHARGED)** is instantiated exactly (A5).
- **O-4:** the proposed label, CLASS-SPLIT, is identity-determined, as
  the theorem document said, and this appendix does not change it. It
  **locates the split**:
  - interior: all nonincreasing-from-retained-site profiles
    (corollary 1), and the FDT neighbourhood;
  - breach: the ramp beyond R* ≈ 83 (exactly between 10 and 100), the
    hot spot beyond R* ≈ 9800, and every profile with T₁ = 0.
- **Nothing here is a property → ingredient edge.** The reversal
  diagnostic's graph stays acyclic.
- No channel moves. O-1 and O-3 are terminal; O-2, O-5, O-6, O-7 are
  unchanged.

**HARD STOP.** Recorded pending the owner's assignment of **O-4's
terminal label** (proposed: CLASS-SPLIT, identity-determined). Next in
the adopted sequence is **D-ORD** (O-5 theorem document, then O-6).
O-2 stays open with its named candidate.
