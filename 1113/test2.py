# 블러링과 케니 에지를 이용한 컬러 에지 검출
import cv2
import numpy as np

def onTrackbar(th):
    rep_edge = cv2.GaussianBlur(rep_gray, (5,5), 0)
    rep_edge = cv2.Canny(rep_edge, th, th*2, 5)
    color_edge = cv2.bitwise_and(image, image, mask=rep_edge)
    # 마스크가 흰색인 부분만 원본이미지 유지.
    result = np.hstack((image, color_edge))
    cv2.imshow("color edge", result)

def Median(value):
    if value > 0:  # 트랙바 값이 1 이상이면 필터 적용
        color_edge = cv2.medianBlur(image, 5)
    else:
        color_edge = image  # 원본 사용
    result = np.hstack((image, color_edge))
    cv2.imshow("color edge", result)

def Gaussian(value):
    if value > 0:  # 트랙바 값이 1 이상이면 필터 적용
        color_edge = cv2.GaussianBlur(image, ksize=(7, 7), sigmaX=10.0)
    else:
        color_edge = image
    result = np.hstack((image, color_edge))
    cv2.imshow("color edge", result)

image = cv2.imread("color_edge.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")

th = 50
# rep_image = cv2.repeat(image, 1, 2)
rep_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

cv2.namedWindow("color edge", cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("Canny th", "color edge", th, 100, onTrackbar)
cv2.createTrackbar('median', "color edge", 0 ,1, Median)
cv2.createTrackbar('gaussian', "color edge", 0 ,1, Gaussian)
# onTrackbar(th)
cv2.waitKey(0)