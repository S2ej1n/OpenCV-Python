# 팽창 - 객체 확장되어 뚜렷, 빈 공간 메워짐
# 외부 배경의 잡음도 확장됨
import cv2
import numpy as np

#이미지 읽기
img = cv2.imread("morph.jpg")
k = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
res_dilate=cv2.dilate(img,k) #팽창

#cv2.imshow("Origin",img)
#cv2.imshow("Dilate",res_dilate)
res = np.hstack((img,res_dilate))
cv2.imshow("Dilate",res)
cv2.waitKey(0)