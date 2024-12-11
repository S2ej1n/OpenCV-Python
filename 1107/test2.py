import numpy as np, cv2

def Trackbar(value):
    pass

title = "dst"
cv2.namedWindow(title)

cv2.createTrackbar("blurBar",title,0,10,Trackbar)
image = cv2.imread("Lenna.png", cv2.IMREAD_GRAYSCALE)

while True:
    if cv2.waitKey(30) ==27:
        break
    value = cv2.getTrackbarPos("blurBar",title)
    if value == 0:
        cv2.imshow(title,image)
    else:
        dst = cv2.GaussianBlur(image, ksize=(7, 7), sigmaX=value)
        cv2.imshow(title,dst)

cv2.destroyAllWindows()
# cv2.waitKey(0)