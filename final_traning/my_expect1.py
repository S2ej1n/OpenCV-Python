# 블러링과 케니에지를 이용해 컬러에지 검출하고
# HSV 색분리로 색깔분리 트랙바 만들기
import cv2

# 여기 imread
img = cv2.imread('color_edge.jpg', cv2.IMREAD_COLOR)
gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 트랙바만들기
def colorBar(value):
    #가우시안 블러링
    blur_img = cv2.GaussianBlur(gray_img, (5,5), 1)
    # 케니에지
    edge_canny = cv2.Canny(blur_img,70,120)

    color_edge = cv2.bitwise_and(hsv_img, hsv_img, mask=edge_canny)

    lower = (value-10, 70, 70)
    upper = (value+10, 255, 255)
    new_img = cv2.inRange(color_edge, lower, upper)

    new_color_edge = cv2.bitwise_and(img, img, mask=new_img)

    cv2.imshow(title, new_color_edge)


value = 0
title = "hello"
cv2.namedWindow(title)
cv2.createTrackbar("colorBar", title, value,300, colorBar)
colorBar(value)
cv2.waitKey(0)