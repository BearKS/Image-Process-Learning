#library
import cv2
from cv2 import cvtColor
import numpy as np
from matplotlib import pyplot as plt
from skimage import exposure
# ------------------------------------------------------------------------------------------ #

# Lab 3.1
img1 = cv2.imread('Image3.jpg')
a = 1.0
b = 0
fps = 15
h = img1.shape[0]
w = img1.shape[1]
size = (w,h)
img_array = []
for  y in np.arange(0.1, 3.0, 0.01):
   Im_gamma = np.uint8((a*((img1/255)**y)+b)*255)
   img_array.append(Im_gamma)

out = cv2.VideoWriter('activity3.mp4',cv2.VideoWriter_fourcc(*'mp4v'), fps, size)
   
for y in range(len(img_array)):
     out.write(img_array[y])
out.release()