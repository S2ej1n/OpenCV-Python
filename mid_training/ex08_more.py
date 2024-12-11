#특정 영역의 타원만을 복사해서 새 창에 표시하기
#컬러영상으로 하기
import numpy as np, cv2

image = cv2.imread("color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")

blue, green, red = cv2.split(image)
# zero_img = np.zeros(image.shape[:2], np.uint8)
image2 = np.zeros((image.shape[0],image.shape[1]), np.uint8)
#타원그리기 타원은 흰색, 나머지 검정.
ellipse = cv2.ellipse(image2,(200,180),(50,80),0,0,360,255,-1)

b = cv2.bitwise_and(blue, image2)
g = cv2.bitwise_and(green, image2)
r = cv2.bitwise_and(red, image2)
dst = cv2.merge([b,g,r])

cv2.imshow('image', image)
# cv2.imshow('image2',image2)
cv2.imshow('dst',dst)
cv2.waitKey()