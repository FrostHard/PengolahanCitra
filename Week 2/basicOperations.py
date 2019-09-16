import cv2
import numpy as np
from matplotlib import pyplot as plt

BLUE = [255,0,0]

img = cv2.imread(r'C:\Users\farre\Desktop\Pengolahan Citra\Week 2\Lenna.png')

px = img[100,100]
print (px)

blue = img[100,100,0]
print (blue)

img[100,100] = [255,255,255]
print (img[100,100])

img.itemset((10,10,2),100)
img.item(10,10,2)

print(img.shape)

print(img.size)

print(img.dtype)

move = img[280:340, 330:390]
img[273:333, 100:160] = move

b,g,r = cv2.split(img)
img = cv2.merge((b,g,r))

replicate = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()