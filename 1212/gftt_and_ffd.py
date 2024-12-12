# GFTT / FFD 사용해서 코너 찾기
# cv2.goodFeaturesToTrack()
# cv2.FastFeatureDetector_create()
# cv2.FastFeatureDetector.detect(img)
import cv2

img = cv2.imread('harris.jpg')
img2 = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# GFTT - 이미지 / 최대 코너 개수 / 코너점 결정 값 / 코너점 사이 최소 거리
corner_gftt = cv2.goodFeaturesToTrack(gray, 400, 0.01, 10)
# 코너점 좌표를 반환한다.

if corner_gftt is not None:
    # 코너 갯수만큼 반복
    for i in range(corner_gftt.shape[0]):
        pt = (int(corner_gftt[i, 0, 0]), int(corner_gftt[i, 0, 1]))
        cv2.circle(img, pt, 1, (0,0,255),2)

# FAST/FFD
retval_fast = cv2.FastFeatureDetector_create(60)
# keypoint 검출 및 그리기
point = retval_fast.detect(img2,None)
# draw = cv2.drawKeypoints(img2, point, None)
draw = cv2.drawKeypoints(img2, point, None, (0,255,0))

cv2.imshow('corner_gftt',img)
cv2.imshow('retval_fast',draw)
cv2.waitKey(0)
cv2.destroyAllWindows()