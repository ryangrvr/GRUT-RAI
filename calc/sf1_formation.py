"""SF-1 formation run: the single authorized execution of SF1_FORMATION_CHARTER_01.md (frozen at
8a4f71c). Authority: SF1_OWNER_RULING_01.md, Issue #2 comment 5903400225, with a campaign-specific
v4 exception for SF-1 only.

Parent (charter §1): H_F = -sum_j (c_j^dag c_{j+1} + h.c.) on the periodic ring Z_L, L even.
- It is one Fock-space Hamiltonian.
- There is no chemical potential and no sector-specific term.
- Single-particle levels are eps(k) = -2 cos k, with k = 2 pi j / L.

Sector selector (§2): the conserved N, which is odd. The reference state is the sector ground state.

Readout (§4): rho_q = sum_j e^{-iqj} n_j. The object is the support of S_{L,N}(q, w).

Invariants (§5):
- I-z = z_P (the L -> inf limit at fixed q, then q -> 0).
- I-q = number of soft momenta, modulo q ~ -q ~ q + 2 pi.

Controls (§6): V-FOCK, A-ODD, C-1 ... C-5 are gating. C-6 is REPORT-ONLY.

Terminal (§7): mechanical. An integrity failure gives RUN VOID.

This script is run ONCE. Any exception is caught, recorded as an integrity/implementation defect,
and the run is RUN VOID. A void run is never silently repaired and re-run.

Usage: python3 calc/sf1_formation.py   (writes SF1_FORMATION_RESULT.json)
"""
import hashlib
import inspect
import json
import math
import pathlib
import sys
import traceback
from fractions import Fraction

import mpmath as mp
import numpy as np
import sympy as sp

ROOT = pathlib.Path(__file__).resolve().parent.parent
CHARTER = ROOT / "SF1_FORMATION_CHARTER_01.md"
CHARTER_COMMIT = "8a4f71c"
OUT = ROOT / "SF1_FORMATION_RESULT.json"
mp.mp.dps = 60

LOG = []


def say(msg):
    print(msg)
    LOG.append(msg)


# ============================ PARENT / READOUT (C-5: one of each, no family tag) ================
def bonds(L):
    """The only definition of the parent's couplings: periodic nearest-neighbour ring."""
    return [(j, (j + 1) % L) for j in range(L)]


def eps(k):
    """Single-particle level of H_F at momentum k (float), from the bonds: -(e^{ik} + e^{-ik})."""
    return -2.0 * math.cos(k)


def fock_H(L):
    """Full 2^L Fock-space H_F built once from bonds(L), with Jordan-Wigner signs. Returns a dense
    matrix. Asserts that N is conserved entry by entry."""
    dim = 1 << L
    H = np.zeros((dim, dim))
    for s in range(dim):
        for (a, b) in bonds(L):
            for (i, j) in ((a, b), (b, a)):  # c_i^dag c_j
                if not (s >> j) & 1:
                    continue
                s1 = s ^ (1 << j)
                sg1 = -1 if bin(s & ((1 << j) - 1)).count("1") % 2 else 1
                if (s1 >> i) & 1:
                    continue
                sg2 = -1 if bin(s1 & ((1 << i) - 1)).count("1") % 2 else 1
                s2 = s1 | (1 << i)
                assert bin(s2).count("1") == bin(s).count("1")
                H[s2, s] += -1.0 * sg1 * sg2
    assert np.allclose(H, H.T)
    return H


def occupied(L, N):
    """Sector reference-state occupation (odd N): j = -M..M (mod L), M = (N-1)/2. Verified by A-ODD
    and V-FOCK."""
    assert N % 2 == 1 and 1 <= N <= L - 1
    M = (N - 1) // 2
    return sorted({j % L for j in range(-M, M + 1)})


def ff_support(L, N, m):
    """I-FF support energies at q = 2 pi m / L (the multiset of particle-hole energies)."""
    M = (N - 1) // 2
    js = np.arange(-M, M + 1)  # signed occupied indices (same set as occupied(L, N))
    mask = np.zeros(L, dtype=bool)
    mask[np.array(occupied(L, N))] = True
    ok = ~mask[(js + m) % L]
    j = js[ok]
    # eps(k2) - eps(k1) = 2cos k1 - 2cos k2 = 4 sin(pi(2j+m)/L) sin(pi m/L)  (exact identity;
    # integer arguments avoid cancellation)
    return 4 * np.sin(np.pi * (2 * j + m) / L) * np.sin(np.pi * m / L)


def ff_lower_edge(L, N, m):
    """Finite-L lower support edge w^-_{L,N}(2 pi m / L) via I-FF."""
    v = ff_support(L, N, m)
    return float(v.min()) if v.size else None


def fock_sector_support(evals, evecs, basis, L, m):
    """Grouped (degenerate-eigenspace-summed) support of rho_q acting on the sector ground state."""
    q = 2 * np.pi * m / L
    phases = np.exp(-1j * q * np.arange(L))
    d = np.array([sum(phases[j] for j in range(L) if (s >> j) & 1) for s in basis])
    v = d * evecs[:, 0]
    amps = evecs.conj().T @ v
    w = np.abs(amps) ** 2
    E = evals - evals[0]
    groups = []
    for e, wt in sorted(zip(E, w)):
        if groups and abs(e - groups[-1][0]) < 1e-9:
            groups[-1][1] += wt
        else:
            groups.append([e, wt])
    return [(e, wt) for e, wt in groups if wt > 1e-12]


def group_vals(vals, tol=1e-9):
    out = []
    for v in sorted(vals):
        if out and abs(v - out[-1][0]) < tol:
            out[-1][1] += 1
        else:
            out.append([v, 1])
    return out


# ============================ FAMILIES (charter §3, frozen) ======================================
Ls_ = sp.Symbol("L", positive=True)
FAMILIES = {
    "D":   dict(role="primary dense", Ls=[258, 1026, 4098, 16386], N=lambda L: L // 2,
                kFinf=sp.pi / 2, Nsym=Ls_ / 2, report_only=False),
    "E":   dict(role="primary dilute", Ls=[256, 1024, 4096, 16384], N=lambda L: 1,
                kFinf=sp.Integer(0), Nsym=sp.Integer(1), report_only=False),
    "D14": dict(role="C-2 control (nu=1/4)", Ls=[260, 1028, 4100, 16388], N=lambda L: L // 4,
                kFinf=sp.pi / 4, Nsym=Ls_ / 4, report_only=False),
    "D34": dict(role="C-1 control (PH of D14)", Ls=[260, 1028, 4100, 16388],
                N=lambda L: 3 * L // 4, kFinf=3 * sp.pi / 4, Nsym=3 * Ls_ / 4, report_only=False),
    "E3":  dict(role="C-3 control (N0=3)", Ls=[256, 1024, 4096, 16384], N=lambda L: 3,
                kFinf=sp.Integer(0), Nsym=sp.Integer(3), report_only=False),
    "Ebar": dict(role="C-1 control (PH of E)", Ls=[256, 1024, 4096, 16384], N=lambda L: L - 1,
                 kFinf=sp.pi, Nsym=Ls_ - 1, report_only=False),
    "C6":  dict(role="C-6 REPORT-ONLY crossover", Ls=[290, 1090, 4226, 16642, 66050],
                N=None, kFinf=sp.Integer(0), Nsym=sp.sqrt(Ls_), report_only=True),
}


def nearest_odd_sqrt(L):
    """Nearest odd integer to sqrt(L), ties to the lower odd (charter §3)."""
    r = math.isqrt(L)
    cands = [c for c in range(max(1, r - 3), r + 4) if c % 2 == 1]
    sq = mp.sqrt(L)  # 60-digit comparison; ties (impossible for the frozen L) go to the lower c
    return min(cands, key=lambda c: (abs(mp.mpf(c) - sq), c))


FAMILIES["C6"]["N"] = nearest_odd_sqrt


def kF_L(L, N):
    return math.pi * (N - 1) / L


# ============================ CLOSED FORMS (charter §5) =========================================
def mpf_of(x):
    return mp.mpf(str(sp.N(x, 70)))


def omega_cf_mp(q, kF):
    """Closed-form P-limit lower edge: the infimum of eps(k+q) - eps(k) over the limit allowed set
    k in [-kF, kF], k+q in [kF, 2pi-kF], for q in (0, pi]."""
    q = q if isinstance(q, mp.mpf) else mp.mpf(q)
    kF = kF if isinstance(kF, mp.mpf) else mpf_of(kF)
    lo = max(-kF, kF - q)
    hi = min(kF, 2 * mp.pi - kF - q)
    if lo > hi:
        return None
    return 4 * mp.sin(q / 2) * min(mp.sin(lo + q / 2), mp.sin(hi + q / 2))


def omega_cf_np(q, kF):
    lo = np.maximum(-kF, kF - q)
    hi = np.minimum(kF, 2 * np.pi - kF - q)
    val = 4 * np.sin(q / 2) * np.minimum(np.sin(lo + q / 2), np.sin(hi + q / 2))
    return np.where(lo <= hi, val, np.nan)


qs = sp.Symbol("q", positive=True)


def small_q_branch(kFinf):
    """Exact small-q specialization of the closed form, checked numerically against the general
    form."""
    if kFinf == 0:
        lo, hi = sp.Integer(0), sp.Integer(0)
    elif kFinf == sp.pi:
        lo, hi = sp.pi - qs, sp.pi - qs
    else:
        lo, hi = kFinf - qs, kFinf
    a = sp.sin(lo + qs / 2)
    b = sp.sin(hi + qs / 2)
    diff = sp.simplify(a - b)
    if diff == 0:
        br = a
    else:
        br = None
        for p in range(1, 5):
            lim = sp.limit(diff / qs ** p, qs, 0, "+")
            if lim.is_number and lim != 0:
                br = b if lim > 0 else a
                break
        if br is None:
            return None, "branch undecidable"
    expr = 4 * sp.sin(qs / 2) * br
    for qv in ("1e-2", "1e-3", "1e-4"):
        gen = omega_cf_mp(qv, mpf_of(kFinf))
        spec = mp.mpf(str(sp.N(expr.subs(qs, sp.Float(qv, 70)), 60)))
        if gen is None or abs(gen - spec) > mp.mpf("1e-40") * max(1, abs(gen)):
            return None, f"specialization mismatch at q={qv}"
    return expr, "ok"


def z_P(kFinf):
    expr, st = small_q_branch(kFinf)
    if expr is None:
        return "UNDEFINED", st, None
    z = sp.limit(sp.log(expr) / sp.log(qs), qs, 0, "+")
    if not (z.is_number and z.is_finite and z > 0):
        return "UNDEFINED", f"limit {z}", str(expr)
    return z, "ok", str(expr)


def z_Pprime(Nsym):
    t = sp.Symbol("t", positive=True)
    w1 = 4 * sp.sin(sp.pi / Ls_) * sp.sin(sp.pi * Nsym / Ls_)
    w1t = sp.simplify(w1.subs(Ls_, 1 / t))
    z = sp.limit(sp.log(w1t) / sp.log(t), t, 0, "+")
    if not (z.is_number and z.is_finite and z > 0):
        return "UNDEFINED", str(w1)
    return z, str(w1)


def fold(x):
    """Representative of q modulo q ~ -q ~ q + 2 pi, in [0, pi] (exact sympy)."""
    r = sp.Mod(x, 2 * sp.pi)
    if r > sp.pi:
        r = 2 * sp.pi - r
    return sp.nsimplify(r)


def soft_set(kFinf):
    raw = [sp.Integer(0), sp.Mod(2 * kFinf, 2 * sp.pi), sp.Mod(-2 * kFinf, 2 * sp.pi)]
    folded = sorted({fold(x) for x in raw}, key=lambda v: float(v))
    kf = mpf_of(kFinf)
    checks = []
    for qstar in folded:
        pts = []
        for sgn in (+1, -1):
            qv = mpf_of(qstar) + sgn * mp.mpf("1e-12")
            if mp.mpf(0) < qv <= mp.pi:
                pts.append(omega_cf_mp(qv, kf))
        ok = bool(pts) and all(p is not None and abs(p) < mp.mpf("1e-9") for p in pts)
        checks.append({"q_star": str(qstar), "vanishes": ok})
    grid = np.pi * np.arange(1, 200001) / 200000
    vals = omega_cf_np(grid, float(kf))
    fl = np.array([float(v) for v in folded])
    far = np.min(np.abs(grid[:, None] - fl[None, :]), axis=1) > 2e-2
    extra = bool(np.any(np.isnan(vals[far])) or np.any(vals[far] < 1e-4))
    defined = all(c["vanishes"] for c in checks) and not extra
    return {"raw": [str(x) for x in raw], "folded": [str(x) for x in folded],
            "candidate_checks": checks, "extra_soft_in_scan": extra,
            "n_soft": len(folded) if defined else "UNDEFINED"}


def grid_m(L, r):
    """q = pi/2^r -> nearest grid m, ties to lower m."""
    x = Fraction(L, 2 ** (r + 1))
    f = x.numerator // x.denominator
    return f if x - f <= Fraction(1, 2) else f + 1


# ============================ RUN =================================================================
R = {"charter": "SF1_FORMATION_CHARTER_01.md", "charter_commit": CHARTER_COMMIT,
     "authority": "SF1_OWNER_RULING_01.md (comment 5903400225)",
     "charter_sha256": hashlib.sha256(CHARTER.read_bytes()).hexdigest(),
     "script_sha256": hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()}
INTEG = {}
DEFECTS = []


def run():
    # ---------------- C-5 audit -------------------------------------------------------------
    say("=== C-5 common parent / readout audit ===")
    fns = [bonds, eps, fock_H, occupied, ff_support, ff_lower_edge, fock_sector_support]
    audit = {}
    ok5 = True
    for f in fns:
        src = inspect.getsource(f)
        params = list(inspect.signature(f).parameters)
        bad = [p for p in params if p.lower() in ("fam", "family", "tag", "sector", "kind", "role")]
        refs = "FAMILIES" in src or "role" in src
        audit[f.__name__] = {"sha256": hashlib.sha256(src.encode()).hexdigest(), "params": params,
                             "family_tag_param": bad, "references_family_table": refs}
        ok5 &= (not bad) and (not refs)
    INTEG["C-5"] = {"pass": ok5, "functions": audit}
    say(f"  C-5 pass = {ok5}")

    # ---------------- V-FOCK + A-ODD (Fock part) + C-1 (Fock part) ----------------------------
    say("=== V-FOCK (full Fock space, one H per L) ===")
    vf = {}
    okV, okAF, okC1F = True, True, True
    fock_store = {}
    for L in (6, 10, 12):
        H = fock_H(L)
        Ns = {1, 3, L - 3, L - 1}
        if L in (6, 10):
            Ns.add(L // 2)
        if L == 12:
            Ns |= {L // 4, 3 * L // 4}
        for N in sorted(Ns):
            basis = [s for s in range(1 << L) if bin(s).count("1") == N]
            blk = H[np.ix_(basis, basis)]
            ev, U = np.linalg.eigh(blk)
            gap = float(ev[1] - ev[0]) if len(ev) > 1 else float("inf")
            occ = occupied(L, N)
            E0an = sum(eps(2 * math.pi * j / L) for j in occ)
            rec = {"dim": len(basis), "E0": float(ev[0]), "E0_analytic": E0an, "gap": gap}
            sup_ok = True
            sups = {}
            for m in range(1, L):
                fs = fock_sector_support(ev, U, basis, L, m)
                ff = group_vals(ff_support(L, N, m).tolist())
                same = (len(fs) == len(ff) and all(abs(a[0] - b[0]) <= 1e-10 for a, b in zip(fs, ff)))
                wmatch = same and all(abs(a[1] - b[1]) < 1e-8 for a, b in zip(fs, ff))
                sups[m] = [round(e, 12) for e, _ in fs]
                if not same:
                    sup_ok = False
                rec.setdefault("unit_weight_match_all_m", True)
                rec["unit_weight_match_all_m"] &= bool(wmatch)
            rec["support_matches_IFF"] = sup_ok
            rec["unique_ground_state"] = bool(gap > 1e-9)
            rec["A_ODD_energy_match"] = bool(abs(ev[0] - E0an) <= 1e-10)
            okV &= sup_ok and rec["unique_ground_state"]
            okAF &= rec["A_ODD_energy_match"] and rec["unique_ground_state"]
            fock_store[(L, N)] = (np.sort(ev), sups)
            vf[f"L={L},N={N}"] = rec
            say(f"  L={L:2d} N={N:2d} dim={len(basis):4d} gap={gap:.3e} "
                f"E0={ev[0]:+.12f} (analytic {E0an:+.12f}) support==IFF:{sup_ok}")
        del H
    c1f = {}
    for (L, N), (spec, sups) in fock_store.items():
        if (L, L - N) in fock_store and N <= L - N:
            spec2, sups2 = fock_store[(L, L - N)]
            sp_eq = len(spec) == len(spec2) and bool(np.max(np.abs(spec - spec2)) <= 1e-10)
            su_eq = all(len(sups[m]) == len(sups2[m]) and
                        all(abs(a - b) <= 1e-10 for a, b in zip(sups[m], sups2[m])) for m in sups)
            c1f[f"L={L}: N={N} <-> {L - N}"] = {"spectra_equal": sp_eq, "supports_equal": su_eq}
            okC1F &= sp_eq and su_eq
    INTEG["V-FOCK"] = {"pass": okV, "sectors": vf}
    say(f"  V-FOCK pass = {okV};  C-1 (Fock) pass = {okC1F}")

    # ---------------- A-ODD analytic on every sector ------------------------------------------
    say("=== A-ODD analytic control (all sectors) ===")
    okA = okAF
    aodd = {}
    sectors = [(L, N) for (L, N) in fock_store]
    for tag, F_ in FAMILIES.items():
        for L in F_["Ls"]:
            sectors.append((L, F_["N"](L)))
    for (L, N) in sectors:
        M = (N - 1) // 2
        a = lambda j: min(j % L, (L - j) % L)
        lowest = {j for j in range(L) if a(j) <= M}
        occ = set(occupied(L, N))
        holes = set(range(L)) - occ
        c_i = (N % 2 == 1) and len(lowest) == N and lowest == occ and \
            all((x in occ) and ((L - x) % L in occ) for x in range(1, M + 1))
        c_ii = (M + 1 <= L // 2) and (eps(2 * math.pi * (M + 1) / L) - eps(2 * math.pi * M / L) > 0)
        c_iii = (L // 2 in holes) and all(((L - h) % L) in holes for h in holes) and \
            (len(holes) % 2 == 1)
        aodd[f"L={L},N={N}"] = {"i": c_i, "ii": c_ii, "iii": c_iii}
        okA &= c_i and c_ii and c_iii
    INTEG["A-ODD"] = {"pass": okA, "fock_agreement": okAF, "n_sectors": len(aodd),
                      "failures": {k: v for k, v in aodd.items() if not all(v.values())}}
    say(f"  A-ODD pass = {okA} over {len(aodd)} sectors")

    # ---------------- per-family closed forms + numeric cross-checks --------------------------
    say("=== Families: closed forms, P and P' ===")
    fam = {}
    okNum = True
    for tag, F_ in FAMILIES.items():
        kFinf = F_["kFinf"]
        zp, zst, expr = z_P(kFinf)
        zpp, w1expr = z_Pprime(F_["Nsym"])
        soft = soft_set(kFinf)
        # numeric cross-check at the largest L (charter §5)
        Lmax = F_["Ls"][-1]
        N = F_["N"](Lmax)
        xs = []
        num_ok = True
        for r in (1, 2, 3, 4, 5):
            m = grid_m(Lmax, r)
            fin = ff_lower_edge(Lmax, N, m)
            cf = omega_cf_mp(mp.pi / 2 ** r, mpf_of(kFinf))
            tol = 4 * abs(kF_L(Lmax, N) - float(kFinf)) + 20 * math.pi / Lmax
            dev = abs(fin - float(cf))
            xs.append({"q": f"pi/{2 ** r}", "m": m, "finite": fin, "closed": float(cf),
                       "dev": dev, "tol": tol, "ok": bool(dev <= tol)})
            num_ok &= bool(dev <= tol)
        # omega_1 closed form vs enumeration at every L
        w1 = []
        for L in F_["Ls"]:
            N_ = F_["N"](L)
            fin = ff_lower_edge(L, N_, 1)
            cf = 4 * math.sin(math.pi / L) * math.sin(math.pi * N_ / L)
            rel = abs(fin - cf) / abs(cf)
            w1.append({"L": L, "N": N_, "kF_L": kF_L(L, N_), "omega1": fin, "closed": cf,
                       "rel": rel, "ok": bool(rel <= 1e-12)})
            num_ok &= bool(rel <= 1e-12)
        slopes = [-(math.log(w1[i + 1]["omega1"]) - math.log(w1[i]["omega1"])) /
                  (math.log(w1[i + 1]["L"]) - math.log(w1[i]["L"])) for i in range(len(w1) - 1)]
        cls = (str(zp), soft["n_soft"])
        fam[tag] = {"role": F_["role"], "report_only": F_["report_only"],
                    "kF_inf": str(kFinf), "z_P": str(zp), "z_P_status": zst,
                    "small_q_edge": expr, "z_Pprime": str(zpp), "omega1_closed": w1expr,
                    "I_q": soft, "class": [str(zp), soft["n_soft"]],
                    "numeric_P": xs, "numeric_omega1": w1,
                    "omega1_logslopes_report": slopes, "numeric_ok": num_ok}
        if not F_["report_only"]:
            okNum &= num_ok
        say(f"  {tag:5s} kF_inf={str(kFinf):6s} z_P={str(zp):4s} z_P'={str(zpp):4s} "
            f"soft(folded)={soft['folded']} n_soft={soft['n_soft']} numeric_ok={num_ok}")
    INTEG["closed_form_numeric"] = {"pass": okNum}

    # ---------------- C-1 family + quotient ---------------------------------------------------
    def cl(t):
        return tuple(fam[t]["class"])
    q_ok = fam["D14"]["I_q"]["folded"] == fam["D34"]["I_q"]["folded"]
    raw_differ = fam["D14"]["I_q"]["raw"][1] != fam["D34"]["I_q"]["raw"][1]
    okC1 = okC1F and cl("D14") == cl("D34") and cl("E") == cl("Ebar") and q_ok
    INTEG["C-1"] = {"pass": okC1, "fock": c1f, "class_D14_eq_D34": cl("D14") == cl("D34"),
                    "class_E_eq_Ebar": cl("E") == cl("Ebar"),
                    "quotient_verified_folded_equal": q_ok,
                    "raw_2kF_representatives": {"D14": fam["D14"]["I_q"]["raw"][1],
                                                "D34": fam["D34"]["I_q"]["raw"][1],
                                                "differ_before_quotient": raw_differ}}
    say(f"  C-1 pass = {okC1} (quotient: folded equal {q_ok}; raw 2kF reps differ {raw_differ})")
    return fam


def terminal(fam):
    integ_ok = all(INTEG[k]["pass"] for k in ("C-5", "V-FOCK", "A-ODD", "C-1", "closed_form_numeric"))
    if not integ_ok:
        return "RUN VOID", {"failed": [k for k in INTEG if not INTEG[k]["pass"]]}

    def cl(t):
        return tuple(fam[t]["class"])

    def undefined(t):
        return fam[t]["z_P"] == "UNDEFINED" and fam[t]["I_q"]["n_soft"] == "UNDEFINED"
    # SECTOR-SMUGGLED is decided by the C-5 audit (single parent/readout functions, no sector tag).
    # Reaching this point requires C-5 to have passed, so it cannot fire independently here.
    smuggled = not INTEG["C-5"]["pass"]
    c4 = {t: fam[t]["z_P"] == fam[t]["z_Pprime"] and fam[t]["z_P"] != "UNDEFINED"
          for t in ("D", "E", "D14", "D34", "E3", "Ebar")}
    c2 = cl("D14") == cl("D")
    c3 = cl("E3") == cl("E")
    ctrl = {"C-2": c2, "C-3": c3, "C-4": c4}
    if smuggled:
        return "SECTOR-SMUGGLED", ctrl
    if undefined("D") or undefined("E") or undefined("D14") or undefined("E3"):
        return "UNFORMULABLE", ctrl
    if cl("D") == cl("E"):
        return "STATE-NOT-LAW", ctrl
    if not all(c4.values()):
        return "EDGE-ONLY-NONROBUST", ctrl
    if not (c2 and c3):
        return "EDGE-ONLY-NONROBUST", ctrl
    return "FORMATION-OF-LAW-CLASS", ctrl


def c6_report(fam):
    f = fam["C6"]
    unique = f["z_P"] == f["z_Pprime"]
    kfs = [(w["L"], w["kF_L"]) for w in f["numeric_omega1"]]
    kslopes = [(math.log(kfs[i + 1][1]) - math.log(kfs[i][1])) /
               (math.log(kfs[i + 1][0]) - math.log(kfs[i][0])) for i in range(len(kfs) - 1)]
    t = sp.Symbol("t", positive=True)
    kf_exp = sp.limit(sp.log((sp.pi * (sp.sqrt(Ls_) - 1) / Ls_).subs(Ls_, 1 / t)) / sp.log(1 / t),
                      t, 0, "+")
    return {"N_L": [w["N"] for w in f["numeric_omega1"]],
            "kF_L_exact": "pi*(N_L-1)/L", "kF_values": kfs,
            "kF_scaling_exponent_symbolic(N~sqrt L)": str(kf_exp),
            "kF_logslopes_report": kslopes,
            "z_P": f["z_P"], "z_Pprime": f["z_Pprime"],
            "unique_one_parameter_z": unique,
            "label": "single z" if unique else "MULTISCALE / PATH-DEPENDENT IR",
            "numeric_ok_report": f["numeric_ok"], "terminal_effect": "NONE (report-only)"}


if __name__ == "__main__":
    fam = None
    try:
        fam = run()
        term, ctrl = terminal(fam)
        R["families"] = fam
        R["controls"] = ctrl
        R["C6_report"] = c6_report(fam)
    except Exception:
        tb = traceback.format_exc()
        DEFECTS.append(tb)
        print(tb)
        term, ctrl = "RUN VOID", {"exception": tb}
        R["families"] = fam
    R["integrity"] = INTEG
    R["defects"] = DEFECTS
    R["terminal"] = term
    R["log"] = LOG
    OUT.write_text(json.dumps(R, indent=1, default=str) + "\n")
    print(f"\nTERMINAL: {term}")
    print(f"controls: {json.dumps(ctrl, default=str)}")
    if "C6_report" in R:
        print(f"C-6: {R['C6_report']['label']} (z_P={R['C6_report']['z_P']}, "
              f"z_P'={R['C6_report']['z_Pprime']})")
    print(f"wrote {OUT.name}; sha256 {hashlib.sha256(OUT.read_bytes()).hexdigest()}")
