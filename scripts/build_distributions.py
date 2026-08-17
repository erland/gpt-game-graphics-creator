#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json, os, re, shutil, zipfile
ROOT=Path(__file__).resolve().parents[1]; DIST=ROOT/'dist'

def valid(v):
    if not re.fullmatch(r'\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?',v):
        raise SystemExit(f'Ogiltig version: {v}')
    return v

def knowledge():
    t=(ROOT/'builder/UPLOAD-MANIFEST.md').read_text(encoding='utf-8').split('## Add in later prompts')[0]
    fs=list(dict.fromkeys(re.findall(r'`knowledge/([^`]+\.md)`',t)))
    if len(fs)!=13: raise SystemExit(f'Uploadmanifestet anger {len(fs)} aktuella Knowledge-filer, väntat 13')
    for f in fs:
        if not (ROOT/'knowledge'/f).is_file(): raise SystemExit(f'Saknad Knowledge-fil: {f}')
    return fs

def cp(s,d): d.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(s,d)
def cptree(s,d):
    if not s.exists(): return
    for p in s.rglob('*'):
        if p.is_file(): cp(p,d/p.relative_to(s))
def sha(p):
    h=hashlib.sha256()
    with open(p,'rb') as f:
        for b in iter(lambda:f.read(1024*1024),b''): h.update(b)
    return h.hexdigest()
def zdir(s,o):
    with zipfile.ZipFile(o,'w',zipfile.ZIP_DEFLATED) as z:
        for p in sorted(s.rglob('*')):
            if p.is_file():
                i=zipfile.ZipInfo(str(p.relative_to(s)).replace(os.sep,'/')); i.date_time=(2020,1,1,0,0,0); i.compress_type=zipfile.ZIP_DEFLATED; i.external_attr=0o644<<16
                z.writestr(i,p.read_bytes())

def main(v):
    v=valid(v); fs=knowledge(); shutil.rmtree(DIST,ignore_errors=True); DIST.mkdir()
    stage=ROOT/'.build-distributions'; shutil.rmtree(stage,ignore_errors=True); custom=stage/'custom'; chat=stage/'chat'; custom.mkdir(parents=True); chat.mkdir(parents=True)
    # Custom GPT installation package: Builder fields, exact current Knowledge and useful contract templates/schemas.
    for rel in ['README.md','builder/NAME.txt','builder/DESCRIPTION.md','builder/MAIN-INSTRUCTION.md','builder/CONVERSATION-STARTERS.md','builder/CAPABILITIES.md','builder/BUILDER-CONFIGURATION.md','builder/BUILDER-CONFIG.yaml','builder/UPLOAD-MANIFEST.md','knowledge/00-KNOWLEDGE-MANIFEST.md']:
        cp(ROOT/rel,custom/rel)
    for f in fs: cp(ROOT/'knowledge'/f,custom/'knowledge'/f)
    cptree(ROOT/'contract',custom/'contract')
    (custom/'VERSION').write_text(v+'\n',encoding='utf-8')
    # Portable chat
    cp(ROOT/'portable/START-HERE.md',chat/'START-HERE.md'); cp(ROOT/'builder/MAIN-INSTRUCTION.md',chat/'assistant/instructions.md'); cp(ROOT/'builder/CONVERSATION-STARTERS.md',chat/'assistant/conversation-starters.md'); cp(ROOT/'builder/DESCRIPTION.md',chat/'assistant/description.md'); cp(ROOT/'builder/CAPABILITIES.md',chat/'assistant/capabilities.md')
    for f in fs: cp(ROOT/'knowledge'/f,chat/'knowledge'/f)
    cptree(ROOT/'contract',chat/'supporting/contract')
    (chat/'VERSION').write_text(v+'\n',encoding='utf-8')
    hashes={}
    for p in sorted(chat.rglob('*')):
        if p.is_file() and p.name!='MANIFEST.json': hashes[str(p.relative_to(chat)).replace(os.sep,'/')]=sha(p)
    (chat/'MANIFEST.json').write_text(json.dumps({'package':'game-graphics-creator','format':'portable-chat-assistant','version':v,'entrypoint':'START-HERE.md','instructions':'assistant/instructions.md','knowledge_count':13,'files':hashes},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    zdir(custom,DIST/f'game-graphics-creator-custom-gpt-v{v}.zip'); zdir(chat,DIST/f'game-graphics-creator-chat-v{v}.zip'); shutil.rmtree(stage,ignore_errors=True)
if __name__=='__main__':
    a=argparse.ArgumentParser(); a.add_argument('--version'); x=a.parse_args(); main(x.version or (ROOT/'VERSION').read_text().strip())
