#!/usr/bin/env python3
"""Tests for the RRP corpus loading/validation path.

The canonical corpus-loading entry point in this repository is
rrp/tools/corpus_validate.py::validate_file, which loads a corpus domain
JSON file from disk and validates it against CORPUS_SCHEMA v0.
Note: there is no rrp/simulator.py or rrp/corpus.py module in the repo —
rrp/corpus/ is a data directory. That absence is recorded, not papered over.
"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
TOOLS = os.path.join(REPO, "rrp", "tools")
sys.path.insert(0, TOOLS)

from corpus_validate import validate_file, SCHEMA_VERSION  # noqa: E402

DOMAINS = os.path.join(REPO, "rrp", "corpus", "domains")


def _entry(claim="test claim", provenance="OBSERVED", verification="VERIFIED",
           source="test source", **extra):
    e = {"claim": claim, "provenance": provenance,
         "verification": verification, "source": source}
    e.update(extra)
    return e


def _record(entries=None, schema=SCHEMA_VERSION):
    rec = {
        "domain": "test_domain", "grade": "TEST", "schema": schema,
        "date": "2026-01-01", "notes": "",
    }
    for f in ("phenomena", "formalism", "primitives", "derived_objects",
              "empirical_inputs", "constants", "symmetries", "limits",
              "known_connections", "known_disconnects", "open_problems",
              "observables", "alternative_formulations", "domain_of_validity"):
        rec[f] = list(entries or [])
    return rec


def test_valid_fixture_record_passes(tmp_path):
    p = tmp_path / "test_domain.json"
    p.write_text(json.dumps(_record([_entry()])))
    errors, warns, counts, vcounts = validate_file(str(p))
    assert errors == []
    assert counts["OBSERVED"] == 1
    assert vcounts["VERIFIED"] == 1


def test_missing_top_level_field_is_error(tmp_path):
    rec = _record([_entry()])
    del rec["domain"]
    p = tmp_path / "bad.json"
    p.write_text(json.dumps(rec))
    errors, _, _, _ = validate_file(str(p))
    assert any("missing top-level field: domain" in e for e in errors)


def test_wrong_schema_version_is_error(tmp_path):
    p = tmp_path / "bad.json"
    p.write_text(json.dumps(_record(schema="CORPUS_SCHEMA v999")))
    errors, _, _, _ = validate_file(str(p))
    assert any("schema version mismatch" in e for e in errors)


def test_illegal_provenance_and_verification_are_errors(tmp_path):
    p = tmp_path / "bad.json"
    p.write_text(json.dumps(_record([
        _entry(provenance="MAGIC", verification="TRUSTED")])))
    errors, _, _, _ = validate_file(str(p))
    assert any("illegal provenance" in e for e in errors)
    assert any("illegal verification" in e for e in errors)


def test_missing_entry_required_keys(tmp_path):
    p = tmp_path / "bad.json"
    p.write_text(json.dumps(_record([{"claim": "no provenance"}])))
    errors, _, _, _ = validate_file(str(p))
    assert any("missing key provenance" in e for e in errors)


def test_unparseable_json_reports_parse_failure(tmp_path):
    p = tmp_path / "bad.json"
    p.write_text("{not json")
    errors, warns, counts, vcounts = validate_file(str(p))
    assert len(errors) == 1 and "JSON parse failure" in errors[0]
    assert warns == [] and all(v == 0 for v in counts.values())


def test_requirement_language_warns(tmp_path):
    p = tmp_path / "warn.json"
    p.write_text(json.dumps(_record([
        _entry(claim="any successful theory must explain X")])))
    errors, warns, _, _ = validate_file(str(p))
    assert errors == [] and any("requirement-language" in w for w in warns)


def test_illegal_edge_class(tmp_path):
    p = tmp_path / "bad.json"
    p.write_text(json.dumps(_record([_entry(edge_class="WISHFUL")])))
    errors, _, _, _ = validate_file(str(p))
    assert any("illegal edge_class" in e for e in errors)


def test_real_corpus_domains_pass():
    """The actual corpus data must be schema-valid on every field."""
    assert os.path.isdir(DOMAINS), "rrp/corpus/domains/ missing from repo"
    files = [os.path.join(DOMAINS, f) for f in os.listdir(DOMAINS)
             if f.endswith(".json")]
    assert files, "no domain files found in rrp/corpus/domains/"
    for path in files:
        errors, _, _, _ = validate_file(path)
        assert errors == [], f"{os.path.basename(path)}: {errors}"


def test_simulator_module_absence_is_recorded():
    """Honest negative: rrp/simulator.py does not exist in this repository.

    This test documents the audit finding instead of manufacturing a
    placeholder module. If a real simulator is added, replace this with a
    genuine import-smoke test against it.
    """
    assert not os.path.exists(os.path.join(REPO, "rrp", "simulator.py")), (
        "rrp/simulator.py now exists — replace this absence-record test "
        "with a real simulator smoke test.")
