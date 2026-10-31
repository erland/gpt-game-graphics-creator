#!/usr/bin/env python3
"""Non-host static evidence for G01-G16. Never interprets these as host PASS."""
import json,re,zipfile,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sources=[ROOT/'canonical/core.md', ROOT/'canonical/skills/graphics-creation/behavior.md',ROOT/'canonical/skills/asset-production/behavior.md']
text='\n'.join(p.read_text() for p in sources).lower()
checks={
'G01':['design sheet','production ready'],
'G02':['128','64','tile'],
'G03':['footprint','anchor','canvas'],
'G04':['footprint','manifest','anchor'],
'G05':['incompatible','slicing'],
'G06':['directions','frame','foot point'],
'G07':['frame order','fps','looping'],
'G08':['alpha','localization'],
'G09':['layer','camera'],
'G10':['design sheet','deterministic'],
'G11':['spacing','margin','deterministic'],
'G12':['revis','approved','version'],
'G13':['swedish','english'],
'G14':['localiz','text'],
'G15':['not verified','external'],
'G16':['visual upgrade','projection','anchor'],
}
results={}
for id,terms in checks.items():
    file=ROOT/'tests'/f'{id}.md'
    exists=file.exists()
    absent=[t for t in terms if t not in text]
    results[id]={'test_file':exists,'static_contract_terms':terms,'missing_terms':absent,'static_status':'supported' if exists and not absent else 'review_required','host_execution':'not_run','functional_result':'not_verified'}
archives={}
for f in sorted((ROOT/'dist').glob('*.zip')):
    with zipfile.ZipFile(f) as z:
        error=z.testzip()
        archives[f.name]={'sha256':hashlib.sha256(f.read_bytes()).hexdigest(),'integrity':'PASS' if error is None else 'FAIL','files':len(z.namelist())}
output={'scope':'STATIC_ONLY_NOT_A_RUNTIME_TEST','source_files':[str(s.relative_to(ROOT)) for s in sources], 'cases':results,'archives':archives}
out=ROOT/'docs/evidence/G01-G16-static-evidence.json'
out.parent.mkdir(exist_ok=True,parents=True)
out.write_text(json.dumps(output,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({'supported':sum(x['static_status']=='supported' for x in results.values()),'review_required':[k for k,v in results.items() if v['static_status']!='supported'],'archives_checked':len(archives),'archive_integrity':all(a['integrity']=='PASS' for a in archives.values())}))
