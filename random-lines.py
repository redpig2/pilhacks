# On some systems, need to import like this:
# import Image
# import ImageDraw

# On others, import like this:
from PIL import Image, ImageDraw

import random

W = 100
im = Image.new('RGB', (W, W))

def get_origin_point():
  return [random.randint(0, W-1), random.randint(0, W-1)]
  
def get_vector():
  return [random.randint(0.3*W, 0.6*W), random.randint(0.3*W, 0.6*W)]

def draw_one_line(draw):
  draw.line(tuple(get_origin_point() + get_vector()), fill=red)

def draw_lines(draw):
  for i in range(30):
    draw_one_line(draw)

draw = ImageDraw.Draw(im)
red = (255, 0, 0)
draw_lines(draw)

im.save('f.png')

