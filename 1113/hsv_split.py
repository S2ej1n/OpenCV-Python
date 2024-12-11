import cv2
import numpy as np

file_name = "HSV_cone.jpg" # 파일명

def lowHue(value):
    pass

def lowSaturation(value):
    pass

def lowValue(value):
    pass

def highHue(value):
    pass

def highSaturation(value):
    pass

def highValue(value):
    pass


# 이미지 크기 조절 - resize
image = cv2.imread(file_name)
h, w, c = image.shape
resize_size = 1.0
if w > 2000:
    resize_size = 0.3
elif w > 1000:
    resize_size = 0.5
image = cv2.resize(image, (0, 0), fx=resize_size, fy=resize_size, interpolation=cv2.INTER_NEAREST)

win_name = "hsv_image"

cv2.namedWindow(win_name)
cv2.createTrackbar('low_H', win_name, 110, 255, lowHue)
cv2.createTrackbar('low_S', win_name, 30, 255, lowSaturation)
cv2.createTrackbar('low_V', win_name, 30, 255, lowValue)
cv2.createTrackbar('high_H', win_name, 130, 255, highHue)
cv2.createTrackbar('high_S', win_name, 255, 255, highSaturation)
cv2.createTrackbar('high_V', win_name, 255, 255, highValue)

img_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

while True:
    txtImage = image.copy()

    low_h = cv2.getTrackbarPos('low_H', win_name)
    high_h = cv2.getTrackbarPos('high_H', win_name)
    low_s = cv2.getTrackbarPos('low_S', win_name)
    high_s = cv2.getTrackbarPos('high_S', win_name)
    low_v = cv2.getTrackbarPos('low_V', win_name)
    high_v = cv2.getTrackbarPos('high_V', win_name)

    low_color = (low_h, low_s, low_v)
    upper_color = (high_h, high_s, high_v)
    img_mask = cv2.inRange(img_hsv, low_color, upper_color)  # 범위내의 픽셀들은 흰색, 나머지 검은색
    img_result = cv2.bitwise_and(txtImage, txtImage, mask=img_mask)

    txt = f"low_hsv({low_h}, {low_s}, {low_v}) / high_hsv({high_h}, {high_s}, {high_v})"
    t_h, t_w, t_c = txtImage.shape
    cv2.putText(img_result, txt, (20, t_h - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 1, cv2.LINE_AA)

    result = np.hstack((image, img_result))
    cv2.imshow(win_name, result)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
            break