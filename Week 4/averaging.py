import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('opencv-logo-white.png')
kernel = np.ones((2,2),np.float32)/4

blur = cv2.blur(img,(5,5))
blurA = cv2.GaussianBlur(img,(5,5),0)     #
#median = cv2.medianBlur(img,5)           # uncomment to use any of these functions.
blurB = cv2.bilateralFilter(img,9,75,75)  #

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred') #change to median for median func
plt.xticks([]), plt.yticks([])
plt.subplot(221),plt.imshow(blurA),plt.title('BlurredA') #change to median for median func
plt.xticks([]), plt.yticks([])
plt.subplot(222),plt.imshow(blurB),plt.title('BlurredB') #change to median for median func
plt.xticks([]), plt.yticks([])
plt.show()