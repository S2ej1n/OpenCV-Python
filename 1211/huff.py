# 책과 다르게 원래 있던 함수를 활용해 따로 작성한거임.
# 허프변환

import numpy as np, cv2

image = cv2.imread('hough.jpg')
if image is None:
    raise Exception("영상 파일 읽기 에러")



cv2.imshow("image", image)
cv2.waitKey(0)