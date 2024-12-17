import cv2

img = cv2.imread("../1106/hsv.png")
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def hsvbar(value):
    lower = (value - 10, 30, 30)
    upper = (value + 10 ,255, 255)
    img_mask = cv2.inRange(img_hsv,lower, upper)
    result = cv2.bitwise_and(img, img, mask = img_mask)
    cv2.imshow(title,result)

title = "hsvTrackbar"
cv2.namedWindow(title)
cv2.createTrackbar("color_var",title,0,300,hsvbar)
cv2.imshow(title, img)
cv2.waitKey(0)