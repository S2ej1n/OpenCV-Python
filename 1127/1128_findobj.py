# 찾을 도형을 선택하세요
# 결과의 좌표값을 활용
import cv2

def input_fun() :
    print("찾을 도형을 선택하세요 \n "
          "1) 삼각형 \n "
          "2) 사각형 \n "
          "3) 원")
    val = input(": ")
    return val

val = input_fun()

# 102는 삼각형, 236은 원, 343은 네모
mydohyong = 0
if val == "1":
    mydohyong = 102  # 삼각형
elif val == "2":
    mydohyong = 343  # 사각형
elif val == "3":
    mydohyong = 236  # 원
else:
    print("도형중에서 골라주세요.")

img = cv2.imread("obj.png")
img2 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, imthres = cv2.threshold(imgray, 220, 255,
                             cv2.THRESH_BINARY_INV)

# 꼭짓점만 - 검출된 외곽선 좌표 CONTOURS
contours, hierarchy = cv2.findContours(imthres, cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)

for j in contours:
    # 아예 한 점만 나오게 근사화 시켰다.
    epsilon = 0.5 * cv2.arcLength(j, True)
    approx = cv2.approxPolyDP(j, epsilon, True)

    # 꼭짓점 그리기
    for point in approx:
        x, y = point[0]
        cv2.circle(img, (x, y), 5, (0, 0, 255), -1)

        # 뭔가 여기서 찾은 좌표값에 딱 맞는게 있으면 될것같았다.
        if x == mydohyong:
            cv2.drawContours(img2, [j], -1, (255, 255, 0), 4)
        #102는 삼각형, 236은 원, 343은 네모 -> 그게 포함되면 그려버리기
            break

# cv2.drawContours(img2,contours,-1,(255,255,0), 4)
# print(contours)

cv2.imshow("obj",img)
cv2.imshow("result",img2)
cv2.waitKey(0)