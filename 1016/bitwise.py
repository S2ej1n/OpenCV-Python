#numpy의 ndarray는 하나의 타입만 받을 수 있음. < 행렬처리시 이거 사용
#비트연산
import numpy as np, cv2

image1 = np.zeros((300,300), np.uint8)  #까만 네모칸
image2 = image1.copy()

h, w = image1.shape[:2]
cx, cy = w//2, h//2 #중심좌표
cv2.circle(image1, (cx, cy), 100, 255, -1)  #중심에 원 그리기
cv2.rectangle(image2, (0, 0, cx, h), 255, -1)   #영상의 가로 절반

image3 = cv2.bitwise_or(image1, image2)
#논리합 => 한쪽이라도 흰색이면 반환행렬도 흰색
image4 = cv2.bitwise_and(image1, image2)
#논리곱 => 두 행렬 모두가 흰색인곳이 흰색
image5 = cv2.bitwise_xor(image1, image2)
#원소간 배타적 논리합 => 다른게 1이고 같으면 0임 -> 같으면 검정, 다르면 하양
image6 = cv2.bitwise_not(image1)
#행렬 반전 => 반전된 영상

cv2.imshow("image1", image1)
cv2.imshow("image2", image2)
cv2.imshow("bitwise_or", image3)
cv2.imshow("bitwise_and", image4)
cv2.imshow("bitwise_xor", image5)
cv2.imshow("bitwise_not", image6)
cv2.waitKey(0)