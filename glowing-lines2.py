from PIL import Image, ImageDraw

import random

W = 500
im = Image.new('RGB', (W, W))
NCOLORS = 19
NLINES = 15

def filled_circle(draw, x, y, r, fill):
  draw.ellipse((x-r, y-r, x+r, y+r), fill=fill)

def make_line_mask(im):
  mask = Image.new('L', im.size, color=0)

  grays = []
  v = 255.0
  for i in range(NCOLORS):
    grays.append(int(v))
    v *= 0.91
  grays.reverse()

  draw=ImageDraw.Draw(mask)
  y = im.size[1]/2
  r = NCOLORS/2
  for i in range(NCOLORS):
    draw.line((r, y, im.size[0]-r, y), fill=grays[i], width=NCOLORS-i)
    filled_circle(draw, r, y, (NCOLORS-i)/2, grays[i])
    filled_circle(draw, im.size[0]-r, y, (NCOLORS-i)/2, grays[i])
  
  mask.save('mask.png')
  return mask


def make_master_line():
  '''Make an image with alpha to be pasted for all lines'''
  im = Image.new('RGB', (W, W), color=(0, 255, 0))
  mask = make_line_mask(im)
  im.putalpha(mask)
  im.save('mline.png')
  return im

def add_line(im0, im1):
  x = random.randint(-W/2, W/2)
  y = random.randint(-W/2, W/2)
  r1 = im1.rotate(random.randint(5, 145))
  im0.paste(r1, (x, y), r1)

def make_image():
  im = Image.new('RGB', (W, W), color=(0, 0, 0))
  ml = make_master_line()
  for i in range(NLINES):
    add_line(im, ml)
  im.save('f.png')

make_image()
