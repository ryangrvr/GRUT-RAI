# S2-1 — RUN VOID CORRECTION 01 (pre-run provenance for the one corrective execution)

**Authority:** `S2_OWNER_RULING_02.md` (Issue #2 comment `5908791267`). One corrective S2-1 execution
is authorized under the unchanged charter and derivation.

| Item | Value |
|---|---|
| Frozen charter (**unchanged**) | `S2_NOISE_ORIGIN_CHARTER_01.md` at `227dd09` |
| Verified derivation (**unchanged**) | `S2_NOISE_ORIGIN_DERIVATION_01.md` at `32645cc` |
| Original script (**preserved**) | `calc/s2_noise_origin.py` at `e92cf29` (blob `81805ec`) |
| Void result (**preserved, not overwritten**) | `S2_NOISE_ORIGIN_RESULT.json` and `S2_NOISE_ORIGIN_VERDICT_01.md` at `81b4f8f` |

## The exact cause

- `sp.nsimplify` was applied to values that were already exact sympy `Rational`s.
- For 8 of the 540 stored values (report-only Δ₄), it returned non-exact radical expressions.
- The report block's `sp.Rational(...)` parse of one of them raised `TypeError`, before E-2 ran.
- So I-5 could not complete, and the run was RUN VOID.

## The patch (the only changes; the exact diff follows)

**1. Three `sp.nsimplify` calls removed**, all on already-exact rationals (ruling §5, "allowed"):
- the member-instantiation list, which now keeps the exact substituted value;
- the two F − GR(∞) report subtractions, which now subtract exact rationals directly.

No replacement simplification heuristic was added.

**2. Output path redirected** to `S2_NOISE_ORIGIN_RESULT_CORRECTIVE_01.json`, together with the docstring
"Usage" line.
- **This is provenance-only.** Without it, the corrective run would overwrite the preserved void artifact
  `S2_NOISE_ORIGIN_RESULT.json`, and the ruling (§5.1) requires that artifact to stay unchanged.
- It has no effect on any computation, predicate or check.

**Unchanged:**
- K; the β, a and profile sets; n_max;
- A, D, 𝓛 and Δ_n;
- the I-1 … I-5 predicates;
- the E-2 algebra and the HT-B identities;
- the exception handling (failures are still recorded in `defects` and set `all_checks_pass = false`);
- the terminal ordering.

```diff
diff --git a/calc/s2_noise_origin.py b/calc/s2_noise_origin.py
index 81805ec..73015a9 100644
--- a/calc/s2_noise_origin.py
+++ b/calc/s2_noise_origin.py
@@ -11,7 +11,7 @@ E-2  symbolic re-derivation of the finite-moment M2 coefficient algebra, and of
      and q - q0 identities used by HT-B.
 E-3  structural checks: K_b symmetric positive definite (exact Cholesky), off-diagonal <= 0, f odd.
 
-Usage: python3 calc/s2_noise_origin.py   (writes S2_NOISE_ORIGIN_RESULT.json)
+Usage: python3 calc/s2_noise_origin.py   (writes S2_NOISE_ORIGIN_RESULT_CORRECTIVE_01.json)
 """
 import hashlib
 import json
@@ -21,7 +21,7 @@ import traceback
 import sympy as sp
 
 ROOT = pathlib.Path(__file__).resolve().parent.parent
-OUT = ROOT / "S2_NOISE_ORIGIN_RESULT.json"
+OUT = ROOT / "S2_NOISE_ORIGIN_RESULT_CORRECTIVE_01.json"  # void artifact S2_NOISE_ORIGIN_RESULT.json preserved
 N = 23
 NMAX = 4
 R = {"charter_commit": "227dd09", "derivation_commit": "32645cc",
@@ -111,7 +111,7 @@ try:
         sub_T = {Ts[i]: Tv[i] for i in range(N)}
         for bv in BETAS:
             for av in AS:
-                vals = [sp.nsimplify(Delta[n].subs(sub_T).subs({b: bv, a: av})) for n in range(NMAX + 1)]
+                vals = [Delta[n].subs(sub_T).subs({b: bv, a: av}) for n in range(NMAX + 1)]
                 key = f"{pname}|beta={bv}|a={av}"
                 tab[key] = {f"Delta_{n}": str(vals[n]) for n in range(NMAX + 1)}
                 tab[key].update({f"t^{n}_coeff": str(vals[n] / sp.factorial(n)) for n in range(NMAX + 1)})
@@ -138,8 +138,8 @@ try:
             rep[f"beta={bv}|a={av}"] = {
                 "G(inf)_Delta_3": g["Delta_3"], "G(inf)_Delta_4": g["Delta_4"],
                 "G(inf)_first_nonzero_order<=4": first,
-                "F_minus_GR(inf)_Delta_3": str(sp.nsimplify(sp.Rational(fk["Delta_3"]) - sp.Rational(gk["Delta_3"]))),
-                "F_minus_GR(inf)_Delta_4": str(sp.nsimplify(sp.Rational(fk["Delta_4"]) - sp.Rational(gk["Delta_4"])))}
+                "F_minus_GR(inf)_Delta_3": str(sp.Rational(fk["Delta_3"]) - sp.Rational(gk["Delta_3"])),
+                "F_minus_GR(inf)_Delta_4": str(sp.Rational(fk["Delta_4"]) - sp.Rational(gk["Delta_4"]))}
     R["reported"] = rep
 
     # ---------------- E-2 symbolic M2 algebra and HT-B identities ----------------
```

## Run rules (ruling §6)

- The **entire** frozen instrument runs from the beginning (E-3, E-1, every member, I-1 … I-4, the
  report-only Δ₄ fields, E-2/I-5, and `all_checks_pass`), in **one** execution.
- Nothing is copied from the void run.
- No RNG and no simulation.
- **Another implementation defect ⇒ stop. No third execution without a new owner ruling.**
