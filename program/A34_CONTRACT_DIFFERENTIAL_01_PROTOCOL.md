# A34_CONTRACT_DIFFERENTIAL_01 — PROTOCOL (frozen before execution)

**Owner charter (2026-09-16, verbatim scope):** *Compare the frozen A3-4 assembled TT
response with the frozen Tier-3 contract loop at O(H²), without modifying either
artifact and without constructing or repairing a new loop.* This comparison precedes any
Ward repair, which stays HARD-STOPped. The fork stays gated; Wall-A stays frozen history.

**The question:** does the finite, gauge/orbit-robust O(H²) TT response (A3-4) already
contain the same physical content as the divergent O(H²) contract loop (Tier-3), with the
divergence attributable specifically to the constant-TT sector Wall-A identified?

## The charter's ten conditions (binding)

1. Establish exactly what the object O is in EACH artifact — external projection,
   internal-leg operator, state, gauge status — as an explicit (O, D, L, R) tuple.
2. Put both into the same explicitly declared representation wherever legitimately
   possible.
3. Compute ΔO = O_contract − O_A3-4.
4. Determine whether the divergent part of ΔO is exactly the constant-TT mode
   h_ij^(0) = ε_ij = L_ζg, ζ^i = ε^i_j x^j/2 — **with the qualification PATCH-LOCAL gauge
   stated every time the word "gauge" is used** (ζ grows linearly; on the slice-wide
   k_ext = 0 locus it is a large diffeomorphism whose gauge/physical status is a
   boundary-condition question the corpus has not posed).
5. Separately determine whether any FINITE O(H²) difference remains after removing the
   identified sector.
6. Do NOT infer that the full loop is gauge invariant or IR finite.
7. Do NOT perform Ward repair.
8. Do NOT reinterpret the s ≥ 2 sector.
9. Do NOT merge A3-4 and the contract loop merely because both are called TT.
10. If the objects are not legitimately comparable, STOP and report precisely why.

## Pre-registered outcomes

- **DIFFERENCE_EXACTLY_GAUGE_SECTOR** — the divergent difference is completely
  accounted for by the identified constant-TT contribution (patch-local gauge).
- **DIFFERENCE_PARTLY_GAUGE** — the identified sector explains part; a residual
  physical/undetermined difference remains, characterized.
- **DIFFERENCE_NOT_GAUGE** — the difference survives after the sector is isolated.
- **OBJECTS_NOT_COMPARABLE** — their (O, D, L, R) tuples prevent a legitimate
  comparison; the precise obstruction named.
- **NO_DIFFERENCE** — ONLY if the comparison genuinely establishes equivalence, never
  because both happen to be finite/divergent in similar ways.

**Standing negative result (owner's, carried verbatim):** *A finite A3-4 object does not
constitute evidence that the contract loop is finite unless the comparison establishes
that they are the same physical observable or that their difference is completely
accounted for.*

**What success earns (owner's ceiling):** at most — *"The observed O(H²) divergence in the
contract representation is attributable to a locally gauge sector, subject to the
unresolved global/large-diffeomorphism and loop-level Ward questions."* Nothing more.

## Known object facts on the record (starting inventory; surveyor extends and corrects)

- **A3-4:** the assembled TT response of the graviton probe, layer (2) verdicts on "the
  declared TT object" (Q1^TT INSIDE: nonlocal TT block = a(ω,k,H,m)·P₂^TT exactly at H⁰,
  H¹, H²; Q3 INSIDE s ≥ 2 convergent, GAPPED; Q5 INSIDE), frozen kernel dd77b19…,
  built from the Tier-1 vertex through the A1–A3 assembly (source vertex + observer
  vertex + external-mode corrections), gauge/orbit-checked at A4 through O(H²); state
  per WALL_A_A3_DECLARATIONS (BD, Option-3a). The owner's closure: K_R is
  "mathematically distinct" from this Σ_R^finite — it lies downstream of a G_R^TT
  dressing "obstructed at wall A." Layer (1) raw non-TT findings kept separate by owner
  directive; the non-TT vector Ward residual is Class B, unresolved.
- **Tier-3 contract loop:** the TT-gauge one-loop pair Σ_> ∓ Σ_< from the same frozen
  Tier-1 dS cubic vertex with frozen Tier-2 TT-gauge BD Wightman legs on the
  q-continuum, k_ext = 0 literally substituted, u_b-free at O(H²); fork (ii) fired
  (retarded α = −1, noise α = −2); Wall-A: the log class is projection-invariant, the
  power class is the k_ext = 0-exactly artifact; ALL IR-divergent leg weight on any patch
  = the constant TT mode.
- **The same vertex feeds both** — this is what makes a comparison conceivable; the
  question is whether the assembly/external structure/dressing makes them different O.

## Anti-optimization

DIFFERENCE_EXACTLY_GAUGE_SECTOR is the framework-favorable direction and the one the
last three results lean toward — named trap. OBJECTS_NOT_COMPARABLE is the
nothing-to-do comfort. NO_DIFFERENCE is the over-unification trap (the program's
characteristic failure: collapsing distinct referents). None preferred; the adversarial
checker attacks hardest in the framework-favorable direction and independently re-runs
the ΔO computation.

## Method (lean)

Surveyor (the two (O, D, L, R) tuples, on the record, with every difference in
construction enumerated) → deriver (representation alignment; ΔO; sector isolation;
residual) → adversarial checker (independent re-run of ΔO and the sector isolation;
object-slippage attack; large-diffeo qualification audit) → resolver on disagreement.
Frozen artifacts read-only; scratch only; computations run, not asserted.

*Frozen 2026-09-16 before any agent ran.*
