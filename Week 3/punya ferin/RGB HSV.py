import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    lower_green = np.array([50, 50, 120])
    upper_green = np.array([70, 255, 255]) 
    green_mask = cv2.inRange(hsv, lower_green, upper_green) # I have the Green threshold image.

    upper_red = np.array([0, 50,50])
    lower_red = np.array([50, 255,255])
    red_mask = cv2.inRange(hsv, upper_red, lower_red)
    
    # Threshold the HSV image to get only blue colors
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask = blue_mask + green_mask + red_mask

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
