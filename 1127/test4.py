# 제일 큰 사각형 찾기
import cv2

img = cv2.imread("rect.png")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, th = cv2.threshold(imgray, 127, 255,
                        cv2.THRESH_BINARY_INV)
coutours, hr = cv2.findContours(th, cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_SIMPLE)

cont = sorted(coutours, key=cv2.contourArea, reverse=True)
print(len(cont))

x, y, w, h = cv2.boundingRect(cont[0])
cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),3)

cv2.imshow("default", img)
cv2.waitKey(0)