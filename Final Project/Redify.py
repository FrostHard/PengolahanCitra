import cv2
import numpy as np
image=cv2.imread("imgB/carotid7.jpg")
image[np.where((image==[0,0,0]).all(axis=2))]=[0,0,255]
cv2.imwrite('colored/result7.png',image)
