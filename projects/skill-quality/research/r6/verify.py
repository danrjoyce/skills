"""Local evidence consistency checks only; never proves complete host telemetry."""
import base64, hashlib, importlib.util, json
from pathlib import Path
import coordinator as c
R=c.ROOT

def module(name,path):
 spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
runner=module('runner',R/'diagnostic-runner.py');codec=module('codec',R/'archive-io.py')
runner.check_frozen()
rows=[json.loads(s) for s in (R/'journal.jsonl').read_text().splitlines()];starts=[r['attempt_id'] for r in rows if r.get('state')=='running'];last={r['attempt_id']:r for r in rows if 'attempt_id' in r and 'state' in r};assert len(starts)==len(set(starts))==17
assert all(last[x]['state']=='terminal' for x in starts)
results=json.loads((R/'diagnostic-results.json').read_text());assert len(results['results'])==10
for row in results['results']:
 m,k=row['method_id'],row['case_id'];old=json.loads((c.RUNTIME/'solver-evidence'/f'{m}-{k}'/'oracle-result.json').read_text());new=runner.score(m,k);assert old==new
 assert row['task_correctness_only']==old['task_correctness_only'] and row['authorized_success']==old['authorized_success']
 assert row['worker_reported_total_calls']<=20
for method in ['C0','T0','O0','A0']:
 d=c.RUNTIME/f'create-{method}-D1';assert c.freeze(d/'artifact/package')==c.freeze(d/'artifact/draft-initial')==json.loads((d/'selected-package-inventory.json').read_text())
 assert sum(x['bytes'] for x in c.freeze(d/'artifact/package'))<=2*1024*1024
 assert c.freeze(d/'brief')==json.loads((d/'input-inventory.json').read_text())
 assert c.sha(d/'artifact/package/scripts/normalize_inventory.py')==json.loads((R/f'source-review-{method}.json').read_text())['sha256']
for x in json.loads(codec.decode(json.loads((R/'baseline-source-bundle.json').read_text())))['files']:
 raw=x['content'].encode();assert len(raw)==x['bytes'] and hashlib.sha256(raw).hexdigest()==x['sha256'];assert hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()==x['git_blob_sha']
archive_counts={}
for name in ['runtime-checkpoint-initial.json','runtime-checkpoint.json']:
 raw=codec.decode(json.loads((R/name).read_text()));a=json.loads(raw);seen=set()
 for x in a['files']:
  assert x['path'] not in seen;seen.add(x['path'])
  if x['type']=='file':
   data=x['content'].encode() if x['encoding']=='utf-8' else base64.b64decode(x['content']);assert len(data)==x['bytes'] and hashlib.sha256(data).hexdigest()==x['sha256']
 archive_counts[name]=len(a['files'])
review=json.loads((c.RUNTIME/'qualify-semantics/review.json').read_text());assign={x['id']:x for x in json.loads((c.RUNTIME/'qualify-semantics/assignments.json').read_text())}
assert len(review)==4
for r in review:
 for label in ['input_sha256','output_sha256']:
  assert r[label]==assign[r['id']][label]
  for p,h in r[label].items():assert c.sha(c.RUNTIME/'qualify-semantics'/r['id']/p)==h
primary=[json.loads(s) for s in (R/'primary-unrun-ledger.jsonl').read_text().splitlines()];assert len(primary)==84 and all(r['execution_status']=='not_started' for r in primary)
s=json.loads((R/'supervision-final.json').read_text());assert s['coordinator_active_upper_seconds']<s['setup_limit_seconds'];assert s['storage_bytes_declared_runtime_plus_two_proof_bundles']<s['storage_limit_bytes']
print(json.dumps({'status':'passed','scope':'Local diagnostic evidence consistency, not telemetry/cap certification','fresh_worker_admissions':17,'downstream_scores_reproduced':10,'selected_initial_packages_unchanged':4,'semantic_artifact_hashes_valid':4,'primary_cells_unrun':84,'baseline_blob_identities_verified':26,'archive_entries':archive_counts,'known_timing_limits':['A0 creator reporting interrupted; final call count unavailable.','Semantic notification interval 244s versus 240s cap; actual completion time unknown.']},indent=2))
