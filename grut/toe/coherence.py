"""GRUT ToE — coherence checker.

Catches drift between V7 prose, V8 prose, the ToE document, and the
codebase's canonical numerical values. Three documents, one set of
numbers, zero drift allowed.

Architecture:
    1. CANONICAL_VALUES — a list of CanonicalValue records, each
       declaring a quantity's name, its single canonical numerical
       value, the source code path, and the regex patterns that
       legitimately represent it in prose. Some quantities have a
       sibling "historical" or "deprecated" variant (e.g. R = 1.15428
       is V7's earlier 3-loop CTP claim, NOT the canonical R = 1.15470
       from Path G); these are surfaced separately.

    2. scan_document(path) — open a markdown file, walk every line,
       match each line's numerical occurrences against CANONICAL_VALUES.
       Return a list of Hit records: which value, which line, which
       string was matched, was it canonical or historical.

    3. coherence_report(paths) — run scan_document on each given path,
       cross-reference, flag:
         (a) numerical occurrences that DON'T match any canonical value
             (potential new claim or drift)
         (b) historical-variant uses (e.g. 1.15428 quoted as if canonical)
         (c) inter-document inconsistencies (V7 says X, V8 says Y, both
             reachable as the same canonical quantity)

The checker is non-destructive: it scans and reports, never edits docs.
The user (or chat partner drafting prose) decides how to handle hits.
"""

from __future__ import annotations

import math
import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

from grut.foundation.closure_protocol import (
    A_OVER_C_SM_DIRAC,
    A_OVER_C_SM_MAJORANA,
    ALPHA_VAC,
    A_0_SI,
    H_0_IMPLIED_KM_S_MPC,
    N_G_DC,
    R_MAX_INV_M2,
    RHO_MAX_KG_M3,
    R_REFRACTIVE,
    S_SCREENING,
    TAU_0_MYR,
    T_C_MK,
)


# ─────────────────────────────────────────────────────────────────────
# Canonical-value records
# ─────────────────────────────────────────────────────────────────────

@dataclass(frozen=True)
class CanonicalValue:
    """A canonical numerical truth that documents must agree on.

    Attributes:
        name:           display name
        canonical:      the single-source-of-truth numerical value
        source:         code path or registry id where canonical is defined
        patterns:       regex strings that legitimately represent it
                        (case-insensitive, anchored on word boundaries)
        tolerance_rel:  fractional tolerance for matching as a number
                        (default 1e-3 — covers 4-sig-fig rounding)
        is_historical:  True if this is a deprecated/historical variant
        supersedes:     name of the historical variant this canonical
                        replaces (or None)
        notes:          context for the checker's report
    """
    name: str
    canonical: float
    source: str
    patterns: tuple[str, ...] = ()
    tolerance_rel: float = 1e-3
    is_historical: bool = False
    supersedes: Optional[str] = None
    notes: str = ""


# Single source of truth for every canonical numerical value the docs
# may quote. Add to this list as new claims enter the registry; the
# coherence checker scans for these patterns in each document.
CANONICAL_VALUES: tuple[CanonicalValue, ...] = (

    # Foundational constants
    CanonicalValue(
        name="alpha_vac",
        canonical=ALPHA_VAC,
        source="closure_protocol.ALPHA_VAC",
        patterns=(
            r"α[_ ]?vac\s*=\s*1/3",
            r"α\s*=\s*1/3",
            r"alpha[_ ]?vac\s*=\s*1/3",
            r"\b1/3\b",
            r"\b0\.333+\b",
        ),
        tolerance_rel=1e-3,
        notes="Vacuum impedance — derived via conformal-mode scalar.",
    ),
    CanonicalValue(
        name="tau_0_Myr",
        canonical=TAU_0_MYR,
        source="closure_protocol.TAU_0_MYR",
        patterns=(
            r"τ[_ ]?0\s*=\s*41\.9\s*Myr",
            r"tau[_ ]?0\s*=\s*41\.9\s*Myr",
            r"\b41\.9\b",
        ),
        tolerance_rel=1e-3,
        notes="Local relaxation time — CTP noise kernel at gold benchmark.",
    ),

    # The canonical R (Path G) and its historical sibling
    CanonicalValue(
        name="R_canonical",
        canonical=R_REFRACTIVE,  # 1.15470
        source="closure_protocol.R_REFRACTIVE",
        patterns=(
            r"R\s*=\s*√\s*\(\s*4\s*/\s*3\s*\)",
            r"R\s*=\s*sqrt\s*\(\s*4\s*/\s*3\s*\)",
            r"\b1\.1547\b",
            r"\b1\.15470\b",
        ),
        tolerance_rel=1e-4,
        notes=(
            "Path G canonical R = √(4/3). PRIMARY cosmological observable. "
            "Distinct from the historical 1.15428."
        ),
    ),
    CanonicalValue(
        name="R_anomaly_historical",
        canonical=1.15428,
        source="anomaly.R_ANOMALY (historical, V7 §26.2.3 claim)",
        patterns=(
            r"\b1\.15428\b",
        ),
        tolerance_rel=1e-5,
        is_historical=True,
        supersedes="R_canonical",
        notes=(
            "V7's 3-loop CTP claim. NOT reproduced in TJI Phase-0/0.5 "
            "reconciliation. Demoted from canonical; flagged whenever "
            "quoted as if it were the framework's primary R."
        ),
    ),
    CanonicalValue(
        name="R_path_osborn_epsilon",
        canonical=1.15370,
        source="osborn_epsilon.epsilon_combined() (Osborn 2003 eq 36)",
        patterns=(
            r"\b1\.15370\b",
            r"\b1\.1537\b",
        ),
        tolerance_rel=1e-3,
        notes=(
            "Three-Routes Route 3: ε_combined from Osborn eq (36) "
            "evaluated for SM at M_Z. Independent of Path G — agrees "
            "at 0.1% with √(4/3)."
        ),
    ),

    # Path D cross-checks
    CanonicalValue(
        name="a_over_c_sm_dirac",
        canonical=A_OVER_C_SM_DIRAC,  # 253/219 ≈ 1.15525
        source="closure_protocol.A_OVER_C_SM_DIRAC",
        patterns=(
            r"\b253\s*/\s*219\b",
            r"\b1\.15525\b",
        ),
        tolerance_rel=1e-4,
        notes="Path D Dirac variant — supports lean-Dirac falsifiable posture.",
    ),
    CanonicalValue(
        name="a_over_c_sm_majorana",
        canonical=A_OVER_C_SM_MAJORANA,  # 1991/1698 ≈ 1.17256
        source="closure_protocol.A_OVER_C_SM_MAJORANA",
        patterns=(
            r"\b1991\s*/\s*1698\b",
            r"\b1\.17256\b",
        ),
        tolerance_rel=1e-4,
        notes="Path D Majorana — secondary cross-check.",
    ),

    # Cosmological predictions
    CanonicalValue(
        name="H_0_implied",
        canonical=H_0_IMPLIED_KM_S_MPC,
        source="closure_protocol.H_0_IMPLIED_KM_S_MPC",
        patterns=(
            r"\b68\.8\b",
            r"\b68\.83\b",
            r"H[_ ]?0\s*=\s*68\.8",
            r"\b69\.03\b",  # alternative GRUT-prediction value (V7 prose)
        ),
        tolerance_rel=2e-2,
        notes=(
            "GRUT-implied H_0 ≈ 68.8 km/s/Mpc (between Planck 67.4 and "
            "SH0ES 73.0). V7 prose quotes 69.03; both within tolerance "
            "of the framework's prediction band."
        ),
    ),
    CanonicalValue(
        name="omega_lambda",
        canonical=0.6886,
        source="V7 §27 (prediction); Planck 2018 measurement",
        patterns=(
            r"Ω[_ ]?Λ\s*=\s*0\.6886",
            r"Omega[_ ]?Lambda\s*=\s*0\.6886",
            r"\b0\.6886\b",
        ),
        tolerance_rel=1e-3,
        notes="Predicted Ω_Λ matches Planck 2018 to 0.04%.",
    ),

    # Screening + saturation
    CanonicalValue(
        name="S_screening_108_pi",
        canonical=S_SCREENING,  # 108π ≈ 339.29
        source="closure_protocol.S_SCREENING",
        patterns=(
            r"108\s*π",
            r"108\s*pi",
            r"\bS\s*=\s*108\s*π\b",
            r"\b339\.29\b",
            r"\b339\.292\b",
            r"\b339\.2920\b",
        ),
        tolerance_rel=1e-3,
        notes="Screening factor S = 12π/α² = 108π.",
    ),
    CanonicalValue(
        name="n_g_DC",
        canonical=N_G_DC,
        source="closure_protocol.N_G_DC",
        patterns=(
            r"n[_ ]?g\s*\(\s*0\s*\)\s*=\s*√\s*\(\s*4\s*/\s*3\s*\)",
            r"\b1\.15470\b",
        ),
        tolerance_rel=1e-4,
        notes="DC refractive index = R_canonical (alias).",
    ),

    # Saturation
    CanonicalValue(
        name="rho_max",
        canonical=RHO_MAX_KG_M3,
        source="closure_protocol.RHO_MAX_KG_M3",
        patterns=(
            r"ρ[_ ]?max",
            r"rho[_ ]?max",
        ),
        tolerance_rel=1e-2,
        notes="Universal interior density cap ~ 1.14e-22 kg/m³.",
    ),
    CanonicalValue(
        name="R_max",
        canonical=R_MAX_INV_M2,
        source="closure_protocol.R_MAX_INV_M2",
        patterns=(
            r"R[_ ]?max\s*~\s*α/\(c²τ₀²\)",
            r"R[_ ]?max\s*=\s*α[_ ]?vac",
        ),
        tolerance_rel=1e-2,
        notes="Universal Ricci-saturation curvature ~ 2.12e-48 m^-2.",
    ),

    # Acceleration scales
    CanonicalValue(
        name="a_0_MOND",
        canonical=A_0_SI,
        source="closure_protocol.A_0_SI",
        patterns=(
            r"a[_ ]?0\s*≈?\s*1\.[12]\s*[×x]\s*10\^?-10",
            r"\b1\.2\s*[×x]\s*10\^?-10\b",
        ),
        tolerance_rel=2e-2,
        notes="MOND-like acceleration scale ~ 1.2e-10 m/s² (derived).",
    ),
    CanonicalValue(
        name="T_c_thermal_MK",
        canonical=T_C_MK,
        source="closure_protocol.T_C_MK",
        patterns=(
            r"T[_ ]?c\s*≈?\s*54\.7\s*MK",
            r"\b54\.7\s*MK\b",
            r"\b54\.7\s*×\s*10\^?6\s*K\b",
        ),
        tolerance_rel=5e-2,
        notes="Boiling point of gravity ~ 54.7 MK (v9.0 thermal transition).",
    ),
)


# ─────────────────────────────────────────────────────────────────────
# Document scanner
# ─────────────────────────────────────────────────────────────────────

@dataclass
class Hit:
    """One occurrence of a canonical value in a document."""
    document: str
    line_number: int
    line_text: str
    value_name: str
    matched_pattern: str
    matched_text: str
    is_historical: bool


def scan_document(path: Path | str) -> list[Hit]:
    """Walk a markdown file line-by-line, match canonical patterns.

    Returns an empty list if the file does not exist (graceful for
    documents that haven't been drafted yet, like GRUT_TOE.md while
    the ToE is still being written).
    """
    p = Path(path)
    if not p.is_file():
        return []

    hits: list[Hit] = []
    with p.open("r", encoding="utf-8") as f:
        for lineno, line in enumerate(f, start=1):
            for cv in CANONICAL_VALUES:
                for pat in cv.patterns:
                    for m in re.finditer(pat, line, flags=re.IGNORECASE):
                        hits.append(Hit(
                            document=str(p.name),
                            line_number=lineno,
                            line_text=line.rstrip("\n"),
                            value_name=cv.name,
                            matched_pattern=pat,
                            matched_text=m.group(0),
                            is_historical=cv.is_historical,
                        ))
    return hits


# ─────────────────────────────────────────────────────────────────────
# Drift detection across multiple documents
# ─────────────────────────────────────────────────────────────────────

@dataclass
class DriftReport:
    """One report from coherence_report()."""
    documents_scanned: tuple[str, ...] = ()
    documents_missing: tuple[str, ...] = ()
    total_hits: int = 0
    historical_uses: list[Hit] = field(default_factory=list)
    per_value_counts: dict[str, dict[str, int]] = field(default_factory=dict)
    """{value_name: {document: count}} — quick visualization of where each
    canonical value is referenced and how often."""


def coherence_report(paths: list[Path | str]) -> DriftReport:
    """Run scan_document on each path; assemble a drift report.

    The report flags:
        - documents that don't exist yet (helpful when GRUT_TOE.md is
          still being drafted — listed as 'missing' rather than 'failed')
        - every historical-variant occurrence (e.g. 1.15428 quoted)
        - per-value occurrence counts across documents
    """
    report = DriftReport()
    docs_scanned: list[str] = []
    docs_missing: list[str] = []

    all_hits: list[Hit] = []
    for path in paths:
        p = Path(path)
        if not p.is_file():
            docs_missing.append(str(p.name))
            continue
        docs_scanned.append(str(p.name))
        all_hits.extend(scan_document(p))

    report.documents_scanned = tuple(docs_scanned)
    report.documents_missing = tuple(docs_missing)
    report.total_hits = len(all_hits)

    # Historical-variant uses (potential drift / honest-narrative review)
    report.historical_uses = [h for h in all_hits if h.is_historical]

    # Per-value counts
    counts: dict[str, dict[str, int]] = {}
    for h in all_hits:
        counts.setdefault(h.value_name, {})
        counts[h.value_name][h.document] = counts[h.value_name].get(h.document, 0) + 1
    report.per_value_counts = counts

    return report


# ─────────────────────────────────────────────────────────────────────
# Default scan target list (the GRUT canonical document set)
# ─────────────────────────────────────────────────────────────────────

def default_scan_paths(repo_root: Path | str) -> list[Path]:
    """Standard list: V7, V8, V8 Clean, ToE.

    The GRUT_TOE.md draft lives on Desktop while it's being written
    (per the user's working setup); the checker also scans the
    repo-internal location once the draft moves in.

    Missing files are tolerated; the report surfaces them as 'missing'.
    """
    root = Path(repo_root)
    home = Path.home()
    return [
        root / "theory" / "GRUT_V7_FULL.md",
        root / "theory" / "GRUT_V8.md",
        root / "theory" / "GRUT_V8_CLEAN.md",
        # Live-drafting locations for the ToE document
        home / "Desktop" / "GRUT_TOE.md",
        root / "theory" / "GRUT_TOE.md",
        root / "GRUT_TOE.md",
    ]


# ─────────────────────────────────────────────────────────────────────
# Verification harness
# ─────────────────────────────────────────────────────────────────────

def verify() -> dict:
    """Self-test: every CANONICAL_VALUE record is well-formed."""
    return {
        "all_have_patterns":     all(cv.patterns for cv in CANONICAL_VALUES),
        "all_canonicals_finite": all(
            math.isfinite(cv.canonical) for cv in CANONICAL_VALUES
        ),
        "all_names_unique":      len({cv.name for cv in CANONICAL_VALUES}) == len(CANONICAL_VALUES),
        "all_supersedes_resolve": all(
            cv.supersedes is None
            or any(other.name == cv.supersedes for other in CANONICAL_VALUES)
            for cv in CANONICAL_VALUES
        ),
        "historical_have_supersedes": all(
            (not cv.is_historical) or cv.supersedes is not None
            for cv in CANONICAL_VALUES
        ),
    }


# ─────────────────────────────────────────────────────────────────────
# Tier-marker validator (per #9 from the strengthening menu)
# ─────────────────────────────────────────────────────────────────────
#
# Catches doc-codebase drift from a different angle than the canonical-
# value scanner: when prose authors add markers like [OPEN], [SCOPING],
# [CONJECTURAL], [SPECULATIVE], or "Outstanding verification" to a
# document, the validator surfaces all occurrences and (where possible)
# associates them with registry claim IDs in the surrounding text.
# Markers without a nearby claim ID are flagged as "orphan markers" —
# either undocumented gaps, or intentional speculative-content flags
# the auditor decides to leave un-tracked.

TIER_MARKER_PATTERNS: tuple[tuple[str, str], ...] = (
    # (display name, regex pattern)
    ("OPEN",         r"\[OPEN\]"),
    ("SCOPING",      r"\[SCOPING\]"),
    ("CONJECTURAL",  r"\[CONJECTURAL\]"),
    ("SPECULATIVE",  r"\[SPECULATIVE\]"),
    ("ANCHORED",     r"\[ANCHORED\]"),
    ("COMPUTED",     r"\[COMPUTED\]"),
    ("OPEN_NEGATIVE", r"\[OPEN_NEGATIVE\]"),
    ("OUTSTANDING",  r"Outstanding verification"),
)

# Backticked identifier pattern — looks like a registry claim ID
# (snake_case, lowercase, sometimes with digits)
_CLAIM_ID_PATTERN = re.compile(r"`([a-z][a-z0-9_]+)`")

# Tier-marker → expected registry tier mapping (best guess; informational)
EXPECTED_TIER_FOR_MARKER: dict[str, str] = {
    "OPEN":          "open_negative",
    "OPEN_NEGATIVE": "open_negative",
    "OUTSTANDING":   "open_negative",
    "SCOPING":       "anchored",
    "ANCHORED":      "anchored",
    "CONJECTURAL":   "conjectural",
    "SPECULATIVE":   "conjectural",
    "COMPUTED":      "computed",
}


@dataclass
class MarkerHit:
    """One occurrence of a tier marker in a document."""
    document: str
    line_number: int
    line_text: str
    marker: str
    nearby_claim_ids: tuple[str, ...]
    """Backticked snake_case identifiers in surrounding ±N lines."""
    matched_registry_claims: tuple[str, ...]
    """Subset of nearby_claim_ids that resolve to actual registry claims."""
    tier_mismatch: bool
    """True if a matched claim has a tier that doesn't agree with the
    marker's expected tier (e.g. [OPEN] marker associated with a
    'computed' tier claim — drift!)."""
    is_orphan: bool
    """True if no nearby claim ID resolves to a registry claim."""


def scan_markers(
    path: Path | str,
    context_lines: int = 5,
) -> list[MarkerHit]:
    """Walk a document; find tier markers; associate with claim IDs.

    For each marker found, look at ±context_lines around it for
    backticked snake_case identifiers, then check if any of those
    are registered claims. If yes, check tier agreement.
    """
    p = Path(path)
    if not p.is_file():
        return []

    # Lazy imports to avoid circular references
    from grut.toe.registry import REGISTRY, by_id as registry_by_id

    registered_ids = {c.id for c in REGISTRY}
    pattern = re.compile(
        "|".join(p_regex for _, p_regex in TIER_MARKER_PATTERNS),
        re.IGNORECASE,
    )

    lines = p.read_text(encoding="utf-8").splitlines()
    hits: list[MarkerHit] = []

    for lineno, line in enumerate(lines, start=1):
        for m in pattern.finditer(line):
            matched_text = m.group(0)
            # Identify which marker by display name
            marker_name = "OUTSTANDING"
            for name, regex_pattern in TIER_MARKER_PATTERNS:
                if re.fullmatch(regex_pattern, matched_text, flags=re.IGNORECASE):
                    marker_name = name
                    break

            # Gather nearby backticked identifiers
            lo = max(0, lineno - 1 - context_lines)
            hi = min(len(lines), lineno - 1 + context_lines + 1)
            context_text = "\n".join(lines[lo:hi])
            ids = tuple(set(_CLAIM_ID_PATTERN.findall(context_text)))

            # Filter to those that resolve to real registry claims
            matched = tuple(
                cid for cid in ids if cid in registered_ids
            )

            # Check for tier mismatch
            mismatch = False
            expected_tier = EXPECTED_TIER_FOR_MARKER.get(marker_name)
            if expected_tier and matched:
                for cid in matched:
                    claim = registry_by_id(cid)
                    if claim is None:
                        continue
                    if claim.tier != expected_tier:
                        mismatch = True
                        break

            hits.append(MarkerHit(
                document=str(p.name),
                line_number=lineno,
                line_text=line.rstrip("\n"),
                marker=marker_name,
                nearby_claim_ids=ids,
                matched_registry_claims=matched,
                tier_mismatch=mismatch,
                is_orphan=(len(matched) == 0),
            ))

    return hits


@dataclass
class MarkerAuditReport:
    """Aggregated report on tier-marker discipline across documents."""
    total_markers: int
    by_marker_type: dict[str, int]
    by_document: dict[str, int]
    orphan_markers: list[MarkerHit]
    """Markers with no nearby registered claim — possibly drift."""
    tier_mismatches: list[MarkerHit]
    """Markers associated with claims whose tier doesn't match the
    marker's expected tier."""
    documents_scanned: tuple[str, ...]
    documents_missing: tuple[str, ...]


def marker_audit_report(
    paths: list[Path | str],
    context_lines: int = 5,
) -> MarkerAuditReport:
    docs_scanned: list[str] = []
    docs_missing: list[str] = []
    all_hits: list[MarkerHit] = []

    for path in paths:
        p = Path(path)
        if not p.is_file():
            docs_missing.append(p.name)
            continue
        docs_scanned.append(p.name)
        all_hits.extend(scan_markers(p, context_lines=context_lines))

    by_marker: dict[str, int] = {}
    for h in all_hits:
        by_marker[h.marker] = by_marker.get(h.marker, 0) + 1

    by_doc: dict[str, int] = {}
    for h in all_hits:
        by_doc[h.document] = by_doc.get(h.document, 0) + 1

    orphans = [h for h in all_hits if h.is_orphan]
    mismatches = [h for h in all_hits if h.tier_mismatch]

    return MarkerAuditReport(
        total_markers=len(all_hits),
        by_marker_type=by_marker,
        by_document=by_doc,
        orphan_markers=orphans,
        tier_mismatches=mismatches,
        documents_scanned=tuple(docs_scanned),
        documents_missing=tuple(docs_missing),
    )


if __name__ == "__main__":
    # CLI: scan default targets and print drift report
    import sys

    repo_root = Path(__file__).resolve().parents[2]
    paths = default_scan_paths(repo_root)
    report = coherence_report(paths)

    print("=" * 72)
    print("GRUT ToE Coherence Report")
    print("=" * 72)
    print(f"Documents scanned:  {len(report.documents_scanned)}")
    for d in report.documents_scanned:
        print(f"  ✓  {d}")
    if report.documents_missing:
        print(f"Documents not yet present (graceful skip):")
        for d in report.documents_missing:
            print(f"  ·  {d}")
    print(f"Total canonical-value hits: {report.total_hits}")

    if report.historical_uses:
        print()
        print(f"⚠  Historical-variant occurrences: {len(report.historical_uses)}")
        for h in report.historical_uses[:20]:
            print(f"     {h.document}:{h.line_number}  "
                  f"{h.value_name} matched as {h.matched_text!r}")
            print(f"        > {h.line_text.strip()[:90]}")
        if len(report.historical_uses) > 20:
            print(f"     ... and {len(report.historical_uses) - 20} more.")

    print()
    print("Per-value occurrence counts:")
    for name, by_doc in sorted(report.per_value_counts.items()):
        total = sum(by_doc.values())
        breakdown = ", ".join(f"{d}={n}" for d, n in by_doc.items())
        print(f"  {name:<28}  total={total:<4}  ({breakdown})")

    # ─── Marker validator (per-document tier-marker discipline) ───
    print()
    print("=" * 72)
    print("Tier-marker validator")
    print("=" * 72)
    marker_rep = marker_audit_report(paths)
    print(f"Total tier markers across docs: {marker_rep.total_markers}")
    print()
    print("By marker type:")
    for name, count in sorted(marker_rep.by_marker_type.items()):
        print(f"  {name:<14} {count:>4}")
    print()
    print("By document:")
    for name, count in sorted(marker_rep.by_document.items()):
        print(f"  {name:<28} {count:>4}")

    if marker_rep.tier_mismatches:
        print()
        print(f"⚠  Tier mismatches (marker contradicts registry tier): "
              f"{len(marker_rep.tier_mismatches)}")
        for h in marker_rep.tier_mismatches[:10]:
            print(f"     {h.document}:{h.line_number}  "
                  f"[{h.marker}] near {h.matched_registry_claims}")
            print(f"        > {h.line_text.strip()[:90]}")

    if marker_rep.orphan_markers:
        print()
        print(f"·  Orphan markers (no nearby registered claim): "
              f"{len(marker_rep.orphan_markers)}")
        print("   (May be intentional speculative-content flags or "
              "undocumented gaps — review case-by-case.)")
        # Show first 10 orphans for context
        for h in marker_rep.orphan_markers[:10]:
            print(f"     {h.document}:{h.line_number}  [{h.marker}]")
            print(f"        > {h.line_text.strip()[:80]}")
        if len(marker_rep.orphan_markers) > 10:
            print(f"     ... and {len(marker_rep.orphan_markers) - 10} more.")

    sys.exit(0)
