# Π₀ ROUTE — CORRECTION 01 (provenance / bookkeeping only; no new physics)

- **Authority:** `PI0_TRACE_CHANNEL_OWNER_RULING_01.md` §§2, 6 (Issue #2 comment `5902971222`).
- **House rule:** create a correction artifact rather than silently changing the old record.
- **Historical documents stay intact.** They point here; their old decision trees are not rewritten.

## What is corrected

**1. `x = f(Π₀/Π₂)` was never instantiated.** The phrase appears as though it were an existing map
at:
- `X_FLOOR_MAP.md:29` ("the banked x = f(Π₀/Π₂) map");
- `X_FLOOR_MAP.md:47` ("convention-level bookkeeping, ledger 0, explicitly NOT R1 closure");
- `X_FLOOR_MAP.md:70`.

**No explicit Π₀/Π₂ → x formula was ever written or executed anywhere in the record.** The
adjective "banked" at `X_FLOOR_MAP.md:29` is unsupported. Π₂ is never defined independently.

**2. `S_IF.md`'s x is a different, later definition.** It defines
x(ω, k²) := c₀(ω, k²) / c₀^{trace-only}(ω, k²), with x = 1 ≡ trace-only and x = 0 ≡ pure-TT
(`S_IF.md:81-84`), declared "A KERNEL, NOT A CONSTANT" (`:90`). That is useful. But it is **not**
the never-written Π₀/Π₂ formula, and it **does not yet** earn a bridge from a computed dS J = 0
spectral weight (Π₀) to the cosmological constant-x family.

**3. What remains missing (upstream), per the owner's revised A-4:**
- an explicit, justified **Π₀ → x** normalization, i.e. how a computed gauge-invariant scalar
  response is normalized to the declared trace-only endpoint / scalar modulus;
- if μ/Σ is consumed, **the inherited one-sided scalar-bookkeeping assumption** (η = 1/μ postulated
  from one-sidedness; `calc/RESULTS_mu_slip_interior.md:13`) must travel with the result.

**4. α is NOT the missing map. Operator overstatement withdrawn.**
`PI0_TRACE_CHANNEL_REOPEN_01.md` §6 and blocker A-4 said a computed Π₀ "would not yield a pinned
μ/Σ without an α-free, audited x → (μ, Σ) map". **That is struck.**
- μ(x) = 1 + xα, η(x) = 1/(1+xα) and Σ(x) = 1 + xα/2 are defined at the inherited-bookkeeping level
  (`GRUT_II_What_Survived.md:47`).
- α = 1/3 is carried by `calc/mu_linear.py` as an existing **conditional/supplied** input.
- D2b was already conditional-theorem grade.

> With a physically normalized x independently derived, the existing supplied α would permit a
> **conditional** μ/Σ prediction. α's presence prevents calling it parameter-free or
> Level-0-derived; it does not prevent prediction. **No "α-free map" is required.**

## Corrected A-4 (governs `PI0_TRACE_CHANNEL_REOPEN_01.md` §0 and §6)

> **A-4 — NORMALIZATION/MAP MISSING:** the record never supplied the explicit Π0 → x map needed to
> turn a trace-channel calculation into the inherited cosmological scalar modulus. α is an existing
> conditional input downstream, not the missing map.

## Corrected A-1 wording (governs `PI0_TRACE_CHANNEL_REOPEN_01.md` §0 and §4)

> The renormalization **doctrine** is fixed: no downstream outcome may choose a finite part. The
> **regulator/scheme completion** remains unresolved and needs a ruling/realization. This is
> **not** unrestricted scheme freedom.

## Pointers (additive; the historical files are unchanged)

The following files carry the claims corrected here. Their readers should consult this file:
- `X_FLOOR_MAP.md` (:29, :47, :70);
- `PREDICTION_UNIQUENESS_MAP_01.md` (:37, :63, :177, :188, the "percent-level μ/Σ via Π₀" route
  statements);
- `GRUT_II_What_Survived.md` (:10, :89);
- `PI0_TRACE_CHANNEL_REOPEN_01.md` (§0 A-1 and A-4, §4, §6). This file carries a banner pointing
  here.
