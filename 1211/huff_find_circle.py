# ball.png를 이용, 허프변환은 직선, 원 두가지에서 사용됨.
# 원을 찾는 코드 찾아서 적용해보기

import cv2
import numpy as np

image = cv2.imread('balls.png')
if image is None:
    print('Image load failed!')
resize_img = cv2.resize(image, (800,800)) #이미지 너무 커서 사이즈 조절
gray_image = cv2.cvtColor(resize_img, cv2.COLOR_BGR2GRAY)

# 노이즈 제거를 위한 가우시안 블러
blur = cv2.GaussianBlur(gray_image, (3,3), 0)

# 허프 원 변환 적용( dp=1.2, minDist=30, cany_max=200 )
circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1.8, 30, None, 200)
# dp 값은 1에 가까울수록 정확하게 원을 검출한다고 하는데, 경험적으로 증감할것.
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # 원 둘레에 초록색 원 그리기
        cv2.circle(resize_img,(i[0], i[1]), i[2], (0, 255, 0), 2)
        # 원 중심점에 빨강색 원 그리기
        cv2.circle(resize_img, (i[0], i[1]), 2, (0,0,255), 5)

cv2.imshow('image', resize_img)
cv2.waitKey(0)
cv2.destroyAllWindows()