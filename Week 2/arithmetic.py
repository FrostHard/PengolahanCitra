import cv2
import numpy as np
from matplotlib import pyplot as plt

e1 = cv2.getTickCount()

x = np.uint8([250])
y = np.uint8([10])

print (cv2.add(x,y)) # 250+10 = 260 => 255

print (x+y)          # 250+10 = 260 % 256 = 4

img1 = cv2.imread('arlberg.jpg')
img2 = cv2.imread('pexels.jpeg')
img3 = cv2.imread('opencv-logo.png')

dst = cv2.addWeighted(img1,0.7,img2,0.3,0)
"""
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()"""

rows,cols,channels = img3.shape
roi = dst[0:rows, 0:cols ]

img3gray = cv2.cvtColor(img3,cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img3gray, 10, 255, cv2.THRESH_BINARY)
mask_inv = cv2.bitwise_not(mask)

dst_bg = cv2.bitwise_and(roi,roi,mask = mask_inv)

img3_fg = cv2.bitwise_and(img3,img3,mask = mask)

dst2 = cv2.add(dst_bg,img3_fg)
dst[0:rows, 0:cols ] = dst2

cv2.imshow('res',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()

# your code execution
e2 = cv2.getTickCount()
time = (e2 - e1)/ cv2.getTickFrequency()
print(time)