from PIL import Image
from pathlib import Path
import sys



def standalize_img(path):
    image = Image.open(path)
    path = Path(path)
    new_image = image.resize((512, 512))
    new_image.save(dst_prnt/path.name)


src_prnt = Path(sys.argv[1])
dst_prnt = Path(f'{src_prnt} - modified')
dst_prnt.mkdir()
for son in src_prnt.glob('*'):
    if son.is_file():
        standalize_img(son)
