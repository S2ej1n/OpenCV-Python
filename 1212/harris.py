# 해리스 코너 검출
import cv2

filename = 'harris.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)
img[dst>0.01*dst.max()]=[0,0,255]
# 원본 이미지에서 적절한 부분을 빨간색으로 표시합니다.

cv2.imshow('dst',img)
cv2.waitKey(0)
cv2.destroyAllWindows()