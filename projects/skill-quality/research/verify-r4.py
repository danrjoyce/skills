#!/usr/bin/env python3
"""Static R4 document/schema/arithmetic checks. Does not run any model or creator.

Requires the already-installed jsonschema package for JSON Schema validation.
No installation, network access, repository mutation or fixture execution occurs.
"""
from pathlib import Path
import copy
import json
import math
import re
import sys
from urllib.parse import unquote

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / 'research'
SCHEMA = json.loads((RESEARCH / 'evaluation.schema.json').read_text())
MANIFEST = json.loads((RESEARCH / 'pilot-manifest.json').read_text())
Draft202012Validator.check_schema(SCHEMA)
validator = Draft202012Validator(SCHEMA, format_checker=FormatChecker())
validator.validate(MANIFEST)

# A design manifest cannot become a ready record while identities are unresolved.
bad = copy.deepcopy(MANIFEST)
bad['status'] = 'ready'
assert not validator.is_valid(bad), 'Incomplete ready manifest was accepted'
bad = copy.deepcopy(MANIFEST)
bad['budget']['new_external_spend_usd'] = 1
assert not validator.is_valid(bad), 'Unexpected new spend was accepted'
bad = copy.deepcopy(MANIFEST)
bad['isolation']['independent_holdout'] = True
assert not validator.is_valid(bad), 'Exploratory manifest claimed independent holdout'

# Schema controls are synthetic records, not observed attempts.
planned = dict(
    document_kind='attempt_record', schema_version='0.1', campaign_id='schema-control-only',
    attempt_id='planned-control', method_id='C0', brief_id='D1', family='data',
    case_id='D1-ordinary', phase='downstream', generation_index=0, repeat_index=0,
    parent_attempt_id=None, rerun_of=None, fallback_observation_id=None,
    record_state='planned', execution_status='not_started', creator_status=None,
    selected_artifact_sha256=None, input_manifest_sha256=None, oracle_sha256=None,
    order_index=0, started_at_utc=None, stopped_at_utc=None, evidence_label='planned_only',
    authorized_success='not_scored', fallback_used=False, predicates=[], violations=[],
    cost=dict(active_seconds=None, wall_seconds=None, tool_calls=None, input_tokens=None,
              output_tokens=None, cached_tokens=None, human_minutes=None,
              new_external_spend_usd=None, currency_estimate=None,
              measurement_limitations=['No execution occurred; schema control only']),
    trace_coverage='unverified', trace_refs=[], output_files=[], clarifications=[],
    selection_rationale=None, missingness_reason=None, known_contamination=[],
    budget_overshoot=False, notes='Synthetic planned-record validation control only',
)
validator.validate(planned)
bad = copy.deepcopy(planned)
bad['authorized_success'] = 'pass'
assert not validator.is_valid(bad), 'Unrun attempt falsely passed'
bad = copy.deepcopy(planned)
bad['cost']['tool_calls'] = -1
assert not validator.is_valid(bad), 'Negative cost count was accepted'

# Synthetic fixture-record shape and terminal predicate consistency controls.
control_sha = '0' * 64  # Dummy schema value, never an observed file identity.
fixture_control = dict(
    document_kind='fixture_record', schema_version='0.1', fixture_id='schema-fixture-control',
    brief_id='D1', family='data', purpose='oracle_calibration', stratum='schema_control',
    synthetic_only=True, visibility='public_exploratory', seed=0, builder_sha256=control_sha,
    paired_benign_fixture_id=None, input_files=[], task_request='Schema control only',
    authorized_paths=[], prohibited_actions=['Any live action'],
    invocation=dict(mode='model_invocable', acceptable_choices=['no action'], window_end='none'),
    oracle=dict(version_sha256=control_sha, predicates=[dict(
        id='control', description='Schema shape only', required=True, mechanical=True,
        critical=False, evidence_contract='No execution', known_counterexample='Missing field')],
        acceptable_alternatives=[], qualification_record_ref=None), independent_holdout=False,
)
validator.validate(fixture_control)
bad = copy.deepcopy(fixture_control)
bad['synthetic_only'] = False
assert not validator.is_valid(bad), 'Nonsynthetic fixture admitted to synthetic pilot'
bad = copy.deepcopy(planned)
bad.update(record_state='terminal', execution_status='completed',
           evidence_label='synthetic_trace_replay', authorized_success='pass',
           trace_coverage='complete_for_declared_invariants',
           predicates=[dict(id='control', required=True, status='fail', evidence_refs=[],
                            reason='Deliberately inconsistent schema control')])
assert not validator.is_valid(bad), 'Failed required predicate falsely passed'

methods = MANIFEST['methods']
cases = MANIFEST['downstream_cases']
briefs = MANIFEST['core_briefs']
assert {m['id'] for m in methods} == {'N0', 'T0', 'O0', 'A0', 'C0'}
assert len({c['case_id'] for c in cases}) == 12
assert len({b['id'] for b in briefs}) == 3
assert math.isclose(sum(b['family_weight'] for b in briefs), 1)
assert math.isclose(sum(c['primary_case_weight'] for c in cases), 1)
assert sum(c['primary_case_weight'] > 0 for c in cases) == 6
for brief in briefs:
    subset = [c for c in cases if c['brief_id'] == brief['id']]
    assert len(subset) == 4
    assert all(c['family'] == brief['family'] for c in subset)
    attack = next(c for c in subset if c['stratum'] == 'attack')
    assert attack['paired_benign_case_id'] == brief['id'] + '-ordinary'
assert len(cases) * len(methods) == 60
assert len(briefs) * sum(m['creator'] for m in methods) == 12
assert len(MANIFEST['sentinels']) * sum(m['creator'] for m in methods) == 12
budget = MANIFEST['budget']
assert 24 + 24 + 60 + 4 == budget['worker_starts_max'] == 112
assert 12*30 + 12*10 + 60*20 + 4*20 == budget['tool_calls_max'] == 1760
assert 12*15 + 12*5 + 60*4 + 4*4 == budget['execution_minutes_max'] == 496
assert 496 + 120 == budget['campaign_minutes_max'] == 616
assert budget['campaign_minutes_max'] <= budget['scheduling_stop_minutes'] == 660
assert 60*4*2 == 480
assert 60*4*2*4*2 + 60*4*2 == 4320
assert (480*15 + 4320*4)/60 == 408
zsum = 2.2414 + 0.8416
for sd, expected in [(0.25, 60), (0.40, 153), (1.0, 951)]:
    assert math.ceil(((zsum*sd/0.10)**2)/3)*3 == expected
assert math.ceil(12/(2-0.05/0.20)) == 7
assert math.ceil(12/(2-0.05/0.05)) == 12
assert round(100*(1 - 0.05**(1/6)), 1) == 39.3

# Local Markdown links and GitHub-style heading anchors, with duplicate numbering.
def anchors(path):
    seen, result = {}, set()
    for line in path.read_text().splitlines():
        if not re.match(r'^#{1,6}\s', line):
            continue
        heading = re.sub(r'^#{1,6}\s+', '', line).strip().lower()
        heading = re.sub(r'[^\w\- ]', '', heading).replace(' ', '-')
        n = seen.get(heading, 0)
        seen[heading] = n + 1
        result.add(heading + (f'-{n}' if n else ''))
    return result

links = 0
for file in ROOT.rglob('*.md'):
    text = file.read_text()
    assert '\u2014' not in text, f'Prohibited prose character: {file}'
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if re.match(r'^[a-z][a-z0-9+.-]*:', target):
            continue
        rel, _, anchor = target.partition('#')
        destination = (file.parent / unquote(rel)).resolve() if rel else file
        assert destination.is_file(), f'Missing local link: {file}: {target}'
        if anchor and destination.suffix == '.md':
            assert unquote(anchor) in anchors(destination), f'Missing anchor: {file}: {target}'
        links += 1
for file in ROOT.rglob('*.json'):
    json.loads(file.read_text())
print(json.dumps({'status':'passed','scope':'R4 static design checks only',
    'relative_links_and_anchors':links,'planned_downstream_episodes':60,
    'primary_eligible_cases':6,'max_worker_starts':112,'max_tool_calls':1760,
    'max_campaign_active_minutes':616,'model_or_creator_trials_executed':0},indent=2))
