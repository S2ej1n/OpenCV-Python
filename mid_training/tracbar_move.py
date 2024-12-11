import numpy as np
import cv2

def onChange(value):
    global image, title
    image[:] = (255, 255, 255)  # 색상을 흰색으로 초기화를 위한 작업
    cv2.rectangle(image, (0, 0), (value, value), blue, 3, cv2.LINE_4)
    cv2.imshow(title, image)

image = np.zeros((300, 500, 3), np.uint8)

blue, green, red = (255, 0, 0), (0, 255, 0), (0, 0, 255)
image[:] = (255, 255, 255)
cv2.rectangle(image, (0, 0), (1, 1), blue, 3, cv2.LINE_4)
title = "Trackbar Event"
cv2.imshow(title, image)

cv2.createTrackbar("Size", title, 0, 300, onChange)

while True:
    key = cv2.waitKey(30)  # 30ms 대기하여 키 입력을 확인
    if key == 27:  # ESC 키를 누르면 종료
        break
    elif key == ord('a'):  # 왼쪽 화살표 키
        current_value = cv2.getTrackbarPos("Size", title)
        print(current_value)
        new_value = max(0, current_value - 1)  # 값 감소
        cv2.setTrackbarPos("Size", title, new_value)
        onChange(new_value)
    elif key == ord('d'):  # 오른쪽 화살표 키
        current_value = cv2.getTrackbarPos("Size", title)
        new_value = min(300, current_value + 1)  # 값 증가
        cv2.setTrackbarPos("Size", title, new_value)
        onChange(new_value)

cv2.destroyAllWindows()
