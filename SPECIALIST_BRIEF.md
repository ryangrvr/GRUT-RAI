# GRUT — specialist brief (2026-06-25)

> ## STATUS: SUPERSEDED (marked 2026-08-09) — do not dispatch
> The original 2026-06-25 program brief. Superseded by the focused pole-vs-cut ask:
> **`DISPATCH_ONE_PAGE.md`** (send this) + `SPECIALIST_BRIEF_rung3_spine.md` (full attachment).
> Retained for the record; several statements below predate banked reversals (see `STATE.md`).

**What this is.** We model the gravitational vacuum as a responsive medium with finite memory,
treated as an open quantum system via the in-in / Schwinger-Keldysh (Calzetta-Hu) effective
action: a doubled-field influence action with a retarded dissipation kernel K_R and a noise
kernel N, FDT/KMS-locked in equilibrium. We are stress-testing the construction and marking,
ruthlessly, what is *shown* vs *derived* vs *assumed*. Below are load-bearing technical points
where we have done the in-house calculation and want your **reflexive sign-off or refutation** —
not a derivation. Each is a standard open-systems / GR / QFT question. Units ħ = k_B = 1 where used.

The discipline: we are **not** asking you to endorse the program — only to confirm or break the
specific standard-physics claims. "It fails for reason X" is exactly as useful to us as "it holds."

---

## Already settled by you (for calibration / the standard we're holding)

**Q0 — finite-T single-pole. ANSWERED (thank you).** For an s=3 super-Ohmic bath J(ω)∼ω³ with a
smooth UV cutoff, the finite-T coth(ω/2T) factor softens the noise IR exponent (S∼ω² in the
thermal IR, S(0)=0) but the 1/ω from coth is exactly cancelled by one power of ω in J, so
S(ω)=aω²+bω⁴+… is **analytic at ω=0** → no second slow pole. Memory stays cutoff-set; single-pole
holds at finite T. **Boundary you flagged:** a genuine second pole appears only if the bath
susceptibility carries its own dynamical scale (resonance / diffusive mode). We've logged that
boundary — it returns in Q2.

---

## Open questions, by priority

### Q1 (pivotal) — Energy-basis decoherence: does it sample S(ΔE/ħ) or S(0)?

**Setup.** A system with Hamiltonian H_S couples to the fluctuating vacuum via the operator
gravity sees — the mass-energy / stress operator A (Anastopoulos-Hu, *CQG* 30 165007, 2013, derive
decoherence in the **energy** basis). In a Born-Markov reduction the dephasing of coherence ρ_nm
splits into (a) a secular/pure-dephasing part ∝ (A_nn−A_mm)² **S(0)**, and (b) transition parts
∝ |A_nk|² **S(ω_nk)**. Our vacuum noise is super-Ohmic with **S(0)=0**.

**The crux.** If the effective coupling operator A commutes with H_S (gravity couples to the
*conserved* energy), only (a) survives → rate ∝ S(0) = 0 → the vacuum is a **quiet** bath for a
static ΔE superposition. If A carries off-diagonal elements at the Bohr frequency ω_nm = ΔE/ħ
(because gravity couples to the full T^{μν}, not exactly H_S), then (b) gives a nonzero rate
Γ(ΔE) = |A_nm|² S(ΔE/ħ)/ħ².

> **Question:** For gravitational coupling to the stress-energy tensor (à la Anastopoulos-Hu),
> does the energy-basis decoherence of a ΔE superposition sample **S(ω = ΔE/ħ)** (transition-driven,
> nonzero) or **S(0) = 0** (pure-dephasing, suppressed)? I.e. is a super-Ohmic responsive vacuum a
> *decohering* or a *quiet* bath for a static energy superposition?

**Gates:** whether our one tabletop falsifier (energy-basis decoherence, scaling with ΔE and
*not* spatial size Δx — the orthogonal-to-DP/CSL wedge) has **any observable magnitude.** Quiet ⇒
the falsifier is faint, possibly dead.

---

### Q2 (pivotal) — Can a single slow relaxation mode cross w = −1?

**Setup.** We model the cosmological vacuum as a relaxing (viscoelastic) medium with one slow
relaxation time τ₂ ∼ 1/H₀ (horizon scale); w(z) leaves −1 only where the response has power at
ω ∼ H(z). A single **passive** (positive-definite loss) relaxor gives a one-sign deviation; our
toy gives w₀ > −1 with **w_a > 0**. DESI 2024-25 hints at w₀ > −1 **with w_a < 0** — a crossing of
the phantom divide (quintom). We are aware of the standard no-go (a single minimally-coupled scalar
/ single barotropic fluid cannot cross w = −1 without ghost/gradient pathology).

> **Question:** Does the in-in (Calzetta-Hu) effective stress tensor of a vacuum with a **single**
> horizon-scale relaxation mode permit w(z) to cross w = −1 (quintom, w_a < 0), or does a
> phantom-divide crossing require **two** modes / a sign-indefinite (non-passive) response — i.e.
> does the standard no-go apply to a dissipative-vacuum relaxor?

**Gates:** whether rung-7 w(z) can match DESI as a second differentiator with **one** parameter
(the economy win), or whether crossing costs a second mode (eroding it). If "needs two modes,"
w(z) is no longer a cheap differentiator.

---

### Q3 (confirm — low priority) — Is GW dissipation Planck-suppressed beyond reach?

**Setup.** Kramers-Kronig ties the elastic Re[χ] (Love-number response) to a dissipative Im[χ];
a GW through the vacuum gets Δφ(ω) and v_g(ω) ≠ c. For a Planck-cutoff super-Ohmic vacuum we get
Im[χ] ∼ (ω/ω_P)^q, q ≥ 1 → predicted Δφ over 40 Mpc is ∼10⁻²³ rad (q=1), **~22–62 orders below**
LIGO sensitivity; GW170817 |c_gw−c|/c < 10⁻¹⁵ satisfied with 26–66 orders to spare (not binding).

> **Question:** Is the GW dissipative response of a Planck-cutoff super-Ohmic vacuum genuinely
> (ω/ω_P)^q suppressed (q ≥ 1, unobservable by ~22+ orders), or is there an enhancement — resonant
> bath mode, coherent build-up over D_L, or a lower effective cutoff — that lifts |χ| toward the
> [10⁻¹⁹, 10⁻¹⁵] detectable-but-not-speed-excluded window?

**Gates:** confirms GW dissipation is dead as a differentiator (we believe outcome (B)). A "no
enhancement" reply closes it.

---

### Q4 (bigger — flag if it's a known dead end before we spend on it)

**Setup.** Jacobson (1995) recovers the Einstein equations from Clausius δQ = T dS but **imports**
entropy ∝ area (sets G) and the Unruh temperature (sets ħ), and is time-symmetric. We want the
conservative sector of the in-in (Calzetta-Hu) effective action plus the diffeomorphism Ward
identity on the doubled-field action to yield the Einstein-Hilbert sector with the **area law
emerging** rather than imported — otherwise GRUT *borrows* GR (and is then a member of the
emergent-gravity family it claims to differ from), which we would mark as borrowed, not hosted.

> **Question:** Is there a known result that the Schwinger-Keldysh effective action of a
> diffeomorphism-invariant vacuum yields the Einstein-Hilbert sector via the Ward identity
> *without* separately assuming entropy ∝ area — or is this known to fail / reduce to the same
> thermodynamic input (Jacobson, Padmanabhan)? Is the Ward-identity route worth attempting, or a
> known dead end?

**Gates:** whether GR is **hosted** (emergent from the in-in machinery) or **borrowed** — i.e.
whether GRUT is a distinct ToE candidate or a relabeling of emergent gravity.

---

## Primary sources behind the above
Calzetta & Hu, *Nonequilibrium QFT* (Cambridge 2008) & PRD 37 2878 (1988) · Feynman-Vernon, Ann.
Phys. 24 118 (1963) · Kubo, Rep. Prog. Phys. 29 255 (1966) · Leggett et al., RMP 59 1 (1987) ·
Anastopoulos & Hu, CQG 30 165007 (2013) · Bassi et al., RMP 85 471 (2013) · Jacobson, PRL 75 1260
(1995) · Riegert, PLB 134 56 (1984) · Komargodski-Schwimmer, JHEP 12 (2011) 099.
