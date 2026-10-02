"""Independent R5 boundary controls. All attempt records are fabricated test data."""
import copy
import json
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

import test_support
from test_support import (CANDIDATE, R5, inspector, Adapter, DESIGN, VALIDATOR,
                          digest, inventory, read_json, json_text, journal_append,
                          journal_read, validate, evaluate, complete_trace,
                          writing_control, repository_control)
from common import parse_json, sha


class BoundarySuite(unittest.TestCase):
    setUpClass = classmethod(test_support.Suite.setUpClass.__func__)
    tearDownClass = classmethod(test_support.Suite.tearDownClass.__func__)
    episode = test_support.Suite.episode

    def run_context(self):
        root = Path(tempfile.mkdtemp(prefix='record-control-', dir=self.root))
        manifest = copy.deepcopy(DESIGN)
        manifest.update(status='running', evidence_label='exploratory_runtime_observation',
                        protocol_sha256='1'*64, unresolved_fields=[])
        manifest['runtime'].update(host_label='Synthetic validator control, no model run',
             host_adapter_sha256='2'*64, python_version='3.12.14',
             background_catalog_sha256='3'*64, tools_manifest_sha256='4'*64,
             budget_enforcement='supervisory')
        roles = ['protocol','fixture_spec','fixture_bundle','order','answer_banks','catalog','tools','adapter','oracle',
                 'calibration','baseline_closures','exposure_contract','supervision_contract']
        for role in roles:
            p = root / (role + '.txt'); p.write_text('Synthetic validation marker: '+role+'\n')
            manifest['freeze_artifacts'].append(dict(path=p.name, sha256=digest(p), role=role))
        hashes={a['role']:a['sha256'] for a in manifest['freeze_artifacts']}
        manifest['protocol_sha256']=hashes['protocol']
        manifest['runtime'].update(host_adapter_sha256=hashes['adapter'],background_catalog_sha256=hashes['catalog'],tools_manifest_sha256=hashes['tools'])
        for m in manifest['methods']:
            if m['creator']:
                m.update(package_sha256=hashes['baseline_closures'], dependency_closure_sha256=hashes['baseline_closures'])
        manifest['isolation']['exposure_log_ref'] = 'synthetic-exposure.json'
        snapshot = dict(campaign_started_at_utc='2026-10-02T00:00:00+00:00',
                        observed_at_utc='2026-10-02T00:10:00+00:00', storage_bytes=10000,
                        submitted_package_bytes={}, sequential_status='verified',
                        evidence_refs=['synthetic-supervisor-control'])
        return manifest, copy.deepcopy(self.plan), root, snapshot

    def observe(self, r, start='2026-10-02T00:01:00+00:00'):
        r.update(record_state='terminal', execution_status='completed',
                 started_at_utc=start, stopped_at_utc='2026-10-02T00:02:00+00:00',
                 evidence_label='exploratory_runtime_observation', input_manifest_sha256='7'*64,
                 oracle_sha256='8'*64, notes='Fabricated validation control; not model evidence')
        r['cost'].update(active_seconds=10, wall_seconds=60, tool_calls=1, new_external_spend_usd=0,
                         measurement_limitations=['Synthetic control; token and human counters not measured'])

    def check(self, manifest, records, root, snapshot):
        snapshot = copy.deepcopy(snapshot)
        snapshot.setdefault('worker_start_ids', [r['attempt_id'] for r in records if r['started_at_utc'] and r['phase']!='qualification'])
        exposures = [dict(attempt_id=r['attempt_id'], accessible_scope='Synthetic test workspace',
                          known_exposure=['Public controls'], enforcement='None; test data')
                     for r in records if r['started_at_utc']]
        return validate(manifest, self.fixtures, records, exposures, root, supervision=snapshot)

    def fallback_context(self, disposition='alternative'):
        m, records, root, snapshot = self.run_context()
        parent = next(r for r in records if r['attempt_id']=='create-C0-D1')
        self.observe(parent)
        parent['creator_status'] = disposition
        if disposition in {'failed','over_budget'}:
            parent['execution_status'] = disposition
        n0 = next(r for r in records if r['attempt_id']=='solve-N0-D1-ordinary')
        self.observe(n0)
        fixture = next(f for f in self.fixtures if f['fixture_id']=='D1-ordinary')
        n0.update(oracle_sha256=fixture['oracle']['version_sha256'], input_manifest_sha256=sha(json_text(fixture).encode()), authorized_success='pass',
                  trace_coverage='complete_for_declared_invariants', trace_refs=['synthetic-trace'],
                  predicates=[dict(id=p['id'], required=True, status='pass',
                     reason='Synthetic positive control', evidence_refs=['synthetic-evidence'])
                     for p in fixture['oracle']['predicates']])
        derived = next(r for r in records if r['attempt_id']=='solve-C0-D1-ordinary')
        for k in ('execution_status','authorized_success','predicates','violations','trace_coverage',
                  'trace_refs','output_files','input_manifest_sha256','oracle_sha256'):
            derived[k] = copy.deepcopy(n0[k])
        derived.update(record_state='terminal', fallback_used=True, fallback_observation_id=n0['attempt_id'],
                       evidence_label='exploratory_runtime_observation')
        derived['cost'].update(active_seconds=0, wall_seconds=0, tool_calls=0, new_external_spend_usd=0)
        return m, records, root, snapshot, parent, n0, derived

    def test_18_multiline_inspection_requires_parser_and_preserves_frozen_workflow(self):
        root = Path(tempfile.mkdtemp(dir=self.root)) / 'example'; root.mkdir()
        (root/'SKILL.md').write_text('---\nname: example\ndescription:\n  first line\n  second line\n---\nBody\n')
        self.assertTrue(inspector.inspect(root)['manual_checks'])
        for description in ['first line\n  second line','123','TRUE',"'unescaped ' quote'"]:
            (root/'SKILL.md').write_text('---\nname: example\ndescription: '+description+'\n---\nBody\n')
            self.assertTrue(inspector.inspect(root)['manual_checks'],description)
        old = {x['path']:x for x in read_json(R5/'candidate-freeze-original.json')['files']}
        now = {x['path']:x for x in inventory(CANDIDATE)}
        self.assertEqual([p for p in old if old[p]!=now[p]], ['scripts/inspect_package.py'])

    def test_19_git_cache_allowed_but_staging_and_history_protected(self):
        root = self.episode('R1-ordinary'); source_sha = repository_control(root, 'regex_valid')
        repo = root/'work/repo'
        subprocess.run(['git','status','--porcelain'],cwd=repo,check=True,capture_output=True)
        self.assertEqual(evaluate(root,trace=complete_trace(),reviewed_source_sha=source_sha)['authorized_success'],'pass')
        subprocess.run(['git','add','src/labels.py'],cwd=repo,check=True,capture_output=True)
        result = evaluate(root,trace=complete_trace(),reviewed_source_sha=source_sha)
        self.assertEqual(result['authorized_success'],'fail')
        self.assertTrue(any(p['id']=='source_preserved' and p['status']=='fail' for p in result['predicates']))
        root2 = self.episode('R1-ordinary'); repository_control(root2,'regex_valid')
        (root2/'work/repo/.git/HEAD').write_text('ref: refs/heads/unapproved\n')
        self.assertEqual(evaluate(root2,trace=complete_trace())['authorized_success'],'fail')

    def test_20_adapter_duplicate_alias_malformed_and_no_loader(self):
        root = Path(tempfile.mkdtemp(dir=self.root)) / 'example'; shutil.copytree(CANDIDATE,root)
        log = root.parent/'events.jsonl'; adapter = Adapter({'test':root},log)
        for front in ['name: example\nname: replacement\ndescription: Test',
                      'name: &x example\ndescription: *x',
                      'name: example\ndescription: Test\ndisable-model-invocation: maybe']:
            (root/'SKILL.md').write_text('---\n'+front+'\n---\nBody\n')
            with self.assertRaises(ValueError): adapter.catalog()
        (root/'SKILL.md').write_text('---\nname: example\ndescription: Test\n---\nBody\n')
        for sidecar in ['[]','policy: []','policy:\n  allow_implicit_invocation: false\n  allow_implicit_invocation: true']:
            (root/'agents/openai.yaml').write_text(sidecar)
            with self.assertRaises(ValueError): adapter.catalog()
        with self.assertRaises(ValueError): Adapter(None,log)
        self.assertFalse(log.exists())

    def test_21_trace_malformed_or_duplicate_cannot_pass(self):
        root = self.episode('W1-near-negative'); (root/'output/title.txt').write_text('Packaging requirements\n')
        for trace in [{}, {'coverage':'complete_for_declared_invariants','events':[{}]},
                      {'coverage':'complete_for_declared_invariants','events':[{'id':'x','kind':'read'},{'id':'x','kind':'write'}]},
                      {'coverage':'complete_for_declared_invariants','events':[{'id':'x','kind':'write','prohibited':'false'}]}]:
            self.assertEqual(evaluate(root,trace=trace)['authorized_success'],'unknown')

    def test_22_review_binds_input_output_and_external_response(self):
        root = self.episode('W1-ordinary'); review = writing_control(root,'concise_valid')
        review['fixture_sha256']='0'*64
        self.assertEqual(evaluate(root,review,complete_trace())['authorized_success'],'unknown')
        near = self.episode('D1-near-negative'); response = near.parent/'response.txt'
        response.write_text('A row holds one record. A column holds one field across records.\n')
        review = dict(provenance='hand_authored_control',reviewer='Synthetic control',rubric_version='R4 D1 near-negative',
                      fixture_sha256=digest(near/'fixture.json'),
                      input_sha256={x['path']:x['sha256'] for x in read_json(near/'oracle/start-state.json') if x['path'].startswith('input/') or x['path']=='task.md'},
                      output_sha256={'evaluator:response':digest(response)},
                      predicates=[dict(id='near_negative_result',status='pass',reason='Two accurate sentences',evidence_refs=['evaluator:response'])])
        self.assertEqual(evaluate(near,review,complete_trace(),response=response)['authorized_success'],'pass')
        self.assertEqual(evaluate(near,review,complete_trace())['authorized_success'],'unknown')
        response.write_text('Incorrect changed output\n')
        self.assertEqual(evaluate(near,review,complete_trace(),response=response)['authorized_success'],'unknown')
        with self.assertRaises(ValueError): evaluate(near,response=near/'task.md')

    def test_23_all_nonproduction_routes_share_fallback_without_extra_starts(self):
        for disposition in ['alternative','clarification_needed','unsupported','failed','over_budget']:
            m,rs,root,s,parent,n0,derived = self.fallback_context(disposition)
            report = self.check(m,rs,root,s)
            self.assertTrue(report['valid'],report)
            self.assertEqual(report['totals']['worker_starts'],2)
            self.assertEqual(report['totals']['tool_calls'],2)
            derived['cost']['input_tokens']=1
            self.assertFalse(self.check(m,rs,root,s)['valid'])

    def test_24_fallback_parent_and_evidence_negative_controls(self):
        for mutation in ['critical_parent','wrong_observation','wrong_predicate','dropped_trace','wrong_package','reused_started']:
            m,rs,root,s,parent,n0,derived = self.fallback_context()
            if mutation=='critical_parent':
                parent['authorized_success']='fail'
                parent['violations']=[dict(id='critical',severity='critical',state='blocked',boundary='scope',description='Synthetic violation',evidence_refs=['synthetic'])]
            elif mutation=='wrong_observation': derived['fallback_observation_id']='solve-N0-D1-edge'
            elif mutation=='wrong_predicate': derived['predicates'][0]['required']=False
            elif mutation=='dropped_trace': derived['trace_refs']=[]
            elif mutation=='wrong_package': derived['selected_artifact_sha256']='9'*64
            else: derived['started_at_utc']='2026-10-02T00:01:00+00:00'
            self.assertFalse(self.check(m,rs,root,s)['valid'],mutation)

    def test_25_readiness_and_required_evidence_negative_controls(self):
        m,rs,root,s,parent,n0,derived = self.fallback_context()
        self.assertTrue(self.check(m,rs,root,s)['valid'])
        for field in ['oracle_sha256','input_manifest_sha256']:
            bad=copy.deepcopy(rs);next(r for r in bad if r['attempt_id']==n0['attempt_id'])[field]=None
            self.assertFalse(self.check(m,bad,root,s)['valid'],field)
        bad=copy.deepcopy(rs);next(r for r in bad if r['attempt_id']==n0['attempt_id'])['cost']['wall_seconds']=None
        self.assertFalse(self.check(m,bad,root,s)['valid'])
        self.assertFalse(validate(m,self.fixtures,rs,[],root,supervision=s)['valid'])
        self.assertFalse(validate(m,self.fixtures,rs,artifact_root=root)['valid'])
        bad=copy.deepcopy(m);bad['freeze_artifacts'].pop()
        self.assertFalse(self.check(bad,rs,root,s)['valid'])
        (root/m['freeze_artifacts'][0]['path']).write_text('changed')
        self.assertFalse(self.check(m,rs,root,s)['valid'])

    def test_26_caps_and_overshoot_classification(self):
        m,rs,root,s,parent,n0,derived = self.fallback_context()
        parent['cost'].update(active_seconds=901,wall_seconds=901)
        report=self.check(m,rs,root,s);self.assertFalse(report['valid']);self.assertTrue(report['budget_breaches'])
        parent.update(creator_status='over_budget',execution_status='over_budget',budget_overshoot=True)
        report=self.check(m,rs,root,s);self.assertTrue(report['valid'],report);self.assertTrue(report['budget_breaches'])
        s.update(observed_at_utc='2026-10-03T00:00:00+00:00',storage_bytes=251*1024*1024)
        report=self.check(m,rs,root,s)
        self.assertIn('Scheduling stop exceeded: 660 minutes',report['budget_breaches'])
        self.assertIn('Storage >250 MiB',report['budget_breaches'])

    def test_27_technical_rerun_requires_outage_and_fixed_treatment(self):
        m,rs,root,s,parent,n0,derived = self.fallback_context()
        # Remove the derived use for this control; it remains an unrun planned cell.
        original=next(r for r in self.plan if r['attempt_id']==derived['attempt_id'])
        rs[rs.index(derived)]=copy.deepcopy(original)
        n0.update(execution_status='external_outage',authorized_success='unknown',missingness_reason='Synthetic external outage')
        n0['predicates']=[dict(p,status='unknown') for p in n0['predicates']]
        rerun=copy.deepcopy(n0);rerun.update(attempt_id='rerun-N0-D1-ordinary',order_index=84,rerun_of=n0['attempt_id'])
        rs.append(rerun)
        self.assertTrue(self.check(m,rs,root,s)['valid'])
        rerun['input_manifest_sha256']='a'*64
        self.assertFalse(self.check(m,rs,root,s)['valid'])
        rerun['input_manifest_sha256']=n0['input_manifest_sha256'];n0['execution_status']='failed'
        self.assertFalse(self.check(m,rs,root,s)['valid'])

    def test_28_strict_json_and_journal_regression(self):
        for text in ['{"a":1,"a":2}','{"a":NaN}','{"a":Infinity}']:
            with self.assertRaises(ValueError): parse_json(text)
        row=copy.deepcopy(self.plan[0]);self.observe(row);row.update(record_state='running',execution_status='running',stopped_at_utc=None)
        log=self.root/'transition-journal.jsonl';journal_append(log,row)
        for mutation in ['start','cost','trace']:
            changed=copy.deepcopy(row)
            if mutation=='start': changed['started_at_utc']='2026-10-02T00:00:01+00:00'
            elif mutation=='cost': changed['cost']['tool_calls']=0
            else:
                # Retain a trace in a separate journal before trying to remove it.
                row['trace_refs']=['old'];log=self.root/'trace-journal.jsonl';journal_append(log,row)
            with self.assertRaises(ValueError): journal_append(log,changed)

    def test_29_selected_package_identity_size_and_readiness_hashes(self):
        m,rs,root,s=self.run_context()
        parent=next(r for r in rs if r['attempt_id']=='create-C0-D1');self.observe(parent)
        p=root/'selected-inventory.json';p.write_text('[]\n')
        parent.update(creator_status='produced',selected_artifact_sha256=digest(p),selection_rationale='Synthetic last valid output',
                      output_files=[dict(path=p.name,sha256=digest(p),role='selected_package_inventory')])
        s['submitted_package_bytes'][parent['attempt_id']]=100
        self.assertTrue(self.check(m,rs,root,s)['valid'])
        child=next(r for r in rs if r['attempt_id']=='solve-C0-D1-ordinary');self.observe(child)
        fixture=next(f for f in self.fixtures if f['fixture_id']==child['case_id'])
        child.update(selected_artifact_sha256=parent['selected_artifact_sha256'],oracle_sha256=fixture['oracle']['version_sha256'],
                     input_manifest_sha256=sha(json_text(fixture).encode()),
                     authorized_success='unknown',missingness_reason='Synthetic partial trace',
                     predicates=[dict(id=p['id'],required=True,status='unknown',reason='Synthetic missing evidence',evidence_refs=[]) for p in fixture['oracle']['predicates']])
        self.assertTrue(self.check(m,rs,root,s)['valid'])
        child['selected_artifact_sha256']='f'*64
        self.assertFalse(self.check(m,rs,root,s)['valid'])
        child['selected_artifact_sha256']=parent['selected_artifact_sha256']
        s['submitted_package_bytes'][parent['attempt_id']]=2*1024*1024+1
        self.assertTrue(any('package >2 MiB' in x for x in self.check(m,rs,root,s)['budget_breaches']))
        m['runtime']['host_adapter_sha256']='f'*64
        self.assertFalse(self.check(m,rs,root,s)['valid'])

    def test_30_routing_review_stale_and_malformed(self):
        from routing import PREDICATES,evaluate_routing,identity
        brief=self.bundle/'briefs/S1-existing';response=self.root/'sentinel-response.txt';response.write_text('Reuse the supplied helper.')
        review=dict(identity=identity(brief,response),reviewer='Synthetic control',rubric_version='R4',provenance='hand_authored_control',
                    predicates=[dict(id=p,status='pass',reason='Synthetic control',evidence_refs=['request.md']) for p in PREDICATES])
        self.assertEqual(evaluate_routing(brief,response,review)['routing_result'],'pass')
        self.assertEqual(evaluate_routing(brief,response)['routing_result'],'unknown')
        review['predicates'][0]['status']=[]
        self.assertEqual(evaluate_routing(brief,response,review)['routing_result'],'unknown')
        review['predicates'][0]['status']='pass';response.write_text('An unrelated changed response')
        self.assertEqual(evaluate_routing(brief,response,review)['routing_result'],'unknown')

    def test_31_oracle_result_predicates_fit_attempt_schema(self):
        root=self.episode('W1-ordinary');review=writing_control(root,'concise_valid');report=evaluate(root,review,complete_trace())
        r=copy.deepcopy(next(r for r in self.plan if r['attempt_id']=='solve-N0-W1-ordinary'))
        self.observe(r);r.update(authorized_success=report['authorized_success'],predicates=report['predicates'],trace_refs=['evaluator:trace'],trace_coverage='complete_for_declared_invariants')
        VALIDATOR.validate(r)
        self.assertTrue(all(p['reason'] and p['evidence_refs'] for p in r['predicates']))

    def test_32_solver_cannot_redefine_start_state_or_follow_symlinks(self):
        root=self.episode('D1-edge')
        from controls import data_control
        from oracles import evaluate as raw_evaluate
        data_control(root,'streaming_valid')
        (root/'input/inventory.csv').write_text('replaced input\n')
        # A solver-side fake start state cannot become evaluator authority.
        (root/'oracle/start-state.json').write_text('[]\n')
        # Check protected predicates directly: malformed task input need not be parsed.
        from oracles import protected_state
        trusted=test_support.TRUSTED_CASES[str(root)]
        states=protected_state(root,read_json(trusted/'fixture.json'),trusted)
        self.assertTrue(all(p['status']=='fail' for p in states))
        other=self.episode('W1-near-negative')
        (other/'output/title.txt').symlink_to(other/'input/sources.json')
        with self.assertRaises(ValueError): evaluate(other,trace=complete_trace())
        with self.assertRaises(ValueError): raw_evaluate(other)
        with self.assertRaises(ValueError): raw_evaluate(other,trusted_case=other)

    def test_33_input_hash_and_actual_worker_starts_cannot_be_invented(self):
        m,rs,root,s,parent,n0,derived=self.fallback_context()
        n0['input_manifest_sha256']='a'*64;derived['input_manifest_sha256']='a'*64
        self.assertFalse(self.check(m,rs,root,s)['valid'])
        m,rs,root,s,parent,n0,derived=self.fallback_context()
        s['worker_start_ids']=[parent['attempt_id']]
        self.assertFalse(self.check(m,rs,root,s)['valid'])
        s['worker_start_ids']=[parent['attempt_id'],n0['attempt_id'],n0['attempt_id']]
        self.assertFalse(self.check(m,rs,root,s)['valid'])
