# What GRUT forbids and contains, and why — the no-go ledger

*A consolidation of the responsive-vacuum program's strongest, most defensible exports: the things it rules out, excludes, or cannot do. Each entry is stated at its **earned strength** (these are not interchangeable), names its **obstruction class**, points to its **register claim** in `provenance/claims.json`, and — the constructive half — states the **specification it imposes on any completion**. The ledger therefore doubles as the forward roadmap: it is the finite, named list of what a completion must supply or route around.*

*Scope: every entry below is a deflationary / no-go / containment result drawn from a **banked** claim in this rebuild's register (net **+13** GRUT). Of the **+13**, **+8 rides on four declared `laundering_ok` waivers** (`rung1_inin_action` +3, `rung5_gr_limit` +2, `rung6_qm_limit` +2, `p_tt_ansatz` +1), each carrying a written stance justification — `validate.py` prints the waived total on its own face. Foundational stances and gates (rung1, rung2) and the single-pole anchor (rung3) are not deflationary exports and are not itemized here. Every entry is a theorem **about GRUT-as-written**, not about nature. Strength labels are load-bearing and distinct — see the legend.*

---

## Strength legend (do not conflate)

| Label | Meaning |
|---|---|
| **FORBIDDEN** | Structural impossibility within GRUT's axioms (a genuine no-go). **This rebuild's register currently banks NONE.** The propagating-pole question appears only as the *settled-negative* α-bridge (entry 1); no claim is banked at structural-impossibility strength. |
| **SETTLED-NEGATIVE** | No known route + a strong structural obstruction, but *not* impossible in every extension — open to a named rescue. |
| **EMPIRICALLY EXCLUDED** | The alternative is killed by data, not (only) by structure. |
| **INVISIBLE-BY-SUPPRESSION** | Real but unobservable; the effect exists, the signature is below any threshold by orders of magnitude. |
| **BORROWED** | Not derivable from GRUT's machinery alone; imported, and marked as such. |

---

## The ledger

### 1. The α-from-anomaly bridge — **SETTLED-NEGATIVE** (not forbidden)
**What is ruled out (at this strength):** that the conformal-anomaly ratio $a/c=1/3$ *normalizes* the transverse-traceless response amplitude $c_0$ of the kernel $K^R=\alpha\,\chi\,P^{TT}$.
**Obstruction class (three, in order):** PRIMARY — projector orthogonality: the trace anomaly is spin-0, the TT response is spin-2, $g^{\mu\nu}P^{TT}=0$, and there is no metric-built scalar→TT intertwiner, so the trace-sector ratio $1/3$ has no shown carrier in the TT channel (the double-trace of the tracefree $P^{TT}$ is identically zero; $1/3$ is a hand-pinned structural label, not a computed contraction output). SECONDARY — independent Ward identities. TERTIARY (independent) — a UV-vs-IR no-RG-protection gap.
**A supporting mechanism (not a fourth obstruction — do not over-count the negative):** the GRUT-specific FDT/KMS cancellation. $N(\omega)/\mathrm{Im}\,K^R(\omega)=2\coth(\hbar\omega/2k_BT)$ is α-free because $c_0=\alpha$ is a common prefactor of $N$ and $\mathrm{Im}\,K^R$ and cancels — so FDT fixes shape/temperature but *leaves the overall scale $c_0$ free*. FDT does not itself obstruct; it simply fails to rescue.
**Register:** `rung9b_bridge` (tier `assumed`, sub_status settled-negative). The bridge is settled-negative **on the three obstructions above and nothing more**; the register banks no FORBIDDEN propagating-pole no-go and explicitly fences the propagating-pole question as a *separate* one that "does not cover this bridge."
**Crucial calibration:** this is **not** a formal no-go — impossibility in every extension is *not* claimed. The α *value* ($a/c=1/3$) is untouched (`rung9a_value`); only its *role as the kernel normalization* is settled-negative. So $c_0=\alpha$ is an **adopted phenomenological parameter**, and the α-dependent exports ($R=\sqrt{1+\alpha}$, $S=12\pi/\alpha^2$, $\Omega_\Lambda$) are conditional on it.
**Spec for a completion:** supply a **new operator identity** — a metric-built scalar→TT intertwiner, or a legitimate CFT route in which the $c$/$C_T$ Weyl-sector coefficient (which lives in the TT sector) normalizes the TT two-point — or accept $c_0$ as an external input. The kinematic 4th-order S⁴ Riegert/Paneitz a/c **carrier**-identification (which mode carries χ) is a *separate, open* front and is not prejudiced by this settled-negative bridge.

### 2. The μ=4/3 linear-cosmology modification — **EXCLUDED (structural + ~4σ-class joint empirical)** (→ the trace-only endpoint is dead; linear cosmology = ΛCDM under the *chosen* c₀=0, and within the computed lensing-bound window otherwise — x < ~0.59 central-inputs, loose-upper per F-MAP, μ−1 ≤ ~0.20; the owed TT-auto calc likely re-tightens)
**What is ruled out:** the growth-rate modification ($\mu\to 4/3$ super-horizon) that GRUT's own conformal coefficient would naively suggest.
**Obstruction class:** a separate-universe (adiabatic-dilatation) consistency no-go (EdS-quantified 2026-08-03: p(4/3)−p_SU = +0.186 ≠ 0; conditional on adiabaticity + the presupposed dilatation bridge, named) **plus** multi-leg empirical disfavoring — ISW-cross **computed ~2.0σ** (1.97 central, Σ-corrected; `calc/isw_exclusion.py` 2026-08-03; the old ~32σ **retired** — impossible in that channel, capped ~9–12σ for a signal-suppressing model, and the banked mechanism direction was backwards) + DESI Σ₀ ~3.5σ (independent; joint ~4σ-class). The low-ℓ TT auto channel is a **prospect** (estimate-grade, own calc owed), not a leg. *(Strength label note: 'EXCLUDED (structural + ~4σ-class joint empirical)' is a hybrid grade — structural no-go plus joint empirical, per this calibration line.)*
**Register:** `mu_linear` (tier `derived-pending`, sub_status `no_go_export`); rests on `p_tt_ansatz`.
**Calibration:** the surviving statement "linear cosmology = ΛCDM" is a *no-go export*, not a clean derivation — it is empirically **selected**, and it rests on the pure-TT projector ansatz (`p_tt_ansatz`, an adopted input), not on "TT annihilates scalars." It removes a would-be signature; it predicts no new one.
**Spec for a completion:** the trace-only μ=4/3 branch is dead; a completion either **derives the scalar-sector vanishing from the action** (without inserting $P^{TT}$ by hand — open, partly frontier-reserved) or accepts the pure-TT ansatz as a stated input. *(Marked 2026-08-03: the derive-from-the-action route is CLOSED at the symmetry level — the p_tt interrogation returned CHOSEN; only the rung3 trace-correlator route remains, and it costs a new +1 — relocation, not discharge. Rung3 resolving against it fires `mu_linear`'s armed tier trigger: `derived-pending` → `assumed`.)*

### 3. An economical evolving dark energy w(z) matching DESI — **NOT EARNED** (needs ≥2 modes; the $w_a$ sign is frontier, not "wrong")
**What is ruled out:** a *single-parameter* (sub-CPL) evolving $w(z)$ matching the DESI quintom hint.
**Obstruction class:** a single passive relaxor (one pole) cannot produce DESI's phantom-divide **crossing** — a $w=-1$ crossing needs ≥2 modes / oscillatory poles / an active response (Vikman 2005; the single-channel deviation is one-signed, staying on one side of $-1$). The trace-anomaly conformalon cannot supply the second mode (no Starobinsky–Yokoyama dynamical mass for the $\Delta_4$ compensator; its stress is $w=+1/3$, the wrong equation of state; magnitude ~8× below DESI at $N=60$) — *that* sub-result is settled-negative (`calc/RESULTS_conformalon.md`). **RETRACTION (2026-06-29, `rung7_w2` sign screen):** the earlier "$w_a>0$, the **wrong sign**" reading is **withdrawn** — the $w_a$ **sign is frontier-indeterminate**. The second law fixes the dissipative branch on the phantom **side** ($w\le-1$, which is what forbids the crossing), but **not** the $w_a$ **slope** sign ($\sigma=\Pi^2/(\zeta T)$ is quadratic in $\Pi$, blind to $\dot\Pi$; the toy's $w_a\le0$ is a $\zeta$=const/Eckart artifact, and other passive $\zeta(a)$ scalings give $w_a>0$). So GRUT is **not** "wrong-sign"; the sourced prediction is $w=-1$ **flat**, and any $w_a\ne0$ (either sign) needs the `mu_linear`-excluded trace sector.
**Register:** `rung7_wz`, `rung7_w2_wa_sign`, `rung7_w3_nocrossing_export` (all tier `to-derive`); `calc/wz_sign.py`, `calc/RESULTS_wz_sign.md`, `calc/RESULTS_conformalon.md`.
**Calibration:** the *structural* claim (a finite-memory vacuum evolves $w$) survives but is weak (any dynamical dark energy evolves); the *economical* (fewer-than-CPL) version is **not earned**; the no-crossing is generic-flavored (Vikman) and conditional on the open `rung3` (a no-go cannot outrank its anchor) — held `to-derive`.
**Spec for a completion:** supply a genuine **second, cosmologically-slow relaxation mode** ($\tau_2\sim 1/H_0$) with sign-changing/active structure — and pay the extra parameter (≈CPL parity), which is exactly what the economy claim was trying to avoid.

### 4. The tabletop gravitational-decoherence falsifier — **INVISIBLE-BY-SUPPRESSION** (quiet-or-faint)
**What is ruled out:** a *parameter-free, observable* energy-basis decoherence wedge.
**Obstruction class:** the dominant diagonal coupling ($T^{00}\sim$ energy density) commutes with $H_S$, so it samples the zero-frequency noise $S(0)=0$ → **quiet**; the wedge-carrying off-diagonal coupling ($T^{0i},T^{ij}\sim v/c$) survives but lands 7–47 orders below detectability. The robust Pikovski time-dilation effect is *position*-basis — the same axis as the collapse models, not the wedge.
**Register:** `rung8_falsifier` (tier `to-derive`); `calc/q1_energy_basis_magnitude.py`, `calc/energy_basis_decoherence.py`.
**Calibration:** the energy-vs-position *wedge* is a real qualitative distinction from Diósi–Penrose/CSL; it just is not a *working observable* — observability would require staking the noise amplitude ~$10^7$× above its natural value, a tuned number at the current matter-wave bound.
**Spec for a completion:** find a leading off-diagonal energy coupling that samples $S(\Delta E)$ at $O(1)$, or a bath resonance/lower-cutoff that lifts the magnitude — otherwise the falsifier does not carry the program.

### 5. Gravitational-wave dissipation as a differentiator — **INVISIBLE-BY-SUPPRESSION**
**What is ruled out:** an observable GW signature (frequency-dependent dephasing, $v_g(\omega)\neq c$) from the dissipative $\mathrm{Im}\,\chi$.
**Obstruction class:** structural Planck-suppression. The dissipative dephasing is real but **~$10^{22}$ (q=1) to ~$10^{62}$ (q=2) orders below the ~0.1 rad detectability threshold**; the GW170817 speed bound is satisfied with 26–66 orders to spare (not even binding), and GRUT sits 21–62 orders below the live $|\chi|$ window $[8\times10^{-20},\,2\times10^{-15}]$.
**Register:** `rung4_love_kk` (tier `shown`); `calc/gw_dissipation_bounds.py`.
**Calibration:** the effect is **real** (absent in lossless GR) but invisible. The smallness is the *same* Planck suppression that makes the theory solar-system-safe — a feature, not a tuning.
**Spec for a completion:** observability would need $\omega_c\sim$ MeV–meV (grossly excluded) or a bath resonance / collective IR mode lifting $|\chi|$ into the live window.

### 6. Deriving General Relativity from the in-in machinery — **BORROWED**
**What is ruled out:** that the Schwinger–Keldysh formalism alone *selects* the Einstein–Hilbert action.
**Obstruction class:** the diffeomorphism Ward identity enforces only $\nabla_\mu T^{\mu\nu}=0$ (a symmetry constraint) and does **not** determine the action — Einstein–Hilbert, $R^2$, $f(R)$, Lovelock, and nonlocal curvature actions all satisfy it. Action-selection requires extra microscopic input ("everyone pays somewhere": Jacobson imports area entropy + Unruh $T$; Sakharov imports UV matter; anomaly-induced gravity imports conformal structure).
**Register:** `rung5_gr_limit` (tier `assumed`, +2: area entropy sets $G$, Unruh $T$ sets $\hbar$).
**Calibration:** GR is **borrowed**, marked as such — GRUT's gravitational sector is, on current footing, a member of the emergent-gravity family (Jacobson/Padmanabhan), not a from-scratch derivation.
**Spec for a completion:** supply the microscopic input that fixes $G$ and the derivative expansion from the conservative part of $\chi$ without importing the area law — an open, hard research program.

### 7. Deriving the Born rule from decoherence — **BORROWED**
**What is ruled out:** that integrating out the bath *derives* the Born probability measure $|\psi|^2$.
**Obstruction class:** the influence-functional reduction reproduces the Schrödinger core plus environment-induced decoherence that selects a *pointer basis* — but a preferred basis is **not** outcome selection (the improper-mixture objection). The decoherence *rate* is a genuine, differentiating output; the probability measure is an inherited postulate.
**Register:** `rung6_qm_limit` (tier `assumed`, +2: the quantization/single-valuedness condition, and the Born probability-measure postulate).
**Calibration:** GRUT recovers quantum mechanics as a limit, not a derivation: the rate is earned, the Born rule is borrowed. The measurement problem is inherited, not solved.
**Spec for a completion:** supply the outcome-probability measure — decoherence + a pointer basis is *necessary but not sufficient*; the $|\psi|^2$ weighting must come from elsewhere.

---

## How to read this ledger

The deflationary entries are not failures; they are GRUT doing the one thing a disciplined theory can do that an enthusiastic one cannot — **telling you exactly what it cannot do, and therefore exactly what is left to build.** Each "spec for a completion" is a precise, finite obligation. Together they convert "build it toward everything" from an aspiration into a bounded program.

And the strengths are not interchangeable. Note in particular what is **absent**: this rebuild banks **no genuine FORBIDDEN (structural-impossibility) no-go.** Its strongest exports are *settled-negative* with a named rescue (entries 1, 3), *empirically excluded* (entry 2), *invisible-by-suppression* (entries 4, 5), and *borrowed* (entries 6, 7). Reporting that absence honestly — rather than promoting a settled-negative obstruction or a prior-lineage argument to "FORBIDDEN" — is itself part of the discipline; over-grading a no-go is the exact failure mode this program exists to prevent.

## Scope — strictly the clean register

Every entry above is drawn from a banked claim in `provenance/claims.json` and its backing computation. **Nothing in this ledger is carried from a prior GRUT lineage** (v2/v3/v4); results from earlier versions have no standing here until they are re-derived inside this rebuild's discipline and banked. That exclusion is the point of the clean rebuild — the artifacts cite only what this register establishes.
