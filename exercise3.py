"""Check the documentation for cv2.pointPolygonTest(), you can find a nice 
image in Red and Blue color. It represents the distance from all pixels to 
the white curve on it. All pixels inside curve is blue depending on the 
distance. Similarly outside points are red. Contour edges are marked with 
White. So problem is simple. Write a code to create such a representation of 
distance."""


import numpy as np
import cv2
img=cv2.imread('pol.png',1)
img_gray=cv2.imread('pol.png',0)

_,cnt,_=cv2.findContours(img_gray,2,1)
cv2.drawContours(img,cnt,0,(0,0,255),2)
(r,c)=img_gray.shape 
for i in range(r):
    for j in range(c):
        dist = cv2.pointPolygonTest(cnt[0],(i,j),True)
        if dist<0:
            img[i,j,:]=(255-(-dist),0,0)
        else:
            img[i,j,:]=(0,0,255-dist)


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
