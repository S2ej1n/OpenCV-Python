#그림 합성 농도 조절
import numpy as np, cv2

image2 = cv2.imread("color.jpg", cv2.IMREAD_COLOR)
image = cv2.imread("../background.jpg", cv2.IMREAD_COLOR)

if image is None: raise Exception("영상파일 읽기 오류")

def A_bar(value):
    # a = value*0.1
    # dst = cv2.addWeighted(image, a, image2, 0.5, 0.0)
    # cv2.imshow(title, dst)
    pass

def B_bar(value):
    # b = value * 0.1
    # dst = cv2.addWeighted(image, 0.5, image2, b, 0.0)
    # cv2.imshow(title, dst)
    pass

title = "Change"
cv2.namedWindow(title)
cv2.createTrackbar('A', title, 0 ,10, A_bar)
cv2.createTrackbar('B', title, 0 ,10, B_bar)

while True:
    if cv2.waitKey(30) >= 0: break
    a = cv2.getTrackbarPos('A',title)
    b = cv2.getTrackbarPos('B',title)
    aa = a*0.1
    bb = b*0.1
    dst = cv2.addWeighted(image, aa, image2, bb, 0.0)
    cv2.imshow(title, dst)

# cv2.waitKey(0)