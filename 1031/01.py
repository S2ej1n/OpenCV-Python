#이미지 히스토그램
import cv2
import numpy as np

def draw_histo(hist, shape=(200,256)):
    hist_img = np.full(shape, 255, np.uint8)
    cv2.normalize(hist, hist, 0, shape[0], cv2.NORM_MINMAX) #정규화
    gap = hist_img.shape[1]/hist.shape[0]
    
    for i, h in enumerate(hist):
        x = int(round(i * gap)) #막대 사각형 시작 x좌표
        w = int(round(gap))
        cv2.rectangle(hist_img, (x, 0, w, int(h)), 0, cv2.FILLED)
    
    return cv2.flip(hist_img, 0) #영상 상하 뒤집기 후 반환

image = cv2.imread("../1017/minMax.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상 파일 읽기 오류")

hist = cv2.calcHist([image], [0], None, [32], [0,256])
hist_img = draw_histo(hist)

cv2.imshow("image", image)
cv2.imshow("hist_img",hist_img)
cv2.waitKey(0)