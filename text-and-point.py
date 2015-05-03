# On some systems, need to import like this:
# import Image
# import ImageDraw

# On others, import like this:
from PIL import Image, ImageDraw

im = Image.new('RGB', (100, 100))

draw = ImageDraw.Draw(im)
red = (255, 0, 0)
draw.text((5,5), 'Hello', red)
draw.point((50, 50), red)

im.save('f.png')

