import os
from PIL import Image

load_path = 'Idle\\'
save_path = 'convert\\'

load_list = os.listdir(load_path)

for file in load_list:
    img_name = file[:-4]

    im = Image.open(load_path + img_name + '.png')
    width, height = im.size

    pink = Image.open('pink.bmp', 'r')
    bg = pink.resize((width, height))
    pink.close()

    for i in range(width):
        for j in range(height):
            [r, g, b, a] = im.getpixel((i, j))
            if a < 10:
                r = 255
                g = 0
                b = 255
            value = (r, g, b)
            bg.putpixel((i, j), value)
    im.close()
    bg.save(save_path + img_name + '.bmp')
