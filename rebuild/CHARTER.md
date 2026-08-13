# GRUT v5 — Build Charter (the constitution for the rebuild)

*This document governs the rebuild. Every other artifact in this workspace is subordinate to it.
The dependency ledger (`provenance/`) is the product; the gate (`provenance/validate.py`) enforces it.*

## 0. Mission
Extend the **clean** GRUT (the from-scratch responsive-vacuum rebuild — `provenance/`, `gate/`,
`calc/`), not the baggage-heavy v4. The deliverable is an audited framework that marks, ruthlessly,
where every claim is *shown* vs *assumed* — the dependency ledger is the product. Build outward one
marked rung at a time. The generative vision (responsiveness as the root of structure) is the
direction; the discipline is what lets the reach become real instead of laundered. **This is not a
theory of everything**, and any draft that starts sounding like one has drifted.

## 1. Five non-negotiable disciplines (the checking machinery)
1. **Tier every claim** — shown / derived / derived-pending (derived modulo a named open input) /
   assumed / to-derive. No untiered claim enters the document.
2. **The anti-laundering gate, as code.** Every claim needs a tier + a primary source + a falsifying
   computation. No net-positive rung (one that adds assumptions) may be sold as a derivation. The gate
   blocks the build on violation.
3. **Pre-screen every forward/resolution claim adversarially, BEFORE banking it** — a panel charged to
   break it, defaulting to broken. Especially anything you want to be true.
4. **The directional-optimism rule (the deepest lesson).** The loop reliably over-claims in one
   direction — toward strengthening the result — and worst on "build toward resolving X" targets. So:
   on any resolution claim, assume you've over-claimed until a pre-screen says otherwise.
   Strength-of-claim and scrutiny move together.
5. **Carry scar tissue, shed baggage.** Verified findings come forward; machinery, dead-end targets,
   and over-elaborate tiering do not.
6. **Pre-registered termination** *(added 2026-08-09)*. The program carries a stop condition written
   **outcomes-first** — what each live empirical channel's result means, sealed before the results
   arrive — then a date, **signed by the human owner** (unsigned = not in force). Work past the date
   requires a new signed condition, not momentum. The stop condition may never be reported on a
   subset of its channels: cherry-picking an ending is the laundering shape, applied to a
   conclusion. Instrument: `provenance/prereg/PREREG_TERMINATION_2026-08-09.txt`.

## 2. The inherited state — DO NOT re-derive or re-break these
Settled at their stated tier. The building chat starts from here.

- **shown** — the four legs: in-in/CTP, Mori–Zwanzig, FDT/KMS, trace-anomaly α — verified vs primaries.
- **derived (clean)** — the arrow existence/direction decomposition (existence intrinsic;
  direction state-dependent = the Past Hypothesis = the KMS gate).
- **derived-pending** — single-pole (pending bath collisionality / bath Hilbert space; the favorable
  lean is near-circular — GRUT's finite-memory/local-influence-functional axiom *is* the analytic
  class, so the lean is the premise restated; the only independent content is the finite-T robustness,
  the coth could have made a slow second pole and doesn't — **do not write single-pole as "the one
  earned result"**); μ_linear = 1 (**derived-pending / no-go export, NOT clean** — the μ=4/3 exclusion
  is the established boundary; the positive μ=1=ΛCDM statement rests on the hand-inserted `p_tt_ansatz`).
- **settled-negative (frozen)** — the α normalization bridge (`rung9b`): settled-negative on three
  named obstructions (projector orthogonality primary); c₀=α survives only as an adopted
  phenomenological parameter. Not "pending" — settled-negative (**not forbidden**: impossibility in
  every extension is *not* claimed; reopen only on a new scalar→TT operator identity or the c/C_T
  Weyl-sector CFT route — see `NO_GO_LEDGER.md` entry 1), Version-I frozen.
- **assumed** (name each at the rung it enters) — the system/bath split (the deepest), GR-limit imports
  (area entropy, Unruh T), the Born rule, the two-scale IR mode for w(z), the SM spectrum.
  *(**Λ REMOVED from this list, 2026-08-04 — overseer-ruled.** It was a category error: an observed
  value is a **datum every candidate theory must reproduce**, not a discretionary posit, and it
  cannot be "dropped" the way an assumption can. Listing it here over-reported the count of
  droppable inputs by one and would have licensed the sentence "the framework does not assume Λ",
  true of a posit and false of a datum. The register's own `lambda_undetermined` node had it right
  all along — `to-derive` / open-field / Δ0 — so the node was correct and the constitution was
  wrong. Found by pointing the instrument at foreign physics; see `VACUUM_CLUSTER_MAP.md`.)*
- **refuted/closed — do not resurrect** — GR-as-derived (the diffeo Ward identity does not select
  Einstein–Hilbert — GR is borrowed); GW dissipation as a differentiator (invisible, ~10²²⁻⁶² down);
  689 Hz as a parameter-free position-basis falsifier (it's energy-basis, quiet-or-faint); the
  economical w(z) (needs ≥2 modes); conformalon-as-second-mode (gives w = +1/3, wrong equation of state).

## 3. The frontier — the one open question, and how to treat it
The deepest open item: **what bath Hilbert space was integrated out to make the influence functional**
— equivalently, what the vacuum is made of. It decides single-pole, the rheology, and the
conformalon's IR. **It is NOT an in-house calculation.** It is the most over-claim-prone region in the
program (the place everyone most wants "Class A / collisional / single-pole survives"). The building
chat specifies and hands it out to whoever can construct the microscopic bath from first principles —
it does not compute-and-bank it by analogy to oscillator baths or to collisionless transport. **Banking
a resolution of this in-house is an automatic fail.**

## 4. Named failure modes — recognize and refuse these
- **DOS-as-J** — density of states ≠ spectral density (J = DOS × |matrix element|²; the 1/ω_k matters).
- **Wrong object** — the T=0 vacuum exponent is not the memory; memory is the finite-T transport object.
- **The match temptation** — a predicted scale landing near an observed one (BAO, k_eq, 12.9 Mpc, 689 Hz)
  is scrutinized hardest, never celebrated. Carry free parameters free; never fit; expose no absolute
  scale you'd be tempted to match.
- **Definition-as-target** — a "check" that re-detects a contrast hard-coded into the chosen functional
  forms is not evidence.
- **Fiat exclusion** — renaming an inconvenient internal branch "not GRUT / a different theory" is
  relabeling, not physics.
- **Premature graduation** — `derived` requires a settling check, not "argued + pending." Awaiting a
  computation ⇒ `derived-pending`, not `derived`.
- **Compound mistaken for omission, and the reverse** *(added 2026-08-04; expect it in every cluster)* —
  the two present **identically** to an analyst. Both feel like "this node is carrying more than one thing."
  They are different defects with different repairs, and applying the wrong repair is worse than missing
  the defect, because it manufactures a false dependency graph.

  | | what it is | the test | the repair |
  |---|---|---|---|
  | **Compound** | one node carrying two separately-dischargeable things | can one part discharge **alone**? | **split** the node |
  | **Omission** | a presupposition booked **nowhere** | is it discharge-blocking for some node **and** unbooked? | **add** a node |

  The tell: if the candidate appears **in the node's own statement**, it is a split question. If it is
  **invisible in the text** and presupposed by the node's discharge, it is an omission — and if several
  nodes presuppose it, it is certainly an omission, because multiplicity rules out its being any one
  node's hidden conjunct. An analyst holding only the split tool "fixes" an omission by cutting the
  nearest node, which mislocates a cluster-wide presupposition into that node's dependency structure.
  **The two tallies are never summed.** Standards: the atomicity test (in `prereg/`) and
  `provenance/OMISSION_STANDARD_v2.txt` (v1 superseded 2026-08-05; the standard is unchanged, three application rulings added).
  *Provenance of this entry: the compound-split re-audit of 2026-08-04 was chartered to find compounds
  and found 2 compounds plus 3 omissions; two of five pre-registered candidates were mislocated splits,
  one of them at medium-high confidence. An adversarial reviewer predicted the confusion **in writing,
  before the count came in**, and was right.*

## 5. Build order
1. **Foundation first, green before forward.** The four legs as shown, the ledger, the gate-as-code,
   the validator passing. No sector expansion on an unproven footing — that's the v4 baggage in cleaner code.
2. **Forward rungs only fully-tiered**, each with its ledger Δ; the net ledger arithmetic must match the
   tiers (a derived-pending rung does not count as an offset).
3. **Any claim that resolves a fork must pass an adversarial pre-screen and survive**, with the result
   relayed up (to the user/overseer) before it's banked.

## 6. Success criterion + how we keep it in check
**Success:** an outside referee, handed the register, sees in one pass and without trusting us what is
shown, derived, assumed, and falsifiable — and the framework holds even its favorite results to the
discipline (single-pole demoted is the proof it's working). **Check loop:** the building chat relays
every forward-claim pre-screen and every tier graduation up through the overseer before banking, so
directional optimism gets caught before it sets. The ledger is the product; the discipline is the
theory's real output.

## 7. Machine-checkable disposition rule (the resident)
The resident (`provenance/resident.py`) protects a claim's disposition only if it can *see* it. So:
**every closed / disfavored disposition marker MUST live in the claim's `sub_status` field** — the
machine-checkable field the resident scans (`settled-negative`, `refuted`, `moot`, `no_go_export`,
`disfavored`, `deferred`, `forbidden`). `tier_note` is **prose-commentary only**; a disposition recorded
there but not in `sub_status` is invisible to the resident, so a later softening of it would bank as a
silent PASS. (This was a real hole: `founding_h2`'s "disfavored" lived only in `tier_note` until the
marker was added to `sub_status`.) **Do not** make the resident scan `tier_note` instead — that is
verified over-reach (≈12 claims' `tier_note`s legitimately mention *other* claims' markers and would be
falsely flagged). The data home, not the scan, is correct: put the marker where the machine looks.

**Corollary (cross-references, added 2026-07-04).** `sub_status` holds a claim's OWN disposition markers only. A *reference* to another claim's marker (e.g. `u6` noting that `info_i2` was screened-refuted) must live in `tier_note`, not `sub_status` — otherwise the resident's `_is_closed` reads the referenced marker as this claim's own and false-flags it (RE-OPENS / BUILDS-ON-CLOSED). This is the third free-text-regex near-miss of the program (after the `refuted`-negation and the version-token); handled by correct data placement, *not* by rewording to dodge the scan. The durable fix remains the noted V2-era floor refactor (structured markers, regex as backstop — `RESULTS_resident.md`).

## 8. The GRUT II charter (governs all Version II work)
> **The purpose of GRUT II is not to derive a Theory of Everything. It is to determine whether constitutive response possesses mathematical structures universal across microscopic realizations. Every branch is a constrained classification problem with explicit failure states — never an ontology to defend.**

Operationally: every V2 claim is a **classification** with *first-class failure conditions* (a "no / only-one-class / reduces-to-known" outcome is a real, publishable result, not a failure of the exercise). No V2 branch may be worked as an ontology to defend, and no "emergent" / "forced" / "universal" verdict is banked without an exhibited derivation. The classification-fence lives in each V2 claim's `sub_status` (machine-watched). This charter (`u0`) is a governing rule, not a register claim.
