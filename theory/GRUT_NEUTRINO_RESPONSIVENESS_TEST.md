# GRUT Decisive Test — Neutrinos / Flavor: does the sector organize around responsiveness?

**Verdict: CONTAINER-SEAM** (with a genuine, falsifiable *pointer* — not a closure).

The flavor sector's *consequences* are real and machine-verified, but the *structure that produces them* (the Z₃ circulant operator, the amplitude a=√2, the scale M₀) does **not** descend from the responsive framework. The repo's own honesty layer says so at its highest tiers: the flavor mechanism is registered `open_negative`, the responsive (CTP fixed-point) route was tried and returns a **NO-GO**, and the framework summary states "Flavor/Koide sits OUTSIDE the vacuum-response scheme (hosted)." This is the failure mode the test exists to detect — and it is self-reported, not hidden.

---

## 1. The test

For each Part IV frontier the decisive question is **not** "is it solved." It is: *does the sector organize around responsiveness* — finding its place on the ladder **Q → F(t) → Responsiveness → Vacuum → Physics → Complexity → Observation** — *or does it require unrelated machinery bolted on from outside?*

A *container* hosts a result: it carries the right numbers but the structure producing them is adopted from elsewhere. An *explanation* generates the structure from the spine. For neutrinos the make-or-break is sharp: the consequences (Koide K=2/3, the normal-ordering preference, the mass spectrum) genuinely *follow from* the Z₃ circulant — but does the Z₃ circulant **itself** descend from responsiveness, or is it a flavor postulate GRUT contains but does not generate?

This verdict was allowed to come back negative. It did.

---

## 2. The five-point placement (content · tier · consequence-vs-ansatz)

All values reproduced in `.venv` (Python 3.12.13); 194 flavor/neutrino tests pass.

| Item | Tier (file:line) | Verified value | Consequence or ansatz? |
|---|---|---|---|
| **Koide K=2/3** (charged leptons, empirical) | `koide_k_2_over_3` **anchored** (registry.py:2778) | K_emp = 0.6666605; dev from 2/3 = 0.0009% | KNOWN — empirical input |
| **Z₃ circulant operator** √mₖ = M₀(1+a·cos(θ+2πk/3)) | `koide_z3_circulant_structure` **computed** (registry.py:2800) | K=2/3 to machine precision at a=√2, N=3 | **ANSATZ — the postulate** |
| K=2/3 from Z₃ | inside above | Kₙ(a)=(1+a²/2)/N; =2/3 only at a=√2 | DERIVED *consequence* of the ansatz (a=√2 tuned) |
| N=3 selection | inside above | Kₙ=2/N is θ-independent ∀N≥3; value 2/3 selects N=3 by matching empiricism, not by uniqueness | Consequence *conditioned on the empirical match* |
| **Charged-lepton Z₃ ⇏ neutrinos** | `charged_lepton_z3_does_not_extend_to_neutrinos` **computed** (registry.py:2874) | min Δm²_atm/Δm²_sol = 194.1 vs observed 33.9 (~6× too large) | CONSTRAINS / FORBIDDEN — sharp structural negative |
| **NH prediction + Σmν** | `neutrino_hierarchy_z3_nh_prediction` **anchored** (registry.py:2918) | m=(0.8, 8.7, 50.2) meV, Σ=59.6 meV, θ=18.9°; IH at boundary | DERIVED consequence of a_ν=1, anchored to NuFIT Δm² |
| **a_ν=1 uniqueness** | `neutrino_z3_coupling_a_equals_1_uniqueness_theorem` **computed** (registry.py:2975) | boundary-gap √3·√(a²−1)=0 exactly at a=1 → K_ν=1/2 | DERIVED (structural; internal to the Z₃ ansatz) |
| **θ=2/9 candidate** = K·α_vac | `koide_theta_2_over_9_uniqueness` **computed (scan) / OPEN (mechanism)** (registry.py:2830) | dev 4.62 ppm, 56× inside PDG window | CANDIDATE IDENTITY — numerical, not derived |
| **M₀** (GeV^½ scale) | `koide_phase_4_open_negative` **open_negative** (registry.py:2429) | fitted 0.560 GeV^½; native μ₀=ℏ/τ₀≈5e-31 eV → ~20-order gap | FREE FIT — no foundation anchor |
| **Flavor mechanism** | `koide_phase_4_open_negative` **open_negative** (registry.py:2429) | — | **OPEN NEGATIVE** |

GRUT **explains (DERIVED):** K=2/3, N=3, the a=√2 unification (A²=N−1), the NH preference + Σmν≈60 meV, a_ν=1 — *all conditional on the Z₃/Yukawa ansatz.*
GRUT **constrains (FORBIDDEN):** charged-lepton Z₃ does not extend to neutrinos (194.1 vs 33.9).
GRUT **hosts:** the Z₃ circulant, a=√2, M₀ — adopted, not generated.
**OPEN:** the mechanism that selects Z₃, M₀, θ, a=√2.

---

## 3. The make-or-break: does Z₃ / M₀ / θ descend from responsiveness?

**No.** The repo states it three independent ways, and the one quantitative test of the responsive route returns the wrong number.

**(3.1) The Z₃-circulant shape is a *conjecture* about the fixed point, not derived from it.** The CTP fixed-point condition z*=z_target[z*] is native GRUT, but V7 §29 marks the *flavor* structure of z_target as "the missing object." Both functions that would compute the operator from the fixed point — `ctp_fixed_point_residual` and `flavor_jacobian_at_fixed_point` (`koide_operator.py:227–260`) — require the caller to *supply* F_spatial/F_temporal because V7 does not specify them for three flavors. The Z₃-circulant Jacobian is **Conjecture F1 — HYPOTHESIS** (`derivation_attempt()` returns `V7_conjecture_F1: HYPOTHESIS (unchanged)`, `V7_section_29: MAPPED (unchanged)`).

**(3.2) The responsive route was tested and is a NO-GO — it points *away* from responsiveness.** `fixed_point_amplitude_nogo()` (verified): GRUT's self-referential impedance balance 2ρ = α_vac = 1/3 gives **K = 4/9 = 0.4444, not 2/3** — a ~50% miss. The Koide amplitude A=√2 sits at **4.24× α_vac**. Verdict string returned by the code: *"NO-GO: GRUT impedance gives K=4/9, not 2/3; Koide needs equipartition (impedance 1, not α_vac=1/3); amplitude is Yukawa-input."* The conclusion: *"K=2/3 and θ=2/9 are NOT derivable from the GRUT constitutive fixed point… the amplitude is irreducibly Yukawa-input."*

**(3.3) The amplitude carries the physics, and it is hosted.** Z₃ fixes only the *form* (θ-independence of K), not the *value*; the value needs a=√2, which is external Yukawa input (`KOIDE_AMPLITUDE_UNIFICATION.md`). This *corrected a V7 over-claim* ("Z₃ forces K=2/3" → false), so the honesty is real and recent.

**(3.4) M₀ is a hard free fit.** Native scale μ₀=ℏ/τ₀ ≈ 5e-31 eV vs fitted M₀=0.560 GeV^½ → ~10^19.4 gap. The code's own conclusion: *"Without an additional mass anchor (Λ_QCD, v_EW, or v_dark) M₀ cannot be derived from the foundation alone."*

**(3.5) The neutrino extension is internal to the ansatz, not descended.** The NH prediction is anchored to NuFIT Δm² "conditional on the postulate a_ν=1"; a_ν=1 follows from a Z₃ boundary-degeneracy argument plus a "suggestive" channel-counting reading whose full anomaly derivation "remains a deeper research question." This is organized *within* the adopted Z₃ structure — not on the Q→F(t)→Responsiveness ladder.

---

## 4. The numerology verdict on θ = 2/9 = K·α_vac

**Statistically real as a match; mechanistically decorative as a tie.**

- **Real:** `koide_theta_uniqueness_verdict()` — θ_mod = 0.22222 rad vs 2/9 = 0.22222, dev = **4.62 ppm**, **56× inside** the 258 ppm PDG τ-mass window; 2/9 is the unique best rational approximant for all denominators 9–193; nearest competitor 43/194 at 2572.7 ppm = **557× worse**; `is_numerology = False`. By the framework's reject-sub-1%-non-distinctive bar this is **not** a sub-threshold coincidence.
- **Cosmetic for the spine question:** the same module returns `test_T1_z3_algebraically_selects_theta = False` (Z₃ gives K=2/3 for *any* θ) and `algebraic_derivation_exists = False`. α_vac enters θ=K·α_vac *only after* K (itself requiring the tuned a=√2) is assumed. It decorates the adopted structure; it does not generate it.
- **The tie is even thinner than it looks.** Because K = 2/3 = 2·(1/3) = **2·α_vac exactly** (verified `K − 2·α_vac = 0.0`), the product **K·α_vac ≡ 2·α_vac² = 2/9** algebraically. `survey_candidate_relations()` lists *both* "K·α_vac" and "2·α_vac²" at the identical 0.00046% deviation. So the "tie" brings in only **one** responsive constant (α_vac), not two independent ones — the apparent two-constant link is an algebraic illusion.

Net: a statistically-real but mechanistically post-hoc candidate identity, carrying a single α_vac, layered on an adopted Z₃ / a=√2 / M₀ ansatz whose responsive route returns the *wrong* number (4/9).

---

## 5. Verdict

**CONTAINER-SEAM.**

The consequences (K=2/3, N=3, the NH preference, Σmν≈60 meV, a_ν=1) genuinely follow from the Z₃ circulant — but that is *"a consequence of Z₃,"* not *"Z₃ descends from responsiveness."* The Z₃ circulant, the amplitude a=√2, and the scale M₀ are an **adopted Yukawa ansatz that GRUT hosts and does not generate.** The one tie to responsiveness, θ=2/9=K·α_vac, is statistically real but mechanistically decorative (and collapses to a single α_vac via K≡2·α_vac); the responsive route to the structure itself — the CTP fixed-point impedance — was tested and returns 4/9, actively pointing toward external Yukawa input.

**Not PARTIAL.** PARTIAL would require the open seam to *point toward* responsiveness as a plausible source. The repo's own work closes that door: the fixed-point route returns the wrong number, and the conclusion is explicit that the amplitude is irreducibly Yukawa-input. The seam points *away* from the ladder, not toward it.

**One honest caveat keeping this off "hard negative":** the consequences cohere *internally* (Z₃ → K=2/3, N=3, A²=N−1, the sharp non-extension at 194.1, the NH preference, the a_ν=1 boundary theorem). The sector is internally well-organized — just organized around an **adopted Z₃/Yukawa ansatz**, not around responsiveness.

**Where it sits on the ladder.** Off-spine. GRUT *hosts* neutrinos (core-chain link E11 is "DOTTED / reachability only"; the framework note locates Flavor/Koide "OUTSIDE the vacuum-response scheme"). It does not place them on Q → F(t) → Responsiveness → Vacuum → Physics.

**The open mechanism seam.** What selects Z₃, M₀, θ, and a=√2 remains `open_negative`. The responsive candidate (the multi-flavor CTP fixed point, Conjecture F1) is a HYPOTHESIS that, where tested quantitatively, fails.

**Falsifiers / upgrade conditions.**
- *Kills the prediction:* a measured **inverted ordering at >5σ** falsifies the NH-preference export (and the a_ν=1 chain it rests on).
- *Upgrades CONTAINER-SEAM → ORGANIZED:* a genuine derivation of the **Z₃-circulant Jacobian + the amplitude a=√2 from the CTP fixed point** (closing Conjecture F1 and yielding K=2/3 rather than 4/9), or a foundation-anchored derivation of **M₀** that closes the ~20-order gap. Either would move the sector onto the ladder.

---

### Key files (absolute)

- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/derived/flavor/koide_operator.py` — fixed-point gap (35–42), `ctp_fixed_point_residual` / `flavor_jacobian_at_fixed_point` + Conjecture F1 (227–260), `derivation_attempt()` (≈350), `survey_candidate_relations` M₀ ~20-order gap (319–340)
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/derived/flavor/koide_circulant_unification.py` — `fixed_point_amplitude_nogo()` → K=4/9, A/α_vac=4.24, verdict "NO-GO … Flavor outside vacuum-response" (33, 96–99)
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/derived/flavor/koide_theta_uniqueness.py` — `koide_theta_uniqueness_verdict()`: 557× margin, `is_numerology=False`, `algebraic_derivation_exists=False`
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/derived/koide/neutrino_hierarchy.py` — min ratio 194.1, NH Σmν=59.6 meV, a_ν=1 boundary-gap √3·√(a²−1)=0
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/grut/toe/registry.py` — tiers at 2429 (open_negative), 2778, 2800, 2830, 2874, 2918, 2975; "Flavor/Koide sits OUTSIDE the vacuum-response scheme" at 5214
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/theory/KOIDE_AMPLITUDE_UNIFICATION.md` — the impedance → 4/9 NO-GO writeup
- `/Users/mpg/Library/Mobile Documents/com~apple~CloudDocs/Ryans Projects/GRUT-RAI-v2/theory/GRUT_V4_CORE_CHAIN.md` — link E11 "DOTTED / reachability only", Z₃ "ASSUMED", a=√2 tuned, mechanism OPEN
