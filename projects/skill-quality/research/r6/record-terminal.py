"""Record a reported terminal state and deterministic diagnostic score."""
import importlib.util, sys
import coordinator as c
spec=importlib.util.spec_from_file_location('runner',c.ROOT/'diagnostic-runner.py');r=importlib.util.module_from_spec(spec);spec.loader.exec_module(r)
method,case,calls,start,stop,outcome=sys.argv[1:7]
result=r.score(method,case)
c.append({'attempt_id':f'solve-{method}-{case}-diagnostic','phase':'downstream','state':'terminal','at_utc':c.now(),'outcome':outcome,'task_correctness_only':result['task_correctness_only'],'authorized_success':result['authorized_success'],'worker_reported_total_calls':None if calls=='null' else int(calls),'authoritative_worker_tool_calls':None,'admission_observed_utc':start,'terminal_message_observed_utc':stop,'oracle_result':f'solver-evidence/{method}-{case}/oracle-result.json','fallback_used':False,'retry_count':0})
print({'method':method,'case':case,'artifact':result['task_correctness_only'],'authorized':result['authorized_success']})
if len(sys.argv)>7:c.append({'attempt_id':sys.argv[7],'phase':'downstream','state':'running','at_utc':c.now()})
