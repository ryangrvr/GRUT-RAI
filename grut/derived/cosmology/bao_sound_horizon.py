"""
BAO sound horizon — GRUT vs Planck, and self-consistent Ly-α comparison.

The BAO peak position measures the sound horizon r_d = r_s(z_drag) set at
the baryon drag epoch.  Any published BAO H(z) value has the form:

    D_H(z)/r_d  =  c / (H(z) × r_d)        (line-of-sight)

where r_d in the denominator is the r_d of the *assumed cosmology* used to
convert the peak angle to a distance.  Comparing GRUT's H(z) to a Planck-
calibrated H_obs therefore introduces a ~0.76% systematic from the r_d
mismatch (GRUT r_d is 0.76% larger than Planck's).

This module removes that systematic by comparing the dimensionless ratio
D_H(z)/r_d directly:

    GRUT predicted:   D_H^GRUT(z) / r_d^GRUT
    Delubac observed: D_H(z=2.34) / r_d = 9.18 ± 0.28  [arXiv:1409.4232]

The ratio D_H/r_d is the cosmology-independent BAO observable; the
self-consistent residual is −1.95σ (GRUT's expansion is ~2% too fast at
z = 2.34 for the Ly-α BAO constraint).

Key results:
    r_d^GRUT   = 148.209 Mpc  (z_drag = 1059.65)
    r_d^Planck = 147.091 Mpc  (z_drag = 1059.95)
    r_d ratio  = GRUT/Planck = 1.00760  (+0.76%)
    D_H/r_d predicted = 8.635;  observed = 9.18 ± 0.28;  residual = −1.95σ

References:
    Delubac+2015: A&A 574, A59  (Ly-α auto-correlation at z=2.34)
    Planck 2018: arXiv:1807.06209 Table 2 (TT+TE+EE+lowE)
"""

from __future__ import annotations

import math

# ── Constants ─────────────────────────────────────────────────────────────────

GRUT_H0     = 69.029   # km/s/Mpc
GRUT_OMBH2  = 0.02237
GRUT_OMCH2  = 0.11582  # Ω_c h² = Ω_m h² − Ω_b h² at GRUT background

PLANCK_H0    = 67.36   # km/s/Mpc  (Planck 2018 TT+TE+EE+lowE)
PLANCK_OMBH2 = 0.02237
PLANCK_OMCH2 = 0.1200

C_KM_S = 299792.458    # speed of light (km/s)

# Delubac+2015 (A&A 574, A59) Ly-α auto-correlation at z=2.34
# Raw BAO observable — dimensionless, cosmology-independent:
#   D_H(z=2.34) / r_d = 9.18 ± 0.28
DELUBAC_Z           = 2.34
DELUBAC_DH_OVER_RD  = 9.18
DELUBAC_SIGMA       = 0.28
DELUBAC_REF         = "Delubac+2015"

# ── Module-level caches ───────────────────────────────────────────────────────

_SH_GRUT   = None   # cached result of grut_sound_horizon()
_SH_PLANCK = None   # cached result of planck_sound_horizon()


# ── CAMB background runner ────────────────────────────────────────────────────

def _run_camb_background(H0: float, ombh2: float, omch2: float) -> dict:
    """Compute sound horizon via CAMB background-only calculation.

    Uses camb.get_background() — ~0.03 s per call, no perturbations needed.
    Returns dict with rdrag, rstar, zdrag, zstar (all in Mpc or dimensionless).
    """
    import camb
    pars = camb.CAMBparams()
    pars.set_cosmology(
        H0=H0, ombh2=ombh2, omch2=omch2,
        mnu=0.06, nnu=3.046, TCMB=2.7255,
    )
    pars.WantCls      = False
    pars.WantTransfer = False
    results = camb.get_background(pars)
    d = results.get_derived_params()
    return {
        "rdrag":  d["rdrag"],   # r_s at baryon drag epoch  (Mpc)
        "zdrag":  d["zdrag"],   # z at drag epoch
        "rstar":  d["rstar"],   # r_s at recombination      (Mpc)
        "zstar":  d["zstar"],   # z at recombination
        "H0":     H0,
        "ombh2":  ombh2,
        "omch2":  omch2,
    }


# ── Public API ────────────────────────────────────────────────────────────────

def grut_sound_horizon() -> dict:
    """Return CAMB-computed sound horizon for GRUT first-principles cosmology.

    Cached after first call.
    Keys: rdrag (Mpc), zdrag, rstar (Mpc), zstar, H0, ombh2, omch2.
    """
    global _SH_GRUT
    if _SH_GRUT is None:
        _SH_GRUT = _run_camb_background(GRUT_H0, GRUT_OMBH2, GRUT_OMCH2)
    return _SH_GRUT


def planck_sound_horizon() -> dict:
    """Return CAMB-computed sound horizon for Planck 2018 cosmology.

    Cached after first call.
    Keys: rdrag (Mpc), zdrag, rstar (Mpc), zstar, H0, ombh2, omch2.
    """
    global _SH_PLANCK
    if _SH_PLANCK is None:
        _SH_PLANCK = _run_camb_background(PLANCK_H0, PLANCK_OMBH2, PLANCK_OMCH2)
    return _SH_PLANCK


def bao_dh_over_rd_comparison() -> dict:
    """Self-consistent BAO comparison at z=2.34 (Delubac+2015 Ly-α).

    Computes GRUT's predicted D_H(z)/r_d^GRUT and compares it directly to
    the dimensionless BAO observable D_H/r_d = 9.18 ± 0.28.

    Returns
    -------
    dict with keys:
        z, H_grut_km_s_Mpc, DH_grut_Mpc, rd_grut_Mpc, rd_planck_Mpc,
        rd_ratio_grut_over_planck, DH_over_rd_grut, DH_over_rd_observed,
        sigma, residual_sigma, reference, note.
    """
    from grut.derived.cosmology.hz_residuals import grut_cosmology, E_z

    cosmo    = grut_cosmology()
    sh_grut  = grut_sound_horizon()
    sh_pl    = planck_sound_horizon()

    H0 = cosmo["H0"]
    Om = cosmo["omega_m"]
    OL = cosmo["omega_lambda"]
    z  = DELUBAC_Z

    Ez      = E_z(z, Om, OL)
    H_grut  = H0 * Ez
    DH_grut = C_KM_S / H_grut
    rd_grut = sh_grut["rdrag"]
    rd_pl   = sh_pl["rdrag"]

    dh_rd_pred = DH_grut / rd_grut
    resid      = (dh_rd_pred - DELUBAC_DH_OVER_RD) / DELUBAC_SIGMA

    return {
        "z":                         z,
        "H_grut_km_s_Mpc":           H_grut,
        "DH_grut_Mpc":               DH_grut,
        "rd_grut_Mpc":               rd_grut,
        "rd_planck_Mpc":             rd_pl,
        "rd_ratio_grut_over_planck": rd_grut / rd_pl,
        "DH_over_rd_grut":           dh_rd_pred,
        "DH_over_rd_observed":       DELUBAC_DH_OVER_RD,
        "sigma":                     DELUBAC_SIGMA,
        "residual_sigma":            resid,
        "reference":                 DELUBAC_REF,
        "note": (
            "Self-consistent: GRUT prediction uses GRUT r_d^CAMB. "
            "Observed D_H/r_d from Delubac+2015, calibration-free. "
            f"Planck-calibrated H(z) comparison gives +1.75σ; "
            "self-consistent D_H/r_d comparison gives "
            f"{resid:+.2f}σ. Both indicate GRUT H(z=2.34) is ~2% too high."
        ),
    }
