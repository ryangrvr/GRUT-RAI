# WALL-D2 PHASE-11 TOY FUNCTIONAL-HESSIAN CALIBRATION -- VERDICT (W-0, computed-and-reported)

Instrument: `PHYSICS_LEDGER/wall_d2_phase11_toy_hessian.py` (standalone; no import of, and
no edit to, any existing file).  Date: 2026-08-27.  Exit code: 0.  FAIL count: 0.

## VERDICT: GREEN

The nine-step protocol ran on the owner-specified toy
`S[h] = 1/2 Int du C(u) (h'(u))^2,  C(u) = 1 + c1 u + c2 u^2`,
with the registered Phase-11 conventions mirrored verbatim in form from
`wall_d2_phases8_12.py` (FT `Sigma_tilde(om) = Int dDelta e^(+i om Delta) Sigma(Delta)`,
`apply_Delta_power = (-i d/dom)^n`, `E_transform`, `u1_pow`/`u2_pow` lever arms).
ALL checks passed.

## Pinned conventions (each backed by the checks in the JSON artifact)

1. **Coefficient placement.** The exact Hessian carries the dressing on the DIFFERENTIATED
   vertex with a locked sign pairing: u2-order `C'(uc-Dl/2) dd' - C(uc-Dl/2) dd''`,
   u1-order `-C'(uc+Dl/2) dd' - C(uc+Dl/2) dd''`. Placement and derivative-order pairing
   are NOT independent: the wrong-vertex hybrid (control D) breaks kernel symmetry and
   every check.
2. **(u_c, Delta) transform.** `u1 = uc + Dl/2, u2 = uc - Dl/2`;
   `d/du2 = 1/2 d/duc - d/dDl`, `d/du1 = 1/2 d/duc + d/dDl` (control A pins the signs).
3. **r-slot convention.** `C(uc +- Dl/2) = sum_r C^(r)(uc) (+-1/2)^r / r! Dl^r` -- the
   registered `u1_pow`/`u2_pow` lever arms at general centre (also exercised directly at
   uc = 0); Taylor terminates at r = 2 (control B pins the 1/2).
4. **Dl^r dd^(q) reduction.** `Dl^r dd^(q) = (-1)^r q!/(q-r)! dd^(q-r)` (r <= q), `0`
   (r > q); verified against delta-action on generic test functions and per-slot
   consistent with the registered E_transform.
5. **FT signs.** `E_transform(p,q) == <Dl^p dd^(q), e^(+i om Dl)>` per term; the conjugate
   action differs on every odd (p,q) (control E). A summed-level global flip is degenerate
   for THIS toy (the exact kernel is distributionally even in Dl) -- disclosed; the pin is
   at the per-term granularity at which engines 4-5 actually apply the rule.

## Computed exact results

- `K_tilde(uc,om) = om^2 C(uc) + (1/4) C''(uc) = c1*om**2*uc + c2*om**2*uc**2 + c2/2 + om**2`
- At the reference `uc = 0`: `K_tilde = c2/2 + om**2`
- Reduced kernel: `-C(uc) dd''(Dl) + (1/4) C''(uc) dd(Dl)` (manifestly centre-symmetric;
  both differentiation orders agree exactly after reduction).
- Plane-wave matrix element (both constructions, exact):
  `2 pi {(S^2/4 + c2/2) dd(Q) - i (c1 S^2/4) dd'(Q) - (c2 S^2/4) dd''(Q)}`.
- **Toy master identity:** `F_B - F_A = (1/4) C''(uc) = c2/2` -- additive, om-independent,
  and structurally ABSENT when `C'' = 0` (the order theorem: flat/linear dressings are
  centre-blind; the defect first bites at `C'' ~ H^2`).

## Controls

| control | required | outcome |
|---|---|---|
| A wrong d/dDl sign in the chain rule | FAIL | detected |
| B lever arm 1 instead of 1/2 | FAIL | detected |
| C frozen-centre shortcut (Route A) | FAIL | detected |
| C' freeze-at-centre variant | FAIL | detected |
| D wrong-vertex coefficient placement | FAIL | detected |
| E conjugate FT sign | FAIL | detected per-term (odd (p,q)); summed-level global flip degenerate for this toy (exact kernel even in Dl) |
| flat C = 1 | PASS | PASS (reduces exactly to -dd'' -> om^2; frozen shortcut exact at C''=0) |

## Scoped notes (no interpretation)

- Normalization correspondence, flagged for the owner: the 2026-08-27 centre-mismatch
  diagnostic reported an OP1 (`c (phi')^2`) discrepancy of `p(p+1)/2 H^2 = (1/2)c''(0)`;
  this toy's exact coefficient with the explicit `1/2` in the action is `(1/4)C''`. The two
  agree iff that instrument's OP1 kernel was normalised without the `1/2`. The rebuild must
  carry this normalization table explicitly.
- The 96/300 H^2 residual remains COMPUTED AND UNINTERPRETED. No basis change, no refit,
  no operator addition, no register edits, nothing banked.

## Next (only if GREEN, per the stop directive)

Generalise the SAME nine-step algorithm to the four frozen operators as an action-functional
(IBP-invariant, F_B-type) instrument; then re-run `wall_d2_span_test.py` UNCHANGED. The
owner-adjudication gate from the 2026-08-27 ruling stands.
