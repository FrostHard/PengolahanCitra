import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('chessboardd.png',0)

chessboard = np.zeros((5,5))
chessboard[1::2, 0::2] = 1
chessboard[0::2, 1::2] = 1

median = cv2.medianBlur(img,5)
mean = cv2.blur(img,(5,5))
weightedAve = cv2.GaussianBlur(img, (5, 5),0)
negative = cv2.bitwise_not(img)
equ = cv2.equalizeHist(img)
res = np.hstack((img,equ))
hist = cv2.calcHist([img],[0],None,[256],[0,256])

cv2.imshow('Chess Board', chessboard)
cv2.imshow('Mean', mean)
cv2.imshow('Median', median)
cv2.imshow('Weighted Average', weightedAve)
cv2.imshow('Negative', negative)
cv2.imshow('Hist', equ)
cv2.imshow('Histogram', hist)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow('chessboard.png', chessboard)
cv2.imshow('mean.png', mean)
cv2.imshow('median.png', median)
cv2.imshow('weightedAverage.png', weightedAve)
cv2.imshow('negative.png', negative)
cv2.imshow('Histogram1.png', equ)
cv2.imshow('Histogram2.png', hist)
