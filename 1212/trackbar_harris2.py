# 수업내용중 k-최근접 이건 Xx 금요일 보강떄 할겨
# 해리스코너 트랙바 달기

import cv2
import numpy as np

def onCornerHarris(thresh):
    # 트랙바의 값에 따라서 매번 초기화 시키면서 값을 적용해야 함으로 이미지 다시 읽음
    img = cv2.imread('harris.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    corner = cv2.cornerHarris(gray, 4, 3, 0.04)
    img[corner > (thresh * 0.01) * corner.max()] = [0, 0, 255]
    cv2.imshow("harris detect", img)

thresh = 1
onCornerHarris(thresh)
cv2.createTrackbar("Threshold", "harris detect", thresh, 20, onCornerHarris)
cv2.waitKey(0)