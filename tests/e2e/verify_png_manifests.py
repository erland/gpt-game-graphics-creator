#!/usr/bin/env python3
"""Validate real PNG and manifest bytes; no host image-generation claim."""
import argparse,hashlib,json,sys
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parent
LOCKS=('id','footprint','projection','anchor','scale','atlas_slot')
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def check(folder, reference, atlas=None):
 errors=[];results=[]
 def fail(x):errors.append(x)
 def read(p):
  try:return json.loads(p.read_text())
  except Exception as e:fail(f'{p}: {e}');return {}
 base=read(Path(folder));target=read(Path(reference))
 aa={a['id']:a for a in base.get('assets',[])};bb={a['id']:a for a in target.get('assets',[])}
 if set(aa)!=set(bb):fail('Asset IDs changed')
 if not aa:fail('No assets')
 for id in sorted(set(aa)&set(bb)):
  a,b=aa[id],bb[id]
  for k in LOCKS:
   if a.get(k)!=b.get(k):fail(f'{id}: locked field {k} changed')
  file=Path(reference).parent/b.get('file','')
  if not file.is_file():fail(f'{id}: missing PNG {file}');continue
  try:
   with Image.open(file) as im:
    im.verify()
   with Image.open(file) as im:
    if im.format!='PNG' or im.mode!='RGBA':fail(f'{id}: requires RGBA PNG')
    if id=='ground-01':
     if im.size!=(128,64):fail(f'{id}: must be 128x64')
     else:
      al=im.getchannel('A')
      if al.getpixel((0,0))!=0 or al.getpixel((64,32))!=255:fail('Tile diamond mask invalid')
    if b.get('sha256')!=digest(file):fail(f'{id}: SHA256 mismatch')
    results.append({'id':id,'file':str(file),'size':list(im.size),'sha256':digest(file)})
  except Exception as e:fail(f'{id}: image read error: {e}')
 if atlas:
  cfg=read(Path(atlas)); atlaspath=Path(atlas).parent/cfg.get('atlas','')
  try:
   with Image.open(atlaspath) as im:
    if list(im.size)!=cfg['canvas']:fail('Atlas canvas size mismatch')
    for c in cfg.get('cells',[]):
     origin=Path(reference).parent/c['file'];xy=tuple(c['xy']);size=tuple(c['size'])
     with Image.open(origin) as src:
      if src.size!=size or im.crop((xy[0],xy[1],xy[0]+size[0],xy[1]+size[1])).tobytes()!=src.tobytes():fail('Atlas cell differs: '+c['id'])
    if cfg['margin']!=8 or cfg['spacing']!=8:fail('Atlas margins/spacing mismatch')
  except Exception as e:fail(f'Atlas read error: {e}')
 return {'status':'PASS' if not errors else 'FAIL','errors':errors,'assets_checked':results,'scope':'ACTUAL_FILE_BYTES_ONLY_NOT_HOST_TEST'}
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--baseline',default=str(ROOT/'fixtures/prototype-manifest.json'));ap.add_argument('--candidate',default=str(ROOT/'fixtures/upgrade-manifest.json'));ap.add_argument('--atlas',default=str(ROOT/'reference-outputs/atlas-layout.json'));ap.add_argument('--output');args=ap.parse_args()
 result=check(args.baseline,args.candidate,args.atlas)
 if args.output:Path(args.output).write_text(json.dumps(result,indent=2)+'\n')
 print(json.dumps(result,indent=2));return 0 if result['status']=='PASS' else 1
if __name__=='__main__':sys.exit(main())
