# T2 THEOREM GATE + ADJUDICATOR PRE-REGISTRATION — sealed

**Date:** 2026-09-24. **Seal:** the git commit introducing this file (adjudicator
tree). **Blindness statement:** produced with NO access to any output of the
builder's rebuilt on-shell instrument, which has not reported. Produced by three
independent *blinded* analytic derivations (routes: direct golden-rule asymptotics;
continuum-QFT limit; multipole/soft expansion against the exact lattice vertex), two
independent applicability analyses (kernel-vs-S-matrix; symmetry audit), and two
adversarial verification passes with fresh numerical instruments (workflow
wf_0e06fe5a-378; per-agent records in the session transcript). All three routes
converged EXACTLY on the exponents below; both attackers reproduced the analytic
prefactors to 0.1% or better with independent root-finding numerics. Errors found
inside the dossier during the attack round are disclosed in §5 — including one that
would have mis-gated a correct run.

Model: the audited chain–graviton system (dispersion ω_q = √(Ω² + 4sin²(q/2)),
acoustic case Ω = 0 primary; TT gravitons ω = |k|; pair vertex
M ∝ e_xx·½[√(ω_qω_q′) + qq′/√(ω_qω_q′)]/√N; on-shell golden-rule
J(ω) with joint energy/momentum enforcement, T = 0, O(κ²)).

## 1. Sealed predictions (per convention — the builder must pin the convention BEFORE running)

**Minimal stress vertex, acoustic chain:**

| Quantity | task-literal (no 1/(2ω_k)) | with 1/(2ω_k) (archived W-convention) |
|---|---|---|
| \|M_on-shell\|² | ω⁶ | ω⁵ |
| J(ω) small-ω | **C·ω⁸**, even series (ω⁸, ω¹⁰, …) | **ω⁷**, odd series |
| naive Γ·cos tail coeff. | vanishes at ALL orders (parity) | nonzero: Γ(8)cos(4π) ≠ 0 |
| K_R late-time (cos convention) | NO algebraic soft tail at any order; literal tail = band-edge ringing J(4⁻)·sin(ω_c t)/t, carrier ω_c = 4 (or k_max if k_max < 4) | genuine monotone **t⁻⁸** |
| sine/retarded component | Γ(9)·C₈·t⁻⁹ | — |

**Tidal variant:** every J exponent +4 (ω¹² / ω¹¹); pointwise J_tidal/J = (ω/k_max)⁴
to machine precision.

**Coefficients (analytic, cross-verified):** angular integral ∫₋₁¹(1−μ²)³(1+μ²)²dμ =
3968/3465; task-literal C₀ = (3968/3465)/(32π·36864) = 3.090054e-7·κ²; kernel-norm
C₈ = (3968/3465)/(8π·36864) = 1.236022e-6 (normalization map: ×4 kernel, ×16π
multipole, ×32π audit units — FROZEN here; a factor "discovered" after the run is a
fail, not a fix). Band-top jump J(4⁻) = 3.5441·κ² task-literal (normal channel
0.53832 + umklapp-wrapped 3.00575). Umklapp threshold ω_U = 2.5668575 (root of
ω = 2 + 2cos(ω/2)). Gapped chain (Ω > 0): J ≡ 0 below 2Ω, threshold step → Ω⁴/8
(kernel-norm) — a step, not a power law.

**Falsifiable side-predictions:** (a) parity — the small-ω series of J (task-literal)
contains NO odd powers; a genuine ω⁹ term falsifies this derivation and must be
reported as such; (b) same-sign (co-propagating) channel: exactly zero on-shell roots
at every ω — subsonic phonons vs lightlike graviton (the builder's independently
found Cherenkov closure; this ledger confirms and sharpens it: closure is exact at
all ω, not only small ω); (c) fragility ladder — supersonic phonons or a
dispersion-only deformation at frozen vertex: slope drops to 4; lattice-sine
potential vertex (2sin(q/2)·2sin(q′/2) instead of qq′): normal-channel J vanishes
IDENTICALLY; kinetic-only vertex: slope 4.

## 2. The theorem content (attribution — what the gate actually establishes)

- The Weinberg soft-graviton theorem does **not** directly constrain this observable:
  no hard legs exist (graviton and both phonons all soft; phonons are not asymptotic
  gravitating states). Citing it as the reason for any exponent here would be wrong.
- What conservation actually delivers: Goldstone decoupling guarantees only amplitude
  O(ω), i.e. **J = O(ω⁴) as an upper bound**. The quadrupole folklore map
  (P ~ ω⁶Q² → J ~ ω⁵) fails for this observable — **an instrument reporting ω⁵ FAILS
  the gate, correctly.**
- The four extra powers beyond ω⁴ are **matter-sector physics**, cleanly separated by
  channel: (i) the open (counter-propagating) channel's kinetic-vs-potential stress
  cancellation is *matter-internal tracelessness* — T₊₋ = 0 of the effective massless
  1+1D field at linear dispersion (exact for any subsonic c_s under consistent
  microscopic deformation; the graviton cone never enters the bracket) — with lattice
  inversion parity skipping the ω² order, leaving amplitude ω³; (ii) the
  *cone-kinematic* protection is the same-sign channel closure (needs v_g ≤ c). The
  original "null-cone degeneracy" label conflated (i) and (ii); this ledger separates
  them. Both must be identified by the run — that identification, not the exponent
  match, is what passes the theorem gate.

## 3. The gate (all critical items must pass; corrected set after the attack round)

G1 **Frozen pre-registration** (hash/timestamped before the run): the 1/(2ω_k)
choice; cos-vs-sin kernel transform incl. prefactor; ordered-pair counting;
polarization-sum and DOS conventions; the analytic normalization map onto §1's
coefficients; fit windows; broadening schedule; tolerances. Sole escape hatch:
kernel-transform convention may be established ONLY by the synthetic pipeline test —
push J_test = ω⁸e^(−ω) through it (cos-type → 8!·9/t¹⁰; sin-type → 8!/t⁹) — never
inferred from physical output.
G2 **On-shell joint enforcement**: ω_k = |k| = ω AND δ(ω − ω_q − ω_q′) AND
q + q′ = k∥ (mod 2π) simultaneously; T = 0; zero mode excluded as exact mode only.
The archived off-shell numbers (|g|² ~ ω^−0.56 / "ω³ / t⁻⁴") are BANNED as targets or
sanity anchors — different observable.
G3 **Vertex unit tests**: on-shell bracket → −√(qp)(q²+p²)/24 with O(ω²) drift;
linear-dispersion switch → 0 to machine precision; lattice-sine vertex → 0
identically; same-sign bracket uncancelled (~2√(qp)).
G4 **Channel audit (corrected)**: zero same-sign roots at every ω; umklapp
identically zero ONLY below ω_U = 2.5668575 — **not 3.5** (a correct instrument shows
J_umk(3.0) ≈ 4.5× the normal channel; the wrong gate number, produced and caught
inside this dossier, fails correct runs); collinear-(1−μ²)²-suppressed continuous
onset above ω_U; small-ω angular shape ∝ (1−μ²)³(1+μ²)².
G5 **Exponent**: local log-slope 8.00 ± 0.05 (7.00 under the propagator convention)
over pre-registered ω ∈ [0.02, 0.32]; doubling ratio 256 (128) within the stated
O(ω²) budget (~1.4% at ω = 0.32). The archived fit window [0.15, 1.2] is outside
asymptopia — pre-registered windows only.
G6 **Coefficient, never slope-only**: J/ω⁸ → the declared-normalization constant
within ≤1% at ω ≤ 0.04 under the pre-frozen map.
G7 **Parity as output**: free fit of J/ω⁸ including odd terms; odd coefficient
consistent with zero.
G8 **Counterfactual core (non-circularity heart)** — controls with different
pre-computed outcomes at identical settings: kinetic-only vertex → slope 4.00 ± 0.05;
linear dispersion → exact zero; lattice-sine vertex → identically zero; gapped chain
→ J ≡ 0 below 2Ω with threshold step Ω⁴/8 (edge-resolving quadrature; note the step
is carried half by the same-sign channel, OPEN for the gapped chain); tidal →
pointwise (ω/k_max)⁴ ratio. The instrument must FIND the cancellation, not inherit it.
G9 **Delta discipline**: Gaussian or histogram energy-delta only; **any Lorentzian
broadening is an automatic fail** (demonstrated 4.45× contamination of the
cancellation-suppressed on-shell weight); η below the same-sign closure gap ~ω³/96 at
the smallest ω probed (leakage above it demonstrated at ~10³×); η-halving and
grid-doubling stability < 0.1%.
G10 **Tail discipline**: the exponent is gated on J(ω) directly, never on raw-K_R
envelope fits (which measure band-edge ringing regardless of soft physics); kernel
tail claims only via FFT carrier identification against the parameter-free carrier
predictions (4, k_max, or 2Ω). Production instrument must differ in class from the
reference quadrature used here (e.g. discrete-N broadened sum or real-time
evolution), or the gate compares the derivation to itself.

## 4. Consequences for the program (recorded now, before any run)

1. Both prior expectations are refuted as predictions for this instrument: the
   archived ω³ story (off-shell artifact) AND the quadrupole ω⁵ hypothesis (wrong
   observable mapping). The theorem gate did its job before any code ran.
2. **V10 inverts on the repaired instrument**: on-shell, tidal (ω¹²) and minimal
   (ω⁸) are genuinely different classes — the vertex class DOES move the exponent,
   restoring the original narrative's expectation that the off-shell run had
   (correctly, for that object) refuted.
3. The literal lattice late-time kernel is band-edge ringing — UV/lattice physics,
   not soft-graviton memory. Any T3-confrontation mapping must therefore compare
   J(ω) exponent classes inside the validity window, never raw late-time K_R fits of
   the lattice instrument.
4. Physics content if the run confirms: in this substrate class, gravitational
   dissipation of acoustic (traceless, subsonic) matter is suppressed far beyond the
   quadrupole class, while gapped sectors dissipate at threshold with no power law —
   sector structure, not vertex folklore, controls dissipation (consistent with V9
   being the real signal in the old run).

## 5. Dossier-internal errors found by the attack round (disclosed)

(a) One applicability analysis carried umklapp gate numbers ("zero below 3.5") that a
CORRECT run would fail — cause identified (threshold configuration is one phonon at
the zone edge + one soft, not both near the edge); corrected to ω_U = 2.5668575.
(b) The multipole route's band-edge fit overcounted the jump ~×1.84 (angular-window
bookkeeping); golden-rule's analytic value stands, verified two independent ways.
(c) A claimed interior singularity at ω = 2 is spurious (kinematically unreachable
below ω_U). (d) The "null-cone degeneracy" mechanism label conflated two protections
(§2). (e) One route's K-tail field answered a different convention than stated
(self-acknowledged); resolved in §1's convention table. Errors (a)–(c) demonstrate
why gate constants must be derived analytically under pinned conventions, never
copied from reference numerics.

## 6. Standing

This ledger is the adjudicator's half of the dual pre-registration. It binds the
adjudicator: if the builder's rebuilt instrument, passing G1–G10, reports exponents
in conflict with §1 under the pinned convention, the DERIVATION is what falls, and
that is reported as the result. The builder's own pre-registration (its tree) remains
independent; agreement or disagreement between the two sealed sets is itself a
recorded outcome. Nothing here has seen a rebuilt-instrument number.
