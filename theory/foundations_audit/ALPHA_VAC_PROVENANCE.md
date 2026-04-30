# α_vac = 1/3 — Provenance Audit

**Date:** April 26, 2026
**Scope:** Provenance audit only. No calculations beyond the simple sensitivity table.
**Question:** Is α_vac = 1/3 a derived theorem, a foundational axiom, or a fitted parameter?
**Bottom line:** **α_vac = 1/3 is an ASSERTION** dressed in derivation language. The cited derivation in v11.1 Appendix H reduces, after stripping descriptive context, to a single bare-statement sentence with no intermediate calculation. The "vacuum impedance from dimensional projection of trace anomaly" claim is not a recognized published physics result. The number 1/3 effectively inherits from v6's holographic SCFT a/c ≈ 4/3 claim, with v11 supplying post-hoc structural narrative.

This does NOT make α_vac = 1/3 wrong. It does mean that **Path G** (R = √(1 + α_vac) = √(4/3) ≈ 1.15470) is **not an independent derivation** — it is a clean reformulation of an unverified value. Path G's epistemic status is "structurally simpler than V7's 3-loop transcendental, but inherits the same ungrounded foundational input."

---

## Stage 1 — Chronological reading of α_vac in V7

V7 references α_vac in three structurally distinct contexts. Section/line numbers from `theory/GRUT_V7_FULL.md`.

### 1a. Foundational definition (V7 §0.2, lines 60, 72–77)

V7 introduces α_vac as one of two "constants that characterize the medium" (line 60), then (lines 72–77) sets the value:

> From v11.1 Appendix H:
>
>     α_vac = 1/d
>     d = 3 ⟹ α = 1/3
>
> α is derived from conformal projection of the trace anomaly in a Kaluza-Klein dimensional-reduction picture. It is not fitted — it is topology. In the reader's words from Appendix H §H.8: *"Spacetime remembers that it lives in more dimensions than we can directly observe."*

This is the **establishing passage**. It does three things at once: (a) cites v11.1 Appendix H as the source, (b) gives a one-sentence summary of the argument ("conformal projection of the trace anomaly in a Kaluza-Klein dimensional-reduction picture"), (c) asserts "It is not fitted — it is topology."

### 1b. Tree-level refractive index (V7 §0.2 line 81, §0.3 lines 89–96)

Once α = 1/3 is set, V7 immediately uses it for the IR refractive index:

    n_g(ω → 0) = √(1 + α) = √(4/3) ≈ 1.15470  (line 81)
    n_g²(ω) = 1 + α / (1 + (ω τ_0)²)         (line 89, single-pole susceptibility)

V7 line 83 explicitly identifies this with the cosmological R: *"This is the same number V7's 3-loop CTP computation refines to R_anomaly = 1.15428. The 0.036% difference is the loop correction — the analog of α_QED ≈ 1/137.036 as the radiative correction to the tree-level 1/137."*

### 1c. Screening factor S = 12π/α² (V7 §0.4 line 109)

V7 derives the canonical S = 108π directly from α_vac:

    S = 12π / α_vac² = 108π ≈ 339.29

So α_vac = 1/3 cascades into S = 12π·9 = 108π. With S fixed, τ_0 = τ_Λ/S follows. Half of GRUT's canonical-constant scaffolding chains off α_vac = 1/3.

### 1d. Three Routes table (V7 §0.5 lines 125–131)

Lines 125–131 show V7's "three routes converge on ≈ 1.1547" claim:

| Route | Value | Inputs | Framework |
|:---|---:|:---|:---|
| n_g(0) = √(4/3) | 1.15470 | α = 1/d (geometric) | Nonlocal EFT (v1-v11) |
| R = \|C_Cosmo / C_FINAL\| | 1.15428 | π, ln 2, ζ(3), SM integers | 3-loop CTP on S^4 (V7 §26) |
| ε_combined(SM, M_Z) | 1.15370 | SM couplings, group theory | Osborn local RG (2003) |

Note: the FIRST entry's "input" is α = 1/d, which is itself the unverified value. The three routes are NOT three independent derivations of 1.1547 — they are three formulations whose convergence depends on the α_vac = 1/d input.

### 1e. v6 → v7-old → V7 lineage (V7 §0.6 line 168)

Critically, V7 line 168 documents the historical origin of the 4/3 number:

| v6.0 (Holographic) | v7.0-old / v11 (Effective Response) | V7 (CTP) |
|:---|:---|:---|
| KK tower echo | Retarded memory kernel K(t) | Noise kernel from δ²S/δz_a² |
| **SCFT anomaly ratio a/c ≈ 4/3** | **Vacuum impedance ε_g ≈ 1.333** | **R_anomaly² = ε_g at 3-loop** |

So in v6 (holographic version), the "4/3" came from an **SCFT anomaly ratio claim a/c ≈ 4/3**. v7-old / v11 re-cast this as "vacuum impedance ε_g = 1.333 = 1 + α with α = 1/3." V7 inherits this re-cast value.

V7 line 172: *"The a/c > 1 paradox from v6 — apparent unitarity violation — was resolved in v7-old: R² = ε_g ≈ 4/3 is an effective dielectric constant, not a central-charge ratio subject to SCFT bounds."*

This is structurally important: **the value 1/3 was set by working backward from v6's a/c = 4/3 holographic claim**, with α = 1/3 chosen so that 1 + α = 4/3.

### 1f. Downstream applications (V7 §0.4, §31, codebase)

α_vac then propagates into:
- S_screening = 12π/α² = 108π (every cosmological observable)
- γ_memory = α_vac / S = 9.82 × 10⁻⁴ (GRUT-modified Friedmann coupling, V7 lines 782, 1977)
- Ω_dm,eff = α = 1/3 (dielectric DM bandwidth integral, V7 lines 2510, 2683 — 27% from Planck)
- Refractive index dispersion at all ω
- Saturn-orbit suppression, MOND a_0 trigger, etc.

The value 1/3 is woven through almost every numerical prediction in V7. Its provenance is correspondingly load-bearing.

---

## Stage 2 — The establishing argument, examined

### 2a. The cited source: v11.1 Appendix H

`/Users/mpg/Desktop/GRUT ToE/v11.1 Genesis Codex/v11.1 8 appenh Vacuum Impedance.pdf` — 2 pages total, "Origin of Vacuum Impedance."

The actual establishing argument occupies §H.4 (one paragraph). Verbatim:

> **H.4 Geometric Derivation of α = 1/3**
>
> Impedance arises from projecting bulk degrees of freedom onto the brane. For a bulk with D spatial dimensions projecting onto a brane with d spatial dimensions:
>
> - only d components of stress–energy directly source observable curvature,
> - the remaining degrees act as reactive storage.
>
> For a conformal projection of the trace anomaly, the impedance factor is fixed by the spatial dimensionality:
>
>     α = 1/d        (H.2)
>
> In our universe:
>
>     d = 3 ⟹ α = 1/3 ≈ 0.333    (H.3)

### 2b. What §H.2–H.3 do (and don't) supply

§H.2 and §H.3 set up Kaluza-Klein language:

- §H.2 *assumes* "the observed 4D gravitational dynamics arises as an effective field theory obtained by coarse-graining a higher-dimensional bulk spacetime" with one compact spatial dimension of radius L. This is a hypothesis, not a derivation from V7's CTP.
- §H.3 schematically defines `α ≡ Response_bulk / Response_brane ∼ Σ_n g_n²/m_n²` with `m_n ∼ n/L` (standard S¹ KK) and `g_n` from "geometric overlap," then states *"The sum is finite after regularization, yielding a purely geometric factor dependent on the codimension of the brane."*

**Critically:** the sum is NOT computed. No regularization is shown. The "purely geometric factor" is asserted, not derived. §H.3 ends with a claim that the sum gives "a factor dependent on the codimension," and §H.4 then jumps directly to `α = 1/d` as if this were what §H.3 produced.

There is no mathematical bridge from the schematic KK sum in §H.3 to the formula `α = 1/d` in §H.4. **The actual establishing claim is the single sentence in §H.4: "For a conformal projection of the trace anomaly, the impedance factor is fixed by the spatial dimensionality."**

That sentence is presented without internal derivation, without external citation, without explicit calculation. It is an **assertion**.

### 2c. Status classification

| Test | Pass? |
|:---|:---|
| Is α_vac = 1/3 a derivation with intermediate steps from more fundamental quantities? | **No.** The "derivation" is one sentence with no intermediate steps. |
| Is α_vac = 1/3 an explicit citation that delegates to another paper for the derivation? | **No.** v11.1 Appendix H is GRUT-internal. No external reference is given for the "α = 1/d" formula. |
| Is α_vac = 1/3 an axiom (definition or fundamental assumption)? | **De facto yes.** The framework requires this value as an input; the surrounding language presents it as derived but no derivation is supplied. |

### 2d. The KK setup as descriptive narrative

§H.2-H.3's Kaluza-Klein language serves as **interpretive scaffolding** ("here's a picture in which α = 1/d is plausible"), not as a derivation. The argument structure is:

1. Imagine a bulk → brane projection (§H.2)
2. Imagine a finite KK-mode sum (§H.3)
3. Assert that conformal projection of the trace anomaly gives α = 1/d (§H.4)

Step 3 is presented as following from steps 1–2, but the math doesn't connect. Steps 1–2 motivate the FORM of the answer (a geometric factor depending on d) but don't pin down 1/d specifically.

**Verdict:** α_vac = 1/3 is an **assertion**, not a derivation. The KK and trace-anomaly language make the assertion *physically plausible* in a hand-wavy sense, but no actual calculation is done.

---

## Stage 3 — Literature check on "vacuum impedance from dimensional projection = 1/d"

### 3a. Web search

Targeted search ("vacuum impedance" "1/d" dimensional reduction trace anomaly Kaluza-Klein viscoelastic susceptibility) returned standard Kaluza-Klein references but **no published result identifying vacuum impedance = 1/d as a generic consequence of dimensional reduction**.

### 3b. Cross-checks against standard physics

- **Kaluza-Klein dimensional reduction:** standard result is that 4D Newton's constant `G_4 = G_5/V_compact`. KK contributions to 4D effective response depend on compactification details (radius, boundary conditions, matter content), NOT simply on spatial dimensionality. There is no standard KK result that produces "susceptibility = 1/d."

- **Viscoelastic susceptibility in condensed matter:** χ(ω) is determined by microscopic relaxation processes (oscillator distributions, relaxation times, defect dynamics). It is NOT a function of the spatial dimensionality of the medium. Real materials with different dimensionality (films, bulk, fibers) have different susceptibilities driven by chemistry, not by `1/d`.

- **Trace anomaly conformal projection:** "Conformal projection of the trace anomaly" is not a standard technical term. Trace anomalies have well-defined coefficients (a, c) that depend on field content (Komargodski-Schwimmer 2011, Duff 1994). These coefficients are not simply equal to `1/d`.

- **Holographic CFT a/c bounds:** SCFTs have `a/c ratios` that satisfy specific bounds (Hofman-Maldacena 2008, etc.). Some specific theories give `a/c = 4/3` or related values, but this is NOT a generic consequence of dimensional projection — it depends on the specific theory.

### 3c. The v6 holographic origin

V7 line 168 itself records that "4/3" originated as an SCFT a/c ratio claim in v6.0. This is the most likely actual provenance: **the value 4/3 came from a v6 holographic argument; v11 Appendix H provides post-hoc structural narrative ("α = 1/d, d = 3") for why 1 + α should equal 4/3.** The "α = 1/d" formulation is reverse-engineered from the desired result, not derived from independent principles.

### 3d. Verdict

The claim "vacuum impedance = 1/d from dimensional projection of trace anomaly" is **not a recognized published physics result**. It is GRUT-internal narrative that motivates the value α = 1/3. The framework can use this value, but it should be labeled as a **foundational axiom** specific to GRUT (with v6 holographic motivation), not as a derivation from standard physics.

---

## Stage 4 — Sensitivity test (R = √(1 + α_vac), Ω_Λ via H_inf = (2−R)/(S·τ_0))

Using V7's own pipeline parameters (S = 108π depends on α via S = 12π/α²; τ_0 = 41.9 Myr):

| α_vac | S = 12π/α² | R = √(1+α) | 2 − R | H_inf [Hz] | Ω_Λ at H₀ = 70 |
|:---:|:---:|:---:|:---:|:---:|:---:|
| 1/4 | 192π ≈ 603.2 | 1.11803 | 0.88197 | ≈ 1.107×10⁻¹⁸ | 0.2382 |
| 0.27 | 12π/0.0729 ≈ 517.0 | 1.12694 | 0.87306 | ≈ 1.279×10⁻¹⁸ | 0.3179 |
| **1/3 (canonical)** | **108π ≈ 339.3** | **1.15470** | **0.84530** | **≈ 1.886×10⁻¹⁸** | **0.6906** |
| 1/2 | 48π ≈ 150.8 | 1.22474 | 0.77526 | ≈ 3.892×10⁻¹⁸ | 2.943 (unphysical) |

**Observation:** the cosmological prediction Ω_Λ is **highly sensitive** to α_vac through the *coupled* effect on S and (2−R). Other plausible values:

- α = 1/4 gives Ω_Λ ≈ 0.24 (way below Planck)
- α = 0.27 gives Ω_Λ ≈ 0.32
- α = 1/3 gives Ω_Λ ≈ 0.69 (Planck match)
- α = 1/2 gives Ω_Λ ≈ 2.94 (unphysical — exceeds 1)

Only α = 1/3 produces a physically sensible Ω_Λ in the right ballpark for Planck. **The framework genuinely requires α_vac near 1/3 for the cosmological prediction to land where Planck observes.** This is doing real predictive work.

But "framework requires α near 1/3 for Planck-match" doesn't mean "α = 1/3 is derived from first principles." It means the framework's coupling structure has α_vac as the load-bearing input that controls Ω_Λ. If α had been something else, the framework's cosmological prediction would have been different.

---

## Stage 5 — Phase I closure protocol cross-reference

### 5a. Codebase implementation

`grut/foundation/closure_protocol.py` line 54:

    ALPHA_VAC: float = 1.0 / 3.0                 # α = 1/d, d = 3 (v11 App H)
    """Vacuum impedance. Fixed by dimensional projection of the trace
    anomaly: α = 1/d where d is spatial dimension. d = 3 ⟹ α = 1/3 exactly."""

The closure protocol **inherits** the value from v11 Appendix H. The docstring re-states the same one-sentence claim. No independent derivation.

Subsequent constants (line 58, 62) chain off α_vac = 1/3:

    S_SCREENING: float = 12 * np.pi / ALPHA_VAC**2   # = 108π
    N_G_DC: float = float(np.sqrt(1.0 + ALPHA_VAC))  # = √(4/3) = 1.15470

### 5b. Phase I closure protocol document (Zenodo DOI 10.5281/zenodo.18008060)

The Zenodo DOI is referenced but the actual document content is not in the local repo. V7 line 109 quotes "Phase I §5: canonical derivation" as the source of `S = 12π/α²`. Without the Zenodo document in hand, the audit cannot verify whether Phase I §5 derives α_vac = 1/3 independently OR inherits it from v11 Appendix H.

**Inference from V7 §0.2 line 72 ("From v11.1 Appendix H: α_vac = 1/d"):** v11 Appendix H is treated as the canonical source. Phase I closure protocol almost certainly inherits the value rather than re-deriving it.

### 5c. No independent derivation found

Across the repo (V7 main, V8, closure_protocol.py code, all theory/derivation files audited), **no document supplies an independent derivation of α_vac = 1/3 from first principles**. Every reference traces to v11 Appendix H, whose §H.4 contains the one-sentence assertion.

---

## Stage 6 — Honest summary

### What α_vac = 1/3 is

**An assertion**, with two layers of supporting context:

1. **Surface narrative (v11.1 Appendix H §H.4):** "α = 1/d from conformal projection of the trace anomaly under dimensional reduction." Single-sentence claim, no calculation, no external citation.
2. **Historical lineage (V7 line 168):** the value 4/3 originated in v6's holographic SCFT a/c ratio claim. v11's "α = 1/d, d = 3" formulation is post-hoc structural narrative reframing the v6 result.

### What α_vac = 1/3 is NOT

- **Not a published-physics result.** "Vacuum impedance = 1/d from dimensional projection" is not a recognized formula in KK theory, viscoelastic medium theory, trace anomaly literature, or holographic CFT. The phrase is GRUT-specific.
- **Not derived from V7's CTP foundations.** The CTP-from-S_CTP machinery does not produce α = 1/3. The CTP framework gives noise kernels and constitutive equations, but α_vac is supplied as an input, not as an output.
- **Not a citation to external work.** v11.1 Appendix H does not cite a source for α = 1/d.

### Implications for Path G

Path G proposed:

    R = √(1 + α_vac) = √(4/3) ≈ 1.15470

with the strength claim that "this is structurally derived from one input: α_vac = 1/d."

**This audit shows that input itself is unverified.** Path G is therefore:

- **A clean reformulation of the v6 holographic 4/3 claim** in viscoelastic-vacuum language. ✓
- **The simplest in-pipeline expression of GRUT's foundational α_vac assumption.** ✓
- **NOT an independent derivation of R from first principles.** ✗ — it inherits the assumed value.
- **Closer to V7's historical 1.15428 than Path D** because both Path G and V7's 1.15428 ultimately trace back to the same 4/3 ancestor (Path G via α_vac, V7 via 3-loop transcendental refinement). ✓
- **Compatible with the user's saturation picture** as a clean structural articulation. ✓

### Path D vs Path G epistemics

| Property | Path D (R = a_SM/c_SM = 1.17256) | Path G (R = √(1+α_vac) = 1.15470) |
|:---|:---|:---|
| Derived from sourced inputs | ✓ KS 2011 + Duff 1994 per-species | ✗ inherits α_vac = 1/3 from v11 App H assertion |
| Reproducible from textbook QFT | ✓ standard trace-anomaly machinery | ✗ "α = 1/d" not in standard physics |
| Aligned with V7 narrative (saturation/dielectric) | partial (different physical object) | ✓ exactly matches v7-old/v11 framing |
| Numerically close to V7's historical 1.15428 | 1.58% off | 0.04% off |
| Identification physically meaningful | ✓ 1-loop SM trace anomaly Euler/Weyl² ratio | ✓ IR refractive index of viscoelastic medium |

### What this means for committing

This audit does NOT invalidate Path G. It clarifies what kind of object Path G's R is:

- **Path G is the cleanest in-framework articulation** of GRUT's cosmological R via the existing α_vac = 1/3 input.
- **Path D is the cleanest cross-check from external sourced QFT.** It produces a different number (1.17 vs 1.15) because it's a different physical object (trace anomaly ratio vs IR refractive index), AND because Path G's α_vac value isn't grounded in external physics.

The honest commitment posture:

- **If we adopt Path G**, V8 §12 should explicitly label α_vac = 1/3 as a foundational AXIOM of GRUT (specific to the framework; motivated by v6 holographic legacy and dimensional-reduction narrative; not a derivation from external physics). The cosmological R then follows cleanly from this axiom.
- **If we adopt Path D**, V8 §12 commits to a number (1.17) that's externally verifiable but doesn't match V7's historical claim or Planck precisely.
- **Hybrid posture:** report both. Path D as the externally-grounded cross-check (with 4% Planck tension); Path G as the framework-internal canonical R (with 0.24% Planck deviation, contingent on accepting α_vac = 1/3 as axiom).

The hybrid posture is most defensible scientifically. It tells specialists exactly what's grounded in external QFT (Path D) and what's GRUT-axiomatic (Path G), without conflating them.

### Recommendation summary

α_vac = 1/3 is **an axiom of GRUT**, not a derivation. Calling it "derived from dimensional projection" overstates what v11.1 Appendix H actually does. Going forward, V8 should label it accordingly:

> **α_vac = 1/3 (axiomatic).** GRUT takes the vacuum impedance to be α_vac = 1/d with d = 3 spatial dimensions, motivated by a viscoelastic-medium-from-dimensional-reduction picture (v11.1 Appendix H). This value is not derived from external physics in published form; it functions as a foundational input of the framework. All cosmological-sector predictions inherit this input; sensitivity is high (see Stage 4). The framework's ability to produce Ω_Λ ≈ 0.69 depends on α_vac being near 1/3.

This is the truthful framing. Path G stands as a clean structural articulation, but the foundational input it builds on requires the axiom label.

---

## Sources

- **V7 main** (`theory/GRUT_V7_FULL.md`): §0.2 lines 72–77 (establishing passage), §0.5 (Three Routes table), §0.6 line 168 (v6→v7 lineage), §26.1 (3-loop refinement)
- **v11.1 Appendix H** (`/Users/mpg/Desktop/GRUT ToE/v11.1 Genesis Codex/v11.1 8 appenh Vacuum Impedance.pdf`): the cited source; full text quoted in §2a above
- **closure_protocol.py** line 54: code implementation, inherits from v11 App H
- **Phase I closure protocol** (Zenodo DOI 10.5281/zenodo.18008060): referenced but not directly audited (document not in repo)
- **Web search** (Stage 3a): no external published support for "vacuum impedance = 1/d from dimensional projection"
- **[Komargodski-Schwimmer 2011](https://arxiv.org/abs/1107.3987)** and **[Duff 1994](https://arxiv.org/abs/hep-th/9308075)**: standard trace-anomaly references; do not contain "α = 1/d" formula

## Verdict

**α_vac = 1/3 is an axiom**, not a derivation, in V7 and its predecessors.

**Path G's R = √(4/3)** is therefore best understood as: *the cleanest in-framework expression of the canonical R given GRUT's α_vac axiom*. It is not an independent derivation that closes the cosmological prediction; it is the framework's own structural articulation.

**The honest framing for V8 §12:** GRUT predicts Ω_Λ ≈ 0.691 conditional on the foundational axiom α_vac = 1/d = 1/3. If a future independent calculation derives α_vac from external physics (CTP machinery, holographic identification, or specialist 3-loop work), the framework's cosmological prediction becomes unconditional. Currently, it is conditional on the axiom.

This is the kind of foundational labeling that makes specialist outreach defensible.
