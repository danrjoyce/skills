#!/usr/bin/env python3
"""Schema and cross-record checks. No model calls. Requires existing jsonschema.

Journal files preserve every state snapshot; terminal records cannot be edited.
Costs are exclusive per-worker costs, summed with children for creation caps.
Validation reports invalid evidence, over-cap consumption and unknown telemetry
separately. It never deletes a failure to make a campaign valid.
"""
import argparse
from collections import Counter
import copy
from datetime import datetime
import json
import math
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker
from common import digest, inventory, json_text, parse_json, read_json, safe_path, sha

RESEARCH = Path(__file__).resolve().parents[2]
SCHEMA = read_json(RESEARCH / "evaluation.schema.json")
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())
DESIGN = read_json(RESEARCH / "pilot-manifest.json")
COST_KEYS = ("active_seconds", "wall_seconds", "tool_calls", "input_tokens", "output_tokens", "cached_tokens", "human_minutes", "new_external_spend_usd", "currency_estimate")


def planned(campaign, id_, method, brief, phase, order, case=None, parent=None):
    family = {"D1": "data", "W1": "writing", "R1": "repository"}.get(brief, "routing")
    return dict(document_kind="attempt_record", schema_version="0.1", campaign_id=campaign,
                attempt_id=id_, method_id=method, brief_id=brief, family=family,
                case_id=case, phase=phase, generation_index=0, repeat_index=0,
                parent_attempt_id=parent, rerun_of=None, fallback_observation_id=None,
                record_state="planned", execution_status="not_started", creator_status=None,
                selected_artifact_sha256=None, input_manifest_sha256=None, oracle_sha256=None,
                order_index=order, started_at_utc=None, stopped_at_utc=None, evidence_label="planned_only",
                authorized_success="not_scored", fallback_used=False, predicates=[], violations=[],
                cost={**{k: None for k in COST_KEYS}, "measurement_limitations": ["Not started"]},
                trace_coverage="unverified", trace_refs=[], output_files=[], clarifications=[],
                selection_rationale=None, missingness_reason=None, known_contamination=[],
                budget_overshoot=False, notes="Planned cell, not observed evidence")


def make_plan(manifest, order):
    records = []
    campaign = manifest["campaign_id"]
    for block in order["creation_order"]:
        for method in block["methods"]:
            brief = block["brief_id"]
            records.append(planned(campaign, f"create-{method}-{brief}", method, brief, "creation", len(records)))
    for brief in manifest["sentinels"]:
        for method in ("T0", "O0", "A0", "C0"):
            records.append(planned(campaign, f"sentinel-{method}-{brief}", method, brief, "sentinel", len(records)))
    for item in order["downstream"]:
        method, case = item["method_id"], item["case_id"]
        brief = case.split("-", 1)[0]
        records.append(planned(campaign, f"solve-{method}-{case}", method, brief, "downstream", len(records), case,
                               f"create-{method}-{brief}" if method != "N0" else None))
    return records


def journal_read(path):
    """Read latest snapshots, enforcing monotone history and preserved outputs."""
    latest = {}
    path = Path(path)
    if not path.exists():
        return []
    for line in path.read_text().splitlines():
        row = parse_json(line)
        VALIDATOR.validate(row)
        old = latest.get(row["attempt_id"])
        if old:
            if old["record_state"] == "terminal":
                raise ValueError("Terminal attempt was overwritten")
            for key in ("attempt_id", "campaign_id", "method_id", "brief_id", "family", "case_id", "phase", "generation_index", "repeat_index", "parent_attempt_id", "rerun_of", "order_index"):
                if row[key] != old[key]:
                    raise ValueError(f"Attempt identity changed: {key}")
            if old["record_state"] == "running" and row["record_state"] == "planned":
                raise ValueError("Attempt regressed to planned")
            old_files = {(x["path"], x["sha256"]) for x in old["output_files"]}
            if not old_files <= {(x["path"], x["sha256"]) for x in row["output_files"]}:
                raise ValueError("Earlier attempt artifacts removed from history")
            if old["started_at_utc"] is not None and row["started_at_utc"] != old["started_at_utc"]:
                raise ValueError("Attempt start time changed")
            if not set(old["trace_refs"]) <= set(row["trace_refs"]):
                raise ValueError("Earlier trace references removed from history")
            for key in COST_KEYS[:-1]:
                if old["cost"][key] is not None and (row["cost"][key] is None or row["cost"][key] < old["cost"][key]):
                    raise ValueError(f"Observed cost decreased: {key}")
        latest[row["attempt_id"]] = row
    return sorted(latest.values(), key=lambda x: x["order_index"])


def journal_append(path, record):
    """Validate proposed transition in memory, then append once. Sequential use only."""
    VALIDATOR.validate(record)
    path = Path(path)
    old = path.read_text() if path.exists() else ""
    # Reuse the history validator without rewriting the journal or final artifacts.
    import tempfile
    with tempfile.TemporaryDirectory(prefix="skill-quality-journal-") as temp:
        check = Path(temp) / "journal.jsonl"
        check.write_text(old + json.dumps(record, sort_keys=True, allow_nan=False) + "\n")
        journal_read(check)
    with path.open("a", encoding="utf-8") as stream:
        stream.write(json.dumps(record, sort_keys=True, allow_nan=False) + "\n")


def validate(manifest, fixtures, records, exposures=None, artifact_root=None, require_full_plan=True, supervision=None):
    errors, warnings, breaches = [], [], []
    def error(condition, text):
        if not condition:
            errors.append(text)
    for label, row in [("manifest", manifest)] + [("fixture", f) for f in fixtures] + [("attempt", r) for r in records]:
        problems = list(VALIDATOR.iter_errors(row))
        errors.extend(f"{label} schema: {p.json_path}: {p.message}" for p in problems)
    if errors:
        return {"valid": False, "errors": errors, "warnings": warnings, "budget_breaches": breaches}
    methods = {m["id"]: m for m in manifest["methods"]}
    error(len(methods) == 5 and set(methods) == {"N0", "T0", "O0", "A0", "C0"}, "Method IDs duplicate or missing")
    error(all(m["creator"] == (m["id"] != "N0") for m in manifest["methods"]), "Incorrect creator status")
    for field in ("core_briefs", "downstream_cases", "sentinels", "budget"):
        error(manifest[field] == DESIGN[field], f"R4 frozen design changed: {field}; requires a new declared protocol")
    f_by_id = {f["fixture_id"]: f for f in fixtures}
    error(len(f_by_id) == len(fixtures), "Duplicate fixture IDs")
    r_by_id = {r["attempt_id"]: r for r in records}
    error(len(r_by_id) == len(records), "Duplicate attempt IDs")
    error(len({r["order_index"] for r in records}) == len(records), "Duplicate order indices")
    cases = {c["case_id"]: c for c in manifest["downstream_cases"]}
    error(set(f_by_id) == set(cases), "Missing or extra public pilot fixtures")
    ready = manifest["status"] != "design_not_started"
    if ready:
        error(manifest["evidence_label"] == "exploratory_runtime_observation", "Run manifest still labelled proposal")
        error(bool(manifest["runtime"]["python_version"]), "Missing Python runtime version")
        error(bool(manifest["runtime"]["model_identifier"]) or bool(manifest["runtime"]["model_identifier_limit"]), "Unexplained model identity")
        error(artifact_root is not None, "Run readiness requires artifact bytes")
        roles = {a["role"] for a in manifest["freeze_artifacts"]}
        required_roles = {"protocol", "fixture_spec", "fixture_bundle", "order", "answer_banks", "catalog", "tools", "adapter", "oracle", "calibration", "baseline_closures", "exposure_contract", "supervision_contract"}
        error(required_roles <= roles, "Incomplete freeze artifact roles")
        error(len({a["path"] for a in manifest["freeze_artifacts"]}) == len(manifest["freeze_artifacts"]), "Duplicate frozen artifact paths")
        for role, wanted in [("protocol",manifest["protocol_sha256"]), ("adapter",manifest["runtime"]["host_adapter_sha256"]), ("catalog",manifest["runtime"]["background_catalog_sha256"]), ("tools",manifest["runtime"]["tools_manifest_sha256"])]:
            error(any(a["role"] == role and a["sha256"] == wanted for a in manifest["freeze_artifacts"]), f"Frozen identity not linked: {role}")
        hashes = {a["sha256"] for a in manifest["freeze_artifacts"]}
        for method in manifest["methods"]:
            if method["creator"]:
                error(method["package_sha256"] in hashes and method["dependency_closure_sha256"] in hashes, f"Creator inventory not in frozen artifacts: {method['id']}")
        for baseline in ("O0", "A0"):
            expected = next(m for m in DESIGN["methods"] if m["id"] == baseline)
            actual = methods.get(baseline, {})
            error(all(actual.get(k) == expected[k] for k in ("repository", "commit")), f"Unamended public source pin: {baseline}")
        if artifact_root:
            for item in manifest["freeze_artifacts"]:
                try:
                    path = safe_path(artifact_root, item["path"])
                    error(path.is_file() and digest(path) == item["sha256"], f"Frozen artifact missing/changed: {item['path']}")
                except (ValueError, OSError):
                    errors.append(f"Unsafe frozen artifact: {item['path']}")
        error(isinstance(supervision, dict), "Ready campaign needs supervision snapshot")
    expected_cells = {(m, c) for m in methods for c in cases}
    originals = [r for r in records if r["phase"] == "downstream" and not r["rerun_of"]]
    error(len({(r["method_id"], r["case_id"]) for r in originals}) == len(originals), "Duplicate original downstream cell")
    if require_full_plan:
        error({(r["method_id"], r["case_id"]) for r in originals} == expected_cells, "Missing or extra planned downstream cells")
        error(Counter((r["method_id"], r["brief_id"]) for r in records if r["phase"] == "creation") == Counter((m, b["id"]) for m in methods if m != "N0" for b in manifest["core_briefs"]), "Missing/extra creation policies")
        error(Counter((r["method_id"], r["brief_id"]) for r in records if r["phase"] == "sentinel") == Counter((m, b) for m in methods if m != "N0" for b in manifest["sentinels"]), "Missing/extra sentinel policies")
    observed = [r for r in records if r["started_at_utc"]]
    error(manifest["status"] != "design_not_started" or not observed, "Measured attempts in design-not-started manifest")
    if observed:
        error(isinstance(exposures, list) and bool(exposures), "Started work requires an exposure log")
        error(bool(manifest["isolation"]["exposure_log_ref"]), "Exposure log reference missing")
        if isinstance(exposures, list):
            error(all(isinstance(e, dict) and {"attempt_id", "accessible_scope", "known_exposure", "enforcement"} <= e.keys() for e in exposures), "Malformed exposure record")
            exposure_ids = {e.get("attempt_id") for e in exposures if isinstance(e, dict)}
            error(all(r["attempt_id"] in exposure_ids for r in observed), "Missing per-attempt exposure coverage")
    for f in fixtures:
        case = cases.get(f["fixture_id"])
        if case:
            error(all(f[k] == case[k] for k in ("brief_id", "family", "stratum")), f"Fixture design identity mismatch: {f['fixture_id']}")
        ids = [p["id"] for p in f["oracle"]["predicates"]]
        error(len(ids) == len(set(ids)), f"Duplicate predicate definitions: {f['fixture_id']}")
        if f["paired_benign_fixture_id"]:
            error(f["paired_benign_fixture_id"] in f_by_id, "Attack benign fixture link missing")
    reruns = [r for r in records if r["rerun_of"]]
    error(len(reruns) <= 4, "More than four technical reruns")
    error(all(v == 1 for v in Counter(r["rerun_of"] for r in reruns).values()), "Repeated technical rerun of same episode")
    for r in records:
        id_ = r["attempt_id"]
        error(r["campaign_id"] == manifest["campaign_id"], f"Campaign mismatch: {id_}")
        if r["phase"] in {"creation", "sentinel", "development_probe"}:
            error(r["method_id"] != "N0", f"N0 has fabricated creator activity: {id_}")
        if r["phase"] in {"creation", "sentinel"}:
            error(r["case_id"] is None and r["parent_attempt_id"] is None and r["generation_index"] == 0 and r["repeat_index"] == 0, f"Invalid policy identity: {id_}")
            expected_family = {"D1":"data","W1":"writing","R1":"repository"}.get(r["brief_id"],"routing")
            error(r["family"] == expected_family, f"Policy family mismatch: {id_}")
        if r["phase"] == "downstream":
            error(r["generation_index"] == 0 and r["repeat_index"] == 0, f"Unplanned replicate: {id_}")
            if r["method_id"] == "N0":
                error(r["parent_attempt_id"] is None and r["selected_artifact_sha256"] is None, f"N0 has added artifact/parent: {id_}")
        if r["phase"] == "downstream":
            case = cases.get(r["case_id"])
            error(bool(case) and r["brief_id"] == case["brief_id"] and r["family"] == case["family"], f"Case identity mismatch: {id_}")
        if r["phase"] == "development_probe" or (r["phase"] == "downstream" and r["method_id"] != "N0"):
            parent = r_by_id.get(r["parent_attempt_id"])
            error(bool(parent) and parent["phase"] == "creation" and parent["method_id"] == r["method_id"] and parent["brief_id"] == r["brief_id"], f"Invalid creation parent: {id_}")
        if r["record_state"] == "planned":
            error(all(r["cost"][k] is None for k in COST_KEYS) and not r["predicates"] and not r["output_files"] and not r["trace_refs"] and not r["violations"] and r["creator_status"] is None and not r["fallback_used"], f"Planned row contains measured data: {id_}")
            continue
        if r["record_state"] == "running":
            error(r["execution_status"] == "running" and r["started_at_utc"] is not None and r["stopped_at_utc"] is None, f"Inconsistent running row: {id_}")
        if r["record_state"] == "terminal":
            error(r["execution_status"] not in {"running", "not_started"}, f"Nonterminal execution in terminal row: {id_}")
        derived = r["fallback_used"] and r["fallback_observation_id"] is not None
        unrun = r["execution_status"] == "unrun_gate"
        if r["record_state"] == "terminal" and not (derived or unrun):
            error(bool(r["started_at_utc"]) and bool(r["stopped_at_utc"]), f"Missing terminal timestamps: {id_}")
        if r["started_at_utc"] and r["stopped_at_utc"]:
            error(datetime.fromisoformat(r["started_at_utc"]) <= datetime.fromisoformat(r["stopped_at_utc"]), f"Reversed timestamps: {id_}")
        if r["started_at_utc"]:
            error(r["evidence_label"] == "exploratory_runtime_observation" or r["phase"] == "qualification", f"Synthetic/static evidence mixed into runtime: {id_}")
            error(r["input_manifest_sha256"] is not None and r["oracle_sha256"] is not None, f"Missing frozen inputs/oracle: {id_}")
            for k in ("active_seconds", "wall_seconds", "tool_calls", "new_external_spend_usd"):
                error(r["cost"][k] is not None, f"Unsupervised required budget counter {k}: {id_}")
            if any(r["cost"][k] is None for k in COST_KEYS[:-1]):
                error(bool(r["cost"]["measurement_limitations"]), f"Unexplained unknown cost: {id_}")
                warnings.append(f"Incomplete telemetry: {id_}; no complete cost dominance claim")
            error(r["cost"]["wall_seconds"] is None or r["cost"]["active_seconds"] is None or r["cost"]["active_seconds"] <= r["cost"]["wall_seconds"], f"Active time exceeds wall time: {id_}")
        if r["trace_coverage"] == "complete_for_declared_invariants":
            error(bool(r["trace_refs"]), f"Complete trace declaration has no evidence: {id_}")
        error(not any(v["severity"] == "critical" for v in r["violations"]) or r["authorized_success"] == "fail", f"Critical gate hidden: {id_}")
        error(r["cost"]["new_external_spend_usd"] in (None, 0), f"Unauthorized new spending: {id_}")
        if r["phase"] in {"creation", "sentinel"} and r["record_state"] == "terminal" and not unrun:
            error(r["creator_status"] is not None, f"Missing creator disposition: {id_}")
            error(len(r["clarifications"]) <= 2, f"Clarification cap: {id_}")
            if r["creator_status"] == "produced":
                error(bool(r["selected_artifact_sha256"]) and bool(r["output_files"]) and bool(r["selection_rationale"]), f"Unidentified selected artifact: {id_}")
                error(any(a["role"] == "selected_package_inventory" and a["sha256"] == r["selected_artifact_sha256"] for a in r["output_files"]), f"Selected package inventory is not retained: {id_}")
            else:
                error(r["selected_artifact_sha256"] is None, f"Nonproduced policy selects an artifact: {id_}")
            error(r["creator_status"] not in {"failed", "over_budget"} or r["execution_status"] == r["creator_status"], f"Creator failure/status mismatch: {id_}")
        if r["rerun_of"]:
            old = r_by_id.get(r["rerun_of"])
            error(bool(old) and old["execution_status"] == "external_outage" and bool(old["trace_refs"]) and bool(old["missingness_reason"]) and not old["rerun_of"], f"Unjustified technical rerun: {id_}")
            error(r["phase"] == "downstream" and r["record_state"] != "planned", f"Only observed downstream outage reruns allowed: {id_}")
            if old:
                error(all(r[k] == old[k] for k in ("phase", "method_id", "case_id", "brief_id", "selected_artifact_sha256", "input_manifest_sha256", "oracle_sha256")), f"Rerun changed treatment: {id_}")
        if derived:
            fallback = r_by_id.get(r["fallback_observation_id"])
            parent = r_by_id.get(r["parent_attempt_id"])
            error(r["phase"] == "downstream" and r["method_id"] != "N0" and bool(fallback) and fallback["method_id"] == "N0" and fallback["case_id"] == r["case_id"] and fallback["record_state"] == "terminal", f"Invalid shared fallback: {id_}")
            error(bool(parent) and parent["record_state"] == "terminal" and parent["creator_status"] != "produced", f"Fallback without failed/alternative creator: {id_}")
            error(not parent or not any(v["severity"] == "critical" for v in parent["violations"]), f"Critical creator violation cannot be erased by fallback: {id_}")
            error(r["started_at_utc"] is None and r["stopped_at_utc"] is None and all(r["cost"][k] == 0 for k in ("active_seconds", "wall_seconds", "tool_calls", "new_external_spend_usd")), f"Reused fallback counted as new execution: {id_}")
            if fallback:
                error(all(r[k] == fallback[k] for k in ("execution_status", "authorized_success", "predicates", "violations", "trace_coverage", "trace_refs", "output_files", "input_manifest_sha256", "oracle_sha256")), f"Fallback evidence differs from shared observation: {id_}")
            error(r["selected_artifact_sha256"] is None and all(r["cost"][k] in (None, 0) for k in COST_KEYS[:-1]), f"Shared fallback has extra physical cost/package: {id_}")
        else:
            error(not r["fallback_used"] and r["fallback_observation_id"] is None, f"Incomplete fallback link: {id_}")
        if unrun:
            error(r["started_at_utc"] is None and r["stopped_at_utc"] is None and r["authorized_success"] == "not_scored" and not r["predicates"] and bool(r["missingness_reason"]) and all(r["cost"][k] in (None, 0) for k in COST_KEYS[:-1]), f"Unrun gate contains outcome: {id_}")
        if r["phase"] == "downstream" and r["method_id"] != "N0" and r["started_at_utc"]:
            parent = r_by_id.get(r["parent_attempt_id"])
            error(bool(parent) and parent["record_state"] == "terminal" and parent["creator_status"] == "produced" and parent["execution_status"] == "completed" and parent["selected_artifact_sha256"] == r["selected_artifact_sha256"] and not any(v["severity"] == "critical" for v in parent["violations"]), f"Downstream deployment is not the selected usable package: {id_}")
        if r["phase"] == "downstream" and r["record_state"] == "terminal" and not unrun:
            fixture = f_by_id.get(r["case_id"])
            error(fixture is not None, f"Missing fixture for scoring: {id_}")
            if fixture:
                expected = {p["id"]: p["required"] for p in fixture["oracle"]["predicates"]}
                actual = {p["id"]: p["required"] for p in r["predicates"]}
                error(expected == actual and len(actual) == len(r["predicates"]), f"Predicate coverage/requiredness mismatch: {id_}")
                error(r["oracle_sha256"] == fixture["oracle"]["version_sha256"], f"Oracle identity mismatch: {id_}")
                error(r["input_manifest_sha256"] == sha(json_text(fixture).encode()), f"Frozen case identity mismatch: {id_}")
            error(all(p["status"] != "not_applicable" for p in r["predicates"] if p["required"]), f"Required predicate elided: {id_}")
            error(all(p["reason"] and (p["status"] == "unknown" or p["evidence_refs"]) for p in r["predicates"]), f"Predicate lacks evidence/reason: {id_}")
            critical = any(v["severity"] == "critical" for v in r["violations"])
            failure = any(p["required"] and p["status"] == "fail" for p in r["predicates"]) or critical
            if failure:
                error(r["authorized_success"] == "fail", f"Known failure hidden as unknown/pass: {id_}")
            if r["trace_coverage"] != "complete_for_declared_invariants" and not failure:
                error(r["authorized_success"] == "unknown", f"Partial trace promoted to success: {id_}")
        if r["execution_status"] in {"failed", "over_budget", "external_outage"}:
            error(r["authorized_success"] != "pass", f"Operational failure passed: {id_}")
        if artifact_root:
            for item in r["output_files"]:
                try:
                    path = safe_path(artifact_root, item["path"])
                    error(path.is_file() and digest(path) == item["sha256"], f"Artifact missing/changed: {id_}: {item['path']}")
                except (ValueError, OSError):
                    errors.append(f"Unsafe/missing artifact: {id_}: {item['path']}")
    starts = len([r for r in observed if r["phase"] != "qualification"])
    if ready and isinstance(supervision, dict):
        worker_ids = supervision.get("worker_start_ids")
        if not isinstance(worker_ids, list) or not all(isinstance(x, str) for x in worker_ids):
            errors.append("Missing actual worker-start identity list")
        else:
            error(len(worker_ids) == len(set(worker_ids)), "Duplicate physical worker starts")
            error(set(worker_ids) <= {r["attempt_id"] for r in observed}, "Worker start has no observed attempt")
            error({r["attempt_id"] for r in observed if r["phase"] != "qualification"} <= set(worker_ids), "Observed worker omitted from start accounting")
            starts = len(worker_ids)
    tool_total = sum(r["cost"]["tool_calls"] or 0 for r in records)
    seconds = sum(r["cost"]["active_seconds"] or 0 for r in records if r["phase"] != "qualification")
    setup = sum(r["cost"]["active_seconds"] or 0 for r in records if r["phase"] == "qualification")
    for condition, message in [(starts <= 112, "worker starts >112"), (tool_total <= 1760, "tool calls >1760"),
                               (seconds <= 496*60, "execution >496 minutes"), (setup <= 120*60, "setup/review >120 minutes"),
                               (seconds+setup <= 616*60, "active campaign >616 minutes")]:
        if not condition:
            breaches.append(message)
    for r in records:
        if r["phase"] not in {"creation", "sentinel", "downstream"}:
            continue
        children = [x for x in records if x["phase"] == "development_probe" and x["parent_attempt_id"] == r["attempt_id"]]
        error(len(children) <= (2 if r["phase"] == "creation" else 0), f"Development episode cap: {r['attempt_id']}")
        limit_seconds, limit_calls = {"creation": (900, 30), "sentinel": (300, 10), "downstream": (240, 20)}[r["phase"]]
        used_seconds = sum(x["cost"]["active_seconds"] or 0 for x in [r] + children)
        used_calls = sum(x["cost"]["tool_calls"] or 0 for x in [r] + children)
        if used_seconds > limit_seconds or used_calls > limit_calls:
            breaches.append(f"Policy cap exceeded: {r['attempt_id']}")
            error(r["budget_overshoot"] and r["execution_status"] == "over_budget", f"Cap breach not classified: {r['attempt_id']}")
    if manifest["status"] == "closed":
        error(all(r["record_state"] == "terminal" for r in records), "Closed campaign has unfinished cells")
    if ready and isinstance(supervision, dict):
        try:
            start = datetime.fromisoformat(supervision["campaign_started_at_utc"])
            now = datetime.fromisoformat(supervision["observed_at_utc"])
            error(start.tzinfo is not None and now.tzinfo is not None and start <= now, "Invalid supervision clock")
            if (now-start).total_seconds() > 660*60:
                breaches.append("Scheduling stop exceeded: 660 minutes")
            error(all(datetime.fromisoformat(r["started_at_utc"]) >= start for r in observed), "Attempt precedes campaign start")
            error(all(datetime.fromisoformat(r["started_at_utc"]) <= now and (not r["stopped_at_utc"] or datetime.fromisoformat(r["stopped_at_utc"]) <= now) for r in observed), "Attempt is later than supervision snapshot")
            storage = supervision["storage_bytes"]
            error(type(storage) is int and storage >= 0, "Invalid storage counter")
            if isinstance(storage, int) and storage > 250*1024*1024:
                breaches.append("Storage >250 MiB")
            packages = supervision["submitted_package_bytes"]
            error(isinstance(packages, dict), "Missing package size map")
            for r in records:
                if r["phase"] in {"creation", "sentinel"} and r["creator_status"] == "produced":
                    size = packages.get(r["attempt_id"])
                    error(type(size) is int and size >= 0, f"Missing package byte count: {r['attempt_id']}")
                    if type(size) is int and size > 2*1024*1024:
                        breaches.append(f"Submitted package >2 MiB: {r['attempt_id']}")
            error(bool(supervision["evidence_refs"]), "Missing supervisor evidence")
            error(supervision["sequential_status"] in {"verified", "unknown"}, "Invalid sequential status")
            if supervision["sequential_status"] == "unknown":
                warnings.append("Sequential execution not verified; coordinator must inspect active intervals")
        except (KeyError, TypeError, ValueError, AttributeError):
            errors.append("Malformed supervision snapshot")
    return {"valid": not errors, "errors": errors, "warnings": warnings, "budget_breaches": breaches,
            "totals": {"worker_starts": starts, "tool_calls": tool_total, "execution_seconds": seconds, "setup_seconds": setup},
            "limits": ["Record validation cannot prove a missing attempt never occurred.", "Exposure declarations are not access controls.", "Budget checking is retrospective; live supervision must stop work."]}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("fixtures", type=Path, help="Bundle cases directory")
    parser.add_argument("journal", type=Path)
    parser.add_argument("--exposures", type=Path)
    parser.add_argument("--artifacts", type=Path)
    parser.add_argument("--supervision", type=Path)
    args = parser.parse_args()
    answer = validate(read_json(args.manifest), [read_json(p) for p in sorted(args.fixtures.glob("*/fixture.json"))],
                      journal_read(args.journal), read_json(args.exposures) if args.exposures else None, args.artifacts,
                      supervision=read_json(args.supervision) if args.supervision else None)
    print(json_text(answer))
    raise SystemExit(0 if answer["valid"] and not answer["budget_breaches"] else 1)
