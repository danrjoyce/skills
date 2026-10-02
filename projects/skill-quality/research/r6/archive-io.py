"""Encode/decode exact JSON evidence bytes; never extract or execute archived files."""
import argparse, base64, gzip, hashlib, json
from pathlib import Path

def encode(data):
    compressed=gzip.compress(data,mtime=0)
    return {'format':'r6-exact-json-archive-envelope-v1','encoding':'gzip+base64','uncompressed_bytes':len(data),'uncompressed_sha256':hashlib.sha256(data).hexdigest(),'compressed_sha256':hashlib.sha256(compressed).hexdigest(),'content':base64.b64encode(compressed).decode('ascii'),'instructions':'Decode with archive-io.py decode INPUT OUTPUT. This yields the exact archived JSON; directory/symlink entries are metadata, not permission to follow or execute them.'}

def decode(obj):
    assert obj['format']=='r6-exact-json-archive-envelope-v1'
    assert 0<=obj['uncompressed_bytes']<=250*1024*1024
    data=base64.b64decode(obj['content'],validate=True)
    assert hashlib.sha256(data).hexdigest()==obj['compressed_sha256']
    raw=gzip.decompress(data)
    assert len(raw)==obj['uncompressed_bytes'] and hashlib.sha256(raw).hexdigest()==obj['uncompressed_sha256']
    json.loads(raw)
    return raw

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('mode',choices=['encode','decode']);p.add_argument('input',type=Path);p.add_argument('output',type=Path);a=p.parse_args()
    if a.mode=='encode':
        raw=a.input.read_bytes();json.loads(raw);out=(json.dumps(encode(raw),sort_keys=True,indent=2)+'\n').encode()
    else:out=decode(json.loads(a.input.read_text()))
    with a.output.open('xb') as stream:stream.write(out)
    print(json.dumps({'output':str(a.output),'bytes':len(out),'sha256':hashlib.sha256(out).hexdigest()}))
