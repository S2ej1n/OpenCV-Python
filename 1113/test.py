# 컬러에지 검출 추가해야됨
import numpy as np, cv2

image = cv2.imread("color_edge.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상 파일 읽기 오류")

def CannyBar(value):
    pass
def Median(value):
    pass
def Gaussian(value):
    pass

canny2 = cv2.Canny(image, 100, 150)

title = "test"
cv2.namedWindow(title)
cv2.createTrackbar('Canny th', title, 0 ,100, CannyBar)
cv2.createTrackbar('median', title, 0 ,1, Median)
cv2.createTrackbar('gaussian', title, 0 ,1, Gaussian)
cv2.imshow("g",canny2)

while True:
    if cv2.waitKey(30) >= 0: break
    c = cv2.getTrackbarPos('Canny th', title)
    m = cv2.getTrackbarPos('median', title)
    g = cv2.getTrackbarPos('gaussian', title)
    if m > 0:
        dst = cv2.medianBlur(image, 5)
        if g > 0:
            dst2 = cv2.GaussianBlur(dst, ksize=(7, 7), sigmaX=10.0)
        else:
            dst2 = dst
    else:
        dst = image
        if g > 0:
            dst2 = cv2.GaussianBlur(dst, ksize=(7, 7), sigmaX=10.0)
        else:
            dst2 = dst
    result = np.hstack((image, dst2))
    cv2.imshow(title, result)