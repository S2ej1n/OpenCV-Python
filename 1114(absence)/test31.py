# 열림 / 닫힘
import cv2
import numpy as np

img = cv2.imread("morph.jpg", cv2.IMREAD_GRAYSCALE)

k = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

opening =cv2.morphologyEx(img, cv2.MORPH_OPEN, k) #열림
closing = cv2.morphologyEx(img,cv2.MORPH_CLOSE,k) #닫힘
open_closing = cv2.morphologyEx(opening,cv2.MORPH_CLOSE, k)

res1 = np.hstack((img,opening))
res2 = np.hstack((closing,open_closing))
res3 = np.vstack((res1,res2))

cv2.imshow("result", res3)
cv2.waitKey(0)
