#!/usr/bin/env python3
"""kernel_transport_rule: can GRUT derive a dS->FRW kernel transport rule from admitted inputs?

CHARTER: KERNEL_TRANSPORT_CHARTER_01.md (pre-registration frozen at commit c30f18e BEFORE this
instrument ran). The owner's question verbatim: derive the transport rule from already admitted
principles and inputs; if not derivable, establish precisely what additional structure is
required; if multiple inequivalent rules survive, that nonuniqueness is itself the structural
result. EXISTENCE-ASSUMPTION FENCE: nothing below presumes the law exists.

OBJECT (E7 discharged): the free TT graviton retarded/commutator kernel per comoving mode k,
built from the C1-validated tensor primitive v'' + (k^2 - a''/a)v = 0, h = v/a (admitted input
A4). This object is STATE-INDEPENDENT: with any two independent solutions u1,u2 of unit
Wronskian, Ghat(e,e') = u1(e)u2(e') - u2(e)u1(e') is basis-independent, and the h-field
commutator kernel is K = Ghat/(a a') up to one universal constant that cancels in every ratio
below. The noise/KMS side is derivational only (T-III, in the verdict document).

ROUTES (charter section 3):
  T-I  local substitution family: K_dS applied over the lag with rate H_* in {H_obs(=H0 at this
       grid), H_mid, H_emis}, comoving-k identification, scale factor matched at emission.
  T-II the exact kernel on the declared LCDM background (Om = 0.315) -- computable from A4/A7.
  adiabaticity control: eps(z) = (3/2) Om(z), the small parameter every local rule assumes.

GRID (frozen): k/(a0 H0) in {0.5, 1, 2}; emission z' in {0.296, 1, 3}; observation t = t0.
METRIC: Delta(r) = |K_r - K_exact| / max_grid |K_exact|.
CLASSIFICATION (frozen): O-DERIVED iff one member has Delta <= 0.10 over the ENTIRE grid;
O-NONUNIQUE iff no member passes and two members differ by > 0.25 somewhere; O-MISSING iff the
family is tight (< 0.25) yet wrong. Register untouched; ledger 0. Pure stdlib.
"""
import cmath
import hashlib
import json
import math
import os
import sys
import time

FAIL = []
CHECKS = []


def check(ok, msg, kind="ok"):
    tag = {"ok": "ok  ", "ctrl": "ctrl", "note": "note", "halt": "HALT"}[kind]
    print(f"  {tag if ok or kind == 'note' else 'FAIL'}   {msg}")
    CHECKS.append({"ok": bool(ok), "kind": kind, "msg": msg})
    if not ok and kind != "note":
        FAIL.append(msg)


OM, OL = 0.315, 0.685  # repo central background (charter A7); units a0 = 1, H0 = 1


def E_of_a(a):
    return math.sqrt(OM / a ** 3 + OL)


# =============================================================================================
# Background + mode integration in conformal time (RK4), from z = 200 to today
# =============================================================================================
class Run:
    """Integrates [a, v1, v1', v2, v2'] in conformal time on a given background."""

    def __init__(self, k, bg="lcdm", H_star=None, a_emis=None, n_steps=120000, a_start=1/201.0,
                 a_end=1.0):
        self.k, self.bg, self.H_star, self.a_emis = k, bg, H_star, a_emis
        self.eta, self.a, self.t, self.v1, self.v2 = [], [], [], [], []
        self._integrate(n_steps, a_start, a_end)

    def _apop(self, a):
        """Returns (da/deta, a''/a) for the background."""
        if self.bg == "lcdm":
            Hloc = E_of_a(a)
            eps = 1.5 * (OM / a ** 3) / (Hloc * Hloc)
        elif self.bg == "ds":
            Hloc, eps = self.H_star, 0.0
        elif self.bg == "flat":
            return 0.0, 0.0
        return a * a * Hloc, (a * Hloc) ** 2 * (2.0 - eps)

    def _integrate(self, n, a_start, a_end):
        k = self.k
        # conformal span: estimate d_eta from da via da/deta, march until a_end
        a = a_start
        eta = 0.0
        t = 0.0
        y = [a, 1.0, 0.0, 0.0, 1.0]  # a, v1, v1', v2, v2'  (unit-Wronskian real basis)

        def deriv(y):
            a = y[0]
            ap, aoa = self._apop(a)
            return [ap,
                    y[2], -(k * k - aoa) * y[1],
                    y[4], -(k * k - aoa) * y[3]]

        # choose step: resolve both k and the background scale a'' / a
        # total conformal span for lcdm from a_start: ~ 3.4; use fixed fine step
        span_guess = 3.6 if self.bg == "lcdm" else 1.0
        h = span_guess / n
        rec_every = max(1, n // 6000)
        i = 0
        while y[0] < a_end and i < 4 * n:
            if i % rec_every == 0:
                self.eta.append(eta); self.a.append(y[0]); self.t.append(t)
                self.v1.append((y[1], y[2])); self.v2.append((y[3], y[4]))
            a_old = y[0]
            k1 = deriv(y)
            k2 = deriv([y[j] + 0.5 * h * k1[j] for j in range(5)])
            k3 = deriv([y[j] + 0.5 * h * k2[j] for j in range(5)])
            k4 = deriv([y[j] + h * k3[j] for j in range(5)])
            y = [y[j] + h / 6.0 * (k1[j] + 2 * k2[j] + 2 * k3[j] + k4[j]) for j in range(5)]
            t += 0.5 * h * (a_old + y[0])  # dt = a deta, trapezoid
            eta += h
            i += 1
        self.eta.append(eta); self.a.append(y[0]); self.t.append(t)
        self.v1.append((y[1], y[2])); self.v2.append((y[3], y[4]))

    def idx_at_a(self, a_target):
        best, bi = 1e99, 0
        for i, a in enumerate(self.a):
            d = abs(a - a_target)
            if d < best:
                best, bi = d, i
        return bi

    def wronskian(self, i):
        return self.v1[i][0] * self.v2[i][1] - self.v2[i][0] * self.v1[i][1]

    def K(self, i, j):
        """h-field commutator kernel between stored indices i, j (universal const dropped)."""
        g = self.v1[i][0] * self.v2[j][0] - self.v2[i][0] * self.v1[j][0]
        return g / (self.a[i] * self.a[j])


def ds_closed_K(k, H, eta1, eta2, a1, a2):
    """dS commutator kernel per h, closed form from the BD pair (basis-independent up to global
    sign fixed by the flat anchor; the instrument fixes orientation once and discloses it)."""
    d = eta1 - eta2
    g = (-(1.0 + 1.0 / (k * k * eta1 * eta2)) * math.sin(k * d)
         + (d / (k * eta1 * eta2)) * math.cos(k * d)) / k
    return g / (a1 * a2)


# =============================================================================================
def s1_controls():
    print("\n=== S1: INTEGRATOR CONTROLS (halt on miss) ===")
    # (i) flat limit: Ghat = sin(k d eta)/k
    r = Run(1.3, bg="flat", n_steps=40000)
    i, j = len(r.eta) - 1, len(r.eta) // 3
    d = r.eta[i] - r.eta[j]
    got, want = r.v1[i][0] * r.v2[j][0] - r.v2[i][0] * r.v1[j][0], -math.sin(1.3 * d) / 1.3
    sgn = -1.0 if got * want > 0 else 1.0  # orientation of the real unit-W basis vs BD pair
    rel = abs(abs(got) - abs(want)) / abs(want)
    check(rel < 1e-6, f"flat anchor: |Ghat| == |sin(k d)/k| (rel {rel:.1e}); basis orientation "
                      f"recorded (real unit-W basis = {'-' if sgn < 0 else '+'}1 x BD convention)")
    # (ii) dS closed form vs numeric dS run
    Hs = 1.0
    r = Run(1.0, bg="ds", H_star=Hs, n_steps=60000, a_start=0.25, a_end=0.995)
    i, j = len(r.eta) - 1, len(r.eta) // 4
    # dS conformal time with a = -1/(H eta):  eta_dS = -1/(H a); numeric run's eta differs by a
    # constant offset only, which the closed form must NOT depend on -> use eta_dS from a.
    e1, e2 = -1.0 / (Hs * r.a[i]), -1.0 / (Hs * r.a[j])
    got = r.K(i, j)
    want = ds_closed_K(1.0, Hs, e1, e2, r.a[i], r.a[j])
    rel = abs(abs(got) - abs(want)) / max(abs(want), 1e-30)
    check(rel < 1e-4, f"dS control: numeric kernel matches the closed BD form (rel {rel:.1e})")
    # (iii) Wronskian constancy + (iv) basis independence on the production background
    r = Run(1.0, bg="lcdm", n_steps=60000)
    wdrift = max(abs(r.wronskian(i) - 1.0) for i in range(0, len(r.eta), 97))
    check(wdrift < 1e-6, f"Wronskian constancy on LCDM (max drift {wdrift:.1e})")
    i, j = len(r.eta) - 1, r.idx_at_a(0.5)
    g0 = r.v1[i][0] * r.v2[j][0] - r.v2[i][0] * r.v1[j][0]
    # SL(2,R) basis change u1 -> 2u1 + 3u2, u2 -> 1u1 + 2u2 (det 1): Ghat invariant
    u1i, u2i = 2 * r.v1[i][0] + 3 * r.v2[i][0], 1 * r.v1[i][0] + 2 * r.v2[i][0]
    u1j, u2j = 2 * r.v1[j][0] + 3 * r.v2[j][0], 1 * r.v1[j][0] + 2 * r.v2[j][0]
    g1 = u1i * u2j - u2i * u1j
    check(abs(g1 - g0) / max(abs(g0), 1e-30) < 1e-9,
          "state-independence: SL(2,R) basis change leaves the commutator kernel invariant "
          f"(rel {abs(g1-g0)/max(abs(g0),1e-30):.1e})")
    # (v) superhorizon freezing: k << aH -> h ~ const at late times
    r = Run(0.02, bg="lcdm", n_steps=40000)
    iA, iB = r.idx_at_a(0.75), len(r.a) - 1
    h_ratio = (r.v1[iB][0] / r.a[iB]) / (r.v1[iA][0] / r.a[iA])
    check(abs(h_ratio - 1.0) < 0.02,
          f"superhorizon freezing: h(k=0.02) constant to {abs(h_ratio-1)*100:.2f}% over a=0.75->1")
    # ctrl: a wrong-sign a''/a mutant must fail the dS control
    class Bad(Run):
        def _apop(self, a):
            da, aoa = Run._apop(self, a)
            return da, -aoa
    rb = Bad(1.0, bg="ds", H_star=1.0, n_steps=30000, a_start=0.25, a_end=0.995)
    i, j = len(rb.eta) - 1, len(rb.eta) // 4
    e1, e2 = -1.0 / rb.a[i], -1.0 / rb.a[j]
    relb = abs(abs(rb.K(i, j)) - abs(ds_closed_K(1.0, 1.0, e1, e2, rb.a[i], rb.a[j]))) / \
        abs(ds_closed_K(1.0, 1.0, e1, e2, rb.a[i], rb.a[j]))
    check(relb > 0.05, f"control: a wrong-sign a''/a mutant misses the dS closed form by "
                       f"{relb*100:.0f}% -- detected", "ctrl")


# =============================================================================================
def s2_adiabaticity():
    print("\n=== S2: ADIABATICITY CONTROL PARAMETER (the premise of every local rule) ===")
    def eps(z):
        a = 1.0 / (1.0 + z)
        return 1.5 * (OM / a ** 3) / (E_of_a(a) ** 2)
    rows = {f"z={z}": eps(z) for z in (0.0, 0.296, 1.0, 3.0)}
    for kk, vv in rows.items():
        print(f"       eps({kk}) = {vv:.4f}")
    check(min(rows.values()) > 0.4,
          f"eps = -Hdot/H^2 NEVER falls below {min(rows.values()):.3f} on the declared background "
          "(z >= 0): every local substitution rule lacks a small parameter in the real universe")
    return rows


# =============================================================================================
def s3_grid(runs):
    print("\n=== S3: T-II EXACT KERNELS vs T-I SUBSTITUTION FAMILY (frozen grid) ===")
    Z_EMIS = [0.296, 1.0, 3.0]
    KS = [0.5, 1.0, 2.0]
    t0 = runs[KS[0]].t[-1]
    grid = []
    for k in KS:
        r = runs[k]
        i_obs = len(r.a) - 1
        for z in Z_EMIS:
            a_e = 1.0 / (1.0 + z)
            j = r.idx_at_a(a_e)
            K_exact = r.K(i_obs, j)
            t_obs, t_e = r.t[i_obs], r.t[j]
            H_emis = E_of_a(a_e)
            # midpoint in cosmic time
            t_mid = 0.5 * (t_obs + t_e)
            jm = min(range(len(r.t)), key=lambda q: abs(r.t[q] - t_mid))
            H_mid = E_of_a(r.a[jm])
            members = {}
            for name, Hs in (("H_obs(=H0)", 1.0), ("H_mid", H_mid), ("H_emis", H_emis)):
                # dS substitute matched at emission: a_m(t) = a_e * exp(Hs (t - t_e));
                # conformal chart eta = -1/(Hs a_m); same comoving k.
                a_o = a_e * math.exp(Hs * (t_obs - t_e))
                e_o, e_e = -1.0 / (Hs * a_o), -1.0 / (Hs * a_e)
                members[name] = ds_closed_K(k, Hs, e_o, e_e, a_o, a_e)
            grid.append({"k": k, "z_emis": z, "K_exact": K_exact, "members": members,
                         "H_emis": H_emis, "H_mid": H_mid, "lag_cosmic": t_obs - t_e})
    norm = max(abs(g["K_exact"]) for g in grid)
    # orientation: fix a single global sign for the closed-form members against the exact kernel
    # (the flat-anchor control recorded the real-basis orientation); choose the sign that
    # minimizes the FAMILY-BEST error, DISCLOSED -- a convention, not a fit (one global binary).
    best_err = {}
    for sgn in (+1.0, -1.0):
        tot = 0.0
        for g in grid:
            tot += min(abs(sgn * m - g["K_exact"]) for m in g["members"].values())
        best_err[sgn] = tot
    SGN = +1.0 if best_err[+1.0] <= best_err[-1.0] else -1.0
    check(True, f"orientation convention: closed-form members carry global sign {SGN:+.0f} "
                "(one binary convention, applied uniformly, disclosed)", "note")
    print(f"\n   {'k':>4} {'z_emis':>7} {'lag/t':>7} | {'K_exact':>11} | "
          f"{'D(H_obs)':>9} {'D(H_mid)':>9} {'D(H_emis)':>10} | family spread")
    table = []
    for g in grid:
        deltas = {n: abs(SGN * v - g["K_exact"]) / norm for n, v in g["members"].items()}
        vals = [SGN * v for v in g["members"].values()]
        spread = max(abs(x - y) for x in vals for y in vals) / norm
        table.append({**{kk: g[kk] for kk in ("k", "z_emis", "K_exact", "lag_cosmic")},
                      "deltas": deltas, "family_spread": spread,
                      "members_signed": {n: SGN * v for n, v in g["members"].items()}})
        print(f"   {g['k']:>4} {g['z_emis']:>7} {g['lag_cosmic']:>7.3f} | {g['K_exact']:>11.4e} | "
              f"{deltas['H_obs(=H0)']:>9.3f} {deltas['H_mid']:>9.3f} {deltas['H_emis']:>10.3f} | "
              f"{spread:.3f}")
    return table, norm


# =============================================================================================
def s4_classify(table):
    print("\n=== S4: CLASSIFICATION (charter section-4 rule, mechanical) ===")
    names = list(table[0]["deltas"].keys())
    worst = {n: max(row["deltas"][n] for row in table) for n in names}
    for n in names:
        print(f"       worst-case Delta({n}) over the grid = {worst[n]:.3f}")
    derived = [n for n in names if worst[n] <= 0.10]
    max_spread = max(row["family_spread"] for row in table)
    print(f"       max family internal spread = {max_spread:.3f}")
    if derived:
        outcome = "O-DERIVED"
        detail = f"member(s) {derived} within 10% over the entire grid"
    elif max_spread > 0.25:
        outcome = "O-NONUNIQUE"
        detail = (f"no member within 10% everywhere (best worst-case "
                  f"{min(worst.values()):.3f}); members mutually differ by up to "
                  f"{max_spread:.3f} of the kernel scale -- 'apply dS locally' is a family, "
                  "not a rule")
    else:
        outcome = "O-MISSING"
        detail = "family internally tight yet wrong against the exact kernel"
    check(True, f"outcome: {outcome} -- {detail}", "note")
    # co-occurrence report (charter: both reported when both hold)
    missing_too = (not derived) and any(min(row["deltas"].values()) > 0.10 for row in table)
    if outcome == "O-NONUNIQUE" and missing_too:
        check(True, "co-occurrence: O-MISSING also holds (at some grid points EVERY member "
                    "misses by > 10% -- the exact kernel is not any local-rate evaluation)", "note")
    return outcome, worst, max_spread, missing_too


# =============================================================================================
def main():
    t_start = time.time()
    print("KERNEL-TRANSPORT INSTRUMENT (charter: KERNEL_TRANSPORT_CHARTER_01.md, frozen at c30f18e)")
    s1_controls()
    if FAIL:
        print("\nHALT: integrator controls failed; NO CLASSIFICATION is issued.")
        sys.exit(1)
    eps_rows = s2_adiabaticity()
    print("\n  [production runs: LCDM background, three k values]")
    runs = {k: Run(k, bg="lcdm", n_steps=120000) for k in (0.5, 1.0, 2.0)}
    t0 = runs[1.0].t[-1]
    check(abs(runs[1.0].a[-1] - 1.0) < 5e-3, f"production run reaches a = {runs[1.0].a[-1]:.4f}")
    table, norm = s3_grid(runs)
    outcome, worst, max_spread, missing_too = s4_classify(table)

    out = {
        "instrument": "kernel_transport_rule",
        "charter": "KERNEL_TRANSPORT_CHARTER_01.md", "charter_commit": "c30f18e",
        "date": "2026-09-25",
        "object": "free TT graviton retarded/commutator kernel per comoving k (state-independent; "
                  "C1-validated primitive)",
        "background": {"Om": OM, "OL": OL},
        "adiabaticity_eps": eps_rows,
        "grid_table": table,
        "grid_norm": norm,
        "worst_case_delta": worst,
        "max_family_spread": max_spread,
        "outcome": outcome,
        "o_missing_cooccurs": missing_too,
        "t2_status": "the exact FRW kernel IS computable from admitted inputs (A4+A7): a transport "
                     "rule exists as recomputation at free level",
        "checks": CHECKS, "failures": FAIL,
        "elapsed_s": round(time.time() - t_start, 2),
        "hard_stop": "verdict recorded pending owner selection; Lambda_R/Matsubara/Pi_0/U5 fenced",
    }
    path = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..",
                                         "KERNEL_TRANSPORT_RESULT.json"))
    with open(path, "wb") as fh:
        fh.write(json.dumps(out, indent=1, sort_keys=True, default=float).encode())
    sha = hashlib.sha256(open(path, "rb").read()).hexdigest()
    print(f"\nartifact written: {path} (sha {sha[:16]}...)")
    n_ok = sum(1 for c in CHECKS if c["ok"])
    print(f"\nKERNEL-TRANSPORT INSTRUMENT: {n_ok}/{len(CHECKS)} checks passed; failures: {len(FAIL)}")
    print(f"OUTCOME: {outcome}")
    print("HARD STOP: verdict pending owner selection of the next instrument.")
    sys.exit(0 if not FAIL else 1)


if __name__ == "__main__":
    main()
