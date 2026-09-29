# L0-1c — PRE-FREEZE DESIGN REVIEW 01 (the record; preview values quarantined here)

**Date:** 2026-09-28/29 · **Object:** the L0-1c (D-LIN) charter draft
(`ab9108a`, rev 2 `dd60e52`) · **Method:** adversarial multi-agent
panel — four independent lenses (method-rule/prohibition compliance;
predicate-registry/instrument-artifact risk; numerical feasibility;
identity-vs-prediction honesty), every finding then independently
adversarially verified (default: refute). 33 agents total. The panel
ran **before freeze**; incorporating its confirmed findings is the
draft discipline working as intended, not amendment-after-results.

**Interruption disclosed:** five honesty-lens verifiers failed on an
account usage limit mid-panel (2026-09-28); the panel was resumed
after reset (2026-09-29) with all completed work replayed from cache
and only the five failed verifications run live. All 29 findings
received machine verdicts; none was adjudicated by the operator alone.

## Verdict tally: 23 confirmed, 6 refuted

| # | Lens | Finding (abbreviated) | Verdict | Disposition in the frozen charter |
|---|---|---|---|---|
| L01C-1 | prohibitions | Outcome A's per-member audit predicate uncomputable for 17/18 (blocker) | CONFIRMED | RC-2 made per-leg (all 18 halved audits); Outcome A restated mechanically (§5) |
| L01C-2 | prohibitions | instrument-vs-physics classification non-mechanical | CONFIRMED | leg roles frozen (§1); control/replication M-failures = HALT; Outcome A only from adjudicating legs; sign identity mechanized (RC-5) |
| L01C-3 | prohibitions | comparator "carried verbatim" has no carrying mechanism | CONFIRMED | textual copy of `fit_residuals` + TAUS, certified by new RC-6 against sealed L0-1a residuals (full precision, exact grade string) |
| L01C-4 | prohibitions | M-1/M-2 tolerance-band inconsistency on [−1e-12, 0] | REFUTED | band unreachable (theorem + margin); no change |
| L01C-5 | prohibitions | VACUOUS misdescribes mixed X-1; precedence unstated | CONFIRMED | VACUOUS = fails at both strong legs; mixed → PARTIAL naming the biting leg; precedence line with inertness note (§5) |
| L01C-6 | prohibitions | scope declarations missing from all lines but Outcome B | CONFIRMED | scope clause hoisted, standalone, binds every outcome incl. VACUOUS/PARTIAL/HALT (§5) |
| L01C-7 | prohibitions | §6 build_K restriction contradicts §1 | CONFIRMED | §6 reworded: build_K supplies K_b to both instruments |
| L01C-R1 | registry | Outcome A not executable (duplicate angle) | REFUTED | (HALT discipline already covers; superseded by L01C-1's stronger fix anyway) |
| L01C-R2 | registry | X-1 can't distinguish in-window activity from pre-window offset | CONFIRMED | D_act linear-continuation activation defect added (X-diag, ungated per design §5); NOT-LOAD-BEARING lines scoped to recorded D_act level |
| L01C-R3 | registry | convex quartic self-limiting: in-window nonlinearity capped uniformly | CONFIRMED | §3.4: max-principle envelope x₁² ≤ 1/(8βt); transient-limited qualifier on Outcome B's face; in-class re-charter limits stated |
| L01C-R4 | registry | P_positivity operationalization silently substituted | CONFIRMED | substitution disclosed (§3.3); trajectory-Gram PSD gate M-3 added (Bernstein reading); line scoped on its face; UNFORMULABLE-YET correctly withheld |
| L01C-R5 | registry | certify survival only where deletion bit | REFUTED | (outcome-rule quantifiers already correct; vacuity handled by X-1 conditioning) |
| L01C-R6 | registry | verdict faces amplitude-blind; Outcome A composable | CONFIRMED | amplitude scope on certificate faces; Outcome A per-property + per-(β,a); H3 falsified at full scope, finding scoped to failing legs; survivors mapped, never certified (§5) |
| L01C-R7 | registry | same band issue as L01C-4 | REFUTED | as L01C-4 |
| L01C-R8 | registry | early grid misses the actual collapse | CONFIRMED | log-anchored early-early grid {0.0005…0.045}, all on h₁ step boundaries, diagnostic-only (§2) |
| NF-1 | numerics | grid-on-boundary claim needs a mandated mechanism | CONFIRMED | integer-count stepping text frozen verbatim (§2) |
| NF-2 | numerics | RC-2 achievable with ~3300× headroom; could tighten | CONFIRMED | tolerance tightened 10⁻⁷ → 10⁻⁹ (~30× margin at binding leg) |
| NF-3 | numerics | RC-1 achievable by ~5 orders | CONFIRMED | kept at 10⁻⁶ |
| NF-4 | numerics | RC-4 achievable; don't tighten below ~10⁻¹¹ | CONFIRMED | kept at 10⁻⁹ |
| NF-5 | numerics | RC-3 unspoofable by rounding | CONFIRMED | kept |
| NF-6 | numerics | comparator crash-guard framing | REFUTED | (numerics all verified; guard already implied — made explicit via RC-5 ordering anyway) |
| NF-7 | numerics | runtime claim honest | CONFIRMED | kept (§6 updated for 38 trajectories) |
| L01C-F1 | honesty | sign-failure branches are theorem-impossible, misclassified as attackable (blocker) | CONFIRMED | RC-5 sign-identity halt gate over all grids, with scope conditions frozen (§3.2); positivity line's nonnegativity half labeled identity-held |
| L01C-F2 | honesty | X-1 misclassified as uncertain; draft's failure mechanism backwards | CONFIRMED | X-1 reclassified certification-grade; corrected persistence mechanism recorded, with the draft's error disclosed (§3.5); analytic band only in frozen text |
| L01C-F3 | honesty | "Outcome A live via the transient entering the window" overbroad | CONFIRMED | transient-exhaustion timing + ≲0.2-nat in-window budget vs ≈2.8-nat discriminant recorded (§3.5); Outcome A's §0 gloss re-grounded on the attackable gates |
| L01C-F4 | honesty | M-2 filed fully attackable; strong analytic structure omitted | CONFIRMED | rebound algebra + exact eigen-row identity 2.3 − φ₂/φ₁ = λ_min frozen (§3.5); β=0 legs identity-grade; finite-window openness precisely delimited |
| L01C-F5 | honesty | same audit-predicate defect as L01C-1; proposed conditional RC-2c | CONFIRMED | **subsumed**: the all-legs unconditional RC-2 is strictly stronger than the proposed conditional RC-2c and removes the post-result branch entirely; F5's worry (an Outcome-B run executing no audit) cannot arise |
| L01C-F6 | honesty | late-slope M-diag misreferenced to λ_min | REFUTED | verifier confirmed rev 2 already contains the fix (§3.6.ii, §4 M-diag); λ₂ ≈ 0.3401 supports the mode-mixture point |
| L01C-F7 | honesty | Outcome B slogan overreaches; β=0 legs miscounted | HALF-CONFIRMED | slogan rescoped to the tested phenomena with P_continuum/P_geometry visibly unclaimed (§0); the miscount half refuted (rev 2's leg roles already correct) |

## The quarantined preview values (adjudicating NOTHING)

In verifying feasibility and findings, panel agents integrated the
frozen system and previewed gate-relevant magnitudes. Per the F2
verifier's discipline ruling, the frozen charter carries analytic
derivations and bands only; the measured previews live here, labeled,
and **the single recorded run's artifact is the record — these numbers
adjudicate nothing and are never compared against gates**:

- X-1 amplitude-collapse deficits ≈ 0.846 (β=3, a=3) and 0.742
  (β=1, a=3); persisting ≈ 0.820 / 0.705 at τ = 40.
- Minimum gated r ≈ +1.229×10⁻⁹, at (β=3, a=3), τ = 40 — positive
  everywhere, consistent with the RC-5 theorem.
- Hardest-leg comparator: R_exp ≈ 1.874 < R_alg ≈ 4.845 →
  EXPONENTIAL-GRADE.
- D_act ≈ 0.029 (β=3) / 0.026 (β=1), attained near τ ≈ 3.5; the
  naive shape-defect confound measures ≈ 0.197 / 0.168 (why D_act,
  not D_shape, was frozen).
- RC feasibility: Richardson sup-rel ≈ 3.0×10⁻¹¹ at the binding leg;
  time-domain-vs-eigen ≈ 3.4×10⁻¹²; superposition ≈ 7.6×10⁻¹⁵;
  smallest true inter-record V-drop ≈ 12%.
- Transient structure at (β=3, a=3): x₁ crosses 0.3 near t ≈ 0.26;
  x₁(1) ≈ 0.074; in-window distortion budget ≈ 0.16 nats.
- λ₂(K_b) ≈ 0.34008 (the window-tail mode-mixture reference).
- **Not previewed anywhere: the trajectory-Gram spectra (M-3), the
  full 18-leg maps, the early-early collapse maps** — the fork's
  genuinely open content, named as such in charter §3.5.

## Standing

This record changes no verdict, moves no channel, and touches no red
gate. The charter that freezes alongside this record is the sole
adjudicating document; where this record and the charter differ, the
charter governs.
