#왼쪽버튼 클릭시 사각형, 오른쪽 버튼 클릭시 원
import random
import numpy as np, cv2

image = np.full((300,500,3), 255, np.uint8)
title = "ex1"

def onMouse(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pt1 = (x,y)
        rx = random.randrange(x+10,x+50)
        ry = random.randrange(y+10,y+50)

        cv2.rectangle(image,pt1,(rx,ry),(0,0,255),2)
        cv2.imshow(title,image)
    elif event == cv2.EVENT_RBUTTONDOWN:
        center = (x, y)
        r = random.randrange(10, 50)

        cv2.circle(image,center,r,(0,255,0),2)
        cv2.imshow(title, image)

cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey()