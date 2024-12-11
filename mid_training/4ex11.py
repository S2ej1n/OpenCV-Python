#왼쪽버튼 클릭시 사각형, 오른쪽 버튼 클릭시 원
#트랙바로 선 굵기 조절

import random
import numpy as np, cv2

image = np.full((300,500,3), 255, np.uint8)
title = "ex1"

l_val = 1  # 초기 선 굵기
r_val = 20  # 초기 원 반지름

def line_bar(value):
    global l_val
    l_val = value

def circle_bar(value):
    global r_val
    r_val = value

def onMouse(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pt1 = (x,y)
        rx = random.randrange(x+10,x+50)
        ry = random.randrange(y+10,y+50)

        cv2.rectangle(image,pt1,(rx,ry),(0,0,255),l_val)
        cv2.imshow(title,image)
    elif event == cv2.EVENT_RBUTTONDOWN:
        center = (x, y)
        r = random.randrange(10, 50)

        cv2.circle(image,center,r_val,(0,255,0),2)
        cv2.imshow(title, image)

cv2.imshow(title, image)  # 창 생성 후에 트랙바 생성
cv2.createTrackbar("lineBar", title, 1, 10, line_bar)
cv2.createTrackbar("circleBar", title, 20, 50, circle_bar)

cv2.setMouseCallback(title, onMouse)

while True:
    if cv2.waitKey(30) == 27:
        break

cv2.waitKey()