"""Replay mechanical scores from curated public synthetic evidence; no model/code execution."""
import hashlib, json, sys, tempfile
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent.parent/'r5/support'))
from oracles import evaluate
from common import safe_path
root=Path(__file__).resolve().parent
rows=json.loads((root/'case-artifacts.json').read_text())['episodes']
with tempfile.TemporaryDirectory(prefix='r6-public-replay-') as tmp:
 for n,row in enumerate(rows):
  episode=Path(tmp)/str(n)/'episode';trusted=Path(tmp)/str(n)/'trusted';episode.mkdir(parents=True);trusted.mkdir()
  for base,key in [(episode,'episode_files'),(trusted,'trusted_fixture_files')]:
   for item in row[key]:
    assert item['encoding']=='utf-8';data=item['content'].encode();assert len(data)==item['bytes'] and hashlib.sha256(data).hexdigest()==item['sha256']
    p=safe_path(base,item['path']);p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
  result=evaluate(episode,trace=row['trace'],trusted_case=trusted)
  assert result==row['oracle_result'],(row['method'],row['case'])
print(json.dumps({'status':'passed','replayed_mechanical_reports':len(rows),'scope':'Curated exact synthetic artifacts only; no complete trace or independent replication claim.'},indent=2))
