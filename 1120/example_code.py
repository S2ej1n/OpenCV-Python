import numpy as np, cv2

img = cv2.imread('ham.jpeg')
h, w, c = img.shape

#cv2.INTER_AREA: 축소에 적합한 보간법
shrink = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

#cv2.INTER_CUBIC: 3차 보간법. 고화질
zoom1 = cv2.resize(img, (w*2, h*2), interpolation=cv2.INTER_CUBIC)

# 배수 Size지정
zoom2 = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

cv2.imshow('Origianl', img)
cv2.imshow('Shrink', shrink)
cv2.imshow('Zoom1', zoom1)
cv2.imshow('Zoom2', zoom2)

cv2.waitKey(0)
cv2.destroyAllWindows()