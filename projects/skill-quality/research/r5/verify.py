#!/usr/bin/env python3
"""R5 static freeze/provenance checks. No creator/model execution or network."""
import ast
import importlib.util
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'support'))
from common import digest, inventory, json_text, read_json, sha
from adapter import Adapter


def tree_sha(rows):
    return sha(json.dumps(rows,sort_keys=True,separators=(',',':'),ensure_ascii=False,allow_nan=False).encode())


def main():
    package=ROOT.parents[1]/'candidate/evidence-skill-creator'
    freeze=read_json(ROOT/'candidate-freeze.json')
    current=inventory(package)
    assert current==freeze['files'],'Candidate bytes differ from freeze'
    assert tree_sha(current)==freeze['tree_sha256'],'Candidate tree identity differs'
    original=read_json(ROOT/'candidate-freeze-original.json')
    assert tree_sha(original['files'])==original['tree_sha256'],'Original inventory identity differs'
    before={r['path']:r for r in original['files']};after={r['path']:r for r in current}
    assert [p for p in before if before[p]!=after[p]]==['scripts/inspect_package.py'],'Undisclosed candidate revision'
    support=read_json(ROOT/'support-freeze.json')
    observed=[r for r in inventory(ROOT) if r['path']=='verify.py' or (r['path'].startswith(('support/','tests/')) and r['path'].endswith('.py'))]
    assert observed==support['files'] and tree_sha(observed)==support['tree_sha256'],'Support bytes differ from freeze'
    protected=read_json(ROOT/'preserved-inputs.json')
    for row in protected['files']:
        assert digest(ROOT.parents[1]/row['path'])==row['sha256'],'Historical input changed: '+row['path']
    for path in list(package.rglob('*.py'))+list(ROOT.rglob('*.py')):
        ast.parse(path.read_text(),filename=path.name)
    for path in ROOT.rglob('*.json'):
        read_json(path)
    spec=importlib.util.spec_from_file_location('inspector',package/'scripts/inspect_package.py')
    inspector=importlib.util.module_from_spec(spec);spec.loader.exec_module(inspector)
    inspection=inspector.inspect(package)
    assert not inspection['errors'] and not inspection['manual_checks'],'Candidate static inspection failed'
    # Catalog parsing reads metadata only; the unused log path is never opened.
    catalog=Adapter({'candidate':package},ROOT/'unused-verification-log.jsonl').catalog()
    assert catalog[0]['invocation']=='model_invocable'
    assert sum(r['bytes'] for r in current)<2*1024*1024
    q=read_json(ROOT/'qualification.json')
    assert q['model_trials']==q['native_runtime_trials']==0
    assert len(q['calibration_controls'])==12 and all(r['repeat_equal'] and r['expected']==r['observed'] for r in q['calibration_controls'])
    assert len(q['instrument_replays'])==11 and all(r['expected']==r['observed'] for r in q['instrument_replays'])
    assert len(q['routing_annotation_controls'])==6 and all(r['expected']==r['observed'] for r in q['routing_annotation_controls'])
    print(json_text({'status':'passed','scope':'R5 static freezes, syntax, metadata and recorded control consistency',
          'candidate_files':len(current),'candidate_bytes':sum(r['bytes'] for r in current),
          'candidate_tree_sha256':tree_sha(current),'support_files':len(observed),
          'preserved_historical_files':len(protected['files']),'model_trials':0,
          'limits':['Control consistency is not an independent rerun; use unit tests and qualify.py.',
                    'No native compatibility, live semantic grader or comparative performance finding.']}))


if __name__=='__main__':
    main()
