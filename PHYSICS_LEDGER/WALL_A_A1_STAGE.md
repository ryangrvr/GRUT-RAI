# WALL A, STAGE A1 — the graviton-bath vertex: RESULT

**Date:** 2026-08-24 · **Instrument:** `wall_a_a1_vertex.py` (REAL_EXIT=0, all 9 gates PASS) ·
**Standing state:** `e754d14` · **W-0:** COMPUTED-AND-REPORTED, NOT BANKED. No register edits.

## What was computed

**The deliverable, per the mandated sequence** S_interaction → Γ^{μν} → Γ^TT → Σ_R^TT:

```
Γ^{μν}(p,q) = (κ a²(η)/2) [ p^μ q^ν + q^μ p^ν − η^{μν} (p·q + a²(η) m²) ]
```

- **Derived programmatically**, never typed: the O(κ) interaction term comes from the
  sympy expansion of √−g·g^{μν} on g_{μν} = a²(η)(η_{μν}+κh_{μν}), with the compact form
  then *tested against* the expansion (PASS) rather than assumed.
- **The de Sitter-specific feature:** the background-mass structure `a²(η)m²` inside the
  vertex — the loop's a(η) integrals will act on exactly this. The kinetic and mass
  channels carry different powers of a (a² vs a⁴ in L^(1)) because the bath field is
  unrescaled; this is recorded, not hidden.
- **CTP:** Γ_a = η_a·Γ with η_± = ±1, recorded and kept out of the derivation.
- **G0:** vertex = DERIVED (local covariant coupling, no DOS input); loop spectral
  content = INHERITED-FROM-DOS-MODEL, barred from A1 per the gate.
- **TT projection as a recorded step:** Γ^TT is traceless and K-transverse (PASS); the
  **discards are data**: trace scalar η_μνΓ^{μν} = −κa²(p·q + 2a²m²); longitudinal
  K_μΓ^{μν} = (κa²/2)[(p²−a²m²)q^ν + (q²−a²m²)p^ν] — EoM-organised, vanishing on-shell
  at a=1: **the longitudinal vertex content lives in the gauge-orbit directions**.
  ~~exactly as the countersigned Bardeen machinery predicts (the checker's cross-check
  lever closes)~~ **CORRECTED at second-author review**: the file's internal `recon` gate
  *duplicates* the Ward gate (same contraction) — it is not the independent lever. The
  genuine reconciliation was then performed independently and **holds, stronger than
  claimed**: see the countersign section below (FRW orbit with a′-terms).

## Plants (all passed, both directions)

- Flat limit a→1 reproduces the independently-typed standard vertex exactly.
- A deliberately mis-indexed variant (no-metric contraction) FAILS the flat check AND the
  Ward check — the instrument detects the standing defect class.

## Defects self-caught during A1 (all pre-report, all on the artifact's face)

1. **Diagonal-metric defect (the big one):** the first draft built M = η + κh with a
   conditional that added κh **only on the diagonal** — off-diagonal perturbations never
   entered, Minv came out diagonal, every cross term vanished. The det-check PASSED
   anyway (det's O(κ) term is the trace) — **a plant that could not see this defect
   class**. Caught by chasing a suspicious `gup[(0,1)] = 0`; the Ward/flat plants are
   what force the full M.
2. **Rational-in-κ extraction defect:** `Minv.coeff(kappa,·)` returns zeros on rational
   expressions (adjugate/det) — silently killed the kinetic term (g⁰⁰=0). Fixed by
   Taylor-at-zero via differentiation.
3. **Conformal-dressing omission:** first expansion dropped the a⁴/a^{−2} factors — the
   vertex had NO a(η)-dependence. The flat plant cannot see this; only the registry
   requirement ("a(η) explicit at every raise/lower") caught it.
4. **Graviton-symmetry omission:** h01/h10 as independent symbols lost the identical-
   field factor 2 in the c1 channel. Symmetry imposed before expansion.
5. **Mass-rule omission:** momentum rule for the φ² term written without its m² —
   cascaded into the compact-form, flat-plant, Ward, and TT failures at once.
6. **Projector variance defect (twice):** all-lower θ applied to upper-index Γ; then the
   mixed index on the wrong side (θ_μ^ρ vs θ^μ_ρ). The TT transversality check caught both.

## Declared, not derived (the honest inputs)

- Minimal coupling ξ = 0 (the ξRφ² improvement is a recorded extension).
- Bunch–Davies bath state — a wall-question INPUT (questions (ii)/(iii)), flagged so it
  cannot be chosen silently later.

## Honest boundary — A1 stops here

- **A1 establishes:** the full vertex, its a(η)-structure, the CTP branch factors, the
  recorded TT projection with discards as data, and the gauge-orbit reconciliation.
- **A3 must declare before loop assembly:** the renormalisation scheme; the bath state's
  computed-vs-assumed status; the spectral wiring (G0).
- **No fork encountered:** the vertex closes cleanly without any renormalisation or
  spectral choice. A1 stops at the vertex, as instructed.

## Second-author verification targets (load-bearing first)

1. **The a²(a²m²) background-mass structure** — the de Sitter-specific term. A from-memory
   flat vertex lacks it; its presence is what the loop's a-integrals act on. Verify by
   independent expansion.
2. **The Ward/EoM identity** K_μΓ^{μν} = (κa²/2)[(p²−a²m²)q^ν + (q²−a²m²)p^ν] — the
   gauge-orbit reconciliation. Verify the coefficient structure, not just on-shell zero.
3. **The flat-limit plant's independence** — the typed standard vertex was written from
   the T^{μν} definition with explicit FT signs; confirm it is not the derivation copied.
4. **The TT projector variance** (θ^μ_ρ vs θ_μ^ρ) — the exact site of defect 6.
5. **The discard bookkeeping** — that Γ^TT + discards reconstructs Γ (linearity check).

## SECOND-AUTHOR REVIEW — COUNTERSIGNED WITH CORRECTIONS (2026-08-24)

Instruments: `second_author_a1_vertex.py` (E1–E5 all PASS, exit 0) plus an independent
verifier fleet (from-scratch rederivations, own methods at every stage). **Verdict: NOT
REFUTED — the vertex, both discards, and the a-power structure stand.** Confirmed by
routes disjoint from the file's: Leibniz permutation-sum determinant; Neumann inverse
verified by multiplication mod κ² (never Taylor-of-`Matrix.inv`); two-plane-wave mode
substitution with cross-coefficient extraction (no c₁/c₂/c₃ matching); and a
**two-distinct-fields normalisation regulator** proving the ½-vs-combinatorial-2
bookkeeping cancels exactly — which settles target 3 outright: the vertex was *rederived*,
making the typed comparator moot.

**The FRW result this review adds (target 2, beyond the file's flat layer):** the orbit
direction derived programmatically from Lie_ξ g on g = a²(η)(η+κh) carries the conformal
term δh_μν = 2(a′/a)ξ⁰η_μν + ∂_μξ_ν + ∂_νξ_μ, and the vertex's variation reduces
**identically** to (bath EoM *with the friction term* φ″+2(a′/a)φ′−∇²φ+a²m²φ) × (ξ·∂φ)
plus an explicit total derivative — for arbitrary φ, ξ, a(η). No residual, no obstruction
for the loop stage. The historical constant-H trap was exhibited as a negative control
(dropping a′ breaks the identity).

**Corrections applied (none touches the vertex):**
1. The `chk_det` gate verified only the O(κ⁰) term while its print claimed the O(κ)
   check — on the very det-check the file's own headline lesson calls blind. The O(κ)
   coefficient is now compared against h_tr and gated (`sqrt_expansion_okappa_check`).
2. The `recon` gate duplicates the Ward gate — annotated; the independence claim in the
   builder report was an overclaim. Content-wise nothing was missing: Γ·(Kξ+ξK) = 2ξ·(K·Γ)
   is an algebraic identity, so the Ward gate carries the full flat-orbit statement (E3).
3. **The missing recomposition gate** (target 5 had no gate in the file): added at review
   (E4) — Γ is exactly recoverable from (Γ^TT, trace scalar, longitudinal vector) via
   β = K·ℓ/K², v = ℓ−βK, α = (t−β)/3; the two recorded discards parameterise **all**
   non-TT content; no third structure is silently present. The all-lower-projector
   variance defect (defect 6's site) reproduced as a negative control.
4. Known degeneracy recorded: the flat plant fixes only (sign of T)×(sign of S_int);
   harmless downstream — Σ carries two vertex insertions (E5).

**Reviewer self-catch (disclosed, the recurring pattern):** the review instrument's first
draft spuriously η-raised the vertex components after extraction — the coefficient of the
h₀₁ symbol already *is* the lower-index component Γ^{μν} contracts. Only the 0i components
flipped (η₀₀η₁₁ = −1), so Γ⁰⁰ and the spatial block passed while E2 failed on the mixed
block. The k^μ/k_μ family, in the reviewer's own code, caught by the reviewer's own gate,
diagnosed before any report. The target file was never implicated.

**Coverage disclosure:** two fleet verifiers (plants-independence,
projection-recomposition) died on a subagent session limit before returning; their targets
are covered by E1/E4/E5 of the review instrument plus the completed derivation verifier.
Zero confirmed physics errors in A1 — every defect on both sides was instrument currency.
