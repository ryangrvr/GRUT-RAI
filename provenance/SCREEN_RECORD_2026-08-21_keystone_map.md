# Screen record — `RUNG3_KEYSTONE_MAP.md` (2026-08-21)

> **Hostile pre-screen per CHARTER §1.3**, charged against the owner's eight screening points,
> defaulting to broken. Method: direct numerical verification of every derivable claim
> (embedding constraints, induced metrics, invariant reductions), then three refuter lenses
> (over-claim / physics-math / consistency) over each point. **Nothing banked; register
> untouched by this process.**

## Verdict summary

| # | owner's screening point | verdict |
|---|---|---|
| 1 | D1 (T = t on the origin worldline) | **PASS** — verified |
| 2 | D2 (no global off-axis identification) | **AMENDED** — refined wording; an embedding error caught and fixed here |
| 3 | D3 (stationarity / spectral density clock-dependence) | **AMENDED — SPLIT into D3a/D3b**; the original blanket claim was FALSE as stated (the screen's main catch) |
| 4 | D4 (exponential relaxation not globally preserved across clocks) | **PASS** — identity verified numerically |
| 5 | D5 (N = Ht) / D6 (KMS-temperature pairing) | **PASS with condition** — D6's BW/Sewell attribution owes primary-source verification before any bank |
| 6 | "Ht ≈ 1 vs Ht ≳ 4.3 not legitimate as filed" | **STANDS AT NARROWER SCOPE** — one of its three defect-legs was removed by D3a; the other two suffice |
| 7 | "the ladder is the STATE's, not the dynamics'" | **LEGITIMATE** — fence added: temperature is clock-form-universal; manifestation is kernel-route-dependent |
| 8 | primitive-inversion / modular-clock identification | **WEAKENED + ONE REFUSAL** — see below |

## The catches (both found by attempting to verify, not by reading)

### Catch 1 — static-patch embedding typo (§1.2)
The map's static embedding read Xᵢ = Hr·nᵢ. Direct constraint check failed:
−X₀²+X⃗²+X₄² ≠ H⁻² off-axis (error r²(H²−H⁴r²)... concretely 1/H² − r²(1−H²r²)·0 − ... computed
numerically at H=1.7, r=0.22). Corrected to Xᵢ = rnᵢ, after which the constraint holds to 1e-12
and D1 is unaffected (axis values identical either way). **Lesson recorded:** the map's own rule —
derive or verify every metric statement — applies to its own §1.2 prose.

### Catch 2 — D3 was overstated; geodesic stationarity holds in cosmic time (§1.2)
The original D3 claimed ρ(ω) "does not exist w.r.t. cosmic time" without qualification.
Numerical falsification: for pairs at equal comoving position, the invariant reduces EXACTLY to

    z = H⁻² cosh(H Δt),   independent of t₀   (verified to 12 decimals, three t₀ samples)

— the classical Gibbons–Hawking geodesic-detector result, derived here from the embedding
rather than cited. So a one-time Fourier transform DOES exist w.r.t. cosmic time along any
comoving worldline, which **licenses the QBM toy's silent clock for along-worldline kernels**.
What survives (also verified): for spatially separated pairs z depends jointly on t₁+t₂ and Δt,
so the FULL object Σ(x;x′) still admits no global reduction; only the static patch offers one
globally (Killing stationarity).

**Cascade applied on the map's face:** D3 split into D3a (worldline stationarity — new, and it
STRENGTHENS part of the toy) and D3b (no full-kernel reduction — survives); C1 re-scoped ("still
NO as filed" but no longer killed by pure clock-conversion); C2's locus moved from "wrong clock"
to "missing reduction + wrong object"; C3 downgraded from violation to licensed-at-scope; C7's
reason upgraded (unperformed reduction, not contradiction); E6 fence added; §1.4 rewritten;
§6.1 weakened from "the modular clock IS the ladder's clock" (interpretation, not derivation) to
"the ladder follows the state's TEMPERATURE, which is clock-form-universal."

### Refusal — response ⇒ unique primitive (owner's job-3 reading)
The reading that primitive inversion asks whether "the structure visible in response theory
uniquely determines the microscopic/modular structure that generated it" is **REFUSED** at this
map's scope: Mori–Zwanzig coarse-graining is many-to-one; distinct microscopics wash to the same
low-frequency influence functional, so invertibility is almost certainly false as stated. The
defensible version is the u4/u5 classification (default-BROKEN, first-class failure states).
Recorded at §6.5 so it is not re-raised from the flattering direction.

## Item-by-item detail

**1. D1 — PASS.** Verified: flat(t,0) and stat(t,0) map to the same embedding point (invariant
of a point with itself = H⁻²) for sampled t; sinh/cosh identification monotone. "Origins
alignable" is the right hedge — the offset is conventional.

**2. D2 — AMENDED.** Two findings. (a) The embedding typo (Catch 1). (b) Over-claim lens:
"no global clock conversion exists" is too strong — pointwise coordinate maps exist since both
T and t are time functions on the shared region; the true statement is that no conversion
preserves the stationary/spectral FORM of both descriptions. Amended on the face.

**3. D3 — AMENDED/SPLIT (the screen's material result).** See Catch 2. The amended pair D3a/D3b
is stronger than the original in one direction (it licenses the toy's clock at worldline scope,
removing an illegitimate leg from C1's kill) and unchanged in the direction that matters for
the dispatch (D3b). Physics-math lens confirmed the cosh identity analytically: expanding the
embedding products, all t₁+t₂ terms cancel at equal x, leaving H⁻²cosh(HΔt).

**4. D4 — PASS.** e^{−Γt} = (HT)^{−Γ/H} with HT = e^{Ht} verified numerically to 1e-12 at
sampled Γ, t. Consequence (rate comparisons across O(1/H) elapsed time are clock-dependent)
stands untouched.

**5. D5 / D6.** D5 trivially exact on dS; FRW half correctly marked assumed. D6's attribution
(BD KMS w.r.t. boost flow at T = H/2π; BW/Sewell structure) is consistent with the literature
the program already tracks, but **no sources.json entry currently verifies it directly**
— condition below. Note the D3a refinement: T_dS governs BOTH reductions, so D6's warning is
about kernel construction and scope-naming, not about a unique "Killing-only" temperature.

**6. The headline conclusion — STANDS AT NARROWER SCOPE.** Of the three defect-legs originally
charged against the "Ht ≈ 1 vs Ht ≳ 4.3" filing, D3a removed the pure clock-conversion leg.
Surviving legs, each independently sufficient: elapsed-time-vs-relaxation-time conflation;
dS-H history vs H₀ question (D5); rung3's asserted object not yet shown to be an along-worldline
kernel (D3b + wall A); D4 locality on rate language. Verdict "not legitimate as filed" is
therefore **correct but for corrected reasons** — which matters, because a refuter who had run
D3a against the original text could have collapsed the whole objection and walked the
conclusion out as over-reach. This is exactly the failure shape CHARTER §1.4 names.

**7. "The ladder is the STATE's" — LEGITIMATE with fence.** Grounds verified: coth poles
present for any J (uniform residue), c-selectivity argument (E2), G_E pole-free at Matsubara
points. Fence added at E6: the KMS weight is clock-form-universal; WHICH kernel manifests the
ladder is route-dependent (E7's two-answer). Both boxed implications recorded: free ladder ⇒
neither the memory pole NOR its impossibility.

**8. Modular-clock identification — WEAKENED; invertibility REFUSED.** Original §6.1 sentence
was interpretation dressed as derivation; D3a forced its replacement (temperature-universality
formulation). The load-bearing open point is unchanged and correctly located at
`PRIMITIVE_INVERSION_SCOPE.md` §5 (whether the flow THE KERNEL USES is the state's modular
flow). The owner's stronger reading — response theory uniquely determining the primitive — is
refused at §6.5 (many-to-one coarse-graining).

## Conditions for re-verdict (AMBER → GREEN)

1. Owner adjudicates the two amendments (this record + the map's face changes).
2. D6/BW-Sewell attribution: verify against primaries and add `sources.json` entries BEFORE any
   claim cites it (the map itself needs no entry — it banks nothing).
3. Targeted re-screen of the amended sections only (§1.2 D2/D3, table C1–C3/C7, §1.4, E6, §6)
   by a lens not used here.
4. The firewall ledger stands as the owner framed it: strengthened = the adverse clock comparison
   invalid-as-filed (at narrower scope); established = the free spectral structure at documented
   scope; unknown = the assembled interacting G_R^TT; NOT established = pole, cut, memory time,
   τ₀, or cosmological behavior. No wording anywhere in the map may drift past this line.

## Firewall note

Suite before/after both screening sessions: **234 passed / 5 failed / 1 skipped**, failures
byte-identical declared reds; `validate.py` PASS throughout; register byte-identical. Nothing in
this process fixed, softened, or touched the guards.

