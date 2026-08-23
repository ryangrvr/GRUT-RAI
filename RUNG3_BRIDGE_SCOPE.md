# The rung-3 bridge audit — which kernel does GRUT actually claim, and what maps it to the licensed worldline object?

> **STATUS: NOTHING BANKED. NOT A CLAIM. NOT A RESULT.**
> The register (`provenance/claims.json`) is untouched by this file. Scoping/orientation
> document written **default-BROKEN** per CHARTER §1.4; may not be cited as content by any
> other artifact; requires adversarial pre-screen (CHARTER §1.3) and overseer relay
> (CHARTER §5.3) before any part enters the register. Commissioned by the owner 2026-08-21 as
> the single authorized next calculation after the keystone-map screen
> (`provenance/SCREEN_RECORD_2026-08-21_keystone_map.md`): determine whether the actual
> gravitational response kernel required by GRUT connects, by a derived projection or limit,
> to the legitimately stationary worldline response established there (D3a).
>
> No ledger net figure is typed anywhere in this document.

## 0. The six authorized questions

1. What exact GRUT memory kernel is being claimed?
2. What exact correlator/response generates it?
3. Is that object a worldline correlator, a spatially projected correlator, or the full
   spacetime self-energy?
4. What mathematical operation maps the actual object onto the worldline spectral object,
   if any?
5. Is that mapping derived, an approximation, or an additional input?
6. Only then: what does the resulting spectrum say about pole / cut / continuum behavior?

Answered in order; §6 is fenced to say almost nothing, because that is what the evidence
supports.

---

## 1. Questions 1–2: the claimed kernel, and what generates it

**The register's own words (quoted from `provenance/claims.json`, not paraphrased):**

- **`rung1_inin_action` (shown):** "The gravitational vacuum is a responsive medium with finite
  memory, described by a single Schwinger-Keldysh influence action S_IF with retarded
  dissipation kernel **K_R** and noise kernel **N** (doubled x_r/x_a fields)."
- **`rung2_kms_gate` (shown):** "In equilibrium the noise kernel N is locked to Im[chi] by FDT
  with a coth(hbar\*omega/2kT) factor; admissible kernels must satisfy KMS detailed balance."
- **`rung3_single_pole` (derived-pending):** "Committing to relativistic massless fast modes
  (omega=c|k|) gives DOS~omega^2, **J(omega)~omega^3** (s=3 super-Ohmic); WITHIN the
  collisional/analytic-bath regime … the Mori-Zwanzig kernel collapses to single-pole /
  Markovian-like."
- Harness structural layer (`provenance/harness.py:199`): the legal interior family is
  **K = c2·P^TT + c0·P^(0s)** — the booked FDT-locked scalar-dial family of the 2026-08-17
  discharge addendum.

So the claimed object is a **spacetime pair (K_R, N)** defined by an influence action on the
doubled closed-time-path contour, with the bath entering through a spectral density J(ω)
justified by a density-of-states argument. What generates it: the integrated-out graviton
sector of the same theory — i.e., ultimately the pure-graviton de Sitter self-energy, the
assembled G_R^TT of the dispatch. **No calc in this repository constructs K_R or N from Σ(x;x′);
J(ω) is staked directly** (η ω³ e^{−(ω/ωc)²} appears as an axiom of the toy layer:
`arrow_origin.py`, `energy_basis_decoherence.py`, `finite_T_*`).

---

## 2. Question 3: classification of every export against the three object-classes

Classes per the owner's structure: **(A) worldline correlator** — stationary in cosmic proper
time, licensed by D3a; **(B) spatially projected / homogeneous susceptibility** χ(ω);
**(C) full spacetime self-energy** Σ(x;x′), no global reduction (D3b).

| export (register node → calc) | object actually used | class | licensing status after the screen |
|---|---|---|---|
| `rung8_falsifier` → `energy_basis_decoherence.py`, `q1_energy_basis_magnitude.py` | noise kernel N driving the Anastopoulos–Hu **detector master equation**: decoherence functional along matter-wave branches | **A** | licensed scope (worldline); verdict quiet-or-faint is a within-A result |
| `rung4_love_kk` → `gw_dissipation_bounds.py` | frequency-domain susceptibility **χ(ω)** acting on plane GWs: dephasing Re χ, dissipative Im χ. The register's own statement says it "recovers **worldline-EFT tidal-response** structure" — borrowed vocabulary, not performed reduction | **B′** (homogeneous-medium susceptibility; stationary-by-construction) | stationarity imported with the susceptibility ansatz; D3a licenses worldline thermal kernels, NOT extended-wave susceptibilities — scope unnamed in-file |
| `rung7_wz` → `wz_dark_energy.py`, `two_scale_desitter.py` | relaxing **χ(ω)** with τ₂ ~ 1/H₀ applied to the homogeneous expansion H(z); SY Langevin along the homogeneous background | **B′** (zero-mode/homogeneous limit) | same import: χ(ω) presumes a stationary reduced kernel that D3b does not provide globally; the homogeneous limit is plausibly worldline-like (one comoving observer's background) but **that reduction is nowhere exhibited** |
| `mu_linear`, ISW/σ₀ exports | quasi-static sub-horizon limit: ω → 0 projector bookkeeping on the FRW frame | **B** (static limit; no spectral content needed) | internally fine (single clock, C5 of the keystone map); inherits only p_tt_ansatz, not any spectral claim |
| `rung3_single_pole` anchor / spine test / dispatch target | assembled **G_R^TT(ω→0) = 2 Im G_R^TT**, i.e. Σ(x;x′) after assembly + resummation + continuation | **C** | never computed; never reduced; THE keystone |

**Finding (the audit's center): GRUT's exports draw on three different reductions of one
nominal object, and neither the register nor any calc states which reduction each export uses,
nor provides the map between them.** The register's kernel language slides between classes
without marking the slide — the same unmarked-slide shape as the clock defect the previous
screen caught, one level deeper.

## 3. Questions 4–5: the mapping operation, and its status

- **C → A (worldline limit of the influence functional).** Such an operation EXISTS in the
  literature the program already borrows from: Feynman–Vernon influence actions restricted to a
  trajectory; worldline EFT tidal response — which `rung4` explicitly invokes by name. But
  **no calc in this repository restricts the graviton Σ to a worldline**; rung4 borrows the
  *structure* (χ(ω) elastic/dissipative split) without performing the reduction.
  **Hazard, named:** point-particle limits typically keep local terms and can drop exactly the
  IR/nonlocal structure rung3 lives on — in dS, where the candidate memory scales ARE IR
  (τ₂ ~ 1/H₀, ladder spacing H), whether the worldline limit retains any of it is open and
  unexamined. A derived C→A map could therefore be *empty of rung3 content* — that possibility
  is itself information.
- **A → C (smearing the worldline kernel back over spacetime with mode functions).** No
  operation exists here at all: the worldline object carries no k-dependence, and the keystone
  question (pole vs cut in ρ_TT(ω→0)) is a question about momentum-resolved assembly
  (source vertex + observer vertex + external legs). A→C is not an approximation of anything
  computed; it would have to be an ADDITIONAL POSTULATE.
- **Answer to Q5, stated plainly: today the identification is an ADDITIONAL INPUT wherever it
  is used.** It is assumed every time rung3 language ("memory time", "single pole", "collision
  rate") is applied to tabletop or cosmological exports, and assumed again — silently — when
  those are read as evidence about the C-class anchor. Derived: nothing. Approximation:
  nowhere exhibited.

### Corollary found during this audit (new, small, load-bearing)

`rung3`'s J(ω) ∼ ω³ justification is a **density-of-states argument importing flat-space
intuition** (ω = c|k| ⇒ DOS ∝ ω²). In de Sitter the free TT spectrum is NOT flat-space-like:
the static-patch family is discrete below O(H) with the zero structure of E5, and the true
low-frequency dS TT spectral density is precisely the open keystone. So the s = 3 super-Ohmic
premise — the premise the entire single-pole derivation rests on — has an **uncomputed
de-Sitter analogue**, and computing it is a corollary of the keystone, not independent
support for it. This weakens "derived-pending" one further notch of conditionality: the
pending input is not only the bath regime, it is the DOS step itself.

---

## 4. Question 6: what the spectrum can say — fenced to almost nothing

Until the classification lands, **no pole/cut/continuum statement transfers between classes**:

- The A-class worldline kernel's spectral structure is analyzable in cosmic time (D3a) and its
  ladder is the state's at T_dS = H/2π (E6) — but no in-house calc has even computed the A-class
  kernel OF THE GRAVITON COUPLING; the toy J(ω) is staked, not derived.
- The B′-class susceptibilities inherit whatever spectral shape they are handed
  (R(x) = x²/(1+x²) is declared illustrative in-file).
- The C-class anchor — the only object rung3 is actually about — is uncomputed (walls A–C of
  the keystone map stand).

The owner's four outcome classes are recorded here **as framing for a future pre-registration,
not as one** (outcome-first instruments are owner-signed per CHARTER §1.6):

1. Derived reduction exists AND carries the required memory behavior → GRUT has a real opening;
   proceed to relaxation scale and cosmological test.
2. Derived reduction exists but yields a DIFFERENT memory structure → the memory ansatz changes;
   constructive, priced at entry.
3. No reduction exists → the worldline result cannot justify the cosmological memory kernel;
   a serious negative result, bankable as such.
4. The full assembled Σ itself supplies the structure → the worldline calculation demotes to
   diagnostic; plausibly the cleanest outcome.

## 5. What the bridge calculation concretely consists of

In-house (this repository's reach):
1. **Exhibit the C→A reduction formally** for the influence functional: restrict S_IF's sources
   to a worldline x(τ), expand in the TT field along it, obtain the induced worldline K_R, N —
   symbolically, at Gaussian order, on the booked family (K = c2·P^TT + c0·P^(0s)).
2. **Track what survives**: which terms of the dS IR structure (ladder, secular logs, tail)
   pass through the point-particle limit — the named hazard of §3.
3. **Classify each export's kernel sentence in the register** (draft edits only, via the
   handover route): every node that says "memory time" or "collision rate" must name its class.

Outside in-house reach by standing rule:
4. Whether the assembled Σ reduces at all — part of wall (A)'s assembly; dispatch territory,
   re-posed with clock named per the keystone map's C7 upgrade.

## 6. Guards

1. Nothing here banks; draft register language goes through `handover/` and the bank gate.
2. The E6 fence is load-bearing: free ladder ⇒ neither memory pole nor its impossibility.
3. D3a licenses ONLY along-worldline statements; any use of it beyond that scope is laundering.
4. Q6 remains unanswered by this document — deliberately. Saying less is the result.
5. The corollary in §3 (DOS step uncomputed in dS) is a candidate defect against
   `rung3_single_pole`'s justification chain: file it as a draft edit for the owner, not as a
   silent repair.

## Firewall note

Suite before this audit: 234 passed / 5 failed / 1 skipped (declared reds, byte-identical);
`validate.py` PASS; register untouched. Re-verified after this document was written.


