import numpy as np
from PIL import Image

width = 5
height = 4

array_1 = np.zeros([height,width,3],dtype = np.uint8)
img = Image.fromarray(array_1)
img.save('test_1.png')

array_2 = np.zeros([100,200,3],dtype = np.uint8)
array_2[:,:100] = [255,128,0]
array_2[:,100:] = [0,0,255]
img = Image.fromarray(array_2)
img.save('test_2.png')

im = Image.open('test_2.png')
rgb_im = im.convert('RGB')
r,g,b = rgb_im.getpixel((150,1))
print(r,g,b)