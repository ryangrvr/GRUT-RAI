# Handoff

## State
**On branch `main_v3` (the GitHub default; v3.0.0.dev0). v2 retired at tag `v2-final`.**
v3 = GR-limit dilatation redundancy broken by one scale L₀=cτ₀≈12.85 Mpc; pillars Q (CTP, proven) +
F (finite memory, postulated); **F breaks D**; **μ_linear=1 → linear cosmology = ΛCDM**.

**The v3 dark-sector AUDIT PHASE (Tests 01–05) is COMPLETE and FROZEN** (tag `v3-audit-complete`,
local; intermediate tag `v3-audit-checkpoint` = Tests 01–04). It compressed the dark sector from
4 mechanisms to **one surviving channel (C5a, W²) + one scale (a₀) + one decisive computation (K⁽²⁾)**.
- T01: dielectric Ω_dm=1/3 + linear enhancement → RULED OUT (omega_dm_equals_alpha → open_negative).
- T02: C5b gate frequency → ASSUMED. T03: C5b gate magnitude → REFUTED (~1/√N).
- T04: C5a (W²) → UNDETERMINED (sign ✓, scaling ✓, magnitude open).
- T05: reduced C5a to the single symbolic K⁽²⁾ computation (`undetermined_needs_symbolic`; soft lean
  toward local-scale → galaxy-marginal, but a cluster ~100× overshoot). Registry:
  `c5a_weyl_squared_dark_sector` (conjectural). Docs: `theory/GRUT_V3_TEST_0[1-5]_*.md`.

## CONSTRUCTIVE phase flagship K⁽²⁾ — RESOLVED & BANKED (June 2026)
Full record `theory/GRUT_V3_K2_DERIVATION.md`; module `grut/derivation/phi_munu/second_order_kernel.py`
(verify() 6/6) + test `tests/derivation/phi_munu/test_second_order_kernel.py` (9/9).
- **A**: W² is the UNIQUE dynamical O(2) operator; E₄ topologically dormant (a-anomaly, NOT No-Go);
  Ricci forbidden.
- **B** (wf whbpphrbb + closure wgzzxunwo): **scale L=L₀** forced — K⁽²⁾(ω,k)=σ·α·χ(ω), no 1/k² pole
  (local causal kernel = polynomial in k²; can't make the 1/∇² a local-r scale needs).
- **C** (wf wq1lz8509 + my direct recompute): **magnitude VIABLE, O(1–100)** at galaxy scales. The
  workflow's "1e-27 ⇒ dies" was TWO BUGS — (1) geometric ρ_eff [1/L²] ÷ SI ρ_baryon [kg/m³] dropping
  c²/G≈1.35e27 (THAT is the fake 1e-27); (2) W²=48(r_s/r)⁶ not 48(GM/c²)²/r⁶. L₀ ≈ weak-field curvature
  radius r/√Φ ~ tens of Mpc. CAUGHT before banking.
- **D**: **shape WRONG (decisive)** — ρ_eff ∝ W² ∝ ρ_baryon² ∝ 1/r⁴ (slope ≈ −3.9) vs the −2 a flat
  curve needs; σ scales magnitude only. → C5a is right-magnitude/wrong-shape, NOT the DM halo.
**VERDICT: GRUT has no derived DM mechanism reproducing halos; dark matter = HOSTED input (derived a₀,
μ_linear=1). Math survives, ontology changes.** Registry `c5a_weyl_squared_dark_sector` → open_negative
(+ ledger entry; 23/23 1:1, suite green).
**Test 06** (wf wo7mvnscu; `theory/GRUT_V3_TEST_06_PROFILE_THEOREM.md`): the user asked whether the
1/r⁴ profile failure is a theorem or an artifact of ρ_eff∝W². ANSWER: **theorem.** All 3 tensor routes
(scalar W², Bach ∇∇C⇒∇²ρ, TT-projected) → ρ_eff∝1/r⁴; the P^TT k_ik_j/k² loophole is CLOSED (degree-0
in |k|, not 1/∇²; K⁽²⁾ k-independent); shallowing to 1/r² needs the 1/∇² locality forbids. 3/3 incl. a
revive-skeptic agree. Module now 8 verify legs (+bach_route_isothermal_slope, tt_projector_is_inert);
test file 11 tests. The dark-sector frontier is now provably CLOSED within the local/causal/No-Go kernel.
**V3 MAP UPDATED** to match: `grut/v3/picture.py` step 6 + new `DARK_SECTOR_STATUS` ("CLOSED pending
covariant review"), summary(), and verify legs (`dark_matter_mechanism_closed`,
`no_dark_matter_channel_in_open_frontiers`); OPEN_FRONTIERS now = α-selection, L0→0, SM-closure, C5c-as-
non-DM-GW-signature; test `tests/v3/test_picture.py::test_dark_matter_mechanism_is_closed`. 76 tests green.
**PRECISION FIX (caught a near-overclaim):** "ρ_eff∝ρ_baryon²/baryon²-tracing" was imprecise — verified
numerically that ρ_eff∝(Weyl)²∝(ρ−⟨ρ⟩)² is 1/r⁴ interior, 1/r⁶ outskirts (exterior tidal), and the
ratio to baryons can RISE outward for truncated disks (so it does NOT vanish with baryons). Corrected
in Test 06 doc, picture.py, registry. Verdict unchanged/strengthened (even steeper = more wrong shape).
Final adversarial review (wf wb8n33cbp): CLEAN — 3/3 independent re-derivations confirm (L₀=12.85 Mpc,
galaxy ratio 52.9, slope ≈ −4, c²/G forensics); both audits found no overclaim/inconsistency, registry/
ledger 1:1, verdict fair. **Flagship FULLY CLOSED.**
1. Other frontiers (post-flagship, no dark-sector moratorium issue since C5a is resolved): α-selection
   (4th-order Riegert a/c); the L₀→0 underlying-redundancy proof. Both were already open pre-flagship.
2. GIT: Tests 01–05 ARE committed locally (commit 2954772; main_v3 ahead of origin by 2, NOT pushed).
   The entire K⁽²⁾ constructive-phase work is UNCOMMITTED in the working tree (new: second_order_kernel.py,
   its test, GRUT_V3_K2_DERIVATION.md; modified: registry.py, ledger.py, GRUT_V3_CONSTRUCTIVE_PHASE.md).
   PUSH + COMMIT both HELD pending the user's call (no commit/push without an explicit ask).
2. **MORATORIUM (active):** propose NO new dark-sector mechanism until K⁽²⁾ is computed (re-spreading
   would reproduce the v2 mechanism-accumulation failure the audit cured). If C5a dies → dark matter
   is a hosted input (with a derived a₀); not a cue to invent a fifth mechanism.
3. Other open frontiers (after / parallel, not dark-sector): α-selection (4th-order Riegert), the
   L₀→0 redundancy proof.

## v3 RE-AUDIT SWEEP — COMPLETE (June 2026, wf wutugktl0)
Re-audited the ~70 v2-inherited claims (2 lenses: ωτ₀ regime + math-survives-ontology), 9 sectors,
adversarial 2nd pass. 51 kept, 20 re-tiered. Applied (registry+ledger, full suite GREEN 3227 passed):
- **→ open_negative (+5 ledger, now 28/28 1:1):** `alpha_vac_derivation` (THE headline — α=1/3 is a
  POSTULATE not derived; "vacuum impedance=1/d" ungrounded; conditional KS-2011 verified but antecedent
  unproven), `bandwidth_integral` (ruled-out linear branch), `modified_linear_growth_first_look` (32σ
  ruled out), `kibble_zurek_dm_route` (retracted post-Test-06), `r_path_d_majorana` (rejected SM alt).
- **→ conjectural (6):** r_max_ricci_saturation, rho_max_universal, r_path_d_dirac, phi_munu_frw_explicit_
  construction, constitutive_growth_poisson_closure, tau_micro_thermal_scale (mechanism/scope unproven).
- **→ anchored (5):** koide_k_2_over_3, h_0_prediction, tau_0_cross_consistency, framework_axioms_locked,
  omega_lambda_prediction (consequences of empirical anchors, not first-principles — I corrected the
  enum which lacked an "anchored" demotion target).
- **→ computed (promote 1):** neutrino_hierarchy_z3_nh_prediction (a_ν=1 derived, Corr #29).
- Reframed contradictory statements; fixed test_coherence fixture (alpha_vac→gr_recovery).
**α=1/3 RESOLVED (user chose "both"):** `alpha_vac_axiom` (NEW, foundational) holds the adopted axiom
("α=1/3 is GRUT's single dimensionless axiom; conditional KS-2011 verified"); `alpha_vac_derivation`
(open_negative + ledger) tracks the OPEN first-principles derivation (Riegert closure + IR-carrier
antecedent). FINAL: 116 claims — foundational 4, computed 46, anchored 18, conjectural 10, open_negative
28 (1:1 ledger), meta 10. Full suite GREEN (3227 passed pre-axiom; 247 toe/conformal post-axiom).
**Registry is now a FULLY-AUDITED source of truth → ready to write the v3 ToE document against it.**

## v3 ToE DOCUMENT — BUILT (June 2026)
`theory/GRUT_TOE_V3.md` — the v3 Theory-of-Everything. 4 parts: I Picture (Q/F/D, the one axiom α, the
scale τ₀), II Forward build (no-gos → μ_linear=1 → certified universe), III Sectors (cosmo params,
decoherence 689Hz=primary falsifier, saturation/BH, R-routes, flavor/Koide hosted, measurement/QM, the
CLOSED dark sector w/ full K² + Test 06 theorem), IV Honesty (28-entry ledger, V2→V3 changes, falsifiers).
EVERY claim stated at its audited tier; all 58 claim-id refs cross-checked valid against the registry.
NOT yet built (offered, the user's call): the publication/upload version (foreword + formatting) and the
PDF (uploads/ pipeline) — a publication step, held with the push. Per-chapter depth references the backend.

## v3 ToE UPLOAD (reader's edition) — BUILT (June 2026)
`uploads/GRUT_TOE_V3_upload.md` — the human-facing, unified-story edition (~11.4k words, 8 chapters +
foreword): Foreword/The Question → The One Idea → The Responsive Vacuum → The Universe That Falls Out →
The Dark-Matter Detective Story → How To Kill It (Predictions) → The Rest of the World, Honestly → The One
Assumption & the Honest Frontier. Drafted by wf w50klzrt5 (8 parallel sections, strict honesty-tiering),
woven by me, adversarially reviewed by wf w296ehsal (accuracy/comprehensibility/honesty); all major
findings fixed (dark sector "unresolved"→"closed"; H₀/Ω_Λ anchored-vs-zero-param clarified; CTP/anomaly/
GH/Path-G glossed for lay readers). Tier-accurate, reader-comprehensible.
**EDITORIAL REVISION (June 2026, user brief — constraint-focused/anti-salesmanship):** reframed around the
AUDIT as central character; foreword now leads with "the framework forbade its own dark-matter mechanism
(Test 06 locality theorem) — survived by rejecting its most attractive prediction"; added **V3-at-a-Glance
status table** (survives/refuted/open) + **Three Pillars section** grading Q=established / F=postulated /
D=PARTIAL (not a proven symmetry — "finite memory acts as the controlled breaking"); demoted
"distinguishability" to shorthand for Q∩F∩D (not an axiom; no info-theoretic overclaim); added dissipative-
strongly-correlated-systems as ANALOGY only; thesis stated as "current organizing interpretation," not proven.
~12.3k words.

## v3 ToE PDF — BUILT (June 2026)
`uploads/GRUT_TOE_V3.pdf` (29 pp, 0.28 MB) via NEW `uploads/generate_pdf_v3.py`
(`uploads/pdf_venv/bin/python3.12 uploads/generate_pdf_v3.py`). Reuses the v2 machinery (imports
`generate_pdf` for fonts/tables/code/equations/inline/header-footer/ChapterMarker); adds: title page,
**interactive** = PDF outline/bookmarks (42 items: chapters+subsections) + clickable TOC + clickable
zenodo URL, and a **chapters-only TOC with page numbers** (10 entries, p.4–25). Preprocess strips the
md title block, promotes ##→# (chapters, page-break each) / ###→## (subsections). KEY GOTCHA fixed:
multiBuild reuses the template across passes, so the bookmark/TOC key counter MUST reset in
`beforeDocument()` (else keys drift each pass → "Index entries not resolved after 10 passes"). Also:
printed TOC is chapters-only (subsections in sidebar only) to avoid multi-page-TOC boundary oscillation.
Title page visually verified (sips→png); glyphs clean; build has no render warnings.
**v3 PDF FIXES (June 2026, user-reported):** (1) expanded the dark-matter VERDICT section in the upload
md (physical intuition for the 1/r⁴-vs-1/r² shape failure, the inverse-Laplacian/locality reasoning,
what "hosted input" honestly means, the escape route); (2) FONT glyphs ∩ ⁽ ⁾ were tofu (□) — added to
the DejaVuSerif fallback via monkeypatch in generate_pdf_v3.py (g._SERIF_FALLBACK|=…); (3) $$ EQUATIONS
fell back to raw-LaTeX text because matplotlib mathtext can't parse unicode Greek/sub/superscripts —
added a unicode→LaTeX preprocess (_uni_to_tex) monkeypatched onto g._latex_preprocess; now 6 image
XObjects (3 eqs+masks), verified rendering; (4) HEADER poke-out (previous chapter title showing behind
the new one on chapter-opening pages) — enlarged the white-out rect in afterFlowable (y=PAGE_H-0.715in,
h=0.205in, w=0.66·content) to fully cover ascenders/descenders; verified worst-case (long prev/short new).
PDF rebuilt: 28pp, 0.28MB, all interactivity intact.
**INTERIOR-PAGE VERIFICATION (the clean way):** `brew install poppler` FAILS on this box (macOS 12 =
Homebrew Tier-3/unsupported; a gobject-introspection dep won't build). The working renderer is
**pypdfium2** (self-contained wheel, no system deps) installed into pdf_venv
(`pdf_venv/bin/python3.12 -m pip install pypdfium2` — NOTE: the venv `pip` script has a stale shebang
from a move, so use `python3.12 -m pip`). Helper: `uploads/render_pages.py FILE.pdf [pages...]` → PNGs in
/tmp. Verified pages 2/8/11/13/17/18 of GRUT_TOE_V3.pdf: TOC w/ page numbers ✓, ∩ renders (p.11 "Q∩F∩D") ✓,
χ equation as math image (p.13) ✓, header poke-out gone (p.17) ✓, expanded verdict + all glyphs (p.18) ✓.

## v3 ToE doc — PROFESSIONAL-TONE + TECHNICAL-BRIEF PASS (June 2026)
`uploads/GRUT_TOE_V3_upload.md` now ~24.5k words, 65-pp PDF. wf wmp6d57mg (9 chapter agents): lifted tone to
professional-scientific, appended a "### Technical Brief" (derivations) to all 9 chapters, proposed 27
figures → `theory/GRUT_V3_FIGURE_PLAN.md` (NOT rendered, per user). **CRITICAL LESSON: the agent-written
technical briefs CONFABULATED math** — verified by wf wjeuyeo2d (adversarial math-check, 1 skeptic/brief):
found 15 issues. Fixed (sympy/backend-confirmed): the α a/c derivation (agent gave 7/6; correct a=1/360,
c=1/120 ⇒ 1/3); Im[χ] sign (was −, correct +ωτ₀/(1+(ωτ₀)²)) ×5; pole ω=i/τ₀→−i/τ₀; χ≈−i/(ωτ₀)→+i/(ωτ₀);
Ω_Λ=(H_inf)²→(H_inf/H₀)² and the false "(2−R)²=0.6886" (it's ≈0.71; 0.6886 is anchored); decoherence
Λ=G²m⁴/(12π²c⁵ℏτ₀) / Gm²/(ℏc⁵R²) → correct Λ=Gm²S(l/R)/(ℏl), S=min(1,(l/R)³/6); regime labels; a fabricated
claim-id `boundary_operator_no_conformal_enhancement`. 3 were FALSE POSITIVES (δ²S_IF not present; χ-α
convention; MW "~62" correct for 6e10 not the verifier's 1e11). All fixes rendered+verified via pypdfium2
(pages 18/40/50). **TAKEAWAY for future briefs: ALWAYS run an adversarial math-check before banking
agent-derived equations.**

## v3 ToE FIGURES — BUILT + EMBEDDED (June 2026)
16 figures (deduped from the 27-plan) in `uploads/figures_v3/*.png`, built by wf wv3tvmemz (7 agents,
shared style + verified formulas) then REVIEWED by me. As with the math pass, agent figures needed fixes:
I rebuilt 5 (`fig_profile_mismatch` had a spurious vertical spike at the 1/r⁴→1/r⁶ break; `fig_susceptibility`
annotation overlapped the legend; `fig_bh_saturation` label occluded; `fig_neutrino_hierarchy` ✗ was a
missing-glyph tofu → drew a red X; `fig_dilatation_breaking` annotation/palette). Builder: `_fix_figs.py`.
Embedded via NEW `parse_md_with_images()` in generate_pdf_v3.py (renders `![cap](figures_v3/x.png)` as
centered, auto-numbered, KeepTogether figures w/ caption). 16 refs inserted at heading anchors in the md.
PDF rebuilt: **74 pp, 2.04 MB, 16 figures embedded** (verified pp.31/50/55 render cleanly), interactivity
intact (68 bookmarks, clickable TOC). Review tooling: `uploads/render_pages.py` (pypdfium2) + contact sheets.
TAKEAWAY (same as math pass): always review agent-generated figures — 5/16 had real bugs.

## Next (open, user's call)
1. (Figures done + embedded.) Optional: a few schematics have minor crowding (neutrino title/headers) — polish if desired.
2. Commit/push still HELD — the user's call (push only on explicit release).
2. Genuinely-open frontiers (never dark-sector): α first-principles derivation (4th-order Riegert);
   the L0→0 redundancy proof; the 3-loop R-route (tji_7_4) numeric closure.

## Context
- **Holding the PUSH** (user: build more before pushing). main_v3 is on GitHub at the v3-build commit;
  ALL of Tests 01–05 are committed locally on main_v3, NOT pushed.
- **Verification workflows must be read-only** (`agentType:'Explore'`). (A non-Explore skeptic edited
  rotation_curves.py in T02 — reviewed/kept; lesson applied for T03–T05.)
- Discipline: adversarial verification; survivors are constraints + honest no-gos; recurring signature
  "math survives, ontology changes." Hold any clean positive to the same check.
- python3.12 for code/tests; uploads/pdf_venv/bin/python3.12 for PDF builds. v2 book/PDF frozen.
