from PIL import Image, ImageDraw

import random

W = 500
im = Image.new('RGB', (W, W))
NCOLORS = 19
COLORS = []

def get_origin_point():
  return [random.randint(0, W-1), random.randint(0, W-1)]
  
def get_vector():
  return [random.randint(0.3*W, 0.6*W), random.randint(0.3*W, 0.6*W)]

def draw_one_line(draw):
  op = get_origin_point()
  vec = get_vector()
  tu = tuple(op + vec)
  for i in range(NCOLORS):
    draw.line(tu, fill=COLORS[i], width=NCOLORS-i)

def draw_lines(draw):
  for i in range(30):
    draw_one_line(draw)

def init_colors(ncolors):
  v = 255.0
  for i in range(ncolors):
    COLORS.append((0, int(v), 0))
    v *= 0.80
  COLORS.reverse()

init_colors(NCOLORS)
draw = ImageDraw.Draw(im)
red = (255, 0, 0)
draw_lines(draw)

im.save('f.png')

