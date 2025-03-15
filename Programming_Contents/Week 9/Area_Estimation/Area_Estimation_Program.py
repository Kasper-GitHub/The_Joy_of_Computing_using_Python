import scipy
from PIL import Image
import numpy
import random
import imageio.v2 as imageio

img = imageio.imread("Random_Map.png")
count_orange = 0
count_black = 0
count = 0

while count < 10000:
    x = random.randint(0,580)
    y = random.randint(0,580)
    z = 0

    if img[x][y][z] > 225:
        count_orange += 1
        count += 1
    elif img[x][y][z] > 180:
        count_black += 1
        count += 1
    else:
        count += 1

print("Orange Area : ",count_orange, "\nBlack Area :", count_black, "\nUnconsidered Area :", count-count_black-count_orange)