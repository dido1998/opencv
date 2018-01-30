"""Write a small application to find the Canny edge detection whose threshold 
values can be varied using two trackbars. This way, you can understand the 
effect of threshold values.""""


import cv2
import numpy as np
t1=0
t2=0
img=cv2.imread('messi.jpeg')

def edge1(x):
     global t1,t2,img
     t1=x
    
def edge2(x):
     global t1,t2,img
     t2=x


cv2.namedWindow('image')
cv2.createTrackbar('threshold min','image',0,200,edge1)
cv2.createTrackbar('threshold_max','image',0,700,edge2)
while(True):
     img1=cv2.Canny(img,t1,t2)
     cv2.imshow('image',img1)
     k = cv2.waitKey(1) & 0xFF
     if k == 27:
         break
cv2.destroyAllWindows()