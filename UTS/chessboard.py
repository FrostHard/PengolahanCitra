import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('chessboardd.png', 0)

chessboard = np.zeros((5,5))
chessboard[1::2, 0::2] = 1
chessboard[0::2, 1::2] = 1

median = cv2.medianBlur(img,5)
mean = cv2.blur(img,(5,5))
weightedAve = cv2.GaussianBlur(img, (5, 5),0)
negative = cv2.bitwise_not(img)
equ = cv2.equalizeHist(img) 
'''
dft = cv2.dft(img, flags = cv2.DFT_COMPLEX_OUTPUT)
dft_shift = np.fft.fftshift(dft)

rows, cols = img.shape
crow, ccol = rows/2 , cols/2     # center

# create a mask first, center square is 1, remaining all zeros
mask = np.zeros((rows, cols, 2), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 1

# apply mask and inverse DFT
fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])
'''

titles = ['Chess Board', 'Mean',
          'Median', 'Negative', 'Weighted Average', 'Histogram']

images = [chessboard, mean, median, negative, weightedAve, equ]

for i in range(6):
    plt.subplot(3,3,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.imwrite('chessboard.png',plt)
