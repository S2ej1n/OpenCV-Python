#이미지 히스토그램 (페이지 241)
import cv2
import numpy as np

def draw_histo(hist, shape=(200,256)):
    hist_img = np.full(shape, 255, np.uint8) # 흰색 배경 이미지 생성
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX) #정규화
    gap = hist_img.shape[1]/hist.shape[0]  # 막대의 너비 계산
    
    for i, h in enumerate(hist):  # 히스토그램 값 반복
        x = int(round(i * gap)) #막대 사각형 시작 x좌표
        w = int(round(gap)) # 막대의 너비
        cv2.rectangle(hist_img, (x, 0, w, int(h)), 0, cv2.FILLED) # 히스토그램 막대 그리기
    
    return cv2.flip(hist_img, 0) #영상 상하 뒤집기 후 반환

image = cv2.imread("color_model.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

hist = cv2.calcHist([image], [0], None, [32], [0,256])
hist_img = draw_histo(hist)
# 히스토그램 이미지: 밝기 값의 빈도를 나타내는 막대 그래프
cv2.imshow("image", image)
cv2.imshow("hist_img",hist_img)
cv2.waitKey(0)


# cv2.calcHist:
# 이미지의 히스토그램을 계산.
# 입력 매개변수:
# [image]: 입력 이미지.
# [0]: 채널 0(그레이스케일).
# None: 마스크 없음.
# [32]: 히스토그램의 빈(bin) 개수 (32개의 구간으로 나눔).
# [0,256]: 픽셀 값 범위 (0~255).
# 반환값: 32개의 빈에 각 픽셀 값이 속한 빈도의 배열.