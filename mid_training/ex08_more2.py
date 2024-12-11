#특정 영역의 타원만을 복사해서 새 창에 표시하기
#컬러영상으로 하기 & 트랙바 타원크기 조절
import numpy as np, cv2

image = cv2.imread("color.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")

blue, green, red = cv2.split(image)

image2 = np.zeros((image.shape[0],image.shape[1]), np.uint8)

def sizeBar(value):
    pass

#트랙바
title = "ellips"
cv2.namedWindow(title)

cv2.createTrackbar("sizeBar",title,0,150,sizeBar)

while True:
    #이게 문제였음.
    if cv2.waitKey(30) == 27:
        break
    value = cv2.getTrackbarPos("sizeBar",title)

    image2[:] = 0  # 이미지 초기화 (이전 타원을 지우기 위함)

    cv2.ellipse(image2, (200, 180), (value, value + 30), 0, 0, 360, 255, -1)

    b = cv2.bitwise_and(blue, image2)
    g = cv2.bitwise_and(green, image2)
    r = cv2.bitwise_and(red, image2)
    dst = cv2.merge([b,g,r])

    cv2.imshow('image', image)
    cv2.imshow(title, dst)

cv2.destroyAllWindows()