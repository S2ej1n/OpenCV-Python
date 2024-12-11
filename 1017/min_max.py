import numpy as np, cv2

image = cv2.imread("minMax.jpg", cv2.IMREAD_GRAYSCALE)
if image is None: raise Exception("영상파일 읽기 에러")

####명암조정!! 이라 생각하면됨
min_val, max_val, _, _ = cv2.minMaxLoc(image)
#화소중 최댓값 최솟값 반환

ratio = 255 / (max_val - min_val)
#차를 이용해 비율을 계산함.
dst = np.round((image - min_val) * ratio).astype('uint8')
#영상 내 최소값 0, 최대값 255로 만든다.
min_dst, max_dst, _, _ = cv2.minMaxLoc(dst)

print("원본 영상 최솟값 = %d, 최댓값=%d" % (min_val, max_val))
print("수정 영상 최솟값 = %d, 최댓값=%d" % (min_dst, max_dst))
cv2.imshow('image', image)
cv2.imshow('dst', dst)
cv2.waitKey(0)