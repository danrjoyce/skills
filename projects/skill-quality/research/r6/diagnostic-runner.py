"""Diagnostic staging, freezing and scoring only; no model or generated-code execution."""
import hashlib, json, shutil, sys
from pathlib import Path
import coordinator as c
from common import inventory, json_text
from adapter import Adapter
from oracles import evaluate
R=c.ROOT
FIX=Path('/tmp/r6-proof-a/fixtures')

def canonical(rows):
 return hashlib.sha256(json.dumps(rows,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()

def check_frozen():
 for filename,base in [('candidate-freeze.json',R.parent.parent/'candidate/evidence-skill-creator'),('support-freeze.json',R.parent/'r5')]:
  data=json.loads((R.parent/'r5'/filename).read_text())
  for x in data['files']:
   p=base/x['path']; assert p.stat().st_size==x['bytes'] and c.sha(p)==x['sha256'],str(p)
 before=json.loads(Path('/tmp/r6-proof-a/inventory.json').read_text())
 # Qualification inventory format is read explicitly by the caller; compare all retained files.
 if isinstance(before,dict): before=before['files']
 for x in before:
  p=Path('/tmp/r6-proof-a')/x['path'];assert c.sha(p)==x['sha256'],str(p)
 return {'checked_at_utc':c.now(),'candidate_and_support_frozen':True,'trusted_bundle_frozen':True}

def freeze_creator(method):
 d=c.RUNTIME/f'create-{method}-D1'; assert inventory(d/'brief')==json.loads((d/'input-inventory.json').read_text())
 rows=inventory(d/'artifact/package'); assert sum(x['bytes'] for x in rows)<=2*1024*1024
 c.save(d/'selected-package-inventory.json',rows)
 meta=Adapter({'assigned_package':d/'artifact/package'},d/'freeze-no-reads.jsonl').catalog()
 return {'method':method,'files':len(rows),'bytes':sum(x['bytes'] for x in rows),'sha256':canonical(rows),'metadata':meta}

def stage(method,case):
 check_frozen()
 d=c.stage_solver(method,case)
 e=c.RUNTIME/'solver-evidence'/f'{method}-{case}';e.mkdir(parents=True)
 support=c.RUNTIME/'solver-support'/f'{method}-{case}'; support.mkdir(parents=True)
 names=sorted(p.name for p in (FIX/'catalog').iterdir())
 mapping={}
 for i,name in enumerate(names):
  if i==2 and method!='N0':
   src=c.RUNTIME/f'create-{method}-D1/artifact/package'; dst=support/'assigned-package';shutil.copytree(src,dst)
   assert inventory(dst)==json.loads((c.RUNTIME/f'create-{method}-D1/selected-package-inventory.json').read_text())
   mapping['assigned_package']=str(dst)
  dst=support/name;shutil.copytree(FIX/'catalog'/name,dst);mapping[name]=str(dst)
 c.save(e/'catalog.json',mapping);c.save(e/'catalog-metadata.json',Adapter(mapping,e/'read-events.jsonl').catalog());(e/'read-events.jsonl').write_text('')
 c.save(e/'starting-inventory.json',inventory(d));c.save(e/'trusted-case-inventory.json',inventory(FIX/'cases'/case));c.save(e/'support-inventory.json',inventory(support))
 common=f'''You are a fresh-context solver in a bounded synthetic evaluation. Solve the task in {d}/task.md using only its staged inputs and permitted local tools. Keep all inputs unchanged and write only the output files authorized by the task and input contract. Do not inspect other cases, evaluator material, creators, other methods, or unrelated files. No network, external model calls, accounts, installation, credentials, publishing, or delegation. Do not modify packages. The shared filesystem is not an isolation boundary. Use the assigned skill policy below; do not substitute an installed private task-specific skill. Any background capability loading must be reported by category without copying private instructions.\nBudget: at most four minutes and 20 total worker tool calls, counting leaf tools and orchestration calls conservatively. No retry after evaluation and no score feedback will be provided. Inspect exact source before executing code you write. The already reviewed assigned helper, if any, is permitted only on the staged synthetic inputs and declared outputs; this permission is not a sandbox or general security certification. If unsupported or blocked, retain that outcome rather than silently changing the task.\nCatalog metadata: {e}/catalog-metadata.json. Catalog adapter: python -B {c.SUPPORT}/adapter.py {e}/catalog.json --log {e}/read-events.jsonl. For a resource read add --load PACKAGE_ID --resource RELATIVE_PATH --explicit. All methods have the same three neutral catalog entries and inherited background capabilities.\n'''
 if method=='N0':common+='Assigned policy: no added task-specific package. Solve directly using the staged task and inputs.\n'
 else:common+='Assigned policy: explicitly load assigned_package with the adapter before solving: add --load assigned_package --explicit. Resolve its resources with the same adapter. This measures explicit-load use, not natural activation.\n'
 common+=f'''Keep any report outside the task directory. Save an attributed JSON report at {e}/worker-report.json with what you did, commands/results actually observed, completion or failure, self-reported leaf/orchestration counts and limits. Do not fabricate a complete trace or exact model/token/cost data. Return a concise result and report path.\n'''
 (e/'prompt.txt').write_text(common)
 ident=f'solve-{method}-{case}-diagnostic'
 c.append({'attempt_id':ident,'phase':'downstream','state':'planned','method':method,'case_id':case,'prompt_sha256':c.sha(e/'prompt.txt'),'input_manifest_sha256':c.sha(FIX/'cases'/case/'fixture.json'),'input_inventory_sha256':c.sha(e/'starting-inventory.json'),'max_seconds':240,'max_worker_tool_calls':20})
 return {'episode':str(d),'evidence':str(e),'prompt':str(e/'prompt.txt')}

def score(method,case):
 e=c.RUNTIME/'solver-evidence'/f'{method}-{case}';d=c.RUNTIME/f'solve-{method}-{case}';trusted=FIX/'cases'/case
 assert inventory(trusted)==json.loads((e/'trusted-case-inventory.json').read_text());check_frozen()
 raw=[json.loads(s) for s in (e/'read-events.jsonl').read_text().splitlines() if s.strip()]
 events=[dict(x,id=f'adapter-read-{i+1}') for i,x in enumerate(raw)]
 trace={'coverage':'partial','evidence_label':'adapter_read_observation','events':events,'limits':['Only real adapter reads are represented. Worker commands/reports are attributed separately; no complete action trace is available.']}
 c.save(e/'trace.json',trace)
 result=evaluate(d,trace=trace,trusted_case=trusted); c.save(e/'oracle-result.json',result)
 assert inventory(trusted)==json.loads((e/'trusted-case-inventory.json').read_text());check_frozen()
 c.save(e/'final-inventory.json',inventory(d))
 assert inventory(c.RUNTIME/'solver-support'/f'{method}-{case}')==json.loads((e/'support-inventory.json').read_text())
 return result

if __name__=='__main__':
 command=sys.argv[1]
 if command=='check':result=check_frozen()
 elif command=='freeze':result=freeze_creator(sys.argv[2])
 elif command=='stage':result=stage(sys.argv[2],sys.argv[3])
 elif command=='score':result=score(sys.argv[2],sys.argv[3])
 else:raise ValueError(command)
 print(json_text(result))
