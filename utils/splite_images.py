
import os
# import image_slicer
import numpy as np
from PIL import Image
from itertools import product



def crop(path, input):
    k = 0

    im = Image.open(input)
    imgwidth, imgheight = im.size


    width = int(np.floor(imgwidth/5))
    height = int(np.floor(imgheight/5))

    for i in range(0,imgheight,height):
        for j in range(0,imgwidth,width):
            box = (j, i, j+width, i+height)
            a = im.crop(box)
            try:
                # o = a.crop(area)
                a.save(os.path.join(path,"IMG-%s.png" % k))
            except Exception as er:
                print(er)
                pass
            k +=1


def crop_2(path, input):
    k = 0

    im = Image.open(input)
    imgwidth, imgheight = im.size

    W = 2
    H = 2

    width = int(np.floor(imgwidth/W))
    height = int(np.floor(imgheight/H))

    x_0 = 0
    y_0 = 0

    for i in range(0,W):
        for j in range(0,H):

            box = (x_0, y_0, x_0+width, y_0+height)
            x_0 = x_0+width
            y_0 =  y_0+height

            # im.crop((left, top, right, bottom))
            a = im.crop(box)  
            try:
                # o = a.crop(area)
                a.save(os.path.join(path,"IMG-%s.png" % k))
            except Exception as er:
                print(er)
                pass
            k +=1



def tile(filename, dir_in, dir_out, d):
    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(dir_in, filename))
    w, h = img.size
    
    grid = product(range(0, h-h%d, d), range(0, w-w%d, d))
    for i, j in grid:
        box = (j, i, j+d, i+d)
        out = os.path.join(dir_out, f'{name}_{i}_{j}{ext}')
        img.crop(box).save(out)




list_files = os.listdir("data/google_map/") 


for file_ in list_files:
    path = "data/google_map_splite_data"
    input = "data/google_map/" + file_
    dir_in =  "data/google_map/"

    # crop_2(path, input)

    tile(file_, dir_in, path, 500)

