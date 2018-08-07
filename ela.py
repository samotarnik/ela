import os
import sys

from PIL import Image
from PIL import ImageChops
from PIL import ImageEnhance


if not len(sys.argv) == 3:
    raise Exception('pass an image as the first argument, quality as the second')


filename = sys.argv[1]
quality = int(sys.argv[2])

basename, extension = os.path.splitext(filename)

resaved = basename + '.resaved.jpg'
ela = basename + '.ela.png'


im = Image.open(filename)
im.save(resaved, 'JPEG', quality=quality)
resaved_im = Image.open(resaved)

ela_im = ImageChops.difference(im, resaved_im)
extrema = ela_im.getextrema()
max_diff = max([ex[1] for ex in extrema])
scale = 255.0/max_diff

ela_im = ImageEnhance.Brightness(ela_im).enhance(scale)

print('Maximum difference was {}'.format(max_diff))
ela_im.save(ela)
# ela_im.show()
