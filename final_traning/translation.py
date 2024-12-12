# 책 예제 추가 - 영상 평행이동
import numpy as np, cv2

def contain(p, shape):
    return 0 <= p[0] < shape[0] and 0 <= p[1] < shape[1]

def translate(img, pt):
    dst = np.zeros(img.shape, img.dtype)  # 원본과 동일한 크기의 빈 이미지 생성
    for i in range(img.shape[0]):        # 이미지의 행(높이) 순회
        for j in range(img.shape[1]):    # 이미지의 열(너비) 순회
            x, y = np.substract((j,i), pt)  # 현재 좌표에서 이동량(pt)을 뺀 새로운 좌표 계산
            if contain((y, x), img.shape):  # 새로운 좌표가 유효한지 확인
                dst[i,j] = img[y,x]         # 유효하다면 값을 복사
    return dst

image = cv2.imread('translate.jpg', cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

dst1 = translate(image, (30,80))
dst2 = translate(image, (-70, -50))

cv2.imshow("image", image)
cv2.imshow("dst1: transted to (30,80)", dst1);
cv2.imshow("dst2: transted to (-70,-50)", dst2);
cv2.waitKey(0)