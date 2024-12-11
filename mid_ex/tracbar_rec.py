#트랙바로 사각형 크기 조절

import numpy as np
import cv2

def onChange(value):
    global image, title
    image[:] = (255, 255, 255)  # 색상을 흰색으로 초기화를 위한 작업
    cv2.rectangle(image, (0, 0), (value, value), blue, 3, cv2.LINE_4)
    cv2.imshow(title, image)

image = np.zeros((300, 500, 3), np.uint8)

blue, green, red = (255,0,0),(0,255,0),(0,0,255)
image[:] = (255,255,255)
cv2.rectangle(image, (0,0), (1,1), blue, 3, cv2.LINE_4)
title = "Trackbar Event"
cv2.imshow(title, image)

cv2.createTrackbar("Brightness", title, 0, 300, onChange)
cv2.waitKey(0)
cv2.destroyAllWindows()