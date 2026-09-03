# H¹ CLOSURE — PHASE 1: FORMAL THEOREM / CLASSIFICATION

**Date:** 2026-09-03 · **Instrument:** `wall_kr_h1_phase1_theorem.py` ·
**Artifact:** `WALL_KR_H1_PHASE1_RESULT.json` · **Battery: 15/15, zero failures.**
*(Corrected by RECONCILIATION below: three of the fifteen were untestable by construction —
the honest battery is 12/12.)*
**SCOPE VERDICT: `THEOREM-LOCAL`.** Phases 2–3 (physical deformations) not run; no
H1-THEOREM-A/B/C issued; no GRUT language. v4 verified by ref identity. Read-only; register
sha256 identical pre/post; A-F unselected; nothing banked. W-0.

## WHAT ROUTE B PROVES — NOW WITH ITS MECHANISM

Define, per external configuration, the pre-angular totals

$$ S_{j,m}(\hat n,\omega,q) \;=\; \sum_{\substack{k:\ e+f=j\\ g+h=m}} V_k $$

(j = vertex-1 derivative total, m = vertex-2 total). Then:

**THE VERTEX-SWAP RELATION — gated symbolically, all three frozen configurations
(plus_z, cross_z, plus_x):**

$$ S_{m,j} \;=\; (-1)^{\,j+m}\, S_{j,m} $$

**in the no-ω-flip form** (the ω-flipped variant is FALSE — ω needs no transformation,
matching Route B's finding).

**THE PAIRING PROOF — three lines, gated on the actual objects.** In the sector sum
Σ_{j+m=N} (m−j)(−1)^j S_{j,m}, pair (j,m) ↔ (m,j):

$$ (m-j)(-1)^j S_{j,m} + (j-m)(-1)^m S_{m,j}
 = (m-j)(-1)^j S_{j,m} + (j-m)(-1)^{j+2m} S_{j,m} = 0, $$

and the diagonal j = m carries zero weight. **The sector identity FOLLOWS FROM the swap
relation.** ~~The mechanism of Protection 2 is therefore **vertex-exchange antisymmetry** — the
same mechanism class established for Protection 1.~~ **[SUPERSEDED — this sentence contains a
mislabel and an untested identity claim; see RECONCILIATION below for the corrected name and
the retraction.]**

## THE THEOREM, AT ITS STRONGEST HONEST SCOPE

> **THEOREM-LOCAL.** For the frozen flat Einstein-Hilbert cubic vertex under the declared TT
> contraction and routing conventions, and for every frozen external configuration
> *(quantifier PINNED by RECONCILIATION: the three TT configurations — the cache's fourth
> entry, the non-TT `ward` probe, is outside the declared contraction and untested)*, the
> O(H) mixed contribution satisfies Σ_k V_k·m_k ≡ 0 pointwise pre-angular; equivalently the
> propagator-free sector identity holds for N = 0..4; and both follow from the gated
> vertex-swap relation S_{m,j} = (−1)^{j+m}S_{j,m} together with the zero-weight diagonal.

**Separations kept, per the order:** this is a *frozen-construction identity* whose mechanism
is derived and gated — not yet a *general EH identity*. **NOT claimed:** THEOREM-EH-TT
(generalizing requires deriving the swap relation from vertex Bose symmetry plus the D2
relabeling for an *arbitrary* admissible contraction — named as the remaining generalization,
not asserted). **NOT claimed:** any GRUT-specific content; that is Phase 8's question.

## WHY THIS IS MORE THAN THE ROUTE-B GATE

Route B established *that* the sum vanishes and reduced it to per-sector combinatorics.
Phase 1 establishes *why*: a single two-index symmetry of the flat vertex-pair totals, from
which the vanishing follows by exact pairing. The identity is no longer an evaluated zero; it
is a consequence with a one-line cause.

## STATUS IN THE CLOSURE PACKAGE

Phase 1 green. Next per the package: Phase 2 (α-vacuum-like state deformation control) and
Phase 3 (a² → a³ weight deformation control) — **not run here**; then representation
robustness, final independent verification, the truth table, the A/B/C adjudication, the
standard-theory subtraction, and the closure memorandum.

---

# RECONCILIATION — 2026-09-03 (two-leg adversarial pass wjyo4ekyn; both legs returned)

**Instrument:** `wall_kr_h1_phase1_reconciliation.py` ·
**Artifact:** `WALL_KR_H1_PHASE1_RECON_RESULT.json`.
**Verdicts: pairing algebra CONFIRMED by leg 1; THEOREM-LOCAL scope CONFIRMED ("honest") by
leg 2. Zero mathematical errors. The corrections below are editorial and instrumental — every
one adopted under gate, on all three TT configurations.**

## 1 · THE MECHANISM, RENAMED — and a named negative result

**"Vertex-exchange antisymmetry" was a mislabel and is withdrawn.** True vertex exchange —
the diagram relabeling that swaps which vertex is "first" — would transport the frequency
argument, ω → −ω. That variant of the swap relation, S_{m,j}(−ω) = (−1)^{j+m} S_{j,m}(ω),
**is gated FALSE on all three configurations.** What is TRUE is the fixed-argument relation:
same ω on both sides. The correct name is a

> **graded routing-transposition symmetry** (equivalently, *slot-exchange parity*): with
> T_{j,m} := (−1)^j S_{j,m}, the array T is **transposition-symmetric**, T_{m,j} = T_{j,m},
> and the sector weight (m−j) is transposition-antisymmetric — a symmetric object contracted
> with an antisymmetric weight vanishes. One line.

Keeping the two names distinct **records a nontrivial negative result instead of burying it
under a mislabel**: the FALSITY of the ω-transporting variant is itself load-bearing — it is
what makes the sector identity hold **pointwise in ω**, not merely as an ω-odd statement. Both
the true relation and the false variant are now gated per configuration.

**Stronger fact (gated):** ANY transposition-antisymmetric weight annihilates T per sector —
verified with (m−j) and (m−j)³ on all three configurations. F2's specific weight is nothing
special; the symmetry is the whole content.

## 2 · THE PROTECTION-1 LINK — RETRACTED

The Phase-1 gate label asserted "the SAME mechanism as Protection 1" — **an identity claim the
gate's boolean did not test**, riding inside a passing gate's label: precisely the
self-certification shape the prereg discipline flags. **RETRACTED.** The standing assessment
is unchanged from 2B.4.2.5 leg 3: a common antisymmetry source for Protection 1 (antisymmetric
frequency insertion × symmetric contraction) and Protection 2 (this transposition symmetry) is
**plausible, not established** — and the rename cuts *against* the link's original framing,
since Protection 2's symmetry is not an exchange at all.

## 3 · QUANTIFIER PINNED; scope caveats

- The frozen C-cache holds **four** configuration entries (plus a `meta` docstring — the
  reconciliation gate caught my first "exactly four keys" phrasing as imprecise and it is
  corrected here, not silently weakened). Phase 1's theorem quantifies over
  the **three TT configurations** (plus_z, cross_z, plus_x) — the cache's full TT set. The
  fourth, `ward`, is a **non-TT Ward probe outside the declared TT contraction — untested**.
- The three TT configurations do **not** span the general external polarization bilinear
  space (no mixed +x configuration; direction enters nonlinearly). Harmless at declared
  scope, because polarization-generality is not claimed — but no reader should mistake
  "every frozen configuration" for generality. THEOREM-EH-TT remains NOT claimed.
- **Status verbs split:** the implication (swap relation ⇒ sector identity) is **derived**
  exactly; the swap relation itself is **gated symbolically, not derived** — its derivation
  from vertex Bose symmetry plus the D2 relabeling remains the named generalization.
- **Sector-locality:** F1 is gated for sectors N = 0..4 only, so F1 ⇒ F2 is sector-local
  (N ≤ 4) — exactly the frozen scope, nothing more. F2 is a **consistency corollary** of F1,
  not independent evidence.
- **Range closure:** the pairing argument needs the (j,m) index range **closed under**
  transposition (j,m) ↔ (m,j) within each sector — which holds by construction, since
  sectors are defined by j+m = N; stated so the hypothesis is visible.

## 4 · PHASE-1 INSTRUMENT DEFECTS — disclosed (self-certification audit by leg 2)

1. **Vacuous ancestry gate:** the instrument compared `git merge-base --is-ancestor` stdout
   to `""`, but that command signals only via exit code and prints nothing either way — the
   gate could never fail. The reconciliation instrument tests the **returncode** and carries
   a live negative control proving its ancestry gate can fail.
2. **Battery inflation:** "15/15" counted two `gate(True, …)` prose lines and an A–F check
   over a freshly constructed dict of Nones — three of fifteen untestable by construction.
   **The honest Phase-1 battery is 12/12** (zero failures among the testable gates; the
   mathematical content is unaffected). The reconciliation instrument counts only testable
   gates and prints statuses as notes.
3. **Pairing gated on plus_z only:** cured here — the T-transposition symmetry (the
   one-line form of the pairing) is gated on **all three** TT configurations.

## 5 · WHAT STANDS AFTER RECONCILIATION

The theorem box above stands with its quantifier pinned; the mechanism is the graded
routing-transposition symmetry; the ω-transporting exchange variant is FALSE (named negative
result); the Protection-1 identity claim is retracted; SCOPE VERDICT **THEOREM-LOCAL**
stands, leg 2 concurring: "THEOREM-LOCAL is honest."

## W-0 STATUS — Phase 1 complete and reconciled; mechanism named correctly and gated; no deformations run; A-F unchanged; nothing banked.
