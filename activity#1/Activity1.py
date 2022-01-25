#library
import cv2
import numpy as np
import math
import matplotlib.image as mpimg

from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

#Lab 1.1
img = cv2.imread('Image.jpg')

cv2.imwrite('Image_BGR.jpg', img)
img_rgb = img[:, :, [2, 1, 0]]

cv2.imwrite('Image_RGB.jpg', img_rgb)

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

r2 = img_rgb[:,:,0]
g2 = img_rgb[:,:,1]
b2 = img_rgb[:,:,2]

show = [img,b,g,r,img_rgb,r2,g2,b2]
showtext = ["BGR","B","G","R","RGB","R","G","B"]
for i in range(0,8):
  plt.subplot(2,4,i+1)
  plt.title(showtext[i])
  plt.imshow(show[i],cmap = 'gray')

plt.tight_layout()

#Lab 1.2

# height,width,channel tran to channel,height,width
# 0,1,2 to 2,0,1

img2 = mpimg.imread('Image.jpg')
img_tran = img2.transpose((2,0,1))
print(img2.shape)
print(img_tran.shape)

#Lab 1.3
# MaxQ = 8 , SMax = 255, Smin = 0
img3 = cv2.imread('Image.jpg')
img3 = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
#print(img3)
def Calculate_BitDepth(img3, bit_depth):
  q_level = 2**bit_depth
  height = img3.shape[0]
  width = img3.shape[1]
  img_array = np.zeros(shape=(height, width), dtype=np.uint8)
  for h in range(height) :
    for w in range(width) :
        q = math.floor( ((img3[h,w])/255) * q_level)
        img_array[h,w] = q
  return img_array

img_new = Calculate_BitDepth(img3,2)
img_new2 = Calculate_BitDepth(img3,4)

show = [img3,img_new,img_new2]
showtext = ["Original","bit_depth: 2","bit_depth: 4"]
fig = plt.figure(2)
for i in range(0,3):
  plt.subplot(2,4,i+1)
  plt.title(showtext[i])
  plt.imshow(show[i],cmap = 'gray')

plt.tight_layout()

#Lab 1.4
img4 = cv2.imread('Image.jpg')
img4 = cv2.cvtColor(img4,cv2.COLOR_BGR2GRAY)

# edit only new_width
scale = 60 # %    # % of original image size
dsize = (int(img.shape[1]*scale/100), int(img.shape[0]*scale/100))
img_resize = cv2.resize(img4, dsize, interpolation = cv2.INTER_AREA)

cv2.imwrite('Image_resize.jpg',img_resize) 

xx,yy = np.mgrid[0:img_resize.shape[0], 0:img_resize.shape[1]]
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(xx, yy, img_resize, cmap='Spectral') 

plt.show()
