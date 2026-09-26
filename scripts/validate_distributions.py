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
        if rd(z,'builder/MAIN-INSTRUCTION.md')!=(ROOT/'assistant/instructions.md').read_bytes():
            raise SystemExit('Custom instruktion avviker från canonical källa')
        if rd(z,'builder/CONVERSATION-STARTERS.md')!=(ROOT/'builder/CONVERSATION-STARTERS.md').read_bytes():
            raise SystemExit('Custom starters avviker')
        for f in kfiles():
            if rd(z,'knowledge/'+f)!=(ROOT/'knowledge'/f).read_bytes(): raise SystemExit(f'Custom Knowledge avviker: {f}')
        if rd(z,'VERSION').decode().strip()!=v: raise SystemExit('Fel VERSION i custom')
        custom_instr=rd(z,'builder/MAIN-INSTRUCTION.md').decode('utf-8')
        for marker in [
            'Separate visual quality from technical validity.',
            'Measure actual files.',
            'Use image generation for visual creation or editing and Code Interpreter & Data Analysis for measurable file operations',
            'Never claim that a capability ran when it was unavailable or not used.',
        ]:
            if marker not in custom_instr:
                raise SystemExit(f'Custom GPT saknar kritisk beteendemarkör: {marker}')
    with zipfile.ZipFile(p) as z:
        if rd(z,'assistant/instructions.md')!=(ROOT/'assistant/instructions.md').read_bytes(): raise SystemExit('Portable instruktion avviker från canonical källa')
        if rd(z,'assistant/conversation-starters.md')!=(ROOT/'builder/CONVERSATION-STARTERS.md').read_bytes(): raise SystemExit('Portable starters avviker')
        for f in kfiles():
            if rd(z,'knowledge/'+f)!=(ROOT/'knowledge'/f).read_bytes(): raise SystemExit(f'Portable Knowledge avviker: {f}')
        chat_instr=rd(z,'assistant/instructions.md').decode('utf-8')
        for marker in [
            'Separate visual quality from technical validity.',
            'Measure actual files.',
            'Use image generation for visual creation or editing and Code Interpreter & Data Analysis for measurable file operations',
            'Never claim that a capability ran when it was unavailable or not used.',
        ]:
            if marker not in chat_instr:
                raise SystemExit(f'Chat saknar kritisk beteendemarkör: {marker}')
        m=json.loads(rd(z,'MANIFEST.json')); 
        if m['version']!=v or m['knowledge_count']!=13: raise SystemExit('Fel portable manifest')
        for n,h in m['files'].items():
            if hb(rd(z,n))!=h: raise SystemExit(f'Hashfel: {n}')
    print(f'OK: båda distributionerna för v{v} är validerade.')
if __name__=='__main__':
    a=argparse.ArgumentParser(); a.add_argument('--version'); x=a.parse_args(); main(x.version or (ROOT/'VERSION').read_text().strip())
