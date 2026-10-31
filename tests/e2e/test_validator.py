import json,subprocess,sys,tempfile,unittest
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT))
from verify_png_manifests import check
class TestRealFiles(unittest.TestCase):
 def setUp(self):
  self.baseline=ROOT/'fixtures/prototype-manifest.json';self.candidate=ROOT/'fixtures/upgrade-manifest.json';self.atlas=ROOT/'reference-outputs/atlas-layout.json'
 def test_valid_images_and_atlas(self):self.assertEqual(check(self.baseline,self.candidate,self.atlas)['status'],'PASS')
 def test_locked_anchor_rejected(self):
  with tempfile.TemporaryDirectory() as td:
   p=Path(td)/'changed.json';data=json.loads(self.candidate.read_text());data['assets'][0]['anchor']=[0,0];p.write_text(json.dumps(data))
   self.assertIn('locked field anchor',str(check(self.baseline,p)['errors']))
 def test_missing_png_rejected(self):
  with tempfile.TemporaryDirectory() as td:
   p=Path(td)/'changed.json';data=json.loads(self.candidate.read_text());data['assets'][0]['file']='nonexistent.png';p.write_text(json.dumps(data))
   self.assertEqual(check(self.baseline,p)['status'],'FAIL')
 def test_checksum_mismatch_rejected(self):
  with tempfile.TemporaryDirectory(dir=ROOT/'fixtures') as td:
   p=Path(td)/'changed.json';data=json.loads(self.candidate.read_text());data['assets'][0]['sha256']='0'*64
   # use a relative path back to the true file from temporary directory
   for a in data['assets']:a['file']='../'+a['file']
   p.write_text(json.dumps(data));self.assertTrue(any('SHA256 mismatch' in x for x in check(self.baseline,p)['errors']))
if __name__=='__main__':unittest.main()
