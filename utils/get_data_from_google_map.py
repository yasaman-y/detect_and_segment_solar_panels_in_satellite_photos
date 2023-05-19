
#  pip install turfpy


from turfpy.measurement import bbox
import math
from PIL import Image
import requests
import os
path = 'data/google_map'

def num2deg(xtile, ytile, zoom):
    n = 2.0 ** zoom
    lon_deg = xtile / n * 360.0 - 180.0
    lat_rad = math.atan(math.sinh(math.pi * (1 - 2 * ytile / n)))
    lat_deg = math.degrees(lat_rad)
    return (lat_deg, lon_deg)

def getXY(lng, lat, zoom):
    tile_size = 256
    numTiles = 1 << zoom
    point_x = (tile_size/ 2 + lng * tile_size / 360.0) * numTiles // tile_size
    sin_y = math.sin(lat * (math.pi / 180.0))
    point_y = ((tile_size / 2) + 0.5 * math.log((1+sin_y)/(1-sin_y)) * -(tile_size / (2 * math.pi))) * numTiles // tile_size
    return int(point_x), int(point_y)


def download_im(geometry, zoom):
    num = 0
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
    minlon, minlat, maxlon, maxlat = bbox(geometry)
    print(minlon, minlat, maxlon, maxlat)

    start_x, start_y = getXY(minlon, maxlat, zoom)
    end_x, end_y = getXY(maxlon, minlat, zoom)


    start_x -=1
    start_y -=1

    end_x +=1
    end_y +=1


    w = (end_x+1 - start_x) * 256
    h = (end_y+1 - start_y) * 256
    result = Image.new("RGB", (w, h))
    result = result.resize((2000, 2000))

    for x in range(start_x, end_x+1):
        for y in range(start_y, end_y+1):
            print(f"donwloading {num}/{((end_x+1) - (start_x)) * ((end_y+1) - (start_y)) }")
            
            while True:
                try:
                    url = "http://mt1.google.com/vt/lyrs=y&x={}&y={}&z={}".format(x,y, zoom)
                    raw = requests.get(url, stream=True, headers=header).raw
                    break
                except:
                    continue
            
            i = Image.open(raw)
            x_paste = (x - start_x) * 256
            y_paste = h - (end_y+1 - y) * 256
            result.paste(i, (x_paste, y_paste))
            num +=1
    name = os.path.join(path, "map_{}_{}_{}_{}.png".format(minlat, minlon, maxlat, maxlon))
    result.save(os.path.join (name))
    return result, start_x, start_y, end_x, end_y, w, h


# geometry = {
#         "coordinates": [
#           [
#             [
#               54.360723589073814,
#               31.900557381839263
#             ],
#             [
#               54.360723589073814,
#               31.89907003779554
#             ],
#             [
#               54.36249344408964,
#               31.89907003779554
#             ],
#             [
#               54.36249344408964,
#               31.900557381839263
#             ],
#             [
#               54.360723589073814,
#               31.900557381839263
#             ]
#           ]
#         ],
#         "type": "Polygon"
#       }

geometry = {'coordinates': [[[-94.57260260212433, 39.14019525724463],
       [-94.57071164476883, 39.14019525724463],
       [-94.57071164476883, 39.141118918340055],
       [-94.57260260212433, 39.141118918340055],
       [-94.57260260212433, 39.14019525724463]]],
     'type': 'Polygon'}
# zoom = 18
zoom = 21



download_im(geometry, zoom)