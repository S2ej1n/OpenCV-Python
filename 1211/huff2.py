import numpy as np, cv2

image = cv2.imread('harness.jpg', cv2.IMREAD_COLOR)
if image is None:
    raise Exception("영상 파일 읽기 에러")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # 명암도 영상 변환
_, th_gray = cv2.threshold(gray, 240, 255, cv2.THRESH_BINARY) #이진 영상 변환
# 밝은 부분(240 이상)을 흰색(255)으로, 나머지는 검은색(0)으로 만듬 -> 이진화 처리

kernel = np.ones((3,3), np.uint8) # 3x3 크기의 커널 생성
morph = cv2.erode(th_gray, kernel, iterations=2) # 침식 연산 - 2번 반복
# 객체의 외곽선을 깎아내고, 노이즈를 줄임

contour, hr = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# 외곽선 검출
sorted_cont = sorted(contour, key=cv2.contourArea, reverse=True)
# 외곽선 면적 기준으로 정렬
rect = cv2.boundingRect(sorted_cont[0])
# 가장 큰 외곽선 주위 사각형 영역 계산
x, y, w, h = np.add(rect, (-10, -10, 20, 20)) # 검출 객체 사각형 크기 확대
# (좌우 상하로 10픽셀씩 확장)
roi = th_gray[y:y+h, x:x+w] # roi 정의

rho, theta = 1, np.pi / 180 # 허프 변환 거리 간격, 각도 간격
canny = cv2.Canny(roi, 40, 100) # 케니 에지 검출

# Hough 변환을 통해 직선 검출. / 50은 최소 교차점 수
lines = cv2.HoughLines(canny, rho, theta, 50) #OpenCV함수
#lines는 (rho, theta)의 배열을 반환
cv2.rectangle(morph, (x,y,w,h), 100, 2) #큰 객체 사각형 표시

# 검출된 선 그리기
canny = cv2.cvtColor(canny, cv2.COLOR_GRAY2BGR)
for i in range(len(lines)):
    # lines 배열에서 각 선의 (rho, theta) 값을 가져옴
    for rho, theta in lines[i]:
        # rho: 직선이 원점에서 가장 가까운 지점까지의 거리.
        # theta: 직선이 원점에서 이루는 각도 (라디안 단위).
        a = np.cos(theta)   # 코사인 theta값
        b = np.sin(theta)
        x0 = a*rho  # 검출 직선상의 x좌표 계산 ( 선의 중심점 계산 )
        y0 = a*rho
        # (x0, y0): 직선이 원점에서 rho 거리만큼 떨어진 점 (중심점).

        # 직선을 화면 밖까지 확장 (1000은 임의의 큰 값임)
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))

        cv2.line(canny, (x1,y1), (x2,y2), (0,0,255), 2)

# 검출된 첫 번째 선의 각도를 이용해 이미지를 반대 방향으로 회전시킴
angle = (np.pi - lines[0, 0, 1]) * 180 / np.pi
# lines[0, 0, 1] : 첫 번째 선의 theta 값을 가져옴. => 각도이기 때문에.
# 각 lines[i][0]은 [rho_i, theta_i]로 이루어진 배열
h, w = image.shape[:2]
center = (w//2, h//2)
rot_map = cv2.getRotationMatrix2D(center, -angle, 1)    # 반대방향 회전 행렬 계산
dst = cv2.warpAffine(image, rot_map, (w,h), cv2.INTER_LINEAR)   # 역회전 수행

cv2.imshow("image", image) #원본
cv2.imshow("binary", th_gray) #이진화
cv2.imshow("morph", morph) #침식 처리
cv2.imshow("line_detect", canny) #검출된 선이 그려진 이미지
cv2.imshow("dst", dst) #회전된 이미지

cv2.waitKey(0)





