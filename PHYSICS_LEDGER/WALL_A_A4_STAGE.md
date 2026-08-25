# WALL A, STAGE A4 — the dual-gauge check: RESULT

**Date:** 2026-08-25 · **Instrument:** `wall_a_a4_dual_gauge.py` (exit 0, all 11 gates PASS) ·
**Standing state:** `8347ac8` (A3 FROZEN, checker-amended F1–F7) ·
**W-0:** COMPUTED-AND-REPORTED, NOT BANKED. No register edits.

**BUILDER DISCLOSURE:** built by the **checker** (Claude) under the standing
build-and-disclose arrangement, on the owner's directive ("finish A4, assemble the loop"),
while the usual builder (Ox) was stalled. The second-author burden therefore flips: the
independent verification below is the load-bearing review, and the Ox countersign slot
remains OPEN.

## What A4 establishes

The synchronous-gauge computation reproduces the gauge-invariant content of the
gauge-UNFIXED computation (A1's full untruncated h), per the frozen Declaration 5.
Four computed facts:

1. **The slice equality** (honest framing: confirmation, not discovery — L1 is linear in
   h, so the h_ij coefficients cannot depend on the removed components): the synchronous
   vertex from the sliced expansion equals the countersigned A1 vertex's ij-block,
   componentwise at general (a, m, p, q).
2. **The transformation to synchronous exists.** Setting h₀₀ + δh₀₀ = 0 gives the ODE
   (aζ⁰)′ = −(a/2)h₀₀, whose general solution is
   ζ⁰ = −(1/2a)∫a h₀₀ dη′ + **C(x)/a**. ~~its residual is EXACTLY the frozen F3
   structure {C(x)/a} × {time-independent Cᵢ(x)} — re-derived, not assumed~~
   **STRUCK-AND-REPLACED after fleet refutation**: the first version of this instrument
   *hard-coded* the ζᵢ conjunct (a print-statement fact — the defect class this program
   hunts, this time in the checker's own code), and the computation it skipped refutes
   the product family: preserving h₀ᵢ = 0 with ζ⁰ = C/a **forces**
   ζᵢ = Cᵢ(x) − (∂ᵢC)·Ia(η), Ia′ = 1/a — a mandatory time-dependent piece coupled to C.
   Corrected by substitution with a negative control (the product family demonstrably
   exits the gauge: δh₀ᵢ = (∂ᵢC)/a ≠ 0); the frozen F3 clause is superseded by
   `WALL_A_A3_DECLARATIONS_V2_AMENDMENT.md`. The parameter count and the asymptotic
   fixing prescription are unchanged — the prescription kills the entire C-sector and
   fixes Cᵢ, so the post-prescription statement stands.
3. **The invariance identity, from first principles:**
   L1(δ_ζh) = E·(ζ·∂φ) − ∂_mV^m identically in (φ, ζ, a(η)), with E the Euler–Lagrange
   expression of L0 (derived in-instrument, equal to
   a²[φ″ + 2(a′/a)φ′ − ∇²φ + a²m²φ] — friction included) and
   V^m = a²(∂^mφ)(ζ·∂φ) − ζ^m L0 from the transport bookkeeping. Hence the two gauge
   computations differ by pure bath-EoM plus a total derivative — the gauge-invariant
   content cannot differ. The **constant-H trap** exhibited as a plant: dropping the
   2(a′/a)ζ⁰ orbit term breaks the identity.
4. **TT blindness:** the spatial-TT projection of the orbit direction vanishes for
   arbitrary (ζ, a′/a, k) — the countersigned δh^TT = 0 instantiated — while a generic
   non-orbit probe survives projection (non-vacuity plant). The TT coupling is identical
   in the two gauges.

## The frozen guard's first live exercise

STEP 0 ran the barred-inputs guard as frozen: registry loaded and echoed verbatim,
transitive import scan (sys.modules), file reads scanned by name AND content hash,
own-source symbol scan. **GUARD CLEAN** — and its output is in the instrument's stdout,
verbatim, as the frozen protocol requires.

## Plants (all detected, both directions)

- Flat limit a→1 reproduces the independently typed flat synchronous vertex (T^{ij}).
- Wrong-a variant (a⁴ on the kinetic channel) FAILS the comparison.
- Constant-H orbit (a′-term dropped) FAILS the invariance identity.
- Projector non-vacuity: a generic h₁₂ probe survives the TT projection.

## Honest boundary

- A4 establishes the vertex-level dual-gauge consistency and unblocks Σ_R^TT assembly
  under the frozen protocol. The **response-level** dual-gauge check — exact symbolic
  equality of Π_nonlocal^invariant between gauges — re-runs at assembly per the frozen
  Declaration 5; A4 does not discharge it.
- Nothing here touches the wall questions (i)/(ii)/(iii); no spectral quantity was
  computed; the registered J(ω) was never reachable (guard-enforced).

## OX COUNTERSIGN (2026-08-25, appended at the open slot)

**Verdict: COUNTERSIGNED — with scope stated.** I independently executed the disk
instrument fresh (REAL_EXIT=0; all 11 gates true; guard live-clean: registry echoed,
12 barred files content-hash-verified, `MICROSCOPIC_TARGET_BENCHMARK.md` barred and
unread, no barred symbol reached the run).

**Independent verification basis** — before discovering the supersession, my own
diverged A4 build (same countersigned A1 objects, independent code) had already
verified the central comparison claims; those results stand and are consistent with
this instrument's gates:

- synchronous derivation: structural match on the sliced expansion; flat-limit plant PASS;
- **Γ^TT exact equality** between the synchronous and unfixed vertices at general (a, m, p, q);
- the unfixed-minus-synchronous difference is **pure discard-sector** (zero TT projection;
  k^iD_ij ∝ k_j — no transverse-vector content);
- conformal-orbit reconciliation with **H = a′/a symbolic** (constant-H trap structurally excluded);
- wrong-a plant detected; barred guard clean.

**Findings from my build that carry into the record** (verified numerically, exact
rational arithmetic):

1. **3D STF coefficient is ½, not ⅓.** In the spatial slice tr θ = 2 (not the 4D layer's
   3), so the spatial STF projector is ½(θθ-sym) − ½θ⊗θ, and the θ-trace scalar
   reconstruction coefficient is ½. A 4D-value ⅓ imported into the spatial slice produces
   a nonzero recomposition residual (pinned by a random-rational-v decomposition test
   with per-piece orthogonality projections).
2. **The synchronous discard bookkeeping has THREE channels** — θ-trace scalar,
   ω-longitudinal scalar, and a genuine **transverse-vector** discard (from p^iq^j+q^ip^j)
   — and the recomposition Γ_syn = Γ^TT + (1/2)θT_θ + ωT_ω + (kV^⊥+V^⊥k)/k² closes
   exactly with all four (verified componentwise, exact rationals). The assembly stage's
   discard bookkeeping should carry all three non-TT channels.
3. **Guard self-reference defect** (fail-closed, harmless): a marker-string search that
   matched its own code literal voids the run rather than passing it — the correct
   conservative behaviour; noted for the assembly guard's implementation.

**Scope of this countersign:** fresh clean execution (all gates), plus my independent
re-derivation of the central comparison claims above, plus structural consistency of the
vertex form with my independently derived +δ^{ij} spatial-block identity. The full
line-by-line reading of the 20 KB instrument is NOT part of this countersign; the
assembly-stage reviewer inherits it as standing context.

**Σ_R^TT assembly: UNBLOCKED** under the frozen protocol, per Declaration 5 (the
response-level Π_nonlocal equality re-runs at assembly).

## FLEET VERIFICATION (second independent leg — landed after the countersign)

**Verifier 1 (transformation + invariance identity): REFUTED the residual-family claim,
CONFIRMED everything else.** The refutation and its fix are recorded in fact 2 above and
in the v2 amendment. Confirmed from scratch with independent symbol layout: the ζ⁰
solution (dsolve gives C/a as the *complete* homogeneous family); the full ζᵢ solution
integrates and satisfies the gauge condition identically; the invariance identity
L1(δ_ζh) = EL·(ζ·∂φ) − ∂_mV^m for arbitrary (φ, ζ, a(η)), with the sign conventions
pinned by an independent diffeomorphism-invariance derivation
(δ_φL0 + L1(δ_ζh) = ∂_m(ζ^m L0)); both negative controls — including a wrong-V^m
control the instrument had not run — break the identity correctly. **Scope of damage
stated by the verifier: steps 4–5 hold for arbitrary ζ, so the gauge-invariant-content
conclusion is unaffected; the post-prescription residual statement stands.**

**Verifier 2 (guard genuineness + slice/TT/plants): NOT REFUTED.** The guard is real,
not decorative: a modified copy importing the *actual* barred Ohmic-plant file (and a
stub of the same name) exits non-zero with the GUARD TRIPPED message; the unmodified
baseline runs clean and matches the repo result JSON (registry echoed, 12 barred files
content-hash-verified, 616 modules scanned).

**Checker cross-confirmation of the Ox countersign's finding 1**: in the spatial slice
tr θ = 2, the STF projector with coefficient ½ is exactly idempotent (0 violations) while
the imported 4D value ⅓ fails idempotence at 81/81 components — the assembly stage must
use the ½. Findings 2 (three non-TT discard channels in the spatial slice) and 3 (guard
fail-closed self-reference) carry into the assembly brief as standing context.

**The verification chain for this stage, in full**: checker built (disclosed); Ox
countersigned with scope stated; the fleet then refuted one of the checker's claims —
every layer catching the layer below, which is the apparatus working, not failing.
