#트랙바를 이용하여 이미지의 밝기 조절
import numpy as np, cv2

image = cv2.imread("minMax.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 오류")

def light_bar(value):
    n_image = cv2.add(image, value)
    # n_image = np.clip(image + value, 0, 255).astype('uint8')
    cv2.imshow(title, n_image)

title = "Change light"
cv2.namedWindow(title)
cv2.createTrackbar('light', title, 0 ,100, light_bar)

cv2.imshow(title, image)
cv2.waitKey(0)