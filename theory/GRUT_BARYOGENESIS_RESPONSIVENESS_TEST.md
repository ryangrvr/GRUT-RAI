# GRUT Decisive Test — Baryogenesis: does the sector organize around responsiveness?

**Verdict: CONTAINER-SEAM.**

The baryon-to-photon ratio η_B ≈ 6.57×10⁻¹⁰ (+7.7% vs Planck 6.10×10⁻¹⁰) is real and machine-verified, but the GRUT factor in the formula — (2−R_B)/S_B — does **not** carry the asymmetry and does **not** use the canonical α-spine. The magnitude is set entirely by **hosted SM J_CP** × an **imported/asserted non-equilibrium K_neq**; the GRUT factor (2−R_B) is an O(1) dressing (=0.982) whose own documentation says so. R_B = 1.018 is a bespoke B-subscripted number, **not** the canonical R=√(4/3)=1.1547, and S_B = 4π×45 = 565.5 is **not** the canonical S = 108π = 339.3. The +7.7% match was *produced* by a documented S_B re-choice (the repo says so verbatim). GRUT hosts baryogenesis; it does not organize it.

This verdict was allowed to come back negative. It did.

---

## 1. The test

For each Part IV frontier the decisive question is **not** "is it solved." It is: *does the sector organize around responsiveness* — finding its place on the ladder **Q → F(t) → Responsiveness → Vacuum → Physics → Complexity → Observation** — *or does it require unrelated machinery bolted on from outside?*

A *container* hosts a result: it carries the right number but the structure producing it is adopted from elsewhere. An *explanation* generates the structure from the spine. For baryogenesis the make-or-break is sharp: η_B's formula **contains** a GRUT factor (2−R_B)/S_B — but (a) is R_B the canonical refractive R and S_B the canonical S, the *same* α-spine that gives Ω_Λ=(2−R)² and H_inf=(2−R)/(Sτ₀)? and (b) is that factor **load-bearing** — does the asymmetry genuinely vanish at R=1 so that R≠1 (a responsive-vacuum fact) *sources* the asymmetry? Or is it an O(1) dressing while J_CP×K_neq carry the magnitude?

---

## 2. The five-point placement (factor · provenance · consequence-vs-ansatz)

All values reproduced in `.venv` (Python 3.12.13); 20 baryogenesis tests pass (`test_baryogenesis.py` 13 + `test_baryogenesis_hardening.py` 7).

η_B = J_CP × K_neq × (2−R_B)/S_B (`grut/derived/baryogenesis/eta.py:54`), registered `baryogenesis_eta_b` **tier=computed** (`registry.py:1696–1722`), deps `r_canonical_path_g`, `ctp_action_structure`.

| Factor | Code (file:line) | Verified value | Sakharov condition | Provenance |
|---|---|---|---|---|
| **J_CP** | `eta.py:13` literal | 3.18×10⁻⁵ (PDG 2024 Jarlskog) | (2) C/CP violation | **HOSTED — SM/CKM input** (correctly labeled) |
| **K_neq** | `eta.py:14` literal | 1.19×10⁻² | (3) non-equilibrium | **IMPORTED/ASSERTED** — hardcoded; *not computed in code*; doc claims "α_eff×δT/T×v/T" but no such calc exists; `covariance.py:37` calls source "structural (EW crossover width, v/T)" ±50% |
| **(2−R_B)** | `eta.py:43–45,54` | 0.9818 (R_B=1.0182) | (2) via R≠1 path asymmetry | **GRUT factor — but cosmetic** (O(1) dressing; see §3) |
| **S_B = 4π·N_Weyl** | `eta.py:30` | 565.487 (=4π×45) | normalization | **GRUT factor — but NOT canonical S=108π=339.3** |
| **B violation** | (no factor) | — | (1) B violation | asserted structural (`z_target ∌ B`), not in the number |
| η_B product | `eta.py:54` | **6.5699×10⁻¹⁰** | — | **+7.703%** vs ETA_OBS=6.1×10⁻¹⁰ |

GRUT **hosts:** J_CP (SM), K_neq (imported freeze-out-style factor, asserted).
GRUT **supplies the form** (2−R_B)/S_B — but with bespoke R_B and a non-canonical S_B, and the factor is O(1).
**The magnitude** of η_B is carried by J_CP (1e-5) × K_neq (1e-2) / S_B (1/565) ≈ 6.7e-10; the GRUT factor moves it by <2%.

---

## 3. The make-or-break: is (2−R_B)/S_B the canonical α-spine, and is it load-bearing?

**No to both. Verified numerically in `.venv`:**

**(3.1) R_B is NOT the canonical R.** Route 1 computes R_B by decomposing the C_FINAL integers (99, 2π², 576·ln2·ζ₃) and re-weighting each by *baryonic field-content fractions* (F_FERMION=4/45, F_GAUGE≈0.104), then R_B = |c_b_cosmo/c_b_final| (`eta.py:32–45`). Result:
- **R_B = 1.018237**, vs canonical **R_REFRACTIVE = √(4/3) = 1.154701** and **R_ANOMALY = 1.15428**.
- R_B − R_REFRACTIVE = **−0.1365** (~12% off). It is a *separate B-subscripted number*, not the α-spine R.

**(3.2) S_B is NOT the canonical S.** S_B = 4π×45 = **565.487**; canonical S_CTP = 108π = **339.292** (`anomaly.py:142`). Ratio S_B/S_CTP = **1.6667 = 5/3**. Different normalization entirely (4×45=180 path-count vs 108).

**(3.3) The factor is an O(1) dressing — the magnitude is hosted.** Verified budget:
- log10 J_CP = −4.498, log10 K_neq = −1.924, log10(1/S_B) = −2.752, **log10(2−R_B) = −0.008** (i.e. ≈1).
- The smallness 1e-5 (J_CP) × 1e-2 (K_neq) / 565 = 6.7e-10 is set *before* the GRUT factor touches it.
- **The doc admits this** (`GRUT_V7_FULL.md:2269`): *"The (2−R_B) factor is O(1), and the smallness of eta comes from J_CP × K_neq."*

**(3.4) The "vanishes at R=1" claim is misleading.** The registry statement (`registry.py:1702`) says *"The asymmetry vanishes at R = 1 — the universe has nonzero baryon asymmetry because R ≠ 1."* But the algebraic zero of (2−R) is at **R=2, not R=1**. At R_B=1 the formula gives η = 6.69×10⁻¹⁰ (**+9.7%** — still a fine match). Across the entire R_B=1→1.0182 range the GRUT factor changes η by **<2%**. The asymmetry does not "vanish at R=1" in any load-bearing sense; (2−R_B) sits at 0.982 ≈ 1 and is nearly inert.

**(3.5) If you use the CANONICAL spine R, the fit gets WORSE.** Plugging R_REFRACTIVE=√(4/3) into the *same* formula gives η = 5.66×10⁻¹⁰ = **−7.3%** (vs +7.7% with R_B=1.018). So the formula explicitly does *not* route through the canonical α-spine; it uses a bespoke R_B tuned by the baryonic-fraction re-weighting that happens to land near +7.7%.

---

## 4. The numerology verdict on the +7.7% match

**A reverse-fit at the S_B step, riding two hosted magnitude-carriers — not an honest derived miss like the warm-relic 418×.**

- **K_neq is free at the ±50% level and uncomputed.** `eta.py:14` hardcodes 1.19×10⁻²; `crosscheck.py:164` and `covariance.py:36–37` both assign it **50% structural uncertainty** (±0.6×10⁻², "EW crossover width, v/T ratio"). A ±50% knob with no in-code derivation directly multiplies η_B. The doc's "Computed: α_eff×δT/T×v/T" (`GRUT_V7_FULL.md:2236`) has **no corresponding calculation in the repository** — it is asserted, not traced. This is the dominant freedom and it is not independently fixed.
- **The match was produced by an S_B re-choice — stated verbatim.** `GRUT_V7_FULL.md:2308–2309`: *"The correction that produced the match: The CTP path-counting normalization S_B uses ALL 45 SM Weyl fermions (S_B = 4π × 45 = 565.5), not just B-carrying quarks… The B-weighting conflated charge content with CTP path counting."* The normalization was changed *to land the number* — the defining move of a reverse-fit, and the repo says so.
- **R_B is not robust.** The two "independent" routes give R_B = 1.018 (Route 1) vs 5.6×10⁻⁵ (Route 2) — an **18,000× spread** — and η_B = 6.57e-10 (+7.7%) vs 1.34e-9 (+119%). Route 2 is excluded; Route 1 is the one that matches. A genuine spine constant does not come in two routes disagreeing by four orders of magnitude with the matching one selected.
- **Contrast with an honest miss.** The warm-relic 418× was a single clean derived number that came out wrong and was *reported* wrong — a real falsified prediction. Here, the only GRUT-distinctive degree of freedom in the magnitude (S_B, and the ±50% K_neq) was adjusted to land inside the band, while the spine R was *not* used because using it makes the fit worse.

Net: the +7.7% is not a clean prediction of the responsive vacuum. It is J_CP (hosted) × K_neq (imported, ±50%, uncomputed) / S_B (re-chosen to fit), with an O(1) GRUT dressing that the doc itself calls O(1).

---

## 5. Verdict

**CONTAINER-SEAM.**

η_B's *consequence* is real (6.57×10⁻¹⁰, +7.7%, 20 tests pass) and the formula *contains* a GRUT factor — but "the formula contains (2−R_B)/S_B" is not "the asymmetry descends from responsiveness." The decisive checks all fail:
- (2−R_B)/S_B is **not** the canonical α-spine: R_B=1.018 ≠ R=√(4/3)=1.155, and S_B=565.5=4π×45 ≠ S=108π=339.3.
- The factor is **not load-bearing**: it is O(1) (=0.982), moves η by <2%, and the doc itself says the smallness comes from J_CP×K_neq.
- The magnitude is **hosted/imported**: J_CP is SM/CKM, K_neq is an uncomputed ±50% non-equilibrium number asserted (not derived) in the doc.
- The +7.7% was **produced by an S_B re-choice** (stated verbatim), and using the *canonical* spine R makes the fit worse (−7.3%).

**Not PARTIAL.** PARTIAL would require the GRUT factor to be the canonical α-spine *and* load-bearing while only the magnitude leg is hosted — i.e. the structural backbone genuinely on the ladder. Here the structural backbone is itself off-spine (R_B≠R, S_B≠S) *and* cosmetic (O(1)), and the one tie that would put it on the ladder — using the canonical R — actively worsens the match. The seam points away from responsiveness, not toward it.

**One honest caveat keeping this off "hard negative":** the *Sakharov-condition mapping* is coherent and the *out-of-equilibrium idea* is genuinely GRUT-flavored. K_neq's narrative — the constitutive lag (the system cannot instantaneously follow z_target across the EW threshold) supplying non-equilibrium even for a smooth SM crossover (`GRUT_V7_FULL.md:2246–2248`) — is a *real* responsiveness mechanism for Sakharov condition (3), and it is the one place baryogenesis touches the CTP arrow. But it is only a *narrative*: K_neq is a hardcoded 1.19×10⁻² with no derivation in code and 50% admitted uncertainty. The idea is on-spine; the number is not.

**Where it sits on the ladder.** Off-spine. GRUT *hosts* baryogenesis: it borrows J_CP (SM CP), borrows/asserts K_neq (non-equilibrium), and dresses the product with an O(1), non-canonical (2−R_B)/S_B. It does not place baryon asymmetry on Q → F(t) → Responsiveness → Vacuum → Physics via the same R≠1 structure as dark energy — the dark-energy structure uses R=√(4/3) and S=108π; baryogenesis uses R_B=1.018 and S_B=4π×45, different numbers chosen for this sector.

**Comparison to the neutrino/flavor result.** Both are CONTAINER-SEAM, but baryogenesis is the **weaker** of the two — *less* organized than flavor. Flavor hosts an adopted Z₃/Yukawa ansatz, but that ansatz is **internally coherent and generative**: Z₃ → K=2/3, N=3, A²=N−1, the sharp non-extension to neutrinos (194.1 vs 33.9), the a_ν=1 boundary theorem, and a genuine falsifiable export (the normal-ordering preference). Its responsive route was even *tested* — the CTP fixed point returns a clean, honest wrong number (K=4/9 instead of 2/3), pointing definitively away from the spine. Baryogenesis has **no comparable structural export and no comparable internal scaffolding**: its GRUT factor is not merely off-spine but *cosmetic* (O(1), <2% of the magnitude); its non-equilibrium factor is uncomputed (±50%); its R_B is route-ambiguous to 18,000×; and — the sharpest tell, with no analog in flavor — substituting the *canonical* spine R actively **degrades** the fit (+7.7% → −7.3%). Flavor is off-spine but internally well-organized around its ansatz; baryogenesis is off-spine *and* assembled-to-fit. Flavor's seam at least points cleanly away; baryogenesis's seam points away *and* the headline export was reverse-fit via a documented S_B re-choice.

**Falsifiers / upgrade conditions.**
- *Kills the export:* a refined PDG/Planck η_B (registry.py:1716) outside the ~8% band, or a refined J_CP/K_neq driving η_B inconsistent with observation. (Note: CMB-S4 ±0.02e-10 will resolve the +7.7% at >20σ per `crosscheck.py:234–238` — but a 20σ deviation *falsifies* this prediction, it does not vindicate it.)
- *Upgrades CONTAINER-SEAM → PARTIAL/ORGANIZED:* (a) derive K_neq from the constitutive lag *in code* (close the α_eff×δT/T×v/T claim, removing the ±50% knob); **and** (b) show the load-bearing factor uses the *canonical* R=√(4/3) and S=108π (the dark-energy spine) rather than bespoke R_B=1.018 / S_B=565.5 — and that doing so *still* lands the observed η_B. As it stands, (b) fails by construction: canonical R gives −7.3%.

---

### Key files (absolute)

- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/derived/baryogenesis/eta.py` — J_CP/K_NEQ literals (13–14), F_FERMION/F_GAUGE field-content fractions (21–25), Route-1 R_B from re-weighted C_FINAL integers (32–45), S_B=4π×45 (30), η product (54)
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/derived/baryogenesis/crosscheck.py` — "free_params: 0" claim (50), K_neq ±50% sensitivity (155–166), CMB-S4 >20σ falsification (234–238)
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/foundation/anomaly.py` — canonical S_CTP=108π=339.292 (142–143), R_ANOMALY=1.15428 (95), C_FINAL/c_cosmo (74–155)
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/derived/cosmology/vacuum.py` — canonical R_REFRACTIVE=√(4/3) (17–21), H_INF=(2−R)/(S·τ₀) with S_CTP (22)
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/utils/covariance.py` — K_NEQ ±50% "structural" (36–37)
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/derived/flavor/koide_operator.py` — K_neq "has no charged-lepton analog … adding one would be ad hoc" (1513–1515)
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/theory/GRUT_V7_FULL.md` — §31 baryogenesis: K_neq "Computed: α_eff×δT/T×v/T" claim (2236, uncomputed in repo), "(2−R_B) is O(1), smallness comes from J_CP×K_neq" (2269), "the correction that produced the match" S_B re-choice (2308–2309)
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/toe/registry.py` — `baryogenesis_eta_b` computed, "vanishes at R=1" statement (1696–1722)
