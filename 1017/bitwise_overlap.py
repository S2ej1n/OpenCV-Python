import numpy as np, cv2

image = cv2.imread("bit_test.jpg", cv2.IMREAD_COLOR)
logo = cv2.imread("logo.jpg", cv2.IMREAD_COLOR)
if image is None or logo is None:
    raise Exception("영상파일 읽기 오류")

masks = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]
#로고 영상 이진화 cv2.THRESH_BINARY
# => 기준값(220)보다 작은 화소는0, 큰 화소는 255로 만듬
masks = cv2.split(masks) #단일채널3개 만듬

##정리 : 흰색만 통과하고 나머지 개무시.
fg_pass_mask = cv2.bitwise_or(masks[0], masks[1])
fg_pass_mask = cv2.bitwise_or(masks[2], fg_pass_mask)
#전경 마스크 => 전경이 포함된 부분은 255(흰), 나머지는 검정색.
#전경(로고모양)유지하고 나머지는 제거하도록 만드는 마스크
#로고만 통과시키고, 나머지(배경)는 제거하는 방식.
bg_pass_mask = cv2.bitwise_not(fg_pass_mask)
#행렬 반전함. => 배경 통과, 전경 제거.

(H, W), (h, w) = image.shape[:2], logo.shape[:2]
x, y = (W-w)//2, (H-h)//2
roi = image[y:y+h, x:x+w] #관심영역 지정, 로고가 들어갈 배경 이미지

#흰색인 부분에 합성이 됨.!!
foreground = cv2.bitwise_and(logo, logo, mask=fg_pass_mask)
#로고에서 필요한 부분만 추출 => 로고의 전경 부분만 추출함.
#두 값이 모두 1일때 결과가 1이 됨 => 즉 0인 부분(로고)은 제거됩니다.
background = cv2.bitwise_and(roi, roi, mask=bg_pass_mask)
#관심영역 부분의 배경만 복사(roi 영역에서 로고가 들어갈 부분의 배경만 추출)

dst = cv2.add(background, foreground)
image[y:y+h, x:x+w] = dst

cv2.imshow('background', background)
cv2.imshow('foreground', foreground)
cv2.imshow('dst',dst)
cv2.imshow('image',image)
cv2.waitKey()