#!/usr/bin/env python3

from pathlib import Path
from PIL import Image

paths = Path("/images").glob("*")
path2 = './opt/icons/'

for img in paths:
    if img.is_file():
       with Image.open(img) as imagem:
           img = str(img).split('/')
           img = img[1] + '.jpeg'
           imagem = imagem.convert('RGB')
           imagem.rotate(270).resize((128, 128)).save("{}{}".format(path2, img))

