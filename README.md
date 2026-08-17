# GRUT ResponsiveAI — workspace

## The two lineages, stated plainly (read this first)

There are **two distinct bodies of work called GRUT**, and they are **not the same theory**:

1. **The v2/v4 lineage** — the earlier public material (the book and its numbers). That lineage is
   **not this repository**, and nothing here certifies it.
2. **The clean rebuild** — **this repository**: the from-scratch reconstruction under the v5
   charter, in which every claim is machine-audited, tiered, sourced, falsifiable, and priced in a
   signed assumption ledger. **The rebuild does not inherit the book's numbers.** Where the two
   lineages disagree, this register's claims — with their sources and falsifiers — are the ones
   this repository stands behind, at exactly the tiers stated and no higher.

To verify the state of this repository yourself, see [`HOW_TO_VERIFY.md`](HOW_TO_VERIFY.md).

<!-- REGISTER-SYNC: 49 nodes, net +14 -->
<!-- REGISTER-TOTAL: 70 = 49 grut + 21 vacuum-cluster; nets +14 grut, +0 cluster -->
*Vocabulary gloss for outside readers (added 2026-08-10 after an external reviewer reasonably misread it): **net +13** is the blind SUM of the register's underived-input ledger — the standing price of every assumption, unchanged for weeks and meant to stay unchanged — not a count of new entries; **CLEAN** means the register is unmodified since the last accepted change. Neither is a progress metric.*

> **📘 Canonical theory book: [`GRUT_ToE.md`](GRUT_ToE.md)** — the single living document for GRUT's
> physical picture (net **+13** GRUT; 49 GRUT-scope nodes + 21 vacuum-cluster = 70 in `claims.json`, validator GREEN). Of the **+13**, **+8 rides on four declared `laundering_ok` waivers** (`rung1_inin_action` +3, `rung5_gr_limit` +2, `rung6_qm_limit` +2, `p_tt_ansatz` +1), each carrying a written stance justification — `validate.py` prints the waived total on its own face. The dated build-log notes lower in this
> README are **historical** and are superseded by `GRUT_ToE.md`; trust the book and the register
> (`provenance/claims.json`) for current state.

> **Governed by [`CHARTER.md`](CHARTER.md) (GRUT v5 Build Charter).** Every artifact here is
> subordinate to it. The dependency ledger (`provenance/`) is the product; the gate
> (`provenance/validate.py`) enforces the five disciplines. The frontier (what bath Hilbert space
> the vacuum is made of) is **not** an in-house calculation — banking a resolution of it here is an
> automatic fail.

Rebuild of the Grand Responsive Universe Theory from a single standable stance:
**the gravitational vacuum is a responsive medium with finite memory, governed by one
in-in (Schwinger-Keldysh) action.** The commitment is not "responsiveness explains
everything" — it is the **discipline** of marking, ruthlessly, where responsiveness is
*shown* vs merely *assumed*. The win condition is a short, marked input list, not zero
inputs.

## Layout
```
provenance/   track (c) — the discipline spine (build this first; it checks everything else)
  sources.json    primary-source register (verified against the actual papers)
  claims.json     the derivation ladder as machine-checkable claims (tier + source + falsifier + ledger_delta)
  validate.py     BLOCKING validator: every claim tiered + sourced + falsifiable; laundering
                  DISCIPLINE enforced (declared fields + a blind ledger sum). It verifies
                  DISCIPLINE, not TRUTH -- a wrong-but-well-provenanced claim passes, an
                  unearned tier graduation is caught by the resident's flags + the firewall,
                  not here, and +8 of +13 sits behind declared laundering_ok stances that the
                  gate now prints on its own face. (Top-line corrected 2026-08-09: the old
                  "no laundering" claimed more than the code enforces -- the guard was honest,
                  the narrative had drifted. Tenth instance of that pattern.)
gate/         the hard gates, as functions not slogans
  kms.py          KMS/FDT admission gate: a kernel enters the foundation only if it passes detailed balance
calc/         the physics calculations (each one a runnable falsifier)
  finite_T_exponent.py   kill-shot #1 — does finite-T break single-pole?
  RESULTS_finite_T.md    the result: soften-not-break (lead; awaiting outside-expert sign-off,
                         which as of 2026-08-12 has never been sought or received)
```
All pure Python 3 stdlib — no deps, so the calculations are inspectable and reproducible as-is.

## Run
```
python3 provenance/validate.py     # tiering gate; exit 1 on any laundering / missing provenance
python3 gate/kms.py                # KMS gate self-test (thermal kernel passes, white noise fails)
python3 calc/finite_T_exponent.py  # kill-shot #1 calculation
```

## State (2026-06-25)
Adversarial review returned REJECT-pending-three-repairs on the physics headline while
crediting the discipline scaffolding. The four legs (in-in/CTP, Mori-Zwanzig, FDT/KMS,
trace-anomaly α) verified against primaries. Open kill-shots:
1. **finite-T single-pole** — COMPUTED: soften-not-break (s:3→2, still super-Ohmic, S(0)=0,
   cutoff-set memory). Pending pole-structure sign-off by an outside expert — never sought or received as of
   2026-08-12; the in-house passes recorded below were owner-run. → `calc/RESULTS_finite_T.md`
2. **falsifier energy-basis** — RECOMPUTED: relocated, not dead. The differentiator is the
   energy-basis signature (Γ scales with energy gap ΔE, ignores spatial size Δx — orthogonal to
   DP/CSL), and it is *independent of #1*. "689 Hz parameter-free" retired → staked cutoff scale
   ω_c + a parameter-free shape; BMV backup withdrawn. New tension: the wedge is sharp but may be
   *faint* (S(0)=0 / cutoff suppression). → `calc/RESULTS_energy_basis.md`
3. **GR recovery imports the explanandum** — at rung 5 the in-in machinery does no work;
   either derive the Einstein sector from χ via the Ward/diffeo identity, or mark GR borrowed.

Plus structural: differentiation funnels onto rung 8 — diversify before staking the program.
**Rung 7 explored** (`calc/wz_dark_energy.py`, `calc/RESULTS_wz.md`): evolving w(z) is a
structural second differentiator, but it **requires a second slow scale τ₂∼1/H₀** — exactly the
"second bath scale" rung 3's confirmation forbids. They coexist by ~40-orders scale separation
(UV cutoff = tabletop single-pole; IR horizon = cosmology w(z)), so GRUT must commit to a
**two-scale vacuum**. A single-mode relaxor cannot produce DESI's w=−1 **crossing** (needs ≥2 modes;
generic/Vikman); the sourced prediction is w=−1 **flat**, and the w_a **sign** of any inserted-scale
evolution is **frontier-indeterminate** (the toy's w_a≤0 is a ζ=const artifact, not "wrong sign") — the
matching shape is to-derive. A second observable independent of rung 8 (GW dissipation from
Im[χ]) is still open.

Rung 3 (`finite_T_exponent.py`) is now **DERIVED** — single-pole confirmed at finite T by an
owner-run open-systems adversarial pass (analyticity: S∼aω²+bω⁴, no second pole), conditional
on no second bath scale (see two-scale finding above). **[QUALIFIED 2026-08-12: this note read
"by an open-systems specialist," which in a public document says *human expert*. The register
never records the modality of any such pass and logs no transmission to an outside human at any
date — see `GLOSSARY.md`'s "specialist" entry. The tier was later re-qualified as
regime-conditional and rung3 now stands `derived-pending`; this build-log line is historical.]**

**Rung 4 GW dissipation** (`gw_dissipation_bounds.py`, `calc/RESULTS_gw.md`): outcome **(B)
real-but-unobservable** — Im[χ] gives GW dephasing/v_g≠c (absent in GR) but ~10²²–10⁶² orders
below LIGO; GW170817 speed bound satisfied with 26–66 orders to spare (not binding). Ruled out as
a second differentiator; the smallness is the same Planck suppression that gives solar-system
safety, so it does not weaken GRUT.

**In-house adversarial-pass verdicts (2026-06-25, four questions worked — `SPECIALIST_BRIEF.md`):**
**[QUALIFIED 2026-08-12: this heading read "Specialist verdicts … all four questions answered,"
which asserts outside experts answered. They did not. These were owner-run passes; the register
logs no transmission to any outside human at any date, and the one drafted ask remains unsent.
See `GLOSSARY.md`'s "specialist" entry (41 occurrences audited, 22 of them of this class).]**
- **Q1** energy-basis falsifier — decision tree confirmed; survival reduces to one operator-algebra
  question: does the effective gravitational coupling satisfy **[A, H_S] ≠ 0**? Yes → samples
  S(ΔE), falsifier lives; no → samples S(0)=0, quiet bath, falsifier dies. **The decisive next calc.**
- **Q2** w(z) — single passive relaxor provisionally **cannot cross w=−1**; DESI quintom needs ≥2
  modes → economy win lost; structural evolution differentiator survives but weak.
- **Q3** GW dissipation — **confirmed dead** (Planck-suppressed). Closed.
- **Q4** GR recovery — Ward identity **cannot** uniquely generate Einstein-Hilbert; **GR is borrowed,
  not hosted**; strong hosting is an open hard program.

**Q1 computed** (`q1_energy_basis_magnitude.py`, `calc/RESULTS_q1_magnitude.md`): ratio-first. The
dominant **diagonal** T^00 coupling is quiet (S(0)=0, Γ=0 → dies); the wedge-carrying
**off-diagonal** T^0i/T^ij coupling is faint (~7–47 orders below detectable); the robust Pikovski
effect is position-basis (not the wedge). The energy-basis falsifier **does not carry the program**
as a parameter-free observable. Rung 8 differentiator → **FAILS-DIFFERENTIATION (quiet-or-faint)**.

**The arrow — attacked and stamped** (`arrow_origin.py`, `calc/RESULTS_arrow.md`, register claim
`arrow_of_time`; toy + 7-agent adversarial workflow, primary-source-verified). Decisive cut:
**existence vs direction.** The in-in machinery intrinsically supplies the *existence/magnitude* of
dissipation (retarded analytic self-energy, positive spectral measure, positive noise), but the
*direction* is **imported** via a low-entropy past-boundary state — decisively the **passivity /
KMS β>0 of the bath** (Pusz-Woronowicz; sign(β) alone fixes damp vs anti-damp, β<0 reverses it),
with factorization (Stosszahlansatz) and the past-endpoint contour as the same assumption in other
guises. Toy: Γ(t) even, full recurrence at t_rec∝N, decay set by the assumed state. No derivation
escapes a low-entropy input. **GRUT does not derive the arrow.**

**What GRUT is (the floor — honorable):** every empirical differentiator fell to honest
calculation (falsifier quiet/faint, GW dissipation dead, GR borrowed, w(z) needs 2 modes), and the
arrow's direction is imported too. GRUT's genuine contribution is **methodological**: the
existence-vs-direction decomposition and the triangulation locating *exactly where and in what form*
the arrow is assumed (the passive past-boundary state) — a real, honest contribution to the
Albert/Price/Carroll problem, not a derivation. The premise that survived is the narrow one: not
"responsiveness explains everything," but "here is exactly where it does and does not, marked, not
laundered." Ledger now **+9** (the Past Hypothesis added as a named underived input).
