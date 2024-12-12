# 수업내용중 k-최근접 이건 Xx 금요일 보강떄 할겨

# 해리스코너 트랙바 달기

import cv2
import numpy as np
from fontTools.unicodedata import block


def drawConer(corner, image, thresh):
    cnt = 0
    corner = cv2.normalize(corner, 0, 100, cv2.NORM_MINMAX)
    corners =[]
    for i in range(1, corner.shape[0]-1):
        for j in range(1, corner.shape[1]-1):
            neighbor = corner[i-1:i+2, j-1:j+2].flatten()
            max = np.max(neighbor[1::2])
            if thresh < corner[i,j] > max: corners.append((j,i))

    for pt in corners:
        cv2.circle(image, pt, 3, (0,230,0), -1)
    return image

def onCornerHarris(thresh):
    dst = drawConer(corner, np.copy(img), thresh)
    cv2.imshow("harris detect", dst)

img = cv2.imread('harris.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = 2

corner = cv2.cornerHarris(gray, 4, 3, 0.04)
onCornerHarris(thresh)
cv2.createTrackbar("Threshold", "harris detect", thresh, 20, onCornerHarris)
cv2.waitKey(0)