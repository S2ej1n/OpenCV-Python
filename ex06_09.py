#그림 합성 농도 조절
import numpy as np, cv2

image2 = cv2.imread("add1.jpg", cv2.IMREAD_GRAYSCALE)
image = cv2.imread("add2.jpg", cv2.IMREAD_GRAYSCALE)

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
cv2.createTrackbar('image1', title, 0 ,100, A_bar)
cv2.createTrackbar('image2', title, 0 ,100, B_bar)


while True:
    if cv2.waitKey(30) >= 0: break
    a = cv2.getTrackbarPos('image1',title)
    b = cv2.getTrackbarPos('image2',title)
    aa = a*0.01
    bb = b*0.01
    dst = cv2.addWeighted(image, aa, image2, bb, 0.0)
    ddst = np.hstack((image2,dst))
    dddst = np.hstack((ddst,image))
    cv2.imshow(title, dddst)

# cv2.waitKey(0)