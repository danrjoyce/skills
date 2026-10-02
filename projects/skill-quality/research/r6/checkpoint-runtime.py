"""Archive only the declared synthetic R6 runtime, without following symlinks."""
import base64, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RUNTIME = Path('/workspace/scratch/7a0d3a848439/r6-runtime')

def archive(root):
    rows=[]
    for p in sorted(root.rglob('*')):
        rel=p.relative_to(root).as_posix()
        if p.is_symlink():
            rows.append({'path':rel,'type':'symlink','target':str(p.readlink())})
        elif p.is_file():
            data=p.read_bytes()
            try:
                content=data.decode('utf-8'); encoding='utf-8'
            except UnicodeDecodeError:
                content=base64.b64encode(data).decode('ascii'); encoding='base64'
            rows.append({'path':rel,'type':'file','bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'encoding':encoding,'content':content})
        elif p.is_dir():
            rows.append({'path':rel,'type':'directory'})
        else:
            raise ValueError('Unexpected special file: '+rel)
    return {'format':'r6-synthetic-runtime-archive-v1','scope':'Declared synthetic runtime only. No hidden host prompts or unrelated workspace content.','files':rows}

if __name__=='__main__':
    target=ROOT/'runtime-checkpoint.json'
    target.write_text(json.dumps(archive(RUNTIME),sort_keys=True,indent=2,ensure_ascii=True)+'\n')
    print(target)
