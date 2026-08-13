# GRUT BUILD — consolidated banking + state-sync (overseer relay)

You are the build AI for the resurrected GRUT (the clean ResponsiveAI workspace), operating under CHARTER.md. This prompt transmits the verified verdicts from a full round of overseer pre-screens and two external specialist briefs (each adversarially verified). Bank EXACTLY what is below, at EXACTLY the stated tiers and calibrations; run the gate; report back. Where a calibration looks subtle, it is load-bearing — do not round it off. Nothing here is optional unless marked "optional".

These are theorems ABOUT GRUT-as-written, not claims about nature. Keep that scope on every bank.

## 0. Operating posture (unchanged)
- Tier every claim. The anti-laundering validator BLOCKS any net-positive rung sold as a derivation. Marked, not laundered.
- Directional-optimism guard, BOTH directions: be most suspicious of anything that strengthens GRUT toward "it works" — AND do not over-demote an anti-GRUT result past what was shown.
- FRONTIER-RESERVED — do NOT compute, approximate, or bank in-house: (i) the bath-microphysics / transport self-energy that would decide single-pole; (ii) the kinematic 4th-order S^4 Riegert/Paneitz a/c that would decide the alpha carrier. Specify and hand out only.
- Relay any tier graduation and any approach to the bath-Hilbert-space UP (to the overseer, via the user) before banking.

### 0a. WORKSPACE PRECONDITION (do this FIRST, before any bank)
This prompt targets the clean ResponsiveAI workspace. Confirm it actually contains the banking targets: GRUT_writeup.md, CHARTER.md, the registry module, and the conformalon source files (conformalon_q2_band.py, RESULTS_conformalon.md, two_scale_desitter.py). If GRUT_writeup.md / CHARTER.md are ABSENT, or you find yourself in a v2/v4 tree (v4/STATE.md, v4/registry.py present instead), STOP and relay to the overseer — do NOT default to banking into v4/WRITEUP.md or v4/registry.py (they are differently numbered and carry different content). The verifications below were quote-based; several named files were NOT present in the v2/v3 trees the overseer could see, so treat every "confirm in the workspace" as a real gate, not a formality.

### 0b. Tier vocabulary (map to the LIVE enum — do not invent a tier)
The registry Tier enum is exactly: ANCHOR, DERIVED, HOSTED, FORBIDDEN, OPEN, CONJECTURAL. "derived-pending" is NOT an enum member — it is a SUB-STATUS string attached to an existing Tier. Map as:
- mu_linear: Tier = DERIVED, sub_status = "no_go_export" (see Item 1).
- single_pole: Tier = ANCHOR, sub_status = "derived-pending" (see Item 3).
- rung9b_bridge: Tier = OPEN, sub_status = "settled-negative" (see Item 5).
If your workspace's enum differs, relay before banking — do not guess a mapping.

### 0c. Expected ledger this round (reconcile, do not recompute from scratch)
Read the current net BEFORE editing (baseline), apply EXACTLY these signed changes, then show before/after so nothing is absorbed:
- p_tt_ansatz: NEW assumed claim, +1 (a COST, not credit).
- mu_linear: Delta 0 (no derivation credit — selected, not derived).
- rung-9 anchor credit: SUSPENDED, -1 -> 0 (suspended, NOT deleted). This must appear as a visible before/after line, never folded silently into a single net number.
- rung9a_value: SHOWN conditional theorem carrying ZERO anchor credit going forward.
- single_pole: unchanged, Delta 0.
- rung9b_bridge: unchanged net (tier OPEN, sub-status sharpened only).
- conformalon thread: CLOSED, Delta 0.
Expected NET delta this round = +1 (the p_tt_ansatz cost) and the visible withdrawal of the rung-9 -1 anchor credit. Report the baseline net, the post-bank net, and confirm the validator is GREEN. If your computed net differs, STOP and relay — do not bank a different net than this.

## 1. mu_linear = 1 — DERIVED + sub_status "no_go_export"  (registry key: mu_linear; companion key: p_tt_ansatz)
- Tier = DERIVED, sub_status = "no_go_export". Frame as a no-go export: "GRUT forbids the mu=4/3 modification its own conformal coefficient would naively suggest — excluded by a separate-universe consistency no-go and falsified at ~32sigma by the low-l ISW excess — so linear cosmology = LambdaCDM (the mu_linear=1 SURVIVOR/selected branch)." It is NOT "derived-clean"; it is empirically SELECTED and a theorem-about-GRUT-as-written.
- RE-TIER / STRIKE OVER-CLAIM: if mu_linear is currently tiered plain DERIVED with "the framework's cleanest result" language (it is, in the standing registry), STRIKE the "cleanest result" / "derived-clean" wording and attach sub_status=no_go_export. "Confirm if already banked" means confirm the tier+framing MATCH this spec, not merely that the key exists.
- CONFIRM-OR-DO, both branches: If mu_linear is already banked — verify Tier=DERIVED, sub_status=no_go_export, the no-go-export framing, and that p_tt_ansatz exists at +1; reconcile any mismatch by UPDATING to this spec. If NOT banked — create it at DERIVED/no_go_export with the framing and register p_tt_ansatz (+1).
- Register the pure-TT projector ansatz as its OWN assumed claim p_tt_ansatz (+1).
- Ledger for item 1 is EXACTLY: mu_linear Delta = 0 (no derivation/anchor credit — it is selected, not derived); p_tt_ansatz = +1 (own assumed claim, a COST). This item nets NON-POSITIVE for GRUT — the validator must never see a derivation credit accrue to mu_linear ("we derived LambdaCDM" is a laundering trap).

## 2. rung-9 (alpha anchor) — SPLIT  (registry keys: rung9a_value, rung9b_bridge)
- rung9a_value (a/c = 1/3): tier SHOWN, but only as the CONDITIONAL theorem "IF the conformal mode is the IR carrier THEN a/c = 1/3" (KS 2011 / Duff), adopted as a dimensionless axiom. NOT a derived absolute anchor. rung9a carries NO anchor credit going forward (the SHOWN axiom is zero-credit).
- rung9b_bridge (that 1/3 normalizes the TT kernel): see Item 5 (Brief 2 settles its sub-status).
- Retire the dielectric (D = epsilon E) analogy as non-load-bearing (it presupposes the TT-ness it must justify). Record this as a verified-note / corroboration field on rung9a_value — NOT a new tiered claim, NO ledger delta.
- FIX the false docstring — match by TEXT, not bare line number (the workspace renumbers). Path: grut/derivation/phi_munu/linearized_ctp_action.py. The false claim spans the docstring at ~lines 449-451 ("the trace contraction (eta^mu nu eta^rho sigma P^TT) ... load-bearing for reproducing alpha_vac=1/3") AND the comment block at ~lines 460-466 ("the conformal-mode contraction gives the framework's alpha_vac = 1/3", with key conformal_mode_amplitude = sp.Rational(1,3) at 466). Replace the FALSE assertion with: the double-trace of the tracefree P^TT is identically zero, so 1/3 is a hand-pinned label / structural input, NOT a computed contraction output. Fix the WHOLE false-framing span (449-451 and 460-466), not just the value at 466.
- Suspend rung-9's -1 "anchor credit" (suspended, not deleted — see 0c). Sharpen ledger item #13 (alpha normalization).

## 3. single-pole — ANCHOR confirmed (Brief 1, Outcome 3a)  (registry key: single_pole)
- Tier UNCHANGED: ANCHOR, sub_status "derived-pending" — neither derived nor refuted. An independent referee-mode specialist found the minimal inputs do not determine the transport class (Outcome 3a = the pre-mapped "confirms anchor, name the missing input" branch). Do NOT demote this anti-GRUT result past what was shown — it is NOT refuted.
- Sharpen the named missing input to the TRANSPORT SELF-ENERGY Sigma controlling G_R = 1/(G0^-1 - Sigma).
- Bank the TWO-LEVEL frontier: (1) commit the system/bath partition -> yields only the FREE bath correlator (super-Ohmic, i.e. collisionless-AT-FREE-LEVEL) which by itself does NOT decide the fork; (2) Sigma additionally needs the bath's INTERNAL dynamics (graviton-graviton scattering / nonlinear mode coupling / Boltzmann) -> compute, read the low-omega scaling class: (Ohmic, Im G_R ~ eta*omega -> single-pole holds; non-Ohmic / Weinberg free-streaming power-law-tail kernel -> single-pole fails). Do NOT use "|omega|" / sub-Ohmic s<1 shorthand for the failure mode — that is one of the three RETIRED mischaracterizations (tidy to the Weinberg reading). Do NOT read free-level super-Ohmicity as the Weinberg free-streaming failure branch — the decision lives entirely in Sigma from the bath's INTERNAL dynamics. single-pole is therefore pending a MODELING COMMITMENT GRUT has not made, NOT a referee computation.
- This low-omega scaling class is FRONTIER-RESERVED: do NOT approximate Sigma or "read" the class off any in-house proxy. Specify and hand out only.
- DROP the "one number / one vertex decides it" framing AND every restatement of it. Verified loci in the v4 mirror (if mirroring): STATE.md line ~42-43 ("the **only** resolution is a real computation: derive ... <T_TT T_TT> from GRUT's z·T_TT vertex") and line ~73-74 ("(that single number decides single-pole)"). Confirm the string is actually present before "dropping" (do not report a no-op as a completed action). Replace with: single-pole is pending a MODELING COMMITMENT (the system/bath partition + the bath's internal dynamics), whose output is a one-bit low-omega scaling CLASS read off a FULL transport self-energy calc — not one number from one vertex.
- Bank three referee rebuttals as corroboration (NO tier change, NO ledger delta — as a verified-note field on single_pole): KMS != viscosity; de Sitter / Gibbons-Hawking != a colliding gas; Weinberg branch cut = an extra collisionless assumption. Tidy the "collisionless branch" (mischaracterized 3 ways across docs) to the Weinberg reading.
- Bank the PROOF, NOT the specialist's favorable prior ("the vacuum probably has finite transport coefficients") — ZERO evidential weight; and "finite eta" is strictly weaker than "single Debye pole".
- Sharpen ledger item #17 (collisionality) to match this two-level framing (the collisionality question is the ANCHOR's open input, decided only by the full transport calc).

## 4. conformalon closure — confirmed-WITH-CAVEAT  (registry key: conformalon thread, e.g. conformalon_q2 / the phenomenological-conformalon claim)
- Bank the phenomenological sub-thread CLOSED and Question-2 (w(z)-vs-alpha-shift compatibility) MOOT on magnitude — but LEAD with the w = +1/3 wrong-equation-of-state argument (Anderson-Molina-Paris-Mottola), which retires the thread independent of fluctuation magnitude.
- DEMOTE leg-1: Wess-Zumino / shift symmetry forbids only a Lagrangian m^2 sigma^2; the actual Starobinsky-Yokoyama killer is leg-2 (no bounded-below potential; e^{4sigma} is a monotone runaway). Do NOT present WZ as the protector.
- Carry the SECULAR factor explicitly: <sigma^2> ~ N/((4pi)^2 Q^2) (~1e-4 at N=60, Q^2~3000). State "too small at realistic N", not "never O(1)".
- KEEP section-8 OPEN: the gauge-invariant two-point <T_ab T_cd> tension is UNTOUCHED — this answer controls only ONE-POINT objects, which is WHY section-8 stays open. Add a line that <sigma^2> != <T_ab T_cd>. GUARD: when you mark the phenomenological sub-thread CLOSED, do NOT let that edit close or remove the section-8 <T_ab T_cd> open item — re-read section 8 after the edit and confirm the gauge-invariant two-point tension is still listed OPEN.
- BLOCKING source-number gate: BEFORE banking item 4 as confirmed, locate and re-read conformalon_q2_band.py, RESULTS_conformalon.md, two_scale_desitter.py and confirm 0.024 vs DESI 0.2 and the <sigma^2>~1e-4 number. If ANY file is absent in the workspace, do NOT bank item 4 as verified — relay to the overseer that the quote-based numbers are unconfirmed. (These files were not present in the v2/v3 trees the overseer could see; the verification was quote-based.)

## 5. alpha-bridge — settled-negative, NOT forbidden (Brief 2, O4)  (registry key: rung9b_bridge)
- Tier stays OPEN (open_negative); SHARPEN the sub-status to: "settled-negative — adopted phenomenological parameter, obstruction-backed, NOT FORBIDDEN, open to a new-identity rescue."
- Record the obstruction to the bridge (a/c = 1/3 normalizing the TT amplitude c_0) — exactly THREE obstructions, in order: PRIMARY projector orthogonality (trace = spin-0 vs TT = spin-2; g^munu P^TT = 0; no metric-built scalar->TT intertwiner); SECONDARY independent Ward identities; TERTIARY-and-independent UV-vs-IR no-RG-protection.
- SEPARATE supporting mechanism (NOT a 4th obstruction — do not over-count the negative): the GRUT-specific FDT/KMS alpha-cancellation. N(omega)/Im K^R(omega) = 2 coth(hbar omega / 2 k_B T) is alpha-FREE because c_0 = alpha is a COMMON PREFACTOR of BOTH N and Im K^R and cancels — FDT fixes shape/temperature but LEAVES the overall scale c_0 free (so FDT does not rescue the bridge either). Optionally bank this cancellation as a short verified note so it is not later mistaken for a restatement of projector orthogonality.
- Do NOT add a refuted branch; do NOT introduce a FORBIDDEN/no-go tier (impossibility-in-every-extension is NOT claimed).
- RECONCILE with the standing FORBIDDEN no-go: the existing FORBIDDEN claim ("no new propagating vacuum pole") is about the PROPAGATING-POLE question and is LEGITIMATE — it does NOT cover the bridge. Keep them as two separate claims; do NOT let the standing FORBIDDEN tier leak onto rung9b_bridge. The bridge is settled-NEGATIVE, not forbidden.
- alpha = 1/3 (the VALUE) is UNTOUCHED — NOT refuted; it keeps its conditional-theorem (ANCHOR-on-a-free-datum) support and remains the single adopted dimensionless axiom.
- The E4 carrier-identification front (the kinematic 4th-order S^4 Riegert/Paneitz a/c as an anomaly ratio, NOT a propagating EOM — clarifying gloss) stays SEPARATE and OPEN. Do NOT fold it into the bridge demotion (E4 != E8: P^TT annihilating the linear-scalar RESPONSE does not establish which mode CARRIES chi). AND do NOT let the bridge's settled-negative status prejudice the kinematic S^4 a/c front — it stays OPEN at full neutrality (no inherited negative weight).
- Tag the alpha-dependent exports R = sqrt(1+alpha), S = 12pi/alpha^2, Omega_Lambda as "conditional on adopted c_0/alpha". These exports INHERIT the SUSPENDED anchor credit — they may NOT carry derived-anchor weight while alpha is only an adopted dimensionless axiom; confirm in the ledger that no anchor credit flows to R/S/Omega_Lambda beyond what rung9a (conditional theorem) licenses. mu_linear = 1 is alpha-free and unaffected (stays the clean LambdaCDM export).

## 6. Do NOT
Over-demote to FORBIDDEN; fold E4 into the bridge OR let the bridge contaminate the OPEN S^4 front; bank the specialists' favorable priors; compute/approximate the frontier items in-house; move alpha up to derived/established or down to refuted; sell any net-positive rung as a derivation; let the standing FORBIDDEN propagating-pole no-go leak onto the settled-negative bridge.

## 7. Citation note
The section pointers used above are for the NEW ResponsiveAI GRUT_writeup.md: sec 3.1 = single-pole; sec 6 = ledger item #17 collisionality; sec 8 = open items. These do NOT transfer to the OLD v4/WRITEUP.md, which numbers differently: there sec 3.1 = alpha, sec 6 = 689Hz, sec 8 = scope. Do NOT bank by those OLD section numbers. Bank in the new doc. If you must mirror to v4, use the FILE LOCI, not section numbers: STATE.md:37-46 (and the line ~42-43 / ~73-74 "one number" passages), registry.py, mori_zwanzig_kernel.py.

## 8. Report back (structured, one-pass checkable)
- Validator: GREEN? Baseline net ledger, post-bank net ledger, and the explicit before/after line showing the rung-9 -1 anchor credit SUSPENDED (-1 -> 0, visible, not absorbed). Itemize: p_tt_ansatz +1; mu_linear Delta 0; rung9a SHOWN/zero-credit; confirm ledger item #13 (alpha normalization) and #17 (collisionality) sharpened.
- For each item 1-5: the registry KEY, the final Tier + sub_status, and a QUOTE-BACK of the load-bearing calibration token —
  - item 1 (mu_linear / p_tt_ansatz): "no-go export, not derived-clean; mu_linear Delta 0, p_tt_ansatz +1".
  - item 2 (rung9a_value): "conditional theorem, dimensionless axiom, NOT absolute anchor; zero anchor credit; docstring fixed at 449-451 + 460-466".
  - item 3 (single_pole): "two-level frontier; scaling CLASS not one number; Weinberg branch (not |omega|); refuted? NO".
  - item 4 (conformalon): "LEAD w=+1/3; leg-2 is the killer; section-8 OPEN; source numbers confirmed/relayed".
  - item 5 (rung9b_bridge): "settled-negative NOT forbidden; projector-orthogonality PRIMARY; FDT/KMS leaves c_0 free; alpha VALUE untouched; E4 separate".
- Which tiers/sub-statuses moved and to what.
- Confirm NO anti-GRUT result was over-demoted past what was shown: single-pole stays ANCHOR (not refuted); conformalon CLOSED is sub-thread-only with section-8 still OPEN (not fully closed); alpha-bridge stays settled-negative (not FORBIDDEN); alpha VALUE not -> refuted.
- Confirm the two frontier items are registered as external/OPEN, NOT computed: (i) bath microphysics / transport self-energy Sigma; (ii) kinematic S^4 Riegert/Paneitz a/c. State the registry home under which each is registered.
- Flag anything the gate caught (especially any laundering it blocked).