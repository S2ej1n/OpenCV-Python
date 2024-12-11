#외곽선찾기

import cv2
import numpy as np

img = cv2.imread("obj2.png")
img2 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, imthres = cv2.threshold(imgray, 150, 255,
                             cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(imthres, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_NONE)
print("contour count ex:",len(contours))

contours2, hierarchy2 = cv2.findContours(imthres, cv2.RETR_TREE,
                                       cv2.CHAIN_APPROX_SIMPLE)
print("contour count tr:",len(contours2))
print("hierarchy2")
print("n , pr, c, p")
print(hierarchy2)

img3 = cv2.cvtColor(imthres,cv2.COLOR_GRAY2BGR)
cv2.drawContours(img3,contours,-1,(0,255,0))
cv2.drawContours(imthres,contours,-1,(0,255,0))

for idx, cont in enumerate(contours2):
    color = [int(i) for i in np.random.randint(0,255,3)]
    cv2.drawContours(img2, contours2, idx, color, 3)
    cv2.putText(img2, str(idx), tuple(cont[0][0]),
                cv2.FONT_HERSHEY_PLAIN, 1, (0,0,255))

cv2.imshow("default",img)
cv2.imshow("default3",img3)
cv2.imshow("default2",img2)
cv2.imshow("imgray",imgray)
cv2.imshow("imthres",imthres)
cv2.waitKey(0)