#중요_타원그리기

import numpy as np, cv2

orange, blue, white = (0,165,255),(255,0,0),(255,255,255)
image = np.full((300, 700, 3), white, np.uint8)

#중심점
pt1, pt2 = (180, 150), (550,150)
size = (120, 60)

#원그리기
cv2.circle(image, pt1, 1, 0, 2)
cv2.circle(image, pt2, 1, 0, 2)

#이미지, 중심점, 크기(x반지름, y반지름), 타원 각도, 시작각도, 종료각도, 색, 두께
cv2.ellipse(image, pt1, size, 0, 0, 360, blue, 1)
cv2.ellipse(image, pt2, size, 90, 0, 360, blue, 1)
cv2.ellipse(image, pt1, size, 0, 30, 270, orange, 4)
cv2.ellipse(image, pt2, size, 90, -45, 90, orange, 4)

cv2.imshow("그리기", image)
cv2.waitKey()