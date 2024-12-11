#왼쪽버튼 클릭시 사각형, 오른쪽 버튼 클릭시 원 책 예제
import random
import numpy as np, cv2

image = np.full((300,500,3), 255, np.uint8)
title = "ex3"

def onMouse(event,x,y,flags,param):
    global title, pt
    if event == cv2.EVENT_LBUTTONDOWN:
        if pt[0] < 0:
            pt = (x,y)
        else:
            cv2.rectangle(image,pt,(x,y),(0,0,255),2)
            cv2.imshow(title,image)
            pt = (-1,-1)
    elif event == cv2.EVENT_RBUTTONDOWN:
        if pt[0] < 0:
            pt = (x,y)
        else:
            dx, dy = pt[0]-x, pt[1]-y
            r = int(np.sqrt(dx*dx + dy*dy))

            cv2.circle(image,pt,r,(0,255,0),2)
            cv2.imshow(title, image)
            pt=(-1,-1)

pt = (-1,-1)
cv2.imshow(title, image)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey()