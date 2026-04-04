# Appendix M — Localized Bosonic Object Support

**Status:** Deterministic audit complete
**Module:** `grut/localized_bosonic_object_audit.py`
**Tests:** `tests/test_localized_bosonic_object_audit.py`
**Depends on:** pre-matter quarantine perimeter (Appendix L / `docs/PRE_MATTER_QUARANTINE_STATUS.md`), `grut/phi_sector_bifurcation.py`, `grut/tau_eff_domain_declaration.py`, `grut/beta_q_sensitivity.py`, `grut/fermionic_emergence_audit.py`

---

## 1. Exact Question Being Audited

> Given the currently audited GRUT architecture **exactly as it exists now**, what kinds of localized bosonic objects are natively supported, if any, without adding new field content, new topological terms, spinors, fermionic structures, or unbuilt matter-sector dynamics?

This is a **disqualification-first** audit. The default posture is to assign the strictest verdict compatible with the evidence. Positive localization claims require demonstrated stability, finite energy, and bounded objecthood — not analogies, not equilibrium coincidences, not topological charge alone.

---

## 2. Current Field Content Considered

The audit uses only the currently declared architecture state (as of the pre-matter quarantine perimeter):

| Object | Symbol | Type | Domain | Regime |
|---|---|---|---|---|
| Canonical scalar — trajectory | `M_drive(t)` | Shell quantity | 0+1D point at `R(t)` | Collapse sector |
| Canonical scalar — field | `Φ(r,t)` | Distributed field | 1+1D, `r ∈ [R_eq, R_ext]` | Constitutive sector |
| O(3) triplet | `Φᵃ`, `a=1,2,3` | Topological object | 3+1D, vacuum manifold `S²` | Candidate ext. (Phase D1+) |
| Lapse proxy | `Ψ_proxy = α_vac = 1/3` | Effective observable | Scalar at equilibrium | Kinematic |
| Relaxation time | `τ_eff = 1/ω₀` | Effective observable | Context-dependent | Three ω definitions |
| Equilibrium radius | `R_eq = 1/3` | Effective observable | Scalar | Canonical |
| Interior frequency | `ω₀ = √27 ≈ 5.196` | Effective observable | Scalar | Interior PDE |
| O(3) hedgehog `n=1` | `Φᵃ = η·xᵃ/|x|` | Candidate localized | 3D radially symmetric | O(3) sector |

**Absent from current architecture** (not to be imported):
- Spinors, Dirac structure (closed by fermionic emergence audit)
- Hopf term / π₃(S²) action term (absent from O(3) sector)
- Gauge fields (D14/D15 closed all coupling routes)
- **Skyrme term** — the quartic stabilizing term `L₄ = (F²/16e²)[∂_μΦᵃ × ∂_νΦᵃ]²` required to stabilize O(3) solitons in D=3. **This is the critical absent ingredient.**
- Covariant 4-vector matter dynamics (τ_eff domain declaration: roadmap unbuilt)

---

## 3. Declared Domain Limitations

From `grut/tau_eff_domain_declaration.py`:

> **All τ_eff results in the current GRUT architecture are produced within: "spherically symmetric, quasi-static, low-frequency, preferred-frame regime."**

Specific constraints:
- **Spherical symmetry:** no angular modes, no frame-dragging
- **Quasi-static:** τ₀ ≪ dynamical timescale, or ω·τ₀ ∼ 1 at transition
- **Preferred frame:** ω evaluated in local rest frame of shell or fluid
- **No 4-covariant ω:** the three ω definitions (H, |V|/R, ω₀) are not related by a tensor law

**Consequence:** Any localization claim is valid only inside this regime. Claims requiring covariant general-relativistic dynamics are **rejected** in this audit. The constitutive field Φ(r,t) and its profile are analyzed within the quasi-static spherically-symmetric domain only.

---

## 4. Localization Criteria Used

A configuration qualifies as a **localized bosonic object** only if it satisfies all of:

1. **Spatial boundedness:** the field has compact support or falls off sufficiently fast that the energy is finite without externally imposed cutoffs.
2. **Dynamical origin:** the localization arises from field dynamics (not from an externally imposed boundary condition such as the shell at `R_eq`).
3. **Bounded energy:** the total field energy is finite and well-defined within the declared domain.
4. **Objecthood:** the configuration can be identified as a distinct physical entity with conserved charges, not merely a distributed background profile.

**Rejected as localization criteria:**
- Nontrivial spatial profile (profile ≠ object)
- Shell boundary condition (external imposition ≠ intrinsic localization)
- Equilibrium coincidence of field values at one radius
- Topological charge alone (charge ≠ stable particle)

---

## 5. Stability Criteria Used

A configuration is **stable** only if it has a genuine energetic minimum under deformations compatible with the declared domain. The four candidate mechanisms are:

| Mechanism | Present in GRUT | Sufficient for stable localized object? |
|---|---|---|
| Shell boundary condition (at `R_eq`) | ✓ Yes | ✗ No — external imposition |
| Constitutive relaxation attractor (ODE → `M/r²`) | ✓ Yes | ✗ No — stabilizes distributed profile, not lump |
| O(3) topological charge conservation | ✓ Yes | ✗ No — charge conserved but configuration collapses |
| Skyrme term `L₄` | ✗ **Absent** | ✓ Would be sufficient — but unbuilt |

**Conclusion:** No currently-present mechanism provides energetic stability for a localized bosonic object.

---

## 6. Finite-Energy Criteria Used

A configuration has **intrinsic finite energy** if the total field energy integral converges without externally imposed IR or UV cutoffs.

**Constitutive scalar Φ(r,t):**
- Equilibrium energy density: `ρ_eq(r) = −M²/(2τ²r⁴)` — negative, diverges as `r → 0`
- Numerical value at `r = R_eq`: `ρ_eq(R_eq) = −6.75` (geometric units)
- Converges only with an IR cutoff at `R_eq` (the shell) and UV regularity
- **Classification:** cutoff-dependent, not intrinsic

**O(3) hedgehog `n=1`:**
- Subject to **Derrick's theorem** (see §7 below)
- Kinetic energy scales as `λ` under `r → λr` in D=3 → no stationary point
- Configuration collapses to zero size without a Skyrme stabilizing term
- **Classification:** no finite-energy stable soliton in D=3 without Skyrme term

**Verdict:** `finite_energy_lump_found = False`

---

## 7. Topological Criteria Used

The topological structure is assessed exactly as it appears in the native architecture, drawing from `grut/fermionic_emergence_audit.py`:

| Homotopy group | Value | Meaning | Present? |
|---|---|---|---|
| `π₂(ℝ)` | 0 | Canonical scalar: no topological defects | Moot (trivial) |
| `π₂(S²)` | ℤ | O(3) hedgehog: integer winding number `n ∈ ℤ` | ✓ Yes |
| `π₃(S²)` | ℤ | Hopf invariant (fermionic statistics if θ=π) | Present abstractly, Hopf **term absent** |

**Bosonic topological charge:** Present via O(3) sector. The `n=1` hedgehog carries integer winding number → bosonic statistics (no Hopf term, so Berry phase = +1).

**Derrick's theorem — the critical no-go:**

> In D=3 spatial dimensions, under `r → λr`:
> - Kinetic energy: `E₂(λ) = λ^{D-2} E₂ = λ E₂` (linear growth in D=3)
> - Skyrme energy: `E₄(λ) = λ^{D-4} E₄ = λ^{-1} E₄` (absent from GRUT)
> - Stationarity condition: `dE/dλ = E₂ − E₄/λ² = 0` → requires `E₄ = λ² E₂` (impossible without E₄ term)
>
> Without the Skyrme term, `dE/dλ = E₂ > 0` everywhere: no stationary point. The configuration collapses to zero size. The topological charge `Q = n` is conserved during collapse (it approaches a distributional limit `n·δ³(r)`), but no stable finite-size object exists.

**Reference:** Derrick (1964), *J. Math. Phys.* **5**, 1252; Skyrme (1961), *Proc. R. Soc. A* **260**, 127.

---

## 8. Exact Verdict

### Primary verdict (from closed label set):

```
particle_candidate_not_yet_established
```

**Rationale:** The O(3) sector provides bosonic topological charge (`π₂(S²) = ℤ`, winding number `n ∈ ℤ`). This constitutes candidate-level evidence for bosonic structure. However, particle status requires stability and finite-energy objecthood, neither of which is established:

- The O(3) `n=1` hedgehog is **Derrick-unstable** in D=3 without a Skyrme term.
- The Skyrme term is **absent** from the current O(3) sector.
- Topological charge is conserved but does not prevent the configuration from collapsing.
- Therefore: bosonic topological charge is present; stable bosonic particle is not.

The strictest compatible verdict in the closed label set is `particle_candidate_not_yet_established`. This is preferred over `bosonic_topological_defect_supported` (which would require demonstrated stability) and over `no_native_localized_bosonic_object_support` (which would deny the topological charge evidence).

### Secondary verdicts:

| Label | Source |
|---|---|
| `shell_localization_only` | Constitutive Φ-field is localized at `R_eq` only because the shell imposes an IR cutoff — external boundary, not intrinsic objecthood |
| `distributed_profile_without_objecthood` | Equilibrium profile `Φ_eq(r) = M/r²` exists throughout space — monotone power-law, no compact support, no energetic minimum |

---

## 9. Exact Nonclaims

The following are **explicitly not claimed** by this audit:

1. **NOT** claiming shell equilibrium establishes localized bosonic matter. `shell_supported_localization = True` is a secondary classification flag, not an objecthood claim.

2. **NOT** claiming the O(3) hedgehog is a stable particle. The winding number `n=1` is conserved, but the configuration is Derrick-unstable without a Skyrme term.

3. **NOT** claiming bosonic topological charge implies particle status. `topological_bosonic_charge_present = True` is a necessary but not sufficient condition. Stability is also required and is absent.

4. **NOT** ruling out stable localized bosonic objects forever. The architecture could be extended with a Skyrme term (or equivalent higher-derivative stabilizing term), but that term is currently absent and unbuilt. Its addition is a coherent extension path.

5. **NOT** claiming the constitutive field profile `Φ(r) = M/r²` is a matter object. It is a distributed profile without compact support, classified as `distributed_profile_without_objecthood`.

6. **NOT** claiming this audit closes the matter-sector question. It establishes the current bound: `particle_candidate_not_yet_established`. Later audits with additional field content may revise upward.

7. **NOT** claiming the O(3) extension is canonical GRUT. It is a candidate extension (Phase D1+), acknowledged from the fermionic emergence audit architecture state.

8. **NOT** claiming Derrick's theorem permanently rules out all bosonic particles from GRUT. It rules out pure-kinetic O(3) sigma model solitons in D=3. A Skyrme term is a coherent extension path that would lift this obstruction.

---

## 10. What Current GRUT Can Legitimately Say About Localized Bosonic Objects

Current GRUT **can** legitimately say:

- The constitutive sector produces a spatially distributed equilibrium profile `Φ_eq(r) = M/r²` within the declared quasi-static spherically-symmetric domain.
- The shell at `R_eq` provides a boundary-condition-imposed localized structure (shell-confined, not intrinsically localized).
- The O(3) extension (Phase D1+) carries bosonic topological charge via `π₂(S²) = ℤ`, with integer winding number `n ∈ ℤ` and bosonic statistics (no Hopf term, Berry phase +1).
- The `n=1` hedgehog configuration is topologically classified and represents a candidate for a localized bosonic entity.
- The topological charge `Q = n·η` is conserved under smooth deformations within the O(3) sector.
- The O(3) sector does not support stable finite-size solitons in its current form due to Derrick's theorem (no Skyrme term).
- The architecture is at candidate level: bosonic topological charge present, particle status not established.

---

## 11. What Current GRUT Cannot Yet Say

Current GRUT **cannot yet** say:

- That the O(3) `n=1` hedgehog is a **stable** bosonic particle. (Derrick's theorem; no Skyrme term; no energetic minimum.)
- That the constitutive field profile `Φ(r) = M/r²` constitutes a **localized bosonic object**. (Power-law, no compact support, requires external cutoffs.)
- That the shell equilibrium at `R_eq` is a **localized bosonic matter** configuration. (External boundary condition, not dynamical localization.)
- That topological charge alone is sufficient for particle status. (Stability required and absent.)
- That the energy of any configuration is **intrinsically finite** without the shell cutoff. (Energy diverges as `r → 0`; requires IR cutoff.)
- That the O(3) sector supports **skyrmion-like bosonic particles** in GRUT. (Skyrme term absent; Derrick obstruction active.)
- That the matter sector is solved or partially solved. (Pre-matter quarantine perimeter remains; matter dynamics unbuilt.)

---

## 12. Matter Support, Object Support, or Profile-Level Structure?

| Level | Verdict |
|---|---|
| **Matter support** | ✗ **Not established.** Matter sector dynamics are explicitly unbuilt. Constitutive profile and shell equilibrium are not matter objects. |
| **Object support** | ✗ **Not established.** No stable finite-energy localized bosonic object exists in the current architecture. Derrick's theorem eliminates the only candidate (O(3) hedgehog) without a Skyrme term. |
| **Profile-level structure** | ✓ **Present.** Constitutive profile `Φ_eq(r) = M/r²` exists, with shell-imposed boundary. This is genuine field structure but is classified as `distributed_profile_without_objecthood`. |
| **Topological charge level** | ✓ **Present.** O(3) sector provides bosonic topological charge. This is genuine bosonic topological content at the candidate level. |

**Summary:** Current GRUT has **profile-level structure** and **topological charge** at the bosonic level. It does not yet have **object-level** or **matter-level** support. The gap is precisely identified: the Skyrme term (or equivalent stabilizing mechanism) is the missing ingredient between `particle_candidate_not_yet_established` and `bosonic_topological_defect_supported`.

---

## Claim Firewall

The following inferences are **explicitly forbidden** by this audit:

| Forbidden inference | Status |
|---|---|
| "Nontrivial profile implies particle" | ✗ Forbidden — profile ≠ object |
| "Shell equilibrium implies localized bosonic matter" | ✗ Forbidden — boundary condition ≠ matter |
| "Topological charge implies stable bosonic particle" | ✗ Forbidden — charge ≠ stability |
| "Constitutive field profile implies matter sector solved" | ✗ Forbidden — profile ≠ matter sector |
| "O(3) hedgehog is a stable particle" | ✗ Forbidden — Derrick unstable |
| "Φ_eq profile is a bosonic particle" | ✗ Forbidden — distributed profile |
| "Shell localization implies matter objecthood" | ✗ Forbidden — BC-imposed |
| "Derrick obstruction can be ignored" | ✗ Forbidden — rigorous no-go in D=3 |
| "Bosonic charge is sufficient for particle status" | ✗ Forbidden — stability also required |
| "Profile objecthood without finite-energy lump" | ✗ Forbidden — lump not found |

All ten forbidden claim checks pass in `tests/test_localized_bosonic_object_audit.py`: `forbidden_claims_triggered = []`.

---

*Generated deterministically by `grut/localized_bosonic_object_audit.py`. The verdict, nonclaims, and forbidden-claim results are computed from Booleans, not asserted post-hoc.*
