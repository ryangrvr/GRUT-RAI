# S5-1 — CORRECTIONS 01 (additive provenance note; owner-ordered)

- **Authority:** `S5_OWNER_RULING_03.md` §6 (Issue #2 comment `5904495463`).
- **Handling:** the generated `S5_CONSERVATIVE_ORIGIN_RESULT.json` is **not rewritten.**
- **Scope:** this note clarifies how the JSON is to be read.

## SOC-1. What S-5 is

`symbolic["S-5 Scheffe pointwise limit"].ok = false` is a preserved supplementary **criterion
defect.** It is **not** a physics defect and not an implementation defect of the derivation.

- **What the criterion demanded:** a strictly decreasing sampled deviation at every x ∈ {−3, −1, 0,
  0.5, 2} across g ∈ {1e-2, 1e-3, 1e-4}.
- **Why that was impossible at x = 0:** there the scaled exact density equals the Cauchy target
  **for every g**, g²ρ̃_g(ω_s) = 2ω_s/π = 1/(πκ). The recorded deviation is identically 1.1e-41 at
  working precision.
- **What passes:** the substantive content. `sympy_limit_matches: true`, and the deviations at
  nonzero x fall as O(g²) (for example 2.3e-5 → 2.3e-7 → 2.3e-9 at x = 0.5).

## SOC-2. What the JSON `"defects": []` field means

- In `calc/s5_conservative_origin.py`, `R["defects"]` collects **exceptions raised in the frozen
  X-1…X-5 cross-check block.**
- `"defects": []` therefore means **"no X-block execution exception."**
- It does **not** mean "every supplementary symbolic predicate passed." Each symbolic predicate
  carries its own `ok` field.

## SOC-3. Independence of the terminal

- The S5-1 terminal (MARKOV-LIMIT-OTHER-CLASS) is **analytic.** It rests on
  `S5_CONSERVATIVE_ORIGIN_DERIVATION_01.md`, committed at `6170129` before any check.
- It is independent of S-5 and of the finite-window X-5.
- The weak-coupling statement rests on the Scheffé L¹ convergence, which controls the Fourier
  transforms uniformly in time (ruling S5-03 §4).
