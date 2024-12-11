import numpy as np, cv2

image = cv2.imread("minMax.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

title = "ex12"

(H,W) = image.shape[:2]
x, y = W//2, H//2

#관심영역1
roi1 = image[0:y, 0:x]
roi1 = cv2.add(roi1, 50)
#처리한걸 다시 원본에 넣기, 이미지에 다시 할당
image[0:y, 0:x] = roi1

#관심영역2
roi2 = image[y:H, x:W]

min_val, max_val, _, _ = cv2.minMaxLoc(roi2)    #화소중 최댓값 최솟값 반환
ratio = 255 / (max_val - min_val)   #차를 이용해 비율을 계산함.
dst = np.round((roi2 - min_val) * ratio).astype('uint8')    #영상 내 최소값 0, 최대값 255로 만든다.
# min_dst, max_dst, _, _ = cv2.minMaxLoc(dst)

image[y:H, x:W]=dst #원본영상 다시 넣기

cv2.imshow(title,image)
cv2.waitKey()