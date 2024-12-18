import numpy as np, cv2

image = cv2.imread("interpolation.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

size = (350,400)
dst1 = cv2.resize(image, size, 0, 0, cv2.INTER_LANCZOS4)
dst2 = cv2.resize(image, size, 0, 0, cv2.INTER_CUBIC)
dst3 = cv2.resize(image, size, 0, 0, cv2.INTER_LINEAR) #cv함수 - 양선형
dst4 = cv2.resize(image, size, 0, 0, cv2.INTER_NEAREST) #cv함수 - 최근접

# 비율조정
dst5 = cv2.resize(image, None, fx=0.3, fy=0.3, interpolation=cv2.INTER_AREA) #cv함수

cv2.imshow("original", image)
cv2.imshow("LANCZOS4", dst1)
cv2.imshow("CUBIC", dst2)
cv2.imshow("LINEAR", dst3)
cv2.imshow("NEAREST", dst4)
cv2.imshow("INTER_AREA", dst5)
cv2.waitKey(0)