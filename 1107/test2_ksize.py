import numpy as np, cv2

def Trackbar(value):
    pass

title = "dst"
cv2.namedWindow(title)

cv2.createTrackbar("blurBar",title,1,20,Trackbar)
image = cv2.imread("Lenna.png", cv2.IMREAD_GRAYSCALE)

while True:
    if cv2.waitKey(30) ==27:
        break
    value = cv2.getTrackbarPos("blurBar",title)

    # kSize를 홀수로 변경 (0이면 기본 이미지)
    # ksize = value if value % 2 == 1 else value + 1
    if value % 2 == 1:  # value가 홀수인지 확인
        ksize = value  # 홀수이면 그대로 사용
    else:
        ksize = value + 1  # 짝수이면 +1을 해서 홀수로 변경

    if ksize <= 0:
        cv2.imshow(title,image)
    else:
        dst = cv2.GaussianBlur(image, ksize=(ksize, ksize), sigmaX=0)
        cv2.imshow(title,dst)

cv2.destroyAllWindows()
# cv2.waitKey(0)