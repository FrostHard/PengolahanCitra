import cv2
import numpy as np

img = cv2.imread(r"C:\Users\farre\Desktop\PCitra\Lenna.png")

blue = img[100,100,0]
print(blue)