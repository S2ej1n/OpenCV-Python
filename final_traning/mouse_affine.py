import cv2
import numpy as np

# 각도를 계산하는 함수
def calc_angle(pt):
    d1 = np.subtract(pts[1], pts[0]).astype(float)  # 첫 번째 점과 두 번째 점의 차이
    d2 = np.subtract(pts[2], pts[0]).astype(float)  # 첫 번째 점과 세 번째 점의 차이

    # 두 방향 벡터의 각도 계산
    angle1 = cv2.fastAtan2(d1[1], d1[0])
    angle2 = cv2.fastAtan2(d2[1], d2[0])
    return angle2 - angle1  # 두 각도의 차이 = 회전 각도

def draw_point(x, y):
    pts.append([x, y])
    print("좌표:", len(pts), [x, y])
    cv2.circle(tmp, (x, y), 2, 255, 2)
    cv2.imshow("image", tmp)

def onMouse(event, x, y, flags, param):
    global tmp, pts
    if event == cv2.EVENT_LBUTTONUP and len(pts) == 0: draw_point(x, y)
    if event == cv2.EVENT_LBUTTONDOWN and len(pts) == 1: draw_point(x, y)
    if event == cv2.EVENT_LBUTTONUP and len(pts) == 2: draw_point(x, y)

    # 회전 수행
    if len(pts) == 3:
        angle = calc_angle(pts)
        print("회전각: %3.2f" % angle)

        # 어파인 변환 행렬 계산 (회전 중심: pts[0], 회전 각도: angle)
        center = tuple(pts[0])  # 회전 중심점
        rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)

        # 어파인 변환 적용
        dst = cv2.warpAffine(image, rotation_matrix, (image.shape[1], image.shape[0]))

        # 결과 출력
        cv2.imshow("image", dst)
        tmp = np.copy(image)
        pts = []  # 좌표 초기화

# 이미지 불러오기
image = cv2.imread("ham.jpeg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

tmp = np.copy(image)
pts = []

cv2.imshow("image", image)
cv2.setMouseCallback("image", onMouse, 0)
cv2.waitKey(0)
cv2.destroyAllWindows()
