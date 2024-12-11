# 책과 다르게 원래 있던 함수를 활용해 따로 작성한거임.
# 허프변환

import numpy as np, cv2

image = cv2.imread('hough.jpg')
if image is None:
    raise Exception("영상 파일 읽기 에러")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5,5), 2, 2)
canny = cv2.Canny(blur, 100, 200, 5)

rho, theta = 1, np.pi / 180
lines = cv2.HoughLines(canny, rho, theta, 80)

for i in range(len(lines)):
    for rho, theta in lines[i]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a*rho
        y0 = b*rho

        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(image, (x1,y1), (x2,y2), (0,0,255), 2)

cv2.imshow("image", image)
cv2.imshow("canny", canny)
cv2.waitKey(0)