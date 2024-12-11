import numpy as np, cv2

image = cv2.imread("laplacian.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

canny2 = cv2.Canny(image, 100, 150)

cv2.imshow("image",image)
cv2.imshow("canny",canny2)
cv2.waitKey(0)