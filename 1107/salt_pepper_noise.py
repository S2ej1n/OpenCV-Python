import numpy as np, cv2

def salt_pepper_noise(img, n):
    h,w = img.shape[:2] # 이미지 높이와 너비 가져오기
    x,y = np.random.randint(0, w, n), np.random.randint(0,h,n)
    # 높이와 너비 사이의 랜덤 값 만듬
    noise = img.copy() # 노이즈 추가할 이미지 생성

    # x = [10, 20, 30]
    # y = [1, 2, 3]
    # list(zip(x, y))  # 결과: [(10, 1), (20, 2), (30, 3)]
    for (x,y) in zip(x,y): #생성된 랜덤 좌표를 순회하며, 해당 좌표의 픽셀 값을 변경.
        noise[y,x] = 0 if np.random.rand() < 0.5 else 255
        # 0.5보다 작으면 해당 좌표 픽셀 값(noise[y, x])을 검정(0)으로 설정.
        # 0.5보다 크면 해당 좌표 픽셀 값을 흰색(255)으로 설정.
    return noise

image = cv2.imread("Lenna.png", cv2.IMREAD_GRAYSCALE)

noise = salt_pepper_noise(image,500)

dst = cv2.medianBlur(noise, 7) #7은 ksize = 커널 크기 = mask의 크기 = window
#kseize를 올릴수록 더 좋아진다
dst2 = cv2.GaussianBlur(noise, ksize=(7,7), sigmaX=10.0)
#sigmaX에 0을 주면 점이 보인다.
dst3 = cv2.blur(noise, ksize=(7,7))

cv2.imshow("noise", noise)
cv2.imshow("medianBlur", dst)
cv2.imshow("GaussianBlur", dst2)
cv2.imshow("blur",dst3)
cv2.waitKey(0)