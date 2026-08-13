#!/usr/bin/env python3
"""operator_basis: the open-EFT operator basis for the quadratic influence action -- the instrument
that adjudicates whether P^TT is FORCED or CHOSEN (register node eft_operator_basis).

THE QUESTION (default-BROKEN, per the wave brief): enumerate the admissible tensor structures for the
quadratic S_IF (the order where K_R lives) for a symmetric rank-2 perturbation on the declared
background, under the REGISTER-DECLARED symmetries ONLY -- p_tt_ansatz is NOT an input, it is the
object under test. Is P^TT the unique admissible structure, or one of several?

PART-1 SYMMETRY INVENTORY (read from the register, not invented -- each tied to its declaring claim):
  S1 rung1 (+3 declared): background Lorentzian causal structure -> retarded/causal kernel K_R(omega,k).
  S2 rung1 (+3 declared): Gaussian/linear-response truncation -> the action is QUADRATIC in h.
  S3 rung1 (+3 declared): the system/bath split -> the influence-functional (reduced) setting itself.
  S4 rung2: KMS/FDT + passivity -- N locked to Im chi; omega*Im chi positive-semidefinite (matrix sense).
  S5 rung5 (assumed): diffeomorphism invariance, WITH its banked Ward limitation (the diffeo Ward
     identity does NOT select the action -- EH/R^2/f(R)/Lovelock all permitted).
  S6 mu_linear's frame: background spatial homogeneity + isotropy (FRW linear cosmology) -- SO(3)
     rotations + translations at fixed k; parity-even inherited from the unperturbed background
     (no parity-violating input is declared anywhere in the register -- NOTED as inherited, not chosen).
  S7 pair symmetry K_{ij,ab} = K_{ab,ij} (Onsager reciprocity). For the NOISE kernel this is
     automatic; for the RETARDED kernel it is a substantive microscopic time-reversal assumption NOT
     implied by S1-S6 -- same 'inherited, not chosen' status as parity (no time-reversal-breaking
     input is declared anywhere in the register). ROBUSTNESS (firewall-verified): either of
     {parity-even, pair-symmetric} ALONE excludes the TT-birefringence structure; the 2-survivor
     result below is unchanged if either (but not both) is dropped.
  NOT inputs: P^TT (p_tt_ansatz -- under test); alpha's placement (rung9a/9b -- tested in Part E).

FRAME AND EXHAUSTIVENESS (the KC5 fence, stated up front): the enumeration works in the spatial
SVT frame at fixed background slicing and fixed spatial momentum k -- the SAME frame in which
p_tt_ansatz and mu_linear state P^TT. Within this frame it is exhaustive to ALL derivative orders
in the sense that every SO(3)-invariant, parity-even, pair-symmetric kernel decomposes on the
enumerated structures with arbitrary coefficient functions of (omega, k^2) -- because k-hat is the
only available direction. What is NOT covered: parity-odd structures (excluded by the parity-even
background; would add Levi-Civita/birefringence operators); pair-ANTISYMMETRIC parity-even
structures (exactly ONE exists at this frame -- the antisymmetric trace-longitudinal mixer -- and
it is excluded by the same Ward test, so relaxing S7 alone does not change the survivor set); and
the full 4d-COVARIANT completion (h_0mu components, time-dependent gauge, the conformal/
Riegert-Paneitz sector) -- that portion is FRONTIER-RESERVED per p_tt_ansatz.overturning_computation
and mu_linear.boundary_condition. Uniqueness/non-uniqueness claims below are AT THIS FRAME/ORDER.

Pure stdlib. Style of rung3_spectral_structure.py / u5u6_deformability.py. Self-tested.
"""
import math

# --------------------------------------------------------------------------------------------------
# Small linear algebra on the 6-dim space of symmetric 3x3 tensors (orthonormal Frobenius basis).
# --------------------------------------------------------------------------------------------------

R2 = math.sqrt(2.0)

def sym_basis():
    """Orthonormal basis E_a of symmetric 3x3 matrices under <A,B> = sum_ij A_ij B_ij."""
    E = []
    for (i, j) in ((0, 0), (1, 1), (2, 2)):
        M = [[0.0] * 3 for _ in range(3)]
        M[i][j] = 1.0
        E.append(M)
    for (i, j) in ((0, 1), (0, 2), (1, 2)):
        M = [[0.0] * 3 for _ in range(3)]
        M[i][j] = M[j][i] = 1.0 / R2
        E.append(M)
    return E

E6 = sym_basis()

def frob(A, B):
    return sum(A[i][j] * B[i][j] for i in range(3) for j in range(3))

def mat6(op):
    """6x6 matrix of a linear operator op: sym3 -> sym3 in the E6 basis."""
    return [[frob(E6[a], op(E6[b])) for b in range(6)] for a in range(6)]

def mm(A, B):
    n = len(A)
    return [[sum(A[i][k] * B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def tr6(A):
    return sum(A[i][i] for i in range(len(A)))

def sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A))] for i in range(len(A))]

def norm6(A):
    return math.sqrt(sum(A[i][j] ** 2 for i in range(len(A)) for j in range(len(A))))

def rank(rows, tol=1e-9):
    """Rank via Gaussian elimination on copies of the row vectors."""
    M = [r[:] for r in rows]
    r = 0
    cols = len(M[0]) if M else 0
    for c in range(cols):
        piv = None
        for i in range(r, len(M)):
            if abs(M[i][c]) > tol:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        pv = M[r][c]
        M[r] = [x / pv for x in M[r]]
        for i in range(len(M)):
            if i != r and abs(M[i][c]) > tol:
                f = M[i][c]
                M[i] = [x - f * y for x, y in zip(M[i], M[r])]
        r += 1
        if r == len(M):
            break
    return r

def flat(A):
    return [A[i][j] for i in range(len(A)) for j in range(len(A))]

# --------------------------------------------------------------------------------------------------
# Projectors at fixed k-hat: T = 1 - kk, L = kk; spin projectors on symmetric tensors.
# --------------------------------------------------------------------------------------------------

def unit(v):
    n = math.sqrt(sum(x * x for x in v))
    return [x / n for x in v]

def TL(khat):
    L = [[khat[i] * khat[j] for j in range(3)] for i in range(3)]
    T = [[(1.0 if i == j else 0.0) - L[i][j] for j in range(3)] for i in range(3)]
    return T, L

def apply3(M, h, N):
    """(M h N)_ij = M_ia h_ab N_bj."""
    out = [[0.0] * 3 for _ in range(3)]
    for i in range(3):
        for j in range(3):
            out[i][j] = sum(M[i][a] * h[a][b] * N[b][j] for a in range(3) for b in range(3))
    return out

def contract(M, h):
    return sum(M[a][b] * h[a][b] for a in range(3) for b in range(3))

def projectors(khat):
    T, L = TL(khat)
    def P2(h):
        ThT = apply3(T, h, T)
        t = contract(T, h)
        return [[ThT[i][j] - 0.5 * T[i][j] * t for j in range(3)] for i in range(3)]
    def P1(h):
        A = apply3(T, h, L)
        B = apply3(L, h, T)
        return [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]
    def P0s(h):
        t = contract(T, h)
        return [[0.5 * T[i][j] * t for j in range(3)] for i in range(3)]
    def P0w(h):
        w = contract(L, h)
        return [[L[i][j] * w for j in range(3)] for i in range(3)]
    def MIX(h):  # the trace<->longitudinal mixing STRUCTURE (not a projector)
        t = contract(T, h)
        w = contract(L, h)
        return [[(T[i][j] * w + L[i][j] * t) / R2 for j in range(3)] for i in range(3)]
    return P2, P1, P0s, P0w, MIX, T, L

def gauge_orbit(khat, kmag=1.0):
    """Span of linearized spatial-diffeo directions g(xi)_ij = k_i xi_j + k_j xi_i at fixed k."""
    k = [kmag * x for x in khat]
    dirs = []
    for e in ([1, 0, 0], [0, 1, 0], [0, 0, 1]):
        g = [[k[i] * e[j] + k[j] * e[i] for j in range(3)] for i in range(3)]
        dirs.append(g)
    return dirs

# --------------------------------------------------------------------------------------------------
# The report
# --------------------------------------------------------------------------------------------------

KHATS = [unit([0.3, -0.7, 0.648]), unit([1.0, 0.2, -0.4]), unit([0.0, 0.0, 1.0])]

def part_A(kh):
    print("\n" + "=" * 94)
    print("PART A -- the spin-projector algebra at fixed k-hat (verification, not assumption)")
    print("=" * 94)
    P2, P1, P0s, P0w, MIX, T, L = projectors(kh)
    m = {n: mat6(f) for n, f in (("P2", P2), ("P1", P1), ("P0s", P0s), ("P0w", P0w))}
    S = [[m["P2"][i][j] + m["P1"][i][j] + m["P0s"][i][j] + m["P0w"][i][j] for j in range(6)] for i in range(6)]
    I6 = [[1.0 if i == j else 0.0 for j in range(6)] for i in range(6)]
    print(f"  completeness |P2+P1+P0s+P0w - 1| = {norm6(sub(S, I6)):.2e}")
    for n in m:
        print(f"  idempotence  |{n}^2-{n}| = {norm6(sub(mm(m[n], m[n]), m[n])):.2e}   dof tr{n} = {tr6(m[n]):.3f}")
    for a in ("P2", "P1", "P0s", "P0w"):
        for b in ("P2", "P1", "P0s", "P0w"):
            if a < b:
                print(f"  orthogonality tr[{a} {b}] = {tr6(mm(m[a], m[b])):.2e}")
    return m

def part_B(kh):
    print("\n" + "=" * 94)
    print("PART B -- exhaustive isotropic structure count (parity-even, pair-symmetric, fixed k-hat)")
    print("=" * 94)
    P2, P1, P0s, P0w, MIX, T, L = projectors(kh)
    structs = [mat6(f) for f in (P2, P1, P0s, P0w, MIX)]
    r = rank([flat(s) for s in structs])
    print(f"  span of {{P2, P1, P0s, P0w, MIX}} as kernel structures: rank = {r} (of 5 candidates)")
    print("  => the general SO(3)-invariant, parity-even, pair-symmetric kernel at fixed (omega,k) is")
    print("     a 5-parameter family of coefficient functions -- P^TT is ONE of FIVE structures before")
    print("     gauge/Ward constraints. (Coefficients arbitrary in (omega,k^2): exhaustive at all")
    print("     derivative orders WITHIN this frame; parity-odd and 4d-covariant completions fenced.)")
    return r

def part_C(kh):
    print("\n" + "=" * 94)
    print("PART C -- the Ward/gauge test (S5): which structures survive diffeo invariance?")
    print("=" * 94)
    P2, P1, P0s, P0w, MIX, T, L = projectors(kh)
    orbit = gauge_orbit(kh)
    names = (("P2", P2), ("P0s", P0s), ("P1", P1), ("P0w", P0w), ("MIX", MIX))
    surv = {}
    for n, f in names:
        mx = max(math.sqrt(frob(f(g), f(g))) for g in orbit)
        surv[n] = mx
        verdict = "ANNIHILATES the gauge orbit -> Ward-consistent" if mx < 1e-12 else "hits the gauge orbit -> NOT gauge-invariant alone"
        print(f"  {n:4s}: max|P(gauge dir)| = {mx:.2e}   {verdict}")
    print("\n  Little-group (helicity) note, verified by the exhaustive count of Part B (no enumerated")
    print("  structure connects the TT and scalar sectors) together with Schur/little-group reasoning:")
    print("  the gauge-invariant subspace is 3-dim = 2 TT (helicity +-2) + 1 transverse-trace scalar")
    print("  (helicity 0); rotational invariance about k-hat forbids TT<->scalar mixing (different")
    print("  helicity), so the Ward+isotropy-consistent kernel family is EXACTLY TWO independent")
    print("  coefficient functions:")
    print("     K = c2(omega,k^2) * P^TT  +  c0(omega,k^2) * P0s")
    print("\n  GAUGE-FOOTING ASYMMETRY (state it -- the two survivors are NOT on equal footing): P2 is")
    print("  invariant under the FULL linearized 4d diffeo group on FRW (helicity protection: scalar/")
    print("  vector gauge modes carry no helicity +-2 part), while P0s's transverse trace is invariant")
    print("  ONLY under the spatial subgroup at fixed slicing -- under time-dependent gauge (xi^0 != 0)")
    print("  it shifts, and full invariance requires the Bardeen completion, which is EXACTLY the")
    print("  frontier-reserved 4d-covariant portion.")
    return surv

def part_D():
    print("\n" + "=" * 94)
    print("PART D -- is the scalar channel KMS/passivity-admissible (S4)? (exhibit, not assumption)")
    print("=" * 94)
    print("  Take c0(omega) = Debye: chi0 = 1/(1 - i omega tau). Passivity requires omega*Im chi0 >= 0:")
    ok = True
    for w in (-3.0, -1.0, -0.3, 0.3, 1.0, 3.0):
        val = w * (w * 1.0 / (1.0 + (w * 1.0) ** 2))  # omega * Im[1/(1-i omega tau)], tau=1
        ok = ok and (val >= -1e-15)
        print(f"    omega={w:+.1f}:  omega*Im chi0 = {val:.4f}  (>= 0)")
    print("  => a passive, KMS-lockable, causal (retarded-analytic) scalar-channel kernel EXISTS.")
    print("     S1 (causality) constrains coefficient analyticity; S4 constrains signs -- NEITHER kills")
    print("     the scalar STRUCTURE (consistent with the banked matrix-passivity fence: passivity can")
    print("     propagate a vanishing, never source one).")
    return ok

def part_E(kh):
    print("\n" + "=" * 94)
    print("PART E -- the alpha coherence check: can the trace-sector anomaly ratio normalize P^TT?")
    print("=" * 94)
    P2, P1, P0s, P0w, MIX, T, L = projectors(kh)
    m2, m0s = mat6(P2), mat6(P0s)
    cross = tr6(mm(m0s, m2))
    delta = [[1.0 if i == j else 0.0 for j in range(3)] for i in range(3)]
    dtrace = max(abs(contract(delta, P2(E6[b]))) for b in range(6))
    print(f"  tr[P0s P2] = {cross:.2e}   (trace sector and TT sector: ZERO overlap in the basis algebra)")
    print(f"  max_b |delta_ij (P2 E_b)_ij| = {dtrace:.2e}   (P^TT output is exactly tracefree)")
    print("  => alpha * chi(omega) * P^TT is FORMALLY admissible (any scalar coefficient may multiply")
    print("     P^TT) -- but NO basis-internal identity maps the trace-sector two-point onto the TT")
    print("     amplitude: the sectors are orthogonal. alpha's VALUE cannot be transported to the TT")
    print("     normalization from within the basis; c2=alpha (this file's name for the P^TT coefficient;")
    print("     the register's historical name for the same adopted constant is c_0) is an ADOPTED")
    print("     external normalization. This RE-VERIFIES, within the enumeration, the same orthogonality")
    print("     fact that is rung9b's banked PRIMARY obstruction -- a COHERENCE CHECK, not new")
    print("     independent evidence (no new route or input enters).")
    return cross, dtrace

def part_F():
    print("\n" + "=" * 94)
    print("PART F -- comparison with the published open-EFT basis (fenced to BANKED facts only)")
    print("=" * 94)
    print("  Banked (salcedo_colas_dufner_pajer2026, overseer-verified 2026-08-02): SCDP write a")
    print("  dissipative TENSOR friction Gamma_T, distinct from alpha_M*H, with MANDATORY stochastic")
    print("  source, in a Schwinger-Keldysh open EFT -- i.e. the mainstream construction NAMES the")
    print("  tensor-sector dissipative operator explicitly. The existence of a named tensor friction")
    print("  does NOT assert TT-uniqueness. Whether their full basis also carries SCALAR-sector")
    print("  dissipative operators is NOT banked in this register -> the full-basis comparison OWES a")
    print("  primary-literature read (overseer-verifiable); do not assert it either way here.")

def main():
    print("=" * 94)
    print("OPERATOR BASIS for the quadratic influence action -- forced-vs-chosen instrument")
    print("(default-BROKEN; p_tt_ansatz is NOT an input; frame/order fences in the docstring)")
    print("=" * 94)
    kh = KHATS[0]
    part_A(kh)
    part_B(kh)
    part_C(kh)
    part_D()
    part_E(kh)
    part_F()

    print("\n" + "=" * 94)
    print("VERDICT (default-BROKEN, honest; AT THE ENUMERATED FRAME/ORDER -- graduates nothing):")
    print("=" * 94)
    print("  (b) CHOSEN at this frame/order: P^TT is NOT unique. Under the full declared inventory")
    print("  (S1 causality, S2 quadratic, S4 KMS/passivity, S5 diffeo-Ward, S6 homogeneity/isotropy,")
    print("  parity-even), the admissible kernel family is TWO independent structures:")
    print("      K = c2 * P^TT  +  c0 * P0s   (transverse-trace scalar),")
    print("  and the scalar channel is exhibited passivity-satisfiable. Restricting c0 = 0 is exactly")
    print("  the p_tt_ansatz choice -- an INPUT, not a consequence, at this order.")
    print("  KC checklist: KC1 clean (enumeration starts from FULL symmetric rank-2; TT never input);")
    print("  KC2 clean (no radiative-dof argument used; the scalar survivor is constrained-sector")
    print("  response -- exactly the KC2 distinction); KC3 clean (no empirical input enters); KC4")
    print("  witness (the surviving scalar is naturally identified with the f(R)/scalar-tensor response")
    print("  channel -- the basis correctly does NOT force TT in theories known to carry a scalar")
    print("  response); KC5 FENCE")
    print("  (spatial-SVT fixed-slicing frame; parity-even; pair-symmetric; 4d-covariant/Riegert-")
    print("  Paneitz completion FRONTIER-RESERVED -- the full-order question stays OPEN).")
    print("  Per the directional guard: this lands on the NON-flattering horn via the light bar")
    print("  ((b) = exhibit one admissible non-TT structure -- exhibited: P0s with Debye c0).")
    print("  LEDGER FENCE: no ledger field touched; eft_operator_basis banks at 0; any p_tt_ansatz")
    print("  consequence is a SEPARATE screen (the p_tt interrogation runs on this instrument).")

    ok = _selftest()
    print(f"\n  SELFTEST: {'PASS' if ok else 'FAIL'}")
    return 0 if ok else 1

# --------------------------------------------------------------------------------------------------
# Exhaustiveness COMPUTED (not asserted): the commutant of the little group O(2) (rotations about
# k-hat + a reflection fixing k-hat) acting on sym-3 kernels. Pair-symmetric commutant must be 5-dim
# (the enumerated structures ARE exhaustive); unrestricted commutant is 6-dim (the +1 is the single
# pair-antisymmetric trace-longitudinal mixer, itself Ward-killed).
# --------------------------------------------------------------------------------------------------

def rot_about(khat, theta):
    """Rodrigues rotation matrix about khat by theta."""
    kx, ky, kz = khat
    K = [[0.0, -kz, ky], [kz, 0.0, -kx], [-ky, kx, 0.0]]
    c, s = math.cos(theta), math.sin(theta)
    R = [[(1.0 if i == j else 0.0) * c + s * K[i][j] + (1 - c) * khat[i] * khat[j]
          for j in range(3)] for i in range(3)]
    return R

def rep6(R):
    """The induced 6x6 rep on symmetric tensors: h -> R h R^T."""
    def op(h):
        Rh = [[sum(R[i][a] * h[a][b] for a in range(3)) for b in range(3)] for i in range(3)]
        return [[sum(Rh[i][b] * R[j][b] for b in range(3)) for j in range(3)] for i in range(3)]
    return mat6(op)

def commutant_dims(khat):
    """(dim of full little-group commutant, dim of pair-symmetric commutant) on 6x6 kernels."""
    # a reflection fixing khat: S = I - 2 n n^T with n orthogonal to khat
    trial = [1.0, 0.0, 0.0] if abs(khat[0]) < 0.9 else [0.0, 1.0, 0.0]
    dot = sum(trial[i] * khat[i] for i in range(3))
    n = unit([trial[i] - dot * khat[i] for i in range(3)])
    gens = [rep6(rot_about(khat, 0.7)), rep6(rot_about(khat, 1.9)),
            rep6([[(1.0 if i == j else 0.0) - 2 * n[i] * n[j] for j in range(3)] for i in range(3)])]
    rows = []
    for M in gens:  # (M X - X M) = 0, coefficient of X[a][b] in eq (i,j): M[i][a] d_jb - d_ia M[b][j]
        for i in range(6):
            for j in range(6):
                row = [0.0] * 36
                for a in range(6):
                    for b in range(6):
                        row[a * 6 + b] = (M[i][a] if b == j else 0.0) - (M[b][j] if a == i else 0.0)
                rows.append(row)
    dim_full = 36 - rank(rows)
    sym_rows = []
    for a in range(6):
        for b in range(a + 1, 6):
            row = [0.0] * 36
            row[a * 6 + b], row[b * 6 + a] = 1.0, -1.0
            sym_rows.append(row)
    dim_sym = 36 - rank(rows + sym_rows)
    return dim_full, dim_sym

# --------------------------------------------------------------------------------------------------
# Self-test: verify the algebra and every load-bearing numeric claim, at MULTIPLE k-hats.
# --------------------------------------------------------------------------------------------------

def _selftest():
    ok = True
    I6 = [[1.0 if i == j else 0.0 for j in range(6)] for i in range(6)]
    for kh in KHATS:
        P2, P1, P0s, P0w, MIX, T, L = projectors(kh)
        m = {n: mat6(f) for n, f in (("P2", P2), ("P1", P1), ("P0s", P0s), ("P0w", P0w))}
        S = [[m["P2"][i][j] + m["P1"][i][j] + m["P0s"][i][j] + m["P0w"][i][j] for j in range(6)] for i in range(6)]
        if norm6(sub(S, I6)) > 1e-10:
            print("   [FAIL] completeness"); ok = False
        for n, d in (("P2", 2.0), ("P1", 2.0), ("P0s", 1.0), ("P0w", 1.0)):
            if norm6(sub(mm(m[n], m[n]), m[n])) > 1e-10 or abs(tr6(m[n]) - d) > 1e-10:
                print(f"   [FAIL] {n} idempotence/dof"); ok = False
        for a in ("P2", "P1", "P0s", "P0w"):
            for b in ("P2", "P1", "P0s", "P0w"):
                if a < b and abs(tr6(mm(m[a], m[b]))) > 1e-10:
                    print(f"   [FAIL] orthogonality {a},{b}"); ok = False
        structs = [mat6(f) for f in (P2, P1, P0s, P0w, MIX)]
        if rank([flat(s) for s in structs]) != 5:
            print("   [FAIL] isotropic structure count != 5"); ok = False
        # EXHAUSTIVENESS COMPUTED: little-group commutant dims (full=6, pair-symmetric=5)
        dim_full, dim_sym = commutant_dims(kh)
        if dim_sym != 5:
            print(f"   [FAIL] pair-symmetric little-group commutant dim {dim_sym} != 5 -- enumeration NOT exhaustive"); ok = False
        if dim_full != 6:
            print(f"   [FAIL] full little-group commutant dim {dim_full} != 6 (expected 5 sym + 1 antisym)"); ok = False
        orbit = gauge_orbit(kh)
        for n, f, mustkill in (("P2", P2, True), ("P0s", P0s, True), ("P1", P1, False), ("P0w", P0w, False)):
            mx = max(math.sqrt(frob(f(g), f(g))) for g in orbit)
            if mustkill and mx > 1e-12:
                print(f"   [FAIL] {n} does not annihilate gauge orbit"); ok = False
            if (not mustkill) and mx < 1e-6:
                print(f"   [FAIL] {n} unexpectedly annihilates gauge orbit"); ok = False
        if abs(tr6(mm(mat6(P0s), mat6(P2)))) > 1e-12:
            print("   [FAIL] trace/TT sectors not orthogonal"); ok = False
        delta = [[1.0 if i == j else 0.0 for j in range(3)] for i in range(3)]
        if max(abs(contract(delta, P2(E6[b]))) for b in range(6)) > 1e-12:
            print("   [FAIL] P2 output not tracefree"); ok = False
    # passivity exhibit for the scalar Debye channel
    for w in (-2.0, -0.5, 0.5, 2.0):
        if w * (w / (1.0 + w * w)) < -1e-15:
            print("   [FAIL] scalar Debye passivity"); ok = False
    return ok


if __name__ == "__main__":
    raise SystemExit(main())
