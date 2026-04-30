# Cosmic X-Crossover — Forward Derivation Investigation

**Status:** Stage 1 complete. Stages 2–4 pending review.
**Started:** 2026-04-28.
**Scope:** ONE specific framework prediction — the cosmic-history evolution of X = ωτ_0 when ω is identified with the Hubble rate. Bounded, single-session.

**SCOPE BOUNDARIES (load-bearing):**
- This investigation does NOT address T_c provenance (`t_c_provenance_inconsistency_open_negative` #15 stays active).
- This investigation does NOT propose Chapter 13 revisions.
- This investigation does NOT adopt the Direction 4+5 reading as the framework's cosmic-history mechanism.
- Whether X_cosmic crossover replaces T_c crossing as the cosmic-history mechanism is research-tier work for future sessions, not closed by this calculation.

**Methodological constraint:** Forward derivation of one specific prediction from the framework's existing constitutive equation. The deliverable is a tier-labeled claim with explicit scope, not a framework-level reading.

---

## Stage 1 — Identify the cosmic-scale ω

### The constitutive susceptibility

The framework's frequency-domain response (Ch 4, Ch 9 dielectric DM):

    n_g²(ω) = 1 + α / (1 + (ωτ_0)²)

The susceptibility (refractive enhancement minus 1):

    Δn_g²(ω) = α / (1 + (ωτ_0)²)

Behaviour:
- **ωτ_0 ≪ 1**: Δn_g² → α = 1/3 (full refractive response)
- **ωτ_0 ≫ 1**: Δn_g² → α/(ωτ_0)² → 0 (suppressed response, GR-recovered)
- **ωτ_0 = 1**: Δn_g² = α/2 (crossover)

The framework's Ch 4 regime classification uses X = max(ω, Λ_grav) × τ_0 to characterize whether a system is in crystal regime (X ≫ 1, deep crystal, GR-recovered) or fluid regime (X ≪ 1, full refractive). Different physical systems have different dominant ω; for cosmological dynamics, identifying ω is the load-bearing question.

### Identification: ω = H for cosmic-scale gravitational dynamics

**Claim:** For cosmic-scale gravitational dynamics, the natural ω entering the framework's susceptibility is the cosmic Hubble rate H = ȧ/a.

**Physical justification:**

1. **H is the cosmic dynamical rate.** It sets the timescale 1/H over which the cosmic background varies. Anything that varies on shorter timescales is "fast" relative to cosmic dynamics; anything slower is "slow" relative to cosmic dynamics. This matches the role ω plays in the susceptibility — the rate at which a disturbance presents itself to the medium.

2. **Cosmological-perturbation-theory analogue.** In standard cosmological perturbation theory, modes "exit" or "re-enter" the Hubble horizon at k = aH. Modes with kc/a > H are sub-Hubble (oscillate at proper frequency above H); modes with kc/a < H are super-Hubble (frozen). The dividing rate is H itself. This is the standard cosmological identification of "the relevant frequency."

3. **Alignment with framework's existing structure for cluster physics.** For cluster mergers, the framework uses ω_cluster = v/l (collision rate scale). For galactic rotation, ω_gal = orbital rate. For CMB perturbations (Ch 9 line 568), the framework uses ω_acoustic and ω_expansion ~ H separately. So H IS already used as a cosmic-scale ω in the framework's own work; this Stage 1 identification just makes it explicit for cosmic-history-wide application.

**Caveats — choices the framework does NOT pin:**

- **Mode-by-mode alternative.** A cosmological mode of comoving wavenumber k has proper frequency ω_k = ck/a. For modes inside the Hubble horizon (k > aH/c), ω_k > H. The X-crossover for such modes would happen at different redshifts than the H-based crossover. The framework doesn't natively select "background H" vs "mode-by-mode ω_k" — this is precisely the kind of choice that surfaced in the n_g(ω) covariance open negative (#9).

- **Conformal vs proper frequency.** In some conventions, ω is defined in conformal time rather than proper time. The two differ by a factor of a (the scale factor). For background-level evaluation at a single epoch, the distinction collapses; for evolution across redshift, it could matter.

- **Multi-mode integration.** The framework's bandwidth integral (Ω_dm = α from integrating Lorentzian susceptibility over linear-regime modes) integrates over a population of modes. The "cosmic-history evolution" question of when refractive DM is observationally dominant is integrated, not single-mode.

This Stage 1 identification commits to **the simplest, most direct interpretation: ω = H for cosmic-scale gravitational dynamics**. The caveats are real and would matter for tighter analysis, but the simplest identification is the right starting point for Stage 2.

### Why this is a derivation, not a framing choice

The framework's constitutive equation has χ(ω) = α/(1 + (ωτ_0)²) hard-coded. The cosmic Hubble rate H is the universally-agreed cosmic dynamical rate. Substituting ω = H into the framework's existing susceptibility is mechanical:

    Δn_g²(cosmic) = α / (1 + (H·τ_0)²)

This isn't choosing an interpretation — it's applying the framework's existing infrastructure to the cosmic-scale case with the natural identification of ω. The output (X_cosmic = H × τ_0, regime depending on its value) is a derived consequence.

What WOULD be an interpretive choice (and is therefore NOT done here):
- Saying X_cosmic crossing "replaces" T_c crossing as the cosmic-history mechanism
- Proposing that the framework has no plasma-physics phase boundary
- Downgrading T_c provenance because of this calculation

The derivation produces a positive prediction. It does not produce an exclusion claim about T_c.

---

## Stage 2 — Compute X_cosmic(z) (PENDING REVIEW)

Plan: use standard cosmology Friedmann equations to compute H(z) in the matter-dominated era. Compute X_cosmic(z) = H(z) × τ_0 across z = 0 to z = 1100. Identify the X_cosmic = 1 crossing redshift.

Inputs (from Planck 2018):
- H_0 = 67.4 km/s/Mpc (or use framework's H_0 = 68.8 from cosmic-baseline; document choice)
- Ω_m ≈ 0.315
- Ω_Λ ≈ 0.685
- Ω_r negligible at z < 3400

H(z) = H_0 × √(Ω_m(1+z)³ + Ω_Λ + Ω_r(1+z)⁴)

For z < 3400 (matter+Λ era), Ω_r contribution is small; use full Friedmann to be precise.

---

## Stage 3 — Verify Λ_grav < H at relevant redshifts (PENDING)

Plan: confirm that for cosmic-scale gravitational dynamics, the H term dominates over Λ_grav in the regime classification X = max(ω, Λ_grav) × τ_0. Λ_grav for cosmic-scale objects (e.g., representative galaxy or cluster) is far smaller than H at all relevant redshifts.

---

## Stage 4 — Register the prediction (LANDED 2026-04-28, with mass-class scope correction)

Registered: `cosmic_x_crossover_prediction` (Ch 4, computed).

**Stage 3 surfaced a mass-class scope finding that the original
Stage 2/4 framing missed:** the framework's regime classification
X = max(ω, Λ_grav) × τ_0 gives different X values for different
mass classes at the same cosmic epoch. For atomic test particles
H dominates Λ_grav by ~10³⁸; for stellar mass and up Λ_grav
dominates H by 76+ orders. The X = 1 crossing at z ≈ 71 applies
ONLY to atomic-scale perturbations of the cosmic background.
Stellar+ mass classes are in deep crystal regime at all epochs
and do not experience this crossover.

The registered claim is therefore scoped specifically to atomic-scale
test-particle perturbations, NOT to "cosmic-history regime evolution"
writ large. Whether atomic-scale perturbations are the load-bearing
mass class for cosmic-history regime evolution is a separate question
not addressed by this calculation.

**The claim explicitly does NOT:**
- Address T_c provenance (#15 stays active)
- Propose Chapter 13 revisions
- Claim X_cosmic crossover replaces T_c crossing as cosmic-history mechanism
- Claim atomic-scale perturbations are THE load-bearing mass class
- Resolve the multi-ω complexity (#9 stays active)

**The claim DOES register:**
- Specific X(z) curve for atomic-scale test-particle perturbations
- X = 1 crossing at z ≈ 71 (Planck H_0) / 70 (framework H_0), <1.4% sensitivity
- T_CMB at crossing ≈ 194-197 K (post-recombination, structure-formation epoch)
- The redshift-independent H/Λ_grav structural fact (= ℏc/(Gm²))
- The mass-class dependence (different X for different mass classes at same epoch)

**Methodological note:** the Stage-2 result was framed as "cosmic-
history regime evolution" before Stage 3's mass-class structure was
visible. Stage 3 surfaced that the calculation actually computes one
specific mass class's regime evolution, not the cosmic history globally.
The claim language was tightened accordingly. This is the same kind
of scope-tightening that surfaced in the primordial A_s rescaling
sensitivity — both cases involve definitional choices the framework
hasn't pinned. The discipline pattern caught the overstep before the
broader claim was registered.

---

## End of Stage 1

Identification ω = H committed with physical justification. Caveats documented. Stage 2 ready to execute on review.

Pausing for review per investigation protocol.
