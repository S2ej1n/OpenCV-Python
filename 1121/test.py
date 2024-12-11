#1 - 마우스 클릭 좌표로 이미지 이동
#2 - 스크롤바로 이미지 회전
#3 - 스크롤바로 이미지 크기 변환
import numpy as np, cv2

image = cv2.imread("ham.jpeg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 에러")



cv2.imshow("image", image)
cv2.waitKey(0)