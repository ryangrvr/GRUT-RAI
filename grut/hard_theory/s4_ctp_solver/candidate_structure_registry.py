"""Registry utilities for candidate extraction readiness."""

from dataclasses import asdict, dataclass
from typing import Dict, List


@dataclass(frozen=True)
class CandidateStructureRecord:
    candidate_id: str
    source_topologies: List[str]
    symbolic_form: str
    associated_invariant: str
    scheme_sensitivity: str
    occurrence_count: int
    status: str = "candidate_not_extracted"
    promotes_claims: bool = False


def create_candidate_record(
    candidate_id: str,
    source_topologies: List[str],
    symbolic_form: str,
    associated_invariant: str,
    scheme_sensitivity: str,
    occurrence_count: int,
) -> Dict[str, object]:
    record = CandidateStructureRecord(
        candidate_id=candidate_id,
        source_topologies=source_topologies,
        symbolic_form=symbolic_form,
        associated_invariant=associated_invariant,
        scheme_sensitivity=scheme_sensitivity,
        occurrence_count=occurrence_count,
    )
    return asdict(record)
