"""Divergence structure records for Stage 3D audits."""

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class DivergenceRecord:
    loop_order: int
    pole_structure: str
    associated_counterterms: List[str]
    regulator: str
    scheme: str
    subtraction_status: str
    status: str


def create_divergence_record(loop_order: int, regulator: str, scheme: str) -> DivergenceRecord:
    return DivergenceRecord(
        loop_order=loop_order,
        pole_structure="unknown",
        associated_counterterms=[],
        regulator=regulator,
        scheme=scheme,
        subtraction_status="not_subtracted",
        status="divergence_tracked_not_renormalized",
    )


def associate_counterterms(record: DivergenceRecord, counterterm_ids: List[str]) -> DivergenceRecord:
    return DivergenceRecord(
        loop_order=record.loop_order,
        pole_structure=record.pole_structure,
        associated_counterterms=list(counterterm_ids),
        regulator=record.regulator,
        scheme=record.scheme,
        subtraction_status=record.subtraction_status,
        status=record.status,
    )
