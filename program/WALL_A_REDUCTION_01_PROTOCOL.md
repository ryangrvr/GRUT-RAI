# WALL_A_REDUCTION_01 — PROTOCOL (frozen before execution)

**Charter.** The wall-A closure (`OWNER_ADJUDICATION_WALL_A_CLOSURE.md`, 2026-08-30)
ends in a HARD STOP: *"No further scientific computation is authorized until a new
owner charter explicitly names the next question."* The owner's 2026-09-16 message names
it: *"Are we actually looking at one physical kernel represented in two ways, or two
different kernels?"* — *"I would let Wall-A tell us whether Candidate 6 is actually
connected to the physics we've been calculating."* — ranked ahead of the smooth-window
test. This protocol executes THAT question only; the HARD STOP's other fences (no K_R
build, no Ward repair, no Q1/Q3/Q4/Q5 alteration, no reinterpretation of s ≥ 2) stay in
force. Nothing banked; register untouched.

**The question, made computable.** Two objects are on the record:
- **O_flat** — the fired flat-slicing k_ext = 0 one-loop kernel (Tier-3, BD bath over the
  whole comoving slice; internal legs on the q-continuum; fork (ii) fired at O(H²):
  q⁻¹ and q⁻² poles from both internal legs going superhorizon together).
- **O_static** — the static-patch (ω_T, l, m) multipole object (calc/static_patch_tt_response.py;
  U3: ρ_l ~ ω_T² for l ≥ 1, IR-finite; internal modes on the discrete Killing tower
  n ≥ l+1, no q → 0 continuum; state = BD restricted = thermal at T_dS).
U2 exhibited the kinematic identity bridge on the k = 0 / l = 2 sector (ω_T = ω_cosmic; a
constant traceless h_ij(t) is l = 2). **If that sector identity holds, the two objects
cannot differ by their external label — so either the loop-level objects differ in
their INTERNAL construction (the bath), or in the LOCUS of the external projection
(slice-wide k = 0 exactly vs. horizon-localized l = 2), or the identity fails at loop
level.** The reduction question is which.

## Pre-registered outcomes

- **ROUTE-A / ONE-KERNEL** — O_static is a projection of the same kernel as O_flat, and the
  IR divergence of O_flat is a property of the *slice-wide, exactly-k = 0 external
  projection*, not of the kernel: a horizon-localized external test function (physical
  size R < 1/H) applied to the SAME flat-slicing loop gives a finite, O_static-matching
  result. Consequence: the fired fork is a statement about an observable no apparatus
  realizes (U1's judgment, now derived), and lim_{k_ext → 0} ≠ value-at-k_ext = 0 — a
  limit-locus result about a specified object (O, D, L, R), with no "zero" vocabulary.
- **ROUTE-B / TWO-KERNELS** — the objects differ at loop level in their internal
  construction: the static tower's discreteness IS an IR completion (chart restriction +
  thermal state), i.e. O_static silently carries a completion of the kind S6 says the
  dynamics does not fix. Consequence: candidate 6's finiteness cannot be imported; the
  choice static-vs-flat is itself the fork, relocated.
- **IDENTITY-FAILS** — the k = 0 / l = 2 sector identity does not survive the loop
  (e.g. the assembled object is not ξ-covariant at O(H²) because the fork fired, so
  neither projection is well-defined without the completion). Consequence: the
  reduction is blocked BY the fork; wall-A cannot run ahead of U3's open input.
- **UNDERDETERMINED** — with the precise computation named.

## The computations (deriver; run, not asserted)

1. **Sector identity at loop level (H⁰, H¹):** where the object is clean, show whether the
   flat k_ext = 0 TT kernel and the static l = 2 kernel agree as functions of the common
   frequency (ω_T = ω_cosmic on the sector), using the frozen Tier-3 integrand cache
   (read-only) and the static calc's master equation. Agreement/disagreement with the
   computation exhibited.
2. **Locus test at O(H²):** take the frozen O(H²) integrand at k_ext ≠ 0 small (if the
   cache is k_ext = 0 only, derive the k_ext-dependence of the two-internal-leg
   superhorizon region from the Tier-2 BD modes — one leg carrying k_ext): does the
   q⁻¹ / q⁻² divergence require k_ext = 0 EXACTLY, or persist for k_ext ≠ 0? Then apply a
   horizon-localized l = 2 external test function (physical width R < 1/H at both times)
   to the flat-slicing loop and compute whether the result is finite.
3. **Static internal-leg check:** is the static tower loop (internal modes n ≥ l+1) equal
   to the BD-continuum loop restricted to the patch for a patch-localized operator (same
   state, same operator ⇒ must agree), or does the tower's discreteness remove weight
   the continuum has? Exhibit the comparison on the sector.
4. **(O, D, L, R) statement:** for the fired divergence, state explicitly O (which
   kernel), D (which chart/slice), L (which limit/locus — k_ext = 0 exactly vs
   k_ext → 0), R (which equivalence — projection equivalence under localized test
   functions). Noncommuting limits ⇏ sectorization: only a projection-invariant
   distinction counts.

## Anti-optimization

ROUTE-A is the framework-favorable direction (it dissolves the IR fork into a
projection artifact) AND the direction the owner's speculation would welcome — named
trap. ROUTE-B is deflation-comfortable. IDENTITY-FAILS is the "blocked, nothing to do"
comfort. None preferred; the adversarial checker attacks whichever the deriver reaches,
hardest in the framework-favorable direction, and must independently re-run computation 2.

## Fences

Zero register/tier/edge edits; frozen artifacts read-only (scratch only); no K_R
construction; rung3's tier untouched; AMBER keystone evidence-only; the fork stays
gated regardless of outcome. Lean: surveyor (what the two objects ARE, on the record) →
deriver → adversarial checker → resolver on disagreement.

*Frozen 2026-09-16 before any agent ran.*
