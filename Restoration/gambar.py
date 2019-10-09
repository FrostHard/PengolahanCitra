import cv2
import numpy as np
from matplotlib import pyplot as plt

horizontal = np.zeros((8,8))
horizontal[1::2, 0::2] = 1
horizontal[1::2, 1::2] = 1

vertical = np.zeros((8,8))
vertical[1::2, 1::2] = 1
vertical[0::2, 1::2] = 1

chessboard = np.zeros((8,8))
chessboard[1::2, 0::2] = 1
chessboard[0::2, 1::2] = 1

hitam = np.zeros(shape=[256, 256, 3], dtype=np.uint8)
putih = 255*np.ones(shape=[256, 256, 3], dtype=np.uint8)



titles = ['Hitam', 'Putih',
          'Horizontal', 'Vertical',
          'Chessboard']

images = [hitam, putih, horizontal, vertical, chessboard]

for i in range(5):
    plt.subplot(3,3,i+1),plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

cv2.imwrite('messigray.png',images)
