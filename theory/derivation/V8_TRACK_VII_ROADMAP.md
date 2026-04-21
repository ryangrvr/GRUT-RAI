# V8 Track VII Roadmap — Re-identifying M_soliton

**Date filed:** April 20, 2026
**Predecessor:** Track VII V7 closed NEGATIVE (see Step 3 log).
**Status:** Open research program.

## Why this roadmap exists

Track VII in V7 aimed to compute Ω_dm natively and close the
zero-parameter H_0 prediction. The result after three steps:

- **Step 2 (STANDS):** M_soliton = 2.11×10⁹ GeV is structurally derived:
  ```
  M_soliton = 2⁹ π √N_ERAS / (27 × C_FINAL^(3/2) × λ)
  ```
  with λ = g²/2 (BPS) and all quantities traced to computed constants.
  Mathematically this formula is correct and the mass it produces is a
  specific GRUT output.

- **Step 1 (RETRACTED):** Ω_dm = 0.38 from XY-universality Kibble-Zurek.
  Superseded by Step 3.

- **Step 3 (CLOSED NEGATIVE):** Correct topology is cosmic strings
  (π_1(U(1)) = ℤ), not monopoles. With strings + XY universality + natural
  KZ-loop vorton mass, Ω_dm = 0.008 — factor 33 LOW. Natural KZ vortons
  have M ≈ 4.7×10⁶ GeV, not M_soliton = 2.11×10⁹ GeV.

**So what does M_soliton actually compute?** That is the V8 research
question.

## Honesty constraints carried into V8

1. M_soliton's structural derivation is preserved. Its physical
   identification is the open question.
2. The "factor of 2" agreement claim from Step 1 is retracted.
3. H_0 = 69.03 km/s/Mpc remains a ONE-PARAMETER prediction
   (uses observed Ω_dm as input). Zero-parameter H_0 is pending.
4. No hypothesis below may be "chosen because it gives Ω_dm = 0.263."
   Each must be derived or rejected on its own merits.

## Three candidate identifications for M_soliton

### Candidate A: SU(2)_dark → U(1)_dark → nothing (two-step breaking)

**The most structurally interesting candidate.**

If V7's U(1)_dark is the low-energy remnant of an SU(2)_dark sector
that broke at a higher scale Λ_UV, then:

- First breaking: SU(2)_dark → U(1)_dark at T = Λ_UV
  - Vacuum manifold: SU(2)/U(1) ≅ S²
  - π_2(S²) = ℤ → 't Hooft-Polyakov MONOPOLES form here
  - Monopole mass: M ~ 4π × Λ_UV / g²_SU(2)
- Second breaking: U(1)_dark → 1 at T = v_dark = 422 MeV
  - Vacuum manifold: U(1) ≅ S¹
  - π_1 = ℤ → cosmic strings (the ones Step 3 computed)
  - Strings are cosmologically negligible (Gμ ~ 10⁻³⁹)

For this to match V7's M_soliton = 2.11×10⁹ GeV, the SU(2) breaking
scale must be around `Λ_UV ~ M_soliton × g²_SU(2) / 4π`. With
g²_SU(2) ~ O(1), `Λ_UV ~ 10⁸-10⁹ GeV`. This is a specific UV scale
that V7 does NOT currently specify.

**To check:**
- Does C_FINAL ∝ (1/anomaly coefficient)² naturally produce a specific
  Λ_UV? The (2⁸ √2 π / 27) prefactor might be the SU(2) monopole
  structural factor at the boundary.
- Kibble-Zurek monopole calculation at Λ_UV (NOT at v_dark). With
  H ~ Λ_UV² / M_Pl, ξ_KZ at the UV transition, compute Ω_dm.
- Does the GRUT constitutive framework admit a natural SU(2) → U(1)
  breaking pattern as the "parent" of the dark sector?

**Blocker:** V7's dark sector explicitly says U(1)_dark. Extending it
to SU(2)_dark requires either (a) a V8 reinterpretation of what
"U(1)_dark" means in V7 — possibly "the residual after a higher
breaking" — or (b) new physics added in V8.

### Candidate B: Non-topological soliton (Q-ball)

Q-balls are lumps of a complex scalar field stabilized by a conserved
global charge Q. Their mass scales as M ~ Q^(3/4) × v. For
M ~ M_soliton with v = 422 MeV:

```
Q ~ (M_soliton / v)^(4/3) = (2.11e9 / 0.422)^(4/3) ~ 10^12
```

Very large charge — not trivially natural, but not forbidden.

Q-ball production does NOT go through Kibble-Zurek. It requires:
- Affleck-Dine dynamics at the end of inflation (need a specific
  flat direction in the potential)
- A conserved U(1) charge (could be the dark U(1)?)
- An initial condition with ⟨Q⟩ ≠ 0

**To check:**
- Does the V7 dark-sector potential have a flat direction that supports
  Q-ball stabilization?
- Can the initial condition ⟨Q⟩ be computed from inflation end?
- Does the prefactor 2⁸√2π/27 match Q-ball mass scaling
  M_Q = A × Q^(3/4) × v with A = 16π/3 ≈ 16.76? Comparing:
  `A_Q / (2⁹π√N/27 / C^(3/2))` — doesn't trivially match.

### Candidate C: Dark baryon from confining dark dynamics

If U(1)_dark is the unbroken U(1) of a larger non-Abelian gauge group
that confines at a lower scale, the DM could be a dark baryon — a
bound state of confined fermions/gluons. Mass scales like the dark
confinement scale Λ_conf times a group-theory factor.

**To check:**
- Does V7's dark sector have an implicit confining scale below v_dark?
- What non-Abelian group would give M_baryon = 2.11×10⁹ GeV with
  Λ_conf at a specific scale?
- Does the 2⁸√2π/27 combinatorial prefactor match color-factor counting
  for any specific non-Abelian group? 2⁸ might be 2⁴ × 2⁴ = SU(2)_L × SU(2)_R
  breaking counts; 27 might be the 3³ for three-quark baryons in SU(N);
  √N_ERAS is mysterious in this context.

## Concrete V8 Step 1 (first move)

**Audit V7 §28 (dark sector)** to determine:

1. Is U(1)_dark stated as fundamental, or as a low-energy effective
   theory?
2. What, if anything, is the GRUT motivation for the specific prefactor
   2⁸√2π/27 in A?
3. Does the √N_ERAS dependence in M_soliton have a physical derivation,
   or does it enter from the stiffness-normalization S_K = 1 constraint
   alone?
4. Is there V7 text that already identifies M_soliton as something other
   than a monopole/topological-defect mass?

This audit does not change any code. It clarifies the physics target
before V8 Step 2 (selecting which of A/B/C to pursue first).

## Rejected paths (do not waste cycles)

- **Reinterpreting p_geom or loop-size to force Ω_dm = 0.263.** Step 3's
  loop-size scan showed that required R ≈ 30×ξ_KZ is not a natural
  Kibble-Zurek scale. No honest derivation gives 0.263 from the U(1)
  string network alone.
- **Choosing mean-field universality over XY "because MF gives 0.19."**
  XY is the correct class for U(1) symmetry breaking by a complex scalar.
  MF's closer number is coincidence.
- **Forcing M_vorton = M_soliton.** Step 3 showed this requires
  loops ~450× larger than ξ_KZ.

## Publication posture

The V7 Hubble paper ships with H_0 = 69.03 km/s/Mpc labeled explicitly
as a **one-parameter prediction** (takes Ω_dm as input from Planck).
Track VII's V7 closure attempt and its negative result are documented
in the derivation log (preserved for honesty ledger). The zero-parameter
claim is withdrawn. V8 Track VII continues this research program.

## Ledger

**15 corrections caught. 0 hallucinations.**

The discipline caught two errors that partially cancelled and would have
propagated into a headline claim. Track VII's V7 arc is honest science:
setup, attempted closure, negative result, preserved for future work.
