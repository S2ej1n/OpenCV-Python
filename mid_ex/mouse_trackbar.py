#마우스 클릭 + 트랙바 이벤트
import numpy as np, cv2

def onChange(value):
    global image, title

    #트랙바 값과 영상 화소값 차분
    add_value = value - int(image[0][0])
    print('추가 화소값: ', add_value)
    image[:] = image + add_value
    cv2.imshow(title, image)

def onMouse(event, x, y, flags, param):
    global image, bar_name

    if event == cv2.EVENT_RBUTTONDOWN:  #마우스 우버튼
        if (image[0][0] < 246):
            image = image + 10
        #슬라이더바 위치 설정
        cv2.setTrackbarPos(bar_name, title, image[0][0])
        cv2.imshow(title, image)
    elif event == cv2.EVENT_LBUTTONDOWN:
        if (image[0][0] >= 10):
            image = image - 10
        cv2.setTrackbarPos(bar_name, title, image[0][0])
        #->마지막 인자가 위치임
        cv2.imshow(title, image)

image = np.zeros((300,500), np.uint8)

title = "Trackbar event"
bar_name = 'Brightness'
cv2.imshow(title, image)

cv2.createTrackbar(bar_name, title, image[0][0], 255, onChange)

#마우스 이벤트에 이거 반드시 넣을것.
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()
