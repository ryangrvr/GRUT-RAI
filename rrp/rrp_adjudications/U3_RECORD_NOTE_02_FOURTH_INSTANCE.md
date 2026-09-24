# U3_RECORD_NOTE_02 — fourth narrative-vs-run instance, at the base rung

**Date:** 2026-09-24. **Found by:** adversarial verification of GRUT_SKELETON_01 v01
(two record-verifiers, workflow wf_c4977c70-167), confirmed at source by the
adjudicator against the RESULT JSONs in the builder tree (read-only). **Affected
records:** `U3_ORIGIN_PERSISTENCE_RESULT.json`, `U3_SPECTRUM_RESULT.json`.

## The findings (all verified at source)

1. **P3** (`P3_eliminating_local_dof_produces_memory_kernel`): `pass: false`, tail
   error 9.95e-01 — while its own summary asserts "Memory EMERGES from locality +
   coarse-graining. This is branch A evidence: persistence can be derived, not
   assumed." The summary narrates the success the check refuted.
2. **P4** (`P4_finite_bath_realization_dimension_equals_M`): `pass: false`, Hankel
   rank {1:1, 2:2, 3:3, **5:4**} — the claimed N = M law breaks at M=5 — while the
   summary asserts "Coarse-graining M local d.o.f. gives N = M as a mathematical
   consequence." Downstream calcs then cite "the N = M topology law remains derived"
   (gravitational-clock consequences; resistive-scale consequences) — prose citing
   prose, with the defining check failed.
3. **E4a** (`memory REQUIRES persistent auxiliary structure (Erlang convergence)`):
   `pass: false`, `status: FAIL` — and the msg states the L1 errors "decrease with n"
   over the recorded sequence **[0.721, 0.825, 0.984, 1.193], which increases**. The
   msg then builds the "representation theorem" language (system/bath split as
   representation) on top of the failed convergence claim.

## Impact

- These three checks are the constructive half of the **U3-LEMMA / base rung** (memory
  ⟺ persistent auxiliary variables; N = M). What still stands on passing checks: the
  **necessity direction** (P1, P2 — persistence requires independent auxiliary state)
  and the conditional-uniqueness/support-observable results (E2a, E2b). What does NOT
  currently stand at check level: constructive realizability, Erlang representability
  convergence, and the N = M law.
- GRUT_SKELETON_01 v01 propagated the verdict prose into its base-rung DERIVED tag;
  v02 demotes it (necessity DERIVED / converse OPEN) and discloses the instance in
  its §10. GRUT_EMERGENCE_THEORY_STATUS_01 §1's "U3-LEMMA" language inherits the same
  demotion at the constructive half (this note is the correction of record).
- The N = M relocation reading ("N derived from topology, relocated onto supplied M")
  is NOT presently bankable: its defining check failed. If the P4 failure is a
  numerical-rank artifact (near-degenerate mode at M=5), the repair below will show it.

## Repairs owed (builder side), in priority order

1. **Diagnose P4**: determine whether rank 4 at M=5 is a genuine counterexample to
   N = M or numerical rank deficiency (tolerance/conditioning of the Hankel test);
   re-run with controlled conditioning; rewrite the summary FROM the outcome.
2. **Diagnose P3**: the 0.995 tail error against a 5e-2 threshold is not marginal —
   either the analytic target K = g² e^(−at)Θ(t) is wrong for the tested chain, or
   the extraction is; identify which, fix, re-run.
3. **E4a**: recompute the Erlang cascade convergence (the recorded sequence diverges —
   likely a normalization or comparison-window error, or the claim is false as
   stated); rewrite msg from the numbers.
4. Rewrite the three summaries and every downstream `consequences` string citing
   "N = M ... derived" from the repaired outcomes. Until then, those strings are
   quarantined as prose-over-failed-checks.

## Standing rule (restated)

Checks outrank prose. A verdict may not assert what its checks refused. This is now
the FOURTH instance (t^(−d) vs t^(−d/2); t^(−3) vs t^(−4); coupling verdict_detail vs
run; P3/P4/E4a vs summaries) — the pattern is systematic enough that every future
calc's verdict should be machine-assembled from check outcomes, not hand-written.
