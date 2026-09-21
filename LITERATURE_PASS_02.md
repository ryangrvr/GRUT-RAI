# LITERATURE_PASS_02 — primary-source / citation-graph verification (IN PROGRESS)

**Date opened:** 2026-09-21. **Authorization:** owner charter (Q1–Q8; no
manuscript edits; v3 untouched throughout; may downgrade novelty, may not
rewrite the calculation). **Method so far:** full-text read of the nearest
primary source (TTW 2103.08547 via ar5iv), PDF read of Kitamoto–Kitazawa
1402.2443 (pp. 1–2), two structural-vocabulary searches (logged below), on
top of Pass 01's eight queries.

**New queries logged:** (9) "secular time dependence cannot be removed field
redefinition wave function renormalization de Sitter self-energy adiabatic";
(10) "frequency space graviton self-energy de Sitter Hubble expansion omega
corrections dispersion relation quantum gravity".

---

## Q1 — Inheritance line (SUBSTANTIALLY ANSWERED, from the TTW full text)

Read via ar5iv, arXiv:2103.08547 confirms: κ² ≡ 16πG (their Eq. 1);
results in **position-space structure functions** (nine for graviton
contributions); flat-space recovery and Capper-1979 comparison in their
§2.2.3; and — decisive for positioning — the paper contains **no
imaginary/absorptive computation, no retarded-kernel construction, no
frequency-domain (ω) representation, no Wigner/average-time decomposition,
no H-expansion of coefficients, and no discussion of removing time
dependence by redefinition or coordinate change** (full-text queries, each
answered in the negative). What the contract inherits from this line: the
diagram class and (via arXiv:2107.13905, still to be read) the
Schwinger–Keldysh retarded conversion. What is the manuscript's own
construction: the Wigner-resolved absorptive extraction, the H-graded
(u_b, ω) coefficient table, and the certificates.

## Q2 — Absorptive precedent (PARTIAL)

Tsamis–Woodard gr-qc/9403056 contains on-shell self-energy sign statements
("the graviton's on-shell self-energy is negative and infrared divergent at
one loop") — a sign-level precedent the manuscript's §3.2 positioning
should acknowledge. No frequency-resolved absorptive dS graviton
coefficients found yet. **Remaining: read gr-qc/9403056's definition of
"on-shell self-energy" and sign convention; search Boyanovsky's dS
self-energy forms for absorptive frequency structure.**

## Q3 — Wigner precedent (STRENGTHENED NEGATIVE, pending breadth)

The nearest primary source affirmatively does **not** use the Wigner
decomposition (full-text answer, not search absence). Generic
nonequilibrium-QFT Wigner methods remain standard (Pass 01). **Remaining:
targeted search for Wigner/average-time resolution applied to any
gravitational self-energy.**

## Q4 — Coefficient-equivalence test (OPEN; H⁰ mapping anchored)

The H⁰ cross-check (owner-authorized, positioning/normalization only) is
anchored: TTW §2.2.3 recovers flat space and matches Capper 1979 under
κ² = 16πG. Completing the check requires equation-level extraction of the
flat structure-function coefficient and a convention map (their FT and TT
conventions vs the contract's κ = 1, ⟨hh⟩ = P^TT×W, e^{+iωΔ} retarded
transform). Web-fetch fidelity at equation level is limited; **the check
may require the owner to pull the PDF equations; alternative source: TW
hep-ph/9602317's flat-limit section.** No literature match found yet for
the certified signatures (H¹ = 0 at this level; the u_b-odd H³ term; the
mixed H⁴/H⁶ coefficients; the ω⁻² power).

## Q5 — No-go equivalence (MAJOR FINDING: the removability discourse exists)

The owner's prediction was right: there is an active literature on whether
dS secular time dependence is removable, in exactly the alternative
vocabularies listed —

- **Removal side:** time-dependent wave-function renormalization ψ → Z_ψ(t)ψ
  canceling quantum corrections (surfaced in the 1609.03293 line);
  counterterm schemes eliminating secular growth order by order (PRD 110,
  123536); Soft de Sitter Effective Theory renormalization/matching
  (arXiv:2603.09438); dynamical-RG resummation (JHEP 04 (2020) 064);
  all-loop dS wavefunction renormalization (arXiv:2603.08794).
- **Non-removal side:** Kitamoto–Kitazawa, arXiv:1402.2443 (read, pp. 1–2):
  soft-graviton IR effects render quartic/Yukawa/gauge couplings and
  Newton's constant time-dependent; the effects are argued to be
  *"the inevitable consequence of the general covariance"* leading to
  *"gauge invariant predictions"* — an existing statement that certain dS
  time dependence is physical/observable, for **couplings**, via IR-log and
  conformal-mode arguments, IR-cutoff-sensitive at one loop.

**Assessment so far:** neither side treats the graviton absorptive
self-energy in Wigner form, and no coefficient-certificate-style argument
has surfaced; but equivalence-of-content is NOT yet excluded — the
Kitamoto–Kitazawa non-removability claim and the SdSET/counterterm
removability claims must be read at the level of *which objects* they cover
and *which transformations* they quotient. The manuscript's positioning
must cite both sides regardless of the novelty outcome. Note one clean
structural difference to check when reading: the certified coefficients are
IR-finite on the stated domain (dimensional continuation, no explicit IR
scale), whereas the Kitamoto–Kitazawa effects are IR-cutoff-sensitive —
if sustained on full reading, this cleanly separates the statements.

## Q6 — Transform/memory references (unchanged; standard)

## Q7 — Observational conversion (HELD, per ruling)

Test to apply when evaluated: if the map from the certified Im Σ_R to an
existing GW observable requires Re Σ, a dressed propagator, or a transport
calculation, the answer is **"not presently supportable."** No conversion
attempted in this pass.

## Q8 — Novelty (NO LANGUAGE; gates unchanged)

---

## Session-2 findings (2026-09-21, continuing)

**Queries logged (cont.):** (11) "Kadanoff-Baym graviton kinetic equation
Wigner function gravitational wave transport curved spacetime self-energy".
**Primary sources read (cont.):** Kitamoto–Kitazawa 1402.2443 (key sections
via PDF text extraction); TW hep-ph/9602317 (flat-limit section via ar5iv,
equation level); SdSET 2603.09438 (abstract).

### Q5 — Kitamoto–Kitazawa branch CLOSED at read level

Their transformation IS the time-dependent wave-function renormalization
class: Z_φ(τ), Z_ψ(τ) ≃ 1 − c·κ²H² log a(τ) (their eqs. 3.11, 3.20, 6.3–6.4).
Their objects: MATTER kinetic terms and couplings (gauge e, quartic λ₄,
Yukawa λ_Y, Newton's G), corrected by soft-graviton IR logarithms with an
explicit comoving IR cutoff ε₀ (their eq. 1.12) sourced by the super-horizon
scale-invariant spectrum. Their own split: kinetic-term IR logs CAN be
absorbed ("the IR logarithms due to soft gravitons can be eliminated in the
free field theories after the wave function renormalization"); effective-
coupling shifts SURVIVE and are argued gauge-invariant/covariance-forced.
**Discriminating comparison (now precise):** same transformation vocabulary
(time-dependent amplitude rescaling — a SUBSET of the manuscript's tested
class, which adds clock reparametrization), but DISJOINT objects (matter
couplings vs the graviton absorptive self-energy) and DISJOINT mechanisms
(IR-cutoff-sensitive log a(τ) growth vs IR-finite polynomial (Hu_b)^n
dependence on the ω ≳ 3.4H domain with no explicit IR scale). The
certificate is NOT their argument in disguise; conversely their result must
be cited as the existing "dS time dependence can be physical/observable"
line. Their §4 on-shell/off-shell IR-cancellation-by-redefinition mechanism
(energy-resolution regularization) is an adjacent matter-self-energy IR
statement, not a graviton absorptive-coefficient statement.

### Q5 — removal-side scope (abstract level)

SdSET 2603.09438: massless SCALAR correlators (trispectrum, six-point,
one-loop power spectrum); no self-energies, no gravitons, no absorptive
parts, no rescaling/reparametrization transformations surfaced at abstract
level. PRD 110, 123536 and JHEP 04 (2020) 064 remain to be scoped, but the
pattern is consistent: the removal-side literature acts on scalar
correlation functions.

### Q4/H⁰ — the flat-limit cross-check: **INCOMPARABLE-AS-CONSTRUCTED**

Equation-level data extracted from TW hep-ph/9602317: renormalized flat
self-energy their Eq. (3.6),
[Σ_flat] = (−iκ²)/(60(2π)⁴)·{(23/2)ηη∂⁴ + (61/2)η^{α(ρ}η^{σ)β}∂⁴
− (23/2)[η∂∂ + η∂∂]∂² − 61 ∂η∂∂² + 42 ∂∂∂∂}(1/x⁴); agreement with Capper in
gauge α = 1, β = −1/2; κ² ≡ 16πG; field g = Ω²(η + κψ); NO TT-projected
scalar coefficient given; NO absorptive analysis. A naive double-TT
projection (only the (61/2) structure survives transversality +
tracelessness) with the standard FT/discontinuity of ∂⁴(1/x⁴) yields an
absorptive coefficient of order 61κ²/(1920π), against the contract's
3/(1280π) = 4.5/(1920π) (κ = 1 units): **no recognizable convention factor
bridges 61 vs 4.5, and the honest verdict is that the comparison is
between DIFFERENT DECLARED OBJECTS** — TW's full pseudo-graviton loop in a
fixed gauge vs the contract's declared TT-bath internal legs (the program's
own D3(iii): TT-bath uniqueness NOT claimed) — with at least five
unresolved mapping layers (per-index-pair TT normalization; ψ-vs-h field
factors; the −i/sign chain; the contract's κ-bookkeeping; gauge). The
off-shell TT-projected coefficient is not gauge-invariant, so coefficient
identity across gauges is not even expected. **What WOULD close a
comparison: a gauge-invariant on-shell absorptive quantity computed on both
sides — future work adjacent to the Re Σ/Ward line; not performed (no new
physics branch).** Positioning consequence: the paper may cite TW (3.6) /
Capper as the flat ANCHOR of the literature line while stating that its own
flat coefficient belongs to the declared TT-bath construction and is not
directly comparable — this PROTECTS the paper from a referee "checking"
A₀ against Capper and claiming error.

### Q3 — sharpened negative

KBE/Wigner methods in curved spacetime are established for MATTER transport
(e.g. arXiv:0807.4551, Boltzmann from Kadanoff–Baym in curved spacetime;
hep-ph/0002012), including FRW backgrounds. The sharpened search (query 11)
surfaced no application to a graviton self-energy. Negative now holds
against both generic and sharpened queries; still not proof of absence.

## Remaining reading list (to close Pass 02)

1. arXiv:2107.13905 — the Schwinger–Keldysh retarded conversion the
   contract inherits (defines the inheritance boundary precisely). [OPEN]
2. ~~TW flat-limit equations~~ [DONE — verdict INCOMPARABLE-AS-CONSTRUCTED,
   see above; equation-level data on file.]
3. ~~Kitamoto–Kitazawa full read~~ [DONE at key-section level — branch
   closed, see above.]
4. PRD 110, 123536 + JHEP 04 (2020) 064 — removal-side scope confirmation
   (SdSET done at abstract level: scalar correlators only). [OPEN]
5. gr-qc/9403056 — the on-shell sign statement and its convention. [OPEN]
6. Boyanovsky dS self-energy papers — absorptive frequency structure. [OPEN]

**No manuscript edits in this pass. v3 (sha a8b4ccda…7706) untouched.**
