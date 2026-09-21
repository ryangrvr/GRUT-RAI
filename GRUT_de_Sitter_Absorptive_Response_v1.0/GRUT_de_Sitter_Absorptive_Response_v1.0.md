# Wigner-time structure of one-loop graviton dissipation in de Sitter space: certified absorptive coefficients through sixth order in H and a no-go for stationary dressings

**D. Ryan Grover**

*Version 1.0 — September 21, 2026.*

*Publication note: this document is the frozen scientific manuscript of the
GRUT research program's terminal calculation campaign, prepared for open
deposit. The scientific content was frozen before this preparation; the
present version differs from the frozen text only in this front matter, the
completed bibliography, and typesetting. All verification is in-house; no
external review has yet occurred (§7, item 9).*

**Author/Scope note.** What is calculated here: the Wigner-time-resolved
absorptive part of the one-loop pure-graviton self-energy on de Sitter
background, through sixth order in H, under a fully declared contract, with
representation tests and their certificates. What is inherited from prior
work: the underlying self-energy object, diagram class, and
Schwinger–Keldysh retarded conversion (§2, §6.5). What is not claimed: any
observational prediction, any resolution of the de Sitter secular/gauge
debate, any result beyond the declared contract and its stated domain
(§6.4, §7).

---

## Abstract

We compute the Wigner-time-resolved absorptive (dissipative) part of the
one-loop
pure-graviton self-energy on a de Sitter background, within a fully declared
contract (transverse-traceless internal legs, adiabatically dressed mode
functions, zero external spatial momentum, dimensional continuation), through
sixth order in the expansion rate H. With x = H·u_b (u_b the Wigner time) and
y = H/ω, the certified result is

> Im Σ_R(ω>0) = (ω⁴/1280π)·P(x, y),
> P = −3 − (104/3)y² + 24x³ − (472/3)xy² − 18x⁴ + 220x²y² − 127y⁴
>     − 48x⁶ + (3448/3)x⁴y² − 3312x²y⁴ − (1280/3)y⁶,

valid for ω ≳ 3.4H, with the H⁵ sector quarantined (extracted in its
delta-class only; see §7). The H¹ sector vanishes exactly; H³ supplies the
first u_b-odd (time-asymmetric) dissipative term. We establish, by a
parameter-free coefficient certificate, that no representation of the form
F(Hu_b)·(ω̃⁴/1280π)·T(H/ω̃) with ω̃ = ω·g(Hu_b) — encompassing all
time-dependent amplitude dressings, frequency rescalings, and their
combinations, corresponding at leading adiabatic order to the action of
local field rescalings and time reparametrizations — reproduces the certified
coefficients. Under the frozen retarded convention, and assuming the retarded
kernel is real at fixed u_b, the certified non-analytic absorptive terms
reconstruct for Δ > 0 as power-law memory tails; the u_b-dependent
contributions occur in the faster-decaying tails (Δ⁻⁵, Δ⁻³, Δ⁻¹), while the
deepest certified infrared contribution (ω⁻²) is u_b-independent at this
order. Local counterterms cannot alter the Δ > 0 content of this certified
non-analytic absorptive sector. No observable is claimed; the calculation is
a result of standard quantum field theory on de Sitter space.

---

## 1. Introduction

How does the dissipative response of the gravitational vacuum depend on
cosmic time? On a de Sitter background the question is sharp: the background
has no global timelike Killing vector adapted to the spatially flat slicing,
so a two-point response kernel Σ_R(t, t′) need not be a function of t − t′
alone. Whether — and in precisely what structural way — the one-loop graviton
self-energy departs from stationarity is a well-posed, computable question,
and this paper answers it at the level of the absorptive (imaginary,
dissipative) part, through sixth order in H, within a fully declared
calculational contract.

The result is presented in the order of its logical construction:
the calculation (§2); the certified absorptive structure (§3); the exact
Fourier/distributional mapping to relative-time memory structure, with its
single physical premise stated explicitly (§4); the representation test — a
no-go certificate for stationary dressings (§5); physical interpretation
(§6); limitations (§7); and what remains unresolved (§8). Section 9 records
provenance. This ordering is deliberate: every interpretive statement in §6
is downstream of a certificate or an exact mapping in §3–§5, and the
qualifications of §7 are part of the result, not caveats appended to it.

This work originated in a research program (GRUT) investigating a
"responsive-vacuum" interpretation of gravitation; the program's own audit
concluded that no result herein distinguishes that interpretation from
standard quantum field theory on de Sitter space (§6.4, §9). The calculation
and its certificates stand independently of any interpretation.

## 2. The calculation

The one-loop graviton self-energy on de Sitter backgrounds is an
established object: computed by Tsamis and Woodard [TW96], with a
flat-space limit matching Capper's gauge-fixed computation [C79, as
matched in TW96]; recomputed from gravitons in cosmology, with a
nine-structure-function representation, by Tan, Tsamis and Woodard
[TTW21a]; and converted to a retarded Schwinger–Keldysh form and applied
to gravitational radiation in [TTW21b], whose conversion (Σ_ret from
Σ₊₊ + Σ₊₋) the present contract inherits. The Wigner-resolved absorptive
construction and everything downstream of §3 are the present work's own
(§6.5).

The object is the retarded self-energy of the transverse-traceless (TT)
graviton on a de Sitter background of expansion rate H, at one loop in the
pure-gravity sector, under the following declared contract (all elements
frozen before computation; see §9 for the audit trail):

- **Internal legs:** the declared TT bath, ⟨hh⟩ = P^TT × W, with the
  Wightman kernels W± = (κ²/q)e^{∓iq(u−u′)}[(1−Hu)(1−Hu′) ± iH²(u−u′)/q +
  H²/q²] — the exact product of linearly dressed adiabatic modes,
  terminating at O(H²) per kernel. TT uniqueness is not claimed.
- **Vertex:** the cubic de Sitter vertex reduced to H-graded bilinear
  C-matrices on the spatial pair basis (maximum H-degree 2).
- **External kinematics:** frequency ω at zero external spatial momentum,
  reached as a controlled k → 0 limit (never the literal point), with an
  executed two-axis isotropy gate.
- **Radial sector:** dimensional continuation only, no explicit IR scale;
  angular averages at symbolic dimension d, with d → 3 taken term-by-term
  (smoothness verified at each order).
- **Retarded convention (frozen, quoted):** Σ_R = −iθ(Δ)·RET with
  Σ̃_R(ω) = ∫₀^∞ dΔ e^{+iωΔ} Σ_R(Δ) — the upper-half-plane-analytic
  transform. The absorptive part is extracted from the ω = +2q cone of the
  loop integrand by the Sokhotski delta class, with a reality gate (iⁿcₙ
  real) enforced per Δ-degree; for the present ω > 0 absorptive
  delta-class extraction the opposite cone has no support (its delta class
  lies at q = −ω/2, outside the measure domain; both cones carry independent
  content for the dispersive part — §8) — verified per degree, term by term.
- **Units:** κ = 1; all coefficients below are exact rationals over π.

The two-time structure is carried in Wigner variables: u_b = (u+u′)/2 (the
Wigner time) and Δ = u − u′, with the transform taken in Δ at fixed u_b. The
expansion is H-graded; the source object carries H-degree 8, of which orders
0–6 are extracted here (orders 7–8 were removed by a builder-level truncation
prior to caching and are outside the certificate; §7).

## 3. The certified absorptive structure

The certified result, with x = H·u_b and y = H/ω:

**Im Σ_R(ω>0) = (ω⁴/1280π) · P(x, y)**

| order | contribution to P | status |
|---|---|---|
| H⁰ | −3 | complete; three independent routes agree |
| H¹ | 0 | complete — vanishes exactly |
| H² | −(104/3)·y² | complete; u_b-free |
| H³ | +24x³ − (472/3)·x·y² | complete — first u_b-odd term |
| H⁴ | −18x⁴ + 220x²y² − 127y⁴ | complete |
| H⁵ | (416/3)x³y² − 496xy⁴ | delta-class only — **quarantined**, never binding |
| H⁶ | −48x⁶ + (3448/3)x⁴y² − 3312x²y⁴ − (1280/3)y⁶ | complete — first negative ω power |

"Complete" means: extracted through gated machinery whose per-degree reality
preconditions all hold, whose d → 3 reduction is smooth piece-by-piece, and
which reproduces the independently established H⁴ coefficient exactly as a
prerequisite gate on every run. At H⁵ the reality precondition fails at one
Δ-degree — the condition under which the extraction's own derivation states
that principal-value content leaks into the absorptive part — so only the
delta-class content is reported there and no binding statement uses it.

Structural features of the certified table:

1. **Validity domain.** The record's own derived boundary is
   ε_H = (104/9)H²/ω², with refusal at ω = √(104/9)·H ≈ 3.399H — the ratio
   of the H² to H⁰ coefficients. The u_b-free tower (−3, −104/3, −127,
   −1280/3) has successive ratios ≈ 11.6, 3.7, 3.4; this three-term pattern
   is suggestive of a lower characteristic scale near ω ∼ 1.8H but does not
   establish a convergence radius — the operative boundary remains the
   refusal at 3.399H.
2. **Sign.** The ≤H⁴ truncation is analytically negative on the stated
   window (exact maximum −599127/270400). The H³/H⁶-inclusive expression
   was negative at every tested grid point, for both signs of u_b — grid
   verification, not an analytic proof. Accordingly, no gain/instability
   was observed within the tested domain.
3. **Time asymmetry.** The first u_b-odd absorptive contribution enters at
   H³ (odd in u_b, even under the joint flip (H, u_b) → (−H, −u_b), as the
   construction's parity mechanism requires), establishing Wigner-time
   asymmetry of the dissipative coefficient. This should not be identified,
   by itself, with an arrow-of-time statement.
4. **Secular self-termination.** The u_b-dependence equals the flat response
   at Hu_b = 6^(−1/4) ≈ 0.64 (at y = 0): the certified truncated response is
   restricted to Wigner drifts below this surface by the adopted
   self-termination criterion.

## 4. Fourier/distributional mapping to relative-time structure

Three layers, kept separate.

**4.1 Mathematical mapping (prescription-independent; conditional on the
§4.2 premise).** For the certified spectral terms, and assuming the retarded
kernel is real at fixed u_b, the frozen convention maps the odd extensions
implied by the §4.2 reality premise to the corresponding Δ > 0
contributions via K(Δ) = (2/π)∫₀^∞ Im Σ̃(ω) sin(ωΔ) dω. This extracts the
non-analytic tail associated with each certified term under the stated
prescription; it does not reconstruct the complete physical kernel, whose
spectrum is certified only on the stated frequency domain (§7, item 1). A local
(contact) operator K = c·δ^(n)(Δ−0⁺) has Σ̃ = c(−iω)ⁿ exactly: only odd n
contributes to the absorptive part, and then as an *analytic odd polynomial*.
The certified terms are even powers of |ω| — no certified term is a
local-operator form. Their Δ > 0 kernels, computed identically under two
independent prescriptions (Abel regularization; analytic continuation
Γ(p+1)·sin(π(p+1)/2)/Δ^(p+1)) and confirmed by direct quadrature:

> ω⁴ → +48/(πΔ⁵)  ω² → −4/(πΔ³)  ω⁰ → +2/(πΔ)

— power-law memory tails, not contact terms. Contact/counterterm ambiguities
are supported at Δ = 0 only and cannot affect any Δ > 0 statement.

**4.2 Physical premise (stated, not derived).** Extending the computed
positive-frequency absorptive coefficients to the full odd spectral function
sgn(ω)|ω|^p — the step on which §4.1's reconstruction rests — requires the
retarded kernel to be *real at fixed u_b*. This is a physical reality
condition on the retarded response (standard for retarded responses of
hermitian sources, and consistent with every gate of the extraction,
including the per-degree reality preconditions), **not** something the cached
loop integrand itself proves: the cached object's pointwise form is dressed
by the assembly's derivative-operator routing and is not pointwise
anti-hermitian. The move from computed coefficient to odd extension is
therefore a stated premise of the tail statements, not an identity.

**4.3 Regime limitation (the infrared window).** For the ω⁻² term (H⁶,
u_b-free), the exact Δ > 0 kernel of the IR-cut model — cutoff ω\* at the
domain boundary — is −Δ·Ci(ω\*Δ) + sin(ω\*Δ)/ω\*: it grows as
Δ[1 − γ_E − ln(ω\*Δ)] **within the window Δ ≲ 1/ω\*** (ω\* = 3.399H, i.e.
Δ ≲ 0.29/H) and is bounded oscillation beyond, in the cut model. The
calculation does not determine the asymptotic behavior beyond the window;
"indefinitely growing secular tail" is *not* a licensed description.

## 5. The representation test: a no-go for stationary dressings

**5.1 The tested class.** Consider representations

> Im Σ = F(x) · (ω̃⁴/1280π) · T(H/ω̃),  ω̃ = ω·g(x),

with F, g analytic (F(0) = g(0) = 1) and T arbitrary through the matched
order. The declared class contains time-dependent amplitude dressings
(g ≡ 1), frequency rescalings (F ≡ 1), and their combinations; in the
leading-adiabatic (Wigner-local) construction used here, it corresponds to
the action of local field rescalings h → Z(u_b)h and time reparametrizations
u → f(u) on a stationary law.

**5.2 The certificate.** Matching the class to the certified table on every
complete slot through total order 6 proceeds as a chain of single linear
equations: the pure-y slots fix t = (−3, −104/3, −127, −1280/3); the measured
H¹ = 0 and H³ data pin the odd parameters f₁ = 118/13, g₁ = −59/26; the
(2,0)/(2,2) slots fix f₂ = 1336/169, g₂ = 14733/1352; and the x²y⁴ slot is
then **parameter-free**: the class requires −169672/169 ≈ −1004.0, while the
complete H⁶ datum is −3312. The residual 390056/169 ≠ 0 refutes the entire
class on complete data, independent of the quarantined H⁵ sector (which
enters no matched slot). Narrower certificates refute the amplitude-only and
rescaling-only subclasses already at H⁴.

**5.3 Robustness.** Because the certified content is non-analytic (§4.1),
local counterterms cannot generate or remove any certified coefficient: the
no-go concerns content that is not a renormalization convention. Beyond
leading adiabatic order, the redefinition orbit acquires gradient
corrections, bounded by the computed field E = (H/ω)|∂ₓP|/|P|. At three of
the fifty evaluated grid points (larger H/ω, the u_b-odd side) the certified
obstruction exceeds the computed gradient-correction bound; at those points
the no-go extends to the tested full orbit. Elsewhere only the
leading-adiabatic statement is claimed.

**5.4 The Wigner-local approximation, quantified.** The same field E measures
the error of replacing the two-time response by a local-frequency form: it
reaches ≈ 0.33 on the tested inner domain (ω ≥ 5H, |Hu_b| ≤ 0.3) and ≈ 1.68
at the ω ≈ 3H edge, dominated by the u_b-odd H³ term. On the tested inner
domain the Wigner-local reduction carries an error reaching approximately
33%, and therefore is **not certified as a controlled reduction** under the
preregistered 20% criterion. Any use of G_R(ω, k) in place of G_R(t, t′; k)
on this domain inherits that error.

## 6. Physical interpretation

**6.1 The central statement.** Within the frozen retarded convention, and
assuming the retarded kernel is real at fixed u_b, the certified non-analytic
absorptive terms reconstruct for Δ > 0 as power-law memory tails. The
u_b-dependent contributions occur in the faster-decaying tails, while the
deepest certified infrared contribution is u_b-independent at this order.
This statement concerns the certified non-analytic absorptive sector; local
counterterms cannot alter its Δ > 0 content. The time-domain behavior of the
ω⁻² contribution remains bounded by the stated infrared window, beyond which
the calculation does not determine the asymptotic behavior.

**6.2 Cosmic-time dependence and memory are not the same thing.** The
original intuition motivating this program fused them; the calculation
separates them. Within the certified response, cosmic-time dependence and
memory *depth* are anti-correlated: the explicitly time-dependent
pieces ride the short-memory tails (Δ⁻⁵, Δ⁻³, Δ⁻¹), and the deepest
certified memory contribution is stationary at this order. Equivalently, in frequency space: no
time-dependent amplitude, no time-dependent clock, and no combination of the
two turns the certified response into a stationary law (§5.2) — yet the
component that most resembles genuine long-time memory carries no explicit
cosmic-time dependence at this order.

**6.3 What kind of result this is.** Every statement above is a result *of*
standard quantum field theory on de Sitter space, obtained within the
declared contract. The calculation provides the Wigner-time-resolved
absorptive coefficients at H³, H⁴, H⁶, including the exact H¹ vanishing and
the first u_b-odd term, together with the stationarity no-go certificate,
the tail/nonstationarity anti-correlation, and the quantified
Wigner-reduction error; a supported novelty statement awaits a documented
literature search. No claim of physics beyond standard QFT is made. The
stationarity no-go is therefore a structural statement about the calculated
self-energy, not an experimental discriminator.

To the best of our knowledge, following the literature search documented
in the program record, the specific Wigner-resolved, H-graded absorptive
coefficient hierarchy studied in this work — including the u_b-odd H³
contribution — and the associated parameter-free stationary-dressing
inconsistency certificate have not previously been reported in this form.
The underlying de Sitter graviton self-energy, its infrared/secular
behavior, absorptive self-energy phenomena in de Sitter, and the broader
question of whether de Sitter time dependence can be removed or
interpreted physically are established subjects with substantial prior
literature (§6.5).

**6.4 Interpretation programs.** A "responsive-medium" reading of the
gravitational vacuum is *consistent with* this structure — an expanding
background carrying time-dependent response that no stationary dressing
absorbs — but nothing here distinguishes such a reading from standard QFT on
de Sitter; the originating program's own audit records that its prediction
ledger is empty and no discriminating observable survived its gates. The
computed absorptive response is parametrically Planck-suppressed; no
observable is claimed. This question was assessed in the literature pass
and is not presently supportable from the certified calculation: every
conversion route examined imports a dressed propagator / response
calculation, establishment of the relevant gauge-invariant status of the
off-shell coefficient, or the additional low-frequency/transport
calculation required for the proposed observable routes.

**6.5 Relation to prior work.** The physical interpretation of secular
effects in de Sitter quantum gravity has been debated, including arguments
concerning gauge dependence, infrared regularity, and the definition of
observables. The present calculation does not resolve that broader debate.
Its stationarity result is instead a statement about the declared
self-energy object and the specified class of amplitude and frequency
dressings.

The closest existing result is [TTW21b]: solving retarded effective field
equations in position space, single-graviton loops produce secular growth
of graviton mode functions, u₁ → (κ²H²/4π²)(4/3)ln²a·u₀, with breakdown
at κ²H²ln²a ~ 1. That is a loop-counting/secular-growth criterion; the
present secular surface Hu_b ≈ 0.64 is a kinematic boundary of the
adopted one-loop H-graded truncation. The two belong to the same de
Sitter infrared/secular physics family but are not competing estimates of
the same quantity. On the physical status of such effects: the negative,
infrared-divergent on-shell graviton self-energy goes back to [TW95];
critiques and gauge/slicing analyses include [DEZ94] and [GT08]
(with reply [GT-R]); infrared-regularity programs include [TU14]; recent
work argues gauge independence of graviton-loop logarithms once
source/observer correlations are included [GIL24]; and soft-graviton
corrections to matter couplings have been argued to be physical and
covariance-forced, with time-dependent wave-function renormalization
absorbing kinetic but not coupling corrections [KK14]. On the removal
side, infrared/secular growth of *scalar correlators* is systematically
absorbed by counterterms in dimensional regularization [HHPS24], treated
in Soft de Sitter Effective Theory [SdSET], and resummed by dynamical
renormalization group methods [DRG]. These transformations act on scalar
correlation functions or matter couplings; none acts on the graviton
absorptive self-energy studied here. Open-system treatments of the
primordial *tensor* spectrum, with explicitly non-Markovian structure
beyond the strict Markovian limit, appear in [OEFT22] — the framework
family within which a two-time treatment of the present certified kernel
would naturally sit. Absorptive and nonstationary self-energy phenomena
on de Sitter are established for matter fields: dS-allowed decays
[BEM10], initial-value nonstationary self-energies and decay widths with
Bose enhancement at T = H/2π [B-line]. Wigner/Kadanoff–Baym two-time
methods are standard in nonequilibrium field theory, including matter
transport in curved spacetime [KBE]; the literature search documented in
the program record did not identify an application producing the
Wigner-resolved absorptive graviton self-energy hierarchy studied here.
Finally, the flat-space calculations [C79, TW96] provide a diagrammatic
and normalization historical anchor; no coefficient identity is asserted
between the present flat coefficient and the gauge-dependent off-shell
coefficient of those calculations, because the compared projected objects
differ in gauge and construction (general-gauge dependence of the
graviton self-energy is itself classical literature [GG78]).

## 7. Limitations

The following are part of the result.

1. Validity domain: ω ≳ 3.4H within the declared truncated expansion
   (boundary derived; coefficient chart-dependent); no claim is made for
   ω < 3.4H.
2. Wigner-time window: secular self-termination at Hu_b ≈ 0.64 (y = 0);
   statements tested at |Hu_b| ≤ 0.5.
3. H⁵ quarantined (delta-class only; a principal-value completion is
   absent); H⁷/H⁸ not extracted (source object degree 8).
4. Re Σ_R not computed: no pole structure, no μ-anchored dispersive
   statement, no full G_R resummation.
5. The Wigner-local reduction is not certified as controlled (§5.4): ~33%
   error on the tested inner domain against a preregistered 20% criterion.
6. The full-orbit form of the stationarity no-go holds on its computed
   subdomain only; elsewhere the statement is leading-adiabatic-order exact.
7. Long-Δ statements beyond Δ ≈ 0.29/H are not licensed; the ω⁻² kernel's
   form beyond the infrared window is undetermined (§4.3).
8. One loop only; internal bath dynamics absent; the ω → 0 transport class
   is undetermined and is excluded here by prior programmatic reservation.
9. All verification is in-house; no external review has yet occurred.
10. Three auxiliary negatives in the wider program record carry a
    must-be-reopened flag and are not used here.
11. The contract's boundary declarations are temporal only; the status of
    the constant-TT mode under the equivalence relation is unresolved, and
    it is not quotiented by assumption.
12. An earlier internal labeling of the u_b-dependent terms as "local" was
    incorrect and is superseded by §4 (the correction is part of the
    program record).
13. The odd spectral extension rests on the stated reality premise (§4.2);
    the counterterm-invariance claim is scoped to the certified
    non-analytic absorptive sector, not the complete self-energy.

## 8. What remains unresolved

The dispersive side (Re Σ_R via principal-value integrals of both cones —
the two cones carry independent content and neither is reconstructible from
the other by conjugation); the H⁵ completion; the deep-infrared completion
ω ≲ H and with it the transport class of the response (a question that
additionally requires the bath's internal dynamics, beyond one loop); the
H⁷/H⁸ sectors; the boundary/equivalence declaration for the constant-TT
mode at spatial infinity; whether any consistent infrared completion exists
in the smooth-window class after the exclusion of sharp completions; and
the foundational questions the wider program leaves standing (outcome
selection; the origin of ħ; the emergent-versus-fundamental status of the
framework), untouched by everything computed here.

## 9. Provenance and methods

The evidence base is frozen and versioned: (i) the program baseline
`GRUT_REALITY_BASELINE_01` (repository GRUT-RAI, branch v4, commit 5bdda88;
registry sha256 dc693eb6…436a9), itself the output of an audited
reconstruction with a quotation-verified record; (ii) the banked calculation
chain T3-01 through T3-09B in the working repository (instruments, result
files, and complete run logs, including disclosed instrument defects and
their corrections), with provenance-pinned caches for every extracted
object. Every number in this paper is mechanically verified against those
artifacts before commit. Computations were performed symbolically (exact
rational arithmetic throughout; numerical checks by independent quadrature
where stated) with AI-assisted execution under a pre-registration
discipline: outcome classes declared before each computation, adversarial
gates required to pass before any number is read, and refuted premises
disclosed rather than removed. Numerical-method failures encountered en
route (two quadrature/extrapolation mis-setups) are recorded in the run
logs as provenance; they are method episodes, not properties of the
transforms, and the corrected calculations appear in §4.

---

## References

- [TW96] N. C. Tsamis, R. P. Woodard, "One loop graviton self-energy in a
  locally de Sitter background," Phys. Rev. D 54, 2621 (1996);
  hep-ph/9602317.
- [C79] D. M. Capper, "A general gauge graviton loop calculation,"
  J. Phys. A 13, 199 (1980) — the computation referred to as Capper (1979)
  and matched in [TW96] (their Eq. 3.15b).
- [GG78] D. M. Capper, M. A. Namazie, "A general gauge calculation of the
  graviton self-energy," Nucl. Phys. B 142, 535 (1978).
- [TTW21a] S. P. Tan, N. C. Tsamis, R. P. Woodard, "Graviton self-energy
  from gravitons in cosmology," Class. Quant. Grav. 38, 145024 (2021);
  arXiv:2103.08547.
- [TTW21b] S. P. Tan, N. C. Tsamis, R. P. Woodard, "How inflationary
  gravitons affect gravitational radiation," arXiv:2107.13905.
- [TW95] N. C. Tsamis, R. P. Woodard, "Strong infrared effects in quantum
  gravity," Ann. Phys. 238, 1 (1995).
- [DEZ94] A. D. Dolgov, M. B. Einhorn, V. I. Zakharov, "On infrared
  effects in de Sitter background," gr-qc/9403056.
- [GT08] J. Garriga, T. Tanaka, "Can infrared gravitons screen Λ?,"
  Phys. Rev. D 77, 024021 (2008); arXiv:0706.0295.
- [GT-R] N. C. Tsamis, R. P. Woodard, "Comment on 'Can infrared gravitons
  screen Λ?'," Phys. Rev. D 78, 028501 (2008); arXiv:0708.2004.
- [TU14] T. Tanaka, Y. Urakawa, "Strong restriction on inflationary vacua
  from the local gauge invariance III," arXiv:1402.2076.
- [GIL24] "Gauge independent logarithms from inflationary gravitons,"
  arXiv:2402.05452.
- [KK14] H. Kitamoto, Y. Kitazawa, "Time dependent couplings as
  observables in de Sitter space," arXiv:1402.2443.
- [HHPS24] J. Huenupi, E. Hughes, G. A. Palma, S. Sypsas, "Regularizing
  infrared divergences in de Sitter spacetime: loops, dimensional
  regularization, and cutoffs," Phys. Rev. D 110, 123536 (2024);
  arXiv:2406.07610.
- [SdSET] "Renormalisation and matching of massless scalar correlation
  functions in Soft de Sitter Effective Theory," arXiv:2603.09438.
- [DRG] "Dynamical RG and critical phenomena in de Sitter space," JHEP 04
  (2020) 064; arXiv:2001.05974.
- [OEFT22] "Quantum corrections to the primordial tensor spectrum: open
  EFTs and Markovian decoupling of UV modes," arXiv:2206.05797.
- [BEM10] J. Bros, H. Epstein, U. Moschella, "Particle decays and
  stability on the de Sitter universe," Ann. Henri Poincaré 11 (2010);
  see also arXiv:0901.4223.
- [B-line] D. Boyanovsky et al.: hep-ph/9606208; astro-ph/0406287;
  arXiv:1203.3903; arXiv:1712.04522.
- [KBE] Kadanoff–Baym/Wigner methods in curved spacetime: e.g.
  arXiv:0807.4551 (transport from Kadanoff–Baym equations in curved
  spacetime); standard nonequilibrium-QFT texts.

---

*Version note (v1.0): the scientific text of this manuscript was frozen
under the program's verification discipline (three owner edit passes; a
mechanical verification battery re-run at each freeze; positioning
additions applied only after a documented literature pass). Nothing in it
may be strengthened without a corresponding certificate; the thirteen
limitations of §7 travel with any excerpt.*
