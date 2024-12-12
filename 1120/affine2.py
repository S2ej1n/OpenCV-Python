# 어파인 변환 이동
import cv2
import numpy as np

img = cv2.imread("matplot.jpg")
rows, cols = img.shape[0:2]

dx, dy = 100, 50

#  X축으로 dx, Y축으로 dy 이동
mtrx = np.float32([[1,0,dx],[0,1,dy]])

dst = cv2.warpAffine(img, mtrx,(cols+dx, rows+dy))
dst2 = cv2.warpAffine(img, mtrx,(cols+dx, rows+dy),
                      None, cv2.INTER_LINEAR, cv2.BORDER_CONSTANT,
                      (255,0,0))

cv2.imshow("test",dst)
cv2.imshow("test2",dst2)
cv2.waitKey(0)