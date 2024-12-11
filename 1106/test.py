# 이진화 트랙바 만들기
import cv2

def onThreshold(value):
    _, img_bin = cv2.threshold(img, value, 255, cv2.THRESH_BINARY)
    cv2.imshow("result", img_bin)

img = cv2.imread("matplot.jpg",cv2.IMREAD_GRAYSCALE)
if img is None: raise Exception("영상파일읽기오류")

cv2.namedWindow("result")
cv2.createTrackbar("threshold","result",0,255,onThreshold)
cv2.waitKey(0)