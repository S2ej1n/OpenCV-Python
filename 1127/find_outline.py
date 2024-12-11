import cv2
from PIL.ImageChops import offset

#contour = 등치선
#cv2.findContours()
#src, mode, method, contours(optional),hierarchy(optional), offset
#src는 바이너리 이미지 - 이진화 이미지

# 그레이 스케일로 불러오기 - 윤곽선 탐지 더 쉽게 하기 위해
img = cv2.imread("obj.png")
gry_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#img = cv2.imread("obj.png", cv2.IMREAD_GRAYSCALE)

# 이진화
# 220 픽셀값 임계점 - 이 값을 기준으로 픽셀을 분류함
# 225 - 픽셀값이 임계점을 넘었을 때 설정할 값 (흰색)
# cv2.THRESH_BINARY_INV: 이진화의 반전 모드.
# 임계값 이하의 픽셀은 흰색(255), 초과하면 검은색(0)으로 설정.
ret, imthres = cv2.threshold(gry_img, 220, 255,
                             cv2.THRESH_BINARY)#THRESH_BINARY_INV

#색상반전
imthres = ~imthres

#외곽선 찾기 (윤곽선 탐지)
coutours, heirarchy = cv2.findContours(imthres,cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_NONE)
#imthres: 윤곽선을 탐지할 대상 이미지.
#cv2.RETR_EXTERNAL: 가장 바깥쪽 윤곽선만 탐지.
#cv2.CHAIN_APPROX_NONE: 윤곽선을 구성하는 모든 점을 저장 (압축 없음).
# 출력값---
# contours: 윤곽선 정보의 리스트. 각 윤곽선은 점들의 배열로 표현.
# hierarchy: 계층 구조 정보. 윤곽선 간의 부모-자식 관계를 나타냄.

#외곽선 찾기
coutours2, heirarchy2 = cv2.findContours(imthres,cv2.RETR_EXTERNAL,
                                       cv2.CHAIN_APPROX_SIMPLE)
#mode: RETR_EXTERNAL-가장 바깥쪽만, RETR_LIST-모든라인,
# RET_COMP-모든라인을 2계층으로

#method: CHAIN_APPROX_NONE-모든 좌표, CHAIN_APPROX_SIMPLE-꼭짓점만

#cv2.drawContours(src, contours, contourIdx, color, thickness)
#contours:찾은 배열- findContours에서 찾은 값
img2 = img.copy()
cv2.drawContours(img,coutours,-1,(255,255,0), 4)
cv2.drawContours(img2,coutours2,-1,(255,255,0), 4)

for i in coutours2:
    for j in i:
        cv2.circle(img2,tuple(j[0]), 1,(0,0,255), -1)


cv2.imshow("default",img)
cv2.imshow("default2",img2)
cv2.imshow("gry_img",gry_img)
cv2.imshow("imthres",imthres)

cv2.waitKey(0)