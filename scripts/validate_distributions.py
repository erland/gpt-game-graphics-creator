#!/usr/bin/env python3
from pathlib import Path
import argparse, hashlib, json, re, zipfile
ROOT=Path(__file__).resolve().parents[1]; DIST=ROOT/'dist'
def kfiles():
    t=(ROOT/'builder/UPLOAD-MANIFEST.md').read_text(encoding='utf-8').split('## Add in later prompts')[0]
    return list(dict.fromkeys(re.findall(r'`knowledge/([^`]+\.md)`',t)))
def rd(z,n):
    try:return z.read(n)
    except KeyError: raise SystemExit(f'Saknad fil i zip: {n}')
def hb(b): return hashlib.sha256(b).hexdigest()
def main(v):
    if len(kfiles())!=13: raise SystemExit('Aktuellt uploadmanifest ska innehålla exakt 13 Knowledge-filer')
    c=DIST/f'game-graphics-creator-custom-gpt-v{v}.zip'; p=DIST/f'game-graphics-creator-chat-v{v}.zip'
    for x in [c,p]:
        if not x.is_file(): raise SystemExit(f'Saknad: {x.name}')
        with zipfile.ZipFile(x) as z:
            if z.testzip(): raise SystemExit(f'Korrupt zip: {x.name}')
    with zipfile.ZipFile(c) as z:
        for rel in ['builder/MAIN-INSTRUCTION.md','builder/CONVERSATION-STARTERS.md']:
            if rd(z,rel)!=(ROOT/rel).read_bytes(): raise SystemExit(f'Custom avviker: {rel}')
        for f in kfiles():
            if rd(z,'knowledge/'+f)!=(ROOT/'knowledge'/f).read_bytes(): raise SystemExit(f'Custom Knowledge avviker: {f}')
        if rd(z,'VERSION').decode().strip()!=v: raise SystemExit('Fel VERSION i custom')
    with zipfile.ZipFile(p) as z:
        if rd(z,'assistant/instructions.md')!=(ROOT/'builder/MAIN-INSTRUCTION.md').read_bytes(): raise SystemExit('Portable instruktion avviker')
        if rd(z,'assistant/conversation-starters.md')!=(ROOT/'builder/CONVERSATION-STARTERS.md').read_bytes(): raise SystemExit('Portable starters avviker')
        for f in kfiles():
            if rd(z,'knowledge/'+f)!=(ROOT/'knowledge'/f).read_bytes(): raise SystemExit(f'Portable Knowledge avviker: {f}')
        m=json.loads(rd(z,'MANIFEST.json')); 
        if m['version']!=v or m['knowledge_count']!=13: raise SystemExit('Fel portable manifest')
        for n,h in m['files'].items():
            if hb(rd(z,n))!=h: raise SystemExit(f'Hashfel: {n}')
    print(f'OK: båda distributionerna för v{v} är validerade.')
if __name__=='__main__':
    a=argparse.ArgumentParser(); a.add_argument('--version'); x=a.parse_args(); main(x.version or (ROOT/'VERSION').read_text().strip())
