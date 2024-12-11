# 침식 - 배경에 있는 잡음 (흰색) 제거
# 그런데 글자 내부의 검정색 공간은 더 커짐
import cv2
import numpy as np

#이미지 읽기
img = cv2.imread("morph.jpg")

#data =[0,1,0,...] #책에서 직접 마스크 만듬
#opencv에서 제공하는 커널 생성 함수
k = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
#형태,커널크기,기준점(anchor)
#cv2.MORPH_RECT 사각형
#cv2.MORPH_ELLIPSE 타원형
#cv2.MORPH_CROSS 십자가형 - 기준점이 있을때만 사용
res_erode=cv2.erode(img,k)
#이미지/ 커널 /옵션 >> 앵커(마스크) /반복 횟수 / 외곽 보정 타입 / 외곽 보정 값


cv2.imshow("Erode",res_erode)
cv2.waitKey(0)