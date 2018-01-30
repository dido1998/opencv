"""Try to find a way to extract more than one colored objects, 
for eg, extract red, blue, green objects simultaneously.
"""

import numpy as np
import cv2
img=cv2.imread('logo.png')
img_hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
red_low=np.array([0,50,50])
red_high=np.array([10,255,255])
blue_low=np.array([110,50,50])
blue_high=np.array([130,255,255])
green_low=np.array([60,50,50])
green_high=np.array([80,255,255])
mask_red=cv2.inRange(img_hsv,red_low,red_high)
mask_green=cv2.inRange(img_hsv,green_low,green_high)
mask_blue=cv2.inRange(img_hsv,blue_low,blue_high)
mask=cv2.add(mask_red,mask_blue,mask_green)
img1=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow('image',img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
