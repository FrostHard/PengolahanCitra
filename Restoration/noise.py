import numpy as np
import cv2
import skimage
from matplotlib import pyplot as plt

img = cv2.imread("horizontal.png")

def plotnoise(img, mode, r, c, i):
    plt.subplot(r,c,i)
    if mode is not None:
        gimg = skimage.util.random_noise(img, mode=mode)
        plt.imshow(gimg)
    else:
        plt.imshow(img)
    plt.title(mode)
    plt.axis("off")

plt.figure(figsize=(18,24))
r=4
c=2
plotnoise(img, "gaussian", r,c,1)
plotnoise(img, "poisson", r,c,2)
plotnoise(img, "s&p", r,c,3)
plotnoise(img, "speckle", r,c,4)
plotnoise(img, None, r,c,5)
plt.show()
