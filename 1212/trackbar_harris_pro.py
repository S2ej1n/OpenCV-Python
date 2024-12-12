# 교수님 코드
import cv2


def onTrack(value):
    k = 0.3 - (value * 0.01)  # 현재 이미지에서 k값이 0.3이면 코너가 검출되지 않음. 값을 내릴수록 코너 검출이 늘어남

    img = cv2.imread(filename)  # 트랙바의 값에 따라서 매번 초기화 시키면서 값을 적용해야 함으로 이미지 다시 읽음

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    dst = cv2.cornerHarris(gray, 2, 3, k)

    img[dst > 0.01 * dst.max()] = [0, 0, 255]

    cv2.imshow(title, img)


title = 'dst'

cv2.namedWindow(title)

cv2.createTrackbar('threshold', title, 0, 100, onTrack)

filename = 'harris.jpg'

img = cv2.imread(filename)

cv2.imshow(title, img)

cv2.waitKey(0)

cv2.destroyAllWindows()