#연습문제 7번

import numpy as np, cv2

logo = cv2.imread("logo.jpg", cv2.IMREAD_COLOR)
if logo is None: raise Exception("영상파일 읽기 오류")

#logo는 컬러 이미지므로, 3차원 배열
blue, green, red = cv2.split(logo) #단일 채널 이미지, 2차원 배열

# frame1 = np.zeros(blue.shape, np.uint8) #이것도 되고
frame1 = np.zeros((logo.shape[0], logo.shape[1]), np.uint8)
#이것도 됨

blue_image = cv2.merge([blue, frame1, frame1])
green_image = cv2.merge([frame1, green, frame1])
red_image = cv2.merge([frame1, frame1, red])

cv2.imshow("logo",logo)
cv2.imshow("blue_img",blue_image)
cv2.imshow("green",green_image)
cv2.imshow("red",red_image)

# cv2.imwrite("test_img.jpg",blue_image)
# print("저장완")
cv2.waitKey()