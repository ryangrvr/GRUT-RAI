# The Forward-Model Harness — GRUT's generative face

*The resident checks the consistency of **claims**; the harness extends it to the consistency-and-phenomenology of whole **models** — candidate universes. Sample a responsive-medium vacuum (a response-kernel spec), turn the shown formalism's crank, see what universe falls out, and hold the result to the machine. It is a **consistency-and-phenomenology harness, not a truth oracle, and not a ToE reclaim.** It tells you which responsive-medium universes are admissible and what they predict; it never tells you which is ours.*

---

## The cardinal invariant — the whole thing lives or dies here

**The machine tests admissibility; only data tests reality. These are structurally separate.** Every candidate universe carries **two independent fields**:

- **`admissible`** — from the discipline + the no-gos. In code, `admissible(spec, claims)` **has no `data` parameter** — it cannot see, and therefore cannot be tuned by, observation.
- **`data_consistent`** — from comparison to observation. Computed **downstream** of admissibility, only for survivors, and it **never feeds back** into `admissible`.

`data_consistent` is **never** an input to `admissible`. No universe is banked `shown`/real for passing the machine; the strongest a candidate earns is *"admissible + predicts X + consistent-with-data-Y-at-current-precision"* — a **candidate** tier, never shown. (Every universe spec carries `tier: "candidate"`; the harness has no path to graduate one to real.) **Merge the two fields and you have rebuilt laundering at the scale of whole universes.** Two tests pin this structurally: `admissible()` takes no data argument, and flipping the observation set never changes admissibility.

**Default-broken:** *"no admissible kernel reproduces our universe"* is a first-class, valuable output. An empty admissible-and-matching set is a real result, returned as such.

---

## The four pieces (`provenance/harness.py`)

1. **Universe spec** — a "GRUT universe" = a response-kernel spec (`spectral_form`, memory `L0`, KMS `T`, the `alpha` anchor, the `projector`, an optional inserted `second_scale` / `tuned_active` response) **+ provenance** (each free choice sourced to a register rung). A candidate, never a banked truth.
2. **Forward map (kernel → observables)** — wires the formalism:
   - **rung4 (shown)** → tidal Love storage Re χ + loss Im χ (KK-linked); GW dissipation real but Planck-suppressed (~10²²–10⁶² below detectable). **Derived.**
   - **rung7 (to-derive, guard tuning)** → w(z): a single UV-memory scale gives **w = −1 flat** (= ΛCDM), the *sourced* prediction; an **evolving** w(z) requires an inserted second slow scale τ₂∼1/H₀ (in the `mu_linear`-excluded trace sector) — so any evolving target is flagged `needs_unsourced_input`. The w_a **sign** of that inserted relaxor is *frontier-indeterminate* (rung7_w2): the second law fixes only the phantom **side** (w≤−1 for the dissipative branch — which forbids a crossing), **not** the w_a slope (the toy's w_a≤0 is a ζ=const artifact; ζ∼1/H² gives w_a>0) — **neither sign is sourced**. **Not fit; the inserted input is flagged, of either sign.** The no-clean-match result is carried by the `evolving ⇒ needs_unsourced_input` **invariant**, not by the sign.
   - **rung8 (to-derive)** → decoherence: the noise kernel N → an Anastopoulos–Hu energy-basis signature Γ(ΔE) that *follows from N* (not inserted); magnitude quiet-or-faint (S(0)=0; off-diagonal 7–47 orders below). **Shape derived from N.**
3. **Admissibility filter** (reuses the resident's register-DAG integrity check, and the same sourcing / closed-disposition discipline as `auditor.py`/`resident.py`, adapted for universe specs) — outputs `admissible` only: the **mu_linear no-go** (TT projector → μ=1 admissible; trace-only → μ=4/3 *excluded*), **rung2/KMS detailed balance**, **provenance consistency** (every *active* kernel input must be sourced to a real, non-closed claim — an un-sourced inserted input, or one leaning on settled-negative/no_go ground, is inadmissible), and the **bounded-family** check (only responsive-medium-with-finite-memory specs; off-premise excluded). It is computed with **no data argument**.
4. **Data-comparison layer** (explicitly the **truth-test**, structurally separate) — admissible survivors' predicted (w(z), decoherence, tidal) vs DESI/ΛCDM w(z) and a tabletop decoherence null. Outputs `data_consistent` **with a `laundering_flag`**: a "match" achieved only via an un-sourced/inserted input or a no-go violation **does not pass**.

---

## What the machine produces — the honest map (default-broken)

Run over the kernel family, the harness reports exactly what the register already implies, now operationalized:

- **Admissible** = the TT / KMS-locked / finite-memory vacua → **μ=1 (ΛCDM at linear order), w=−1 flat, energy-basis (quiet) decoherence, invisible tidal.**
- **Excluded** = trace-only (μ=4/3 no-go), non-KMS baths, off-premise (free-streaming) specs.
- **Data-consistent (clean)** = the single-scale vacuum predicting **w=−1** — consistent with ΛCDM at current precision.
- **Match-only-via-laundering (flagged, not a pass)** = a kernel that hits DESI's evolving w_a<0 — **including the passive 2-scale representative, which now carries the dissipative (DESI-*sign*) branch and matches DESI's sign within precision** — yet is refused because the evolving w(z) requires an inserted, un-sourced second scale. It matches DESI yet is flagged on **inserted-input grounds alone**: the strongest showcase that the machine refuses a DESI-looking universe without the sourcing.

**Verdict:** the responsive-medium premise admits ΛCDM-like vacua and produces **no distinctive matching universe without laundering**. Reproducing DESI's *evolving* w(z) — of **either sign** — requires an un-sourced second scale → the match is laundering, flagged and excluded. This holds **for a stronger reason than the sign**: it is the `evolving ⇒ needs_unsourced_input` invariant, not the wa sign, that blocks the match (the passive representative now *matches DESI's sign* and is still refused). An honest negative on a distinctive responsive-medium signature — not a forced match, and consistent claim-by-claim with the banked register (`mu_linear`=ΛCDM no-go, rung7 sourced=flat with an inserted-2nd-scale evolution whose sign is frontier-indeterminate, rung8 quiet/faint).

---

## Scope, guards, and honesty

- **Consistency-and-phenomenology harness, not a truth oracle, not a ToE reclaim.** It maps the admissible responsive-medium universes and their predictions; it never asserts which is ours.
- **Two-stage separation is structural** (above): admissibility and data-consistency are different fields; data never tunes admissibility.
- **No tuning-as-laundering:** matching data by a kernel that violates a no-go or needs an inserted input is **flagged, not passed.**
- **Bounded family:** only responsive-medium-with-finite-memory universes — the premise's boundary is a feature, not a gap.
- **Strictly the v5 register; no prior-lineage import.** The w(z)/decoherence maps are re-derived here against the v5 rungs (the v4 MGCAMB runs have no standing).
- **The register is untouched.** Sampling universes adds no physics input: the harness **reads** `claims.json` for admissibility and **writes nothing**; gate stays GREEN at net **+12**, 43 nodes. (Only a *derived* forward map would add a claim — and that would be posed default-broken and firewalled, not banked by the sampler.)
- **The decoherence null is non-discriminating** (honest caveat): all admissible kernels predict S(0)=0 (a quiet bath), so the tabletop-null check passes every one — it never rescues *or* distinguishes a DESI universe. The w(z) axis carries the discrimination; the decoherence axis only confirms the bath is quiet.

## Firewall record (two passes, both directions)

An independent both-directions firewall (steelman a clean match / break the machine / scope) ran on the harness; the first pass confirmed the **cardinal invariant is structural** and the **honest map accurate** (a 576→960-spec steelman sweep found no clean DESI match — only ΛCDM), and drove **two real laundering holes**, now closed: (1) the laundering guard fired only on the DESI branch, so an inserted-input universe could collect a clean *ΛCDM* match by widening the precision — the guard now fires on **both** branches, and `data_consistent` itself enforces *no clean evolving match* (defense-in-depth, holds even under `python -O`); (2) provenance checked only that present entries resolve — it now requires **every active input to be sourced**, and forbids sourcing to closed ground. The **re-firewall verdict was BANK-CLEAN** — break agent *holds*, exhaustive sweeps found zero leaks, the honest map confirmed by independent re-derivation. Regression tests reproduce all three escapes and pin them closed.

**Sign correction (2026-06-29, overseer-ruled — rung7_w2 sign screen).** The forward_wz w_a>0 "wrong sign" assertion was an un-earned over-claim (the *reactive* branch; not sign-constrained). It is softened to **frontier-indeterminate**, and the passive 2-scale representative is **flipped to the dissipative/2nd-law (DESI-*sign*, w_a≤0) branch** — so it now *matches DESI's sign within precision and is still refused*, on inserted-input grounds alone. This was the point: the no-clean-match guarantee never rested on the sign — it rests on the `evolving ⇒ needs_unsourced_input` invariant — so the sign correction makes the machine a **stronger** showcase, not a weaker one. `n_data_consistent_clean` is **unchanged** (still exactly one clean: the single-scale ΛCDM). Two regression tests pin it (`test_evolving_DESI_sign_branch_still_flagged_laundering`, `test_sign_flip_leaves_clean_count_unchanged`).

## Reproducibility
```
python3 provenance/harness.py        # demo: a kernel family -> admissible set, predictions, data-consistent subset
python3 provenance/test_harness.py    # 23 tests (cardinal invariant, exclusions, forward map, no-laundering, sign-flip showcase, default-broken)
python3 provenance/validate.py        # the gate: GREEN, net +12, 43 nodes (harness writes nothing)
```
Pure Python stdlib; the harness reads the register and reports; it never writes it, and it never banks a universe as real.


*Sync note (2026-08-02): the run-now expectations above are as-of-phase; for the live count and net, see the `GRUT_ToE.md` header and changelog (REGISTER-SYNC-guarded).*
