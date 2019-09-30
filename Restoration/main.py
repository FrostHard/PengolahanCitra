import cv2
import numpy as np
from matplotlib import pyplot as plt

imgA = cv2.imread('Lenna.png',0)

gblur = cv2.GaussianBlur(imgA,(5,5),0)
median = cv2.medianBlur(imgA,5)
dst = cv2.filter2D(imgA,-1,kernel)

titles = ['Gaussian Blur',
          'Median Blur']

images = [gblur, median]

for i in range(2):
    plt.subplot(2,1,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()
