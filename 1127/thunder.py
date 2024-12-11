#번개
import cv2
import numpy as np

img = cv2.imread("thunder.png")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)
coutours, hy = cv2.findContours(th, cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)

# contours의 경우 리스트 형태로 찾은 contour를 가지고 있다.
cont = coutours[0]

# 감싸는 사각형
x,y, w, h = cv2.boundingRect(cont) #좌표를 가져옴
cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,0), 3) #좌표에 맞게 그림

# 최소한의 사각형 - 녹색
rect = cv2.minAreaRect(cont)
box = cv2.boxPoints(rect)

box = np.intp(box)
cv2.drawContours(img, [box], -1, (0,255,0), 3)

# 최소한의 원 - 파란색
(x,y), radius = cv2.minEnclosingCircle(cont)
cv2.circle(img, (int(x),int(y)), int(radius), (255,0,0), 3)

# 최소한의 삼각형 - 핑크
ret, tri = cv2.minEnclosingTriangle(cont)
cv2.polylines(img, [np.int32(tri)], True, (255,0,255))

# 최소한의 타원 - 노랑
ellipse = cv2.fitEllipse(cont)
cv2.ellipse(img, ellipse,(0,255,255),3)

#중심점을 통과하는 직선
[vx, vy, x, y] = cv2.fitLine(cont, cv2.DIST_L2,
                             0,0.01, 0.01)
cols, rows = img.shape[:2]
cv2.line(img,(0, int(0-x*(vy/vx) + y)), (cols-1, int((cols-x)*(vy/vx) + y)),(0,0,255),2)

cv2.imshow("default", img)
cv2.waitKey(0)