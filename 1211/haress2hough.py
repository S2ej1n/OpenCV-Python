# 하네스를 확률 하프변환으로 수정해보기

import cv2
import numpy as np

image = cv2.imread('harness.jpg', cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상 파일 읽기 에러")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 그레이로 영상 변환
_, th_gray = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY) #이진 영상 변환
kernel = np.ones((3,3), np.uint8)
morph = cv2.erode(th_gray, kernel, iterations=2) # 침식 연산 - 2번 반복

contour, hr = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
sorted_cont = sorted(contour, key=cv2.contourArea, reverse=True)
rect = cv2.boundingRect(sorted_cont[0])
x, y, w, h = np.add(rect, (-10, -10, 20, 20)) # 검출 객체 사각형 크기 확대
roi = th_gray[y:y+h, x:x+w]
rho, theta = 1, np.pi / 180 # 허프 변환 거리 간격, 각도 간격
canny = cv2.Canny(roi, 40, 100) # 케니 에지 검출

lines = cv2.HoughLinesP(canny, rho, theta, 50, None, 50, 10) #OpenCV함수

cv2.rectangle(morph, (x,y,w,h), 100, 2) #큰 객체 사각형 표시

canny = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)

for line in lines:
    # line - 각 선의 정보를 포함하는 배열, 각 요소는 [x1, y1, x2, y2] 형식의 좌표
    x1, y1, x2, y2 = line[0]
    cv2.line(canny, (x1,y1), (x2,y2), (0,0,255), 2)

angle = (np.pi - lines[0, 0, 1]) * 180 / np.pi

# # 첫 번째 선의 좌표 가져오기
# x1, y1, x2, y2 = lines[0][0]
# 선의 기울기 기반 각도 계산
# angle = np.arctan2(y2 - y1, x2 - x1) * 180 / np.pi



h, w = image.shape[:2]
center = (w//2, h//2)
rot_map = cv2.getRotationMatrix2D(center, -angle, 1)    # 반대방향 회전 행렬 계산
dst = cv2.warpAffine(image, rot_map, (w,h), cv2.INTER_LINEAR)

cv2.imshow("image", image)
cv2.imshow("binary", th_gray)
cv2.imshow("morph", morph)
cv2.imshow("line_detect", canny)
cv2.imshow("dst", dst)

cv2.waitKey(0)

