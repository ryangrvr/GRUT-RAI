"""GRUT Theory of Everything — synthesis layer.

This package is the predictive engine for the GRUT ToE document. It
holds the structured claim registry that anchors every physical
assertion in the framework to code, tests, derivation logs, and
honest-negative records.

Modules:
    registry    — the canonical Claim dataclass and REGISTRY tuple
    (more to come: dependencies, coherence, ledger, director)

Usage:
    from grut.toe.registry import REGISTRY, Claim, by_chapter, by_tier
"""

from grut.toe.registry import (
    Claim,
    REGISTRY,
    Tier,
    by_chapter,
    by_id,
    by_tier,
    chapter_summary,
)
from grut.toe.dependencies import (
    direct_dependencies,
    direct_dependents,
    downstream_chain,
    fan_in,
    fan_out,
    fan_out_ranking,
    graph_summary,
    high_value_open_negatives,
    leaves,
    roots,
    topological_order,
    transitive_dependencies,
    transitive_dependents,
    upstream_chain,
)
from grut.toe.ledger import (
    LedgerEntry,
    OPEN_NEGATIVES,
    affects_summary,
    closure_dependency_chain,
    coverage_report as ledger_coverage_report,
)
from grut.toe.render import (
    render_all_chapter_footers,
    render_chapter_12_open_questions,
    render_chapter_claims_footer,
    render_chapter_full_footer,
    render_chapter_open_negatives,
    render_open_negative_entry,
    render_summary_table,
)
from grut.toe.render_appendices import (
    render_all_appendices,
    render_appendix_d_derivation_index,
    render_appendix_e_claim_registry,
    render_appendix_f_dependency_graph,
)
from grut.toe.coherence import (
    MarkerAuditReport,
    MarkerHit,
    TIER_MARKER_PATTERNS,
    marker_audit_report,
    scan_markers,
)
from grut.toe.dashboard import (
    PREDICTIONS,
    Prediction,
    PredictionStatus,
    STATUS_GLYPH,
    all_categories as dashboard_categories,
    by_category as predictions_by_category,
    by_id as prediction_by_id,
    by_status as predictions_by_status,
    render_full_dashboard,
    render_predictions_table,
    status_summary,
)

__all__ = [
    "Claim",
    "REGISTRY",
    "Tier",
    "by_chapter",
    "by_id",
    "by_tier",
    "chapter_summary",
    "direct_dependencies",
    "direct_dependents",
    "downstream_chain",
    "fan_in",
    "fan_out",
    "fan_out_ranking",
    "graph_summary",
    "high_value_open_negatives",
    "leaves",
    "roots",
    "topological_order",
    "transitive_dependencies",
    "transitive_dependents",
    "upstream_chain",
]
