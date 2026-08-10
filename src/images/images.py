import os.path
from PIL import Image, ImageDraw, ImageColor
#Рефлексия по предыдущему заданию#
#В общем решено верно, но мое решение более громоздкое
def change_format_modify(curr_format, convert_format):
    for f in os.listdir("."):
        if os.path.isfile(f):
            if f.endswith(curr_format):
                im = Image.open(f)
                draw = ImageDraw.Draw(im)
                sz = im.size
                draw.rectangle([sz[0] // 2 - 25, sz[1] // 2 - 25, sz[0] // 2 + 25, sz[1] // 2 + 25], outline="red", width=2)
                draw.multiline_text((sz[0] // 2 - 25,sz[1] // 2 - 25), 'Hello,\nWorld!', fill="black")
                im.save(os.path.splitext(f)[0] + '.' + convert_format)

change_format_modify('jpg', 'png')	                