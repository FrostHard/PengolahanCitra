import cv2
import numpy as np

# black blank image
blank_image = np.zeros(shape=[512, 512, 3], dtype=np.uint8)
# print(blank_image.shape)
cv2.imshow("Black Blank", blank_image)

# white blank image
blank_image2 = 255 * np.ones(shape=[512, 512, 3], dtype=np.uint8)
cv2.imshow("White Blank", blank_image2)

cv2.waitKey(0)
cv2.destroyAllWindows()
