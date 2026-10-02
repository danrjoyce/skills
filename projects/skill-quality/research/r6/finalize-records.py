"""Derive bounded diagnostic summaries from retained observations, without new trials."""
import importlib.util, json
from datetime import datetime, timezone
from pathlib import Path
import coordinator as c
from common import inventory
R=c.ROOT
rows=[json.loads(x) for x in (R/'journal.jsonl').read_text().splitlines()]
latest={x['attempt_id']:x for x in rows if 'attempt_id' in x}
order=json.loads((R/'diagnostic-order.json').read_text())['downstream']
results=[]
for o in order:
 m,k=o['method_id'],o['case_id'];t=latest[f'solve-{m}-{k}-diagnostic'];assert t['state']=='terminal'
 e=c.RUNTIME/'solver-evidence'/f'{m}-{k}';oracle=json.loads((e/'oracle-result.json').read_text())
 results.append({'method_id':m,'case_id':k,'order_index':o['order_index'],'task_correctness_only':oracle['task_correctness_only'],'authorized_success':oracle['authorized_success'],'predicates':oracle['predicates'],'worker_reported_total_calls':t['worker_reported_total_calls'],'wall_seconds_admission_to_observed_terminal':(datetime.fromisoformat(t['terminal_message_observed_utc'].replace('Z','+00:00'))-datetime.fromisoformat(t['admission_observed_utc'].replace('Z','+00:00'))).total_seconds(),'final_inventory':json.loads((e/'final-inventory.json').read_text()),'real_adapter_read_count':len((e/'read-events.jsonl').read_text().splitlines()),'oracle_sha256':c.sha(e/'oracle-result.json'),'worker_report_sha256':c.sha(e/'worker-report.json') if (e/'worker-report.json').exists() else None,'trace_coverage':'partial','fallback_used':False,'physical_worker_starts':1})
summary=[]
for method in ['N0','T0','O0','A0','C0']:
 rr=[x for x in results if x['method_id']==method];assert len(rr)==2
 summary.append({'method':method,'assigned_cases':2,'observed_cases':len(rr),'artifact_passes':sum(x['task_correctness_only']=='pass' for x in rr),'artifact_failures':sum(x['task_correctness_only']=='fail' for x in rr),'authorized_success_lower':sum(x['authorized_success']=='pass' for x in rr),'authorized_success_upper':sum(x['authorized_success']!='fail' for x in rr),'worker_reported_downstream_calls':sum(x['worker_reported_total_calls'] for x in rr) if all(x['worker_reported_total_calls'] is not None for x in rr) else None,'observed_downstream_wall_seconds':sum(x['wall_seconds_admission_to_observed_terminal'] for x in rr)})
c.save(R/'diagnostic-results.json',{'scope':'explicit_load_diagnostic only; two public D1 cases per method; not primary or native performance','denominator_fixed':10,'results':results,'by_method':summary,'limits':['Not independent repeated creations or reliability estimates.','Actual serving model, token/cost and complete action telemetry unavailable.','Worker reports are attributed; only adapter reads have real byte-hashed events.','No fallback or technical rerun was used.']})
starts=[x['attempt_id'] for x in rows if x.get('state')=='running'];assert len(starts)==len(set(starts))
now=datetime.now(timezone.utc);wall=(now-datetime.fromisoformat('2026-10-02T17:15:34+00:00')).total_seconds();wait=480+sum(x.get('seconds',0) for x in rows if x.get('event')=='completed_coordinator_wait')
storage=sum(p.stat().st_size for root in [c.RUNTIME,Path('/tmp/r6-proof-a'),Path('/tmp/r6-proof-b')] for p in root.rglob('*') if p.is_file() and not p.is_symlink())
c.save(R/'supervision-final.json',{'observed_at_utc':now.isoformat(),'campaign_started_at_utc':'2026-10-02T17:15:34+00:00','confirmed_fresh_worker_start_ids':starts,'confirmed_fresh_worker_starts':len(starts),'additional_same_creator_resume_turns':1,'campaign_wall_seconds':wall,'completed_explicit_wait_seconds_deducted':wait,'coordinator_active_upper_seconds':wall-wait,'coordinator_exact_active_seconds':None,'setup_limit_seconds':7200,'campaign_total_limit_seconds':36960,'scheduling_stop_seconds':39600,'storage_bytes_declared_runtime_plus_two_proof_bundles':storage,'storage_limit_bytes':250*1024*1024,'authoritative_global_tool_calls':None,'model_identifier':None,'tokens':None,'dollar_equivalent_cost':None,'new_external_spend_usd':0,'sequential_status':'One substantive worker observed at a time; A0 paused for one development solver and then resumed. A0 interrupted at deadline. No authoritative per-boundary process trace.','upper_bound_method':'All elapsed coordinator wall time since original campaign start charged except explicitly completed logged waits, including prior 480 seconds. Unknown publication stall and context gap remain charged. Includes worker/coordinator overlap outside waits.','limits':'Setup upper bound is conservative rather than exact active time. All-call cap remains unverified. A0 final author call count unavailable after interruption.'})
manifest=json.loads((R/'actual-run-manifest.json').read_text());manifest.update({'diagnostic_status':'completed_bounded_diagnostic_with_report_cutoff','completed_creator_episodes':4,'creator_reporting_interrupted':1,'completed_downstream_episodes':10,'completed_semantic_qualifications':1,'confirmed_worker_starts':len(starts),'development_solver_starts':1,'primary_started_cells':0,'primary_status':'methodology_gated_unrun','finalized_at_utc':now.isoformat()});c.save(R/'actual-run-manifest.json',manifest)
# Human-readable exact selected sources separate from the compressed full runtime.
packages=[]
for method in ['C0','T0','O0','A0']:
 d=c.RUNTIME/f'create-{method}-D1';inv=json.loads((d/'selected-package-inventory.json').read_text());assert inventory(d/'artifact/package')==inv
 packages.append({'method':method,'selected_inventory':inv,'files':[dict(x,encoding='utf-8',content=(d/'artifact/package'/x['path']).read_text()) for x in inv]})
c.save(R/'selected-packages.json',{'format':'exact-selected-synthetic-packages-v1','packages':packages})
print(json.dumps({'summary':summary,'starts':len(starts),'setup_upper_seconds':wall-wait,'storage_bytes':storage},indent=2))
