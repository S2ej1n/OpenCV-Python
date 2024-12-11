import numpy as np, cv2

def salt_pepper_noise(img, n):
    h,w = img.shape[:2]
    x,y = np.random.randint(0, w, n), np.random.randint(0,h,n)
    noise = img.copy()
    for (x,y) in zip(x,y):
        noise[y,x] = 0 if np.random.rand()<0.5 else 255
    return noise

image = cv2.imread("Lenna.png", cv2.IMREAD_GRAYSCALE)
noise = salt_pepper_noise(image,500)
dst = cv2.medianBlur(noise, 7) #7은 ksize = 커널 크기 = mask의 크기 = window
#kseize를 올릴수록 더 좋아진다
dst2 = cv2.GaussianBlur(noise, ksize=(7,7), sigmaX=10.0)
#sigmaX에 0을 주면 점이 보인다.
dst3 = cv2.blur(noise, ksize=(7,7))

cv2.imshow("noise", noise)
cv2.imshow("dst", dst)
cv2.imshow("dst2", dst2)
cv2.imshow("dst3",dst3)
cv2.waitKey(0)