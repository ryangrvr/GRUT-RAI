# μ OWNER DECISION PACKAGE

**Date:** 2026-09-01 · **Authorization:** owner, post-μ-audit ·
**Instrument:** `wall_kr_mu_owner_package.py` · **Companion:**
`WALL_KR_MU_OWNER_DECISION_RESULT.json` · **Battery: 20/20, zero
failures.** · **Frozen inputs touched: NONE** (re-hashed byte-identical).
**No calculation was performed. No value of μ was selected.**
**W-0: computed-and-reported, NOT banked. HARD STOP.**

## CRITICAL FIREWALL (required, verbatim)

> **"No numerical value for μ may be selected by optimizing, preserving,
> creating, removing, or matching an Axis-2 spectral or memory
> outcome."**
>
> **"μ = WC is not licensed by dimensional analysis alone."**
>
> **"The comparator-side plant is not an admissible source for fixing
> μ."**

Enforced mechanically: the instrument's executable body was scanned and
contains no Axis-2 outcome token, no regime verdict, and no
WC-as-μ assignment; the Axis-2 artifact is hash-pinned for provenance
only and its `out` block is never dereferenced; no pre-repair log is
read. The scanner carries its own teeth-control.

## 1. AUTHORITY TABLE — eight entries, **zero** supply a numerical μ

| file | section | status | predates Axis-2 | supplies numerical μ | independent of spectral outcome |
|---|---|---|---|---|---|
| `WALL_A_A3_DECLARATIONS.md` | Decl. 1 / F2 (renormalisation condition) | frozen | yes | **no** | yes |
| `WALL_A_A3_DECLARATIONS.md` | Decl. 1 / F1 (local predicate) | frozen | yes | **no** | yes |
| `WALL_A_A3_DECLARATIONS.md` | Decl. 1b (counterterm basis) | frozen | yes | **no** | yes |
| `WALL_A_A3_DECLARATIONS_V4_AMENDMENT.md` | local-predicate restatement | frozen | yes | **no** (repeated mention, not an independent convention) | yes |
| `K_R_OWNER_CHARTER.md` | §3 probe-coupling normalization | frozen | yes | **no** (fixes the *amplitude* chain, not a renormalization point) | yes |
| `K_R_CONTRACT_EXECUTION_CHARTER.md` | STEP 10 | frozen | yes | **no** (and *blocks* importing any matter-scope scale) | yes |
| `wall_j_omega_comparison.py` | `chi_A` evaluation slice (`muS: 1`) | frozen instrument, **matter scope, comparator-side** | yes | **no** — an evaluation slice; STEP 10 bars parameter transfer | yes |
| `wall_a_g1_ohmic_plant.py` | `WC = 1.0` | **BARRED INPUT** | yes | **no** — using it is the registry's forbidden direction | **NO — it is the comparator** |

Repeated mentions of μ were **not** counted as independent conventions.

## 2. THREE DIFFERENT THINGS, SEPARATED AND DEMONSTRATED

- **(A) Dimensional units.** Executable: the kernel is exactly degree-4
  homogeneous under the *joint* rescaling (ω, μ) → (λω, λμ), so
  **[μ] = [ω] = frequency**. This identity holds for **every** numerical
  μ — therefore it **cannot select one**.
- **(B) Renormalization prescription.** The frozen record fixes the
  subtraction completely (pole-only MS, zero finite discretion) *while
  keeping μ symbolic*. A prescription that is **complete without a
  numerical scale** — so (B) does not imply (C).
- **(C) Numerical identification of μ with a physical scale.** **Absent
  from the record**, and not implied by (A) or (B).

## 3. CAN μ BE REMOVED INSTEAD? — **YES, and this is the finding**

Derived from the existing formalism (no RG equations invented, no new
running computed): changing the renormalization point μ → μ′ requires
c4 → c4 + A·log(μ²/μ′²), a shift that is **ω-independent** — the (μ, c4)
pair is redundant by exactly one function's worth. Hence the invariant

    Lambda_R = mu * exp( c4 / (2A) )     — RG-invariant (gated)

and the entire H⁰ real kernel collapses to

    Re Sigma^{H0}(omega) = 2 A omega^4 log( Lambda_R / omega )

**One dimensionful constant, not two.** A negative control confirms the
invariance breaks under a perturbed shift, so the gate is not a
tautology.

**Consequence for the decision:** "declare μ" and "declare Λ_R" are the
*same single new input* in different clothes. Option 2 therefore has a
cleaner exact form — report the one RG-invariant constant and leave
**it** undetermined — which makes explicit that exactly **one** number
is in question and that no loop calculation at this order can supply it.
(Λ_R/μ is a pure number recorded in the Axis-2 artifact; it is
deliberately **not** reproduced here, since interpreting it is Axis-2
content.)

## 4. OWNER DECISION TREE

- **BRANCH A** — a pre-existing registered convention fixes numerical μ:
  **NOT SUPPORTED** (zero authorities supply one).
- **BRANCH B** — multiple admissible pre-existing conventions; owner
  selects: **NOT SUPPORTED** (zero, not several).
- **BRANCH C** — no pre-existing convention fixes μ, so a numerical μ is
  a genuinely **NEW declared input**: **SUPPORTED** by the authority
  sweep. No authoritative contrary evidence was found.

## 5. OWNER ACTION REQUIRED (the builder does not choose)

**EITHER**
1. **formally introduce a new numerical renormalization-scale
   convention** — equivalently, declare Λ_R — with provenance and
   **independent** justification, priced as a new register input;

**OR**
2. **leave μ symbolic** (equivalently, leave Λ_R undetermined) and
   accept Axis-2 as μ-parametric / indeterminate.

## 6. IMPACT MAP

**Blocked by μ:** the Axis-2 *absolute* classification (the sign
structure on the registered window); the consequence-cell adjudication
that depends on Axis 2; any claim requiring a unique real-axis sign
structure.

**Settled independently of μ:** the H⁰ absorptive coefficient
Im Σ = −3ω⁴/(1280π); the branch-cut structure (branch point at ω = 0,
gapless two-graviton continuum); the nonlocal logarithmic coefficient
A = −3/(1280π²), equal to the 1/ε residue; H⁰ local **c0 = 0 and
c2 = 0** (exact, structural); the contract K_R nonlocal content; and
**Axis 1** (s-class and convergence), which reads only Im χ.

**Not overstated:** c4 is settled **given μ** — it is not a
μ-independent number. The μ-invariant content of the local sector is the
single constant Λ_R, which remains **undetermined**.

## DEFECT HISTORY (gate-side, disclosed)

Three reds across two runs, all in the instrument's own self-checks: the
token-scan control planted the very literal it forbids (caught by the
scan itself, now built from runtime fragments); the RG-invariance gates
needed positivity assumptions before sympy would combine the logs; and
the scan's own descriptive prose tripped the strict token list — the
**prose was reworded rather than the list weakened**.

## CONCLUSION

**CURRENT μ RULING: C**
**MEANING:** No pre-existing numerical convention was found. A numerical
μ would be a new declared input.
**OWNER ACTION REQUIRED:** Choose whether to introduce such a new
convention independently of Axis-2, or retain μ symbolic.
**AXIS-2: C / unchanged.**
