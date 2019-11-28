import cv2
img1 = cv2.imread('imgA/carotid1.jpg')
img2 = cv2.imread('colored/result1.png')

#img1 = cv2.resize(img1, (512,512))
#img2 = cv2.resize(img2, (512,512))

dst = cv2.addWeighted(img1,2,img2,1,0)

cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
