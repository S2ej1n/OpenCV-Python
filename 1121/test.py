#1 - 마우스 클릭 좌표로 이미지 이동
#2 - 스크롤바로 이미지 회전
#3 - 스크롤바로 이미지 크기 변환
import numpy as np, cv2

image = cv2.imread("hams.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 에러")
resize_img = cv2.resize(image, (450,300))

def onMouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        rows, cols = resize_img.shape[0:2]
        dx, dy = x, y
        M = np.float32([[1,0,dx], [0,1,dy]])
        dst = cv2.warpAffine(resize_img, M, (cols + dx, rows +dy))
        cv2.imshow(title1, dst)

def Rotation(value2):
    h, w = resize_img.shape[:2]
    center = (w // 2, h // 2)
    rot_mat = cv2.getRotationMatrix2D(center,value2,1)
    dst2 = cv2.warpAffine(resize_img, rot_mat, (w,h), cv2.INTER_LINEAR)
    cv2.imshow(title2, dst2)

def Scale(value3):
    dst3 = cv2.resize(resize_img, None, fx=(value3)*0.1, fy=(value3)*0.1, interpolation=cv2.INTER_LINEAR)
    cv2.imshow(title3, dst3)

value2 = 0
value3 = 15
title1 = "translate"
title2 = "rotation"
title3 = "scale"

cv2.namedWindow(title1)
cv2.namedWindow(title2)
cv2.namedWindow(title3)

cv2.createTrackbar("Rotation", title2, value2, 360, Rotation)
cv2.createTrackbar("Scale", title3, value3,30, Scale)
cv2.setMouseCallback(title1, onMouse)

cv2.imshow(title1, resize_img)
cv2.imshow(title2, resize_img) #기본 이미지 출력 - 이거 없으면 까만화면에서 시작
cv2.imshow(title3, resize_img)
cv2.waitKey(0)