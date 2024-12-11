#교수님 예제
import numpy as np
import cv2

#opencv에서 기본 색은 BGR을 상요한다.
blue, green, red = (255,0,0),(0,255,0),(0,0,255)

image = np.zeros((400,600,3), np.uint8)
image[:] = (255,255,255) #모든 픽셀 다 채움
pt1, pt2 = (50,50), (250,150)

cv2.rectangle(image, pt1, pt2, blue, 3, cv2.LINE_4)

cv2.imshow("test", image)
cv2.waitKey(0)
cv2.destroyAllWindows()