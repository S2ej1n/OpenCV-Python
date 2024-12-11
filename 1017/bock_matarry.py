import cv2

image = cv2.imread("bit_test.jpg", cv2.IMREAD_COLOR)
if image is None: raise Exception("영상파일 읽기 오류")

x_axis = cv2.flip(image,0)
#x축 기준 상하 뒤집기
y_axis = cv2.flip(image,1)
#y축 기준 좌우 뒤집기
xy_axis = cv2.flip(image,-1)
#모두 뒤집기
rep_axis = cv2.repeat(image,1, 2)
#반복 -> 세로방향, 가로뱡향 2번
trans_axis = cv2.transpose(image)
#전치행렬

titles = ['image', 'x_axis', 'y_axis', 'xy_axis', 'rep_axis', 'trans_axis']
for title in titles:
    cv2.imshow(title, eval(title))
cv2.waitKey(0)