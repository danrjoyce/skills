"""R6 evidence preparation only. Does not invoke, contain, or supervise a model."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, shutil, sys
ROOT=Path(__file__).resolve().parent
RUNTIME=Path('/workspace/scratch/7a0d3a848439/r6-runtime')
SUPPORT=ROOT.parent/'r5/support'
sys.path.insert(0,str(SUPPORT))
from common import inventory, json_text

def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def now(): return datetime.now(timezone.utc).isoformat()
def save(p,obj): Path(p).write_text(json_text(obj))
def append(row):
 with (ROOT/'journal.jsonl').open('a') as f: f.write(json.dumps(row,sort_keys=True)+'\n')
def freeze(path): return inventory(Path(path))
def stage_creator(method):
 d=RUNTIME/('create-'+method+'-D1'); d.mkdir()
 shutil.copytree('/tmp/r6-proof-a/fixtures/briefs/D1',d/'brief')
 (d/'artifact').mkdir(); (d/'read-events.jsonl').write_text('')
 save(d/'input-inventory.json',freeze(d/'brief'))
 return d
def stage_solver(method,case):
 d=RUNTIME/f'solve-{method}-{case}'; d.mkdir()
 trusted=Path('/tmp/r6-proof-a/fixtures/cases')/case
 for p in trusted.iterdir():
  if p.name in ['oracle','fixture.json']: continue
  if p.is_dir(): shutil.copytree(p,d/p.name)
  else: shutil.copy2(p,d/p.name)
 return d
if __name__=='__main__':
 if sys.argv[1]=='stage-creator': print(stage_creator(sys.argv[2]))
 elif sys.argv[1]=='stage-solver': print(stage_solver(sys.argv[2],sys.argv[3]))
