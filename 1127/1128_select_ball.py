# 특정색(본인선택)의 공의 개수를 출력하고, 이미지 찾아 표시
# HSV 색 분리 활용
import cv2

img = cv2.imread("balls.png")
# 이미지 사이즈 너무 커서 조절
resize_img = cv2.resize(img, (800,800))
# hsv로 변환
hsv_img = cv2.cvtColor(resize_img, cv2.COLOR_BGR2HSV)
# 파랑이의 색상은 120, 낮은 채도 어두운 명도
lower_blue = (100, 30, 60) # 파란색의 120에서 약간 낮춤. 이게 젤 깔끔
upper_blue = (140, 255, 255)
img_mask = cv2.inRange(hsv_img, lower_blue, upper_blue)

# 마스크 생성후 비트와이즈 연산
# mask_img = cv2.bitwise_and(resize_img, resize_img, mask = img_mask)
# ret, th = cv2.threshold(img_mask, 220, 255, cv2.THRESH_BINARY_INV)

# 어짜피 마스크 이미지는 이진화된것 같아서 그냥 넣었더니 되었다..
contours, hy = cv2.findContours(img_mask, cv2.RETR_EXTERNAL,
                                cv2.CHAIN_APPROX_NONE)

# 혹시 0일수도 있으니까
if len(contours) != 0:
    for cont in contours:
        x, y, w, h = cv2.boundingRect(cont)
        cv2.rectangle(resize_img, (x,y), (x+w, y+h), (0,255,0), 3) #좌표에 맞게 그림
    print( "파란공의 개수는 약",len(contours),"개")

cv2.imshow("image",resize_img)
cv2.imshow("image2",img_mask)

cv2.waitKey(0)