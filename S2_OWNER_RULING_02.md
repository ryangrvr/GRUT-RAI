# S2 — OWNER RULING 02 (S2-1 RUN VOID stands; one corrective execution authorized)

**Date:** 2026-09-30 · **Recorded by the owner on Issue #2, comment `5908791267`**, after review of
`227dd09` (charter), `32645cc` (verified derivation), `e92cf29` (pre-run script) and `81b4f8f` (the
preserved void artifact and verdict). The comment is authoritative; this file records it.

## 1. The first execution stays RUN VOID

- No physics terminal comes from it, and the partial artifact is **not** retroactively converted.
- **Option 2 is NOT adopted.** Waiving I-5/E-2 after seeing favourable I-1 … I-4 outputs would weaken
  the pre-registered gate post hoc.
- The verified derivation is real evidence, but it does not authorize bypassing a frozen execution
  control.

## 2. The defect is isolated and non-physics

- **No silent repair occurred:** the script at `e92cf29` is byte-identical to the one at `81b4f8f`
  (blob `81805ec…`).
- **Cause:** `sp.nsimplify` was applied to exact values. It rewrote 8 report-only Δ₄ entries as
  radical expressions, and the report block's parse then failed before E-2.
- **Unaffected:** the parent, the Dynkin operator, the coefficient formulas, HT-B, the members and
  the terminal mapping.

## 3. HT-B is accepted as the theorem basis for the corrective run

- **Step A** forces 𝔼ξ₁² = 0 (in the extended reals), hence ξ₁ = 0 a.s., without presupposing a
  second moment.
- **Step B:** coming down from infinity controls the bath amplitude; the uniform bound |e| ≤ Ct² and
  the pointwise e = o(t²) give 𝔼e = o(t²) for arbitrary ν by dominated convergence. The stochastic
  side instead carries −24βT₁a·t².
- **HT-B closes at the recorded analytic scope for T₁ > 0.**
- **This does not assign the terminal.** The frozen execution controls must still pass.

## 4. ONE CORRECTIVE S2-1 EXECUTION is authorized

- It runs under the **same charter `227dd09`** and the **same derivation `32645cc`**.
- It replaces the voided run. It is not a new campaign.
- The v4 exception is extended solely to this corrective execution.

## 5. Patch firewall

**Sequence:**
1. Preserve `e92cf29` and `81b4f8f` unchanged.
2. Patch the script.
3. Commit it.
4. Execute once.

**Allowed:** remove `sp.nsimplify` wherever the operands are already exact rationals:
- in the member-instantiation list, keep the exact substituted value;
- in the F − GR report arithmetic, subtract the exact rationals directly.

Making all exact-rational/report paths consistently free of `nsimplify` is acceptable.

**Forbidden changes:**
- K; the β, a or profile sets; n_max;
- A, D, 𝓛 or Δ_n;
- any I-1 … I-5 predicate;
- the E-2 algebra or the HT-B identities;
- terminal ordering;
- exception handling that hides failures;
- **any new simplification heuristic.**

*Make exact arithmetic more literal, not more permissive.*

**Required pre-run provenance:** `S2_RUN_VOID_CORRECTION_01.md`, containing:
- the original script commit and the void result commit;
- the exact cause and the exact patch diff;
- a statement that the charter and derivation are unchanged;
- this authorization.

## 6. Corrective-run rules

- **Execute the entire frozen instrument from the beginning**, not a resume at E-2. The valid result
  must come from one complete artifact.
- **No output of the previous run may be copied.** The new result must produce, by itself:
  - E-3 and E-1;
  - every member instantiation;
  - I-1 … I-4;
  - the report-only Δ₄ fields;
  - E-2 / I-5;
  - the final `all_checks_pass`.
- No RNG, no simulation, and no extra symbolic theorem search after the patch.
- **Another implementation defect ⇒ stop again. NO THIRD EXECUTION WITHOUT A NEW OWNER RULING.**

## 7. The terminal after the corrective run

- Apply the frozen mapping mechanically.
  - If I-1 … I-5 pass, the finite-moment M2 algebra passes, HT-B stands and no counterexample exists,
    the result is **FULL-DISCRIMINATOR-CONFIRMED.**
  - A coefficient or control failure with no implementation defect goes to the refutation branch.
  - An implementation defect gives RUN VOID.
- **Do not pre-write the terminal.**

## 8. Scope if FULL-DISCRIMINATOR-CONFIRMED lands

The strongest allowed statement:

> **Within the declared nonlinear C-B class, ongoing stochastic forcing is observationally
> distinguishable in the retained mean-response map from uncertainty confined to the initial
> condition on the same deterministic state space.**

It would establish the failure of the S-1 initial-uncertainty equivalence in this class. It would
not establish:
- ontological randomness;
- that an enlarged Hamiltonian bath cannot reproduce the reduced process;
- quantum outcomes or Born probabilities;
- that the L0-1c drift is derived.

**Mechanism:** noise-generated spread + drift curvature → mean-response structure.

## 9. HARD STOP after the corrective verdict

- Commit the new result and verdict, preserve the RUN VOID record, and update CURRENT_STATE.
- **Not opened automatically:**
  - a Hamiltonian-bath follow-up;
  - S-3, the reversal diagnostic, S-6;
  - S5-WB or S5-OD;
  - gravity, Π₀ or cosmology.
