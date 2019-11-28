import cv2
import numpy as np

def nothing(x):
    pass
# Using HSV Segmentation 
# Trackbar for setting to specific color to detect wanted shape.
# L = Lower, U = upper
# H = Hue, S = Satruation, V = Value
cv2.namedWindow("Setting")
cv2.createTrackbar("LH", "Setting", 0, 255, nothing)
cv2.createTrackbar("LS", "Setting", 0, 255, nothing)
cv2.createTrackbar("LV", "Setting", 0, 255, nothing)
cv2.createTrackbar("UH", "Setting", 255, 255, nothing)
cv2.createTrackbar("US", "Setting", 255, 255, nothing)
cv2.createTrackbar("UV", "Setting", 255, 255, nothing)

while True:
    frame = cv2.imread('C:\\Users\\Farrell\\Documents\\GitHub\\PengolahanCitra\\Final Project\\img\\carotid8.jpg')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("LH", "Setting")
    l_s = cv2.getTrackbarPos("LS", "Setting")
    l_v = cv2.getTrackbarPos("LV", "Setting")

    u_h = cv2.getTrackbarPos("UH", "Setting")
    u_s = cv2.getTrackbarPos("US", "Setting")
    u_v = cv2.getTrackbarPos("UV", "Setting")

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv2.inRange(hsv, l_b, u_b)

    result = cv2.bitwise_and(frame, frame, mask=mask)

# Load image
    cv2.imshow("original", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("result", result)

    key = cv2.waitKey(1)
    if key == 27:
        break
# Press Esc to quit
cv2.destroyAllWindows()
 
