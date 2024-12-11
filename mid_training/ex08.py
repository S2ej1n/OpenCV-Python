#특정 영역의 타원만을 복사해서 새 창에 표시하기
import numpy as np, cv2

image = cv2.imread("color.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

image2 = np.zeros((image.shape[0],image.shape[1]), np.uint8)
#타원그리기 타원은 흰색, 나머지 검정.
# taone = cv2.circle(image2,(100,200),100,255,-1)

ellipse = cv2.ellipse(image2,(200,180),(50,80),0,0,360,255,-1)
dst = cv2.bitwise_and(image, image2)

cv2.imshow('image', image)
# cv2.imshow('image2',image2)
cv2.imshow('dst',dst)
cv2.waitKey()