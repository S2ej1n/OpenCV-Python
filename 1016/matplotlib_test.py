#MATPLOTLIB 라이브러리

import cv2
import matplotlib.pyplot as plt

image = cv2.imread("matplot.jpg", cv2.IMREAD_COLOR) #img는 BGR컬러
if image is None: raise Exception("영상파일 읽기 에러")

rows, cols = image.shape[:2]    #영상 크기 정보
rgb_img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)    #컬러 공간 변환
gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  #명암도 영상 변환

fig = plt.figure(num=1, figsize=(3,4))  #그림생성
plt.imshow(image)   #그림 표시 => image는 BGR인데 figure객체는 RGB로 표시해서 보색으로 모니터에 보여짐.
plt.title("figure1- original(bgr)") #그림 제목
plt.axis('off')     #축없음
plt.tight_layout()  #여백 없음

fig = plt.figure(figsize=(6,4))     #그림 생성
plt.suptitle("figure2- pyplot image display")   #전체 제목 지정
plt.subplot(1,2,1,), plt.imshow(rgb_img)
#서브 플롯 그림 행,열, 순번 지정.(1행 2열의 서브 플롯중 첫번쨰 플롯에)
plt.axis([0,cols,rows,0]), plt.title('rgb color')
#축 범위(x축 : 0~너비, y축: 높이~0), 서브 플롯 제목
plt.subplot(1,2,2), plt.imshow(gray_img, cmap='gray')
#서브플롯 그림, 명암도로 표시
plt.title('gray_img2')
plt.show()      #전체 그림 띄우기